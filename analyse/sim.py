import re, json, random, collections as C, sys
import numpy as np
import os
HERE=os.path.dirname(os.path.abspath(__file__))
DATA=os.path.join(HERE,'data')
SITE=os.path.join(HERE,'..','index.html')
pct=json.load(open(os.path.join(HERE,'resultaten','gangbaarheid.json')))
T=lambda w: tuple(re.findall('IJ|[A-Z]', w.upper()))
words=sorted(pct); lex=[T(w) for w in words]; N=len(lex)
s=open(SITE).read()
real=[T(w) for w,f in json.loads(re.search(r'id="wordsData">(.*?)</script>',s,re.S).group(1))['w12'] if f]
real=[w for w in real if len(w)==12]
AL=[chr(c) for c in range(65,91)]+['IJ']; ID={a:i for i,a in enumerate(AL)}; K=len(AL)
L=np.array([[ID[c] for c in w] for w in lex],dtype=np.int16); IDX={w:i for i,w in enumerate(lex)}
PCT=np.array([pct[w] for w in words]); rowbase=(np.arange(N)*K)[:,None]
VOW={'A','E','I','O','U','IJ'}; RARE=set('VZJWFBKPD'); COMMON=list('EANRTOISLDGKMUBVPHWCZF')
args=dict(a.split('=') for a in sys.argv[3:])
MODE=args.get('herkenning','gangbaar'); BASE=float(args.get('start','0.5')); SPREAD=float(args.get('spreiding','0.5')); INC=float(args.get('erbij','0.05'))
P0 = np.full(N,BASE); READ=int(args.get('lezen','9')); AHA=float(args.get('aha','0'))
EDGE=float(args.get('rand','1')); EDGEPOS=[0,1,10,11]
SAL=np.array([EDGE if j in EDGEPOS else 1.0 for j in range(12)]); SAL=SAL/SAL.mean()
FLOOR=float(args.get('basis','0')); KNOW = FLOOR+(1-FLOOR)*PCT if MODE=='gangbaar' else np.ones(N)   # kans dat een woord in je woordenschat zit

def draw(r):
    w=[31,26,12,10,6,2]; x=r.random()*87
    for i,v in enumerate(w):
        x-=v
        if x<0: return i
    return 0

def deal(target,r):
    """Zelfde model als 'zoals in de uitzendingen' op de site."""
    F=draw(r); Cc=min(draw(r),12-F); Lm=1 if F>0 and r.random()<1/114 else 0
    q=list(range(12)); r.shuffle(q)
    tiles=[]
    for k,p in enumerate(q):
        t=target[p]
        if k<Lm: tiles.append(dict(pos=p,true=t,shown=None,unsure=False))
        elif k<F: tiles.append(dict(pos=p,true=t,shown=r.choice([c for c in COMMON if c!=t]),unsure=True))
        elif k<F+Cc: tiles.append(dict(pos=p,true=t,shown=t,unsure=True))
        else: tiles.append(dict(pos=p,true=t,shown=t,unsure=False))
    return tiles,F

def alive(U,p,tiles,placed,boost=0.0):
    vis=U<np.minimum(1.0,p[:,None]*SAL[None,:]+boost)
    have=np.zeros(K); jokers=0
    for t in tiles:
        if t['shown'] and not t.get('wrong'): have[ID[t['shown']]]+=1
        # joker: leeg vakje, streepje, of een onzekere letter die nog niet gekocht is (kan iets anders zijn)
        if (not t['shown']) or t.get('wrong') or (t['unsure'] and not t.get('bought')): jokers+=1
    cnt=np.bincount((rowbase+L).ravel(),weights=vis.ravel(),minlength=N*K).reshape(N,K)
    ok=np.maximum(cnt-have[None,:],0).sum(1)<=jokers
    for pos,l in placed.items(): ok&=(~vis[:,pos])|(L[:,pos]==l)
    return ok

def choose(tiles,strat,r,ev=None):
    free=[t for t in tiles if not t.get('bought')]
    if not free: return None
    if strat=='willekeurig': return r.choice(free)
    if strat=='achteraf beste': return min(free,key=ev)
    cnt=C.Counter(t['shown'] for t in free if t['shown'])
    uns=[t for t in free if t['unsure'] or not t['shown']]
    sure=[t for t in free if not(t['unsure'] or not t['shown'])]
    groups=[[t for t in sure if cnt[t['shown']]==1 and t['shown'] in RARE],
            [t for t in sure if cnt[t['shown']]==1 and t['shown'] not in VOW],
            [t for t in sure if cnt[t['shown']]==1 and t['shown']!='E'],
            [t for t in sure if t['shown']!='E'], sure]
    if strat=='rand':
        EDGEL=set('SBPVGLRK')
        e=[t for t in sure if cnt[t['shown']]==1 and t['shown'] in EDGEL]
        order=[uns, e]+groups
        for g in order:
            if g: return r.choice(g)
    if strat=='hybride':   # weinig twijfel: eerst de onzekere; veel twijfel: eerst medeklinkers
        nun=sum(1 for t in tiles if (t['unsure'] or not t['shown']))
        order=[uns]+groups if nun<=2 else groups+[uns]
    elif strat=='hybride2':  # hoogstens 2 onzekere eerst, dan medeklinkers, dan de rest
        nb=sum(1 for t in tiles if t.get('bought') and (t['unsure'] or not t['shown']))
        order=([uns] if nb<2 else [])+groups+[uns]
    else: order=[uns]+groups if strat=='schema' else groups+[uns]
    for g in order:
        if g: return r.choice(g)

RR=json.loads(re.search(r'id="roundsData">(.*?)</script>',open(SITE).read(),re.S).group(1))
def deal_real(rd,r):
    tiles=[]; F=sum(rd['f'])
    for q in range(12):
        sh=rd['b'][q]; sh=None if sh in ('-','') else sh
        tiles.append(dict(pos=rd['p'][q],true=rd['c'][q],shown=sh,unsure=bool(rd['f'][q]) and sh is not None))
    Cc=min(draw(r),12-F); good=[t for t in tiles if not t['unsure'] and t['shown']]; r.shuffle(good)
    for t in good[:Cc]: t['unsure']=True
    return tiles,F
def play(target,strat,r,nr,rd=None):
    tiles,F=deal_real(rd,r) if rd else deal(target,r); U=nr.random((N,12)); ti=IDX[target]
    known=nr.random(N)<KNOW; tknown=bool(known[ti]); known[ti]=False   # doelwoord apart
    placed={}; k=0; wrong=0; excl=~known; gain=0.0
    while True:
        p=np.full(N,P0)
        af=alive(U,p,tiles,placed,gain); a=af&~excl; n=int(a.sum())
        if all(t.get('bought') for t in tiles): return k,wrong,F,tknown
        tgt=tknown and bool(af[ti])
        if tgt: n+=1
        if not tknown and len(placed)>=READ: return k,wrong,F,tknown   # genoeg letters op hun plek: je leest het woord
        if n==1:
            if tgt: return k,wrong,F,tknown
            wrong+=1; excl|=a; continue
        ev=None
        if strat=='achteraf beste':
            def ev(t):
                pl=dict(placed); tt=[dict(x) for x in tiles]
                if t['shown']==t['true']: pl[t['pos']]=ID[t['true']]
                else:
                    for x in tt:
                        if x['pos']==t['pos']: x['wrong']=True
                a2=alive(U,np.full(N,P0),tt,pl,gain+INC)&~excl
                return a2.sum()
        t=choose(tiles,strat,r,ev); t['bought']=True; k+=1
        gain+=INC*(EDGE if t['pos'] in EDGEPOS else 1.0)/(1+(EDGE-1)*len(EDGEPOS)/12)
        if not tknown and r.random()<AHA: tknown=True   # het kwartje valt
        if t['shown']==t['true']: placed[t['pos']]=ID[t['true']]
        else: t['wrong']=True    # streepje: foute letter valt weg

which=sys.argv[1]; reps=int(sys.argv[2]); strat=args.get('strategie','schema')
r=random.Random(3); nr=np.random.default_rng(3)
if which=='uitzending':
    jobs=[(T(rd['w']),rd) for rd in RR for _ in range(reps)]
    jobs=[(t,rd) for t,rd in jobs if len(t)==12 and t in IDX]
    out=[play(t,strat,r,nr,rd) for t,rd in jobs]
    per=C.defaultdict(list)
    for (t,rd),o in zip(jobs,out): per[rd['id']+rd['w']].append(o[0])
    realk={rd['id']+rd['w']:rd['k'] for rd in RR}
    xs=[sum(v)/len(v) for k,v in per.items()]; ys=[realk[k] for k in per]
    mx,my=sum(xs)/len(xs),sum(ys)/len(ys)
    cor=sum((a-mx)*(b-my) for a,b in zip(xs,ys))/(sum((a-mx)**2 for a in xs)*sum((b-my)**2 for b in ys))**.5
    print('correlatie per ronde met echt:',round(cor,2),'| echt gem',round(my,2))
else:
    targets = real*reps if which=='echt' else random.Random(11).sample([w for w in lex if w not in set(real)],reps)
    out=[play(t,strat,r,nr) for t in targets]
b=[o[0] for o in out]; n=len(b)
byF=C.defaultdict(list); unk=[o for o in out if not o[3]]
for o in out: byF[min(o[2],3)].append(o[0])
print(json.dumps(dict(woorden=which,strategie=strat,herkenning=MODE,start=BASE,n=n,gem=round(sum(b)/n,2),mediaan=sorted(b)[n//2],
  verdeling={k:round(100*v/n) for k,v in sorted(C.Counter(min(x,9) for x in b).items())},
  fout_geraden=round(sum(o[1] for o in out)/n,2), doel_onbekend=round(100*len(unk)/n), gem_als_bekend=round(sum(o[0] for o in out if o[3])/max(1,n-len(unk)),2), gem_als_onbekend=round(sum(o[0] for o in unk)/max(1,len(unk)),2),
  per_aantal_fout={k:round(sum(v)/len(v),2) for k,v in sorted(byF.items())}),ensure_ascii=False))

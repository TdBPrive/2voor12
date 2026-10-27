import sys,json,glob,os
P=dict(a.split('=') for a in sys.argv[1:])
sys.argv=['x','echt','1']+[f'{k}={v}' for k,v in P.items()]
HERE=__import__('os').path.dirname(__import__('os').path.abspath(__file__))
TEST=P.pop('test','a'); SPELER=P.pop('speler','speler1')
exec(open(__import__('os').path.join(HERE,'sim.py')).read().replace('__file__',repr(__import__('os').path.join(HERE,'sim.py'))).split("which=sys.argv[1]")[0])
items=json.load(open(os.path.join(HERE,'resultaten',f'anagramtest_{TEST}_opgaven.json')))
res=json.load(open(os.path.join(HERE,'resultaten',f'anagramtest_{TEST}_{SPELER}.json')))
nr=np.random.default_rng(5); r=random.Random(5); REPS=int(P.get('reps','40'))
out={}
for it in items:
    t=T(it['w']); ti=IDX.get(t)
    if ti is None: print('mist',it['w']); continue
    tiles=[dict(pos=i,true=c,shown=c,unsure=False) for i,c in enumerate(t)]
    placed={q:ID[t[q]] for q in it['pos']}
    gain=sum(INC*(EDGE if q in EDGEPOS else 1.0)/(1+(EDGE-1)*len(EDGEPOS)/12) for q in it['pos'])
    ok=0
    for _ in range(REPS):
        U=nr.random((N,12)); known=nr.random(N)<KNOW; tk=bool(known[ti]) or any(r.random()<AHA for _ in it['pos']); known[ti]=False
        af=alive(U,np.full(N,P0),tiles,placed,gain); n=int((af&known).sum())+ (1 if tk and af[ti] else 0)
        ok+= (n==1 and tk and bool(af[ti]))
    out[it['w']]=ok/REPS
by={}
for it in items: by.setdefault(it['k'],[]).append(out[it['w']])
real={}
for it in items: real.setdefault(it['k'],[]).append(1 if res[it['w']]['solved'] else 0)
print(' '.join(f"k={k}: model {sum(v)/len(v):.0%} speler {sum(real[k])/len(real[k]):.0%} |" for k,v in sorted(by.items())))

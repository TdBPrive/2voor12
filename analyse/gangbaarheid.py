import re, json, math, statistics as st
import os
HERE=os.path.dirname(os.path.abspath(__file__))
DATA=os.path.join(HERE,'data')
SITE=os.path.join(HERE,'..','index.html')
F={}
for line in open(os.path.join(DATA,'nl_full.txt'),encoding='utf-8'):
    w,c=line.rsplit(' ',1); F[w]=int(c)
T=lambda w: re.findall('ij|[a-z]', w)
lex=[x for x in open(os.path.join(DATA,'opentaal','elements','basiswoorden-gekeurd.txt'),encoding='utf-8').read().split('\n') if re.fullmatch('[a-z]+',x) and len(T(x))==12]
s=open(SITE).read()
real=[w.lower() for w,f in json.loads(re.search(r'id="wordsData">(.*?)</script>',s,re.S).group(1))['w12'] if f]
real=[w for w in real if len(T(w))==12]
lex=sorted(set(lex)|set(real))
def split(w):
    best=(0,None)
    for i in range(3,len(w)-2):
        a,b=w[:i],w[i:]
        for aa in {a, a[:-1] if a.endswith('s') else a, a[:-2] if a.endswith('en') else a}:
            fa,fb=F.get(aa,0),F.get(b,0)
            if len(aa)>=2 and min(fa,fb)>best[0]: best=(min(fa,fb),(aa,b))
    return best
rows={}
for w in lex: rows[w]=(F.get(w,0),)+split(w)
both=[r[0]/r[1] for r in rows.values() if r[0]>0 and r[1]>0]
k=st.median(both); print('woorden met eigen frequentie',sum(r[0]>0 for r in rows.values()),'van',len(lex),'mediane verhouding heel/delen',k)
score={w:math.log10(1+max(r[0], k*r[1])) for w,r in rows.items()}
order=sorted(lex,key=lambda w:score[w]); pct={w:i/(len(order)-1) for i,w in enumerate(order)}
json.dump(pct,open(os.path.join(HERE,'resultaten','gangbaarheid.json'),'w'))
rp=sorted(pct[w] for w in real); print('echte woorden percentiel: mediaan',round(rp[len(rp)//2],2),'p10',round(rp[len(rp)//10],2),'p90',round(rp[int(len(rp)*.9)],2))
for w in ['sportkantine','strandjutter','schoenendoos','zweetdruppel','receptionist','salariskloof','godsgeschenk','incheckbalie']: print(w, rows[w][0], rows[w][2], round(pct[w],2))
print('minst gangbaar:',order[:8]); print('meest gangbaar:',order[-12:])
print('voorbeelden rond 50%:',order[len(order)//2-4:len(order)//2+4])

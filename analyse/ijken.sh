run(){ python3 sim.py uitzending 3 strategie=schema "$@" | python3 -c "
import sys,json
c=''
for l in sys.stdin:
  if l.startswith('{'):
    d=json.loads(l); v={int(k):x for k,x in d['verdeling'].items()}
    b=lambda a,z: sum(x for k,x in v.items() if a<=k<=z)
    print('$*'.ljust(32),'gem',d['gem'],'| 0-2',b(0,2),'3-4',b(3,4),'5-7',b(5,7),'8+',b(8,99),'| per fout',list(d['per_aantal_fout'].values()),'| r',c)
  else: c=l.strip().split(':')[1].split('|')[0].strip()
"; }

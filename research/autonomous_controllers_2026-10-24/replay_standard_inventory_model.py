#!/usr/bin/env python3
"""Materialize the SAT clock model and certify its whole finite-seed future."""
import json,re,sys
from collections import defaultdict
from pathlib import Path
from check_standard_fixed_inventory import setup,P,OUT,W
from check_extremal_read_coupling import quotient,D
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'computability'))
from check_rigid_reachability import State,forward
from periodic_tail_checker import first_mismatch

def main():
 raw=json.loads((OUT/'standard_fixed_inventory_result.json').read_text());model=raw['standard_control']['model'];values={}
 for key,token in re.findall(r'^(\w+) -> (-?\d+|\(- \d+\))$',model,re.M):values[key]=-int(token[3:-1])if token.startswith('(- ')else int(token)
 ev,d,H,points,ix,opts,original=setup();events={}
 for i,p in enumerate(points):
  s=values[f's{i}'];assert s==original[i];hs=opts[i][s]
  ts=[values[f't{i}_{j}']for j in range(len(hs))];assert all(b-a>=4 and(b-a)%4==0 for a,b in zip(ts,ts[1:]))
  for j,h in enumerate(hs):
   t=ts[j];phase=t%P;k=(phase-t)//P;q=(p[0]+k*d[0],p[1]+k*d[1]);assert phase not in events
   events[phase]={'phase':phase,'position':q,'incoming_heading':h,'turn':'R'if j%2==0 else'L','class':p,'rank':j,'clock':t}
 assert len(events)==P;sequence=[events[t]for t in range(P)];word=''.join(e['turn']for e in sequence);p=sequence[0]['position'];h=sequence[0]['incoming_heading'];p0=p;h0=h
 for e in sequence:
  assert e['position']==p and e['incoming_heading']==h;h=(h+(1 if e['turn']=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 assert h==h0 and p==(p0[0]+d[0],p0[1]+d[1]);assert word in W+W
 groups=defaultdict(list)
 for e in sequence:
  r,k=quotient(e['position'],d);groups[r].append((e['phase']-P*k,k,e['turn']))
 seed=set()
 for r,g in groups.items():
  g.sort();assert g[0][2]=='R' and all(a[2]!=b[2]for a,b in zip(g,g[1:]))
  for n in range(min(k for _,k,_ in g),max(k for _,k,_ in g)):
   c=next(c for _,k,c in g if k<=n)
   if c=='L':seed.add((r[0]+n*d[0],r[1]+n*d[1]))
 state=State(frozenset(seed),p0,h0);assert first_mismatch(state,word)is None
 s=state
 for t in range(P*3):assert ('L'if s.p in s.black else'R')==word[t%P];s=forward(s)
 result={'status':'PASS exact SAT clock-model materialization, literal successor orbit, and full infinite finite-seed periodic-tail verification','word':word,'standard_phase':(W+W).find(word),'position':p0,'heading':h0,'drift':d,'seed':sorted(seed),'seed_mass':len(seed),'events':sequence,'literal_extra_periods':3,'full_tail_mismatch':None}
 (OUT/'standard_inventory_positive_model_certificate.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items()if k not in('events','word','seed')},indent=2))
if __name__=='__main__':main()

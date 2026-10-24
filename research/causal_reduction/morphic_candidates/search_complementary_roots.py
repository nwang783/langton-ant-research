"""Complementary initial phases omitted by the earlier R-prolongable search.
Exhaustive finite family controls, with analytic mass filters. Survivors are UNKNOWN.
"""
import itertools,collections,json,pathlib,sys,time,hashlib
from search_uniform_turns import check
HERE=pathlib.Path(__file__).resolve().parent
D=((0,1),(1,0),(0,-1),(-1,0))

def spec(w):
 x=y=h=0;seen={}
 for c in w:
  p=x,y
  if seen.get(p)==c:return None
  seen[p]=c;h=(h+(1 if c=='R'else-1))%4;dx,dy=D[h];x+=dx;y+=dy
 return h,x,y

def filt(u,v,a2,mode):
 n=len(u);q=2*u.count('R')-n;r=2*v.count('R')-n;alpha=(q+r)//2
 if alpha<0:return 'negative_asymptotic_mass'
 if alpha and n>a2:return 'signed_mass_exceeds_area'
 if alpha==0:
  if mode=='L':return 'L_root_symmetric_mass'
  if q*q<=a2:return 'two_cycle_mass_below_midpoint'
  if abs(q)>a2:return 'signed_mass_exceeds_area'
 return None

def run(n,cap):
 groups=collections.defaultdict(list);start=time.time();valid=0
 for a in itertools.product('RL',repeat=n):
  w=''.join(a);g=spec(w)
  if g is not None and g[0]in(1,3)and g[1]*g[1]+g[2]*g[2]>1:groups[g].append(w);valid+=1
 totals=collections.Counter();by_mode=collections.defaultdict(collections.Counter);surv=[];latest={};digest=hashlib.sha256();records=[]
 for(h,x,y),us in groups.items():
  if h!=1:continue
  a2=x*x+y*y
  for u in us:
   for v in groups.get((3,-x,-y),[]):
    modes=[]
    if v[0]=='L':modes.append(('L','L',1))
    if u[0]=='L'and v[0]=='R':modes.append(('two_cycle','R',2))
    for mode,s,period in modes:
     f=filt(u,v,a2,mode)
     if f:r={'kind':'analytic_filter','filter':f}
     else:r=check(u,v,s,period,cap)
     r.update(n=n,u=u,v=v,root=s,first_cycle=period,scale=[x,y],mode=mode)
     totals[r['kind']]+=1;by_mode[mode][r['kind']]+=1
     if r['kind']=='prefix_survivor':surv.append(r);print('SURVIVOR',json.dumps(r),flush=True)
     if r['kind']=='chronology_conflict'and r['time']>latest.get(mode,{}).get('time',-1):latest[mode]=r
     digest.update(json.dumps(r,sort_keys=True).encode()+b'\n');records.append(r)
 return dict(length=n,internally_valid_images=valid,totals=dict(totals),by_mode={k:dict(v)for k,v in by_mode.items()},survivors=surv,latest=latest,record_sha256=digest.hexdigest(),seconds=time.time()-start),records

if __name__=='__main__':
 maximum=int(sys.argv[1])if len(sys.argv)>1 else 17
 cap=int(sys.argv[2])if len(sys.argv)>2 else 100000
 summary=[];allrows=[]
 for n in range(3,maximum+1,2):
  r,rows=run(n,cap);summary.append(r);allrows.extend(rows);print('LENGTH',json.dumps(r),flush=True)
  (HERE/f'complementary_roots_l{maximum}.json').write_text(json.dumps(dict(scope='All internally alternating-valid common-scale expanding geometric turn substitutions at odd lengths3..maximum, with L-prolongable root or first-letter2-cycle. Analytic mass filters and finite conflicts only; survivors are UNKNOWN.',maximum=maximum,prefix_cap=cap,results=summary)))
 (HERE/f'complementary_roots_l{maximum}_records.json').write_text(json.dumps(allrows))

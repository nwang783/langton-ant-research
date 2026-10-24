"""Discovery, not an all-parameter or finite-seed theorem.

Two fresh defects on a mature infinite standard SE input. The second is on
phase72 of the ordinary first defect's certified outgoing highway. Full
infinite old input is retained; no finite-transfer conclusion is inferred.
"""
import sys,json,gzip,hashlib
from pathlib import Path
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'))
from ant_exact import P,D,W,plan,canonical_source,step,PHASES
sys.path.insert(0,str(ROOT/'scattering/transverse'))
from crossing import Field,tail
S=json.loads((ROOT/'continuation_2026-10-22/ant_continuation/one_bit_certificate_restored.json').read_text())
FRESH=[13,14,15,27,28,29,32,38,45,46,47,55,56,57,60,61,62,70,71,75,89]
Q,_,_,_=plan(W,(0,0),2)
u=lambda p:p[0]-p[1];z=lambda p:sum(p)
def plus(p,q):return p[0]+q[0],p[1]+q[1]
def run(r,k,cap=500000):
 age=S['thresholds'][r];R=next(x for x in S['cases'] if x['n']==age and x['r']==r)
 p=tuple(R['position']);h=R['heading'];phase=R['phase'];tw=W[phase:]+W[:phase];drift=tuple(R['tail']['drift'])
 ex=plan(tw[:(72-phase)%104],p,h)[2];q2=plus(ex,(k*drift[0],k*drift[1]));assert q2!=Q[r]
 field=Field([(plus(b,(-2,2)),(-2,2),0,None) for b in D],P^{Q[r],q2})
 p=(0,0);h=2;letters=[];low=0;high=0;zmin=zmax=0;hit=None
 for t in range(cap):
  if p==q2 and hit is None:hit=t
  low=min(low,u(p));high=max(high,u(p));zmin=min(zmin,z(p));zmax=max(zmax,z(p))
  p,h,ch=field.step(p,h);letters.append(ch)
  if t<r:assert ch==W[t]
  if t==r:assert ch!=W[r]
  if hit is not None and t>hit+52000 and (t+1)%104==0:
   w=''.join(letters[-104:])
   if w in PHASES and ''.join(letters[-312:])==w*3:
    cert=tail(field,p,h,w)
    if cert:
     reads,_,_,_=plan(w,p,h);low=min(low,min(map(u,reads)));high=max(high,max(map(u,reads)));zmin=min(zmin,min(map(z,reads)));zmax=max(zmax,max(map(z,reads)))
     filename=f'r{r}_k{k}.txt.gz'
     with gzip.open(HERE/filename,'wt') as f:f.write(''.join(letters))
     return dict(r=r,k=k,q1=Q[r],q2=q2,first_tail_phase=phase,first_tail_drift=drift,second_hit=hit,capture=t+1,pose=[p,h],tail=cert,limits={'u':[low,high],'z':[zmin,zmax]},forward_guard_possible=cert['drift'][0]-cert['drift'][1]>=0,word_file=filename)
 return dict(r=r,k=k,q2=q2,second_hit=hit,status='cap',pose=[p,h],limits={'u':[low,high],'z':[zmin,zmax]})
if __name__=='__main__':
 rows=[]
 ks=list(map(int,sys.argv[1:])) or [100,101]
 for r in FRESH:
  for k in ks:
   out=run(r,k);rows.append(out);print(json.dumps(out),flush=True)
   (HERE/'discovery.json').write_text(json.dumps(rows,indent=2)+'\n')

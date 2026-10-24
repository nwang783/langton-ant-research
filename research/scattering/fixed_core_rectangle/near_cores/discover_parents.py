"""Candidate discovery for finitely many near retained-core two-bit parents."""
import sys,json,gzip
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,'/workspace/shared/langton/continuation_2026-10-22/ant_continuation')
from ant_exact import step,certify_period,PHASES
sys.path.insert(0,'/workspace/shared/langton/continuation_2026-10-22/ant_continuation2/planar_structure')
from extract_exceptional_template import long_runs

def run(m,n,cap=1500000):
 q=(-33-2*n,-14-2*n);s=(-23-2*m,31+2*m);B={q,s};p=(0,0);h=0;letters=[];last='';contacts={}
 for t in range(cap):
  if p in (q,s) and p not in contacts:contacts[p]=t
  p,h,ch=step(B,p,h);letters.append(ch);last=(last+ch)[-312:]
  if t>1000 and t%104==103 and last[-104:] in PHASES and last==last[-104:]*3:
   cert=certify_period(B,p,h,last[-104:])
   if cert:
    w=''.join(letters)
    return dict(m=m,n=n,capture=t+1,pose=[p,h],tail=cert,phase=PHASES[last[-104:]],contacts=[(q,t) for q,t in contacts.items()]),w
 return dict(m=m,n=n,status='cutoff',pose=[p,h]),None

def extract(m,r0,w0,r1,w1):
 rr0,rr1=long_runs(w0),long_runs(w1);assert len(rr0)==len(rr1),(m,'run count')
 l0=l1=0;segs=[]
 for (a0,c0),(a1,c1) in zip(rr0,rr1):
  assert w0[l0:a0]==w1[l1:a1],(m,'fixed piece mismatch',a0,a1)
  if l0<a0:segs.append(dict(type='finite',word=w0[l0:a0]))
  assert w0[a0:a0+104]==w1[a1:a1+104]
  coef=c1-c0;segs.append(dict(type='periods',word=w0[a0:a0+104],count=[coef,c0-200*coef]))
  l0=a0+104*c0;l1=a1+104*c1
 assert w0[l0:]==w1[l1:]
 if l0<len(w0):segs.append(dict(type='finite',word=w0[l0:]))
 tcoef=len(w1)-len(w0);p0,h0=r0['pose'];p1,h1=r1['pose'];assert h0==h1
 pc=[p1[i]-p0[i] for i in (0,1)];pk=[p0[i]-200*pc[i] for i in (0,1)]
 return dict(status='two-sample candidate; exact symbolic proof required',m=m,base=200,segments=segs,infinite_tail_word=w0[-104:],time=[tcoef,len(w0)-200*tcoef],pose_coeff=pc,pose_constant=pk,heading=h0,drift=r0['tail']['drift'])

if __name__=='__main__':
 out=[]
 for m in range(15):
  r0,w0=run(m,200);r1,w1=run(m,201)
  row=dict(m=m,r0=r0,r1=r1)
  if w0 and w1:
   try:
    T=extract(m,r0,w0,r1,w1);(HERE/f'template_m{m}.json').write_text(json.dumps(T,indent=2)+'\n')
    row['candidate']={k:v for k,v in T.items() if k not in ('segments','infinite_tail_word')}
   except AssertionError as e:row['candidate_failure']=str(e)
  out.append(row);print(json.dumps(row),flush=True)
  (HERE/'discovery.json').write_text(json.dumps(out,indent=2)+'\n')

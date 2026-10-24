"""Exact controls for the two checker-axis incidence parameters.
The mined words are verified literally, independently of their blank history.
No global model is inferred from a finite action.
"""
import json,pathlib,collections
D=((0,1),(1,0),(0,-1),(-1,0))
SAMPLES=[('R','LRLLLLRRRRLRRLRRLRRLL'),('R','RRLLRLRRRRLRRRRLLLLRLRLLRLLRL'),('L','RLLRLRRRRLRRRRLLLLRLRLLRLLRLL')]

def analyze(w,root):
 x=y=h=0;last={};first={};vis=[];counts=[0]*8;charge=0;mn=0;ds=0
 for t,c in enumerate(w):
  q=(x,y);assert last.get(q)!=c,(w,t,q,c)
  first.setdefault(q,c);last[q]=c;counts[2*h+(c=='L')]+=1;vis.append(q)
  eps=1 if c=='R' else -1;charge+=eps;mn=min(mn,charge);ds+=(-1)**t*eps
  h=(h+eps)%4;x+=D[h][0];y+=D[h][1]
 expected=(1,0,1) if root=='R' else (-1,0,3)
 assert (x,y,h)==expected and charge==(1 if root=='R' else -1)
 excess=counts.copy();excess[root=='L']-=1;B,A=excess[:2]
 assert excess==[B,A,A,B,B,A,A,B]
 assert ds==charge+4*(B-A)
 seed=sorted(q for q,c in first.items() if c=='L');out=set(seed)
 for q in vis:out.symmetric_difference_update([q])
 return dict(root=root,word=w,length=len(w),counts=counts,A=A,B=B,delta=B-A,charge=charge,checker_signed_charge=ds,prefix_min=mn,minimum_input=seed,output=sorted(out),read_support=sorted(first))

records=[analyze(w,c) for c,w in SAMPLES]
r,l=SAMPLES[1][1],SAMPLES[2][1];assert r[1:]+'L'==l
cases=[]
# Exact scalar recurrence controls, including unequal image lengths and the
# allowed lambda=-1 mode. The geometries/charges are checked above or directly.
R9='RRRRLLLLR';L9='LRRLLLLRR'
for R,L in [(r,l),(R9,l),(r,L9),(R9,L9)]:
 ar=analyze(R,'R');al=analyze(L,'L');dr=ar['delta'];dl=al['delta'];lam=1+2*(dr-dl);b=2*(dr+dl)
 for root in 'RL':
  w=root;d=1 if root=='R' else -1;seq=[d]
  for level in range(1,4):
   w=''.join(R if c=='R' else L for c in w);d=lam*d+b
   direct=sum((1 if c=='R' else -1)*(-1)**j for j,c in enumerate(w));assert direct==d
   seq.append(d)
  cases.append(dict(R=R,L=L,root=root,lambda_value=lam,bias=b,checker_sequence=seq))
p=pathlib.Path(__file__);ans=dict(status='EXACT LOCAL CONTROLS ONLY',samples=records,scalar_recurrence_controls=cases)
p.with_suffix('.json').write_text(json.dumps(ans,indent=2)+'\n');print(json.dumps(dict(samples=[{k:q[k] for k in ['root','length','A','B','delta','prefix_min','checker_signed_charge']} for q in records],recurrence_cases=len(cases))))

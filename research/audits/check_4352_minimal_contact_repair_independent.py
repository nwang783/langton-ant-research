from pathlib import Path
from itertools import product
import json,hashlib
R=Path(__file__).resolve().parents[1];U=R/'causal_reduction/unit_scale';D=(1j,1,-1j,-1);xy=lambda p:(int(p.real),int(p.imag))
def trace(w,p,h):
 rows=[]
 for i,c in enumerate(w):rows.append((i,p,h,c));h=(h+(1 if c=='R'else-1))%4;p+=D[h]
 return rows,p,h
m=json.loads((U/'prepared4352_two_phase_manifest.json').read_text());L=json.loads((U/'prepared4352_fresh_launch.json').read_text());q=14-7j;owned=14-8j
lr,_,_=trace(L['forward_prelude_word'],complex(*L['forward_entry_pose'][0]),L['forward_entry_pose'][1]);hist=[(i,h,c)for i,p,h,c in lr if p==owned];assert hist==[(5209,0,'L'),(5213,2,'R'),(5217,0,'L')]
wr,ep,eh=trace(m['stages'][11]['word'],-2+3j,3);assert ep==24+29j
assert not[(i,(owned-p).real/26)for i,p,h,c in wr if(owned-p).real==(owned-p).imag and (owned-p).real%26==0 and (owned-p).real>=0]
mins=[]
for s in m['stages'][12:14]:
 (a,x),(b,y)=s['start_x_N_constant'],s['start_y_N_constant'];rr,p,h=trace(s['word'],complex(x,y),s['heading']);du=int(p.real+p.imag)-x-y;lo=min(int(p.real+p.imag)for i,p,h,c in rr);cm,cc=s['count_N_constant'];coef=a+b
 if du<0:coef+=du*cm;lo+=du*(cc-1)
 assert coef>=0 and coef+lo>6;mins.append((coef,lo))
pr,pe,ph=trace((m['stages'][13]['word']*2)[:17353],117+111j,0);assert(pe,ph)==(q,3)and all(p!=owned for i,p,h,c in pr)
counts=[];records=[]
for n in(1,5,9):
 geom=0;legal=[]
 for bits in product('RL',repeat=n-1):
  w='L'+''.join(bits);rr,p,h=trace(w,q,3)
  if(p,h)!=(14-6j,0):continue
  geom+=1;last={};bad=None
  for i,p,h,c in rr:
   if last.get(p)==c:bad=(i,xy(p),c);break
   last[p]=c
  if bad is None:legal.append(w);assert rr[1][1]==owned and rr[1][3]=='L'
  records.append(dict(word=w,internal_conflict=bad))
 counts.append(dict(length=n,geometric=geom,internally_legal=legal))
assert [x['geometric']for x in counts]==[0,2,18]
assert set(sum([x['internally_legal']for x in counts],[]))=={'LLLLR','LLRRRRLLR','LLLRRRRLR','LLLLRLLLL'}
# Starting W forces odd step1 vertical. Odd final length has (n+1)/2
# vertical moves; displacement +1 requires this count odd, hence n=1 mod4.
out=dict(status='PASS independent exact-pose repairs length<=9 and all-M inherited-white ownership',note_sha256=hashlib.sha256((U/'prepared4352_minimal_contact_repair.md').read_bytes()).hexdigest(),manifest_sha256=hashlib.sha256((U/'prepared4352_two_phase_manifest.json').read_bytes()).hexdigest(),counts=counts,records=records,owned_cell=xy(owned),last_launch_reads=hist,later_min_u_affine=mins,scope='Only initial additions disjoint from entire preceding READ preserve the stated contact. No longer repair, earlier deviation or changed producer excluded.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(out['note_sha256'])

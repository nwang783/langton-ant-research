"""Normalize the fixed 171 retained one-turn corners and their exact reversals.
No image or cap search. Contracts are finite literal read histories; no new
all-parameter preparation or infinite-tail realization is asserted here.
"""
from pathlib import Path
import hashlib,json
P=Path(__file__).resolve().parent
H=json.loads((P/'short_refinement_scaffold_inputs.json').read_text())['H']
I=H[::-1].translate(str.maketrans('RL','LR'))
D=((0,1),(1,0),(0,-1),(-1,0))

def rot(p,k):
 x,y=p
 for _ in range(k%4):x,y=y,-x
 return x,y

def trace(w,p=(0,0),h=1):
 rows=[]
 for i,c in enumerate(w):
  rows.append((i,p,h,c));h=(h+(1 if c=='R' else -1))%4
  d=D[h];p=p[0]+d[0],p[1]+d[1]
 return rows,p,h

def contract(rows):
 first={};last={};odd=set()
 for i,p,h,c in rows:
  assert p not in last or last[p]!=c,(p,i,c)
  first.setdefault(p,c);last[p]=c;odd.symmetric_difference_update({p})
 B={p for p,c in first.items()if c=='L'}
 return {'required_black':sorted(B),'required_white':sorted(p for p,c in first.items()if c=='R'),
         'complete_xor':sorted(odd),'minimal_output_black':sorted(B^odd),'reads':len(rows)}

def main():
 cases=json.loads((P/'single_turn_corner_selected.json').read_text())['cases'];out=[]
 for idx,c in enumerate(cases):
  a,b=c['in_phase'],c['out_phase'];w=H[:a]+c['cap']+(H[b:]if b else'')
  rows,q,h=trace(w);f=contract(rows);assert h in(0,2)
  iw=w[::-1].translate(str.maketrans('RL','LR'))
  s=(q[0]-D[h][0],q[1]-D[h][1]);ih=(h+2)%4
  ir,ep,eh=trace(iw,s,ih);assert(ep,eh)==((-1,0),3)
  # Literal time-reversal identity, with every incoming pose checked.
  for (j,p0,h0,c0),(i,p1,h1,c1) in zip(ir,reversed(rows)):
   outgoing=(h1+(1 if c1=='R' else -1))%4
   assert p0==p1 and h0==(outgoing+2)%4 and c0!=c1
  ic=contract(ir)
  assert set(map(tuple,ic['required_black']))==set(map(tuple,f['minimal_output_black']))
  assert set(map(tuple,ic['minimal_output_black']))==set(map(tuple,f['required_black']))
  # Canonical I output heading E, preserving phase0 and setting input at origin.
  # The extra half-turn is a genuine proper rotation, not a sector-changing reflection.
  er,eq,eg=trace(iw,(0,0),(ih+2)%4);assert eg==1
  expected=rot((-1-s[0],-s[1]),2);assert eq==expected
  ec=contract(er)
  # A finite two-sided 30-period control, including all shared-cell histories.
  fr,fp,fh=trace(H*30+w+H*30);fc=contract(fr)
  rev=(H*30+w+H*30)[::-1].translate(str.maketrans('RL','LR'))
  rr,rp,rh=trace(rev,(fp[0]-D[fh][0],fp[1]-D[fh][1]),(fh+2)%4)
  rc=contract(rr);assert rp==(-1,0) and rh==3
  assert set(map(tuple,rc['required_black']))==set(map(tuple,fc['minimal_output_black']))
  out.append({'index':idx,'source_signature':[a,c['cap'],b],
    'forward_word':w,'forward_start':[[0,0],1],'forward_end':[q,h],
    'inverse_word':iw,'inverse_conjugate_start':[s,ih],'inverse_conjugate_end':[[-1,0],3],
    'inverse_output_E_start':[[0,0],(ih+2)%4],'inverse_output_E_end':[eq,eg],
    'inverse_output_E_contract':ec,'full_30_plus_corner_plus_30_control_reads':len(rr)})
 result={'scope':__doc__,'source_sha256':hashlib.sha256((P/'single_turn_corner_selected.json').read_bytes()).hexdigest(),
   'H':H,'I':I,'convention':'Headings N,E,S,W=0,1,2,3; clockwise rotations. Exact inverse pose R(p,h)=(p-D[h],h+2), board unchanged.',
   'count':len(out),'distinct_forward_words':len({z['forward_word']for z in out}),'cases':out}
 target=P/'retained_inverse_corner_contracts.json';target.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({k:result[k]for k in('count','distinct_forward_words','source_sha256')}))
 print('output_sha256',hashlib.sha256(target.read_bytes()).hexdigest())
if __name__=='__main__':main()

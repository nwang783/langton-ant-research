"""Read-set geometry only; color validity comes from the separate certificate."""
import json
from pathlib import Path
from bivariate import A
from certify_bivariate import N,M
HERE=Path(__file__).resolve().parent

def main():
 T=json.loads((HERE/'template.json').read_text());base=A.point(0,0);h=0;maxwidth=0;checks=0;records=[]
 periods={1:A.add(N,(0,0,8)),3:A.add(N,(0,0,7)),5:M,7:A.add(M,(0,0,2)),9:A.add(N,(0,0,-20)),11:A.add(A.add(N,M),(0,0,10))}
 def width(q,d=None):
  nonlocal checks
  choices=[]
  for norm in ((1,1),(1,-1)):
   a=A.add(A.scale(q[0],norm[0]),A.scale(q[1],norm[1]))
   if a[:2]==(0,0) and (d is None or sum(x*y for x,y in zip(norm,d))==0):choices.append(abs(a[2]))
  assert choices,('no fixed diagonal strip',q,d)
  checks+=1;return min(choices)
 for i,s in enumerate(T['segments']):
  qs,_,end,eh=A.plan(s['word'],(0,0),h)
  d=end if s['type']=='periods' else None
  H=max(width(A.translate_local(q,base,0),d) for q in qs);maxwidth=max(maxwidth,H)
  records.append(dict(segment=i,width=H))
  if d is None:base=A.translate_local(end,base,0)
  else:base=A.padd(base,(A.scale(periods[i],d[0]),A.scale(periods[i],d[1])))
  h=eh
 qs,_,end,eh=A.plan(T['infinite_tail_word'],(0,0),h)
 H=max(width(A.translate_local(q,base,0),end) for q in qs);maxwidth=max(maxwidth,H)
 out=dict(status='all-parameter complete read geometry verified',common_diagonal_cross_half_width=maxwidth,tail_width=H,read_identities=checks,records=records)
 (HERE/'geometry.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

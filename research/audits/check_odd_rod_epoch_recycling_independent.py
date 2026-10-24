from pathlib import Path
from collections import Counter
import hashlib,json
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];p=SELF.parent/'check_serial_bridge_archive_independent.py';ns={'__file__':str(p)};exec(p.read_text().split('# Fixed local masks')[0],ns)
ends,graph,component,rank,connected,step,wvertex=[ns[k]for k in('ends','graph','component','rank','connected','step','wvertex')];controls=[];total=0
for r in(1,2,3,7,19,50,101):
 B={complex(x,0)for x in range(2*r+1)};birth={q:0 for q in B};p=0j;h=1;wk=int(wvertex(p,h).real+wvertex(p,h).imag)%4;zk=2-wk
 prior=set(B)|{-1};pp,hh,ch=step(prior,-1+0j,2);assert(prior,pp,hh,ch)==(B,p,h,'L')
 a='LRRL'*r+'L';reset='RRRRL';b='LRRL'*r;word=a+reset+b;ev=Counter();used=[];born1={};turnaround={2*r+1+1j,2*r+1,2*r}
 for t,ch in enumerate(word,1):
  q=p;assert('L'if q in B else'R')==ch
  non={k:connected(B-{q}if ch=='L'else B,k,*ends(q,k))for k in(0,2)}
  for k,v in non.items():
   if v:ev[(t,ch,'w'if k==wk else'z')]+=1
  if t<=len(a)or t>len(a)+5:assert not any(non.values())
  if ch=='R':
   birth[q]=t
   if t<=len(a):born1[q]=t
  else:
   if t>len(a)+5:assert q in born1 and birth[q]==born1[q];used.append((q,birth[q],t))
   if t<=len(a):assert birth[q]==0
   if len(a)<t<=len(a)+5:assert birth[q]==len(a)+1
   del birth[q]
  p,h,ch2=step(B,p,h);assert ch2==ch;total+=1
  if t==len(a):assert B=={complex(x,1)for x in range(2*r)}and(p,h)==(2*r+1j,0)and not graph(B,wk).get(wvertex(p,h))
  if t==len(a)+5:assert B=={complex(x,1)for x in range(2*r)}|turnaround and(p,h)==(2*r-1+1j,3)and len(component(B,wk,wvertex(p,h))[1])==2*r
 assert B=={complex(x,0)for x in range(2*r)}|turnaround and(p,h)==(-1+1j,3)and len(B)==2*r+3
 assert not graph(B,wk).get(wvertex(p,h))and rank(B,0)==rank(B,2)==0
 assert set(q for q,bb,dd in used)==set(born1)and len(used)==2*r
 assert ev=={(4*r+5,'R','z'):1,(4*r+6,'L','z'):1}
 for j in range(r):
  i=r-1-j;odd,even=used[2*j:2*j+2]
  assert odd==(2*i+1+1j,4*i+3,4*r+4*j+7)
  assert even==(2*i+1j,4*i+2,4*r+4*j+10)
 controls.append({'r':r,'initial_mass':2*r+1,'first_reads':4*r+1,'reset_reads':5,'second_reads':4*r,'recycled_first_epoch_lifetimes':len(used),'final_mass':2*r+3,'first_second_age':used[0][2]-used[0][1],'last_second_age':used[-1][2]-used[-1][1]})
D=ROOT/'actual_zipper_spiral_2026-10-23';sha=hashlib.sha256((D/'odd_rod_complete_output_recycling.md').read_bytes()).hexdigest();assert sha=='f98a45b0c5b500c631d3e0fa2462b664d39de4e29821b1b39c0aaf080c6834d5'
out={'status':'PASS all-r complete first-epoch-output recycling after one actual reset','note_sha256':sha,'controls':controls,'literal_reads':total,'analytic':['The known LRRL rod local four-read pattern transports the exact bottom row to top row. The extra odd terminal black is unread until the final L, giving the displayed exact first state. The reset writes four cells and deletes its first, leaving exactly three charged turnaround cells and headingW at the old upper-row endpoint. Their coordinates are outside every second-transport read, so the rotated LRRL pattern consumes precisely all first-output cells.','Both two-row transport graphs are forests by the ordered frontier local rod geometry. During the second transport the retained turnaround w star has only its one possible lower-row endpoint contact, and its z path has only its one possible right endpoint contact with the whole moving-row vertex union; all other vertices are farther right. Thus no bridge is bypassed and no full graph cycle is omitted.','The reset has stationary isolated w cursor, four bridge arms and a final bridge deletion. Its four z arms close one unit cycle on the fourth R and the next L erases it. The reset is exceptional by r4 despite no w cycle event; it is not part of either ordinary epoch.','Actual birth/death matching pairs every second-epoch L with a unique first-epoch R, and no reset or original lifetime. The consumed ages are8j+8 and8j+12, ranging8 to8r+4. All turnaround writes remain on the complete final board.','The entry is a literal proper post-L cut, both long epochs end at an isolated w cursor, and the next block is therefore exceptional RRRRL. First gain-1, second gain0, total gain2 includingreset; this demonstrates100% fuel recycling but not positive square-root regenerative gain or a repeatable growing construction.'],'scope':'All finite r>=1, exact complete seed2r+1. No infinite growth, capture failure or global cubic sharpness.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])

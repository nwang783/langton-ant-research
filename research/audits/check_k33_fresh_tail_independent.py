from pathlib import Path
from collections import deque,Counter
import json,hashlib
P=Path(__file__).resolve().parents[1];dirs=[1j,1,-1j,-1]
def choices(board,p):return [board[p]]if p in board else([False]if p.imag>=0 else[False,True])
def extend(p,h,board,bit):
 h=h*(1j if bit else -1j);b=board.copy();b[p]=not bit;return p+h,h,b
# Derive complete first-row catalogs directly, independently of saved F/G words.
def climb(H,budget):
 todo=deque([(0j,1j,{},'',0,0)]);answers=[]
 while todo:
  p,h,b,w,N,S=todo.popleft()
  if p.imag==H:answers.append((w,S));continue
  for bit in choices(b,p):
   q,g,c=extend(p,h,b,bit);nn=N+(g==1j);ss=S+(g==-1j)
   if ss<=budget and nn<=H+budget:todo.append((q,g,c,w+('L'if bit else'R'),nn,ss))
 return answers
one=climb(1,2);two=climb(2,3)
assert sorted(one)==[('RRRLLLLRLR',2),('RRRRLR',1)],one
assert two==[('RRRRLRRRRLLLLRLR',3)],two
suffix=two[0][0];p=0j;h=1j;board={}
for c in suffix:
 bit=c=='L';assert bit in choices(board,p);p,h,board=extend(p,h,board,bit)
assert (p,h)==(-2+2j,1j)
initial=board.copy();target=(8,10,8,7);todo=deque([(p,h,board,'',(0,0,0,0))]);nodes={};accepted=[]
while todo:
 p,h,b,w,counts=todo.popleft();opts=choices(b,p);pruned=[]
 if len(w)==33:accepted.append(w)
 else:
  for bit in opts:
   q,g,c=extend(p,h,b,bit);d=dirs.index(g)
   if counts[d]>=target[d]:pruned.append(d);continue
   cc=list(counts);cc[d]+=1;todo.append((q,g,c,w+('L'if bit else'R'),tuple(cc)))
 nodes[w]={'word':w,'pose':[int(p.real),int(p.imag),dirs.index(h)],'counts':list(counts),'options':[int(x)for x in opts],'pruned':pruned}
assert not accepted and len(nodes)==425 and max(map(len,nodes))==31
source=P/'computability/check_k33_fresh_tail.json';report=json.loads(source.read_text());assert nodes=={r['word']:r for r in report['tree']}
assert report['fixed_output_board']==sorted([[int(p.real),int(p.imag),int(b)]for p,b in initial.items()])
out={'status':'PASS independent pristine-crossing inventory and complete continuation tree','one_row_catalog':one,'two_row_three_south_catalog':two,'continuation_nodes':len(nodes),'maximum_legal_extension':max(map(len,nodes)),'accepted33':accepted,'certificate_sha256':hashlib.sha256(source.read_bytes()).hexdigest()}
(P/'audits/k33_fresh_tail_independent.json').write_text(json.dumps(out,indent=2));print(json.dumps(out))

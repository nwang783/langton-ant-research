from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parents[1]
# Independent local complete white states: incoming headings are literal N,E,S,W.
states=[]
for h in range(4):
 for name,hs in [('R',[h]),('D',[h,h]),('S',[h,(h+2)%4]),('A',[h,h,(h+2)%4]),('B',[h,(h+2)%4,(h+2)%4])]:
  out=[(v+(1 if i%2==0 else -1))%4 for i,v in enumerate(hs)]
  states.append((name+str(h),hs,out))
violations=[]
for name,hs,outs in states:
 for j,h in enumerate(hs):
  if h==0 and sum(o==1 for o in outs[:j])>=2:violations.append((name,j))
assert not violations
# First-to-first displacement(-1,-3), alternating axes, first E, last N.
import itertools
lengths=[]
for n in range(2,12,2):
 found=False
 for mids in itertools.product((0,1),repeat=n-2):
  dx=1;dy=1
  for j,s in enumerate(mids,1):
   if j%2==0:dx+=1 if s else -1
   else:dy+=1 if s else -1
  if (dx,dy)==(-1,-3):found=True;break
 if found:lengths.append(n)
assert min(lengths)==10
C=lambda h:7*(h//3)+(0,1,3)[h%3]
triples=[]
for b in range(3,10002,2):
 for k in range(5,3*b+1,4):
  ell=(k-1)//4
  pairs=[(ell+(1-z)//2,max(0,z-ell-1))for z in [3,b]]
  if all(s>=C(h)for s,h in pairs):triples.append([3,b,k])
assert triples==[[3,3,9],[3,5,13],[3,7,21],[3,11,33]],triples
notes=['periodic_classification_new/cap_three_marked_a_transport.md','computability/rectangular_fresh_record_bounds.md']
out={'status':'PASS independent finite algebra controls','white_histories':len(states),'later_north_after_two_east_departures':violations,'shortest_required_detour_length':min(lengths),'rectangular_triples_through_b10001':triples,'note_hashes':{p:hashlib.sha256((P/p).read_bytes()).hexdigest()for p in notes},'scope':'The finite b scan supplements the analytic residue proof; it is not the all-b argument.'}
(P/'audits/marked_a_rectangular_controls.json').write_text(json.dumps(out,indent=2));print(json.dumps(out))

"""Fresh all-packet residual identities and finite grammar boundary exceptions."""
from pathlib import Path
import json
words={'D':'LLLLRLRRRR','C':'LLLLRLRRRRLRRRR','V':'LLLLRLRRRRLRRLRRRR'};M='LLLLRLRRRRL';names=['D','DC','DCC','DCCC','V','VC','VCC']
def trace(w):
 p=0j;h=1j;required={};last={};flip=set();context=set()
 for t,c in enumerate(w):
  if last.get(p)==c:return None
  required.setdefault(p,c=='L');last[p]=c;context.add(p);flip.symmetric_difference_update({p});h*=(-1j if c=='R'else 1j);p+=h
 return p,h,{p for p,b in required.items()if b},flip,context
K=trace(M)[2];raw=[''.join(words[c]for c in n)for n in names];checks=[]
for name,w in zip(names,raw):
 end,h,_,flip,_=trace(w);_,_,entry,_,context=trace(w+M);endcore={end+h/1j*z for z in K}
 assert K<=entry and endcore<=entry^flip and K<=context and endcore<=context and flip<=context
 inputs=entry-K;outputs=(entry^flip)-endcore
 assert inputs<=context and outputs<=context
 # Every residual token not in inputs lies outside the COMPLETE context,
 # since all other context cells outside the core are forced white.
 assert context-(K|inputs)==context-entry
 # A wholly unchanged extra black token can therefore neither collide with
 # a new output nor migrate into the new core.
 assert not((inputs|outputs|endcore)-context)
 checks.append({'packet':name,'input_count':len(inputs),'output_count':len(outputs),'black_increment':w.count('R')-w.count('L')})
assert trace(words['C']*4+M)is None
assert trace(words['D']+words['C']*4+M)is None
assert trace(words['V']+words['C']*3+M)is None
assert all(trace(raw[2]+w+M)is None for w in raw)
assert all(trace(w+raw[3]+M)is None for w in raw)
assert [words[z].count('R')-words[z].count('L')for z in['D','C','V']]==[0,3,4]
assert trace(words['D'])[:2]==(1+1j,1j)
out={'status':'PASS residual token protection and recurrent-packet boundary reduction','packets':checks,'recurrent_packet_types':[0,1,4,5,6],'boundary_exceptions':{'DCC':'cannot have a successor packet','DCCC':'cannot have a predecessor packet'},'forbidden_long_runs':['CCCC','DCCCC','VCCC'],'macro_mass_increments':[0,3,4],'D_endpoint':[1,1,0]}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])

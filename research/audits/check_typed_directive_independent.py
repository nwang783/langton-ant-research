"""Independent palette, local assignment tree, Cartesian inventory and third-level replay."""
from pathlib import Path
from itertools import product
from collections import Counter
import hashlib,json,array,time
R=Path(__file__).resolve().parents[1];D=R/'causal_reduction/unit_scale';start=time.monotonic()
HEAD=(1j,1,-1j,-1)
def replay(word,h=0):
 z=0j;v=HEAD[h];last={}
 for t,c in enumerate(word):
  if last.get(z)==c:return t
  last[z]=c;v*= -1j if c=='R'else 1j;z+=v
 return None
pal=[['R'],['L']]
for letters in product('RL',repeat=9):
 word=''.join(letters);e=word.count('R')-word.count('L')
 if e not in(-1,1):continue
 z=0j;v=1j
 for c in word:v*= -1j if c=='R'else 1j;z+=v
 if z==e and v==e and replay(word)is None:pal[e<0].append(word)
assert list(map(len,pal))==[7,7]
def typed(word,h):
 ans=[]
 for c in word:
  ans.append(2*h+(c=='L'));h=(h+(1 if c=='R'else-1))%4
 return ans
for s in range(8):
 for w in pal[s%2][1:]:assert Counter(typed(w,s//2))==Counter({a:1+(a==s)for a in range(8)})
def expansion(word,h,mapping):return ''.join(mapping[s]for s in typed(word,h))
survivors=[];nodes=0
for sign in range(2):
 for primitive in pal[sign][1:]:
  states=typed(primitive,0)
  def search(j,assignment,board,p,heading,word):
   global nodes
   nodes+=1
   if j==len(states):
    assert len(assignment)==8
    survivors.append((primitive,tuple(assignment[s]for s in range(8)),word));return
   s=states[j];assert heading==HEAD[s//2]
   for image in ([assignment[s]]if s in assignment else pal[s%2]):
    field=board.copy();q=p;v=heading;ok=True
    for c in image:
     if field.get(q)==c:ok=False;break
     field[q]=c;v*= -1j if c=='R'else 1j;q+=v
    if ok:
     aa=assignment.copy();aa[s]=image;search(j+1,aa,field,q,v,word+image)
  search(0,{}, {},0j,1j,'')
assert len(survivors)==312
old=json.loads((D/'probe_typed_transport_composition.survivors.json').read_text())
assert set(survivors)=={(x['primitive'],tuple(x['assignment']),x['word'])for x in old}
outer=set()
for primitive,f,word in survivors:
 if len(word)>9:
  for turn in range(4):outer.add(tuple(f[(s-2*turn)%8]for s in range(8)))
assert len(outer)==544
controllers={};pair_count=0
for f in sorted(outer):
 domains=[]
 for s in range(8):
  options=[]
  for word in pal[s%2]:
   expanded=expansion(word,s//2,f)
   if replay(expanded,s//2)is None:options.append((word,expanded))
  domains.append(options)
 for picks in product(*domains):
  if all(len(w)==1 for w,c in picks):continue
  pair_count+=1;g=tuple(w for w,c in picks);C=tuple(c for w,c in picks)
  assert C not in controllers
  controllers[C]=(f,g)
assert pair_count==len(controllers)==29840
inventory=json.loads((D/'analyze_typed_phase_pairs.inventory.json').read_text())
assert [tuple(x['composite'])for x in inventory]==sorted(controllers)
assert all(controllers[tuple(x['composite'])]==(tuple(x['outer']),tuple(x['inner']))for x in inventory)
print(json.dumps({'inventory_pass':True,'survivors':312,'outer_maps':544,'controllers':len(controllers),'nodes':nodes,'seconds':time.monotonic()-start}),flush=True)
# Stream fine letters directly, rather than expanding a complete composed string.
values=array.array('H');hist=Counter()
for C in sorted(controllers):
 for s in range(8):
  for primitive in pal[s%2][1:]:
   states=typed(primitive,s//2);z=0j;h=HEAD[s//2];seen={};t=0;conflict=None
   for state in states:
    if conflict is not None:break
    for c in C[state]:
     if seen.get(z)==c:conflict=t;break
     seen[z]=c;h*= -1j if c=='R'else 1j;z+=h;t+=1
   assert conflict is not None,(C,s,primitive)
   values.append(conflict);hist[conflict]+=1
assert len(values)==1432320


import sys
if sys.byteorder!='little':values.byteswap()
raw=values.tobytes();source=D/'check_typed_third_level.conflicts.u16'
assert raw==source.read_bytes()
out={'status':'PASS independent full typed-directive certificate','palette':pal,'assignment_tree_nodes':nodes,'local_survivors':312,'outer_candidates':544,'distinct_composites':len(controllers),'primitive_extension_cases':len(values),'latest_conflict':max(hist),'extension_sha256':hashlib.sha256(raw).hexdigest(),'inventory_sha256':hashlib.sha256((D/'analyze_typed_phase_pairs.inventory.json').read_bytes()).hexdigest(),'seconds':time.monotonic()-start,'scope':'Eight physical-state identity/nine phases; arbitrary directive schedules. No hidden-state or larger-primitive extension.'}
(R/'audits/typed_directive_independent.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)

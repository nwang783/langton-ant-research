from pathlib import Path
from collections import Counter,deque
from itertools import product
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'K1_pipeline_detours_2026-10-23';H='NESW';vec=dict(N=1j,E=1,S=-1j,W=-1);letter={v:k for k,v in vec.items()};cp=dict(A=1,Z=0,Y=1j,B=1+1j);op=dict(A=1-1j,Z=-1-1j,Y=-1+1j,B=1+1j)
base=json.loads((D/'canonical_max_face_child_ports.json').read_text())['rows'];assert len(base)==110
xy=lambda p:(int(p.real),int(p.imag))
def outs(h):return [vec[c]*(-1j if k%2==0 else 1j)for k,c in enumerate(h)]
def cell(z,ll,q):return ll+(1+1j)/2+(z-(1+1j)/2)*(1j)**q
def solve(packages,links=(),extra=None):
 hs={};hc={};births=[]
 for row,ll,q in packages:
  rot=1j**q
  for k,h in row['headings'].items():
   z=cell(cp[k],ll,q);hh=''.join(letter[vec[c]*rot]for c in h)
   if z in hs and hs[z]!=hh:return
   hs[z]=hh
  for z,h in[(ll,0)]+[(ll+op[k]*rot,0 if row['other'].get(k,'M')=='M'else-int(row['other'][k][2:]))for k in op]:
   if z in hc and hc[z]!=h:return
   hc[z]=h
  births.append((cell(1,ll,q),[(cell(cp[k],ll,q),vec[o]*rot)for k,o in [('A','W'),('Z','N'),('Y','E'),('B','S')]]))
 if extra is not None:
  z,h=extra
  if z in hs and hs[z]!=h:return
  hs[z]=h
  rr=Counter(h[::2]);assert 0-2j in hc and hc[-2j]==0
  if hc.get(-1-1j)!=rr['S']-rr['N']:return
 nodes=[(z,k)for z,h in hs.items()for k in range(len(h))];edges=[];eq=[];oo={z:outs(h)for z,h in hs.items()}
 for z,h in hs.items():
  for k in range(len(h)-1):edges.append(((z,k),(z,k+1),4))
  for v in vec.values():
   w=z+v
   if w not in hs:continue
   a=[(z,k)for k,o in enumerate(oo[z])if o==v];b=[(w,k)for k,i in enumerate(hs[w])if vec[i]==v]
   if len(a)!=len(b):return
   for a,b in zip(a,b):edges.extend([(a,b,1),(b,a,-1)]);eq.extend([(a,b,1),(b,a,-1)])
 for ent,bound in births:
  first=[]
  for z,v in bound:
   matches=[(z,k)for k,o in enumerate(oo[z])if o==v]
   if not matches:return
   first.append(matches[0])
  if(ent,1)not in first:return
  edges.extend(((ent,1),z,1)for z in first if z!=(ent,1))
 for ent,ex in links:edges.extend([((ent,1),(ex,0),1),((ex,0),(ent,2),1),((ent,2),(ex,1),1)])
 t={n:0 for n in nodes}
 for _ in nodes:
  changed=False
  for a,b,k in edges:
   if t[b]<t[a]+k:t[b]=t[a]+k;changed=True
  if not changed:break
 else:return
 return hs,hc,t,eq

def floor(row):
 pos=dict(A='S',Z='W',Y='N',B='E');return min(-h[::2].count(pos[k])-max(Counter(h[1::2]).values())for k,h in row['headings'].items())
even=[r for r in base if all(len(h)%2==0 for h in r['headings'].values())];assert len(even)==24
eligible=[r for r in even if floor(r)>=-3];assert len(eligible)==23
modes=[]
for row in eligible:
 for ex in row['potential_children']:
  s=solve([(row,0j,0)],[(1,cp[ex])])
  if s is None:continue
  h=row['headings'];bits=(int(h['A'][3]==h['A'][1]),int(h[ex][3]==h[ex][1]));assert bits[0]==bits[1]
  modes.append(dict(profile=row,exit=ex,bits=bits))
ct=Counter((r['exit'],r['bits'])for r in modes);assert ct=={('Z',(0,0)):7,('Z',(1,1)):3,('Y',(0,0)):2,('B',(0,0)):4,('B',(1,1)):4}
ref=json.loads((D/'reverse_even_plateau_span3_face_modes.json').read_text())['rows'];key=lambda r:(json.dumps(r['profile']['headings'],sort_keys=True),r['exit'],tuple(r['bits']));assert set(map(key,modes))==set(map(key,ref))
# Independent complete physical three-selected-face and actual equal-height J closure.
zero=[r for r in modes if r['bits']==(0,0)];straight=[r for r in zero if r['exit']=='Y'];qr={'Z':3,'Y':0,'B':1};triples=[];attempts=0
for pre,cur,nxt in product(zero,straight,zero):
 q=qr[pre['exit']];parts=[(pre['profile'],1-1j,q),(cur['profile'],0j,0),(nxt['profile'],-1+1j,0)];links=[(cell(1,1-1j,q),1),(1,1j),(1j,cp[nxt['exit']]-1+1j)];attempts+=1
 z=solve(parts,links)
 if z is not None:triples.append((pre,cur,nxt,parts,links))
assert attempts==len(triples)==338
closed=[];Jattempts=0
for pre,cur,nxt,parts,links in triples:
 for row,q in product(eligible,range(4)):
  Jattempts+=1;z=solve(parts+[(row,-1-1j,q)],links)
  if z is None:continue
  hs,hc,t,eq=z;assert pre['exit']==nxt['exit']=='B'and q==0
  want={-1j:'NNSS',-1-1j:'EWWE',-1:'NSSN',0:'WWEE'};assert all(hs[p]==h for p,h in want.items())
  # Verify the claimed clock differences from EXACT shared-port equalities, not selected minimal clocks.
  g={n:[]for n in t}
  for a,b,k in eq:g[a].append((b,k))
  def difference(a,b):
   seen={a:0};todo=[a]
   for x in todo:
    for y,k in g[x]:
     if y in seen:assert seen[y]==seen[x]+k
     else:seen[y]=seen[x]+k;todo.append(y)
   return seen[b]
  assert difference((1,1),(-1j,0))==-2 and difference((1,1),(1j,0))==2 and difference((1,2),(-1j,2))==2
  # Each corner's first R/first L fails an outgoing canonical child from J.
  jp=row['headings'];assert row['potential_children']==[]
  closed.append({'pre':pre['profile']['headings'],'cur':cur['profile']['headings'],'next':nxt['profile']['headings'],'J':jp,'physical_histories':{str(xy(p)):h for p,h in hs.items()},'exact_clock_differences':[-2,2,2]})
assert Jattempts==31096 and len(closed)==2
# Four selected LRLR faces plus lower q, which belongs to preceding Q face(0,-2).
qopts=[]
for n in(2,4):
 for x in product('NS',repeat=n):
  h=''.join(x);rn=h[::2].count('N');rs=h[::2].count('S');lm=max(h[1::2].count(c)for c in'NS')
  if rn>=rs and-rn-lm>=-3:qopts.append(h)
poses=[(1-1j,3),(0j,0),(1+1j,3),(2j,0)];contacts=[1-1j,1,1+1j,1+2j,1+3j];links=list(zip(contacts,contacts[1:]));lr=[];lrc={}
for bit in(0,1):
 L=[r for r in modes if r['exit']=='Z'and r['bits']==(bit,bit)];RR=[r for r in modes if r['exit']=='B'and r['bits']==(bit,bit)];ntry=0;nsurv=0
 for pp,qh in product(product(L,RR,L,RR),qopts):
  ntry+=1;packages=[(r['profile'],ll,q)for r,(ll,q)in zip(pp,poses)];z=solve(packages,links,(-1j,qh))
  if z is None:continue
  nsurv+=1;assert bit==1 and pp[1]['profile']['headings']==dict(A='NNSN',Z='WWWE',Y='NNNS',B='EEWE')
  assert pp[1]['profile']['other']['Z']==pp[1]['profile']['other']['Y']=='M-2'
  lr.append({'bit':bit,'q':qh,'faces':[r['profile']['headings']for r in pp],'physical_histories':{str(xy(p)):h for p,h in z[0].items()}})
 lrc[bit]={'attempts':ntry,'survivors':nsurv}
assert lrc=={0:{'attempts':9408,'survivors':0},1:{'attempts':1728,'survivors':5}}
files=['root_free_L_reverse_K1_forces_locked_axis_rail.md']+[f'reverse_even_plateau_span3_{s}.{ext}'for s in['face_modes','straight_branch','LRLR_overlap']for ext in['py','json']];hashes={f:hashlib.sha256((D/f).read_bytes()).hexdigest()for f in files};assert hashes[files[0]]=='2ca8c00228325aa5a8703f247ff060b49935b3291c87faddf2f2ec5bd403cd84'
out={'status':'PASS root-free original M-3 L valley reverse K1 selected curve is locked axis rail; no global exclusion','source_hashes':hashes,'all_even_profiles':24,'floor_eligible_profiles':23,'twenty_modes':[{'headings':x['profile']['headings'],'exit':x['exit'],'bits':x['bits']}for x in modes],'mode_counts':{str(k):v for k,v in ct.items()},'selected_triples':338,'J_completions_tested':Jattempts,'two_straight_obligations':closed,'q_options':qopts,'LRLR_counts':lrc,'five_state1_necessary_overlaps':lr,'analytic_review':[
'The root-free original L minimum Q atM-3 gives only a reverse WHITE-even collar, not a WHITE reverse board. Its reverse L floor is lambda-3 everywhere. The complete canonical face inventory is local to its four actual corners; restricting those24 even rows by this genuine floor leaves23. Independent physical shared-ordinal/canonical-minimum/same-cell-spacing constraints plus exact K1 entry-exit order give20 modes and no bit changes.',
'The two possible state0 straight faces force an equal-height diagonal neighbor J, hence J belongs to the SAME plateau and all four J corners are legitimately WHITE-even. Independent338 selected triples and31096 J completions leave exactly two RIGHT/STRAIGHT/RIGHT configurations with J no possible canonical outgoing child. This uses no assumption on a remote off-Q helper.',
'J cannot be on the chosen canonical birth cycle, since it has outdegree0. At q and z every negative contact enters J, so it cannot be a Gamma contact; the other corners are positive flat. The whole closed J square is disjoint from Gamma and connected through its known LEFT sector, including short quotient lifts. Exact port equalities, independently traced rather than read from one minimum solution, put qL1 strictly between exitR0 and entryR2. Different physical cells rule out endpoint equality. The prepared selected-WHITE cursor lemma places that entire interval RIGHT, contradiction. Only boundary-collar WHITE is needed.',
'The no-LL proof is local: the three genuine parent edges involve four Q faces, and its unused flat cell touches two of them, so that cell is also WHITE-even. Strict actual birth order and its second-output-before-first-input contradiction require no off-Q coloring. With no straight, zero total turn of the embedded essential full-quotient curve implies cyclic LR alternation.',
'The extra lower q(0,-1) in the LRLR calculation is incident to the actual PRECEDING selected Q face(0,-2), even though that face is outside the four displayed packages. Thus q must be WHITE-even with its SE C height0; other C=R_S-R_N<=0 and floor are justified. Omitting it would lose a necessary supplier constraint; setting any truly off-Q helper WHITE would be unjustified. Independent9408/1728 cases give0/5, locking every first RIGHT to row4.',
'Each RIGHT lies in a lifted LRLR window, also for short full quotients. The locked corner histories and alternating quarter-turns propagate a single contact column with two-face displacement(0,2) after rotation. An actual closed full quotient therefore has axis full drift, without primitive reduction. This excludes a root-free shallow minimum only in non-axis fronts; axis rails, odd collars, deeper retreat and prepared BLACK suppliers are not excluded. No original-fuel or capture conclusion follows.'
]}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(ct,lrc)

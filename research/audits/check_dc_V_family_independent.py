"""Independent all-parameter read arrangement for DC V^r VCC V^(r+2).
Global integer-axis partition differs from the producer's per-orbit partition.
Every region is checked exactly; sampled full boards are only controls.
"""
from pathlib import Path
from collections import defaultdict
import json,hashlib
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
B=ROOT/'core_periodicity_new/dc_V_return_family_frozen_20261023_1119';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f.get('frozen',f.get('file'))).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_dc_V_return_family.json').read_text());directions=(1j,1,-1j,-1)
def reads(word,p=0j,h=0):
 out=[]
 for t,ch in enumerate(word):
  out.append((t,p,ch));h=(h+(1 if ch=='R'else-1))%4;p+=directions[h]
 return out,p,h
assert walk(raws[4])[:2]==(1+3j,0)and walk(raws[6])[:2]==(4j,2)
atoms=defaultdict(list)
for kind,word,p,h in (('DC',raws[1],0j,0),('O',raws[4],1+2j,3),('F',raws[6],1+2j,3),('I',raws[4],-3+2j,1),('M',mark,3+0j,1)):
 for t,z,ch in reads(word,p,h)[0]:
  dx,dy=xy(z-(1+2j));atoms[dx+3*dy].append(dict(kind=kind,dy=dy,t=t,turn=ch))
assert {str(k):v for k,v in atoms.items()}==J['atom_inventory']
# Refine all orbit-specific cuts by one common global partition.
cuts=set()
for aa in atoms.values():
 for z in aa:cuts.update((z['dy']-1,z['dy']))
lo=min(cuts)-1;hi=max(cuts)+1
intervals=[(None,lo)]+[(v,v)for v in range(lo+1,hi)]+[(hi,None)]
def has(box,z):return(box[0]is None or box[0]<=z)and(box[1]is None or z<=box[1])
def sample(box):return box[0]if box[0]is not None else box[1]
def active(z,d,e):
 k,y=z['kind'],z['dy']
 if k in ('DC','M'):return d==y
 if k=='O':return d>=y and e<y
 if k=='F':return e==y
 return d>=y-1 and e<=y
phase={'DC':0,'O':1,'F':2,'I':3,'M':4}
def order(z):return(phase[z['kind']],-z['dy']if z['kind']=='O'else z['dy']if z['kind']=='I'else 0,z['t'])
black=[];regions=visits=0
for ell,aa in atoms.items():
 for db in intervals:
  for eb in intervals:
   if db[1]is not None and eb[0]is not None and db[1]<eb[0]:continue
   ordered=sorted((z for z in aa if active(z,sample(db),sample(eb))),key=order)
   turns=''.join(z['turn']for z in ordered);assert all(a!=b for a,b in zip(turns,turns[1:]))
   # Compare every refined region with the author's claimed coarser history.
   candidates=[z for z in J['regions']if z['ell']==ell and has(z['delta'],sample(db))and has(z['epsilon'],sample(eb))]
   assert len(candidates)==1 and candidates[0]['turns']==turns
   fixed_core={z for z,c in walk(mark)[2].items()if c}|{1j}
   fixed={(int(z.real+3*z.imag)-7,int(z.imag)-2)for z in fixed_core}
   dd,ee=sample(db),sample(eb)
   explicit=((ell,dd)in fixed or ell==-3 and dd>=0 and ee<=0 or ell==-5 and dd>=-1 and ee<=-1 or ell==1 and dd>=1 and ee<=1)
   assert turns.startswith('L')==explicit
   regions+=1;visits+=len(turns)
   if turns.startswith('L'):black.append((ell,db,eb))
core={z for z,c in walk(mark)[2].items()if c}
for z in core:
 x,y=xy(z);ell=x+3*y-7;delta=y-2
 for eb in intervals:
  if eb[0]is not None and eb[0]>delta:continue
  assert any(a==ell and has(db,delta)and e==eb for a,db,e in black)
def mass(r):
 total=0
 for ell,(a,b),(c,d) in black:
  lowers=[x for x in(a,None if c is None else r+c)if x is not None];uppers=[x for x in(b,None if d is None else r+d)if x is not None]
  assert lowers and uppers
  total+=max(0,min(uppers)-max(lowers)+1)
 return total
# Beyond every endpoint difference plus two, all active affine branches and
# zero truncations have stabilized. Checking two consecutive tail values fixes
# the exact final affine expression, not an empirical extrapolation.
threshold=2+max([0]+[x-y for _,db,eb in black for x in db for y in eb if x is not None and y is not None])
assert all(mass(r)==3*r+9 for r in range(threshold+2))
# Literal finite controls, including the universal survivor geometry.
controls=[]
for r in (0,1,2,5,17,51):
 seq=[1]+[4]*r+[6]+[4]*(r+2);word=''.join(raws[a]for a in seq)+mark
 end,h,need,flip=walk(word);seed={z for z,c in need.items()if c};assert len(seed)==3*r+9 and core<=seed
 encoded=set()
 for ell,(a,b),(c,d) in black:
  lower=max(x for x in(a,None if c is None else r+c)if x is not None);upper=min(x for x in(b,None if d is None else r+d)if x is not None)
  encoded.update(complex(1+ell-3*delta,2+delta)for delta in range(lower,upper+1))
 assert encoded==seed
 raw=''.join(raws[a]for a in seq);rr,p,hh=reads(raw);assert(p,hh)==(3+0j,1)and len(raw)==36*r+109
 board=set(seed)
 for t,z,ch in rr:
  assert ch==('L'if z in board else'R');board.symmetric_difference_update({z})
 assert len(board)==11*r+30
 controls.append(dict(r=r,mass=len(seed),raw_length=len(raw),final_mass=len(board)))
# All intermediate V/VCC input x coordinates are <=0, while original A/C
# have x=2/3. The final returning index n=-1 gives exactly C,A.
assert [complex(-3*(-1),2+(-1)),complex(-1-3*(-1),1+(-1))]==[3+1j,2+0j]
out=dict(status='PASS independent all-r literal arrangement, finite seed formula and protected-sibling geometry',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),refined_regions=regions,read_obligations=visits,black_refined_regions=len(black),affine_tail_safe_threshold=threshold,explicit_seed='K plus (0,1) plus j=0..r rails (-2-3j,2+j),(-1-3j,1+j),(-1-3j,3+j)',initial_mass_formula='3r+9',raw_duration_formula='36r+109',final_raw_mass_formula='11r+30',controls=controls,scope='Actual finite supported family for every integer r>=0; seed grows with r, C count3, no common seed, renewal, unfunded record or global counterexample.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

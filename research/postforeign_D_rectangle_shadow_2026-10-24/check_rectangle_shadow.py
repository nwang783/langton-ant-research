"""All-length named D-rectangle obstruction and exact finite regressions.
Not a search over generic histories and not arbitrary-tail simplicity.
"""
from pathlib import Path
from collections import Counter
import importlib.util,json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('l',R/'word_stabilization/check_foreign_return_interfaces.py');l=importlib.util.module_from_spec(s);s.loader.exec_module(l);s=importlib.util.spec_from_file_location('o',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');o=importlib.util.module_from_spec(s);s.loader.exec_module(o);W=o.WORDS

def add(a,b):return(a[0]+b[0],a[1]+b[1])
def after(w,p=(0,0,0)):
 q,h=p[:2],p[2]
 for c in w:h=(h+(1 if c=='R'else-1))%4;q=add(q,l.DIRS[h])
 return *q,h
def fine(a):
 p=(0,0);h=0;rr=[]
 for t,c in enumerate(W[a]):rr.append(dict(cell=p,tick0=t,read1=t+1,turn=c));h=(h+(1 if c=='R'else-1))%4;p=add(p,l.DIRS[h])
 return rr
F={a:fine(a)for a in'DCV'}
assert {a:[(min(r['cell'][j]for r in rr),max(r['cell'][j]for r in rr))for j in(0,1)]for a,rr in F.items()}=={'D':[(-1,2),(-1,1)],'C':[(-1,2),(-1,2)],'V':[(-1,2),(-1,3)]}
assert all(next(r for r in F[a]if r['cell']==(2,0))['tick0']==8 for a in'DV')
# All affine stage formulae are in the initial postforeign D frame, normalizedN.
# a>=0,b>=1, 0<=j<=a for N/S;0<=j<=b-1 for W/E.
stages=[dict(stage='N_D',head=['j','j'],heading=0,j_range='0..a',raw_min_y='j-1 >= -1',raw_min_x='j-1 >= -1'),dict(stage='C1',head=['a+1','a+1'],heading=0,raw_min_y='a >= 0'),dict(stage='W_D',head=['a+1-j','a+2+j'],heading=3,j_range='0..b-1',raw_min_y='a+1+j >= 1'),dict(stage='C2',head=['a+1-b','a+2+b'],heading=3,raw_min_y='a+b+1 >= 2'),dict(stage='S_D',head=['a-b-j','a+b+2-j'],heading=2,j_range='0..a',raw_min_y='a+b+1-j >= b+1 >= 2'),dict(stage='C3',head=['-b-1','b+1'],heading=2,raw_min_y='b-1 >= 0'),dict(stage='E_D',head=['-b-1+j','b-j'],heading=1,j_range='0..b-1',raw_min_y='b-j-2 >= -1'),dict(stage='last_V',head=['-1','0'],heading=1)]
# Exact finite symbolic coefficients for each literal read; minima over the
# moving index occur at an endpoint. All expressions have nonnegative
# coefficients after substituting a>=0,b=1+B,j limits.
bounds=[]
for stage in stages[:-1]:
 a=stage['stage'];atom='C'if a[0]=='C'else'D';h=stage['heading']
 for rr in F[atom]:
  x,y=l.rot(rr['cell'],h)
  if a=='N_D':assert x>=-1 and y>=-1
  elif a=='C1':assert 1+y>=0
  elif a=='W_D':assert 2+y>=1
  elif a=='C2':assert 3+y>=2
  elif a=='S_D':assert 3+y>=2
  elif a=='C3':assert 2+y>=0
  elif a=='E_D':assert 1+y>=-1
  bounds.append(dict(stage=a,tick0=rr['tick0'],rotated_offset=(x,y),turn=rr['turn']))
assert len(bounds)==85
# F target g=(-2,-1) is outside the N-rail x cone and below all subsequent
# pre-last-E reads: for j<=b-2 their y>=0. Last E D starts(-2,1,E).
# Q/B target g=(-1,-2) is below every pre-last-V read, whose y>=-1.
foreign=[]
for A,own,g,reader in[('F',47,(-2,-1),'D'),('Q',57,(-1,-2),'V'),('B',67,(-1,-2),'V')]:
 geom=l.literal_geometry(W[A]);ep=tuple(geom['endpoint']);local=add(ep[:2],l.rot(g,ep[2]));tr=l.trace(W[A]+l.M)
 assert tr['last'][local]==('R',own) and list(local)in geom['outputs']
 head=(-2,1,1)if A=='F'else(-1,0,1);target=add(head[:2],l.rot((2,0),head[2]));assert target==g
 foreign.append(dict(A=A,actual_A_RAW_exit=ep,foreign_output_local=local,source_tick0=own,source_read1=own+1,in_A_O=True,output_in_postforeign_D_frame=g,first_incompatible_reader=reader,reader_head=head,reader_tick0=8,reader_read1=9))

def owner(T,tick):
 for j,a in enumerate(T):
  if tick<len(W[a]):return dict(atom=a,atom_index0=j,tick0=tick,read1=tick+1)
  tick-=len(W[a])
 return dict(atom='actual following word',tick0=tick,read1=tick+1)
rect=[];vcc=[]
for a in range(6):
 for b in range(1,7):
  P='D'*(a+1)+'C'+'D'*b+'C'+'D'*(a+1)+'C'+'D'*b+'V'
  assert after(''.join(W[c]for c in P[:-1]))==(-1,0,1)
  for pre in('','U'):
   for A in'FQB':
    T=pre+A+P;tr=l.trace(''.join(W[c]for c in T)+l.M);assert not tr['feasible']
    if not pre or A!='F':
     assert tr['previous_read']==len(W['U'])*len(pre)+({'F':47,'Q':57,'B':67}[A])
     assert owner(T,tr['conflict_read'])['atom']==('D'if A=='F'else'V') and owner(T,tr['conflict_read'])['tick0']==8
    rect.append(dict(a=a,b=b,word=T,immutable=tr,previous_owner=owner(T,tr['previous_read']),conflict_owner=owner(T,tr['conflict_read'])))
for pre in('','U','UC','UCC'):
 for A in'FQB':
  T=pre+A+'VCCVCC';tr=l.trace(''.join(W[c]for c in T)+l.M);assert not tr['feasible'];vcc.append(dict(word=T,immutable=tr,previous_owner=owner(T,tr['previous_read']),conflict_owner=owner(T,tr['conflict_read'])))
# Retain both genuine U-entry positive prefixes; all unlisted cells WHITE.
positive=[]
for T in('UQVCCV','UBVCCV'):
 tr=l.trace(''.join(W[a]for a in T)+l.M);assert tr['feasible'];seed={p for p,(c,t)in tr['first'].items()if c=='L'};black=set(seed);p=(0,0);h=0
 for tick,c in enumerate(''.join(W[a]for a in T)+l.M):
  assert(p in black)==(c=='L');black.remove(p)if c=='L'else black.add(p);h=(h+(1 if c=='R'else-1))%4;p=add(p,l.DIRS[h])
 positive.append(dict(word=T,complete_seed=sorted(seed),seed_mass=len(seed),actual_reads=sum(len(W[a])for a in T)+11,actual_next_prefix_exit=(*p,h)))
result=dict(status='AUTHOR_ALL_LENGTH_NAMED_TEMPLATE_FROZEN_PENDING_REVIEW',scope='Only A P(a,b), a>=0,b>=1, P=D^(a+1) C D^b C D^(a+1) C D^b V. All three foreign choices fail before completion, independent of any earlier field or U prefix. Not arbitrary-tail simplicity.',all_affine_stage_heads_and_raw_bounds=stages,all85_exact_stage_read_offsets=bounds,all3_genuine_foreign_output_guard_transforms=foreign,all216_finite_rectangle_regressions=rect,all12_VCC_pose_return_regressions=vcc,two_genuine_U_entry_fourth_V_positive_prefixes=positive,retained_scope='Exact four-C full-pose return in a complete G8 factor was already excluded by1344. The rectangle targets a proper oldD crossing, not a pose return, but this named D-only family is blocked by a foreign-owned lastR shadow. Mixed V/U rails may read it and are not excluded.',no_generic_search_cutoff_or_mixed_rail_barrier_or_general_tail_simplicity=True)
(H/'rectangle_shadow.json').write_text(json.dumps(result,indent=2)+'\n');print('All-length stage bounds verified;3 actual foreign lastR shadows,216 rectangle and12 exact-pose regressions,2 genuine U-entry positive prefixes retained.')

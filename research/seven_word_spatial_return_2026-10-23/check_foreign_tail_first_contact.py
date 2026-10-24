"""Exact first contacts on genuine Q/B tails after the common F-prefix.
Finite geometric parallelograms only; no ant-prefix or word-tree search.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import hashlib,json
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json';WP=R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json'
G=json.loads(GP.read_text())['geometry'];G7=json.loads(WP.read_text())['macro_words'];M=G[0]['marker'];VEC=((0,1),(1,0),(0,-1),(-1,0));K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)};L={(0,0),(0,1),(1,0),(1,1)}
def rot(q,h):
 x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def det(a,b):return a[0]*b[1]-a[1]*b[0]
def derive(w):
 p=(0,0);h=0;req={};par=set();reads={}
 for t,ch in enumerate(w):
  bit=(ch=='L')^(p in par);assert p not in req or req[p]==bit
  req[p]=bit;reads.setdefault(p,[]).append((t,ch));par.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;p=add(p,VEC[h])
 return req,p,h,reads
WORDS={'D':G[0]['word'],'C':G[1]['word'][len(G[0]['word']):],'V':G[4]['word'],'U':G[7]['word']};STEPS={'D':(2,2),'C':(2,2),'V':(2,6),'U':(0,8)}
def source_chord(a):return(-1,-1),add((-1,-1),STEPS[a])
def closed_hit(a,b,c,d):
 u,v,z=sub(b,a),sub(d,c),sub(c,a);den=det(u,v)
 if den:
  s,t=F(det(z,v),den),F(det(z,u),den)
  return dict(kind='point',s=s,t=t)if 0<=s<=1 and 0<=t<=1 else None
 if det(z,u):return None
 k=0 if u[0]else 1;lo,hi=sorted((F(c[k]-a[k],u[k]),F(d[k]-a[k],u[k])));lo=max(F(0),lo);hi=min(F(1),hi)
 return dict(kind='collinear',lo=lo,hi=hi)if lo<=hi else None

def first_tail_hit(a,b,c,d):
 u,v,z=sub(b,a),sub(d,c),sub(c,a);den=det(u,v)
 if den:
  s,t=F(det(z,v),den),F(det(z,u),den)
  return dict(kind='point',s=s,t=t)if 0<=s<1 and 0<t<=1 else None
 if det(z,u):return None
 # Collinear first onset, not an arbitrary point later inside an overlap.
 k=0 if v[0]else 1;ts=[F(a[k]-c[k],v[k]),F(b[k]-c[k],v[k])];t=min(ts)
 if not 0<t<=1:return None
 point=(c[0]+t*v[0],c[1]+t*v[1]);j=0 if u[0]else 1;s=F(point[j]-a[j],u[j])
 return dict(kind='collinear_first_onset',s=s,t=t)if 0<=s<1 else None
allrows={};Ufilters={}
for gi,name,local_end in((5,'Q',(-7,-7)),(6,'B',(-5,-9))):
 req,_,_,reads=derive(G7[gi]['word']+M);rows=[]
 for residue in range(4):
  h=(-residue)%4
  for a in WORDS:
   A,B=source_chord(a);u=sub(B,A);base=rot((-7,-3),h);tail=rot(sub(local_end,(-7,-3)),h)
   corners=[sub(add(A,(s*u[0],s*u[1])),add(base,(t*tail[0],t*tail[1])))for s in(0,1)for t in(0,1)]
   bounds=[((min(q[i]for q in corners)+1)//2,max(q[i]for q in corners)//2)for i in range(2)]
   for x in range(bounds[0][0],bounds[0][1]+1):
    for y in range(bounds[1][0],bounds[1][1]+1):
     if(x+y+h)%2:continue
     p=x,y;offset=(2*x,2*y);start=add(offset,rot((-1,-1),h));middle=add(offset,base);end=add(offset,rot(local_end,h))
     prefix_hit=closed_hit(A,B,start,middle)
     legal_adjacent=False
     if prefix_hit:
      assert prefix_hit['kind']=='point'
      if prefix_hit['t']!=0 or prefix_hit['s']!=1:continue
      _,ep,dh,_=derive(WORDS[a]);legal_adjacent=p==ep and h==dh
      if not legal_adjacent:continue
     hit=first_tail_hit(A,B,middle,end)
     if hit is None:continue
     ages=[n for n in(residue,residue+4)if n>0 or a!='C']
     rows.append(dict(foreign=name,source_atom=a,foreign_pose=(*p,h),contact=hit,permitted_C_ages=ages,preceding_C_bits=[int(n>=4)for n in ages],exact_candidate_bounds=bounds,legal_F_entry_adjacent_source_endpoint=legal_adjacent))
 allrows[name]=rows
 ur=[]
 for row in rows:
  if row['source_atom']!='U':continue
  x,y,h=row['foreign_pose'];p=x,y
  core={add(p,rot(q,h))for q in K};white={add(p,rot(q,h))for q,b in req.items()if not b};inputs={add(p,rot(q,h))for q,b in req.items()if b}-core
  reason='held_star_in_core'if core&L else'held_star_before_white'if white&L else'unexcluded_necessary_interface'
  input_tags=sorted(inputs&L);surviving=[];age_cuts=[]
  for n,b in zip(row['permitted_C_ages'],row['preceding_C_bits']):
   if reason!='unexcluded_necessary_interface':why=reason
   elif n<=1 and input_tags:why='signed_first_foreign_star_effect_requires_age_at_least_two'
   elif name=='B' and row['foreign_pose']==(-3,6,3) and n==1:
    qlocal=rot(sub((-1,2),p),-h);assert qlocal==(-4,-2)and req[qlocal]is False and reads[qlocal][0]==(52,'R')
    why='signed_q_survives_until_age_two_but_foreign_requires_it_white'
   else:why='unexcluded_necessary_interface';surviving.append(dict(C_age=n,preceding_C_bit=b))
   age_cuts.append(dict(C_age=n,preceding_C_bit=b,reason=why))
  ur.append(dict(**row,context_reason=reason,old_star_input_hits=input_tags,age_classification=age_cuts,remaining_age_labels=surviving))
 Ufilters[name]=ur
assert len(allrows['Q'])==24 and sum(len(r['permitted_C_ages'])for r in allrows['Q'])==47
assert len(allrows['B'])==39 and sum(len(r['permitted_C_ages'])for r in allrows['B'])==76
assert sum(r['contact']['kind']=='collinear_first_onset'for r in allrows['Q'])==1
assert not any(r['contact']['kind']=='collinear_first_onset'for r in allrows['B'])
assert Counter(r['context_reason']for r in Ufilters['Q'])=={'held_star_before_white':7,'held_star_in_core':1,'unexcluded_necessary_interface':1}
assert Counter(r['context_reason']for r in Ufilters['B'])=={'held_star_before_white':10,'held_star_in_core':1,'unexcluded_necessary_interface':4}
remaining=[dict(foreign=r['foreign'],foreign_pose=r['foreign_pose'],labels=r['remaining_age_labels'])for a in'QB'for r in Ufilters[a]if r['remaining_age_labels']]
assert remaining==[dict(foreign='Q',foreign_pose=(-4,3,3),labels=[dict(C_age=5,preceding_C_bit=1)]),dict(foreign='B',foreign_pose=(2,6,0),labels=[dict(C_age=4,preceding_C_bit=1)]),dict(foreign='B',foreign_pose=(-5,2,3),labels=[dict(C_age=5,preceding_C_bit=1)]),dict(foreign='B',foreign_pose=(-3,6,3),labels=[dict(C_age=5,preceding_C_bit=1)]),dict(foreign='B',foreign_pose=(3,0,1),labels=[dict(C_age=3,preceding_C_bit=0),dict(C_age=7,preceding_C_bit=1)])]
D=[GP,WP,H/'foreign_kinked_barrier_manifest.json',H/'foreign_U_early_star_exclusion_manifest.json',R/'core_periodicity_new/U_entry_simplicity_frozen_20261023_1616/manifest.json',R/'core_periodicity_new/U_left_star_permanence_frozen_20261023_1918/manifest.json',R/'core_periodicity_new/U_recycled_q_consumer_frozen_20261023_1954/manifest.json',Path(__file__).resolve()]
def enc(x):
 if isinstance(x,F):return int(x)if x.denominator==1 else str(x)
 if isinstance(x,dict):return{k:enc(v)for k,v in x.items()}
 if isinstance(x,(tuple,list)):return[enc(v)for v in x]
 return x
o=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_AUDIT',scope='Necessary first-contact obligations on actual Q/B tail proxy pieces after their actual F prefix; no internal marker, ghost-path barrier, attained creator reset or global proxy simplicity. Full contexts and signed early U/q history reduce U-source cases only.',counts={name:dict(geometries=len(rs),clock_labels=sum(len(r['permitted_C_ages'])for r in rs))for name,rs in allrows.items()},rows=allrows,U_source_filters=Ufilters,remaining_U_source_cases=remaining,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'foreign_tail_first_contact.json').write_text(json.dumps(enc(o),indent=2)+'\n')
print('Q tails: 24 geometries /47 labels. B tails:39/76. Five U-source interfaces with six remaining age labels; one is preceding-non-C B(3,0,E), age3.')

"""Exact first-consumer classification for a fresh U recycled-q output.
"""
from pathlib import Path
from fractions import Fraction
from collections import Counter
import json,hashlib
W=Path(__file__).resolve().parent;GP=W/'chronology_dcuv/literal_residual_geometry.json';G=json.loads(GP.read_text())['geometry'];L={(0,0),(0,1),(1,0),(1,1)};q=(-1,2);A=(-1,3);B=(-3,5);Cword=G[1]['word'][len(G[0]['word']):]
def rot(p,h):
 x,y=p;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,z):return p[0]+z[0],p[1]+z[1]
def sub(p,z):return p[0]-z[0],p[1]-z[1]
def cross(p,z):return p[0]*z[1]-p[1]*z[0]
def on(p,a,b):return cross(sub(p,a),sub(b,a))==0 and sum((p[i]-a[i])*(p[i]-b[i])for i in range(2))<=0
def contact(a,b,c,d):
 u=sub(b,a);v=sub(d,c);r=sub(c,a);z=cross(u,v)
 if z:
  s=Fraction(cross(r,v),z);t=Fraction(cross(r,u),z)
  return [[str(Fraction(a[k])+s*u[k])for k in range(2)]]if 0<=s<=1 and 0<=t<=1 else[]
 return[list(p)for p in sorted({a,b,c,d})if on(p,a,b)and on(p,c,d)]
def center(p,h):return add((2*p[0],2*p[1]),rot((-1,-1),h))
def run(word,p=(0,0),h=0):
 for ch in word:h=(h+(-1 if ch=='L'else 1))%4;p=add(p,rot((0,1),h))
 return p,h
source_segment=((-1,-1),(-1,7));assert tuple(Fraction(source_segment[0][k])+Fraction(1,2)*(source_segment[1][k]-source_segment[0][k])for k in range(2))==A
# Source q is the physical even-dual edge A--B. Its fresh final identity
# starts after the creating full packet, with its full-source start C clock.
assert set([(2*q[0]-1,2*q[1]+1),(2*q[0]+1,2*q[1]-1)])=={A,B}
rows=[]
for target in[0,1,4,5,6,7,8,9]:
 for h in range(4):
  for si,i in enumerate(G[target]['inputs']):
   p=sub(q,rot(i,h));r=dict(consumer=target,head=[*p,h],input_slot=si)
   if(sum(p)+h)%2:r['reason']='wrong_sector'
   else:
    ctx={add(p,rot(z[:2],h))for z in G[target]['requirements']};hit=sorted(ctx&L);U0=center(p,h);vec=(2,2)if target in[0,1]else(2,6)if target in[4,5,6]else(0,8);U1=add(U0,rot(vec,h))
    if hit:r.update(reason='permanent_source_L_star_context',hits=hit)
    elif contact(U0,U1,*source_segment):
     r.update(reason='consumer_base_contacts_source_U',base_start=U0,base_end=U1,contacts=contact(U0,U1,*source_segment))
    else:
     assert h==2
     if target in[4,5]:
      assert p==(-1,5)and si==0 and U1==B
      assert add(p,rot(G[target]['inputs'][1],h))==(-2,3)
      r.update(reason='only_V_VC_lower_exact_age2_with_older_selected_helper',base_start=U0,base_end=U1,forced_C_age=2,other_selected_input=(-2,3),selected_minimum=3,selected_latest_birth_clock=-1)
     else:
      assert target in[7,8]and(p,si)in[((-2,4),1),((-2,6),2)]
      r.update(reason='signed_recycled_q_to_U_exclusion',base_start=U0,base_end=U1)
   rows.append(r)
counts=dict(Counter(r['reason']for r in rows));assert len(rows)==92;assert counts['only_V_VC_lower_exact_age2_with_older_selected_helper']==2;assert counts['signed_recycled_q_to_U_exclusion']==4
source_prefix=[]
for s in[7,8,9]:
 assert q in set(map(tuple,G[s]['outputs']))
 p,h=run(G[7]['word']);P=center(p,h);assert P==(-1,7);assert contact(A,P,B,A)==[['-1','3']]
 z=[]
 for k in range(G[s]['name'].count('C')):
  X=center(p,h);p,h=run(Cword,p,h);Y=center(p,h);assert not contact(X,Y,B,A);z.append([X,Y])
 source_prefix.append(dict(source=s,post_midpoint_U_remainder=[A,P],C_tail_chords=z))
# Principal join directions: consumer S=6, bridge SE=7, source N=2
# in units pi/4; the two actual signed turns are +1,+3.
joins=[1,3];assert sum(joins)==4
D=[GP]+[W/p/'manifest.json'for p in['U_left_star_permanence_frozen_20261023_1918','U_entry_simplicity_frozen_20261023_1616','current_residual_barrier_frozen_20261023_1822','U_renewal_exact_clock_frozen_20261023_1902','U_recycled_q_return_frozen_20261023_1939','chronology_dcuv/critical_ucc_count5/age_five_queries']]+[Path(__file__).resolve()]
R=dict(status='AUTHOR_U_RECYCLED_Q_EXACT_CONSUMER_PENDING_AUDIT',scope='A genuine fresh U-family recycled-q output(-1,2) can retire only as V/VC lower input at source-relative(-1,5,S), exact source-inclusive C age2. The other selected input(-2,3) strictly predates creating U. If creator is factor-first that helper is a separate singleton entry root, so this V/VC merges at least two reset historical components. No arbitrary later-creator component conclusion or permanence.',all_92_consumer_alignments=rows,counts=counts,source_partial_atom_and_tail_bridge_checks=source_prefix,V_turn_identity='future n*pi/2+alphaV-pi/2; closing (3*pi/4-alphaV)+3*pi/4; total n*pi/2+pi',forced_Cgap=2,selected_helper_latest_birth_clock=-1,dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(W/'chronology_dcuv/U_recycled_q_consumer.json').write_text(json.dumps(R,indent=2)+'\n');print(json.dumps(counts,indent=2))

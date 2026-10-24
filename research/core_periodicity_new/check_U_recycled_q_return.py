"""Protected single-edge Jordan obstruction: a fresh U recycled-q output
cannot become any U-family input later inside the retained factor.
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
for target in[7,8,9]:
 for h in range(4):
  for si,i in enumerate(G[target]['inputs']):
   p=sub(q,rot(i,h));r=dict(consumer=target,head=[*p,h],input_slot=si)
   if(sum(p)+h)%2:r['reason']='wrong_sector'
   else:
    ctx={add(p,rot(z[:2],h))for z in G[target]['requirements']};hit=sorted(ctx&L);U0=center(p,h);U1=add(U0,rot((0,8),h))
    if hit:r.update(reason='permanent_source_L_star_context',hits=hit)
    elif contact(U0,U1,*source_segment):
     assert contact(U0,U1,*source_segment)==[['-1','5']]
     assert tuple(Fraction(U0[k])+Fraction(1,4)*(U1[k]-U0[k])for k in range(2))==(-1,5)
     r.update(reason='consumer_base_hits_source_U_strict_interior',base_start=U0,base_end=U1,contact_doubled=(-1,5),source_parameter='3/4',consumer_parameter='1/4')
    else:
     assert h==2 and(p,si)in[((-2,4),1),((-2,6),2)]
     t=Fraction(1,2)if si==1 else Fraction(1)
     assert tuple(Fraction(U0[k])+t*(U1[k]-U0[k])for k in range(2))==B
     assert contact(U0,B,B,A)==[['-3','5']]
     r.update(reason='Jordan_forces_Cgap2_below_true_input_minimum',base_start=U0,base_end=U1,consumer_parameter=str(t),contact_doubled=B,forced_C_age=2,signed_input_minimum=3 if si==1 else 5)
   rows.append(r)
counts=dict(Counter(r['reason']for r in rows));assert counts==dict(wrong_sector=30,permanent_source_L_star_context=23,consumer_base_hits_source_U_strict_interior=3,Jordan_forces_Cgap2_below_true_input_minimum=4)
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
D=[GP]+[W/p/'manifest.json'for p in['U_left_star_permanence_frozen_20261023_1918','U_entry_simplicity_frozen_20261023_1616','current_residual_barrier_frozen_20261023_1822','U_renewal_exact_clock_frozen_20261023_1902','chronology_dcuv/critical_ucc_count5/age_five_queries']]+[Path(__file__).resolve()]
R=dict(status='AUTHOR_RECYCLED_Q_U_RETURN_EXCLUSION_PENDING_INDEPENDENT_AUDIT',scope='Every genuine earlier U-family recycled-q output(-1,2) is excluded from all later U-family input slots in the same actual complete-eight factor. This is NOT a claim of permanence against D/V consumers. Current single-edge Jordan closure forces the only geometric candidates to have source-inclusive C age2, below their signed lower3/upper5 minima. No record, youngest-q, fixed excursion box or search cap.',normalized_source_q=q,source_midpoint=A,other_edge_endpoint=B,all_60_U_consumer_alignments=rows,counts=counts,source_partial_atom_and_tail_bridge_checks=source_prefix,bridge_join_turns_in_pi_over_4=joins,analytic_total_closed_turn='n*pi/2+pi',Jordan_forced_nonnegative_Cgap=2,dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(W/'chronology_dcuv/U_recycled_q_return.json').write_text(json.dumps(R,indent=2)+'\n');print(json.dumps(counts,indent=2))

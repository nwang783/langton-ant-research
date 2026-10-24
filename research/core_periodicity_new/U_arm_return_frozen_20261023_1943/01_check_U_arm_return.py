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
source_segment=((-1,-1),(-1,7));t=(1,2)
W0=(-1,3);L0=(1,1);T0=(3,3);X0=(1,5)
bridge=[X0,T0,L0,W0]
def edge(q):
 x,y=q
 return((2*x-1,2*y-1),(2*x+1,2*y+1))if(x+y)%2==0 else((2*x-1,2*y+1),(2*x+1,2*y-1))
assert set(edge(t))=={X0,T0};assert set(edge((1,1)))=={T0,L0};assert set(edge((0,1)))=={L0,W0}
rows=[]
for target in[7,8,9]:
 for h in range(4):
  for si,i in enumerate(G[target]['inputs']):
   p=sub(t,rot(i,h));r=dict(consumer=target,head=[*p,h],input_slot=si)
   if(sum(p)+h)%2:r['reason']='wrong_sector'
   else:
    ctx={add(p,rot(z[:2],h))for z in G[target]['requirements']};hit=sorted(ctx&L);U0=center(p,h);U1=add(U0,rot((0,8),h))
    if hit:r.update(reason='permanent_source_L_star_context',hits=hit)
    elif contact(U0,U1,*source_segment):r.update(reason='consumer_base_contacts_source_U',contact=contact(U0,U1,*source_segment))
    else:
     assert(target,p,h,si)==(7,(0,6),2,2);assert U1==X0
     for a,b in zip(bridge,bridge[1:]):assert contact(U0,U1,a,b)==([['1','5']]if a==X0 else[])
     r.update(reason='Jordan_Cgap6_plus_retired_upper_deadline',base_start=U0,base_end=U1,forced_C_age=6,other_upper_d=[0,3],d_signed_minimum=5,d_latest_producer_clock=1)
   rows.append(r)
counts=dict(Counter(r['reason']for r in rows));assert len(rows)==60;assert counts['Jordan_Cgap6_plus_retired_upper_deadline']==1
prefix=[]
for source in[7,8,9]:
 assert t in set(map(tuple,G[source]['outputs']));assert(0,3)in set(map(tuple,G[source]['inputs']));assert(0,3)not in set(map(tuple,G[source]['outputs']))
 p,h=run(G[7]['word']);P=center(p,h);assert P==(-1,7)
 for a,b in zip(bridge,bridge[1:]):assert contact(W0,P,a,b)==([['-1','3']]if b==W0 else[])
 tail=[]
 for k in range(G[source]['name'].count('C')):
  A0=center(p,h);p,h=run(Cword,p,h);B0=center(p,h)
  for a,b in zip(bridge,bridge[1:]):assert not contact(A0,B0,a,b)
  tail.append([A0,B0])
 prefix.append(dict(source=source,source_c=G[source]['name'].count('C'),endpoint=[*p,h],tail_chords=tail))
# Counterclockwise directions: source N2, consumer S6, closing SE7, SW5,NW3.
joins=[1,-2,-2,-1];assert sum(joins)==-4
zero_rows=[];turn_rows=[];out_rows=[]
for source in[0,4,7]:
 dx,dy,dh=G[source]['endpoint'];assert dh==0
 assert dx>=0 and dy>0 and dy-dx>=0
 wx,wy=rot((dx,dy),3);assert wy-wx>=0
 zero_rows.append(dict(source=source,N_endpoint=[dx,dy],N_y_increment=dy,N_H_increment=dy-dx,W_H_increment=wy-wx))
for source in[1,5,8]:
 dx,dy,dh=G[source]['endpoint'];assert dh==3 and dy-dx>=1
 turn_rows.append(dict(source=source,N_to_W_endpoint=[dx,dy],H_increment=dy-dx))
for source in[0,1,4,5,6,7,8,9]:
 out=list(map(tuple,G[source]['outputs']));assert min(y for x,y in out)>=0;assert min(x+y for x,y in out)>=0
 out_rows.append(dict(source=source,N_min_output_y=min(y for x,y in out),W_min_output_H=min(x+y for x,y in out)))
D=[GP]+[W/p/'manifest.json'for p in['U_left_star_permanence_frozen_20261023_1918','U_entry_simplicity_frozen_20261023_1616','current_residual_barrier_frozen_20261023_1822','U_renewal_exact_clock_frozen_20261023_1902','chronology_dcuv/critical_ucc_count5/age_five_queries']]+[Path(__file__).resolve()]
R=dict(status='AUTHOR_U_ARM_TO_U_RETURN_EXCLUSION_PENDING_INDEPENDENT_AUDIT',scope='A genuine earlier U-family output(1,2) cannot feed any later U-family input in the same complete-eight factor. This is NOT permanence against D/V. Permanent left-star plus current t gives a protected Jordan bridge forcing n6 in the sole remaining geometry. Its other upper d=(0,3) was retired by creator and cannot be reproduced by producer-clock1, whereas upper age5 requires that deadline. No record or historical-component premise.',counts=counts,all_60_consumer_alignments=rows,source_interface=prefix,bridge_doubled=bridge,join_turns_pi_over_4=joins,total_closed_turn='n*pi/2-pi',forced_nonnegative_Cgap=6,zero_C_endpoint_rows=zero_rows,one_C_turn_endpoint_rows=turn_rows,all_output_coordinate_bounds=out_rows,dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(W/'chronology_dcuv/U_arm_return.json').write_text(json.dumps(R,indent=2)+'\n');print(json.dumps(counts,indent=2))

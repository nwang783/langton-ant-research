"""Standalone all-future ray/parity verification of the common 11-cell tail trap."""
from pathlib import Path
import json,hashlib
OUT=Path(__file__).parent
D=((0,1),(1,0),(0,-1),(-1,0))
def rot(q,r):
 x,y=q
 for _ in range(r):x,y=y,-x
 return x,y

def geom(p,h,w):
 qs=[]
 for c in w:qs.append(p);h=(h+(1 if c=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 return qs,p,h

def mult(v,d):
 k=None
 for a,b in zip(v,d):
  if b:
   if a%b:return None
   r=a//b
   if k is not None and r!=k:return None
   k=r
  elif a:return None
 return k

def infinite(B,p,h,H):
 qs,p1,h1=geom(p,h,H);d=(p1[0]-p[0],p1[1]-p[1]);assert h1==h and d!=(0,0)
 tests=0
 for i,q in enumerate(qs):
  thresholds=[];epochs={0}
  for j,r in enumerate(qs):
   k=mult((r[0]-q[0],r[1]-q[1]),d)
   if k is not None and(k>0 or(k==0 and j<i)):thresholds.append(k);epochs.add(k)
  for r in B:
   k=mult((r[0]-q[0],r[1]-q[1]),d)
   if k is not None and k>=0:epochs|={k,k+1}
  for k in epochs:
   x=(q[0]+k*d[0],q[1]+k*d[1]);bit=(x in B)^(sum(j<=k for j in thresholds)%2)
   assert bit==(H[i]=='L'),(i,k,x,bit);tests+=1
 return qs,d,tests

def replay(B,p,h,w):
 B=set(B);seen=set();firstL=set()
 for i,c in enumerate(w):
  assert c==('L'if p in B else'R'),(i,p,c)
  if p not in seen and c=='L':firstL.add(p)
  seen.add(p)
  if c=='L':B.remove(p);h=(h-1)%4
  else:B.add(p);h=(h+1)%4
  p=(p[0]+D[h][0],p[1]+D[h][1])
 return B,p,h,seen,firstL

def hits(S,seen,qs,d):
 return {x for x in S if x in seen or any((k:=mult((x[0]-q[0],x[1]-q[1]),d))is not None and k>=0 for q in qs)}

if __name__=='__main__':
 data=json.loads((OUT/'TERMINAL_TRAP_CERTIFICATE.json').read_text());I=set(map(tuple,data['eleven_cell_source']));C=data['fixed_continuation'];H=data['period'];assert len(I)==11 and len(C)==278 and len(H)==104
 B,p,h,seen,firstL=replay(I,(0,0),2,C);qs,d,tests=infinite(B,p,h,H);assert firstL==I
 G={x for x in seen|set(qs)if x[1]>=-4};assert len(G)==63 and I<=G
 assert d==(2,-2)and max(y for x,y in qs)==-4
 assert all(x[1]<-4 or x in G for x in seen|set(qs))
 source=dict(finite_guard_cells=sorted(G),finite_guard_size=63,required_black_guard=sorted(I),required_white_guard=sorted(G-I),required_white_halfplane='y < -4',all_future_reads_outside_guard_in_white_halfplane=True,source=sorted(I),start_pose=[(0,0),2],prefix_duration=len(C),canonical_tail_pose=[p,h],canonical_tail_drift=d,after_prefix_black=sorted(B),ray_threshold_tests=tests,all11_initial_cells_consumed_in_prefix=True)
 baseline=json.loads((OUT/'THREE_POSITIVE_PASSES_CHECKED.json').read_text())['cases'];reg=json.loads((OUT/'REGENERATION_BOUNDARY_CHECKED.json').read_text())['cases'];out=[]
 for c,r in zip(baseline,reg):
  q=c['q'];B0=set(map(tuple,c['full_final_field']));p0,h0=tuple(c['final_pose'][0]),c['final_pose'][1]
  normalized={rot((x-p0[0],y-p0[1]),(2-h0)%4)for x,y in B0};assert min(y for x,y in normalized)>=-4 and normalized&G==I
  transI={tuple(a+b for a,b in zip(rot(x,(h0-2)%4),p0))for x in I};assert transI<=B0
  B,p,h,seen,_=replay(B0,p0,h0,C);qs,d,tests=infinite(B,p,h,H)
  touched=hits(B0,seen,qs,d);assert touched==transI
  A3={tuple(x)for x,o,b in c['full_final_lifetime_labels']if o=='third_positive_ordinary'};J3=set(map(tuple,r['next_direct_stitches']));A2={tuple(x)for x,b in c['remaining_second_lifetimes']}
  assert not hits(A3,seen,qs,d)and not hits(J3,seen,qs,d)
  out.append(dict(q=q,satisfies_pristine_halfplane_and_63_cell_guard=True,third_endpoint_pose=[p0,h0],current_black_ever_read_in_future=sorted(touched),ignored_black_archive_mass=len(B0-touched),entire_third_R_output_unread_forever=len(A3),next_q_minus_1_stitches_unread_and_white_forever=sorted(J3),second_R_boundary_lifetimes_used=sorted(hits(A2,seen,qs,d)),second_R_boundary_lifetimes_unread_forever=sorted(A2-hits(A2,seen,qs,d)),standard_tail_after_third=278,total_standard_tail_time=c['total_duration']+278,tail_pose=[p,h],tail_drift=d,full_tail_entry_black=sorted(B),ray_threshold_tests=tests))
  print({k:out[-1][k]for k in['q','ignored_black_archive_mass','entire_third_R_output_unread_forever','total_standard_tail_time','tail_pose','tail_drift']},flush=True)
 (OUT/'TERMINAL_TRAP_CHECKED.json').write_text(json.dumps(dict(status='AUTHOR all-future exact check, independent review requested',source=source,cases=out),indent=2)+'\n')

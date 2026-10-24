from pathlib import Path
from itertools import product
from collections import Counter,deque
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'MIDDLE_SHORT_COINCIDENT_FIRST_LAST_C_CORE.md';A=D/'middle_short_coincident_C_cycles_certificate.json'
assert sha(P).startswith('6a240f5a')and sha(A).startswith('1edb1fad')and sha(D/'certify_middle_short_coincident_C_cycles.py').startswith('9294dbc8');J=json.loads(A.read_text())
for f,h in J['dependencies'].items():assert sha(D/f)==h
N={};exec((S.parent/'check_drift31_refined_top_gap_independent.py').read_text().split("for line in(P/'DRIFT31_REFINED_TOP_ODD_GAP_SHA256SUMS')")[0],N)
graph,verify_rel,check_witness,rk,canon,oh=[N[k]for k in['graph','verify_rel','check_witness','rk','canon','o']]
words=['S','W','S','EEWE','SSNS','EEWE','NNNSS','EEEWW'];head='NESW';states=[{t:[head.index(h)for h in w]for t,w in enumerate(words)}];counts={};maxbounds={};total=0
for stage in J['stages']:
 t=stage['target_level'];assert t in[8,9,10];assert len(states)==stage['parent_count'];assert set(map(canon,states))=={canon({int(k):v for k,v in p['complete_parent'].items()})for p in stage['parents']};nxt=[];co=Counter();bounds=[]
 for p in stage['parents']:
  H={int(k):v for k,v in p['complete_parent'].items()};ih,I,out_h,O=(0,len(rk(H[t-3],0,True)),1,H[t-1].count(1))if t%2==0 else(3,len(rk(H[t-1],3,True)),2,H[t-3].count(2));bound=2*(I+O);bounds.append(bound)
  assert(p['incoming_heading'],p['incoming_total'],p['outgoing_heading'],p['outgoing_total'],p['derived_even_length_bound'])==(ih,I,out_h,O,bound)
  rel=verify_rel(H,t,p['all_physical_returns']);domain=[]
  # Independent complete binary words, not author's parity-position generator.
  for n in range(0,bound+1,2):
   for w in product((ih,(ih+2)%4),repeat=n):
    if w.count(ih)==I and len(rk(w,out_h,True))==O:domain.append(w)
  supplied=p['all_complete_count_domains'];assert set(domain)=={tuple(r['word'])for r in supplied}and len(domain)==len(supplied);total+=len(domain)
  for row in supplied:
   w=row['word'];kind=row['outcome'];co[kind]+=1
   if kind=='first_return_rank_mismatch':
    rr=row['witness'];q=p['all_physical_returns'][rr['physical_return_index']];a=rk(w,q['outgoing_heading'],True)[q['outgoing_ordinal']];b=rk(w,q['incoming_heading'])[q['incoming_ordinal']];assert(a,b)==(rr['source_rank'],rr['target_rank'])and b!=a+1
   else:
    assert all(rk(w,h2)[b]==rk(w,h1,True)[a]+1 for h1,h2,a,b,duration in rel);HH=H|{t:w};check_witness(HH,row)
    if kind=='open':
     su,ev,ch,seen,lev=graph(HH);assert ev==seen
     # An OPEN interface is merely unrejected, not an attained calendar/front.
     for seq in ch:
      prior={}
      for (z,r),k in seq:
       pt=-z+k*(3+1j)
       if pt in prior:assert r==prior[pt]+1
       prior[pt]=r
     nxt.append(HH)
 counts[t]=dict(co);maxbounds[t]=max(bounds);assert dict(co)==stage['domain_outcomes'];states=nxt
assert total==46+249+649 and len(states)==6
assert set(map(canon,states))=={canon({int(t):v for t,v in H.items()})for H in J['six_open_T0_through_T10_interfaces']}
old=json.loads((D/'drift31_middle_short_even_gap_discovery.json').read_text())['states'];assert set(map(canon,states))=={canon({int(t):v for t,v in H.items() if 0<=int(t)<=10})for H in old}
V=[1j,1,-1j,-1];off=[-1j,-1-1j,-1,0j];T=lambda p:int(3*p.imag-p.real);xy=lambda p:[int(p.real),int(p.imag)]
profiles=[];all_faces=[];period_paths=[]
def norm(z):a,s,n,p,c=z;return[a-p,s+p,n,c+18*p]
def add(a,b):return[x+y for x,y in zip(a,b)]
for H in states:
 su,events,chains,seen,levels=graph(H);w=H[8];nr=rk(w,0);assert nr[:2]==[0,1]and nr[2]in[3,5]and len(w)==8 and w[7]==2;assert rk(w,1,True)[0]==0 and rk(w,1,True)[-1]==7
 # Construct the actual 18-step full-voltage path from T7.R2 to T7.R0+d.
 e=(7,2);k=0;path=[(e,k)]
 while len(path)==1 or e!=(7,0):
  assert e in su;e,dk=su[e];k+=dk;path.append((e,k));assert len(path)<=19
 assert len(path)==19 and k==1;assert path[-2]==((8,0),1);period_paths.append([[list(e),k]for e,k in path])
 # Physical times satisfy a+P=s+18. No presumed calendar or chosen sheet.
 adj={}
 for e,(f,k)in su.items():
  adj.setdefault(e,[]).append((f,[0,0,0,-k,1]));adj.setdefault(f,[]).append((e,[0,0,0,k,-1]))
 vals={(7,0):[1,0,0,0,0],(7,2):[0,1,0,0,0],(8,nr[2]):[0,0,1,0,0]};queue=deque(vals)
 while queue:
  e=queue.popleft()
  for f,inc in adj.get(e,[]):
   q=add(vals[e],inc)
   if f in vals:assert norm(q)==norm(vals[f])
   else:vals[f]=q;queue.append(f)
 assert norm(vals[8,0])==[1,0,0,-1]and norm(vals[8,1])==[1,0,0,3]and norm(vals[8,7])==[0,1,0,-1]
 fs=[]
 for F in[-7-2j,-6-1j,-8-1j]:
  ff=[]
  for h in range(4):
   p=F-off[h];t=T(p);k=int(p.imag);assert t in H
   for r,hh in enumerate(H[t]):
    if hh!=h:continue
    tm=vals.get((t,r))
    if tm is not None:tm=add(tm,[0,0,0,k,0]);tm=norm(tm)
    else:assert(t,r,k)==(7,1,0)and F==-8-1j # a<T7.L1<s from actual complete ranks
    ff.append(dict(level=t,rank=r,lift=k,point=xy(p),heading=h,clock_a_s_n_constant=tm))
  fs.append(dict(face=xy(F),events=ff))
 assert[len(f['events'])for f in fs]==[6,8,10]
 assert sorted(tuple(e['clock_a_s_n_constant'])for e in fs[0]['events'])==[(0,1,0,i)for i in[2,3,4,5,6,14]]
 # C3's seven other clocks are s+7..s+11,s+15,s+16; its final T5.L3
 # follows T5.L1 at s+16 by >=4 on the same physical cell.
 assert sorted(tuple(e['clock_a_s_n_constant'])for e in fs[1]['events']if not(e['level']==5 and e['rank']==3))==[(0,1,0,i)for i in[7,8,9,10,11,15,16]]
 last3=next(e for e in fs[1]['events']if(e['level'],e['rank'])==(5,3));assert last3['clock_a_s_n_constant']==[-1,1,1,17]
 # C5's unknown T7.L1 lies between a and s; third N n precedes s-1.
 assert sorted(tuple(e['clock_a_s_n_constant'])for e in fs[2]['events']if e['clock_a_s_n_constant']is not None)==sorted([(1,0,0,i)for i in[-1,0,1,2,3]]+[(0,1,0,i)for i in[0,1,13]]+[(0,0,1,0)])
 # Selected last reads physically land on precisely the next C-cycle face.
 for F,t,r,k,G in[(-8-1j,4,3,-1,-7-2j),(-7-2j,3,3,-1,-6-1j),(-6-1j,5,3,0,-5+0j)]:
  p=-t+k*(3+1j);h=H[t][r];ho=oh(h,r);assert p+off[h]==F and p+V[ho]+off[ho]==G
 # Actual four-update carry, not a zero-identity switch.
 e=(4,3);k=-1;carry=[(e,k)]
 for _ in range(4):e,dk=su[e];k+=dk;carry.append((e,k))
 assert carry==[((4,3),-1),((3,3),-1),((6,2),0),((5,1),0),((8,0),1)];assert ''.join('R'if e[1]%2==0 else'L'for e,k in carry[:-1])=='LLRL'
 profiles.append(dict(T8=''.join(head[h]for h in w),third_N_rank=nr[2],n_upper_s_minus=1+4*(7-nr[2]),period_lower=18+4+4*6,face_spans=['12','P+n-s-8','P-4'],four_update_carry=[[list(e),k]for e,k in carry]));all_faces.append(fs)
prior=R/'audits/check_middle_short_three_C_cycle_independent.json';assert sha(prior)=='db18d1b72524d69fdc4d7dd56ea7b1280612e5aafa77579f97a6c8114436219e'
O=dict(status='PASS exact six-interface local cover and coincident three-face first/last C core; no branch exclusion',proof=sha(P),certificate=sha(A),script=sha(S),signed_first_cycle=sha(prior),domain_counts=counts,max_derived_even_bounds=maxbounds,complete_domains_checked=total,six_survivors=[{t:''.join(head[h]for h in w)for t,w in H.items()}for H in states],all_physical_face_clock_inventories=all_faces,profiles=profiles,actual_full_voltage_period_paths=period_paths,analytic_review=[
'The complete WHITE full middle-short odd inventory makes T8,T9,T10 even. Exact known ports derive n<=2(I+J), without a global visit cap. Independent complete binary-word enumeration yields46/249/649 domains, and every discarded domain has a rebuilt physical first-return mismatch, skipped-rank path or positive voltage clock cycle. The six necessary survivors equal the previously retained discovery set. Higher levels>=11 remain UNKNOWN.',
'In both surviving T8 words its first N is R0, second N L1, third N L3 orL5, final read S/L7. The literal successor path T7.R2 to T7.R0+d has18 updates and no invented connector, giving a+P=s+18. At this physical T8, L1=a+3 and L7=s-1; six consecutive read gaps each>=4 imply s-a>=28 and P>=46.',
'Every active read on all four corners of each C face is included. C1 has exactly six clocks s+2,3,4,5,6,14. C3 has seven clocks s+7..11,s+15,s+16 plus T5.L3=n+P-1, which is later than its own L1 at s+16. C5 has all10 reads, including unrestricted T7.L1 strictly between a ands; all are earlier than final T4.L3=s+13. Thus the maxima are COMPLETE faces, not cropped named-event maxima.',
'The already signed first cycle and the independently reconstructed last exit cycle use the same three distinct face classes. Last edges are T4.L3,T3.L3,T5.L3 with full displacement d. Positive gaps1,P+n-s-15,s-n+14 sum exactlyP. First L1 and last L3 events are distinct; there is no literal handoff or permitted splice.',
'Face spans are12,P+n-s-8,P-4. T8 third-N to L7 ordering yields n<=s-17 or s-9, so the middle span is <=P-25 orP-17. Positivity follows from its complete history. All three spans are<P; the actual last-C5 to next-first-C5+d carry is precisely four updates LLRL.',
'All six interfaces remain necessary open data, not full factors or controllers. The external P-15 interval and all higher ages are unrestricted. No full odd-inventory exclusion, lifetime-boundary type exclusion, forest connectivity, WHITE S1 or universal attraction is inferred. Coincident standard outer cycles remain a compatible positive warning.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(counts,maxbounds);print(sha(S.with_suffix('.json')))

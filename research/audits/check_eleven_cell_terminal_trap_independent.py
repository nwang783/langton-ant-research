from pathlib import Path
from collections import Counter
import hashlib,json
S=Path(__file__).resolve();R=S.parents[1];P=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();m=json.loads((P/'TERMINAL_TRAP_AUTHOR_MANIFEST.json').read_text())
for k,h in m['files'].items():assert sha(P/k)==h
for k,h in m['dependencies'].items():assert sha(P/k)==h
cert=json.loads((P/'TERMINAL_TRAP_CERTIFICATE.json').read_text());ref=json.loads((P/'TERMINAL_TRAP_CHECKED.json').read_text());third=json.loads((P/'THREE_POSITIVE_PASSES_CHECKED.json').read_text());regen=json.loads((P/'REGENERATION_BOUNDARY_CHECKED.json').read_text());V=(1j,1,-1j,-1);xy=lambda q:(int(q.real),int(q.imag));C=cert['fixed_continuation'];H=cert['period'];I={complex(*p)for p in cert['eleven_cell_source']};assert len(I)==11 and len(C)==278 and len(H)==104
std=json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];assert len(std)==104 and H in std+std

def replay(B,p,h,word,check=True):
 B=set(B);reads=[];old=set(B);consumed=set()
 for t,c in enumerate(word):
  reads.append(p)
  if check:assert c==('L'if p in B else'R'),(t,xy(p),c)
  if c=='L':
   if check:B.remove(p)
   else:B.discard(p)
   if p in old:old.remove(p);consumed.add(p)
   h=(h-1)%4
  else:B.add(p);h=(h+1)%4
  p+=V[h]
 return B,p,h,reads,consumed

def multiple(z,d):
 if d.real:
  if int(z.real)%int(d.real):return None
  k=int(z.real)//int(d.real)
 else:
  if z.real or int(z.imag)%int(d.imag):return None
  k=int(z.imag)//int(d.imag)
 return k if z==k*d else None

def tail(B,p,h):
 _,end,hh,qs,_=replay([],p,h,H,False);d=end-p;assert hh==h and d!=0;phase_cert=[]
 for i,q in enumerate(qs):
  # Every earlier occurrence at phasej is at epoch k-m for qj-qi=m*d.
  births=[]
  for j,z in enumerate(qs):
   m=multiple(z-q,d)
   if m is not None and(m>0 or m==0 and j<i):births.append(m)
  black_epochs={k for z in B if(k:=multiple(z-q,d))is not None and k>=0};cuts={0}|set(births)|black_epochs|{k+1 for k in black_epochs};tests=[]
  for k in sorted(cuts):
   parity=((k in black_epochs)+sum(m<=k for m in births))%2;assert parity==(H[i]=='L'),(i,k,xy(q+k*d),parity);tests.append((k,parity))
  # Constant on every interval between listed cuts, including the unbounded final interval.
  phase_cert.append({'phase':i,'earlier_occurrence_thresholds':sorted(births),'initial_black_epochs':sorted(black_epochs),'all_change_point_tests':tests})
 return qs,d,phase_cert

def ever(S,finite,qs,d):return {z for z in S if z in finite or any((k:=multiple(z-q,d))is not None and k>=0 for q in qs)}
B,p,h,reads,dead=replay(I,0j,2,C);assert(p,h)==(-9-5j,2)and dead==I;qs,d,tc=tail(B,p,h);assert d==2-2j;G={q for q in set(reads+qs)if q.imag>=-4};assert len(G)==63 and I<=G and len(G-I)==52
assert min(z.real for z in qs)==-9 and max(z.real for z in qs)==-1 and min(z.imag for z in qs)==-9 and max(z.imag for z in qs)==-4
assert {xy(z)for z in G}==set(map(tuple,ref['source']['finite_guard_cells']))and{xy(z)for z in G-I}==set(map(tuple,ref['source']['required_white_guard']))
results=[]
for c,rg,rr in zip(third['cases'],regen['cases'],ref['cases']):
 q=c['q'];assert q==rr['q'];B0={complex(*z)for z in c['full_final_field']};p0=complex(*c['final_pose'][0]);h0=c['final_pose'][1];rot=(-1j)**((2-h0)%4);norm={(z-p0)*rot for z in B0};assert min(z.imag for z in norm)>=-4 and norm&G==I
 source={p0+z/rot for z in I};B,p,h,reads,dead=replay(B0,p0,h0,C);assert source<=dead;qs,d,tc2=tail(B,p,h);touched=ever(B0,set(reads),qs,d);assert touched==source
 A3={complex(*z)for z,o,b in c['full_final_lifetime_labels']if o=='third_positive_ordinary'};A2={complex(*z)for z,b in c['remaining_second_lifetimes']};extra={complex(*z)for z in c['surviving_original_added_lifetimes']};J={complex(*z)for z in rg['next_direct_stitches']}
 assert not ever(A3,set(reads),qs,d)and not ever(J,set(reads),qs,d)and not(J&B0);use2=ever(A2,set(reads),qs,d);assert len(use2)==2 and len(A2-use2)==3 and extra<=dead and extra<=source
 own={'q':q,'total_standard_tail_time':c['total_duration']+278,'tail_pose':[list(xy(p)),h],'tail_drift':list(xy(d)),'ignored_black_archive_mass':len(B0-touched),'entire_third_R_output_unread_forever':len(A3)}
 for k,v in own.items():assert rr[k]==v
 assert {xy(z)for z in B}==set(map(tuple,rr['full_tail_entry_black']))and{xy(z)for z in use2}==set(map(tuple,rr['second_R_boundary_lifetimes_used']))
 own['exact_finite_guard_match']=True;own['phase_threshold_test_count']=sum(len(z['all_change_point_tests'])for z in tc2);results.append(own)
assert [z['total_standard_tail_time']for z in results]==[1357,2599,4321,6523]
out={'status':'PASS universal63-cell/pristine-half-plane sufficient capture criterion and all-future capture of FOUR supplied third-pass boards','bindings':m,'source_seed':sorted(map(xy,I)),'canonical_H_phase_in_retained_word':(std+std).index(H),'guard_size':63,'black_guard_size':11,'white_guard_size':52,'source_all104_exact_infinite_thresholds':tc,'four_complete_board_results':results,'analytic_review':[
'The eleven-cell finite seed executes the actual278-read prefix, consumes all eleven original identities, and enters the retained canonical104 cyclic word with headingS and drift(2,-2). Exact tail verification enumerates every physical phase-pair translation threshold and every initial-board ray intersection. Parity is constant between these finitely many change points and after the last one; no observed finite-repeat inference is used.',
'G contains exactly all prefix/first-tail read cells withy>=-4. First-tail footprint hasy<=-4, and every later copy translates down by2, hence liesy<=-6. Every future read outsideG is therefore in initially white half-plane y<-4. ANY board B contained in y>=-4 and agreeing withI onG has exactly the same entire future read field by first-difference induction, even if B has infinite mass in the unread half-plane. This is a sufficient boundary condition, not attraction to that condition.',
'All four full third-endpoint boards were normalized by proper rotation/translation, not cropped. They satisfy the entire half-plane condition and all63 guard bits. Independently replayed the prefix on those complete fields and verified all future ray parities again. Capture times1357/2599/4321/6523 are certified sufficient starts, not claimed minimal.',
'Only eleven currently black cells of each full endpoint ever enter the future read set. ALL third-R lifetimes101/231/409/635 and every missing next direct stitch are unread forever. Two of the five second-R boundary identities are consumed; the other three persist unread. The three old added-cycle survivors are genuinely consumed in the prefix. None of the archived material is deleted from the board.',
'The universal boundary criterion is analytic, but reachability by the guide/spiral family is certified ONLY for q3/5/7/9. No all-q construction, arbitrary architecture termination, regenerative loop, global finite-seed capture, or unbounded-gain theorem is inferred.'
]};S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])

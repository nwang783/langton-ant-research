"""Independent literal full-field and all-future debt audit. No author import."""
from pathlib import Path
import json, hashlib, collections, time
ROOT=Path('/workspace/shared/langton'); P=ROOT/'global_attraction_bridge_2026-10-24'; OUT=ROOT/'audits'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((P/'RETURN_PERMANENT_OUTPUT_DEBT_MANIFEST.json').read_text())
for group in ['files','retained_dependencies']:
 for f,h in manifest[group].items(): assert sha(P/f)==h,(f,sha(P/f),h)
J=json.loads((P/'RETURN_PERMANENT_OUTPUT_DEBT_CHECKED.json').read_text())
vec=(1j,1,-1j,-1)
def pair(z): return [int(z.real),int(z.imag)]
def zkey(z): return z.real,z.imag
def sim_seed(seed,h,N):
 B=set(seed);p=0j
 for t in range(N):
  black=p in B
  if black:B.remove(p)
  else:B.add(p)
  h=(h+(-1 if black else 1))%4;p+=vec[h]
 return B,p,h
G={-1j,1+1j,1+3j,2+2j}
def twenty(n):
 B=set()
 for p,h in [(0j,1),(n-1+n*1j,0),(-n+(3*n-4)*1j,3),(-5*n+5-n*1j,2),(-3*n+(-3*n+8)*1j,1)]:
  B.update(p+z*((-1j)**(h-1)) for z in G)
 assert len(B)==20
 return B
C,p,h=sim_seed(twenty(20),1,624*20-1516);assert (p,h)==(2j,1)
recovery={z-2j for z in C if z.real>=-16 and -14<=z.real+z.imag<=12};assert len(recovery)==90
seed={complex(*q) for q in json.loads((P/'MINIMAL_COHORT_RESTART_CHECKED.json').read_text())['initial_seed']}
jobs=[('four_cell_reference',G,1,390,()),('protected_recovery90',recovery,1,983,()),('defect14',seed,1,500,(44,46,52,58)),('filled15',seed|{-3-2j},1,500,()),('blank',set(),0,10081,())]
jobs += [(f'twenty_n{n}',twenty(n),1,624*n-1516+983,(60,)) for n in (20,80,400)]
def ray_k(delta,d):
 # Exact integer diagonal membership; complex parts are small integral floats.
 x,y=int(delta.real),int(delta.imag); dx,dy=int(d.real),int(d.imag)
 if x%dx: return None
 k=x//dx
 return k if y==k*dy else None

def verify_future(B,p,h):
 C=set(B);q=p;hh=h;pts=[];letters=[]
 for i in range(104):
  pts.append(q);b=q in C;letters.append('L' if b else 'R')
  if b:C.remove(q)
  else:C.add(q)
  hh=(hh+(-1 if b else 1))%4;q+=vec[hh]
 d=q-p;assert hh==h and abs(d.real)==abs(d.imag)==2
 total_checks=0
 for i,q in enumerate(pts):
  increments=collections.Counter()
  for j,r in enumerate(pts):
   m=ray_k(r-q,d)
   if m is not None and (m>0 or m==0 and j<i): increments[m]+=1
  board_hits=set()
  for z in B:
   k=ray_k(z-q,d)
   if k is not None and k>=0: board_hits.add(k)
  critical={0}|set(increments)|board_hits|{k+1 for k in board_hits}
  # Include every change boundary, and the final constant ray interval.
  for k in sorted(critical):
   colour=(int(k in board_hits)+sum(v for m,v in increments.items() if m<=k))%2
   assert colour==int(letters[i]=='L'),(i,k)
  total_checks+=len(critical)
 fates={}
 for z,ident in B.items():
  hits=[104*k+i for i,r in enumerate(pts) if (k:=ray_k(z-r,d)) is not None and k>=0]
  if hits:fates[ident]=min(hits)
 return ''.join(letters),d,fates,total_checks

def check_case(job,expected):
 name,seed,h,N,targets=job;started=time.time()
 assert name==expected['name'] and sorted(map(pair,seed))==expected['initial_black']
 B={z:-i-1 for i,z in enumerate(sorted(seed,key=zkey))};all_cells=dict((v,k) for k,v in B.items());birth={};death={};positions=[];heads=[];mass=[];turn=[];snap=None;p=0j
 for t in range(N):
  positions.append(p);heads.append(h);mass.append(len(B))
  if t==61:snap=dict(B)
  if p in B:
   death[B.pop(p)]=t;turn.append('L');h=(h-1)%4
  else:
   B[p]=t;birth[t]=p;all_cells[t]=p;turn.append('R');h=(h+1)%4
  p+=vec[h]
 positions.append(p);heads.append(h);mass.append(len(B))
 word,drift,fates,checks=verify_future(B,p,h)
 assert word==expected['terminal_word'] and pair(drift)==expected['terminal_drift']
 assert [pair(p),h]==expected['terminal_pose'] and checks==expected['all_period_parity_tests']
 death.update({ident:N+t for ident,t in fates.items()})
 terminal=[dict(cell=pair(z),lifetime=ident,first_future_read=death.get(ident)) for z,ident in sorted(B.items(),key=lambda r:zkey(r[0]))]
 assert terminal==expected['terminal_black']
 initial=[dict(cell=pair(z),lifetime=-i-1,death=death.get(-i-1)) for i,z in enumerate(sorted(seed,key=zkey))]
 assert initial==expected['initial_read_fates']
 assert [dict(cell=pair(z),lifetime=ident,death=death.get(ident)) for z,ident in sorted(snap.items(),key=lambda r:zkey(r[0]))]==expected['state61']
 L=[sum(i in death for i in range(-len(seed),0))];Pcount=[0];initial_permanent=len(seed)-L[0]
 for t,ch in enumerate(turn):
  L.append(L[-1]+(int(t in death) if ch=='R' else -1))
  Pcount.append(Pcount[-1]+int(ch=='R' and t not in death))
  assert mass[t+1]-L[-1]==initial_permanent+Pcount[-1]
 assert L[-1]==len(fates)
 # Independent explicit-coordinate extrema tree, earliest ties.
 xs=[int(z.real) for z in positions];ys=[int(z.imag) for z in positions]
 def join(a,b):
  if a is None:return b
  if b is None:return a
  return (a[0] if (xs[a[0]],a[0])<=(xs[b[0]],b[0]) else b[0],
          a[1] if (-xs[a[1]],a[1])<=(-xs[b[1]],b[1]) else b[1],
          a[2] if (ys[a[2]],a[2])<=(ys[b[2]],b[2]) else b[2],
          a[3] if (-ys[a[3]],a[3])<=(-ys[b[3]],b[3]) else b[3])
 size=1<<(N+1).bit_length();tree=[None]*(2*size)
 for i in range(N+1):tree[size+i]=(i,)*4
 for i in range(size-1,0,-1):tree[i]=join(tree[2*i],tree[2*i+1])
 def query(l,r):
  l+=size;r+=size+1;ans=None
  while l<r:
   if l&1:ans=join(ans,tree[l]);l+=1
   if r&1:r-=1;ans=join(ans,tree[r])
   l//=2;r//=2
  return ans
 M=max(L);counts=0;minimum=None;selected=[];delta=[0]*(N+1);excess=0;charged=0;large=0
 for b,q in birth.items():
  d=death.get(b)
  if d is None or d>N:continue
  a=b+1;ix=query(a,d)
  dist=lambda t:max(abs(xs[t]-q.real),abs(ys[t]-q.imag))
  D=int(max(map(dist,ix)));tau=min(t for t in ix if dist(t)==D)
  Pn=Pcount[d]-Pcount[a];lhs=Pn+L[a]+2*L[tau]+L[d]
  axis=0 if abs(xs[tau]-q.real)==D else 1
  coordinate=xs if axis==0 else ys
  hv=lambda t:int(vec[heads[t]].real if axis==0 else vec[heads[t]].imag)
  mu=lambda t:2*coordinate[t]-hv(t)
  exact=4+abs(mu(tau)-mu(a))+abs(mu(tau)-mu(d))
  assert lhs>=exact>=4*D
  row=dict(birth=b,death=d,cell=pair(q),age=d-b,peak_cut=tau,peak_pose=pair(positions[tau]),radius=D,permanent_births=Pn,relevant_at_birth=L[a],relevant_at_peak=L[tau],relevant_at_death=L[d],lhs=lhs,rhs=4*D,midpoint_rhs=exact,slack=lhs-4*D)
  counts+=1
  if minimum is None or row['slack']<minimum['slack']:minimum=row
  if b in targets:selected.append(row)
  if D>M:excess+=D-M;charged+=Pn;large+=1;delta[a]+=1;delta[d]-=1
 assert minimum==expected['minimum_slack_control'] and selected==expected['selected_returns']
 overlap=0;weighted=0;maxoverlap=0
 for t in range(N):
  overlap+=delta[t]
  if t in birth and t not in death:
   assert overlap<=L[t]<=M;weighted+=overlap;maxoverlap=max(maxoverlap,overlap)
 amort=dict(count=large,sum_radius_excess=excess,four_times_excess=4*excess,permanent_births_with_multiplicity=charged,maximum_permanent_birth_overlap=maxoverlap,upper_bound=M*Pcount[-1])
 assert charged==weighted and 4*excess<=charged<=amort['upper_bound']
 assert amort==expected['amortized_large_returns']
 assert counts==expected['checked_consumed_R_lifetimes'] and M==expected['relevant_mass_max'] and Pcount[-1]==expected['permanent_births_through_run']
 for t,v in expected['selected_mass_relevance'].items():
  t=int(t);assert v==dict(full=mass[t],relevant=L[t],permanent=Pcount[t])
 # Extra independent named linewise checks, not in author implementation.
 line_controls=[]
 for row in selected:
  b=row['birth'];d=row['death'];a=b+1;tau=row['peak_cut'];q=birth[b];D=row['radius'];axis=0 if abs(xs[tau]-q.real)==D else 1
  coord=lambda z:int(z.real if axis==0 else z.imag)
  peak=coord(positions[tau]);ea=coord(positions[a]);ed=coord(q)
  low=min(peak,ea,ed);high=max(peak,ea,ed)
  lines=[r for r in range(low+1,high) if (peak-r)*(ea-r)<0 and (peak-r)*(ed-r)<0]
  assert len(lines)>=max(0,D-2)
  relevant_lines=[]
  for cut in (a,tau,d):
   cc=collections.Counter(coord(z) for ident,z in all_cells.items() if ident in death and (ident<0 or ident<cut) and cut<=death[ident]);relevant_lines.append(cc)
   assert sum(cc.values())==L[cut]
  pp=collections.Counter(coord(z) for ident,z in birth.items() if a<=ident<d and ident not in death)
  line_min=None
  for r in lines:
   ll=pp[r]+relevant_lines[0][r]+2*relevant_lines[1][r]+relevant_lines[2][r]
   assert ll>=4;line_min=ll if line_min is None else min(line_min,ll)
  distinct=sum(pp[r]>0 for r in lines)
  assert distinct>=max(0,D-2-M)
  line_controls.append(dict(birth=b,axis=axis,strict_common_lines=len(lines),minimum_line_debt=line_min,lines_with_permanent_output=distinct,required_under_M=max(0,D-2-M)))
 r=dict(name=name,full_updates=N,completed_R_lifetimes=counts,all_future_parity_checks=checks,terminal_mass=len(B),initial_permanent_bits=initial_permanent,relevant_max=M,permanent_R_births=Pcount[-1],amortization=amort,selected=selected,linewise=line_controls,seconds=round(time.time()-started,3))
 print(json.dumps(r),flush=True);return r
results=[check_case(job,e) for job,e in zip(jobs,J['controls'])]
assert len(results)==8 and sum(r['full_updates'] for r in results)==322855 and sum(r['completed_R_lifetimes'] for r in results)==142797
report=dict(status='PASS: analytic theorem and independently reconstructed eight complete full-future controls',author_manifest_sha256=sha(P/'RETURN_PERMANENT_OUTPUT_DEBT_MANIFEST.json'),proof_sha256=sha(P/'RETURNING_LIFETIME_PERMANENT_OUTPUT_DEBT.md'),checker_sha256=sha(Path(__file__)),controls=results,scope='Retained axial transport applied to actual eventually-consumed lifetimes and actually permanent births. Entire C* cap and per-return permanent-output cap remain hypotheses. Conditional eventual nonzero translation is not canonical104 or global attraction.',reporting_qualification='Author selected_mass_relevance.permanent counts new permanent R births, not initially permanent cells. Full mass minus relevant mass equals initial permanent mass plus this counter at every cut.')
(OUT/'return_permanent_debt_independent.json').write_text(json.dumps(report,indent=2)+'\n')
print('PASS',sha(OUT/'return_permanent_debt_independent.json'))

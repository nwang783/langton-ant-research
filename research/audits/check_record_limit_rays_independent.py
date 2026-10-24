from pathlib import Path
from collections import defaultdict
import hashlib,json
S=Path(__file__);R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'RECORD_LIMIT_RAY_DEPENDENCY_MANIFEST.json'
assert sha(MF)=='857ef830b767ec907656a1fe34eb7bce1b17d83e89b88c3f956d31a56f2c8322';mf=json.loads(MF.read_text())
for group in ('files','dependencies'):
 for f,h in mf[group].items():assert sha(D/f)==h
J=json.loads((D/'RECORD_LIMIT_RAY_DEPENDENCY_CHECKED.json').read_text());src=json.loads((D/'RECORD_GAP_COMPACTNESS_CHECKED.json').read_text());ns={'__file__':str(S.with_name('check_phase13_double_scatter_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Canonical source')[0],ns);geometry,sim,cert,xy,V=[ns[k]for k in('geometry','sim','cert','xy','V')]
seed={complex(*q)for q in src['limit']['seed']};prefix=src['limit']['finite_prefix'];w=J['tail_word'];L=len(prefix);assert L==2762==J['prefix_length'];z=cert(sim(seed,L,0j,0,prefix),w);Q,H,end,hh=geometry(z['p'],z['h'],w);d=end-z['p'];assert d==-2-2j

def mult(v,d):
 k=v.real/d.real
 return int(k)if k==int(k)and v==int(k)*d else None

def class_stable(qs,d):
 hist=defaultdict(list)
 for i,q in enumerate(qs):
  k=(int(q.real)//abs(int(d.real)))*(1 if d.real>0 else-1);r=q-k*d;hist[r].append((i-104*k,i,k))
 return sorted(min(ls)[1]for ls in hist.values())
stable=class_stable(Q,d);assert len(stable)==22 and all(w[i]=='R'for i in stable);threshold=0
for i,q in enumerate(Q):
 row=J['all_104_phase_witnesses'][i];assert row['phase']==i and row['stable_first_visit']==(i in stable)
 if i not in stable:
  a,m=row['earlier_phase'],row['earlier_period_offset'];assert q==Q[a]+m*d and 104*m+a<i;threshold=max(threshold,-m)
 else:
  periods=[k for p in set(z['pts'])|seed if (k:=mult(p-q,d))is not None and k>=0];last=max(periods,default=None);threshold=max(threshold,(last if last is not None else-1)+1)
  assert row['finite_prefix_seed_last_period']==last and row['ray_anchor']==xy(q) and row['normal_depth_offset']==-q.imag and row['delay_depth_constant']==L+i+52*q.imag
assert threshold==J['stable_threshold']==1
cyclic=[]
for row in J['all_cyclic_first_visit_inventories']:
 shift=row['shift'];ww=w[shift:]+w[:shift];qq,_,dd,eh=geometry(0j,1,ww);assert eh==1 and abs(dd.real)==abs(dd.imag)==2
 stable2=class_stable(qq,dd);assert stable2==row['stable_first_visit_phases'] and len(stable2)==22 and all(ww[i]=='R'for i in stable2)
 # Every nonstable phase must have an earlier actual visit beyond reported fringe.
 bound=row['finite_fringe_period_bound']
 for i,q in enumerate(qq):
  if i in stable2:continue
  assert any((m:=mult(q-v,dd))is not None and 104*m+a<i and bound+m>=0 for a,v in enumerate(qq))
 seen=set();required=[]
 for k in range(bound+1):
  for i,q in enumerate(qq):
   p=q+k*dd
   if p not in seen and ww[i]=='L':required.append(xy(p))
   seen.add(p)
 assert required==row['required_initial_black'] and 11<=len(required)<=22
 cyclic.append(dict(phase=shift,stable_count=22,firstL_fringe=len(required),certified_fringe=bound))
assert len(cyclic)==104
# Exact first hit on the full extra current field, independent of the comparison emitter.
first={}
for t,q in enumerate(z['pts']):first.setdefault(q,t)
def hit(extra):
 candidates=[]
 for p in extra:
  if p in first:candidates.append((first[p],p))
  for i,q in enumerate(Q):
   k=mult(p-q,d)
   if k is not None and k>=0:candidates.append((L+104*k+i,p))
 return min(candidates,key=lambda t:t[0])if candidates else None
controls=[];total=0
for row in J['controls']:
 n=row['n'];sr=next(q for q in src['controls']if q['n']==n);p=complex(*sr['last_N_pose'][0]);B={complex(*q)-p:i for q,i in sr['whole_last_N_black']};assert seed<=set(B)
 t,q=hit(set(B)-seed);k,i=divmod(t-L,104);assert(t,q,k,i)==(104*n+2134,-2*n-27+(-2*n-33)*1j,n-7,100)and i in stable
 assert t==52*(-q.imag)+418 and B[q]==20165
 field=dict(B);head=0j;heading=0;expected=prefix+w*k+w[:i];assert len(expected)==t
 for s,c in enumerate(expected):
  old=field.pop(head,None);assert (old is not None)==(c=='L')
  if old is None:field[head]=10**12+s
  heading=(heading+(1 if c=='R'else -1))%4;head+=V[heading]
 assert head==q and field[q]==20165 and w[i]=='R'
 age=sr['last_N_record_cut']+t-B[q];depth=int(-q.imag);assert age==208*n+11640 and age>=53*depth+418
 assert row==dict(n=n,full_record_black_mass=len(B),extra_mass=len(B)-len(seed),first_contact_delay=t,cell=xy(q),normal_depth=depth,tail_phase=i,tail_period=k,old_record_lifetime_birth=20165,consumption_age=age,age_geometric_lower_bound=53*depth+418,physical_prefix_reads=t)
 controls.append(row);total+=t
assert total==83050
O=dict(status='PASS conditional canonical trapped-record-limit old-input ray dependency only',manifest=sha(MF),script=sha(S),canonical_phases=104,stable_first_visit_rays=22,firstL_fringe_range=[min(z['firstL_fringe']for z in cyclic),max(z['firstL_fringe']for z in cyclic)],specified_limit_threshold=1,controls=controls,full_current_field_reads=total,analytic_review=[
'For each of104 cyclic canonical words, stable first visits are independently recovered as minimum canonical times of FULL drift read classes, not inferred from bounded simulation. Exactly22 phases qualify and all areR. Each other phase has an explicit earlier phase/period witness; exhaustive finite fringe firstL sites number11..22. Thus arbitrary-support initial fields realizing a lengthL prefix plus canonical tail have at most L+22 initiallyBLACK future-read sites. Prefix modifications only remove possible first-L inputs from this bound, never add more thanL.',
'Deleting every never-read initiallyBLACK site gives the finite K with the exact same entire future, even when the original support is infinite. This does not imply finite total required exposure: infinitely many WHITE old-side sites can matter. Local convergence eventually includes every cell of finite K with its BLACK color. For full returning record states, a first reference read of extra initialBLACK must occur, else their whole future equals the never-returning limit.',
'At that first discrepancy the reference reads the cell for the first time and prescribesR, while the actual old-at-record BLACK lifetime is consumed byL. No birth during the coincident comparison can create this difference. Finite-prefix continuity makes discrepancy times diverge; a bounded cell has a fixed first read time, so positions escape every bounded box. Eventually they are on the22 stable rays; subselection fixes a phase and sends its period index to infinity.',
'Because the reference never crosses the record line, a rotated canonical axis projection cannot be+2 and is therefore-2. Exact s=-a.q_i+2k and u=L+i+104k give u=52s+c_i. For an R-born current input the unit-speed path from birth cell to record head gives elapsed age>=s, hence complete age>=53s+c_i. In ONE fixed finite orbit, all ever-consumed original identities retire by a finite cut; late selected inputs areR-born, and unbounded death times admit a distinct-identity subsequence. Across seeds this distinctness is not inferred.',
'The signed MT northern limit has finite296 pruning, prefix2762 and stable threshold1. Three complete current fields are retained for83050 exact updates before their first added-black collision at phase100,k=n-7,cell(-2n-27,-2n-33). The consumed SAME physical identity is genuine M R9752 at absolute20165; delay104n+2134=52depth+418 and full age208n+11640 reconstruct.',
'This is a necessary conditional dependency under a canonical trapped limit, not proof that such a limit occurs, that dependencies nest, lie in a fixed physical band, add costs injectively, or cannot regenerate indefinitely. Every named finite control captures. Unrestricted record-limit classification, outward-limit occurrence and universal attraction remain open.'
]);S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))

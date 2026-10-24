from pathlib import Path
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'kernel_cycle_lift_2026-10-24';src=R/'reframe_finite_seed_2026-10-24/cap7_structure_probe.json';ns={'__file__':str(SELF)};exec((SELF.parent/'check_cycle_birth_finite_fuel_independent.py').read_text().split('cells=')[0],ns)
component,step,wvertex,ends=[ns[k]for k in('component','step','wvertex','ends')]
def xy(q):return(int(q.real),int(q.imag))
def key(S):return sorted(map(xy,S))
def trans(S,p,h):return{p+complex(*q)*(-1j)**h for q in S}
J=json.loads(src.read_text())['cycle_witness'];assert J['word']=='RRLLLL'and len(J['transitions'])==6
seed={-1-1j,-1+0j,1-1j,2-1j,2+0j};B=set(seed);p=0j;h=0;trace=[];deaths={};initialC={1-1j,2-1j,2+0j}
for tick in range(13):
 C=component(B,0,wvertex(p,h))[1];z=2*p+(-1-1j)*(-1j)**h;Z=component(B,2,z)[1];trace.append({'cut':tick,'pose':[xy(p),h],'board':key(B),'w':key(C),'z':key(Z)})
 if tick<6:
  t=J['transitions'][tick];assert C==trans(t['input_component'],p,h)
  before=set(B);pp,hh=p,h
  p,h,c=step(B,p,h);assert c==t['turn'];N=component(B,0,wvertex(p,h))[1]
  assert N==trans(t['output_active'],pp,hh)
  assert B-N==set() # imported old dimer and current part comprise all after first R
  if c=='L':deaths[pp]=tick
 elif tick<12:
  pp=p;p,h,c=step(B,p,h);assert c==J['word'][tick%6]
  if c=='L':deaths[pp]=tick
assert max(len(t['w'])for t in trace[:7])==7
assert trace[6]['pose']==[(1,-1),2]
assert set(complex(*q)for q in trace[6]['board'])=={-1-1j,-1+0j,0j}
assert set(B)=={1-1j}and len(trace[7]['w'])==4
next_import=trans(J['transitions'][0]['imported_component'],1-1j,2);assert next_import=={2-1j,2+0j};assert deaths[2-1j]==3 and deaths[2+0j]==4
# Independently collect every complete-port initial-bit constraint of the prescribed double profile.
p=0j;h=0;parity=set();constraints={};conflicts=[];specific=[]
T=J['transitions']*2
for tick in range(13):
 if tick<12:C=trans(T[tick]['input_component'],p,h)
 else:C=trans(J['transitions'][0]['input_component'],p,h)
 V={wvertex(p,h)}|{v for q in C for v in ends(q,0)};ports={(v+dd)/2 for v in V for dd in[1+1j,1-1j,-1+1j,-1-1j]}
 for q in ports:
  bit=(q in C)^(q in parity)
  if q==2-1j:specific.append((tick,int(bit)))
  if q in constraints and constraints[q][0]!=bit:conflicts.append((xy(q),constraints[q][1],tick,int(constraints[q][0]),int(bit)))
  constraints.setdefault(q,(bit,tick))
 if tick<12:parity.symmetric_difference_update({p});h=(h+(1 if T[tick]['turn']=='R'else-1))%4;p+=1j*(-1j)**h
assert(0,1)in specific and(7,0)in specific and conflicts
files=[src,D/'CAP7_NONEMPTY_CORE_DOUBLE_LOOP_OBSTRUCTION.md',D/'cap7_nonempty_cycle_certificate.json',D/'finite_general_component_profile_lift.py']
out={'status':'PASS supplied cap7 nonempty six-transition profile is singly physical but cannot repeat immediately','dependencies':{str(f.relative_to(R)):hashlib.sha256(f.read_bytes()).hexdigest()for f in files},'actual_double_literal_trace':trace,'next_required_import':key(next_import),'specific_deleted_cell_initial_bit_requirements':specific,'all_double_profile_conflicts':conflicts,'analytic':['The five-cell full board realizes every exact first-loop active component. At firstR the complete old dimer imports; R1 closes a cycle, L2 erases it, and L3/L4 destroy the two cells needed as the NEXT imported dimer. No passive component is emitted.','The actual seam pose is(1,-1,S), so the next required dimer is fixed at(2,-1),(2,0), not freely repositionable. Both were physically deleted and remain unread before the next firstR. Complete-field constraints consequently require the same initial cell(2,-1) BLACK atcut0 and WHITE atcut7. No additional unread exterior can repair an already deleted physical cell.','As an adversarial control, RRLLLL twice is a valid literal execution of the same five-cell board. Its second firstR has active mass4 rather than prescribed6, and the full output after12updates is singleton(1,-1). Thus the obstruction concerns exact full-state profile recurrence, not the word, rotation, or a false two-loop color conflict.'],'scope':'Only six supplied transitions and their actual fields are certified. No full cap7 kernel/SCC coverage, cap7 exit, return grammar or capture conclusion.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])

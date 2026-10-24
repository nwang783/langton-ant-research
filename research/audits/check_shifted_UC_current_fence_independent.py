from pathlib import Path
from fractions import Fraction
from collections import deque
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'returned_D_UC_current_fence_guards_2026-10-24';ns={'__file__':str(SELF)};exec((SELF.parent/'check_foreign_kinked_barrier_turn_independent.py').read_text().split('geometries=[]')[0],ns)
W,M,walk,xy=[ns[k]for k in('W','M','walk','xy')]
def at(q,p,h):return p+q*(-1j)**h
def center(p,h):return 2*p+(-1-1j)*(-1j)**h
def edge(q):return (2*q-1-1j,2*q+1+1j)if int(q.real+q.imag)%2==0 else(2*q-1+1j,2*q+1-1j)
def cross(a,b):return int(a.real*b.imag-a.imag*b.real)
def meet(a,b,c,d):
 u=b-a;v=d-c;w=c-a;den=cross(u,v)
 if den:
  s=Fraction(cross(w,v),den);t=Fraction(cross(w,u),den);return 0<=s<=1 and 0<=t<=1
 if cross(w,u):return False
 k=(lambda z:int(z.real))if u.real else(lambda z:int(z.imag));lo,hi=sorted([Fraction(k(c-a),k(u)),Fraction(k(d-a),k(u))]);return max(0,lo)<=min(1,hi)
cat=json.loads((R/'seven_word_spatial_return_2026-10-23/first_returned_atom_contact.json').read_text())['old_source_contact_cases'];rows=[]
for ix,label,cycle in[(15,'DDD',False),(15,'V',False),(30,'DD',False),(15,'DD',True),(30,'D',True)]:
 run=walk(''.join(W[c]for c in label));H=int(run['p'].imag);x=int(run['p'].real);p=-5-x-H*1j;h=1
 uc=walk(W['U']+W['C']);assert at(uc['p'],p,h)+run['p']==0 and(uc['h']+h)%4==0
 source=walk(W['U']);star={at(q,p,h)for q in[0j,1j,1+0j,1+1j]};Z={at(q,p,h)for q in[1+0j,1+1j,2+0j,2+1j]};held=star|Z if cycle else star
 # Own C does not read these original output identities again.
 for q in [0j,1j,1+0j,1+1j]+([2+0j,2+1j]if cycle else[]):
  br=[(t,c)for t,(z,hh,c)in enumerate(source['reads'])if z==q];full=[(t,c)for t,(z,hh,c)in enumerate(uc['reads'])if z==q];assert br==full and br[-1][1]=='R'
 C=cat[ix];fp=complex(*C['foreign_pose'][:2]);rp=complex(*C['returned_pose'][:2]);rh=C['returned_pose'][2];L=-9 if ix==15 else-7
 combined=walk(W['F']+W[C['returned_atom']]+M);assert combined['feasible'];foot={at(q,fp,1)for q in combined['req']};assert not held&foot
 fs=center(fp,1);fe=center(rp,rh);assert fe==at(-7-3j,2*fp,1);contact=-1-1j if ix==15 else 0j
 for q in held:
  a,b=edge(q);assert not meet(a,b,fs,fe)and not meet(a,b,fe,contact)
 adj={}
 for q in held:
  a,b=edge(q);adj.setdefault(a,[]).append((b,q));adj.setdefault(b,[]).append((a,q))
 start=center(p,1);assert start in adj;low=min(adj,key=lambda z:(z.imag,z.real));assert low.imag==L
 prev={start:None};todo=[start]
 for a in todo:
  for b,q in adj[a]:
   if b not in prev:prev[b]=(a,q);todo.append(b)
 assert low in prev;verts=[low];cells=[];v=low
 while prev[v]is not None:v,q=prev[v];verts.append(v);cells.append(q)
 gate=at(3-1j,p,1)
 if cycle:assert gate.imag==fp.imag and fp.real-gate.real==10
 rows.append({'case':ix,'Nrun':label,'UCentry':xy(p),'uses_cycle':cycle,'center_inside':xy(start),'support':L,'held':sorted(map(xy,held)),'path_vertices':list(reversed(list(map(xy,verts)))),'path_cells':list(reversed(list(map(xy,cells)))),'gate':xy(gate)if cycle else None})
A=json.loads((D/'D_UC_current_fence_guards.json').read_text());assert len(A['five_exact_current_fence_guards'])==len(rows)
for a,b in zip(rows,A['five_exact_current_fence_guards']):assert(a['case'],a['Nrun'],a['UCentry'],a['held'])==(b['catalogue_id'],b['following_actual_N_run'],tuple(b['UC_entry'][:2]),list(map(tuple,b['held_cells'])))
mp=D/'manifest.json';mf=json.loads(mp.read_text())
for f in mf['files']:assert hashlib.sha256((D/f['file']).read_bytes()).hexdigest()==f['sha256']
for f,h in A['dependencies'].items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==h
out={'status':'PASS five shiftedUC current-edge support contradictions','manifest_sha256':hashlib.sha256(mp.read_bytes()).hexdigest(),'five_current_paths':rows,'analytic':['The signed first-contact Jordan horizon puts the entire strictly earlier connected center prefix inside the CCW loop, including the actual creating-U start. Its whole boundary has doubled y>=L, so no bounded-interior point can have y<=L. This is the first-contact scope, not a general returned-path simplicity theorem.','Each displayed original U-star is a connected graph of SAME currently residual output edges containing that earlier U start. Three cases already reach the exact support line. The source UC own tail preserves all those identities. The signed current-edge barrier forbids every later old-eight atomic boundary contact while they remain residual; it includes endpoint contacts, since an incident endpoint edge would be active core, not residual.','For the two cases requiring original cycle edges, the only possible first breaker is the signed right U-family gate at exact source-entry age4, hence selectedD clock3. A complete positive tail would finish after the clock3 foreign, so the breaker must be plainU. Its entry and F have equal y and horizontal gap10. Every further E D/V strictly lowers y; only U strides4 could connect, including the breaker itself. Ten is not a positive multiple of4, so the original cycle has not broken. No blanket cycle permanence is assumed.','For all five connected held graphs, exact full F+returned+M footprint misses every SAME identity, and exact rational edge intersections with the actual F and returned-first-contact segments are empty. Thus these particular identities physically survive the new pieces, without importing an old-language postforeign age law.','A continuous held-edge path starting inside and ending on the supporting line must intersect the Jordan boundary. Old-boundary intersections are barred by current residual status; both new pieces were checked directly. This contradiction removes exactly the five listed UC boundary/run cases. No historical connector, vanished birth edge, extra core wire, cycle fuel, or global closure is used.'],'scope':mf['scope'],'dependencies':A['dependencies']}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])

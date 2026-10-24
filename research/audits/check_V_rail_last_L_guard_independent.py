from pathlib import Path
from itertools import product
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'seven_word_spatial_return_2026-10-23';p=SELF.with_name('check_foreign_kinked_barrier_turn_independent.py');ns={'__file__':str(p)};exec(p.read_text().split('geometries=[]')[0],ns)
W,M,walk,xy=[ns[k]for k in('W','M','walk','xy')]
def footprint(w):
 p=0j;h=0;out=[]
 for t,c in enumerate(w):
  out.append((p,c,t));h=(h+(1 if c=='R'else-1))%4;p+=1j*(-1j)**h
 return out,p,h
V,ve,vh=footprint(W['V']);VCC,te,th=footprint(W['V']+W['C']*2);assert(ve,vh)==(1+3j,0)and(te,th)==(4j,2)
def hits(seq,c,reverse=False):
 # Equality x=d directly derives the full integer domain from every actual read, no radius scan.
 H={}
 for p,ch,t in seq:
  d=int(p.real)
  if p.imag==(3*d+4-c if reverse else 3*d+c)and(not reverse or d>=1):H.setdefault(d,[]).append((ch,t))
 return H
interfaces=[]
for a,c,tick in[('D',3,11),('U',2,12)]:
 f=hits(V,c);tail=hits(VCC,c);rev=hits(V,c,True)
 assert f==({-1:[('L',1)]}if a=='D'else{-1:[('L',2)],0:[('R',12)]})
 assert{d:hs for d,hs in tail.items()if d<=0}==({-1:[('L',1)],0:[('L',19)]}if a=='D'else{-1:[('L',2)],0:[('R',12),('L',20)]})
 assert not rev
 g=1j if a=='D'else 2j;seq,_,_=footprint(W[a]+M);reads=[(ch,t)for q,ch,t in seq if q==g];assert reads[0]==('L',tick)
 interfaces.append({'next_base':a,'c':c,'forward':f,'VCC':tail,'previous_reverse_contacts':rev,'first_goal_read':reads[0]})
 # Exact full histories cover the actual first-deletion identity at domain corners and an interior pair, as corroboration only.
 for r,j in[(0,0),(0,1),(1,0),(1,1),(1,2),(17,0),(17,8),(17,18)]:
  raw=W['V']*r+W['V']+W['C']*2+W['V']*j;seq,p,h=footprint(raw);n=r-j;victim=n+(3*n+c)*1j
  assert(p,h)==(n+(3*n+4)*1j,2)
  rr=[(ch,t)for q,ch,t in seq if q==victim];assert rr[-1]==('L',18*n+(19 if a=='D'else 20))
  proposed,_,_=footprint(W[a]+M);assert p+g*(-1j)**h==victim
  tr=walk(raw+W[a]+M);assert not tr['feasible']and tr['i']==len(raw)+tick
# Exact genuine finite controls and the newly unread root.
old=json.loads((D/'ordered_W_seal_withdrawal_controls.json').read_text())['controls'];positive=[]
for z in old:
 w=''.join(W[a]for token in z['full_packet_sequence']for a in token)+M;B={complex(*q)for q in z['complete_finite_seed']};p=0j;h=0
 for ch in w:
  assert(p in B)==(ch=='L');B.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;p+=1j*(-1j)**h
 positive.append({'tokens':z['full_packet_sequence'],'seed_mass':len(z['complete_finite_seed'])})
raw=W['U']+W['V']*2+W['C']*2+W['V']*3;word=raw+M;tr=walk(word);assert tr['feasible']and len(raw)==148
seed={q for q,(black,t)in tr['req'].items()if black}if isinstance(next(iter(tr['req'].values())),tuple)else{q for q,b in tr['req'].items()if b}
# walk's req is the exact before-color Boolean map.
assert len(seed)==17
oldseed={complex(*q)for q in old[0]['complete_finite_seed']};assert seed-oldseed=={-2+3j}and oldseed<=seed
B=set(seed);p=0j;h=0;qr=[];newreads=[]
for t,ch in enumerate(word):
 assert(p in B)==(ch=='L')
 if p==-1+2j:qr.append((ch,t))
 if p==-2+3j:newreads.append((ch,t))
 B.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;p+=1j*(-1j)**h
assert qr==[('L',13),('R',21),('L',149)]and newreads[0]==('L',143)
oldword=''.join(W[a]for tok in old[0]['full_packet_sequence']for a in tok)+M;assert all(q!=-2+3j for q,c,t in footprint(oldword)[0])
# Derive endpoint equations directly from symbolic affine coefficients in(a,r), no bounded count search.
eps={a:footprint(W[a])[1]for a in'DVU'};assert eps=={'D':1+1j,'V':1+3j,'U':4j}
endpoint=[]
for a,X,Y,off in[('F',2,-5,0),('Q',4,-5,1),('B',5,-4,2)]:
 # E displacement=(d+3v+4u,-d-v); target-minus-Estart=(a+3r+X+4,-a-r+Y-1).
 assert X+Y+3==2*off
 dc=1-Y-off;assert dc>=3
 endpoint.append({'foreign':a,'V_plus_2U_offset':off,'D_plus_V_offset':1-Y,'D_lower_constant':dc})
def checkmanifest(file):
 p=D/file;j=json.loads(p.read_text());f=j['files']
 if isinstance(f,list):
  for z in f:assert hashlib.sha256((D/z['file']).read_bytes()).hexdigest()==z['sha256']
 else:
  for n,h in f.items():assert hashlib.sha256((D/n).read_bytes()).hexdigest()==h
 return hashlib.sha256(p.read_bytes()).hexdigest()
m1=checkmanifest('V_rail_forced_reverse_block_manifest.json');m2=checkmanifest('V_rail_no_further_C_scope_clarification_manifest.json')
out={'status':'PASS one-next-base all-length last-L guard and C3 endpoint corollary WITH mandatory no-further-C clarification','manifest_sha256':m1,'mandatory_scope_clarification_sha256':m2,'fresh_affine_interfaces':interfaces,'original_regressions':positive,'new_positive_17_seed':sorted(map(xy,seed)),'new_positive_reads':len(word),'new_root_reads':newreads,'original_U_q_reads':qr,'endpoint_identities':endpoint,'analytic':['For g=(r-j,3(r-j)+c), forward-copy equality reduces exactly to(d,3d+c), with d=r-j-i. Literal footprints enumerate every possible integer d by its actual x coordinate. For j>=1 the final L is at copy i=r-j+1 (plainV or terminalVCC); for j0 it is in VCC C1. The n=-1 endpoint is the first packet actual core L, not a negative-index source. All later forward slots and all earlier reverse copies are excluded by the same complete footprint identities.','Thus for every r>=0,0<=j<=r+1 both victims have lastL at18(r-j)+19/+20 and no later read. Proposed D/U firstL is context11/RAW12, giving an immutable repeatedL contradiction on any initial field. D11 is actual next-word tick1/read2 (or an ownedCtail in DC), not D RAW; U12 is ownRAW read13.','The original note iteration was overbroad without a no-additional-C condition. The mandatory separate clarification restricts the r+2 PLAIN reverse-V consequence to no furtherC before firstD/U. The one-next-base guard itself is unchanged. VC/VCC heading changes are not silently ruled out by that guard.','For the C3 application W=D^a V^r VCC has a>=1 and spends the two remainingCs, so S is empty and E starts(-a-3r-4,1+a+r). The exact equations v+2u=r/r+1/r+2 and d+v=a+r+6/a+r+6/a+r+5 force d>0. Since noCs remain, firstD/U must follow>=r+2Vs. F/Q total weight is insufficient; B consumes all allowed weight, leaving noU despite actual last-before-B requiringU. This excludes exactly the stated all-length W subfamily.','Both genuine withdrawn-seal controls replay unchanged. The exact new17-black U,V,VCC,V,V,V+actualM11 has159 physical reads; its sole addedroot(-2,3) was unread in the old16-black prefix and firstreadsL143. OriginalUq readsL13,R21,L149, with finalmarker retirement nextwordread2. No seed clipping or source-free positive is used.'],'scope':'No mixed-W, additional-C reverse-run, arbitrary S-stage, whole-ledger contraction, second-foreign or five-target closure. Withdrawn6ea48d5 remains withdrawn.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])

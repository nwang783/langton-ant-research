from pathlib import Path
from itertools import product
import hashlib,json
S=Path(__file__).resolve();R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for l in (D/'TIME_GATE_SHA256SUMS').read_text().splitlines():h,p=l.split(None,1);assert sha(R/p)==h
ref=json.loads((D/'check_overlap_twelve_gate.json').read_text());V=(1j,1,-1j,-1);tables=[]
for side in ['target','source']:
 for gap in [4,8]:
  count=0;geoms=[]
  for seq in product('RL',repeat=gap):
   w=''.join(seq)
   if side=='target'and(w[0]!='R'or w[-1]!='R'):continue
   if side=='source'and w[:2]!='RL':continue
   count+=1;p=0j;h=0;rd=[]
   for t,c in enumerate(w):rd.append((t,p,h,c));h=(h+(1 if c=='R'else-1))%4;p+=V[h]
   if p!=0 or h!=(2 if side=='target'else 0):continue
   colors={};conflict=None
   for t,p,h,c in rd+[(gap,0j,h,'L')]:
    before=(c=='L')
    if p in colors and colors[p]!=before:conflict=(t,[int(p.real),int(p.imag)],c);break
    colors[p]=not before
   assert conflict is not None;geoms.append((w,conflict))
  assert count==(4 if gap==4 else 64)and len(geoms)==(0 if gap==4 else 3)
  rr=next(x for x in ref['tables']if x['kind']==side and x['gap']==gap);assert{w for w,c in geoms}=={x['word']for x in rr['rejections']};tables.append(dict(side=side,gap=gap,candidates=count,geometries=geoms))
c=ref['sharp_control'];B={complex(*q)for q in c['initial_black']};p=complex(*c['initial_position']);h=c['initial_heading'];H={};fields=[]
assert len(B)==7 and len(c['word'])==26
for t,ch in enumerate(c['word']):
 assert('L'if p in B else'R')==ch;z={'t':t,'p':[int(p.real),int(p.imag)],'h':h,'c':ch};assert z==c['trace'][t];H.setdefault(p,[]).append(z);fields.append(sorted([int(q.real),int(q.imag)]for q in B));B.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;p+=V[h]
assert sorted([int(q.real),int(q.imag)]for q in B)==c['final_black']and[p.real,p.imag]==c['final_position']and h==c['final_heading']
assert H[1j]==c['source_history']and H[0j]==c['target_history'];assert[(z['t'],z['h'],z['c'])for z in H[1j]]==[(12,1,'R'),(24,1,'L')];assert[(z['t'],z['h'],z['c'])for z in H[0j]]==[(1,0,'R'),(13,2,'L')]
out={'status':'PASS all-cap twelve-time overlap gate and finite locally sharp26-read control','author_note':sha(D/'OVERLAP_TWELVE_TIME_GATE.md'),'short_gap_tables':tables,'full26_field_trace':fields,'source_history':H[1j],'target_history':H[0j],'source_age':12,'target_age':12,'combined_span':23,'analytic_review':[
'The signed overlap port rule is used only when both endpoints belong to selected first/last counterflow cycles, hence both are even, sourceSAME and targetOPPOSITE. Every physical return length is divisible by4, so a positive first-to-last age below12 is exactly4 or8, regardless visit cap.',
'At target start firstR and opposite incoming lastL, the preceding shared source event isR. Thus the gap word starts/endsR, displacement0, finalincomingS, with endpointL required. At source firstR the immediate target lastL forces prefixRL; sameincoming lastL requires displacement0,headingN. These are complete necessary local constraints; OTHER cells may start either color.',
'Independent full enumeration gives4/64 prefix-compatible words per side at4/8, no geometric4 returns and exactlythree geometric8 returns each. All fail exact same-cell alternation including the finalL. This is an exact short return proof, not a cap/period/width scan and not a clean-background assumption.',
'On each b cycle a shared-edge target is a LEFT corner with q=targetage/4>=3 instead of baseline1. Distinct overlap targets and equal R/L corners yield P>=ell+8c. Reversing gives the same bound using the originalsourceage for the corresponding last-L cycle. Sum separately to kF P>=LF+8C and kL P>=LL+8C. These estimates and the spatial inventory bound constrain the same period and may not be added as disjoint charges.',
'The complete seven-black26-read control has internal sourceR12(E)/L24(E), targetR1(N)/L13(S), both ages12 and totalspan23. Every actual field/read/pose matches, finalcompleteboard hassevenblack. This demonstrates sharpness only for the prepared finite interface; LAST is not asserted globally, and no essential cycle or translating controller is attained.' ]}
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])

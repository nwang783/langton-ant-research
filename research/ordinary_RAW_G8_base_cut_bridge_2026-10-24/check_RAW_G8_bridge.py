"""Exact local grammar at BASE cuts, not arbitrary-ant language coverage.
A terminal DCC is retained as an attained exception to complete-G8 parsing.
"""
from pathlib import Path
import importlib.util,json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent

def load(n,p):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=load('literal',R/'word_stabilization/check_foreign_return_interfaces.py');o=load('owner',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS

def add(p,q):return p[0]+q[0],p[1]+q[1]
def after(w,p=(0,0,0)):
 q,h=p[:2],p[2]
 for c in w:h=(h+(1 if c=='R'else-1))%4;q=add(q,l.DIRS[h])
 return*q,h

def at(q,p):return add(p[:2],l.rot(q,p[2]))
def spell(word):return ''.join(W[a]for a in word)
def owner_for(word,t):
 off=0
 for i,a in enumerate(word):
  if t<off+len(W[a]):return dict(atom_index0=i,atom=a,atom_tick0=t-off,atom_read_number1=t-off+1,turn=W[a][t-off])
  off+=len(W[a])
 return dict(owner='actual following word supplied by M11',next_word_tick0=t-off,next_word_read_number1=t-off+1,turn=l.M[t-off])
# Every named ordinary RAW has the same physical entry prefix; the short
# D10 uses the ACTUAL next firstL for its marker's eleventh letter.
marker=[]
for a in'DCVU':
 raw=W[a]
 if len(raw)>=11:assert raw[:11]==l.M;mode='own first11 RAW'
 else:
  assert a=='D'and raw==l.M[:10]and all(W[b][0]==l.M[10]for b in'DCVUFQB');mode='own first10 plus ACTUAL next word firstL'
 marker.append(dict(atom=a,RAW_length=len(raw),M11_supply=mode))
fixed=[]
for word in['DCCD','DCCV','DCCU','VCCC','UCCC']:
 t=l.trace(spell(word)+l.M);assert not t['feasible'];fixed.append(dict(word=word,conflict=t,previous_owner=owner_for(word,t['previous_read']),conflicting_owner=owner_for(word,t['conflict_read'])))
# The DCCC incoming-bud conflict is the SAME actual previous R and no
# intermediate read, not a lifetime theorem or CORE reset.
beta=(1,-1);d3=spell('DCCC');dt=l.trace(d3+l.M);assert dt['feasible']and beta not in l.trace(d3)['first']and dt['first'][beta]==('R',62)and len(d3)==55
bud=[]
for prev in'DCVUFQB':
 raw=W[prev];tr=l.trace(raw);ep=after(raw);g=at(beta,ep);assert tr['last'][g]==('R',len(raw)-2)and list(g)in l.literal_geometry(raw)['outputs']
 t=l.trace(raw+d3+l.M);assert not t['feasible']and t['cell']==list(g)and t['previous_read']==len(raw)-2 and t['conflict_read']==len(raw)+62 and t['turn']=='R'
 bud.append(dict(actual_preceding_RAW=prev,previous_RAW_EXIT=ep,SAME_EXIT_bud=g,last_R_tick0=len(raw)-2,RAW_birth_owner=o.describe(prev,len(raw)-2),DCCC_RAW_MISS=True,DCCC_context_first_R_tick0=62,following_owner=owner_for('DCCC',62),whole_conflict=t))
G8={'D','DC','V','VC','VCC','U','UC','UCC'}
def parse(word):
 assert word and word[0]in'DVU'and set(word)<=set('DCVU')
 out=[];i=0
 while i<len(word):
  assert word[i]in'DVU';j=i+1
  while j<len(word)and word[j]=='C':j+=1
  token=word[i:j]
  if token not in G8:return dict(packets=out,unparsed=word[i:],offset=i)
  out.append(token);i=j
 return dict(packets=out,unparsed='',offset=len(word))
# This is a spelling partition, not a finite-language proof by enumeration.
# The no-long-C-run proof below establishes arbitrary-length admissibility.
controls=[]
for word,sourceidx in [('DCCC',None),('UDCC',0),('UQUDCC',2),('UQUCCV',2)]:
 raw=spell(word);t=l.trace(raw+l.M);assert t['feasible'];seed={p for p,(c,k)in t['first'].items()if c=='L'};B=set(seed);p=(0,0,0)
 for c in raw+l.M:
  assert(p[:2]in B)==(c=='L')
  if c=='L':B.remove(p[:2])
  else:B.add(p[:2])
  p=after(c,p)
 selected=word if sourceidx is None else word[sourceidx:];par=parse(selected)
 if word=='UQUCCV':assert par['packets']==['UCC','V']and not par['unparsed']
 elif word!='DCCC':assert par['unparsed']=='DCC'
 controls.append(dict(word=word,selected_source_index0=sourceidx,selected_ordinary_word=selected,selected_parse=par,complete_seed=sorted(seed),all_actual_RAW_plus_M_reads=len(raw)+11,scope='Physical positive regression; terminal DCC and prepared factor-first DCCC are deliberately NOT called G8.'))
# Exact terminal-point actor list at the selected fresh U entry. Affine
# heads are obtained from G = head+rot(-1,-1)/2+t*rot(v)/2, not a radius scan.
from fractions import Fraction as Q

def sub(p,q):return p[0]-q[0],p[1]-q[1]
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def z(p):return at((-1,-1),(2*p[0],2*p[1],p[2]))
G=(-1,-1);terminal=[];LEFT={(0,0),(0,1)}
for a in'DCVU':
 ep=after(W[a]);v0=sub(z(ep),z((0,0,0)));den=abs(v0[0])or abs(v0[1]);tr=l.trace(W[a]+l.M)
 for h in range(4):
  v=l.rot(v0,h);c=l.rot((-1,-1),h)
  # The endpoints' odd integer coordinates and integer heads force t to
  # divide the nonzero chord coordinate; this denominator is exhaustive.
  for j in range(1,den+1):
   t=Q(j,den);nx=Q(G[0]-c[0])-t*v[0];ny=Q(G[1]-c[1])-t*v[1]
   if nx.denominator!=1 or ny.denominator!=1 or int(nx)%2 or int(ny)%2:continue
   p=(int(nx)//2,int(ny)//2,h)
   if(sum(p[:2])+h)%2:continue
   start=z(p)
   # Opposite collinear approach meets source interior BEFORE its entry;
   # same-direction onset from below is a genuine retained contact.
   if v[0]==0 and(v[1]<=0 or start[1]>=G[1]):continue
   Ks=[k for k in range(7)if(-k)%4==h and (2<k<6 or k==6 and a!='U')]
   bad=[];roles=[]
   for tag in sorted(LEFT):
    q=l.rot(sub(tag,p[:2]),-h);f=tr['first'].get(q);roles.append(dict(tag=tag,local=q,first=f,owner=o.describe(a,f[1])if f else None))
    if q in l.K or f and f[0]=='R':bad.append(dict(tag=tag,role='ENTRY_CORE'if q in l.K else'first_WHITE',local=q))
   terminal.append(dict(atom=a,entry=p,new_t=str(t),necessary_source_relative_C=Ks,LEFT_conflicts=bad,LEFT_roles=roles,route='SAME_LEFT_CURRENT_CORE_or_WHITE'if bad else'base_cut_G8_bridge'))
assert len(terminal)==18 and len([r for r in terminal if r['LEFT_conflicts']])==13
assert{(q['atom'],tuple(q['entry']))for q in terminal if not q['LEFT_conflicts']}=={('D',(-1,0,1)),('V',(-3,0,1)),('U',(0,-2,0)),('U',(-4,-1,1)),('U',(-2,-1,1))}
assert all(q['atom']in'DVU'for q in terminal if not q['LEFT_conflicts'])
D=[R/'word_stabilization/check_foreign_return_interfaces.py',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py',R/'core_periodicity_new/U_entry_simplicity_frozen_20261023_1616/manifest.json',R/'audits/check_U_entry_simplicity_independent.json',R/'fresh_RAW_U_LEFT_all_length_2026-10-24/manifest.json',R/'audits/check_fresh_U_LEFT_all_length_independent.json',R/'one_foreign_first_contact_compression_2026-10-24/manifest.json',R/'audits/check_one_foreign_contact_C_window_independent.json']
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='Exact ordinary RAW factor beginning at a D/V/U base and ending at a D/V/U base, with ACTUAL final M11. If the first base is D, it has an ACTUAL preceding seven-atom RAW; for initial V/U no external predecessor is needed. Then the factor partitions into D,DC,V,VC,VCC,U,UC,UCC actual packets. This is a restricted-word grammar theorem, not arbitrary ant coverage or terminal-C parsing.',all4_actual_M11_supplies=marker,all5_fixed_literal_conflicts=fixed,all7_actual_predecessor_DCCC_EXIT_bud_conflicts=bud,DCCC_identity_statement='Previous RAW final-R at own len-2 is SAME CURRENT physical EXIT beta. DCCC RAW entirely MISSES it. Its actual following word tick7/read8 first requires R at DCCC context62, an immutable repeated R. No minimum age or residual-only repair argument is used.',arbitrary_length_parse_proof='Write each ordinary word as maximal base-plus-C runs. VCCC/UCCC forbid >=3 Cs after V/U, using actual next M if needed. DCC followed D/V/U is forbidden by the three fixed conflicts. >=3 Cs after D is forbidden by the actual preceding RAW EXIT-bud conflict; this previous atom exists internally unless D is first, where it is a stated hypothesis. Because the factor ends at a BASE, a DCC run cannot be terminal, hence every D run has <=1 C. Thus each maximal run is exactly a chosen G8 packet, with identical real RAW cuts and actual M11 supply. No bounded-length enumeration is used.',source_U_invocation='For a selected fresh RAW U, every D has a real preceding RAW inside the factor. The first maximal run is ACTUAL U/UC/UCC and the ending base is an ACTUAL completed D/V/U G8 packet with the SAME final M11. The signed U-entry center-simplicity theorem applies to arbitrary actual complete entry field; an earlier foreign or unrelated history lies outside the factor and is not an extra required ancestry. Therefore the selected-U-to-ending-base atomic proxy is injective without assuming it before the conclusion.',all18_foreign_EXIT_outgoing_b1U_terminal_actors=terminal,terminal_consequence='If the first ordinary RAW after a foreign is U, a GLOBAL first contact at that foreign EXIT is owned by outgoing U. Nonadjacent contact C is excluded by CURRENT LEFT at ENTRY (all four terminal C poses have an actual CORE/WHITE conflict). Every remaining D/V/U actor is excluded by the source-U base-cut G8 bridge and signed U-entry simplicity. The initial adjacent join with the foreign, and U immediately leaving its own entry, are not counted as recontacts.',terminal_DCC_exception='An ordinary factor ending in C may end in DCC, not a chosen packet. Actual UDCC and UQUDCC+M controls are positive. No full ordinary-tail simplicity is inferred at those terminal cuts, and no claim is made about contacts involving earlier sources before the new U.',positive_scope_regressions=controls,not_claimed=['No arbitrary seven-atom coverage of an ant trajectory.','No second foreign.','No conversion of a merely RAW-complete terminal DCC into G8.','No source-D/C/V arbitrary-tail simplicity.','No LEFT persistence through a contact atom.'],dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'RAW_G8_bridge.json').write_text(json.dumps(out,indent=2)+'\n');print('Base-cut RAW->G8:5 fixed conflicts +7 immutable previous EXIT-bud DCCC guards. Terminal U-entry point18=13LEFT+5 actualG8. Four attained scope regressions retained.')

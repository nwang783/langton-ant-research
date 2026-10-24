from pathlib import Path
from fractions import Fraction
from math import gcd
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'ordinary_RAW_G8_base_cut_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='8a311a4c67a3447c06ff6feddadacb4928a3ffba63f4b8e8088c4663e2a36704'
for k,base in [('files',D),('dependencies',R)]:
 for f,h in json.loads(MF.read_text())[k].items():assert sha(base/f)==h
J=json.loads((D/'RAW_G8_bridge.json').read_text());ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy,center,meet=[ns[k]for k in('W','M','K','tr','rot','xy','center','meet')]
spell=lambda word:''.join(W[a]for a in word)
def own(word,t):
 off=0
 for k,a in enumerate(word):
  if t<off+len(W[a]):return dict(atom_index0=k,atom=a,atom_tick0=t-off,atom_read_number1=t-off+1,turn=W[a][t-off])
  off+=len(W[a])
 return dict(owner='actual following word supplied by M11',next_word_tick0=t-off,next_word_read_number1=t-off+1,turn=M[t-off])
for a in'DCVU':
 if a=='D':assert len(W[a])==10 and W[a]==M[:10]and all(W[b][0]==M[10]for b in'DCVUFQB')
 else:assert W[a][:11]==M
conflicts=[]
for row in J['all5_fixed_literal_conflicts']:
 word=row['word'];z=tr(spell(word)+M);bad=z['bad'];assert bad is not None
 t,prev,cell,ch=bad;ref=row['conflict'];assert xy(cell)==ref['cell']and prev==ref['previous_read']and t==ref['conflict_read']and ch==ref['turn'];assert own(word,prev)==row['previous_owner']and own(word,t)==row['conflicting_owner'];conflicts.append([word,prev,t,ch])
assert {r[0]for r in conflicts}=={'DCCD','DCCV','DCCU','VCCC','UCCC'}
beta=1-1j;d3=spell('DCCC');z=tr(d3+M);assert not z['bad']and beta not in tr(d3)['req'];assert next((t,c)for t,(q,h,c)in enumerate(z['reads'])if q==beta)==(62,'R')and len(d3)==55
for row in J['all7_actual_predecessor_DCCC_EXIT_bud_conflicts']:
 a=row['actual_preceding_RAW'];raw=tr(W[a]);g=raw['p']+rot(raw['h'])*beta;assert raw['last'][g]==('R',len(W[a])-2)and g not in {raw['p']+rot(raw['h'])*q for q in K};bad=tr(W[a]+d3+M)['bad'];assert bad==(len(W[a])+62,len(W[a])-2,g,'R')
 assert row['SAME_EXIT_bud']==xy(g)and row['last_R_tick0']==len(W[a])-2 and row['following_owner']==own('DCCC',62)
# The dependency is literally stated for ANY actual complete U-family-entry factor.
fd=R/'core_periodicity_new/U_entry_simplicity_frozen_20261023_1616';fm=json.loads((fd/'manifest.json').read_text())
for r in fm['files']:assert sha(fd/r['frozen'])==r['sha256']
text=(fd/'00_U_entry_center_simplicity.md').read_text();assert 'Let an actual finite factor of the complete recurrent-eight language begin\nwith U, UC, or UCC.'in text and 'resulting continuous polygonal path is injective in path time'in text
signed=json.loads((R/'audits/check_U_entry_simplicity_independent.json').read_text());assert signed['status'].startswith('PASS')and signed['U_first_packet_ids']==[7,8,9]
G8={'D','DC','V','VC','VCC','U','UC','UCC'}
def parse(word):
 ans=[];i=0
 while i<len(word):
  assert word[i]in'DVU';j=i+1
  while j<len(word)and word[j]=='C':j+=1
  if word[i:j]not in G8:return dict(packets=ans,unparsed=word[i:],offset=i)
  ans.append(word[i:j]);i=j
 return dict(packets=ans,unparsed='',offset=len(word))
controls=[]
for row in J['positive_scope_regressions']:
 word=row['word'];raw=spell(word)+M;z=tr(raw);assert not z['bad'];seed={q for q,b in z['req'].items()if b};assert sorted(map(xy,seed))==row['complete_seed']and len(raw)==row['all_actual_RAW_plus_M_reads'];B=set(seed);p=0j;h=0
 for c in raw:
  assert(p in B)==(c=='L');B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=rot(h)*1j
 selected=word if row['selected_source_index0']is None else word[row['selected_source_index0']:];assert parse(selected)==row['selected_parse'];controls.append(dict(word=word,seed_size=len(seed),reads=len(raw),final_black=sorted(map(xy,B)),final_pose=xy(p)+[h]))
# Exact lattice endpoint equation, using gcd of BOTH vector coordinates.
G=-1-1j;LEFT={0j,1j};rows={};survivors=[];cuts=0
for a in'DCVU':
 raw=tr(W[a]);v0=center(raw['p'],raw['h'])-center(0j,0);g=gcd(abs(int(v0.real)),abs(int(v0.imag)))
 for h in range(4):
  v=v0*rot(h);c=(-1-1j)*rot(h)
  for j in range(1,g+1):
   t=Fraction(j,g);nx=Fraction(int((G-c).real))-t*int(v.real);ny=Fraction(int((G-c).imag))-t*int(v.imag)
   if nx.denominator!=1 or ny.denominator!=1 or int(nx)%2 or int(ny)%2:continue
   p=int(nx)//2+(int(ny)//2)*1j
   if(int(p.real+p.imag)+h)%2:continue
   start=center(p,h)
   if v.real==0 and(v.imag<=0 or start.imag>=G.imag):continue
   ky=(a,tuple(xy(p)+[h]),str(t));assert ky not in rows
   ctx=tr(W[a]+M);bad=[]
   for q in LEFT:
    loc=(q-p)/rot(h)
    if loc in K or ctx['req'].get(loc)is False:bad.append(q)
   rows[ky]=bad
   if bad:cuts+=1
   else:survivors.append((a,p,h));assert any((q-p)/rot(h)in I for q in LEFT for I in [{r for r,b in ctx['req'].items()if b and r not in K}])
ref={(r['atom'],tuple(r['entry']),r['new_t']):r for r in J['all18_foreign_EXIT_outgoing_b1U_terminal_actors']};assert set(rows)==set(ref)and len(rows)==18 and cuts==13
for ky,bad in rows.items():
 rr=ref[ky];assert set(map(tuple,map(xy,bad)))=={tuple(z['tag'])for z in rr['LEFT_conflicts']};a,praw,_=ky;p=complex(*praw[:2]);h=praw[2]
 for role in rr['LEFT_roles']:
  q=complex(*role['tag']);loc=(q-p)/rot(h);assert role['local']==xy(loc)
  ff=next(((c,t)for t,(qq,hh,c)in enumerate(tr(W[a]+M)['reads'])if qq==loc),None);assert (list(ff)if ff else None)==role['first']
  if ff:assert role['owner']['context_tick0']==ff[1]
assert set(survivors)=={('D',-1+0j,1),('V',-3+0j,1),('U',-4-1j,1),('U',-2-1j,1),('U',-2j,0)}
out=dict(status='PASS exact ordinary RAW-to-G8 grammar at BASE cuts and outgoing firstpostU terminal closure',manifest=sha(MF),script=sha(S),fixed_conflicts=conflicts,actual_predecessor_bud_cases=7,terminal_actor_count=18,LEFT_field_cuts=13,true_input_BASE_actors=5,controls=controls,analytic_review=[
'Every maximal base-plus-C run is governed by actual immutable read conflicts. V/U cannot have three Cs; DCC cannot be followed by a base. A D run with >=3 Cs has an ACTUAL preceding seven-atom RAW unless it is factor-firstD, where this is an explicit hypothesis. That preceding RAW creates beta at ownlen-2; DCCC entirely misses it before actual nextwordR7/context62. This excludes all long D runs without a maturity law or bounded word enumeration.',
'Because the factor ends in a BASE, terminal DCC cannot escape the run argument. Thus all maximal runs are exactly D/DC/V/VC/VCC/U/UC/UCC at real cuts. Internal markers are actual next RAW prefixes; shortD supplies10 plus the actual nextfirstL. Terminal marker is the SAME stipulatedM11, never an invented completed tail.',
'The frozen signed U-entry theorem is explicitly for ANY actual complete recurrent-eight factor beginningU/UC/UCC, with no pre-factor ancestry or WHITE-entry premise. A fresh U after an earlier foreign therefore starts a valid new factor; every internal D has its real predecessor. Simplicity follows from that theorem AFTER the grammar proof and is not assumed circularly.',
'All18 endpoint actor poses are independently derived from the exact affine lattice equation using gcd of both chord coordinates. Positive-time endpoints and codirected U onset are retained; opposite collinear approach would already meet source interior. Outgoing-U ownership of the foreign EXIT is explicit, and the initial adjacent foreign/U join is not treated as a recontact.',
'Thirteen poses, including every C actor, violate SAME LEFT CURRENT at global-first ENTRY. The other five genuinely take at least one LEFT identity as a TRUE input; no entry-field contradiction is claimed. They are ending BASE atoms, so the selected-U-to-actor interval parses into actualG8 and the signed U-entry injectivity excludes them regardless of any additional clock metadata.',
'Prepared factor-firstDCCC and terminalUDCC/UQUDCC are actual full-field positives, not covered by the grammar. UQUCCV selects the new postQ U and really parsesUCC,V. No terminal-C/all-tail simplicity, contact with sources before the selectedU, anotherforeign, arbitrary-ant language coverage or capture is inferred.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))

from pathlib import Path
from fractions import Fraction
import json,hashlib,itertools,collections
R=Path('/workspace/shared/langton');P=R/'postforeign_first_source_three_atom_transfer_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=P/'manifest.json';assert sha(mf)=='997238b2da95a6de47dd46291e6d67b5f1d699663d40ba18a5a73ff645e5320d';MNF=json.loads(mf.read_text())
for f,h in MNF['files'].items():assert sha(P/f)==h
p=R/'audits/check_old_V_second_age1_independent.py';ns={'__file__':str(p)};exec(p.read_text().split('# Universal')[0],ns)
W,M,K,tr,pieces,meet,xy,V,rot,center=[ns[k]for k in['W','M','K','tr','pieces','meet','xy','V','rot','center']];J=json.loads((P/'first_source_transfer.json').read_text())
for f,h in J['dependencies'].items():assert sha(R/f)==h
sources={}
for a in'DCVU':
 t=tr(W[a]);ek={t['p']+q*rot(t['h'])for q in K};O={q:i for q,(ch,i)in t['last'].items()if ch=='R'and q not in ek};sources[a]=O
 assert {(tuple(xy(q)),i)for q,i in O.items()}=={(tuple(r['source_output_cell']),r['last_R_birth_tick0'])for r in J['all4_actual_atomic_sources_and_fresh_R_output_identities'][a]}
assert {a:len(O)for a,O in sources.items()}=={'D':1,'C':3,'V':6,'U':9}
keys=set();contacts=[];legal=0
for ts in itertools.product('DCVU',repeat=3):
 toks=''.join(ts);a,b,c=ts;seg=pieces(toks);hit=meet(*seg[0],*seg[2]);T=tr(''.join(W[x]for x in ts)+M);row=next(r for r in J['all64_ordinary_triple_geometry_and_literal_rows']if r['ordinary_atoms']==toks)
 assert row['complete_triple_feasible']==(T['bad']is None)
 if hit:contacts.append((toks,hit));assert T['bad']==(42,2,-1-1j,'L')
 if T['bad']:continue
 legal+=1;t2=tr(W[a]);t3=tr(W[a]+W[b]);t4=tr(''.join(W[x]for x in ts))
 for q,birth in sources[a].items():
  for t,w in[(t2,W[b]+M),(t3,W[c]+M)]:assert q not in{z for z,_,_ in tr(w,t['p'],t['h'])['reads']}
  for t in[t2,t3,t4]:assert q not in{t['p']+z*rot(t['h'])for z in K}
  keys.add((toks,tuple(xy(q)),birth))
assert legal==55 and contacts==[('CCU',(Fraction(0),Fraction(1,2)))]and len(keys)==270
assert keys=={(r['ordinary_atoms'],tuple(r['original_source_R_fact']['source_output_cell']),r['original_source_R_fact']['last_R_birth_tick0'])for r in J['all270_SAME_original_output_transfer_rows']}
controls=[]
for row in J['five_complete_prepared_fourth_erosion_controls']:
 ts=row['tokens'];word=''.join(W[a]for a in ts)+M;rawlen=len(word)-len(M);tt=tr(word);assert tt['bad']is None
 seed={q for q,b in tt['req'].items()if b};assert sorted(map(xy,seed))==row['complete_seed']and len(seed)==row['initial_black_mass'];B={q:('initial',None)for q in seed};p=0j;h=0;sn={};birth=row['first_V_A_birth_tick0'];death=row['original_A_actual_death_global_tick0'];q=complex(*row['first_V_genuine_A_cell']);s4=row['fourth_V_start_tick0']
 for i,ch in enumerate(word):
  rec=row['all_actual_fine_reads'][i];ident=B.get(p);assert ch==('L'if ident is not None else'R')and rec['cell']==xy(p)and rec['turn']==ch
  assert rec['before_identity']==(list(ident)if ident is not None else None)
  if ch=='L':del B[p]
  else:B[p]=('R',i)
  if i==birth:assert p==q and ch=='R'
  if i==death:assert p==q and ch=='L'and ident==('R',birth)
  h=(h+(1 if ch=='R'else-1))%4;p+=V[h]
  if str(i+1)in row['exact_cut_states']:
   z=row['exact_cut_states'][str(i+1)];alive=B.get(q)==('R',birth);core=q in{p+x*rot(h)for x in K};assert xy(p)==z['head']and h==z['heading']and alive==z['SAME_original_physically_alive']and core==z['inside_actual_active_core']and (alive and not core)==z['CURRENT_same_original_residual'];sn[i+1]=(alive,core)
 assert sn[s4]==(True,False)and sn[s4+18]==(True,True)and death==s4+19 and B.get(q)!=('R',birth)
 owner=row['original_A_death_owner'];assert owner['actual_atom']=='next actual word'and owner['next_word_tick0']==1 and owner['next_word_read_number1']==2
 seg=pieces(ts)
 for i,j in itertools.combinations(range(len(seg)),2):
  hit=meet(*seg[i],*seg[j]);assert hit==((1,0)if j==i+1 else None)
 controls.append([''.join(ts),len(seed),len(word),birth,s4,death])
assert controls==[['FVCCV',22,133,67,104,123],['QVCCV',23,141,75,112,131],['BVCCV',26,151,85,122,141],['UQVCCV',28,169,103,140,159],['UBVCCV',31,179,113,150,169]]
assert tr(''.join(W[a]for a in'UFVCCV')+M)['bad']==(157,21,-1+2j,'R')
# Stored source convention has cell(-1,2), not a sign-changed guess.
report={'status':'PASS finite 64-triple/270 same-ID transfer and five complete fourth-erosion controls','manifest_sha256':sha(mf),'script_sha256':sha(Path(__file__)),'legal_triples':legal,'same_original_output_instances':len(keys),'full_board_controls':controls,'analytic_scope':['Literal atomic outputs are actual RAW last-R identities outside exitK. No fullproducer-age law or age after foreign is used.','All legal triple contexts include actual finalM11; later RAW+futureM footprints are tested for absence only, never treated as executed early. Complete original cohort remains physically unread and CURRENT through third RAW exit/fourth entry.','Only b3/b1 geometry CCU is RAW-inconsistent; foreign pieces remain a separate dependency.','Five complete prepared boards replay every fine read with full physical birth identities and actual cores. Genuine UQ/UB old prefixes and all expanded foreign-kink proxies are simple. FirstV A is CURRENT at fourthV entry, SAME aliveCORE at exit, physically L-deleted next-word tick1/read2.','Fourth erosion is of a new postforeign V cohort, not original creatingU star. It does not entail proxy contact and defeats naive iteration of this finite cohort transfer.'],'not_claimed':['arbitrary-tail persistence','third global simplicity','postforeign maturity','infinite continuation or attraction']}
p=R/'audits/third_source_transfer_independent.json';p.write_text(json.dumps(report,indent=2)+'\n');print(sha(p));print(report['status'])

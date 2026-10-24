from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];ns={'__file__':str(SELF)};exec((SELF.parent/'check_foreign_kinked_barrier_turn_independent.py').read_text().split('geometries=[]')[0],ns)
walk,W,M,xy=[ns[x]for x in('walk','W','M','xy')];D=ROOT/'returned_V_source_reduction_2026-10-23';a=json.loads((D/'returned_V_source_reduction.json').read_text());K={-1-1j,-1,-1j,0,1}
names=['D','DC','V','VC','VCC','U','UC','UCC'];raw={n:walk(''.join(W[c]for c in n))for n in names};ctx={n:walk(''.join(W[c]for c in n)+M)for n in names};I={n:{q for q,b in ctx[n]['req'].items()if b}-K for n in names}
outputs={n:({q for q,b in ctx[n]['req'].items()if b}^raw[n]['odd'])-{raw[n]['p']+q*(-1j)**raw[n]['h']for q in K}for n in names};S=outputs['V'];assert len(S)==6
for n in('V','VC','VCC'):
 assert S<=outputs[n]
 for q in S:
  base=[(i,c)for i,(p,h,c)in enumerate(raw['V']['reads'])if p==q];allr=[(i,c)for i,(p,h,c)in enumerate(raw[n]['reads'])if p==q];assert base==allr and allr[-1][1]=='R'
mins={k:v['certified_minimum_C_age']for k,v in json.loads((ROOT/'audits/dcuv_count5_replay/queries.json').read_text())['slots'].items()};assert min(mins.values())==2
cu=walk(W['C']+W['U']);assert not cu['feasible']and(cu['i'],cu['q'],cu['first'])==(29,-1,1)
cat=json.loads((ROOT/'seven_word_spatial_return_2026-10-23/first_returned_atom_contact.json').read_text())['old_source_contact_cases'];refs={r['catalogue_case']:r for r in a['all112_V_source_rows']};counts=Counter();remaining=[];early=[]
def ncounts(z):
 x,y=xy(z);out=[]
 for v in range(max(0,x+1)):
  d=x-v;rem=y-d-3*v
  if d>=0 and rem>=0 and rem%4==0:out.append((d,v,rem//4))
 return out
def ecounts(z):
 x,y=xy(z);down=-y;out=[]
 for v in range(max(0,down+1)):
  d=down-v;rem=x-d-3*v
  if d>=0 and rem>=0 and rem%4==0:out.append((d,v,rem//4))
 return out
common=[]
for f,p in [('F',2-3j),('Q',4-3j)]:
 ff=walk(W[f]+M);qlocal=(2-p)*1j;assert ff['req'][qlocal]is False
 for n in('D','V','U'):
  for i in I[n]:
   entry=2-i*(-1j);end=entry+raw[n]['p']*(-1j);sol=ecounts(p-end);assert end!=p and all(v==u==0 for d,v,u in sol);common.append((f,n,xy(i),xy(entry),xy(end),sol))
assert len(common)==16
for ix,row in enumerate(cat):
 if row['source_atom']!='V':continue
 age=row['source_to_foreign_C_age'];f=row['foreign'];ret=row['returned_atom'];p=complex(*row['foreign_pose'][:2]);h=row['foreign_pose'][2];tr=walk(W[f]+W[ret]+M);assert tr['feasible'];white={p+q*(-1j)**h for q,b in tr['req'].items()if not b};guard=None
 if age<=1:
  hit=S&white
  if hit:kind='young_all_six_V_base_identities_current_before_combined_WHITE';guard=min(hit,key=xy)
  elif age==0:
   sol=ncounts(p-(1+3j));assert sol
   assert all((v==u==0 if f=='Q'else u==0)for d,v,u in sol);kind='clock0_N_run_has_no_actual_allowed_last_foreign_predecessor';early.append((ix,kind,sol))
  else:
   assert h==3 and p.imag<=4
   if p.imag<4:kind='one_C_N_to_W_head_minimum_y4_exceeds_foreign_y'
   else:
    num=1-int(p.real)
    if num<0 or num%4:kind='clock1_y4_W_U_only_run_wrong_x_residue'
    else:assert num//4>=1;kind='clock1_forces_actual_VC_then_U_and_raw_C_U_is_literal_conflict'
   early.append((ix,kind))
 elif 0 in white:kind='genuine_V_r_first_retirement5_vs_combined_before_WHITE';guard=0
 elif age<=3 and 1 in white:kind='genuine_V_B_first_retirement4_vs_combined_before_WHITE';guard=1
 elif age==3 and(f,p)in[('F',2-3j),('Q',4-3j)]:kind='genuine_common_bud3_E_clearer_endpoint_guard';guard=2
 else:kind='necessary_geometry_not_asserted_attained';remaining.append(ix)
 ref=refs[ix];assert ref['classification']==kind
 if guard is not None:
  assert guard in white and list(xy(guard))==ref['chosen_same_source_guard'];z=(guard-p)*1j**h;first=next((i,c)for i,(q,hh,c)in enumerate(tr['reads'])if q==z);assert list(first)==ref['actual_combined_first_read']
 counts[kind]+=1
assert len(refs)==112 and len(early)==11 and remaining==[167,168,169,173,174,175,211,212,213,214,215,216,217,218,219,220,221,222]
assert counts==Counter(a['classification_counts'])
controls=[]
for label,ti,q in [('VCDCVVCDUF',188,2),('VCDCDUCVUBD',97,-1),('UCCVCDCVVCDUF',102,-1+1j)]:
 word=''.join(W[c]for c in label);r=walk(word);assert not r['feasible']and(r['i'],r['q'])==(ti,q)
 if label=='VCDCVVCDUF':
  good=walk(word[:ti]);seed={z for z,b in good['req'].items()if b};assert len(seed)==27
  board=set(seed);p=0j;h=0
  for c in word[:ti]:assert(p in board)==(c=='L');board.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=(1j,1,-1j,-1)[h]
  assert p==2 and p in board and word[ti]=='R'
 controls.append((label,ti,xy(q)))
mp=D/'manifest.json';mh=hashlib.sha256(mp.read_bytes()).hexdigest();assert mh=='b1bd1068c341bfc4e54e224ca4e29df44da6561842cc642c6ecc9456ac883df9'
for f,h in json.loads(mp.read_text())['files'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
for f,h in a['dependencies'].items():assert hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h
out={'status':'PASS 94 of112 old-V first-returned-contact labels excluded;18 necessary clock3 residues retained','manifest_sha256':mh,'classifications':dict(counts),'six_base_outputs':sorted(map(xy,S)),'minimum_produced_input_age_used':2,'early_unbounded_head_cases':early,'all16_common_bud_E_endpoint_obligations':common,'residual_catalogue_ids':remaining,'fixed_failed_connector_controls':controls,'analytic':['Every genuine V/VC/VCC source retains all six exact base last-R identities through its actual source C tails. At foreign clocks0/1 no later full input can retire them, using the correct universal minimum2. A source not yet fully complete cannot precede the foreign, so no internal-tail birth clock is substituted for full-source entry.','At clock0 the unbounded N-run count equations leave only DD before Q or V before B, both forbidden by actual complete-eight/foreign adjacency. At clock1 y>=4; equality forces the unique C immediately after the source V base, hence genuine VC, followed only by W-U bases. Wrong x congruence or the exact C-U RAW conflict excludes the remaining cases.','Signed all-age original r first-retirement5 and B first-retirement4 hold only in the actual simple old-eight prefix. Combined foreign+returned+M11 requirements are pulled back to foreign ENTRY, so no postforeign age law or identity persistence is assumed.','Common R8 bud cannot retire before3 Cs. At foreign clock3 its prior full retiring packet must be plain E-heading D/V/U; all8 input roles are included, including marker-only core absorption. All16 exact zero-C E continuation obligations to F2,-3 or Q4,-3 fail actual last-V/U adjacency, with no empty-run exception. B5,-2 and F4,-3 require BLACK, not WHITE, and remain untouched by this guard.','The27-cell prescribed connector really reaches F and executes its first41 RAW reads before the old common bud forces L instead of R. It is not a complete foreign, returned contact, or certified U-entry history. Two other fixed attempts fail earlier on genuine deleted-core cells.'],'scope':'Only chronological FIRST new immediate returned-atom contact with old outgoing V source in the signed catalogue.18 geometries remain necessary only. No returned simplicity, all-seven termination, second foreign or capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(counts)

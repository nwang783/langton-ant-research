from pathlib import Path
from collections import Counter
from itertools import product
import ast,json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'genuine_LL_caps_are_XY_and_force_an_off_cycle_nested_return.md';C=D/'check_genuine_LL_XY_nested_reader.json';assert sha(P).startswith('fd3860a0')and sha(C).startswith('b5c4987e')and sha(D/'check_genuine_LL_XY_nested_reader.py').startswith('8b6d3b24');J=json.loads(C.read_text());base=json.loads((D/'check_LL_cyclic_supplier_reactivation_modes.json').read_text());ns={'__file__':str(S.with_name('check_global_max_flow2_staircase_independent.py'))};exec(Path(ns['__file__']).read_text().split('rows=[];stats=Counter()')[0],ns);V,out,cv,string,NS,EW,test=[ns[k]for k in('V','out','cv','string','NS','EW','test')];xy=lambda p:[int(p.real),int(p.imag)];cin=lambda w,h:[i for i,a in enumerate(w)if a==h];cout=lambda w,h:[i for i in range(len(w))if out(w,i)==h];Cs=[w for w in EW if len(cin(w,1))==2 and len(cout(w,0))==2];assert set(map(string,Cs))=={'EEW','WEE','EEWW','EWWE','WEEW','WWEE'}and set(J['C_complete_domain'])==set(map(string,Cs))
counts=Counter();allkept=[]
for root in base['roots']:
 for rx in root['cyclic_necessary_profiles']:
  hs0={complex(*ast.literal_eval(p)):cv(w)for p,w in rx['histories'].items()};cc=Counter();kept=[]
  for b,c in product(('SSNN','SNNS'),Cs):
   hs=hs0|{1-1j:cv(b),2-1j:c};r,witness=test(hs);kind={'skipped':'skipped_rank','clock':'clock','open':'open'}.get(r,r);cc[kind]+=1
   if r!='open':assert r=='skipped';continue
   assert b=='SNNS'and string(c)in('WEE','WEEW');succ={}
   for p,w in hs.items():
    for h,v in enumerate(V):
     if p+v not in hs:continue
     a=cout(w,h);bb=cin(hs[p+v],h);assert len(a)==len(bb);succ.update({(p,i):(p+v,j)for i,j in zip(a,bb)})
   path=[(2-1j,1)]
   while path[-1]!=(2-1j,2):assert len(path)<20;path.append(succ[path[-1]])
   word=''.join('R'if i%2==0 else'L'for p,i in path[:-1]);assert word==('LLRRRRLL'if rx['kind']=='P'else'LLRRLLLLRRLL');assert path[:3]==[(2-1j,1),(2+0j,1),(1+0j,2)]and path[-3:]==[(1+0j,3),(1-1j,3),(2-1j,2)]
   kept.append(dict(B=b,C=string(c),word=word,literal_return=[[xy(p),i]for p,i in path],Delta12=len(path)-1))
  ref=next(r for r in J['rows']if r['root']==root['root']and r['reaction']==rx['kind']and r['counts']==dict(cc))
  # There are two N reaction inventories per root; distinguish their literal paths.
  ref=next(r for r in J['rows']if r['root']==root['root']and r['reaction']==rx['kind']and {json.dumps(v,sort_keys=True)for v in r['survivors']}=={json.dumps(v,sort_keys=True)for v in kept})
  assert len(kept)==2 and ref['counts']==dict(cc);counts.update(cc);allkept.extend(kept)
assert dict(counts)==J['all72_counts']and counts=={'skipped_rank':60,'open':12}
# Direct role checks retain both C3/C4 and R3/R4, and distinct positive/negative D suppliers.
assert out(cv('SNNS'),0)==3
assert len(cin(cv('WEE'),3))==1 and len(cout(cv('NNS'),1))==1
assert out(cv('WEE'),0)==out(cv('WEEW'),0)==0
assert cout(cv('WEE'),0)[1]==cout(cv('WEEW'),0)[1]==cin(cv('WEE'),1)[0]==cin(cv('WEEW'),1)[0]==1
reports=['check_cyclic_LL_reactivation_independent.json','check_LL_reactivation_disjoint_independent.json','check_LL_RR_matching_independent.json','check_LL_post_X_RR_cap_independent.json'];deps={}
for f in reports:
 p=S.with_name(f);assert json.loads(p.read_text())['status'].startswith('PASS');deps[f]=sha(p)
O={'status':'PASS complete72 nested-reader interface, genuine XY cap and off-this-Gamma reader injection','proof':sha(P),'certificate':sha(C),'script':sha(S),'counts':dict(counts),'complete_C_domain':list(map(string,Cs)),'twelve_open_necessary_rows':allkept,'signed_dependencies':deps,'analytic_review':['Allcomplete capfour C histories are allowed, not justE-first: exactEin2/Nout2 gives sixwords. Independent existingphysicalrank/clock/height checker rejects60 of72 products by literal nextrank failure andretains exactly12. These necessaryopens arenot actualfactors.','The three E-first words and passiveWWEE have secondE<=secondN, whereas known ports force secondE>X3>X2>secondN. RemainingWEE/WEEW sharefirstE=secondN=L1. B=SSNN wouldsupplythat firstE afterX3, contradiction, so every genuinepostX partnerisSNNS/Y. Exact C1->R1->X2 andX3->B3->C2 give Cgap8/12 withfull literalwordsLLRRRRLL/LLRRLLLLRRLL.','C LEFTonGamma wouldneed predecessorB departingE, butB.R0departsW. C RIGHTwouldgo toR; WEE hasoneuseincomingW, while WEEW makesa forbiddenYX RRcap ifRNNSS, andRNNS hasoneuseoutgoingE. ThusCoffGamma. RRIGHTwouldneedC; RLEFTwouldneedDdepartS. NegativeDfirstWdepartsN; positiveD EWWE alreadyoffGammabyits actual LEFTarrivalR0, incompatiblewitheveryGammaR0 RIGHT. Full-drift copiescannotcreate another physicalpredecessor.','OffGammaR followsgeometricLEFT intoX.R2, andC followsintoR, so theirwhole historiesareontheLEFT side. Theexisting signedX reactivation channel, theactualflatY B.L3 andoffGamma endpointsmake the entireextendedreturnpartofONE actualLEFTowner, notanadded independentowner. EarlierC.R0 andoptionalL3 remain.','EachactualC.L1 successorchain determinesR.L1 thenX.R2; equalityup tofulldrift thereforedetermines the sameXclass anditsunique precedingLLroot. Thisproves rootclass->Cclass injection, not ownerinjection ordisjointfuel. OddC is anoutputclass; evenC remainsunpaidoldstock, withnoiteration, completion orglobalexclusion claim.']};S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))

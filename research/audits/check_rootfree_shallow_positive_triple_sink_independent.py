from pathlib import Path
import hashlib,json
S=Path(__file__).resolve();R=S.parents[1];D=R/'K1_pipeline_detours_2026-10-23';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();note=D/'rootfree_shallow_valley_forces_unmatched_positive_triple_sink.md';assert sha(note)=='aa7dadc25df6d4c1b071c027e436824166159e9c25112da4cf5d78f233c41eae'
H='NESW';V=(1j,1,-1j,-1);rev={'Z':'WWWE','A':'NNSN','B':'EEWE','Y':'NNNS'};orig={}
for c,word in rev.items():
 q=[H.index(z)for z in word];revout=[(z+(1 if i%2==0 else-1))%4 for i,z in enumerate(q)];orig[c]=''.join(H[(z+2)%4]for z in reversed(revout))
assert orig=={'Z':'SSNS','A':'EEEW','B':'SSSN','Y':'WWEW'}
pos={'Z':0j,'A':1+0j,'B':1+1j,'Y':1j};step={'Z':('A',0),'A':('B',-1),'B':('Y',0),'Y':('Z',0)};rows=[]
out=lambda word,i:(H.index(word[i])+(1 if i%2==0 else-1))%4
for s,(t,shift)in step.items():
 delta=pos[t]+2j*shift-pos[s];direction=V.index(delta);sr=[i for i in range(4)if out(orig[s],i)==direction];tr=[i for i in range(4)if H.index(orig[t][i])==direction]
 assert len(sr)==len(tr)==3 and (sr[1],tr[1])==(2,1)
 matched=1 in sr and 2 in sr and 1 in tr and 2 in tr and[sr.index(1),sr.index(2)]==[tr.index(1),tr.index(2)];assert not matched
 # Repair at target sends incomingL1 to outgoingR2; exactly the next G3edge.
 nt,nsh=step[t];nd=pos[nt]+2j*nsh-pos[t];assert V[out(orig[t],2)]==nd
 rows.append(dict(source=s,target=t,target_k_shift=shift,travel=H[direction],source_ranks=sr,target_ranks=tr,actual_rank_pairs=list(map(list,zip(sr,tr))),middle_source_rank=2,middle_target_rank=1,matched_rank12=False))
ref=json.loads((D/'rootfree_axis_rail_original_triple_cycle.json').read_text());assert orig==ref['original_histories']and rows==ref['ports']
# Literal oneunit geometry and turns; no actual front supplied.
pts=[0j,1+0j,1-1j,-1j,-2j];dirs=[V.index(b-a)for a,b in zip(pts,pts[1:])];turns=[(dirs[i]-dirs[i-1])%4 for i in range(4)];assert dirs==[1,2,3,2]and turns==[3,1,1,3]
controls=[]
for a in [1,2,3,7,31]:
 p=[z-2j*k for k in range(a)for z in pts[:-1]];keys={(int(z.real),int(z.imag)%(2*a))for z in p};assert len(p)==len(keys)==4*a;assert pts[-1]-2j*(a-1)==-2j*a;controls.append({'a':a,'distinct_full_drift_cells':len(keys),'winding':1})
bindings={n:sha(S.with_name(n+'.json'))for n in ['check_reverse_rootfree_locked_axis_independent','check_matched_rank12_erasure_independent','check_rootfree_valley_left_defect_independent']}
outp={'status':'PASS root-free shallow reverse-axis rail forces an original positive unmatched G3(M) sink circle','author_note':sha(note),'author_fixed_inventory':sha(D/'rootfree_axis_rail_original_triple_cycle.json'),'dependencies':bindings,'original_histories':orig,'ports':rows,'full_drift_controls':controls,'analytic_review':[
'Read-event reversal maps originalincoming to negative reverseOUTGOING and reversesrankorder, not merelynegativeincoming. Fresh four-history inversion gives SSNS/EEEW/SSSN/WWEW. Physicalpositions and k-shifts give Zk→Ak→B(k-1)→Y(k-1)→Z(k-1), E,S,W,S displacement0,-2.',
'Signed root-freeM-3 reverse WHITE-collar theorem fixes full reversedrift0,2a, notprimitive2. Actualoriginalfullquotient has exactly4a distinctcirclecells: x0/1 and yparityseparateroles,kmoda separatesthe rest. Its totaldisplacement is originald0,-2a so winding+1. Eachvertex hasunique tripleinput/output, allleftLfacesbelongQ and rightCheightM bysigned G3preservation anddifference3.',
'All four completeordinaltables include R0/L3 and middle sourceR2→targetL1. Canonicalrepair swaps1/2, so nodeincomingL1→outgoingR2 atEVERYcell. It lies at middle sheetM-1 and every incidentexchange ispositive, a clocksink. AllfourphysicalportsareUNMATCHED: exactordinalshifts prevent sourceL1/R2→targetL1/R2. Thus noincidentexchange iserasedbythe signedmatched-pair reduction.',
'For each successiveedge actualT1(next)=T2(current)+1. StartingatoneT1, itspositivewaittoT2 andthenunitphysicalstep give the nextT1. Monotonicityandfullwinding+1 imply these4a waitsandstepspartitionONEactualPinterval, P=4a+sumDelta. SamephysicalcellgapDelta positive4multiple givesP>=20a=10||d||inf; notadditivewithothercurrentbounds. R0/L3 occurwithinthisactualpartition, notdiscarded.',
'CanonicalcornerwordLRRLcyclicLLRR isnotmax-facebirthword, so no-LL birththeoremcannotexcludeit. ExistingpreparedW20sinksneedexplicitinputfuel anddonotrealizecompleteWHITEfront. Only thisconditionalcircleisclassified, notallG3components,supplierassemblies orcontrollers; LEFTodd-or-deeperalternative remainsnoninjective.' ]}
S.with_suffix('.json').write_text(json.dumps(outp,indent=2)+'\n');print(outp['status'])

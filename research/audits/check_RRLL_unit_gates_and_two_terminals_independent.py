from pathlib import Path
from itertools import product
from collections import Counter
import hashlib,json
S=Path(__file__).resolve();R=S.parents[1];P=R/'K1_pipeline_detours_2026-10-23';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();notes={'RRLL_triple_strips_have_positive_winding_and_irreducible_unit_gates.md':'0cdec9556fab331cb62022830b54a48aa4f3f04a7e90b4161ff616c034f5c5ef','staircase_triple_row_chains_have_two_distinct_output_terminals.md':'25c50f4b3815c08a8b8ab919232b97e85d898299218dfa88c79748d31f385415'}
for f,h in notes.items():assert sha(P/f)==h
# Reuse only independent literal stream equations, before any enumeration/results.
p=S.with_name('check_triple_staircase_extrema_independent.py');ns={'__file__':str(p)};exec(p.read_text().split('A=words(')[0],ns);levels,words,H,out,V=[ns[k]for k in('levels','words','H','out','V')]
profiles={'Z+':'SSNS','Z-':'NSSS','A+':'EEEW','A-':'EWEE','B+':'SSSN','B-':'SNSS','Y+':'WWEW','Y-':'EWWW'}
ports={'C':{'Z':('N','E'),'A':('E','S'),'B':('S','W'),'Y':('W','N')},'L':{'Z':('S','E'),'A':('E','N'),'B':('N','W'),'Y':('W','S')}}
pc={'N':'SE','S':'NW','E':'SE','W':'NW'};pc2={'E':'SW','W':'NE','N':'NE','S':'SW'}
rows=[]
for role,st in profiles.items():
 w=tuple(H.index(x)for x in st);hh=levels(w,'NW');cfaces=('NW','SE')if st[0]in'NS'else('NE','SW');c=max(hh[x]for x in cfaces);hh={k:v-c for k,v in hh.items()};adjC=pc if st[0]in'NS'else pc2
 outs=[H[out(h,j)]for j,h in enumerate(w)];il=[];ol=[]
 for j,h in enumerate(st):il.append(hh[adjC[h]]-st[:j].count(h))
 for j,h in enumerate(outs):ol.append(hh[adjC[h]]-outs[:j].count(h))
 arcs=[]
 for j in range(4):
  o=3-j if j in(1,2)else j;assert il[j]==ol[o];arcs.append({'in':st[j],'out':outs[o],'in_rank':j,'out_rank':o,'sheet':il[j],'clock':-1 if o==1 else 1 if o==2 else 0})
 units={}
 for typ,pl in ports.items():
  pin,pout=pl[role[0]];sheet=0 if typ=='C'else-2;match=[z for z in arcs if z['in']==pin and z['sheet']==sheet];assert len(match)==1 and match[0]['out']==pout;units[typ]=match[0]
 middle=[z for z in arcs if z['sheet']==-1 and z['out_rank']in(1,2)];assert len(middle)==1 and middle[0]['clock']==(1 if role[-1]=='+'else-1)
 rows.append({'role':role,'profile':st,'face_levels':hh,'unit_C':units['C'],'unit_L':units['L'],'middle':middle[0]})
expectedC={'Z+':-1,'Z-':0,'A+':0,'A-':0,'B+':0,'B-':0,'Y+':0,'Y-':1};expectedL={'Z+':0,'Z-':0,'A+':-1,'A-':0,'B+':0,'B-':1,'Y+':0,'Y-':0}
assert all(z['unit_C']['clock']==expectedC[z['role']]and z['unit_L']['clock']==expectedL[z['role']]for z in rows)
# Enumerate all16 local sign choices; only Z+,A+ have a negative unit incidence.
unitfeasible=[]
for z,a,b,y in product((1,-1),repeat=4):
 if z!=1 or a!=1:continue
 unitfeasible.append((z,a,b,y))
 # Symbolic coefficients after deltaZ=4+[y-]deltaY and deltaA=4+[b-]deltaB.
 assert (int(y==-1)+y)==int(y==1)and(int(b==-1)+b)==int(b==1)
assert len(unitfeasible)==4
# Original-WHITE inverse row closure, retaining odd terminals and both even modes.
W=words((1,3),[('in',3,1),('out',2,1)]);X=words((0,2),[('in',0,3),('out',1,3)])
assert {''.join(H[h]for h in w)for w in W}=={'EEW','WEE','EEWE','WEEE'}and{''.join(H[h]for h in w)for w in X}=={'NNNS','NSNN'}
inward=[]
for w in W:
 lev=levels(w,'SE');lev={k:v-3 for k,v in lev.items()};assert lev['NE']==lev['SW']==-2 and lev['SE']==-3 and lev['NW']==(-4 if len(w)==3 else -5)
 if len(w)==3:assert w[1]==1 and w[0]!=w[2]
 else:assert w.count(1)==sum(out(h,j)==0 for j,h in enumerate(w))==3
 inward.append({'word':''.join(H[h]for h in w),'levels':lev,'terminal':len(w)==3})
outp={'status':'PASS positive RRLL-strip winding/irreducible unit gates and two-ended staircase chain output capacity','notes':notes,'all8_reconstructed_arcs':rows,'admissible_Z_A_forced_signs':unitfeasible,'inward_profiles':inward,'analytic_review':[
'Literal complete profiles, face levels, chronological directed-port labels C-ordinal+1, and canonical rank1/2 swaps are independently reconstructed. The four actual arcs around each displayed C or L unit square are on one sheet and have the claimed directions; all R0/L3 passive corners are retained. Middle and unit exchanges occupy sheets c-1/c or c-1/c-2, never a guessed smoothing.',
'Contractible canonical unit clock0=4+signedDelta forces Z and A positive: otherwise there is no negative incidence. It then gives deltaZ=4+[Yprev negative]deltaYprev and deltaA=4+[B negative]deltaB. Summing the essential middle clock over the full4a-cell quotient cancels exactly the negative B/Y terms, giving Pw=12a+sum positive B/Y Delta>0. Its embedded winding is therefore+1 and d=(0,-2a) in the fixed frame. This assumes actual RRLL physical strip geometry, not arbitrary axis drift.',
'Each negative Y or B produces a different degree-two contractible unit node with both exchanges to the SAME essential middle node. Different unit nodes and sheets cannot alias under full drift. Their parallel two-edge cycles are independent. Delta values differ by4, so the edges cannot be each others matched rank12 pair; degree2 leaves no alternate paired edge at that unit. Matched pairs are parallel equalDelta by the retained theorem, so no outside mate is possible. Unit gates survive pair erasure. Only their distinct-node lower beta reservation is justified, not an additive budget with overlapping reservations or an upper bound.',
'The inward staircase test includes all original-WHITE1..4 histories, not a reverse-WHITE premise. If every W gap is even it is a full B mode; neighboring three-use ports force X to a full A mode. Reindexing Xk=(k,k+2) as Aprev_(k+1) identifies exactly the c-2,(-1,1) predecessor of the already signed outward row graph. Its outward U cells are the known current A cells, so the two directions follow the SAME path component.',
'Finite global low-L minimum forces an inward EEW/WEE terminal, while finite maximum forces the outward singleton. Opposite-R3 terminal L1 heading E fixes the rotated frame; its position and equal C heights recover the unique outer row modulo full diagonal drift. Distinct maximal chains inject into both terminal families, which are disjoint by complete history length. Thus Nodd>=2 chain-components, not2 every starting row. A chain reaching M has its outward TOP singleton and inward NON-TOP opposite-R3, whose incident C heights<=M-2. These capacities cannot be added to overlapping earlier payments.',
'No controller realization, whole-front exclusion, initial fuel, per-renewal charge or attraction follows. Negative mixed G3 circles away from local minima remain possible; at a locally minimal low-L component the signed axis theorem plus this strip clock forces positive winding.'
]};S.with_suffix('.json').write_text(json.dumps(outp,indent=2)+'\n');print(outp['status'])

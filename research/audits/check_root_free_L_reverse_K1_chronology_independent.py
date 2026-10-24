from pathlib import Path
from itertools import product
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'K1_pipeline_detours_2026-10-23';vec={'N':1j,'E':1,'S':-1j,'W':-1};name={v:k for k,v in vec.items()};rows=[]
for hs in product('NS',repeat=4):
 incoming=[vec[c]for c in hs];out=[v*(-1j if i%2==0 else 1j)for i,v in enumerate(incoming)];rev=[-v for v in reversed(out)]
 if not(rev[0]==rev[1]and rev[2]==-rev[0]):continue
 assert incoming[1]==incoming[2]==-incoming[3];H=incoming[1];direction=(1+1j)*(H/1j)
 def side(v):return 'LEFT'if(direction.conjugate()*v).imag>0 else'RIGHT'
 sides=[[side(-a),side(b)]for a,b in zip(incoming,out)];assert sides[1:]==[['RIGHT','LEFT'],['RIGHT','RIGHT'],['LEFT','RIGHT']]
 top=incoming[0]==H;assert sides[0]==(['RIGHT','RIGHT']if top else['LEFT','LEFT'])
 Rs=Counter(hs[::2]);Inc=Counter(hs);cs={'NW':0,'SE':Rs['N']-Rs['S']};ls={'NE':-Inc['S'],'SW':cs['SE']-Inc['N']};assert len(set(ls.values()))==1;m=ls['NE'];C={k:v-m for k,v in cs.items()};L={k:v-m for k,v in ls.items()};assert sorted(C.values())==([1,3]if top else[2,2])
 if top:
  maxsector=1-1j if C['SE']==3 else-1+1j;assert side(maxsector)=='RIGHT'
 rows.append({'word':''.join(hs),'reverse_incoming':''.join(name[v]for v in rev),'C_minus_m':C,'L_minus_m':L,'sides':sides,'type':'TOP'if top else'FLAT'})
assert len(rows)==4 and {z['word']for z in rows}=={'NNNS','SNNS','SSSN','NSSN'}
# Formal reverse rank/index map, rather than testing arbitrary timestamps.
# Reverse K1 sequence tau0(k),tau2(k-1),tau1(k),tau0(k+1),tau2(k),tau1(k+1).
revseq=[(0,0),(2,-1),(1,0),(0,1),(2,0),(1,1)];rank={0:3,1:2,2:1,3:0};forward=[(rank[r],-offset)for r,offset in reversed(revseq)]
assert forward==[(2,-1),(1,0),(3,-1),(2,0),(1,1),(3,0)]
files=['root_free_L_plateau_forward_reverse_K1_chronology.md','root_free_L_plateau_forward_reverse_K1_controls.py','root_free_L_plateau_forward_reverse_K1_controls.json'];hashes={f:hashlib.sha256((D/f).read_bytes()).hexdigest()for f in files};assert hashes[files[0]]=='fc0f63b9e95041463800e7736afe608d5c201a456bc4a9ac5dbbfb8b93fdfcb6'
A=json.loads((D/files[2]).read_text())['rows'];assert{z['word']for z in rows}=={z['forward_headings']for z in A}
for a in A:
 z=next(z for z in rows if z['word']==a['forward_headings']);assert z['reverse_incoming']==a['reverse_headings']and z['sides']==a['side_inventory']and z['C_minus_m']==a['C_minus_m']
out={'status':'PASS root-free L-plateau reverse-K1 to exact forward rank-two chronology','source_hashes':hashes,'fresh_four_complete_rows':rows,'formal_forward_rank_and_index_offsets':forward,'analytic_review':[
'No odd incident corner means the entire Q collar is reverse-WHITE, not the whole reversed board. Signed prepared plateau positivity and selected-contact cursor theorem apply there. At m=M-3 and K1 forward c_left=M-2, reverse retreat is1. Each selected reverse birth has at least3 reads; original evenness then makes exactly4, so the four-rank map is exhaustive.',
'The exact read-event conjugacy is reverseincoming=-forwardOUTGOING on the postflip board, with eventtime -t. Reversing the reverse-parent order k=-j and its K1 six-event chain gives exactly T2(j-1)<T1(j)<T3(j-1)<T2(j)<T1(j+1)<T3(j). Full quotient seams give j+ell translated+d and times+P, without primitive-period reduction.',
'Fresh16 N/S four-read possibilities leave4 rows, or TOP NNNS and FLAT SNNS up to rotation. Both L sectors equalm. TOP C heights arem+3 andm+1, FLAT bothm+2. Full forward crossing list: L1 RIGHTtoLEFT, R2 staysRIGHT,L3 LEFTtoRIGHT, R0 staysRIGHT inTOP andLEFT inFLAT. No occurrence is erased or assigned to an unjustified nearest excursion.',
'The TOP global-C maximum sector is geometrically RIGHT of the forward-oriented Lcut. Its original R0 uses that actual face boundary; the preceding boundary departure is atT0-1, so its canonical first boundary birth is no later. Two actual same-cell return gaps>=4 give B_C<=T2-9. This is one clock comparison, not an ancestry cycle or additive resource.',
'Reverse BLACK odd-output histories away fromQ remain in the actual currents. Existing global zero-output whole-front machinery cannot be imported to those helper cells. The shared valley may touch different maximum components through other contacts; one-sided selected TOP adjacency does not exclude that.'
],'scope':'Complete WHITE cap-four K1 original front with positive required output; locally minimal m=M-3 L plateau with no odd incident corner. Conditional essential reverse curve chronology, not exclusion, realization, or global reverse-WHITE claim.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])

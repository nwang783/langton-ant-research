from pathlib import Path
from collections import Counter
import ast,json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'K1_pipeline_detours_2026-10-23';A=json.loads((D/'prepared_D102_black_helper_connected_control.json').read_text());word=A['word'];seed={complex(*q)for q in A['prepared_black']};B=set(seed);p=1+0j;h=0;H='NESW';trace=[];hist={};states=[]
for t,c in enumerate(word):
 assert('L'if p in B else'R')==c;out=(h+(1 if c=='R'else-1))%4;r={'time':t,'cell':[int(p.real),int(p.imag)],'incoming':H[h],'turn':c,'outgoing':H[out]};assert r==A['trace'][t];trace.append(r);hist.setdefault(p,[]).append(r);states.append(sorted((int(q.real),int(q.imag))for q in B));B^={p};h=out;p+=1j*(-1j)**h
assert(len(word),len(seed),len(B),p,h)==(102,17,9,3j,0);assert sorted((int(q.real),int(q.imag))for q in B)==list(map(tuple,A['final_black']));assert Counter(word)=={'R':47,'L':55};assert len(hist)==44 and max(map(len,hist.values()))==4
for z,hh in A['known_headings'].items():
 q=complex(*ast.literal_eval(z));rr=hist[q];assert ''.join(r['incoming']for r in rr)==hh;assert ''.join(r['turn']for r in rr)==('L'if q==-2+2j else'RLRL');assert(q in seed)==(q==-2+2j)
faces=dict(D=0j,J=-1-1j,P0=-2,I=-1+1j,G=1+1j);bounds={}
for n,f in faces.items():
 ports=[(f+1,'W'),(f,'N'),(f+1j,'E'),(f+1+1j,'S')];tt=[min(r['time']for r in hist[q]if r['outgoing']==o)for q,o in ports];bounds[n]=tt;assert min(tt)==A['first_boundary_times'][n]
assert {n:min(t)for n,t in bounds.items()}==dict(D=4,J=9,P0=24,I=39,G=43)
route=[(-1+1j,2),(-1+2j,1),(-2+2j,0),(-2+1j,3),(-1+1j,3)];assert[hist[q][k]['time']for q,k in route]==[51,52,53,54,55]and ''.join(hist[q][k]['turn']for q,k in route)=='RLLLL'
old=json.loads((D/'prepared_D158_connected_late_parent_control.json').read_text());assert word==old['word'][:53]+'L'+old['word'][78:126]
files=['prepared_D102_black_helper_connected_control.md','prepared_D102_black_helper_connected_control.py','prepared_D102_black_helper_connected_control.json'];hs={f:hashlib.sha256((D/f).read_bytes()).hexdigest()for f in files}
out={'status':'PASS literal finite preparedD102 BLACK-helper control, no global front/controller claim','source_hashes':hs,'fresh_all102_reads':trace,'fresh_all_precut_complete_boards':states,'final_complete_board':sorted((int(q.real),int(q.imag))for q in B),'first_directed_boundary_departures':bounds,'analytic_review':[
'The explicit complete17-black seed, with every other cell WHITE, executes the supplied102-turn word without any intervention. Fresh physical colors, positions, incoming/outgoing headings and every complete finite board match. It ends(0,3,N) with9black cells after47R/55L, and no cell is read more than4times in the entire factor.',
'All15 designated package cells start WHITE and realize exactly their full within-factor RLRL histories; f(-2,2) startsBLACK and has the singleL incomingW. The five directed boundary first-departure times are4,9,24,39,43, reconstructed independently from actual physical outgoing edges, not copied local-solver clocks. The actual51..55 five-read route is RLLLL.',
'The word equals exactly the stated prescribed D158 splice old[:53]+L+old[78:126]. This confirms the one-word construction without an exterior search. The previous failed same-seed bit edit is not a premise of this verification and is not treated as a successful control.',
'The directed boundary chronology does not establish a bi-infinite global maximum-face parent graph or assign globally consistent stream heights. Complete within-factor histories do not prohibit later revisits. Reversal starts from the full nine-black exit field and changes event conventions; neither direction is a complete WHITE front or an autonomous/regenerative controller. This is a genuine finite connected helper possibility, not indefinite supply or a capture counterexample.'
]}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])

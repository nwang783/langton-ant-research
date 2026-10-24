from pathlib import Path
from collections import defaultdict
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();files={'STANDARD_LIFETIME_CYCLE_DELETION_COUNTERCHECK.md':'4ce5bbc12b766d5c02566ccca641c22874ced9a2a4e21722ff54915004b4c7e4','certify_standard_lifetime_cycle_deletion.py':'2f8f1811b26a5c5a27579ccb653f46d22fafc7c022e899b9d624226e86a8cba2','standard_lifetime_cycle_deletion_certificate.json':'1b708039f476ea970b1dfeeddfabce47afc0af012fbbbdfa7d6cb738c521abac'}
for f,h in files.items():assert sha(D/f)==h
J=json.loads((D/'standard_lifetime_cycle_deletion_certificate.json').read_text());signed=R/'audits/check_lifetime_boundary_graph_independent.json';assert sha(signed)=='2146e0898133417c220dbd595812f59308252169dbdeaa0d4c812fd9e5d933dc'
for f,h in J['dependency_hashes'].items():assert sha(D/f)==h
W=json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];assert hashlib.sha256(W.encode()).hexdigest()==J['standard_word_sha256'];C=json.loads((D/'lifetime_boundary_graph_certificate.json').read_text())['controls']['S104']['graph']['internal_cycles'];C=[set(x['events'])for x in C];assert list(map(sorted,C))==J['five_complete_internal_components'];assert sum(map(len,C))==len(set.union(*C))and sorted(map(len,C))==[2,2,2,2,14]
for c in C:assert sum(1 if W[i]=='R'else-1 for i in c)==0
V=[1j,1,-1j,-1];xy=lambda p:[int(p.real),int(p.imag)];seen=set();out=[]
for mask,row in enumerate(J['all31_cases'],1):
 selected=[i for i in range(5)if mask>>i&1];cut=set().union(*(C[i]for i in selected));w=''.join(c for i,c in enumerate(W)if i not in cut);assert selected==row['selected_component_indices']and sorted(cut)==row['deleted_event_phases']and w==row['remaining_word']and w not in seen;seen.add(w);p=0j;h=0;events=[]
 for i,c in enumerate(w):events.append(p);h=(h+(1 if c=='R'else-1))%4;p+=V[h]
 d=p;assert h==0 and d!=0 and xy(d)==row['full_drift']and len(w)==row['period']and w.count('R')-w.count('L')==12;H=defaultdict(list);coord=(lambda z:int(z.real))if d.real else(lambda z:int(z.imag));D0=coord(d)
 for i,q in enumerate(events):
  k=coord(q)//abs(D0)*(1 if D0>0 else-1);r=q-k*d;H[r].append(dict(phase=i,full_lift=k,stable_clock=i-k*len(w),position=xy(q),turn=w[i]))
 for a in H.values():a.sort(key=lambda z:z['stable_clock'])
 wit=row['literal_non_alternation_witness'];hist=H[complex(*wit['full_class_representative'])];assert hist==wit['complete_stable_class_history'];a,b=wit['earlier'],wit['later'];i=hist.index(a);assert hist[i+1]==b and a['turn']==b['turn'];out.append(dict(mask=mask,period=len(w),drift=xy(d),conflict_phases=[a['phase'],b['phase']],conflict_turn=a['turn']))
assert len(out)==31
result=dict(status='PASS all31 nonempty standard internal-component phase deletions fail repetition on every board',script=sha(S),files=files,signed_graph=sha(signed),cases=out,analytic_review=['Each selected complete internal component has zero R-minus-L count. Removing arbitrary unions preserves heading and turn excess12, but is not assumed to preserve spatial trajectory. Every remaining word is recomputed from scratch.','Each witness lists a COMPLETE physical full-drift class sorted by actual stable time, not raw phase. The two displayed consecutive identical turns forbid that repeated infinite word under ANY initial color at that cell, including BLACK-first and infinite prepared input. Axis resulting drifts are handled with a nonzero-coordinate quotient, not the non-axis graph hypothesis.','All31 words are distinct and every nonempty subset is covered. Cyclic cut changes and rigid rotations only relabel the same deletion surgery. No alternative reconnection, reorder, broader surgery family, physical internal-cycle deletion or controller uniqueness is excluded.']);S.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(result['status']);print(sha(S.with_suffix('.json')))

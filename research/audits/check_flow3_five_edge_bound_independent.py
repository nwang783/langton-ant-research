from pathlib import Path
from itertools import product
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();proof=D/'global_max_flow3_segments_have_at_most_five_edges.md';assert sha(proof)=='0a4a6a90cce92d158bc438fb8e53149c3608e454f9b6d6688ae92276c6627a0b'
J=json.loads((D/'flow3_segment_turn_reduction_control.json').read_text());dep=json.loads((R/'audits/check_maximal_departure_segments_independent.json').read_text());assert dep['bindings']['maximal_flow2_flow3_departure_segments.md']=='b955fed15a4e99779763667a44e3bbf32e06b184758f9977d42465f91130c50b'
V={'N':1j,'E':1,'S':-1j,'W':-1};I={v:k for k,v in V.items()};out=lambda w:[I[V[h]*(-1j if r%2==0 else 1j)]for r,h in enumerate(w)];pos={'Z':0j,'A':1,'B':1-1j,'Y':-1j};rows=[]
for a,b in product(['EEEW','EWEE'],['SSSN','SNSS']):
 hs=dict(Z='NSSS',A=a,B=b,Y='EWWW');succ={}
 for x,y,d in [('Z','A','E'),('A','B','S'),('B','Y','W'),('Y','Z','N')]:
  assert pos[x]+V[d]==pos[y];sr=[r for r,h in enumerate(out(hs[x]))if h==d];tt=[r for r,h in enumerate(hs[y])if h==d];assert len(sr)==len(tt)==(1 if x=='Y' else 3)
  for r,t in zip(sr,tt):succ[x,r]=(y,t)
 assert[succ[z]for z in[('Z',0),('A',0),('B',0),('Y',2)]]==[('A',0),('B',0),('Y',1),('Z',0)]
 rec=next(r for r in J['LRRL_rows']if r['histories']==hs);assert rec['missing_edge_flow']==1
 rows.append(hs)
# Reconstruct full right transition types, retaining odd endpoints and one-use rerouting.
starts={};ends={}
for n in range(1,5):
 for tail in product('EW',repeat=n-1):
  w='E'+''.join(tail);f=w.count('E');g=out(w).count('S')
  if g==3 and f!=3:starts[w]=(f,g)
  if f==3 and g!=3:ends[w]=(f,g)
assert starts=={'EWE':(2,3),'EWWW':(1,3)}and ends=={'EEE':(3,2),'EEWE':(3,1)}
templates=['RR']+['R'*a+'L'*b+'R'*c for b in(1,2)for a in(1,2)for c in(1,2)]
assert set(templates)==set(J['necessary_turn_templates'])and len(templates)==9 and max(len(w)-1 for w in templates)==5
outj=dict(status='PASS at-most-five physical edges for maximal open flow3 b-segments at locally maximal selected C',proof_sha256=sha(proof),control_sha256=sha(D/'flow3_segment_turn_reduction_control.json'),four_LRRL_rows=rows,source_types=starts,sink_types=ends,nine_necessary_templates=templates,max_edges=5,analytic_review=[
'All four LRRL profile choices give physical ordinal equations Z0->A0->B0->Y1 and Y2->Z0 across the real missing square edge of total flow1. Thus T1Y=T2Y+4, contrary to T2Y>=T1Y+4. No height, period, exterior or uninterrupted-cursor assumption needed.',
'Signed b955 local LRL obstruction uses only the two internal LEFT profiles, either internal RIGHT sign and true outside supplier. Its higher adjacent C face contradicts local maximality. Endpoints cannot be LEFT because the complete constant-selected-C LEFT inventory preserves physical multiplicity.',
'An embedded essential unit-grid b-circle cannot contain three identical successive turns: their four physical edges close a contractible square. This includes edges beyond a maximal segment endpoint because the full b-circle is embedded.',
'Two separate LEFT runs in the segment would have one or two RIGHT turns between them, producing forbidden LRL/LRRL. Hence at most one LEFT run of length<=2, with RIGHT endpoint runs of length1/2. The complete nine templates have at most six vertices/five edges; no maximum length was guessed or scanned.',
'Closed all3 is already excluded at local C maximum by signed b955. One-use rerouting EWWW/EEWE is retained; no number-of-segments, age, period, source fuel, arbitrary b-tree or nonmaximal-C bound follows. Templates are necessary, not attained.'
]);S.with_suffix('.json').write_text(json.dumps(outj,indent=2)+'\n');print(outj['status']);print(sha(S.with_suffix('.json')))

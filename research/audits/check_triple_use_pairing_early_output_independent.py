from pathlib import Path
from itertools import product
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'K1_pipeline_detours_2026-10-23'
notes={'triple_use_current_pairs_top_same_R_outputs.md':'3ffd2f42af3fe147dcc9b13f207343cc1ac82ea06174a9a73a79c25e9507aba6','early_triple_output_via_triple_use_pairing.md':'874d5586c71ca3b2e6c90a093374399c6670457f1e030d3d592d0b2316b431d6'}
for f,h in notes.items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
# Count physical arrivals/departures directly from turns, rather than use author's flow formula.
vec={'E':1+0j,'W':-1+0j,'N':1j,'S':-1j};name={v:k for k,v in vec.items()};sectors={'W':('SW','NW'),'E':('NE','SE'),'N':('NE','NW'),'S':('SW','SE')};rows=[]
for n in range(1,5):
 for hs in product('EW',repeat=n):
  h=''.join(hs);inc=Counter();out=Counter()
  for i,x in enumerate(h):
   v=vec[x];inc[name[-v]]+=1;out[name[v*(-1j if i%2==0 else 1j)]]+=1
  f=inc+out;rE=h[::2].count('E');rW=h[::2].count('W');lE=h[1::2].count('E');lW=h[1::2].count('W');a=-max(rE,rW)
  C={'NE':rW+a,'SW':rE+a};L={'NW':a-lE,'SE':a-lW}
  for p,(c,l)in sectors.items():assert f[p]==C[c]-L[l]
  tp=[p for p in 'WENS'if f[p]==3];di=sum(inc[p]==3 for p in tp);do=sum(out[p]==3 for p in tp)
  if not tp:typ='absent'
  elif len(tp)==1:
   assert n==3 and h[0]==h[2];typ='sink'if h[1]==h[0]else'source';assert(di,do)==((1,0)if typ=='sink'else(0,1))
  else:
   assert n==4 and len(tp)==2 and(di,do)==(1,1);typ='internal'
  assert all(C[sectors[p][0]]==0 and L[sectors[p][1]]==-3 for p in tp)
  ls={sectors[p][1]for p in tp};cs={sectors[p][0]for p in tp}
  if len(ls)==2:assert h[0]==h[2] and len(cs)==1 # cannot be a selected opposite-R curve corner
  if len(cs)==2:assert len(ls)==1
  rows.append({'headings':h,'physical_incoming_ports':dict(inc),'physical_outgoing_ports':dict(out),'C':C,'L':L,'triple_ports':tp,'type':typ,'changes_diagonal_L_face':len(ls)==2})
assert len(rows)==30 and Counter(r['type']for r in rows)=={'absent':18,'sink':2,'source':2,'internal':8}
author=json.loads((D/'triple_use_edge_graph_local_inventory.json').read_text())
for a,b in zip(rows,author['rows']):assert a['headings']==b['headings']and set(a['triple_ports'])==set(b['triple_ports'])and a['C']==b['C']and a['L']==b['L']and a['type']==b['type']
# Project the previously independently signed six-mode joint reservations by physical type.
reservations={'S3':{'shallow':['j singleton','x oppositeR','e oppositeR'],'sinks':['q SSS'],'sources':[]},'S4a':{'shallow':['j singleton'],'sinks':['q SSS','t SSS'],'sources':['r WEW']},'S4b':{'shallow':['j singleton'],'sinks':['t SSS'],'sources':[]},'R3':{'shallow':['x oppositeR','e oppositeR'],'sinks':['q SSS'],'sources':[]},'R4a':{'shallow':['d oppositeR'],'sinks':['q SSS','t SSS'],'sources':['r WEW']},'R4b':{'shallow':['d oppositeR'],'sinks':['t SSS'],'sources':[]}}
for x in ['SSS','WEW']:
 h=x.replace('S','E');r=next(r for r in rows if r['headings']==h);assert r['type']==('sink'if x=='SSS'else'source')
weights={k:len(v['shallow'])+2*len(v['sinks'])for k,v in reservations.items()};rootweights={k:len(v['shallow'])+len(v['sinks'])for k,v in reservations.items()};assert weights=={'S3':5,'S4a':5,'S4b':3,'R3':4,'R4a':5,'R4b':3}and min(rootweights.values())==2
prior=SELF.parent/'check_early_leaf_roles_two_outputs_independent.json';assert hashlib.sha256(prior.read_bytes()).hexdigest()=='e28a37ac7bb15cb61ecbc93485083e3c6a44eb0536cb30cfc4b64016f52482fa'
out={'status':'PASS triple-use spatial endpoint pairing, plateau preservation and early Nodd>=3*n_A projection','note_sha256':notes,'fresh30_physical_port_histories':rows,'types':dict(Counter(r['type']for r in rows)),'signed_reservation_projection':reservations,'top_output_weights':weights,'shallow_plus_pair_root_weights':rootweights,'prior_independent_joint_injection_report_sha256':hashlib.sha256(prior.read_bytes()).hexdigest(),'analytic':[
'Full-pose periodicity has P even and drift checker-parity even, so the physical Manhattan edge direction and incoming-axis type descend to the actual full quotient without a spurious type change. There are finitely many used edge/cell classes. Lifted multiedge incidences are retained.',
'At each fixed C level c, the direct30-history inventory gives only absent vertices, one-input/one-output internal vertices, and odd same-R source/sink endpoints. Both internal ports have C=c,L=c-3. In any finite directed multigraph with these degrees a source path cannot merge, enter a cycle, revisit its source or revisit an internal vertex; it terminates at a distinct sink. Hence source/sink classes pair bijectively and Nsame(c)=2J(c). This is spatial graph incidence, not chronological occurrence matching.',
'Along the path either the right C face is unchanged or its two diagonal sectors at level c meet in the retained C-face graph; likewise for L at c-3. Thus both level components are preserved. I also explicitly checked the selected-curve corner issue: whenever the two L sectors differ, the internal word has equal R headings and is not a selected opposite-R contact. At an opposite-R selected corner with triple ports, both ports share one L sector. Hence low-plateau pairing cannot sneak across the selected curve through a diagonal corner.',
'In an actual inter-max band with minimum<=M-3, shallow top odd classes cannot root the minimum. If there is no non-top root, each top same-R root has its paired endpoint in the same L plateau, strictly in the same band; different spatial bands use different pairs. Rooted bands therefore number at most Nodd-Ntop+J=Nodd-Nshallow-J. The existing disjoint physical-current partition yields P>=6D+12D max(0,r-1-Nodd+Nshallow+J).',
'The previously signed early joint injections supply A0=n_A+2nS3+nR3 mutually distinct shallow top outputs and G=n_A+nS4a+nR4a mutually distinct all-same-heading sinks. Existing r=WEW reservations are sources and are NOT added again. Since J>=G, Ntop=Nshallow+2J>=A0+2G, giving weights5,5,3,4,5,3 and Nodd>=3n_A. Likewise Nshallow+J>=A0+G>=2n_A gives the stated strengthened band-root subtraction.'
],'scope':'Complete WHITE cap4 full-drift front. Pairing itself needs no K1; ordered-band and early-family consequences retain K1 and all actual source hypotheses. No path-length payment, original fuel, manufactured band count, whole-front exclusion or capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])

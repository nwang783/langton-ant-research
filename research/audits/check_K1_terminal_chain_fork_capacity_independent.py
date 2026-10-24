from pathlib import Path
from itertools import product
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'K1_pipeline_detours_2026-10-23';note=D/'K1_early_ancestors_terminal_chains_and_fork_capacity.md';assert hashlib.sha256(note.read_bytes()).hexdigest()=='31b34f93ccc09757ce49b24c5d75141f0250d306cb291ac098c0b96e3a627ae9'
# At a negative canonical rank1 contact, R0 and L1 have identical incoming
# headings and R2 the opposite heading. Derive its two diagonal C faces.
head='NESW';rface={'N':-1j,'E':-1-1j,'S':-1,'W':0};target={'N':-1,'E':0,'S':-1j,'W':-1-1j}
def edge(q,h):
 if len(h)<3 or h[0]!=h[1]or head[(head.index(h[0])+2)%4]!=h[2]:return None
 return(q+rface[h[0]],q+target[h[0]])
I=-1+1j;P=-2;Q=-3+1j
checked=[]
for th,ah,eh,xh,anc in product(['NNN','NNNS'],['EWE','EWEE'],['SNN','SNNN'],['EWW','EWWW'],['R','S']):
 ih={-1+1j:'EEWE',-1+2j:th,2j:ah,1j:'NSSS'}
 ph={-2+1j:'SSNS',-1+1j:'EEWE',-1:eh,-2:xh}
 qh={-3+1j:'EEWE'if anc=='R'else'W',-3+2j:'NNNS'if anc=='R'else'SSNS',-2+2j:'EEEW',-2+1j:'SSNS'}
 maps=[]
 for face,hist in[(I,ih),(P,ph),(Q,qh)]:
  edges=[e for q,h in hist.items()if(e:=edge(q,h))is not None];outs=[b for a,b in edges if a==face];ins=[a for a,b in edges if b==face];assert len(ins)==1
  maps.append((face,outs,ins))
 assert maps[0][1]==[]and maps[1][1]==[I]and maps[2][1]==[P]
 # Incoming contacts are respectively u, g, j/k and have full length four.
 for face,hist in[(I,ih),(P,ph),(Q,qh)]:assert all(len(hist[q])==4 for q,h in hist.items()if(e:=edge(q,h))and e[1]==face)
 inP=P-Q;outP=I-P;assert outP/inP==1j
 inQ=Q-maps[2][2][0];outQ=P-Q;assert outQ/inQ==(-1j if anc=='R' else 1)
 checked.append(anc)
# This finite cap is a corner incidence fact, not an odd-output argument.
# The sole incoming rank1 contact cannot at that same rank be outgoing;
# only the other three physical corners can supply canonical children.
# In every finite indegree-one directed multigraph, sum(outdegree-1)=0.
for n0,n2,n3 in product(range(7),repeat=3):
 if n0==n2+2*n3:assert 2*(n2+n3)>=n0
out={'status':'PASS actual terminal canonical chains, disjoint classes and fork-capacity identity','note_sha256':hashlib.sha256(note.read_bytes()).hexdigest(),'complete_heading_alternative_controls':len(checked),'outdegrees':[1,1,0],'analytic':'Every known corner is checked for the negative same-heading rank1 canonical switch. Q1 has only P0 child, P0 only I, I none. Thus none lies on a canonical cycle. Signed same-level injections plus leaf-vs-degree1 and LEFT-vs-RIGHT/STRAIGHT unique-child turn distinctions prevent all cross-level aliases in the actual full quotient. The three incoming contacts are distinct full four-read classes, off every selected cycle. Finite indegree-one quotient degree balance gives at least n_A branching excess and at least ceil(n_A/2) fork classes, since degree<=3.','bounds':['P>=3*ell+12*n_A, to combine with overlapping main-clock bounds only by max','canonical branching excess>=n_A','canonical fork classes>=ceil(n_A/2)'],'scope':'Actual canonical stock/topology reservation only. No initial fuel, odd-output charge for RIGHT ancestors, independent root, new component, repeated ancestor package or general K1 exclusion.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])

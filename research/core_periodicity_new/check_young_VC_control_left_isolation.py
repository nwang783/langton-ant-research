from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent;GP=R/'chronology_dcuv/literal_residual_geometry.json';G=json.loads(GP.read_text())['geometry'];keep=[0,1,4,5,6,7,8,9];DIR=((0,1),(1,0),(0,-1),(-1,0));suffix=[5,5,5,4,0,7]
def rot(q,h):x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
rows=[]
for a in keep:
 h=(-G[a]['endpoint'][2])%4;e=rot(G[a]['endpoint'][:2],h);p=(-e[0],-e[1]);start=[*p,h];last={};bad=None
 word=G[a]['word']+''.join(G[b]['word']for b in suffix)+G[7]['marker']
 for t,ch in enumerate(word):
  if p in last and last[p][1]==ch:
   bad=dict(cell=p,previous_read=last[p][0],conflicting_read=t,turn=ch);break
  last[p]=(t,ch);h=(h+(-1 if ch=='L' else 1))%4;p=(p[0]+DIR[h][0],p[1]+DIR[h][1])
 assert bad;rows.append(dict(predecessor=a,start_pose=start,conflict=bad,conflict_suffix_phase=bad['conflicting_read']-len(G[a]['word'])))
assert max(r['conflict_suffix_phase']for r in rows)==138
# Freshness: existing window7 already contains every rejection; no new language.
dfa=[]
for k in(5,6,7):
 JP=R/f'chronology_dcuv/literal_factor_dfa_k{k}.json';J=json.loads(JP.read_text());ix={a:i for i,a in enumerate(J['keep'])}
 def accepts(word):
  s=J['initial_class']
  for a in word:
   s=J['transitions'][s][ix[a]]
   if s<0:return False
  return True
 ok=[a for a in keep if accepts([a]+suffix)];assert ok==([0]if k<7 else[]);dfa.append(dict(window=k,suffix_admitted=accepts(suffix),admitted_predecessors=ok,sha256=hashlib.sha256(JP.read_bytes()).hexdigest()))
J=dict(status='AUTHOR_COMPLETE_EIGHT_PREDECESSOR_LITERAL_EXCLUSION_PASS',scope='Only fixed VC,VC,VC,V,D,U suffix; no preceding recurrent8 packet on any board. Existing k7 already encodes this. No generic VC-young3 exclusion.',suffix=suffix,rows=rows,existing_DFA_freshness=dfa,consequence='If this suffix occurs within a complete recurrent8 factor, its firstVC must be the factor first packet. Its entry residual inputs/upper supports therefore fund the target; cannot replace them by an unseen complete8 earlier history.',input_sha256=hashlib.sha256(GP.read_bytes()).hexdigest())
(R/'chronology_dcuv/young_VC_control_left_isolation.json').write_text(json.dumps(J,indent=2)+'\n');print(rows)

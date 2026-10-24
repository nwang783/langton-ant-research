#!/usr/bin/env python3
"""No same-orbit exact-inverse15324 eraser on complete actual output.
One first-principles inverse proposal; no word/cap/phase/horizon search.
"""
from pathlib import Path
from collections import defaultdict
import json,hashlib
P=Path('/workspace/shared/langton/causal_reduction/unit_scale');O=Path(__file__).parent
W=json.loads((P/'prepared4352_output_return_wave.json').read_text())['word'];NF=json.loads((P/'prepared15324_return_normal_form.json').read_text());D=((0,1),(1,0),(0,-1),(-1,0))
p=(13,7);h=0;G=defaultdict(list)
for i,c in enumerate(W):
 a=p[0]%78;G[p[0]-p[1],a].append(((p[0]-a)//-78,i,c));h=(h+(-1 if c=='L'else 1))%4;v=D[h];p=p[0]+v[0],p[1]+v[1]
assert(p,h)==((-65,-71),0)
for g in G.values():g.sort(key=lambda a:(-a[0],a[1]));assert all(a[2]!=b[2]for a,b in zip(g,g[1:]))
I={(t,a)for t,b in NF['bulk_mod26']for a in range(b,78,26)};T={j for j,g in G.items()if len(g)%2};S=I^T
required_input={j for j,g in G.items()if g[0][2]=='L'};assert required_input==I&G.keys()and len(required_input)==1439
A=S&G.keys();assert len(A)==1847 and len(S)==3300
At={t for t,a in A};St={t for t,a in S};assert At==set(range(-28,47))
components=[]
for t in sorted(St):
 if not components or t!=components[-1][1]+1:components.append([t,t])
 else:components[-1][1]=t
eligible=[c for c in components if c[1]-c[0]+1>=len(At)];assert eligible==[[-28,46]]
# A length75 consecutive interval can only fit the UNIQUE length75 component.
# Opposite orientation reflects[-28,46] to[-46,28]. No bounded translation scan.
shifts={0:[0],2:[18]};source_sigma=(13+7+0)%2;invp=(13,6);invh=2;inverse_sigma=(sum(invp)+invh)%2;assert source_sigma==0 and inverse_sigma==1
for rot,ds in shifts.items():assert all((inverse_sigma+d)%2!=source_sigma for d in ds)
# Countercontrol: exact inverse itself has the expected negative charge and
# physically reverses the supplied one-period path, at its genuine odd sector.
IW=W[::-1].translate(str.maketrans('RL','LR'));pp=(p[0]-D[h][0],p[1]-D[h][1]);hh=(h+2)%4;start=pp;start_h=hh
for c in IW:
 hh=(hh+(-1 if c=='L'else 1))%4;v=D[hh];pp=pp[0]+v[0],pp[1]+v[1]
assert (pp[0]-start[0],pp[1]-start[1])==(78,78)and hh==start_h and IW.count('R')-IW.count('L')==-408
out={'status':'AUTHOR analytic all-translation same-sector obstruction','scope':__doc__,'complete_output_classes':len(S),'inverse_required_black_classes':len(A),'required_black_normal_interval':[-28,46],'complete_output_black_normal_components':components,'only_long_component':eligible[0],'parallel_halfturn_normal_shifts':shifts,'source_sector':source_sigma,'exact_inverse_sector':inverse_sigma,'all_candidate_shifts_even':True,'inverse_charge':-408,'inverse_drift':[78,78],'perpendicular_reason':'Nonempty required-black rays leave the finite source normal hull, so no finite cap can supply them.','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(O/'exact_inverse15324_sector_obstruction.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

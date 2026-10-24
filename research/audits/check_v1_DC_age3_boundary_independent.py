from pathlib import Path
import json,hashlib
P=Path(__file__).resolve();prefix=P.with_name('check_U1_young3_shadow_independent.py').read_text().split('rows=[];cases=[]')[0];exec(compile(prefix,str(P.with_name('check_U1_young3_shadow_independent.py')),'exec'))
B=ROOT/'core_periodicity_new/v1_DC_age3_boundary_frozen_20261023_1244';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['file']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_v1_DC_age3_boundary_shadow.json').read_text());goal=1j;qh=1;q=1-1j;source=1;assert G[source][:2]==(1+2j,3)
assert q not in G[source][3]|G[source][4]|K and G[source][2].get(q,True)is True
for dst in(4,5):assert G[dst][2][rotation(q-goal,-qh)]is False and rotation(q-goal,-qh)==2+1j
cases=[];preds=[]
for p in ids:
 c=counts[p];h=(-G[p][1])%4;start=-rotation(G[p][0],h);outputs={start+rotation(o,h):o for o in G[p][4]};assert q in outputs
 preds.append({'predecessor':p,'pose':[*xy(start),h],'shadow_slot':xy(outputs[q])})
 for a in ids:
  for z in G[a][3]:
   for n in range(c+1,c+4):
    rem=c+3-n
    if n<oldages[a,z]or counts[a]>rem:continue
    ch=(c-n)%4;pos=q-rotation(z,ch);end=pos+rotation(G[base[a]][0],ch)
    if ch==3:
     assert n==c+1 and pos.real>1 and G[source][1]==3;why='zero-C west preclearer cone'
    elif ch==2:
     assert rem==1 and end.imag-1<goal.imag;why='one-C south/east postbase cone'
    elif ch==1:
     assert rem==0 and counts[a]==0 and(end.real>goal.real or end.imag<goal.imag);why='zero-C east postconsumer cone'
    else:raise AssertionError((p,a,z,n))
    cases.append({'predecessor':p,'consumer':a,'input':list(xy(z)),'age':n,'consumer_pose':[*xy(pos),ch],'remaining_C':rem,'base_endpoint':list(xy(end)),'reason':why})
assert len(cases)==153
key=lambda r:(r['predecessor'],r['consumer'],tuple(r['input']),r['age'])
ac={key(r):r for r in J['retirement_cases']};oc={key(r):r for r in cases};assert ac.keys()==oc.keys()
for k,r in oc.items():
 for field in('consumer_pose','remaining_C','base_endpoint'):assert r[field]==ac[k][field]
# Source-first funding and exact V1 goal score, from literal exits/potential.
assert G[source][3]=={1j}and 28+2*H(1j)==30
O=sorted(G[4][4],key=xy);end=goal+rotation(G[4][0],qh);eh=(qh+G[4][1])%4
score=max(2*H(end)+A[eh],*(2*H(goal+rotation(o,qh))+w[f'w_4_{i}_{qh}']for i,o in enumerate(O)));assert score==28<30
out={'status':'PASS independent full8 predecessor and153 all-word retirement cases','manifest_sha256':hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),'predecessors':preds,'retirement_cases':cases,'goal_score':score,'I28_source_initial_activation':30,'scope':'Precise oldDC(3,1) to V/VC lower(0,3), target(0,1,E), produced age3 forces DC factor-first. Thus this conditional V1 role is funded, and the DC V^r VCC V^(r+2) family has no complete-eight left extension. Other V1 origins/ages and U1 remain open.'}
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k!='retirement_cases'})

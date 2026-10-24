"""Necessary full-word matching of current high tokens to HB/age compatible roles.
Supports the direct age-height and lifted residue-age witness formats.
"""
from pathlib import Path
import sys,json,collections
src,out=map(Path,sys.argv[1:3]);J=json.loads(src.read_text());G=json.loads(Path('chronology_dcuv/literal_residual_geometry.json').read_text())['geometry'];P={tuple(map(int,s.split()[:7]))for s in Path('chronology_dcuv/protected_patch2.tsv').read_text().splitlines()if s and not s.startswith('#')};age={(a,x,y):r for a,x,y,r in json.loads(Path('chronology_dcuv/counted_input_age_rules_complete.json').read_text())};F=-10;phase=1
rows=J.get('rows',J.get('replayed_states'));assert rows
mod=None
if len(rows[0]['pose'])==3:
 model=json.loads(Path(J['source_file']).read_text());mod=model['modulus']
def rot(p,h):x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def coord(p):x,y=rot(p,phase);return x+y,x-y
outputs=[];inputs=[];C=0
for k,row in enumerate(rows):
 a=row['packet'];h,q=row['pose'][:2];tr=row['pose'][2]if mod else None
 if q is not None:
  for slot in G[a]['inputs']:
   dz,dt=coord(rot(slot,h));z=q+dz
   if z>F:inputs.append({'packet_index':k,'packet':a,'heading':h,'slot':slot,'height':z,'residue':(tr+dt)%mod if mod else None,'C':C,'age':age[a,*slot]})
  if k<len(rows)-1:
   for slot in G[a]['outputs']:
    dz,dt=coord(rot(slot,h));z=q+dz
    if z>F:outputs.append({'packet_index':k,'packet':a,'heading':h,'slot':slot,'height':z,'residue':(tr+dt)%mod if mod else None,'C':C})
 C+=G[a]['name'].count('C')
adj=[];beforeHB=[]
for v in inputs:
 L=[];pre=[]
 for i,u in enumerate(outputs):
  if u['packet_index']>=v['packet_index']or(u['height'],u['residue'])!=(v['height'],v['residue'])or v['C']-u['C']<v['age']:continue
  pre.append(i);dh=(v['heading']-u['heading'])%4;x,y=rot(v['slot'],dh);ox,oy=u['slot'];tup=u['packet'],v['packet'],ox-x,oy-y,dh,ox,oy
  if tup not in P:L.append(i)
 adj.append(L);beforeHB.append(pre)
matched=[-1]*len(outputs);matchedinput=[-1]*len(inputs)
def aug(k,seen):
 for i in adj[k]:
  if i in seen:continue
  seen.add(i)
  if matched[i]<0 or aug(matched[i],seen):matched[i]=k;matchedinput[k]=i;return True
 return False
failed=[]
for k in range(len(inputs)):
 if not aug(k,set()):failed.append(k)
halls=[]
for root in failed:
 left={root};right=set();todo=[root]
 for k in todo:
  for i in adj[k]:
   if i in right:continue
   right.add(i);u=matched[i]
   assert u>=0
   if u not in left:left.add(u);todo.append(u)
 assert len(left)>len(right)
 halls.append({'inputs':len(left),'eligible_outputs':len(right),'height':inputs[root]['height'],'residue':inputs[root]['residue'],'input_obligations':[inputs[k]for k in sorted(left)],'eligible_producers':[outputs[k]for k in sorted(right)]})
R={'status':'COMPLETE_HB_ROLE_MATCH'if not failed else'HB_ROLE_HALL_DEFICIT','packets_including_goal':len(rows),'strict_packets':len(rows)-1,'modulus':mod,'high_inputs':len(inputs),'high_outputs':len(outputs),'matched':len(inputs)-len(failed),'first_failed_input':inputs[failed[0]]if failed else None,'zero_candidate_inputs':[{'input':inputs[k],'age_eligible_outputs_before_HB':len(beforeHB[k])}for k,L in enumerate(adj)if not L],'smallest_Hall_obstruction':min(halls,key=lambda x:x['inputs'])if halls else None,'scope':'Necessary current-token matching using height, optional transverse residue, exact birth C timestamps, signed input ages and signed HB producer-output eligibility. A perfect matching is not physical realizability.'};out.write_text(json.dumps(R,indent=2)+'\n');print({k:v for k,v in R.items()if k not in ['smallest_Hall_obstruction','zero_candidate_inputs']})

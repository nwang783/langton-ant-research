"""Fixed abstract word necessary matching, not a physical record certificate."""
from pathlib import Path
import json,hashlib,collections
R=Path(__file__).resolve().parent;wp=R/'chronology_dcuv/delayed_height_probe/v1_k7_deep_age_interval8.best.replay.json';gp=R/'chronology_dcuv/literal_residual_geometry.json';cp=R/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';hp=R/'../word_stabilization/dcv_producer_closed_family.tsv';bp=R/'chronology_dcuv/protected_patch2.tsv'
W=json.loads(wp.read_text());G=json.loads(gp.read_text())['geometry'];ids=(0,1,4,5,6,7,8,9);ni={a:i for i,a in enumerate(ids)};Cdeny={tuple(map(int,s.split()[:8]))for s in cp.read_text().splitlines()};Hdeny={tuple(map(int,s.split()[:7]))for s in hp.read_text().splitlines()if s and not s.startswith('#')};Bdeny={tuple(map(int,s.split()[:7]))for s in bp.read_text().splitlines()if s and not s.startswith('#')};F=-10
rot=lambda p,h:((p[0],p[1]),(p[1],-p[0]),(-p[0],-p[1]),(-p[1],p[0]))[h%4]
ht=lambda p:p[1]-p[0]
inputs=[];outputs=[];clock=0;rows=W['rows'];ucprefix=[0]
for r in rows:ucprefix.append(ucprefix[-1]+int(r['packet']in(7,8,9)))
for k,r in enumerate(rows):
 a=r['packet'];h,q=r['pose'];assert q is not None
 for si,s in enumerate(G[a]['inputs']):
  z=q+ht(rot(s,h))
  if z>F:inputs.append({'step':k,'packet':a,'heading':h,'slot_index':si,'slot':s,'height':z,'birth_clock_at_consumption':clock})
 if k<len(rows)-1:
  for si,s in enumerate(G[a]['outputs']):
   z=q+ht(rot(s,h))
   if z>F:outputs.append({'step':k,'packet':a,'heading':h,'slot_index':si,'slot':s,'height':z,'birth_clock':clock})
 clock+=G[a]['name'].count('C')
A=[];rejectstats=collections.Counter();candidate_detail=[]
for v in inputs:
 row=[]
 for j,u in enumerate(outputs):
  if u['step']>=v['step']or u['height']!=v['height']:continue
  age=v['birth_clock_at_consumption']-u['birth_clock'];dh=(v['heading']-u['heading'])%4;x,y=rot(v['slot'],dh);ox,oy=u['slot'];dx,dy=ox-x,oy-y;key=(u['packet'],v['packet'],dx,dy,dh,ox,oy)
  if key in Bdeny:rejectstats['HB']+=1;continue
  if(ni[u['packet']],ni[v['packet']],dx,dy,dh,ox,oy,min(age,5))in Cdeny:rejectstats['count5']+=1;continue
  dcv=ucprefix[v['step']]-ucprefix[u['step']]==0 and u['packet']not in(7,8,9)and v['packet']not in(7,8,9)
  if dcv and key in Hdeny:rejectstats['scoped_DCV198']+=1;continue
  row.append(j)
 A.append(row)
matched=[-1]*len(outputs);mi=[-1]*len(inputs)
def aug(k,seen):
 for j in A[k]:
  if j in seen:continue
  seen.add(j)
  if matched[j]<0 or aug(matched[j],seen):matched[j]=k;mi[k]=j;return True
 return False
failed=[]
for k in range(len(inputs)):
 if not aug(k,set()):failed.append(k)
halls=[]
for root in failed:
 L={root};RR=set();todo=[root]
 for k in todo:
  for j in A[k]:
   if j in RR:continue
   RR.add(j);m=matched[j]
   if m>=0 and m not in L:L.add(m);todo.append(m)
 halls.append({'input_indices':sorted(L),'output_indices':sorted(RR),'deficit':len(L)-len(RR)})
goal=[]
for k,v in enumerate(inputs):
 if v['step']==len(rows)-1:
  goal.append({'input':v,'eligible_sources':[{**outputs[j],'C_age':v['birth_clock_at_consumption']-outputs[j]['birth_clock']}for j in A[k]]})
J={'status':'NECESSARY_MATCH_EXISTS'if not failed else'FIXED_WORD_NECESSARY_MATCH_IMPOSSIBLE','scope':'Only this saved age/height abstract word, all high identity matchings, signed HB/count5 plus strictly U-free DCV198. No transverse position, joint V input history or global record closure follows.','word_including_goal':W['word_including_goal'],'high_inputs':len(inputs),'high_outputs':len(outputs),'matched':len(inputs)-len(failed),'rejections':dict(rejectstats),'goal_candidates':goal,'inputs':inputs,'outputs':outputs,'adjacency':A,'matching':mi,'Hall_deficits':halls,'dependencies':{str(p.relative_to(R)if p.is_relative_to(R)else p):hashlib.sha256(p.read_bytes()).hexdigest()for p in(wp,gp,cp,hp,bp)}}
(R/'chronology_dcuv/v1_fixedword_new_origins.json').write_text(json.dumps(J,indent=2)+'\n');print({'status':J['status'],'high_inputs':len(inputs),'matched':J['matched'],'reject':J['rejections'],'smallest_Hall':min(halls,key=lambda z:len(z['input_indices']))if halls else None,'goal_candidate_counts':[len(z['eligible_sources'])for z in goal]})
for g in goal:print('goal',g['input'],'sourceCages',[(u['step'],u['packet'],u['slot'],u['C_age'])for u in g['eligible_sources']])

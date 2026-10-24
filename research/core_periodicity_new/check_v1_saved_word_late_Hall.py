"""Four-versus-three typed-origin control on one obsolete abstract V1 word.
No global record claim; H198 is applied only within the U-free suffix.
"""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent;wp=R/'chronology_dcuv/delayed_height_probe/v1_k7_deep_age_interval8.best.replay.json';gp=R/'chronology_dcuv/literal_residual_geometry.json';hp=R/'../word_stabilization/dcv_producer_closed_family.tsv';bp=R/'chronology_dcuv/protected_patch2.tsv';W=json.loads(wp.read_text());G=json.loads(gp.read_text())['geometry'];H={tuple(map(int,s.split()))for s in hp.read_text().splitlines()};B={tuple(map(int,s.split()[:7]))for s in bp.read_text().splitlines()};rows=W['rows'];rot=lambda q,h:((q[0],q[1]),(q[1],-q[0]),(-q[0],-q[1]),(-q[1],q[0]))[h%4];ht=lambda q:q[1]-q[0];O=[];I=[];clock=0
for j,r in enumerate(rows):
 a=r['packet'];h,q=r['pose']
 if j+1<len(rows):assert rows[j+1]['pose']==[(h+G[a]['endpoint'][2])%4,q+ht(rot(G[a]['endpoint'][:2],h))]
 if j<len(rows)-1:
  for k,z in enumerate(G[a]['outputs']):
   level=q+ht(rot(z,h))
   if level==1:O.append({'step':j,'packet':a,'heading':h,'slot_index':k,'slot':z,'height':1,'birth_C':clock})
 if j in(142,143,147,148):
  for k,z in enumerate(G[a]['inputs']):
   level=q+ht(rot(z,h))
   if level==1:I.append({'step':j,'packet':a,'heading':h,'slot_index':k,'slot':z,'height':1,'C':clock,'minimum_produced_age':2 if a==4 and z==[0,3] else 3})
 clock+=G[a]['name'].count('C')
assert len(I)==4;adj=[];rejections=[]
for v in I:
 adjv=[];reject=[]
 for j,u in enumerate(O):
  if u['step']>=v['step']:continue
  age=v['C']-u['birth_C'];dh=(v['heading']-u['heading'])%4;x,y=rot(v['slot'],dh);ox,oy=u['slot'];key=(u['packet'],v['packet'],ox-x,oy-y,dh,ox,oy)
  if age<v['minimum_produced_age']:why='signed_marginal_age'
  elif key in B:why='signed_full8_HB'
  else:
   assert all(r['packet']not in(7,8,9)for r in rows[u['step']:v['step']+1])
   why='signed_scoped_DCV198'if key in H else None
  if why:reject.append({'output_index':j,'reason':why,'clause':key,'C_age':age})
  else:adjv.append(j)
 adj.append(adjv);rejections.append(reject)
union=sorted(set(sum(adj,[])));assert len(union)==3;assert[(O[j]['step'],O[j]['slot'])for j in union]==[(95,[1,0]),(136,[0,0]),(141,[2,0])]
# The sole U-family action is initial and all its inputs are untracked old cells.
r=rows[0];firstI=[r['pose'][1]+ht(rot(z,r['pose'][0]))for z in G[r['packet']]['inputs']];assert max(firstI)<=-10;assert all(r['packet']not in(7,8,9)for r in rows[1:])
J={'status':'AUTHOR_FIXED_WORD_HALL_DEFICIT_PASS','scope':'Only saved V1 age/height word, high initial residuals absent. Four current identity obligations cannot be matched to three eligible births. This does NOT exclude V1 or demonstrate usefulness of new LN at a V consumer.','word_including_goal':W['word_including_goal'],'source_first_pose':rows[0]['pose'],'all_head_height_updates_exact':True,'high_initial_white_boundary':-10,'height':'phase1 y-x in target normalized frame','four_inputs':I,'all_prior_height1_outputs':O,'eligible_output_indices':adj,'rejected_output_origins':rejections,'Hall_union_output_indices':union,'Hall_union_outputs':[O[j]for j in union],'deficit':1,'initial_UCC_input_heights':firstI,'LN_at_only_U_action':'May assign all5 input identities entry-old births, hence joint law is vacuous in this saved control.','dependencies':{str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in(wp,gp,hp,bp)}}
(R/'chronology_dcuv/v1_saved_word_late_Hall.json').write_text(json.dumps(J,indent=2)+'\n');print({'inputs':[(v['step'],v['packet'],v['slot'])for v in I],'eligible_sources':[(O[j]['step'],O[j]['packet'],O[j]['slot'])for j in union],'rows':adj,'deficit':1,'new_U_law_applicable':False})

"""Four-C halfplane persistence and noninitial marked-pose nonreturn.
Uses signed1309 maturation only; no new count threshold/query.
"""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent;GP=R/'chronology_dcuv/literal_residual_geometry.json';G=json.loads(GP.read_text())['geometry'];rot=lambda q,h:((q[0],q[1]),(q[1],-q[0]),(-q[0],-q[1]),(-q[1],q[0]))[h]
rows=[]
for h in(0,1):
 for b in(0,4,7):
  step=rot(G[b]['endpoint'][:2],h)
  for inp in G[b]['inputs']:
   ri=rot(inp,h);p=(1-ri[0],-1-ri[1]);end=(p[0]+step[0],p[1]+step[1]);assert end[0]>=1
   rows.append(dict(first_retirement_postexit_C=4 if h==0 else 3,heading=h,consumer=b,input=inp,base_start=p,base_end=end,remaining_C=0 if h==0 else 1,final_marked_min_x=end[0]+(0 if h==0 else 1)))
assert all(rot(G[b]['endpoint'][:2],h)[0]>=0 for b in(0,4,7)for h in(0,1))
C=G[1]['word'][len(G[0]['word']):];D=((0,1),(1,0),(0,-1),(-1,0));p=(0,0);h=1
for ch in C:h=(h+(-1 if ch=='L'else 1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
assert(p,h)==((1,0),0)
J=dict(status='AUTHOR_FOUR_C_SHADOW_HALFPLANE_AND_NONRETURN_PASS',scope='Noninitial complete8 markedA, current predecessorbud. At4Cs later markedBheading same asA andX<=0, oldbudstillcurrent. Exact samehead/heading return at4C impossible becauseB requires freshnewbudatsamecell. No countquery>existing1309; no allCnonreturn/capture.',all16_endpoints=rows,remaining_E_to_N_C_displacement=[1,0,0],same_pose_collision=dict(old_identity='Fresh from packet immediately beforeA, survives untilbeforeB',new_identity='Fresh from different packet immediately beforeB',cell=[1,-1],contradiction='Oldidentity would needretirement beforeB to permitnewOinstallation, but persistence excludesit'),dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,Path(__file__).resolve()]})
(R/'chronology_dcuv/four_C_bud_nonreturn.json').write_text(json.dumps(J,indent=2)+'\n');print(dict(endpoints=len(rows),delta3_min_final_x=min(r['final_marked_min_x']for r in rows if r['first_retirement_postexit_C']==3),delta4_min_final_x=min(r['final_marked_min_x']for r in rows if r['first_retirement_postexit_C']==4)))

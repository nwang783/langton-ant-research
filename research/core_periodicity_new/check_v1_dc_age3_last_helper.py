"""Exact endpoint masks for an all-word conditional V1 support lemma."""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent;gp=R/'chronology_dcuv/literal_residual_geometry.json';G=json.loads(gp.read_text())['geometry'];K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)}
def rot(q,h):x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return(p[0]+q[0],p[1]+q[1])
def height(q):return q[0]+q[1]
def ht(q,h):return height(rot(q,h))
base=(0,4,7);endpoints={a:G[a]['endpoint']for a in base};assert endpoints=={0:[1,1,0],4:[1,3,0],7:[0,4,0]}
Cword=G[1]['word'][len(G[0]['word']):];assert len(Cword)==15
for a,b,c in[(1,0,1),(5,4,1),(6,4,2),(8,7,1),(9,7,2)]:assert G[a]['word']==G[b]['word']+Cword*c
p=(0,0);h=0;D=((0,1),(1,0),(0,-1),(-1,0))
for ch in Cword:h=(h+(-1 if ch=='L'else 1))%4;p=add(p,D[h])
assert p==(0,1)and h==3
# With core center c=(-1/2,-1/2), the standalone C center step is(1,1).
c=(-.5,-.5);cc=rot(c,3);center_step=(p[0]+cc[0]-c[0],p[1]+cc[1]-c[1]);assert center_step==(1.,1.)
heights={h:{G[a]['name']:ht(G[a]['endpoint'][:2],h)for a in base}for h in(3,2,1)}
assert heights=={3:{'D':0,'V':-2,'U':-4},2:{'D':-2,'V':-4,'U':-4},1:{'D':0,'V':2,'U':4}}
C_heights=[ht((1,1),h)for h in(3,2)];assert C_heights==[0,-2]
# Helper heights relative to a goal head of H=0; translation adds H.
maskrows=[]
for a,offset,critical,age in[(4,-2,(0,3),2),(7,-4,(-1,4),5)]:
 inputs=[offset+ht(q,1)for q in G[a]['inputs']];outputs=[offset+ht(q,1)for q in G[a]['outputs']];assert offset+ht(critical,1)==1 and max(outputs)==-1
 maskrows.append({'helper_packet':a,'heading':1,'head_height_minus_H':offset,'input_heights_minus_H':inputs,'output_heights_minus_H':outputs,'critical_input':critical,'critical_input_height_minus_H':1,'critical_input_min_age_if_produced':age,'candidate_created_peak':26 if a==4 else 30,'candidate_record_score_minus_2H':2*offset+(26 if a==4 else 30)})
assert[ht(q,1)for q in G[4]['inputs']]==[3,1]
Dpost=[ht(q,1)for q in G[0]['outputs']];assert Dpost==[-2]
# Sharp physical V-helper control, unconditioned direct board run plus ordered ledger.
seed=K|{(-2,2),(-1,1),(-1,3),(0,1)};word=[1,6,4,4];B=set(seed);p=(0,0);h=0;t=0;T={q:('entry',None)for q in seed-K};clock=0;contacts=[];steps=[]
for j,a in enumerate(word):
 I=[add(p,rot(q,h))for q in G[a]['inputs']]
 if j==2:
  assert p==(-3,2)and h==1 and clock==3
  assert all(q in T for q in[(2,0),(0,2),(3,1)])
  ages={str(q):(None if T[q][1]is None else clock-T[q][1])for q in[(2,0),(0,2),(3,1)]};assert ages=={'(2, 0)':3,'(0, 2)':2,'(3, 1)':3}
  contacts.append({'prehelper_time':t,'helper_pose':[*p,h],'goal_head_height':1,'goal_selected_identity_cell':[2,0],'helper_critical_identity_cell':[0,2],'goal_other_identity_cell':[3,1],'C_ages':ages})
 ins=[T.pop(q)for q in I]
 for si,q in enumerate(G[a]['outputs']):
  w=add(p,rot(q,h));assert w not in T;T[w]=(j,clock)
 for ch in G[a]['word']:
  assert(ch=='L')==(p in B)
  if p in B:B.remove(p)
  else:B.add(p)
  h=(h+(-1 if ch=='L'else 1))%4;p=add(p,D[h]);t+=1
 clock+=G[a]['name'].count('C');steps.append([j,a,t,*p,h,clock])
for ch in G[4]['marker']:
 assert(ch=='L')==(p in B)
 if p in B:B.remove(p)
 else:B.add(p)
 h=(h+(-1 if ch=='L'else 1))%4;p=add(p,D[h]);t+=1
assert t==120
J={'status':'AUTHOR_ALL_WORD_LAST_HELPER_PROOF_MASKS_PASS','scope':'Conditional DC output(3,1)→V input(0,3), relativeconsumer(0,1,h1), exact source-included age3, all strict intermediates recurrent-eight. No whole V1 exclusion or general producer claim.','height':'X+Y in sourceDC normalized N frame; goal is headingE/globalphase1. H is consumer head height. This equals record model phase1 height after target normalization.','base_endpoint_heights_by_heading':heights,'Cword':Cword,'C_center_step':[1,1],'strict_C_center_height_steps':C_heights,'zero_base_height_balance':'h+2i=b+2c+d+2e+2f','variables':'pre-W counts a,b,c; middle-S d,e,f; post-E g,h,i for D,V,U, including bases attached to C tails.','why_positive_RHS':'One C2 packet is VCC/UCC and has pre-W V/U base; two C1 packets need a middle-S D/V/U base. Thus RHS>=1 and post-E V/U exists.','last_helper_masks':maskrows,'later_D_output_heights_minus_H':Dpost,'prehelper_obligations':{'H+1':'two distinct current residual identities; V-helper ages>=2,>=3, U-helper ages>=5,>=3; entry identities formal age infinity','H+3':'one current protected DC output identity, C-age exactly3','last_helper_record_score':'S-4, with S=2H+26, V1/U1 peaks26/30'},'sharp_V_helper_literal_control':{'seed':sorted(seed),'word':word,'reads_including_final_marker':t,'helper_cut':contacts,'steps':steps},'input_sha256':hashlib.sha256(gp.read_bytes()).hexdigest()}
(R/'chronology_dcuv/v1_dc_age3_last_helper.json').write_text(json.dumps(J,indent=2)+'\n');print({'height_balance':J['zero_base_height_balance'],'helper_masks':maskrows,'positive_cut':contacts})

"""Complete one-C classification for the VCC young-lower-pair gate.
All five nonnegative cone solutions, not a finite-depth search.
"""
from pathlib import Path
from itertools import product
import json,hashlib
R=Path(__file__).resolve().parent;gp=R/'chronology_dcuv/literal_residual_geometry.json';G=json.loads(gp.read_text())['geometry'];D=((0,1),(1,0),(0,-1),(-1,0));K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)}
def rot(q,h):x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return(p[0]+q[0],p[1]+q[1])
def trace(seq):
 p=(0,0);h=0;t=0;col={};first={};last={};seed=set();poses=[];bad=None;events=[]
 for j,a in enumerate(seq):
  poses.append([*p,h]);ww=G[a]['word']+(G[a]['marker']if j==len(seq)-1 else'')
  for c in ww:
   b=c=='L'
   if p in col and col[p]!=b:bad={'time':t,'cell':p,'turn':c,'previous':last[p]};break
   if p not in col:first[p]=[t,c]
   if p not in col and b:seed.add(p)
   col[p]=not b;last[p]=[t,c];events.append([t,*p,h,c]);h=(h+(-1 if b else 1))%4;p=add(p,D[h]);t+=1
  if bad:break
 return {'feasible':bad is None,'conflict':bad,'poses':poses,'initial_black_cells':sorted(seed),'events':events,'raw_length':sum(len(G[a]['word'])for a in seq),'full_program_length':sum(len(G[a]['word'])for a in seq)+len(G[seq[-1]]['marker'])}
# Pre-E counts a,b,c (D,V,U), post-N counts d,e,f. Exact equations:
# a+3b+4c+d+e=4, -a-b+d+3e+4f=0.
# Hence d+2e+2f+b+2c=2. All b,c,d,e,f<=2 and a<=4.
solutions=[];words=[]
for b,c,d,e,f in product(range(3),repeat=5):
 if d+2*e+2*f+b+2*c!=2:continue
 a=d+3*e+4*f-b
 if a<0 or a+3*b+4*c+d+e!=4:continue
 assert a+b+c>=1 and a<=4
 # Each solution has just one nonzero pre-type and one post-type.
 pre=[0]*a+[4]*b+[7]*c;post=[0]*d+[4]*e+[7]*f;assert len(set(pre))==1 and len(set(post))<=1
 strict=pre[:-1]+[{0:1,4:5,7:8}[pre[-1]]]+post
 solutions.append({'pre_DVU':[a,b,c],'post_DVU':[d,e,f],'strict_word':strict});words.append(strict)
assert sorted(words)==sorted([[8],[0,1,0,0],[0,0,1,4],[0,0,0,1,7],[5,0]])
records=[]
for strict in words:
 r=trace([6]+strict+[7]);r.pop('events');r['strict_word']=strict;records.append(r)
assert [r['strict_word']for r in records if r['feasible']]==[[5,0]]
controls=[];expected_seed=sorted(K|{(0,3),(1,2),(-1,2),(4,0),(2,-1),(3,-1)})
for tail in(7,8,9):
 s=[6,5,0,tail];r=trace(s);assert r['feasible']and r['initial_black_cells']==expected_seed and r['poses']==[[0,0,0],[0,4,2],[-1,0,1],[0,-1,1]]
 r.pop('events');r['word']=s;controls.append(r)
# All five target identities survive every strict complete context. Upper three
# already existed before source, because target age3 is less than their age>=5.
targetI={add((0,-1),rot(q,1))for q in G[7]['inputs']};assert targetI=={(1,0),(2,0),(4,0),(2,-1),(3,-1)}
for a,p,h in[(5,(0,4),2),(0,(-1,0),1)]:
 ctx={add(p,rot(q[:2],h))for q in G[a]['requirements']};assert not ctx&targetI
oldhelper=(-1,2);assert oldhelper not in {tuple(q)for q in G[6]['outputs']};assert oldhelper not in {tuple(q[:2])for q in G[6]['requirements']}
VCI={add((0,4),rot(q,2))for q in G[5]['inputs']};assert VCI=={(0,1),oldhelper}
basehead=add((0,4),rot(G[4]['endpoint'][:2],2));basecore={add(basehead,rot(q,2))for q in K};assert basehead==(-1,1)and VCI<=basecore
# Explicit unconditioned board check at the indicated base endpoint.
B=set(expected_seed);p=(0,0);h=0
for t,c in enumerate(''.join(G[a]['word']for a in[6,5,0,7])+G[7]['marker']):
 assert(c=='L')==(p in B)
 if p in B:B.remove(p)
 else:B.add(p)
 h=(h+(-1 if c=='L'else 1))%4;p=add(p,D[h])
 if t+1==66:assert p==basehead and h==2 and basecore<=B
J={'status':'AUTHOR_COMPLETE_ONE_C_YOUNG_VCC_PREFIX_PASS','scope':'Conditional sourceVCC supplies both U lower inputs at exact source-included age3, consumer relative pose(0,-1,h1). All complete recurrent-eight intermediates, arbitrary initial board, no depth cap. Known positive preserved.','source_packet':6,'consumer_packets':[7,8,9],'relative_consumer_pose':[0,-1,1],'protected_target_inputs':sorted(targetI),'normalization_for_cone_equations':{'source_pose':[-1,0,3],'postsource_pose':[-5,0,1],'consumer_pose':[0,0,0],'core_center_correction':[-0.5,-0.5],'remaining_center_displacement':[5,-1],'single_C_center_displacement':[1,-1],'zero_run_displacement':[4,0]},'exact_equations':['a+3b+4c+d+e=4','-a-b+d+3e+4f=0','d+2e+2f+b+2c=2'],'all_five_nonnegative_solutions':solutions,'all_five_literal_records':records,'unique_surviving_strict_word':[5,0],'all_three_actual_controls':controls,'mandatory_older_helper':{'cell':oldhelper,'not_in_source_context_or_outputs':True,'strict_VC_inputs':sorted(VCI),'actual_black_core_time':66,'actual_black_core_pose':[-1,1,2],'root_component_warning':'Predates source, not necessarily initial or a new incidence component under inherited history.'},'input_sha256':hashlib.sha256(gp.read_bytes()).hexdigest()}
(R/'chronology_dcuv/young_U_vcc_forced_prefix.json').write_text(json.dumps(J,indent=2)+'\n');print({'five_strict_words':words,'only_survivor':[5,0],'helper':oldhelper,'helper_core_time':66,'control_seed_mass':len(expected_seed),'all_tail_lengths':[r['full_program_length']for r in controls]})

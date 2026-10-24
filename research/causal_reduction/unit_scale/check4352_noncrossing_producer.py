"""Literal entire-field five-flight/four-router4352 producer.
The supplied289-cell launch and all earlier writes are retained. No all-N
inference follows from this finite control; a separate affine proof is needed.
"""
from pathlib import Path
import json,hashlib,sys
from check_prepared1564_router_geometry import H,trace,infer
P=Path(__file__).resolve().parent;G=P.parents[1]/'nonlinear_global_budget_2026-10-23'
J=json.loads((P/'prepared4352_noncrossing_router_plan.json').read_text())
L=json.loads((P/'prepared4352_fresh_launch.json').read_text());W=json.loads((G/'second_prepared_wave_certificate.json').read_text())['word']
V=((0,1),(1,0),(0,-1),(-1,0))
def pose(u,t):
 assert(u+t)%2==0
 return((u+t)//2,(u-t)//2)
def setup(R,N):
 assert R%4==0 and R>=48
 us=[-2*R+1,4*R+3,-4*R+3,2*R+1];start=pose(R+1,25);p=start;h=3
 B=set(infer(H*30,p,h)['input']);assert len(B)==13
 stages=[];caps=[]
 for router,u in zip(J['routers'],us):
  t,a,head=router['source_lane'];q=pose(u,t);assert q[0]%2==a and h==head
  d=2 if h==1 else-2;dx=q[0]-p[0];assert q[1]-p[1]==dx and dx%d==0 and dx//d>=0
  stages.append({'kind':'H','count':dx//d,'start':[p,h]});p=q
  cap={(p[0]+x,p[1]+y)for x,y in router['extra_black_relative_input']};assert not B&cap;B|=cap;caps.append(sorted(cap))
  stages.append({'kind':'router','index':router['index'],'word':router['word'],'start':[p,h]});qq,h=router['endpoint'];p=p[0]+qq[0],p[1]+qq[1]
 q=(-20,-15);dx=q[0]-p[0];assert q[1]-p[1]==dx and dx%(-2)==0
 stages.append({'kind':'H','count':dx//(-2),'start':[p,h]});p=q
 stages.append({'kind':'H-prefix','word':H[:28],'start':[p,h]});last=list(trace(H[:28],p,h))[-1];p,h=last[1],last[2]
 assert[p,h]==[tuple(L['forward_entry_pose'][0]),L['forward_entry_pose'][1]]
 cap={tuple(q)for q in L['fresh_cap']};assert not B&cap;B|=cap
 stages.append({'kind':'launch','word':L['forward_prelude_word'],'start':[p,h]})
 stages.append({'kind':'wave','count':N,'start':[(-2,3),3]})
 return start,B,stages,caps

def run(R,N):
 start,B,stages,caps=setup(R,N);initial=set(B);p=start;h=3;t=0;last={};first={};reports=[];bad=None
 for stage in stages:
  w=H*stage['count']if stage['kind']=='H'else W*stage['count']if stage['kind']=='wave'else stage['word']
  assert[p,h]==stage['start'];st=t
  for c in w:
   actual='L'if p in B else'R'
   if actual!=c:
    bad={'time':t,'pose':[p,h],'wanted':c,'actual':actual,'kind':stage['kind'],'index':stage.get('index'),'offset':t-st,'prior':last.get(p)};break
   first.setdefault(p,c);last[p]=[t,h,c];B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;v=V[h];p=p[0]+v[0],p[1]+v[1];t+=1
  reports.append({'kind':stage['kind'],'index':stage.get('index'),'count':stage.get('count'),'start_time':st,'end_time':t,'end_pose':[p,h],'mass':len(B)})
  if bad:break
 out={'scope':__doc__,'R':R,'N':N,'initial_pose':[start,3],'initial_seed':sorted(initial),'initial_mass':len(initial),'status':'literal PASS'if bad is None else'literal FAIL','conflict':bad,'segments':reports,'read_count':t,'final_pose':[p,h],'final_black_mass':len(B),'minimal_first_L_input':len([c for c in first.values()if c=='L']),'unused_initial_black':sorted(initial-first.keys()),'final_field_sha256':hashlib.sha256(json.dumps(sorted(B),separators=(',',':')).encode()).hexdigest()}
 return out
if __name__=='__main__':
 N=int(sys.argv[1])if len(sys.argv)>1 else 1;R=200+52*N;out=run(R,N)
 (P/f'prepared4352_noncrossing_R{R}_N{N}.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items()if k not in('initial_seed','unused_initial_black')},indent=2),flush=True)

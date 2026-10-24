"""Literal whole-board check of the concrete seven-flight/six-cap producer.
All preloaded cells and every earlier write are retained. Finite controls only;
no all-parameter conclusion is inferred by this script.
"""
from pathlib import Path
import json,sys,time,hashlib
from check_prepared1564_router_geometry import H,trace,infer
P=Path(__file__).resolve().parent
J=json.loads((P/'prepared1564_noncrossing_router_plan.json').read_text());L=json.loads((P/'prepared1564_fresh_launch_cap.json').read_text())
G=P.parents[1]/'nonlinear_global_budget_2026-10-23';W=json.loads((G/'prepared_travelling_wave_certificate.json').read_text())['word']
V=((0,1),(1,0),(0,-1),(-1,0))
def pose(u,t):assert(u+t)%2==0;return((u+t)//2,(u-t)//2)
def setup(R,N):
 assert R%4==0 and R>=12
 us=[-2*R+3,2*R+1,-4*R+3,4*R+3,-2*R+1,2*R+3]
 start=pose(R+3,-37);p=start;h=3;segments=[];B=set(infer(H*30,start,h)['input']);assert len(B)==13
 caps=[]
 for r,u in zip(J['routers'],us):
  t,a,hh=r['source_lane'];q=pose(u,t);assert q[0]%2==a and hh==h
  dx,dy=q[0]-p[0],q[1]-p[1];d=2 if h==1 else -2
  assert dx==dy and dx%d==0 and dx//d>=0
  m=dx//d;segments.append({'kind':'H','count':m,'start':[p,h]});p=q
  cc={(p[0]+x,p[1]+y)for x,y in r['extra_black_relative_input']};assert not B&cc;B|=cc;caps.append(sorted(cc))
  segments.append({'kind':'router','index':r['index'],'word':r['word'],'start':[p,h]})
  (x,y),h=r['endpoint'];p=p[0]+x,p[1]+y
 q=(7,6);dx=q[0]-p[0];assert q[1]-p[1]==dx and dx%(-2)==0 and dx//(-2)>=0
 segments.append({'kind':'H','count':dx//(-2),'start':[p,h]});p=q
 segments.append({'kind':'H-prefix','word':H[:55],'start':[p,h]});_,p,h=list(trace(H[:55],p,h))[-1][0:3]
 assert(p,h)==((4,0),2)
 cc={tuple(z)for z in L['fresh_cap']};assert not B&cc;B|=cc
 segments.append({'kind':'launch','word':L['forward_prelude'],'start':[p,h]})
 segments.append({'kind':'wave','count':N,'start':[(-6,-6),0]})
 return start,B,segments,caps

def run(R,N):
 start,B,segments,caps=setup(R,N);initial=set(B);p=start;h=3;t=0;last={};reports=[];bad=None
 for s in segments:
  if s['kind']=='H':word=H*s['count']
  elif s['kind']=='wave':word=W*s['count']
  else:word=s['word']
  assert[p,h]==s['start'],(s['kind'],p,h,s['start'])
  st=t
  for c in word:
   actual='L'if p in B else'R'
   if actual!=c:
    bad={'time':t,'pose':[p,h],'wanted':c,'actual':actual,'segment_kind':s['kind'],'router_index':s.get('index'),'offset':t-st,'prior':last.get(p)};break
   last[p]=[t,h,c];B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;v=V[h];p=p[0]+v[0],p[1]+v[1];t+=1
  reports.append({'kind':s['kind'],'index':s.get('index'),'count':s.get('count'),'start_time':st,'end_time':t,'end_pose':[p,h],'mass':len(B)})
  if bad:break
 out={'R':R,'wave_periods':N,'initial_mass':len(initial),'initial_seed':sorted(initial),'status':'literal PASS'if not bad else'literal FAIL','conflict':bad,'segments':reports,'read_count':t,'final_pose':[p,h],
 'final_black_mass':len(B),'final_black_sha256':hashlib.sha256(json.dumps(sorted(B),separators=(',',':')).encode()).hexdigest()}
 return out
if __name__=='__main__':
 R=int(sys.argv[1])if len(sys.argv)>1 else 100;N=int(sys.argv[2])if len(sys.argv)>2 else 3
 out=run(R,N);(P/f'prepared1564_noncrossing_R{R}_N{N}.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items()if k!='initial_seed'},indent=2),flush=True)

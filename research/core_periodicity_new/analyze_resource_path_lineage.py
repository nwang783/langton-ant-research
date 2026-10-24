"""Report exact retained-cell lineage for a reconstructed path; discovery only.
CLI MODEL.json WITNESS.txt OUTPUT.json. Understands ordinary and fused reset graphs.
"""
import json,sys
from pathlib import Path
from resource_profile import load_profile
J=json.loads(Path(sys.argv[1]).read_text());profile,data,_=load_profile(J['resource_profile_file']);G=data['geometry']['geometry'];F=data['ordinary'];FP=data['protected'];H={tuple(r)for r in J.get('candidate_hypotheses',[])};P=set(map(tuple,J['points']));labels={tuple(c):(J['source'],sl,(0,0),0,-1)for sl,c in enumerate(G[J['source']]['outputs'])if tuple(c)in P};path=[];events=[]
def rot(p,h):x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
for line in Path(sys.argv[2]).read_text().splitlines():
 if line.startswith('WITNESS '):
  sid,col,a=map(int,line.split()[1:]);path.append({'pose':J['poses'][sid]if sid<J['out']else None,'color':col,'packet_id':a})
for i,s in enumerate(path):
 if s['pose']is None:continue
 x,y,h=s['pose'];a=s['packet_id'];world=lambda z:(x+rot(z,h)[0],y+rot(z,h)[1])
 for z in G[a]['inputs']:
  q=world(z)
  if q in labels:
   aa,sl,pp,hh,born=labels[q];r=(aa,a,*rot((x-pp[0],y-pp[1]),-hh),(h-hh)%4,*G[aa]['outputs'][sl]);events.append({'cell':q,'birth_step':born,'step':i,'row':r,'signed':r[:5]in F or r in FP,'hypothesis':r in H,'outer_to_goal':born<0 and i==len(path)-1})
 for rr in G[a]['requirements']:labels.pop(world(rr[:2]),None)
 for sl,z in enumerate(G[a]['outputs']):
  q=world(z)
  if q in P:labels[q]=(a,sl,(x,y),h,i)
Path(sys.argv[3]).write_text(json.dumps({'path':path,'events':events},indent=2));print(json.dumps(events,indent=2))

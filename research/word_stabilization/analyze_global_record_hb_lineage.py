from pathlib import Path
import json,sys
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R/'core_periodicity_new'));from resource_profile import load_profile
source,witness,out=map(Path,sys.argv[1:4]);J=json.loads(source.read_text());P,D,M=load_profile(J['resource_profile_file']);G=D['geometry']['geometry'];F=D['ordinary'];FP=D['protected'];patch=set(map(tuple,J['points']));labels={};events=[];rows=[]
def rot(q,h):x,y=q;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def world(p,q):z=rot(q,p[2]);return p[0]+z[0],p[1]+z[1]
for l in witness.read_text().splitlines():
 if l.startswith('WITNESS'):
  _,s,m,a=l.split();s,m,a=map(int,(s,m,a));rows.append((s,m,a))
for step,(sid,mask,a)in enumerate(rows):
 if sid>=len(J['poses']):continue
 p=J['poses'][sid];g=G[a];ctx={tuple(x[:2])for x in g['requirements']}
 for z in g['inputs']:
  q=world(p,z)
  if q in labels:
   b,k,pp,born=labels[q];rel=rot((p[0]-pp[0],p[1]-pp[1]),-pp[2]);row=(b,a,*rel,(p[2]-pp[2])%4,*G[b]['outputs'][k]);events.append({'cell':q,'source_step':born,'target_step':step,'tuple':row,'ordinary_forbidden':row[:5]in F,'protected_forbidden':row in FP})
 for q in list(labels):
  if rot((q[0]-p[0],q[1]-p[1]),-p[2])in ctx:del labels[q]
 for k,z in enumerate(g['outputs']):
  q=world(p,z)
  if q in patch:labels[q]=(a,k,p,step)
O={'model':str(source.resolve()),'witness':str(witness.resolve()),'events':events,'forbidden_cells':sorted({tuple(e['cell'])for e in events if e['ordinary_forbidden']or e['protected_forbidden']})};out.write_text(json.dumps(O,indent=2)+'\n');print(json.dumps(O,indent=2))

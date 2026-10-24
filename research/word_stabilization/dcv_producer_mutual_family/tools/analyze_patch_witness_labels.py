from pathlib import Path
import json,sys
P=Path('/workspace/shared/langton/core_periodicity_new');W=Path('/workspace/shared/langton/word_stabilization');model=json.loads(Path(sys.argv[1]).read_text());path=json.loads(Path(sys.argv[2]).read_text());G=json.loads((W/'dcv_residual_core_resources.json').read_text())['geometry'];H69=json.loads((W/'dcv_conditional_confinement_optimized.json').read_text())['unproved_bad_transfers'];bad={ (r['source_packet'],r['target_packet'],*r['target_pose'],*r['source_output']):i+1 for i,r in enumerate(H69)};H221={tuple(map(int,l.split()[:7]))for l in(W/'dcv_companion_candidate221.tsv').read_text().splitlines()};patch={tuple(p)for p in model['points']}
def rot(p,h):
 x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def world(p,h,z):r=rot(z,h);return p[0]+r[0],p[1]+r[1]
M=json.loads((W/'seven_sub_dcv_port_quotient.json').read_text())['macro_words'];D=((0,1),(1,0),(0,-1),(-1,0))
def footprint(w):
 p=(0,0);h=0;seen=set()
 for c in w:
  seen.add(p);h=(h+(1 if c=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 return seen
C=[footprint(m['word']+m['end_marker'])for m in M]
labels={tuple(q):(model['source'],k,(0,0),0,-1)for k,q in enumerate(G[model['source']]['outputs'])if tuple(q)in patch};events=[]
for step,row in enumerate(path):
 if row['pose']is None:continue
 x,y,h=row['pose'];p=(x,y);a=row['packet_id']if'packet_id'in row else['D','DC','DCC','DCCC','V','VC','VCC'].index(row['action'])
 for j,z in enumerate(G[a]['inputs']):
  q=world(p,h,z)
  if q in labels:
   b,k,pp,hh,born=labels[q];rel=rot((x-pp[0],y-pp[1]),-hh);entry=(b,a,*rel,(h-hh)%4,*G[b]['outputs'][k]);e={'cell':q,'source_step':born,'target_step':step,'tuple':entry,'bad69_index':bad.get(entry),'candidate221':entry in H221,'outer_to_goal':born==-1 and step==len(path)-1};events.append(e)
   print(e)
  labels.pop(q,None)
 for q in list(labels):
  if rot((q[0]-x,q[1]-y),-h)in C[a]:labels.pop(q)
 for k,z in enumerate(G[a]['outputs']):
  q=world(p,h,z)
  if q in patch:labels[q]=(a,k,p,h,step)
Path(sys.argv[2]).with_suffix('.labels.json').write_text(json.dumps(events,indent=2))

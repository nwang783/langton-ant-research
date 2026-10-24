"""Literal finite positive controls for protected DCUV packet transfers."""
from pathlib import Path
import json,sys,hashlib,time
ROOT=Path(__file__).resolve().parents[1];P=ROOT/'core_periodicity_new/chronology_dcuv';profile=json.loads((P/'profile.json').read_text());G=json.loads(Path(profile['files']['geometry']['path']).read_text())['geometry'];F={tuple(map(int,l.split()[:5]))for l in Path(profile['files']['ordinary']['path']).read_text().splitlines()};FP={tuple(map(int,l.split()[:7]))for l in Path(profile['files']['protected']['path']).read_text().splitlines()};limit=int(sys.argv[1])if len(sys.argv)>1 else 5
D=((0,1),(1,0),(0,-1),(-1,0));M='LLLLRLRRRRL';seen={};nodes=0;counts=[0]*(limit+1);start=time.time();K={tuple(z)for z in json.loads(Path(profile['files']['geometry']['path']).read_text())['core']};minimum_roots={}
def rot(p,h):
 x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def world(p,h,z):x,y=rot(z,h);return p[0]+x,p[1]+y
def literal(w):
 p=(0,0);h=0;last={};first={}
 for c in w:
  if last.get(p)==c:return None
  first.setdefault(p,c);last[p]=c;h=(h+(1 if c=='R'else-1))%4;d=D[h];p=(p[0]+d[0],p[1]+d[1])
 return sorted([list(p)for p,c in first.items()if c=='L'])
C=[{(x,y)for x,y,*_ in g['requirements']}for g in G]
def events(path,seed):
 p=(0,0);h=0;labels={};poses=[];out=[];tokens={tuple(q):None for q in seed if tuple(q)not in K};rootcounts=[]
 for t,a in enumerate(path):
  poses.append((p,h));g=G[a];roots=0
  for z in g['inputs']:
   q=world(p,h,z);assert q in tokens,(path,t,q);roots+=tokens.pop(q)is None
  for z in g['outputs']:
   q=world(p,h,z);assert q not in tokens,(path,t,q);tokens[q]=t
  rootcounts.append(roots)
  if a>=7 and t+1<len(path) and (a not in minimum_roots or roots<minimum_roots[a]['initial_tokens']):minimum_roots[a]={'name':g['name'],'initial_tokens':roots,'packet_ids':path.copy(),'packet_index':t,'rootcounts_so_far':rootcounts.copy(),'initial_black_seed':seed}
  for j,z in enumerate(g['inputs']):
   q=world(p,h,z)
   if q in labels and t+1<len(path):
    s,b,k=labels[q];pp,hh=poses[s];xy=rot((p[0]-pp[0],p[1]-pp[1]),-hh);row=(b,a,*xy,(h-hh)%4,*G[b]['outputs'][k]);assert row[:5]not in F and row not in FP,row
    if row not in seen:out.append((row,s,t,j))
  # Complete-context retirement, followed by ordered fresh output installation.
  for q in list(labels):
   if rot((q[0]-p[0],q[1]-p[1]),-h)in C[a]:del labels[q]
  for k,z in enumerate(g['outputs']):labels[world(p,h,z)]=(t,a,k)
  p=world(p,h,g['endpoint'][:2]);h=(h+g['endpoint'][2])%4
 return out,poses

def dfs(path,raw):
 global nodes
 nodes+=1;seed=literal(raw+M)
 if seed is None:return
 counts[len(path)]+=1
 es,poses=events(path,seed)
 for row,s,t,j in es:
  if row not in seen:seen[row]={'tuple':row,'packet_ids':path.copy(),'packet_names':[G[a]['name']for a in path],'source_index':s,'target_index':t,'target_input_slot':j,'source_pose':[*poses[s][0],poses[s][1]],'target_pose':[*poses[t][0],poses[t][1]],'initial_black_seed':seed,'raw_word':raw,'terminal_marker':M}
 if len(path)<limit:
  for a,g in enumerate(G):dfs(path+[a],raw+g['word'])
dfs([],'')
out={'status':'Literal positive controls only; bounded enumeration is not an absence theorem','packet_depth':limit,'candidate_nodes':nodes,'feasible_by_packet_length':counts,'transfer_count':len(seen),'minimum_U_initial_tokens':minimum_roots,'seconds':time.time()-start,'profile_sha256':hashlib.sha256((P/'profile.json').read_bytes()).hexdigest(),'witnesses':[seen[k]for k in sorted(seen)]};(P/f'observed_transfers_depth{limit}.json').write_text(json.dumps(out,indent=2)+'\n');(P/f'observed_transfers_depth{limit}.tsv').write_text(''.join(' '.join(map(str,k))+'\n'for k in sorted(seen)));print(json.dumps({k:v for k,v in out.items()if k!='witnesses'},indent=2))

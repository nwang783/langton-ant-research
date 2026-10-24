"""Unfold exact-low summary edges to genuine finite packet-DFA paths, then replay
all high identities with exact birth-C timestamps and synchronized head height.
CLI ASSEMBLED.json WITNESS.txt UNIT_GRAPH.json OUTPUT.json.
"""
from pathlib import Path
from collections import deque
import json,sys
src,txt,unit,out=map(Path,sys.argv[1:5]);M=json.loads(src.read_text());S=json.loads(Path(M['source_file']).read_text());D=json.loads(Path(S['dfa_file']).read_text());U=json.loads(unit.read_text());G=json.loads(Path('chronology_dcuv/literal_residual_geometry.json').read_text())['geometry'];rules={(a,x,y):r for a,x,y,r in json.loads(Path('chronology_dcuv/counted_input_age_rules_complete.json').read_text())};F=S['initial_bound'];phase=S['phase'];L=M['cutoff'];nd=len(D['transitions']);E=U['edges'];adj=[[]for _ in U['nodes']]
for i,e in enumerate(E):adj[e[0]].append(i)
first={p['unit_edges'][0]:p['packet']for p in U['packet_expansions']};cache={}
def search(starts,target,dep,need):
 B=16
 while True:
  labels=[];seen={};todo=deque()
  for u,z in starts(B):
   k=u,z,0
   if k not in seen:seen[k]=len(labels);labels.append((u,z,0,-1,-1));todo.append(len(labels)-1)
  found=None
  while todo:
   ii=todo.popleft();u,z,c,_,_=labels[ii]
   if u==target and z==dep and(need is None or c==need):found=ii;break
   for ei in adj[u]:
    _,v,dd,cc=E[ei];zz=z+dd
    if not 0<=zz<=B:continue
    cap=min(4,c+cc);k=v,zz,cap
    if k in seen:continue
    seen[k]=len(labels);labels.append((v,zz,cap,ii,ei));todo.append(len(labels)-1)
  if found is not None:
   seq=[];ix=found
   while labels[ix][3]>=0:seq.append(labels[ix][4]);ix=labels[ix][3]
   seq.reverse();word=[first[e]for e in seq if e in first];return word,labels[ix][:3],{'stack_cap_used_to_find_finite_witness':B,'visited':len(labels),'unit_steps':len(seq)}
  B*=2

def rot(p,h):x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def ht(p):return sum(rot(p,phase))
lines=txt.read_text().splitlines();p=int(next(s for s in lines if s.startswith('start ')).split()[1]);assert p in M['initial_controls'];h,q,d,*_=M['positions'][p];word=[];rows=[];unfolds=[]
def append(a):
 global h,q,d
 rows.append({'packet':a,'pose':[h,q],'dfa_before':d});word.append(a);v=G[a];q+=ht(rot(v['endpoint'][:2],h));h=(h+v['endpoint'][2])%4;d=D['transitions'][d][D['keep'].index(a)];assert d>=0
if M['positions'][p][3]=='low':
 target=h*nd+d;dep=L-q
 starts=lambda B:[(hh*nd+D['initial_class'],z)for hh in range(4)for z in range(B+1)if(L-z-hh)%2==0]
 pref,st,control=search(starts,target,dep,None);h=st[0]//nd;d=D['initial_class'];q=L-st[1]
 for a in pref:append(a)
 assert[h,q,d]==M['positions'][p][:3];unfolds.append({'kind':'initial_low_prefix','packets':pref,**control})
initialpose=rows[0]['pose']if rows else[h,q]
for s in lines:
 if not s.startswith('EDGE '):continue
 v=list(map(int,s.split()[1:]));ei,fr,to,a=v[:4];assert p==fr and M['transitions'][ei][:3]==[fr,to,a];assert[h,q,d]==M['positions'][fr][:3];op=M['operations'][M['transitions'][ei][3]]
 if a>=0:append(a)
 else:
  assert not any(op[1]+op[2]);hh,qq,dd=M['positions'][to][:3];key=h,d,L-q,hh,dd,L-qq,op[0]
  if key not in cache:
   st=h*nd+d;dep=L-q;goal=hh*nd+dd;starts=lambda B:[(st,dep)];cache[key]=search(starts,goal,L-qq,op[0])
  seq,_,control=cache[key];beforeq=q
  for b in seq:assert q<=L;append(b);assert q<=L
  unfolds.append({'kind':'summary','edge':ei,'packets':seq,**control})
 assert[h,q,d]==M['positions'][to][:3];p=to
assert any(pp==p for pp,_ in M['goal_requirements']);assert h==q==0;append(S['target'])
# Completely separate timestamp/multiset replay of all actual packet slots.
C=0;tokens={};peak=0
for k,row in enumerate(rows):
 a=row['packet'];hh,qq=row['pose'];c=G[a]['name'].count('C');cons=[]
 for z,r in sorted([(qq+ht(rot(v,hh)),rules[a,*v])for v in G[a]['inputs']if qq+ht(rot(v,hh))>F],key=lambda x:-x[1]):
  vv=tokens.setdefault(z,[]);eligible=[i for i,b in enumerate(vv)if C-b>=r];assert eligible,(k,a,z,r,[C-b for b in vv]);i=max(eligible,key=lambda i:vv[i]);b=vv.pop(i);cons.append({'height':z,'minimum_age':r,'actual_age':C-b})
 row.update(C_before=C,consumed=cons)
 for v in G[a]['outputs']:
  z=qq+ht(rot(v,hh))
  if z>F:tokens.setdefault(z,[]).append(C)
 C+=c;peak=max(peak,max(map(len,tokens.values()),default=0))
R={'status':'PASS_EXACT_LOW_UNFOLDED_RESOURCE_PATH','packets_including_goal':len(word),'strict_packets':len(word)-1,'total_C_before_goal':rows[-1]['C_before'],'peak_count_per_height':peak,'initial_pose':initialpose,'actual_height_range':[min(r['pose'][1]for r in rows),max(r['pose'][1]for r in rows)],'word_including_goal':word,'rows':rows,'low_unfoldings':unfolds,'scope':'Every summary is replaced by a genuine finite packet-DFA low walk. Head-height chronology and all current high token ages/counts are exact. No transverse position matching or literal ant sufficiency is asserted.'};out.write_text(json.dumps(R,indent=2)+'\n');print({k:v for k,v in R.items()if k not in ['word_including_goal','rows','low_unfoldings']})

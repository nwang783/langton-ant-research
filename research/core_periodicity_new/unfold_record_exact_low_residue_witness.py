"""Constructively unfold low-summary profiles and check the complete current
high(height,transverse residue,C-age) ledger with exact global C timestamps.
CLI ASSEMBLED.json WITNESS.txt BASE_UNIT_GRAPH.json OUTPUT.json.
"""
from pathlib import Path
from collections import deque
import json,sys
src,txt,unit,out=map(Path,sys.argv[1:5]);M=json.loads(src.read_text());S=json.loads(Path(M['source_file']).read_text());D=json.loads(Path(S['dfa_file']).read_text());U=json.loads(unit.read_text());G=json.loads(Path('chronology_dcuv/literal_residual_geometry.json').read_text())['geometry'];rules={(a,x,y):r for a,x,y,r in json.loads(Path('chronology_dcuv/counted_input_age_rules_complete.json').read_text())};F=S['initial_bound'];phase=S['phase'];L=M['cutoff'];nd=len(D['transitions']);mod=M['modulus'];E=U['edges'];adj=[[]for _ in U['nodes']]
def rot(p,h):x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def coord(p):x,y=rot(p,phase);return x+y,x-y
first={p['unit_edges'][0]:(p['packet'],p['source'][0])for p in U['packet_expansions']};dt={ei:coord(rot(G[a]['endpoint'][:2],h))[1]%mod for ei,(a,h)in first.items()}
for i,e in enumerate(E):adj[e[0]].append(i)
cache={}
def search(starts,target,dep,trtarget,need):
 B=16
 while True:
  labels=[];seen={};todo=deque()
  for u,z,tr in starts(B):
   key=u,z,0,tr
   if key not in seen:seen[key]=len(labels);labels.append((u,z,0,tr,-1,-1));todo.append(len(labels)-1)
  found=None
  while todo:
   ii=todo.popleft();u,z,c,tr,_,_=labels[ii]
   if u==target and z==dep and tr==trtarget and(need is None or c==need):found=ii;break
   for ei in adj[u]:
    _,v,dd,cc=E[ei];zz=z+dd
    if not 0<=zz<=B:continue
    cap=min(4,c+cc);tr2=(tr+dt.get(ei,0))%mod;key=v,zz,cap,tr2
    if key in seen:continue
    seen[key]=len(labels);labels.append((v,zz,cap,tr2,ii,ei));todo.append(len(labels)-1)
  if found is not None:
   seq=[];ix=found
   while labels[ix][4]>=0:seq.append(labels[ix][5]);ix=labels[ix][4]
   seq.reverse();word=[first[e][0]for e in seq if e in first];return word,labels[ix][:4],{'stack_cap_used_to_find_finite_witness':B,'visited':len(labels),'unit_steps':len(seq)}
  B*=2
lines=txt.read_text().splitlines();trace=[list(map(int,x.split()[1:]))for x in lines if x.startswith('EDGE ')];p=int(next(s for s in lines if s.startswith('start ')).split()[1]);assert p in M['initial_controls'];nactual=len(M['actual_transitions']);needrows={(v[0]-nactual)//2 for v in trace if v[0]>=nactual};profiles={}
with Path(M['ports_file']).open()as f:
 fmt,np,ne,ni,mm=next(f).split();np,ne=map(int,[np,ne]);next(f)
 for _ in range(np):next(f)
 for k in range(ne):
  line=next(f)
  if k in needrows:profiles[k]=tuple(map(int,line.split()))
lowix={(v[5],v[3]):i for i,v in enumerate(M['positions'])if v[4]=='low'}
rows=[];word=[];unfolds=[];checkpoints=[];h,q,d,tr=M['positions'][p][:4]
def append(a):
 global h,q,d,tr
 rows.append({'packet':a,'pose':[h,q,tr],'dfa_before':d});word.append(a);v=G[a];dq,dt=coord(rot(v['endpoint'][:2],h));q+=dq;tr=(tr+dt)%mod;h=(h+v['endpoint'][2])%4;d=D['transitions'][d][D['keep'].index(a)];assert d>=0
if M['positions'][p][4]=='low':
 target=h*nd+d;dep=L-q;targettr=tr;starts=lambda B:[(hh*nd+D['initial_class'],z,t)for hh in range(4)for z in range(B+1)if(L-z-hh)%2==0 for t in range(hh%2,mod,2)]
 pref,st,control=search(starts,target,dep,targettr,None);h=st[0]//nd;d=D['initial_class'];q=L-st[1];tr=st[3]
 for a in pref:append(a)
 assert[h,q,d,tr]==M['positions'][p][:4];unfolds.append({'kind':'initial_low_prefix','packets':pref,**control})
initialpose=rows[0]['pose']if rows else[h,q,tr]
for vals in trace:
 ei,fr,to,a=vals[:4];checkpoints.append((len(rows),vals[4:]));assert p==fr and[h,q,d,tr]==M['positions'][fr][:4]
 if ei<nactual:edge=M['actual_transitions'][ei]
 else:
  k,variant=divmod(ei-nactual,2);pp,qq,dtp,c=profiles[k];hh=M['low_port_rows'][pp][0];t=hh%2+2*variant;edge=[lowix[pp,t],lowix[qq,(t+dtp)%mod],-1,M['zero_operator_ids'][c]]
 assert edge[:3]==[fr,to,a];op=M['operations'][edge[3]]
 if a>=0:append(a)
 else:
  assert not any(op[1]+op[2]);hh,qq,dd,tt=M['positions'][to][:4];key=h,d,L-q,tr,hh,dd,L-qq,tt,op[0]
  if key not in cache:
   st=h*nd+d;dep=L-q;goal=hh*nd+dd;tstart=tr;starts=lambda B:[(st,dep,tstart)];cache[key]=search(starts,goal,L-qq,tt,op[0])
  seq,_,control=cache[key]
  for b in seq:assert q<=L;append(b);assert q<=L
  unfolds.append({'kind':'summary','edge':ei,'packets':seq,**control})
 assert[h,q,d,tr]==M['positions'][to][:4];p=to
assert any(pp==p for pp,_ in M['goal_requirements']);assert h==q==tr==0;append(S['target'])
C=0;tokens={};peak=0;cp={k:v for k,v in checkpoints}
for k,row in enumerate(rows):
 if k in cp:
  actual=[sum(C-b>=j for b in tokens.get(tuple(place),[]))for place in M['places']for j in range(5)];assert actual==cp[k],('printed resource mismatch',k)
 a=row['packet'];hh,qq,tt=row['pose'];c=G[a]['name'].count('C');cons=[];req=[]
 for v in G[a]['inputs']:
  dq,dt=coord(rot(v,hh));z=qq+dq
  if z>F:req.append(((z,(tt+dt)%mod),rules[a,*v]))
 for place,r in sorted(req,key=lambda x:-x[1]):
  vv=tokens.setdefault(place,[]);eligible=[i for i,b in enumerate(vv)if C-b>=r];assert eligible,(k,a,place,r,[C-b for b in vv]);i=max(eligible,key=lambda i:vv[i]);b=vv.pop(i);cons.append({'place':place,'minimum_age':r,'actual_age':C-b})
 row.update(C_before=C,consumed=cons)
 for v in G[a]['outputs']:
  dq,dt=coord(rot(v,hh));z=qq+dq
  if z>F:tokens.setdefault((z,(tt+dt)%mod),[]).append(C)
 C+=c;peak=max(peak,max(map(len,tokens.values()),default=0))
R={'status':'PASS_EXACT_LOW_RESIDUE_UNFOLDED_RESOURCE_PATH','source_file':str(src.resolve()),'packets_including_goal':len(word),'strict_packets':len(word)-1,'total_C_before_goal':rows[-1]['C_before'],'peak_count_per_place':peak,'initial_pose':initialpose,'actual_height_range':[min(r['pose'][1]for r in rows),max(r['pose'][1]for r in rows)],'word_including_goal':word,'rows':rows,'low_unfoldings':unfolds,'scope':'Every summary profile is replaced by a genuine finite packet-DFA low walk with its exact net transverse residue. Head-height chronology, head residue and all current high token ages/counts are exact. No full transverse-coordinate matching or literal ant sufficiency is asserted.'};out.write_text(json.dumps(R,indent=2)+'\n');print({k:v for k,v in R.items()if k not in ['word_including_goal','rows','low_unfoldings']})

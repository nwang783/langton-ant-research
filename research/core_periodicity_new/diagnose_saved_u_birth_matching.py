"""Finite matching diagnostic for ONE saved nonphysical resource word.
Exhausts the final-input birth-order cases, not physical ant trajectories.
"""
from pathlib import Path
from collections import deque
import json,hashlib,sys
USE_COUNT='hb_age5'not in sys.argv[1:]
PRESERVE_BINS='freebins'not in sys.argv[1:]
W=Path(__file__).resolve().parent;SRC=W/'chronology_dcuv/delayed_height_probe/u1_k5_exact_low_residue_age.unfolded.json';J=json.loads(SRC.read_text());M=json.loads(Path(J['source_file']).read_text());G=json.loads((W/'chronology_dcuv/literal_residual_geometry.json').read_text())['geometry'];mod=M['modulus'];cap=M['age_cap'];places=set(map(tuple,M['places']));F=M['cutoff'];IDS=(0,1,4,5,6,7,8,9);mp={a:i for i,a in enumerate(IDS)}
HB={tuple(map(int,l.split()[:7]))for l in(W/'chronology_dcuv/protected_patch2.tsv').read_text().splitlines()};CP=W/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';COUNT={tuple(map(int,l.split()[:8]))for l in CP.read_text().splitlines()}
def rot(p,h):x,y=p;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def plc(slot,row):
 h,q,tr=row['pose'];x,y=rot(rot(slot,h),1);return(q+x+y,(tr+x-y)%mod)
outs=[];ins=[];goals={};prefix_pool={p:[]for p in places};pool_at_goal=None
for k,row in enumerate(J['rows']):
 p=row['packet'];C=row['C_before'];given={tuple(x['place']):x['actual_age']for x in row['consumed']}
 if k==len(J['rows'])-1:pool_at_goal={str(s):sorted(C-b for b in prefix_pool[plc(s,row)])for s in map(tuple,G[p]['inputs'])}
 for s in G[p]['inputs']:
  pp=plc(s,row)
  if pp not in places:continue
  oldage=given[pp];idx=len(ins);ins.append(dict(step=k,packet=p,heading=row['pose'][0],slot=s,place=pp,C=C,required_bin=min(cap,oldage),old_age=oldage))
  if k==len(J['rows'])-1:goals[tuple(s)]=idx
  prefix_pool[pp].remove(C-oldage)
 if k<len(J['rows'])-1:
  for s in G[p]['outputs']:
   pp=plc(s,row)
   if pp in places:
    outs.append(dict(step=k,packet=p,heading=row['pose'][0],slot=s,place=pp,C=C));prefix_pool[pp].append(C)
def minage(v):
 p=v['packet'];s=tuple(v['slot'])
 if p in(0,1):return 3
 if p in(4,5):return 2 if s==(0,3)else 3
 if p==6:return 5
 return 5 if s in((-1,4),(0,2),(0,3))else 3
ADJ=[]
for v in ins:
 L=[]
 for i,u in enumerate(outs):
  age=v['C']-u['C']
  if u['step']>=v['step']or u['place']!=v['place']or age<minage(v)or PRESERVE_BINS and min(cap,age)!=v['required_bin']:continue
  dh=(v['heading']-u['heading'])%4;x,y=rot(v['slot'],dh);ox,oy=u['slot'];tup=(u['packet'],v['packet'],ox-x,oy-y,dh,ox,oy);ct=(mp[u['packet']],mp[v['packet']],ox-x,oy-y,dh,ox,oy,min(age,5))
  if tup in HB or USE_COUNT and ct in COUNT:continue
  L.append(i)
 ADJ.append(L)
def matching(adj):
 match=[-1]*len(outs);back=[-1]*len(ins)
 def aug(k,seen):
  for i in adj[k]:
   if i in seen:continue
   seen.add(i)
   if match[i]<0 or aug(match[i],seen):match[i]=k;back[k]=i;return True
  return False
 for k in range(len(ins)):
  if not aug(k,set()):
   left={k};right=set();Q=[k]
   for u in Q:
    for i in adj[u]:
     if i in right:continue
     right.add(i);z=match[i]
     assert z>=0
     if z not in left:left.add(z);Q.append(z)
   assert len(left)>len(right)
   return None,dict(inputs=sorted(left),outputs=sorted(right))
 return back,None
base,hall=matching(ADJ);qidx=goals[-1,2];aidx=goals[-1,1];cidx=goals[0,2];didx=goals[0,3];cases=[];hit=None
if base:
 for qi in ADJ[qidx]:
  for mode in('a','cd'):
   A=[L.copy()for L in ADJ];A[qidx]=[qi];chosen=[aidx]if mode=='a'else[cidx,didx];qb=outs[qi]['step']
   for j in chosen:A[j]=[i for i in A[j]if outs[i]['step']>=qb]
   sol,HH=matching(A);cases.append(dict(q_output=qi,q_birth_packet=qb,mode=mode,matched=sol is not None,hall=HH))
   if sol is not None:hit=sol;break
  if hit:break
ages=None;births=None
if hit:
 ages={str(s):ins[j]['C']-outs[hit[j]]['C']for s,j in goals.items()};births={str(s):outs[hit[j]]['step']for s,j in goals.items()}
O=dict(status='NECESSARY_MATCHING_WITH_FINAL_BIRTH_ORDER_EXISTS'if hit else'NO_MATCH_IN_STATED_EXACT_FINITE_DIAGNOSTIC',source_file=str(SRC),exact_count5_clauses_applied=USE_COUNT,input_tokens=len(ins),output_tokens=len(outs),age_bin_cap=cap,age_bin_path_preserved=PRESERVE_BINS,base_signed_HB_count5_match_exists=base is not None,base_hall=hall,saved_prefix_final_pools=pool_at_goal,old_final_ages={str(s):ins[j]['old_age']for s,j in goals.items()},cases=cases,alternative_final_ages=ages,alternative_final_birth_packets=births,goal_candidates={str(s):[dict(output_index=i,**outs[i],age=ins[j]['C']-outs[i]['C'])for i in ADJ[j]]for s,j in goals.items()},matching=hit,inputs=ins,outputs=outs,scope='Only height/residue origin matching of one already nonphysical saved word, under zero initial high tokens. Age bins are preserved only when age_bin_path_preserved is true; signed HB plus JO/KV minima are always used, exact count5 clauses only if flagged. No physical realization or generic search claim.',dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[SRC,Path(__file__).resolve()]})
T=W/'chronology_dcuv/delayed_height_probe'/('u1_k5_joint_birth_matching_'+('full_signed'if USE_COUNT else'hb_age5')+(''if PRESERVE_BINS else'_freebins')+'.json');T.write_text(json.dumps(O,indent=2)+'\n');print({k:v for k,v in O.items()if k not in('matching','inputs','outputs','cases','dependencies')});print('cases',len(cases),'q candidates',len(ADJ[qidx]));print(T)

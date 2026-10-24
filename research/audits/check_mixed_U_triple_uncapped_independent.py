from pathlib import Path
from collections import defaultdict
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();F=D/'mixed_U_to_triple_source_forces_six_reads_and_height_raise.md';assert sha(F)=='669221aa17ef792084214ae1b71576ff8f7d43358c3de9f7df5a7244b87e1d9f';C=D/'mixed_U_triple_helper_uncapped_count_control.json';assert sha(C)=='0cf1dc01a698f256a33b08d66e2f88c574f1ef9bc6d9bbbff3e6e5c0af10384c';J=json.loads(C.read_text())
H='NESW';V={'N':1j,'E':1,'S':-1j,'W':-1};out=lambda w:[H[(H.index(c)+(1 if r%2==0 else-1))%4]for r,c in enumerate(w)];rank=lambda w,d,output=False:[r for r,c in enumerate(out(w)if output else w)if c==d]
profiles={'u':'WEEW','s':'NSN','w':'WEEE'};pos={'u':1j,'s':2j,'w':1+2j};edges=[]
for a,b,d in [('u','s','N'),('s','w','E')]:
 src=rank(profiles[a],d,True);dst=rank(profiles[b],d);assert len(src)==len(dst)
 edges += [(a,r,b,s)for r,s in zip(src,dst)]
assert all(e in edges for e in [('u',0,'s',0),('s',0,'w',1),('u',1,'s',2),('s',2,'w',3)])
assert rank(profiles['u'],'W')==[0,3]and rank(profiles['w'],'S',True)==[2]
rows=[]
# Proven complete count algebra: j even =>floor(n/2)=1; j odd=>floor(n/2)=3.
for n in (2,3,6,7):
 for j in range(n):
  if n//2!=(1 if j%2==0 else 3):continue
  w='N'*j+'S'+'N'*(n-j-1);dep=rank(w,'W',True);assert len(dep)==2
  rn=sum(c=='N'for c in w[::2]);rows.append(dict(history=w,S_rank=j,W_departure_ranks=dep,strict_bracket=dep[0]<j<dep[1],R_N_count=rn,height_raise=rn))
canon=lambda z:json.dumps(z,sort_keys=True);assert set(map(canon,rows))==set(map(canon,J['all_derived_count_profiles']))
surv=[z['history']for z in rows if z['strict_bracket']];assert surv==J['strict_survivors']==['NNNSNN','NNNSNNN']
heights={}
for helper in surv:
 raw={pos[k]:v for k,v in profiles.items()};raw[1+1j]=helper;eq={};adj=defaultdict(list)
 for p,w in raw.items():
  ia='NS'if(int(p.real)+int(p.imag))%2==0 else'EW';oa='EW'if ia=='NS'else'NS'
  for d in oa:
   key=p,d;f=out(w).count(d)
   if key in eq:assert eq[key]==f
   eq[key]=f
  for d in ia:
   key=p-V[d],d;f=w.count(d)
   if key in eq:assert eq[key]==f
   eq[key]=f
 for(p,d),f in eq.items():
  c,l={'E':(p-1j,p),'W':(p-1,p-1-1j),'N':(p,p-1),'S':(p-1-1j,p-1j)}[d];adj[l].append((c,f));adj[c].append((l,-f))
 vals={1j:0};todo=[1j]
 while todo:
  p=todo.pop()
  for q,f in adj[p]:
   if q in vals:assert vals[q]==vals[p]+f
   else:vals[q]=vals[p]+f;todo.append(q)
 assert vals[1+1j]==-1 and vals[0]==-2 and vals[1]==len(helper)-3
 heights[helper]={'C_NW':vals[1j],'L_NE':vals[1+1j],'L_SW':vals[0],'C_SE':vals[1]}
outobj=dict(status='PASS uncapped mixed U->3 helper count and higher-C obstruction',proof=sha(F),control=sha(C),actual_boundary_edges=edges,derived_complete_count_profiles=rows,strict_survivors=surv,stream_heights_relative_c=heights,analytic_review=[
'Complete uWEEW,sNSN,wWEEE histories fix every physical port copy. Exact uR0->sR0->wL1 and uL1->sR2->wL3 imply T2w>=T0u+6 and <=T1u-2. With T3u>=T1u+8, helper firstW=T0u-1 < uniqueS=T2w+1 < secondW=T3u-1. All earlier helper reads remain allowed.',
'Ant parity sector makes helper arrivals N/S only. Sin1 andWout2 give m+1=2 if soleS at even rank, or m-1=2 if odd. Thus n2/3 or6/7 is DERIVED, not imposed. Strict event bracket rejects all even-rankS and leaves only oddrank3, hence entire historiesNNNSNN/NNNSNNN withW ranks1/5.',
'Unrestricted directed-port stream equations independently reconstruct sharedNW C=c, NE L=c-1,SW L=c-2 andSE C=c+3/c+4, including the optional seventh R. No cap4 maximum rule is applied at helperD; its multiplicity starts unrestricted.',
'Therefore any complete exterior needs>=6 helper reads; cap4 is impossible. If the displayed boundary c is GLOBAL C maximum the higher face also contradicts it with unrestricted exterior cap. At a nonmaximal level these remain genuine necessary higher-C escape modes, not an all-front exclusion or iterative fuel claim.'
]);S.with_suffix('.json').write_text(json.dumps(outobj,indent=2)+'\n');print(outobj['status']);print(sha(S.with_suffix('.json')))

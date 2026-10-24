#!/usr/bin/env python3
"""Complete DERIVED local-history family, no imposed visit cap.
A survivor is only an OPEN chronology interface, never a physical front.
"""
import json,math,time
from itertools import combinations,product
from collections import Counter
from pathlib import Path
from check_extremal_read_coupling import D,quotient,cycles
PTS=[(r,t-r)for t in range(-1,3)for r in (0,1)];IX={p:i for i,p in enumerate(PTS)};DRIFT=(2,-2)
A_MODES=[(1,1,3,3),(1,1,3,3,3),(3,1,3,3,1)]
def q_words(I,J):
 out=[]
 for n in range(2,13,2):
  s=I+n//2-J
  if s%2:continue
  X=s//2;Y=I-X
  if not 0<=X<=n//2 or not 0<=Y<=n//2:continue
  for rr,ll in product(combinations(range(0,n,2),X),combinations(range(1,n,2),Y)):
   nn=set(rr)|set(ll);out.append(tuple(0 if k in nn else 2 for k in range(n)))
 return out

def assess(H):
 nodes=[(i,j)for i,hs in enumerate(H)for j in range(len(hs))];out={};incoming={};ports=[]
 for i,p in enumerate(PTS):
  for h in range(4):
   src=[j for j,hi in enumerate(H[i])if(hi+(1 if j%2==0 else-1))%4==h]
   if not src:continue
   q,k=quotient((p[0]+D[h][0],p[1]+D[h][1]),DRIFT)
   if q not in IX:
    ports +=[('out',i,j,h,q,k)for j in src];continue
   ii=IX[q];dst=[j for j,hi in enumerate(H[ii])if hi==h];assert len(src)==len(dst)
   for u,v in zip(src,dst):out[i,u]=((ii,v),k);incoming[ii,v]=((i,u),k)
 for i,j in nodes:
  if(i,j)not in incoming:
   h=H[i][j];q,k=quotient((PTS[i][0]-D[h][0],PTS[i][1]-D[h][1]),DRIFT);assert q not in IX
   ports.append(('in',i,j,h,q,k))
 chains=[];where={};seen=set()
 for start in nodes:
  if start in incoming:continue
  seq=[];at=start;k=0
  while True:
   assert at not in seen;seen.add(at);where[at]=(len(chains),len(seq),k);seq.append((at,k))
   if at not in out:break
   at,dk=out[at];k+=dk
  chains.append(seq)
 if len(seen)!=len(nodes):
  at=next(v for v in nodes if v not in seen);seq=[];ind={};k=0
  while at not in ind:
   ind[at]=len(seq);seq.append((at,k));at,dk=out[at];k+=dk
  cc=seq[ind[at]:]
  return'closed_event_component',{'cycle':cc,'winding':k-cc[0][1]}
 for seq in chains:
  prev={}
  for z,((i,j),k) in enumerate(seq):
   p=(PTS[i][0]+k*DRIFT[0],PTS[i][1]+k*DRIFT[1])
   if p in prev and j!=prev[p][0]+1:
    rank,begin=prev[p]
    return'skipped_physical_rank',{'segment':seq[begin:z+1],'same_physical_cell':p,'earlier_rank':rank,'later_rank':j}
   prev[p]=(j,z)
 F={};K={};E={}
 for i,hs in enumerate(H):
  if(i,0)in out:
   (ii,j),k=out[i,0];F[PTS[i]]=(PTS[ii],k)
   if j==len(H[ii])-1:E[PTS[i]]=(PTS[ii],k)
  if len(hs)%2==0:
   target=(i,len(hs)-1)
   if target in incoming:
    (ii,j),k=incoming[target];K[PTS[i]]=(PTS[ii],-k)
 if any(z['winding']!=-1 for z in cycles(F)):return'first_cycle_winding',None
 if any(z['winding']!=1 for z in cycles(K)):return'last_cycle_winding',None
 if len(cycles(E))>1:return'two_E_cycles',None
 # Chain-base difference inequalities. C+K*P, all inter-chain C positive.
 ee={};N=len(nodes);period=4*N+4
 def add(u,v,C,K):
  z=(C+K*period,C,K);ee[u,v]=max(ee.get((u,v),(-10**100,0,0)),z)
 for i,hs in enumerate(H):
  for j in range(len(hs)-1):
   u,a,ka=where[i,j];v,b,kb=where[i,j+1];C=4+a-b;Kc=kb-ka
   if u==v:
    if C+Kc*period>0:return'within_chain_rank_clock',None
   else:add(u,v,max(C,len(chains[u])),Kc)
 n=len(chains);dist=[0]*n;prev=[None]*n
 for z in range(n):
  changed=False
  for (u,v),(w,C,Kc)in ee.items():
   if dist[v]<dist[u]+w:dist[v]=dist[u]+w;prev[v]=(u,v,C,Kc);changed=True
  if not changed:break
 else:return'chain_clock_cycle',None
 # Potentials realize the relaxed chain system at this explicit period.
 # Site-time phase corrections follow automatically along physical edges;
 # round each chain root to the correct mod4, then propagate by multiples4.
 residue=[(2*PTS[seq[0][0][0]][0]-sum(PTS[seq[0][0][0]])%2)%4 for seq in chains]
 zd=residue[:]
 for _ in range(n):
  changed=False
  for (u,v),(w,C,Kc)in ee.items():
   want=zd[u]+w;new=want+(residue[v]-want)%4
   if zd[v]<new:zd[v]=new;changed=True
  if not changed:break
 else:return'phase_adjusted_clock_cycle',None
 clocks={f'{i}:{j}':zd[c]+a-k*period for(i,j),(c,a,k)in where.items()}
 assert all(clocks[f'{i}:{j+1}']>=clocks[f'{i}:{j}']+4 for i,hs in enumerate(H)for j in range(len(hs)-1))
 for (i,j),((ii,jj),k)in out.items():assert clocks[f'{i}:{j}']+1==clocks[f'{ii}:{jj}']+k*period
 return'open_survivor',{'points':PTS,'headings':H,'event_count':N,'period_for_relaxed_clocks':period,'representative_clocks':clocks,'chains':chains,'open_ports':ports,'first_cycles':cycles(F),'reverse_last_cycles':cycles(K),'E_cycles':cycles(E),'phase_collisions':N-len({v%period for v in clocks.values()}),'limitations':'Exact open matching/rank/chain clocks only. No single whole event cycle, phase-distinctness, global travel or shared-colour field is claimed.'}

def main():
 stats=Counter();survivors=[];by_modes={};rejections=[];start=time.time()
 for a,b in product(range(3),repeat=2):
  A=A_MODES[a];B=A_MODES[b];qq=q_words(len(A)-2,len(B)-2);rr=q_words(len(B)-2,len(A)-2);sub=Counter()
  for qi,ri in product(range(len(qq)),range(len(rr))):
   q,r=qq[qi],rr[ri]
   H=[(3,),(3,),(2,2,0),(2,2,0),A,B,q,r];kind,wit=assess(H);stats[kind]+=1;sub[kind]+=1
   if kind=='open_survivor':survivors.append(dict(wit,case=[a,b,qi,ri]))
   else:
    assert kind in ('closed_event_component','skipped_physical_rank') and wit
    rejections.append({'case':[a,b,qi,ri],'reason':kind,'witness':wit})
  by_modes[f'{a},{b}']={'candidate_count':len(qq)*len(rr),'outcomes':dict(sub)}
 result={'scope':__doc__,'candidate_count':sum(stats.values()),'outcomes':dict(stats),'by_modes':by_modes,'representative_survivors':survivors,'seconds':time.time()-start}
 Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items()if k!='representative_survivors'},indent=2))
 Path(__file__).with_name('g8_two_outer_rows_rejection_certificate.json').write_text(json.dumps({'case_order':'A0 mode, A1 mode, Q0 heading index, Q1 heading index; all options generated by q_words.','rejections':rejections},separators=(',',':'))+'\n')
if __name__=='__main__':main()

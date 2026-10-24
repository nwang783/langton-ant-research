#!/usr/bin/env python3
"""All-cap g8 local completion covers for three exact one-minimum interfaces.
No period/width cap. All higher ports are open. Every bound follows fixed ports.
"""
import json,hashlib,time
from collections import Counter
from itertools import product
from pathlib import Path
from check_extremal_read_coupling import D,quotient
import certify_diagonal_read_minimum as base
ROOT=Path(__file__).resolve().parent
TARGETS=[v for v in product(range(9),repeat=4)if sum(v)==8 and all(x%4==2 for x in(v[0]-v[1],v[3]-v[2],v[0]-v[2],v[3]-v[1]))]
IDS=[(1,(0,0)),(1,(1,0)),(3,(3,0))]

def inventory(H):
 v=[0]*4
 for i,h in enumerate(H):
  if len(h)%2:
   t=i//2-1;r=i%2;v[2*r+(t-r)%2]+=1
 return v

def allowed(H):
 v=inventory(H);return [a for a in TARGETS if all(x<=y for x,y in zip(v,a))]

def returns(H,G):
 result=[[],[]]
 for chain in G['chains']:
  (i,j),k=chain[0];assert k==0;p=G['points'][i];h=H[i][j];source=(p[0]-D[h][0],p[1]-D[h][1]);r,v=quotient(source,(2,-2))
  (ii,jj),kk=chain[-1];p=G['points'][ii];ho=(H[ii][jj]+(1 if jj%2==0 else-1))%4;target=(p[0]+2*kk+D[ho][0],p[1]-2*kk+D[ho][1]);assert sum(source)==sum(target)==len(H)//2-1
  if source==target:
   a=[z for z,x in enumerate(H[i])if x==h].index(j);b=[z for z,x in enumerate(H[ii])if(x+(1 if z%2==0 else-1))%4==ho].index(jj)
   result[r[0]].append({'outgoing_ordinal':a,'incoming_ordinal':b,'duration':len(chain)+1,'physical_source':source,'lower_chain':chain})
 return result

def complete_histories(I,J,isC,rels):
 # Exhaustive binary-heading prefix tree, pruning only fixed counts and actual
 # immediately-consecutive return ranks. Both possible final parities remain.
 plus,minus,dep=(1,3,2)if isC else(0,2,3)
 dm={z['outgoing_ordinal']:z['incoming_ordinal']for z in rels};pm={v:k for k,v in dm.items()};assert len(dm)==len(pm)==len(rels)
 bound=2*(I+J)+int(isC);out=[]
 def dfs(hs,ni,nj,lastdep,pending):
  k=len(hs)
  if ni==I and nj==J and pending is None:out.append(hs)
  if k==bound:return
  for h in(plus,minus):
   isp=h==plus;isd=(h+(1 if k%2==0 else-1))%4==dep;ii=ni+isp;jj=nj+isd
   if ii>I or jj>J:continue
   if pending is not None and not(isp and ni==pending):continue
   if isp and ni in pm and lastdep!=pm[ni]:continue
   nxt=dm.get(nj)if isd else None
   if nxt is not None and ii!=nxt:continue
   dfs(hs+(h,),ii,jj,nj if isd else None,nxt)
 dfs((),0,0,None,None)
 assert len(out)==len(set(out))
 return out,bound

def domains(H,G):
 nextT=len(H)//2-1;isC=bool(nextT%2);a,b=H[-2:];oc=lambda hs,d:sum((x+(1 if j%2==0 else-1))%4==d for j,x in enumerate(hs))
 ports=[(oc(b,1),a.count(2)),(oc(a,1),b.count(2))]if isC else[(oc(a,0),b.count(3)),(oc(b,0),a.count(3))]
 rs=returns(H,G);words=[];bounds=[]
 for r in(0,1):
  ww,bound=complete_histories(*ports[r],isC,rs[r]);words.append(ww);bounds.append(bound)
 return words,ports,rs,bounds

def main():
 start=time.time();source=json.loads((ROOT/'certify_diagonal_read_minimum.json').read_text());old=json.loads((ROOT/'diagonal_selected_pair_exclusions_certificate.json').read_text());oldids={(a,tuple(b))for a,b in old['remaining100_ids']};assert set(IDS)<=oldids
 branches=[];total=Counter();cycle_winds=Counter()
 for case,indices in IDS:
  c=source['cases'][case];s=next(x for x in c['survivors']if tuple(x['A_indices'])==indices);initial=[tuple(h)for h in c['lower_headings']+s['A_headings']];frontier=[initial];rounds=[]
  for row in range(3):
   details=[];nxt=[];stats=Counter()
   for H in frontier:
    k,G=base.graph(H);assert k=='open'and allowed(H);(AA,BB),ports,rels,bounds=domains(H,G);cases=[]
    for ai,a in enumerate(AA):
     for bi,b in enumerate(BB):
      HH=H+[a,b];v=inventory(HH)
      if not allowed(HH):
       kind='residue_budget';w={'named_odd_parity_inventory':v,'violated_bins':[next(i for i,(x,y)in enumerate(zip(v,target))if x>y)for target in TARGETS]}
      else:kind,w=base.graph(HH)
      stats[kind]+=1;total[kind]+=1
      item={'helper_indices':[ai,bi],'outcome':kind}
      if kind=='open':nxt.append(HH)
      else:
       if kind=='closed_component':assert w['winding']<=0 or w['other_local_events']>0;cycle_winds[w['winding']]+=1
       item['witness']=w
      cases.append(item)
    details.append({'complete_histories':H,'next_normal_level':len(H)//2-1,'port_counts':ports,'derived_read_bounds':bounds,'actual_first_return_paths':rels,'complete_helper_domains':[AA,BB],'all_pairs':cases})
   rounds.append({'parent_count':len(frontier),'outcomes':dict(stats),'parents':details});frontier=nxt
   print('BRANCH',case,indices,'ROUND',row,'parents',len(details),'outcomes',dict(stats),flush=True)
  assert not frontier;branches.append({'coarse_id':[case,list(indices)],'initial_histories':initial,'rounds':rounds,'final_open_count':0})
 remain=oldids-set(IDS);assert len(remain)==97
 result={'scope':__doc__,'full_drift':[2,-2],'growth':8,'source227_sha256':hashlib.sha256((ROOT/'certify_diagonal_read_minimum.json').read_bytes()).hexdigest(),'prior100_sha256':hashlib.sha256((ROOT/'diagonal_selected_pair_exclusions_certificate.json').read_bytes()).hexdigest(),'all_ten_full_g8_parity_vectors':TARGETS,'three_excluded_ids':[[a,list(b)]for a,b in IDS],'exact_remaining97_ids':[[a,list(b)]for a,b in sorted(remain)],'total_pair_outcomes':dict(total),'closed_cycle_windings':dict(cycle_winds),'branches':branches,'seconds':time.time()-start,'warning':'One fourth one-minimum branch and all96 two-minimum branches remain OPEN; no entire g8 controller classification.'}
 (ROOT/'one_minimum_three_branches_certificate.json').write_text(json.dumps(result,separators=(',',':'))+'\n');print('DONE',dict(total),dict(cycle_winds),'seconds',result['seconds'],flush=True)
if __name__=='__main__':main()

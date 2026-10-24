#!/usr/bin/env python3
"""All-period exact a5,c3 exclusion of the supplied201 prepared factor.
Derived upper-port bounds, complete return-constrained prefix covers,
physical lifetime fragments and explicit ordinal/clock witnesses only.
"""
from pathlib import Path
from collections import Counter,defaultdict
import json,hashlib
from certify_drift31_read_minimum import depart,returns_to
from partial_drift31_graph import graph
R=Path(__file__).resolve().parent

def fmt(H):return{str(t):list(h)for t,h in sorted(H.items())}
def complete_prefix_cover(I,J,ih,oh,paths,parity):
 dm={p['outgoing_ordinal']:p['incoming_ordinal']for p in paths};pm={v:k for k,v in dm.items()};assert len(dm)==len(pm)==len(paths)
 assert all(p['outgoing_heading']==oh and p['incoming_heading']==ih for p in paths)
 bound=2*(I+J)+1;out=[];tree=[]
 def dfs(hs,ni,nj,lastdep,pending):
  k=len(hs);idx=len(tree);node={'prefix':list(hs),'incoming_count':ni,'outgoing_count':nj,'previous_departure_ordinal':lastdep,'pending_arrival_ordinal':pending,'complete':ni==I and nj==J and pending is None and k%2==parity,'branches':[]};tree.append(node)
  if node['complete']:out.append(hs)
  if k==bound:node['at_derived_bound']=True;return idx
  for h in(ih,(ih+2)%4):
   isp=h==ih;isd=(h+(1 if k%2==0 else-1))%4==oh;ii=ni+isp;jj=nj+isd;why=None
   if ii>I or jj>J:why='fixed_port_count_exceeded'
   elif pending is not None and not(isp and ni==pending):why='forced_next_physical_return_arrival_missing'
   elif isp and ni in pm and lastdep!=pm[ni]:why='forced_previous_physical_return_departure_missing'
   nxt=dm.get(nj)if isd else None
   if why is None and nxt is not None and ii!=nxt:why='wrong_arrival_ordinal_before_forced_return'
   if why is not None:node['branches'].append({'heading':h,'pruned':why})
   else:node['branches'].append({'heading':h,'child':dfs(hs+(h,),ii,jj,nj if isd else None,nxt)})
  return idx
 assert dfs((),0,0,None,None)==0
 return out,bound,tree

def fragment_embedding(h,groups):
 ends={0};rows=[]
 for g in groups:
  starts=[j for j in range(len(h)-len(g)+1)if all(h[j+a]==e['incoming_heading']and(j+a)%2==int(e['turn']=='L')for a,e in enumerate(g))]
  nxt={j+len(g)for e in ends for j in starts if j>=e}
  rows.append({'complete_physical_fragment':g,'all_matching_start_ranks':starts,'reachable_previous_end_ranks':sorted(ends),'reachable_new_end_ranks':sorted(nxt)})
  ends=nxt
 return bool(ends),rows

def main():
 F=json.load(open(R/'open79_paid_chain201_certificate.json'));E=F['events'];by=defaultdict(lambda:defaultdict(list))
 for e in E:by[e['normal_level']][tuple(e['position'])].append(e)
 # Exact factor membership implies P>200: p(P) must equal p(0)+(3,1).
 assert len(E)==201 and E[0]['position']==[2,1]
 assert all(tuple(e['position'])!=(5,2)for e in E)
 groups={t:sorted(d.values(),key=lambda g:(-g[0]['position'][1],g[0]['time']))for t,d in by.items()}
 # Every distinct physical point in one class has a distinct full y lift.
 for t,gg in groups.items():assert len({g[0]['position'][1]for g in gg})==len(gg)
 O={0,1,2,6,7,19,32,34};states=[{34:(0,),35:(),36:(),37:()}];rounds=[];total=Counter();prefix_nodes=0
 for t in range(33,26,-1):
  out=[];parents=[];counts=Counter()
  for H in states:
   lev=sorted(H);kind,G=graph([H[z]for z in lev],lev);assert kind=='open';_,paths=returns_to([H[z]for z in lev],G,t)
   if t%2==0:ih,I,oh,J=2,len(depart(H[t+3],2)),3,H[t+1].count(3)
   else:ih,I,oh,J=1,len(depart(H[t+1],1)),0,H[t+3].count(0)
   domain,bound,tree=complete_prefix_cover(I,J,ih,oh,paths,int(t in O));prefix_nodes+=len(tree);cases=[]
   for h in domain:
    HH=H|{t:h};ll=sorted(HH);kind,w=graph([HH[z]for z in ll],ll);row={'word':list(h),'outcome':kind}
    if kind=='open':
     ok,em=fragment_embedding(h,groups.get(t,[]));row['complete_fragment_embedding']=em
     if ok:out.append(HH)
     else:kind='no_complete_fragment_embedding';row['outcome']=kind
    else:row['witness']=w
    counts[kind]+=1;cases.append(row)
   parents.append({'complete_upper_before':fmt(H),'incoming_heading_count':[ih,I],'outgoing_heading_count':[oh,J],'derived_bound':bound,'required_parity':int(t in O),'actual_first_return_paths':paths,'exhaustive_prefix_tree':tree,'complete_return_compatible_domain':[list(h)for h in domain],'all_outcomes':cases})
  rounds.append({'level':t,'input_parent_count':len(states),'parents':parents,'counts':dict(counts)});total.update(counts);states=out;print(t,'parents',len(parents),dict(counts),flush=True)
 assert not states
 assert rounds[-1]['counts']=={'positive_rank_clock_cycle':24,'no_complete_fragment_embedding':11,'skipped_rank':50}
 assert rounds[-2]['counts']=={'open':9,'skipped_rank':6,'no_complete_fragment_embedding':9,'positive_rank_clock_cycle':2}
 assert sum(len(p['complete_return_compatible_domain'])for rr in rounds for p in rr['parents'])==187
 out={'scope':__doc__,'full_odd_inventory':sorted(O),'max_complete_read_level':34,'period_lower_bound':{'P_strictly_greater_than':200,'proof':'A full(3,1) translation period from the factor start(2,1) must revisit(5,2) at timeP. None of the201 observed read positions is(5,2).'},'physical_fragment_order':{'canonical_clock':'actual_time - full_y_lift * P','proof':'All observed times lie in[0,200], so P>200 orders distinct full-y-lift fragments strictly by decreasing lift. Each physical fragment is consecutive in its own complete rank history; unobserved ranks between fragments remain allowed.','groups_used':{str(t):gg for t,gg in groups.items()if 27<=t<=34}},'lower_exterior':'All levels <=26 are omitted and UNKNOWN throughout.','rounds':rounds,'total_outcome_counts':dict(total),'total_return_compatible_complete_words':187,'total_prefix_nodes':prefix_nodes,'final_open_count':0,'limits':'Excludes the supplied201 factor in the exact a5,c3 inventory at all periods and all multiplicities. The derived lower bound P>200 is not a search cutoff. Does not exclude every a5 front or any larger-a embedding. All prepared input lifetimes are retained; only complete ownership and physical chronology rule out this completion.','dependency_hashes':{f:hashlib.sha256((R/f).read_bytes()).hexdigest()for f in ['OPEN79_PAID_CHAIN201_AND_UNPAID67_CONTRAST.md','open79_paid_chain201_certificate.json','DRIFT31_TWO_QUAD_EXTREME_READ_EXCLUSIONS.md','certify_drift31_read_minimum.py','partial_drift31_graph.py']}}
 (R/'paid201_top_c3_owner_obstruction_certificate.json').write_text(json.dumps(out,separators=(',',':'))+'\n');print('PASS all187 return-compatible words, explicit prefix coverage and every physical rank/clock witness; total prefix nodes',prefix_nodes)
if __name__=='__main__':main()

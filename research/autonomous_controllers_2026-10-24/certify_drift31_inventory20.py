#!/usr/bin/env python3
"""Proof-producing complete two-ended rejection of one supplied O20 inventory.
No solver, imposed multiplicity cap, or period bound. Every omitted class is
UNKNOWN until joined; outer empty read levels follow actual complete extrema.
"""
from pathlib import Path
import hashlib,json
from collections import Counter
from partial_drift31_graph import graph
from certify_drift31_read_minimum import words,returns_to,depart
ROOT=Path(__file__).resolve().parent
ODD={0,1,2,5,6,8,13,20}
PROOF=[];COUNTS=Counter()
def fmt(H):return{str(t):list(h)for t,h in sorted(H.items())}
def GG(H):
 levels=sorted(H);return graph([H[t]for t in levels],levels)
def relation_paths(H,t):
 k,G=GG(H);assert k=='open'
 levels=sorted(H);_,pp=returns_to([H[z]for z in levels],G,t)
 return G,pp

def expand(states,t,side,exact_length=None):
 result=[];stats=Counter()
 for H in states:
  G,pp=relation_paths(H,t)
  if side=='bottom':
   if t%2==0:ih,I,oh,J=0,len(depart(H[t-3],0)),1,H[t-1].count(1)
   else:ih,I,oh,J=3,len(depart(H[t-1],3)),2,H[t-3].count(2)
  else:
   if t%2==0:ih,I,oh,J=2,len(depart(H[t+3],2)),3,H[t+1].count(3)
   else:ih,I,oh,J=1,len(depart(H[t+1],1)),0,H[t+3].count(0)
  bound=2*(I+J)+1
  if exact_length is not None:bound=exact_length(H)
  raw=words(t%2,bound,ih,I,oh,J)
  dd=[]
  for h in raw:
   if len(h)%2!=int(t in ODD):continue
   if exact_length is not None and len(h)!=bound:continue
   if not all([j for j,hi in enumerate(h)if hi==p['incoming_heading']][p['incoming_ordinal']]==depart(h,p['outgoing_heading'])[p['outgoing_ordinal']]+1 for p in pp):continue
   dd.append(h)
  entry={'level':t,'side':side,'complete_named_before':fmt(H),'known_incoming_heading_count':[ih,I],'known_outgoing_heading_count':[oh,J],'derived_bound':bound,'bound_is_exact_length':exact_length is not None,'parity':int(t in ODD),'actual_first_return_paths':pp,'complete_domain_after_necessary_returns':dd,'outcomes':[]}
  for h in dd:
   HH=H|{t:tuple(h)};kind,w=GG(HH);stats[kind]+=1;out={'history':h,'outcome':kind}
   if kind=='open':result.append(HH)
   else:
    out['witness']=w
    if kind=='closed_component':
     assert w['winding']<=0 or w['other_local_events']>0
   entry['outcomes'].append(out)
  PROOF.append(entry)
 COUNTS[f'{side}_T{t}_parents']+=len(states)
 for k,v in stats.items():COUNTS[f'{side}_T{t}_{k}']+=v
 print(t,side,len(states),dict(stats),flush=True)
 return result

def main():
 bot={t:tuple('NESW'.index(c)for c in s)for t,s in enumerate(['S','W','S','EEWE','SSNS','EEW','NNN','EEEW'])}|{t:()for t in [-3,-2,-1]}
 top={20:(0,),21:(),22:(),23:()}
 T=[top]
 for t in [19,18,17,16,15,14]:T=expand(T,t,'top')
 assert len(T)==2 and {H[14]for H in T}=={(0,0,2,2,0,2,0,0),(0,0,2,2,0,0,0,2)}
 assert all(H[15]==(1,3,3,1,1,3)and H[16]==(0,0,2,0,0,2)for H in T)
 B=[bot]
 for t in [8,9,10]:B=expand(B,t,'bottom')
 assert len(B)==4
 # Before T11 is read, both sides fix all its outgoing counts.
 # S output = #S incoming atT8=5, N output = #N incoming atT14=5.
 merged=[b|t for b in B for t in T]
 for H in merged:
  assert GG(H)[0]=='open';assert H[8].count(2)==5 and H[14].count(0)==5
 M=expand(merged,11,'bottom',lambda H:H[8].count(2)+H[14].count(0))
 assert len(M)==44
 # Both incoming counts at T12 are now fixed: eight N fromT9 and four S fromT15.
 for H in M:assert len(depart(H[9],0))==8 and len(depart(H[15],2))==4
 final=expand(M,12,'bottom',lambda H:len(depart(H[9],0))+len(depart(H[15],2)))
 assert not final
 assert COUNTS['bottom_T12_skipped_rank']==43 and COUNTS['bottom_T12_positive_rank_clock_cycle']==9 and COUNTS['bottom_T12_closed_component']==6
 result={'scope':__doc__,'full_drift':[3,1],'full_odd_inventory':sorted(ODD),'complete_read_extrema':[0,20],'forced_two_quad_prefix':fmt(bot),'top_seed':fmt(top),'counts':dict(COUNTS),'all_proof_records':PROOF,'surviving_top_interfaces':[fmt(H)for H in T],'surviving_bottom_T10_interfaces':[fmt(H)for H in B],'final_open_count':0,'unassigned_middle_level':13,'dependency_hashes':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()for p in ['DRIFT31_CIRCLE_MIDDLE_READ_REDUCTION.md','DRIFT31_TWO_QUAD_EXTREME_READ_EXCLUSIONS.md','partial_drift31_graph.py','certify_drift31_read_minimum.py']},'warning':'This excludes only extensions of the two-quad single-used F-circle prefix with this exact FULL odd inventory. It does not exclude larger c or other drifts/circle branches. T13 and every omitted exterior class are UNKNOWN, never empty.'}
 (ROOT/'drift31_inventory20_certificate.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
 print(dict(COUNTS))
if __name__=='__main__':main()

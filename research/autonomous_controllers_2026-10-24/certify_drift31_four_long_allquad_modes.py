#!/usr/bin/env python3
"""All-cap rejection of four specified long T6 all-quad circle interfaces.
No odd-output/growth assumption in this local extension. Exterior UNKNOWN.
"""
import json,hashlib
from pathlib import Path
from collections import Counter
from certify_drift31_read_minimum import words,depart,returns_to
from partial_drift31_graph import graph
ROOT=Path(__file__).resolve().parent

def fmt(H):return{str(t):list(h)for t,h in sorted(H.items())}
def GG(H):
 L=sorted(H);return graph([H[t]for t in L],L)
def ext(H,t):
 k,G=GG(H);assert k=='open';L=sorted(H);_,pp=returns_to([H[z]for z in L],G,t)
 if t%2==0:ih,I,oh,J=0,len(depart(H[t-3],0)),1,H[t-1].count(1)
 else:ih,I,oh,J=3,len(depart(H[t-1],3)),2,H[t-3].count(2)
 dd=[]
 for h in words(t%2,2*(I+J)+1,ih,I,oh,J):
  if not all([j for j,hi in enumerate(h)if hi==p['incoming_heading']][p['incoming_ordinal']]==depart(h,p['outgoing_heading'])[p['outgoing_ordinal']]+1 for p in pp):continue
  dd.append(h)
 return {'level':t,'histories_before':fmt(H),'incoming_heading_count':[ih,I],'outgoing_heading_count':[oh,J],'derived_bound':2*(I+J)+1,'actual_first_returns':pp,'complete_domain':dd}

def main():
 src=json.loads((ROOT/'drift31_circle_middle_reads_certificate.json').read_text());modes=[s for s in src['eight_OPEN_interfaces']if len(s['T5'])==4 and len(s['T6'])>=8];assert len(modes)==4
 records=[];C=Counter()
 for s in modes:
  H={t:tuple(h)for t,h in enumerate(s['complete_named_histories'])};e=ext(H,8);out=[]
  for h in e['complete_domain']:
   HH=H|{8:tuple(h)};k,w=GG(HH);C['T8_'+k]+=1;r={'history':h,'T8_outcome':k}
   if k!='open':r['witness']=w;out.append(r);continue
   # Use actual same-physical returns before generating any T9 word.
   L=sorted(HH);_,pp=returns_to([HH[t]for t in L],w,9)
   first=[i for i,p in enumerate(pp)if p['incoming_heading']==3 and p['outgoing_heading']==2 and p['incoming_ordinal']==0]
   pair=None
   for i in first:
    a=pp[i]['outgoing_ordinal']
    for j,p in enumerate(pp):
     if p['incoming_heading']==3 and p['outgoing_heading']==2 and p['outgoing_ordinal']==a+1 and p['incoming_ordinal']!=1:pair=[i,j]
   if pair:
    r.update(outcome='rotated_first_arrival_Rule_B',actual_T9_returns=pp,rule_path_pair=pair);C['T9_Rule_B']+=1
   else:
    f=ext(HH,9);fout=[]
    for z in f['complete_domain']:
     kk,ww=GG(HH|{9:tuple(z)});assert kk=='skipped_rank';C['T9_skipped_rank']+=1;fout.append({'history':z,'outcome':kk,'witness':ww})
    assert fout;r.update(outcome='complete_T9_domain_rejected',T9_cover=f,T9_outcomes=fout)
   out.append(r)
  e['all_T8_outcomes']=out;records.append(e)
 assert C['T9_Rule_B']==16 and C['T9_skipped_rank']==42
 result={'scope':__doc__,'source_middle_read_certificate_sha256':hashlib.sha256((ROOT/'drift31_circle_middle_reads_certificate.json').read_bytes()).hexdigest(),'signed_rule_B_note_sha256':hashlib.sha256((ROOT/'FIRST_N_RETURN_RULES_DIAGONAL_REDUCTION.md').read_bytes()).hexdigest(),'four_excluded_modes':[[s['T6'],s['T7']]for s in modes],'records':records,'counts':dict(C),'remaining_short_modes':[[s['T6'],s['T7']]for s in src['eight_OPEN_interfaces']if len(s['T5'])==4 and len(s['T6'])<8],'warning':'No higher completion, three-short-mode exclusion or single-used-circle existence is asserted.'}
 (ROOT/'drift31_four_long_allquad_modes_certificate.json').write_text(json.dumps(result,separators=(',',':'))+'\n');print(dict(C))
if __name__=='__main__':main()

#!/usr/bin/env python3
"""One-period standard104 surgery: reorder all return excursions at ONE pose.
Full spatial event inventory is unchanged; exact stable histories decide words.
"""
import json,hashlib
from itertools import permutations
from collections import defaultdict,Counter
from pathlib import Path
from check_extremal_read_coupling import ROOT,event_word,quotient
OUT=Path(__file__).resolve().parent
W=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];P=len(W)

def classify(w):
 ev,d,h=event_word(w);assert h==0 and d!=(0,0);H=defaultdict(list)
 for e in ev:
  r,k=quotient(e['p'],d);H[r].append({'clock':e['t']-P*k,'phase':e['t'],'turn':e['c'],'physical_position':e['p'],'copy':k})
 for r,es in sorted(H.items()):
  es.sort(key=lambda e:e['clock'])
  for a,b in zip(es,es[1:]):
   if a['turn']==b['turn']:return {'status':'nonalternating','class':r,'first':a,'second':b}
 black=[r for r,es in H.items()if sorted(es,key=lambda e:e['clock'])[0]['turn']=='L']
 if black:return {'status':'prepared_input_only','black_first_classes':sorted(black)}
 return {'status':'complete_WHITE','standard':w in W+W,'drift':d}

def main():
 stats=Counter();rows=[];distinct={};source_profiles=[]
 for i in range(P):
  base=W[i:]+W[:i];ev,d,h=event_word(base);cuts=[e['t']for e in ev if e['p']==(0,0)and e['hi']==0]
  loops=[base[a:b]for a,b in zip(cuts,cuts[1:])];tail=base[cuts[-1]:];source_profiles.append({'phase':i,'cuts':cuts,'loop_lengths':list(map(len,loops))})
  baseline_inventory=Counter((e['p'],e['hi'],e['ho'],e['c'])for e in ev)
  for perm in permutations(range(len(loops))):
   candidate=''.join(loops[j]for j in perm)+tail;cev,cd,ch=event_word(candidate);assert cd==d and ch==h
   assert Counter((e['p'],e['hi'],e['ho'],e['c'])for e in cev)==baseline_inventory
   result=classify(candidate);stats['all_parameter_choices']+=1;stats[result['status']]+=1
   if candidate not in W+W:stats['nonstandard_parameter_choices']+=1
   distinct.setdefault(candidate,result)
   rows.append({'base_phase':i,'permutation':perm,'word':candidate,'result':result})
 dc=Counter(r['status']for r in distinct.values());nonstandard={w:r for w,r in distinct.items()if w not in W+W};nd=Counter(r['status']for r in nonstandard.values())
 out={'scope':__doc__,'standard_sha256':hashlib.sha256(W.encode()).hexdigest(),'source_pose_slots':source_profiles,'counts':dict(stats),'distinct_words':len(distinct),'distinct_status_counts':dict(dc),'distinct_nonstandard_words':len(nonstandard),'distinct_nonstandard_status_counts':dict(nd),'all_candidates':rows,'complete_WHITE_nonstandard':[{ 'word':w,'result':r}for w,r in nonstandard.items()if r['status']=='complete_WHITE']}
 (OUT/'standard_pose_excursion_surgery.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k not in('source_pose_slots','all_candidates')},indent=2))
if __name__=='__main__':main()

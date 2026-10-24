"""One exact lookup in the EXISTING k7 literal corpus, no expanded search."""
import json
from pathlib import Path
R=Path(__file__).resolve().parent
D=json.loads((R/'chronology_dcuv/literal_factor_dfa_k7.json').read_text());G=json.loads((R/'chronology_dcuv/literal_residual_geometry.json').read_text())['geometry']
IDS=(0,1,4,5,6,7,8,9)

def rot(p,h):
 x,y=p;return ((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
words=[tuple(w) for w in D['states']]
for i,w in enumerate(D['states']):
 if len(w)==6:
  words.extend(tuple(w+[a]) for a,target in zip(IDS,D['transitions'][D['state_to_class'][i]]) if target>=0)
words=sorted(set(words),key=lambda w:(len(w),w));hits=[];c_hist={}
for w in words:
 p,h,c=(0,0),0,0
 for a in w:
  e=G[a]['endpoint'];v=rot(e[:2],h);p=p[0]+v[0],p[1]+v[1];h=(h+e[2])%4;c+=G[a]['name'].count('C')
 if w and p==(0,0) and h==0:
  hits.append({'word':w,'names':[G[a]['name'] for a in w],'C_count':c});c_hist[c]=c_hist.get(c,0)+1
result={'scope':'Exactly the existing literal k7 corpus through7 full packets; absence is bounded evidence only, not all-return exclusion.','saved_literal_words':len(words),'return_count':len(hits),'C_count_histogram':c_hist,'returns':hits}
(R/'chronology_dcuv/retained_k7_full_pose_return_lookup.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))

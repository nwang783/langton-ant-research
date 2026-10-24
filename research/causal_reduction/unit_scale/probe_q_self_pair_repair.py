"""Target the one missing Q self-interface class using its two adjacent minimal endpoint bypasses."""
from pathlib import Path
import json,collections,hashlib
import certify_short_refinement_rup as core
P=Path(__file__).parent
Q=json.loads((P/'forward108_prepared_control.json').read_text())['word']
source=json.loads((P/'forward108_self_interfaces.json').read_text());O=set(map(tuple,source['source_output']))
pal=json.loads((P/'minimal_pair_bypass_geometry.json').read_text())['inventories']
records=[]
for j in(71,72):
 for k,rep in enumerate(pal[Q[j:j+2]][1:]):
  w=Q[:j]+rep+Q[j+2:];rr,e,h=core.trace(w,(0,14),3);assert(e,h)==((-2,12),3)
  by=collections.defaultdict(list)
  for t,(p,hh,c)in enumerate(rr):by[(p[0]-p[1],p[0]%2)].append((t+len(w)*(p[0]//2),t,p,c))
  bad=[];I=set();out=set()
  for a,es in sorted(by.items()):
   es.sort()
   if es[0][-1]=='L':I.add(a)
   if es[-1][-1]=='R':out.add(a)
   if(a in O)!=(es[0][-1]=='L'):bad.append(dict(kind='input',orbit=a,first=es[0],source_black=a in O))
   for u,v in zip(es,es[1:]):
    if u[-1]==v[-1]:bad.append(dict(kind='repeat',orbit=a,previous=u,current=v))
  records.append(dict(pair_phase=j,pair=Q[j:j+2],replacement=rep,word=w,input=sorted(I),output=sorted(out),bad=bad))
result=dict(scope=__doc__,records=records,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(P/'q_self_pair_repair_probe.json').write_text(json.dumps(result,indent=2)+'\n')
for x in records:print(x['pair_phase'],x['replacement'],len(x['bad']),x['bad'][:2])

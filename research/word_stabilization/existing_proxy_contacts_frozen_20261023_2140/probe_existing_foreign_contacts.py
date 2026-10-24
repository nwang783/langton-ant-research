"""Scan ONLY the fixed existing six-return physical-history edge list.
No extension, continuation enumeration, new prefix tree, depth cap, or node cap.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict,Counter
import json,importlib.util
W=Path('/workspace/shared/langton/word_stabilization')
spec=importlib.util.spec_from_file_location('lit',W/'check_foreign_return_interfaces.py');lit=importlib.util.module_from_spec(spec);spec.loader.exec_module(lit)
G=json.loads((W/'shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json').read_text());words=[x['word']for x in G['macro_words']];M=lit.M
H=json.loads((W/'shifted1_llrlrrrrlll_history6_scc2_port_quotient.json').read_text())
R=[line.split()for line in(W/'shifted1_llrlrrrrlll.returns.tsv').read_text().splitlines()]
R.sort(key=lambda x:(len(x[2]),x[2],x[0],x[1]))
A=defaultdict(list)
for ei,(u,a,v)in enumerate(G['quotient_edges']):A[(u,a)].append((v,ei))
def graphpath(labels):
 states={q:[]for q in range(214)}
 for a in labels:
  out={}
  for q,path in states.items():
   for r,i in A[(q,a)]:out.setdefault(r,path+[i])
  states=out
 if not states:return None
 q,p=next(iter(states.items()));return p

def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def contact(a,b,c,d):
 u=sub(b,a);v=sub(d,c);p=sub(c,a);det=cross(u,v)
 if det:
  s=Q(cross(p,v),det);t=Q(cross(p,u),det)
  if 0<=s<=1 and 0<=t<=1:return {'s':str(s),'t':str(t),'point':[str(a[k]+s*u[k])for k in(0,1)]}
  return None
 if cross(p,u):return None
 k=0 if u[0] else 1
 s0=Q(c[k]-a[k],u[k]);s1=Q(d[k]-a[k],u[k]);lo=max(Q(0),min(s0,s1));hi=min(Q(1),max(s0,s1))
 if lo>hi:return None
 return {'s_interval':[str(lo),str(hi)],'overlap':lo<hi,'point':[str(a[k]+lo*u[k])for k in(0,1)]}

def pieces(labels):
 p=(0,0);h=0;z=(-1,-1);out=[]
 for bi,a in enumerate(labels):
  start=z
  # Doubled corrected-center displacement per genuine proxy piece.
  ds={0:[(2,2)],1:[(2,2)],2:[(2,6)],3:[(0,8)],4:[(-6,-2)],5:[(-6,-2),(0,-4)],6:[(-6,-2),(2,-6)]}[a]
  for pi,d in enumerate(ds):
   d=lit.rot(d,h);z=(z[0]+d[0],z[1]+d[1]);out.append({'a':start,'b':z,'label':a,'block':bi,'piece':pi});start=z
  raw=lit.trace(words[a]);ep=lit.rot(raw['pose'][:2],h);p=(p[0]+ep[0],p[1]+ep[1]);h=(h+raw['pose'][2])%4
  r=lit.rot((-1,-1),h);assert z==(2*p[0]+r[0],2*p[1]+r[1])
 return out

def firstcontact(ps):
 for j in range(len(ps)):
  hits=[]
  for i in range(j):
   a,b=ps[i],ps[j];hit=contact(a['a'],a['b'],b['a'],b['b'])
   if hit is None:continue
   if j==i+1 and not hit.get('overlap') and hit.get('point')==list(map(str,a['b'])):continue
   hits.append((i,hit))
  if hits:
   i,hit=hits[0];return {'earlier_piece':i,'later_piece':j,'earlier':ps[i],'later':ps[j],'intersection':hit}
 return None

def main():
 seen=set();hist_count=0;parsed_count=0;kind=Counter();best={};allfound=[]
 for he,(u,a,v)in enumerate(H['history_edges']):
  ids=H['history_states'][u]+[H['source_return_ids'][a]]
  tup=tuple(ids)
  if tup in seen:continue
  seen.add(tup);hist_count+=1
  raw=''.join(R[i][2]for i in ids);full=raw+R[ids[-1]][1]
  check=lit.trace(full);assert check['feasible']
  starts=[i for i in range(len(raw))if full.startswith(M,i)]
  for start in starts:
   labels=[];pos=start;cuts=[]
   while pos<len(raw):
    opts=[(a,len(w))for a,w in enumerate(words)if pos+len(w)<=len(raw)and full.startswith(w+M,pos)]
    if not opts:break
    assert len(opts)==1
    a,n=opts[0];labels.append(a);cuts.append(pos);pos+=n
   if len(labels)<2 or not any(a>=4 for a in labels):continue
   parsed_count+=1;gp=graphpath(labels)
   if gp is None:continue
   ps=pieces(labels);fc=firstcontact(ps)
   if fc:
    key=('U_entry_'if labels[0]==3 else 'other_entry_')+('foreign_first'if fc['earlier']['label']>=4 or fc['later']['label']>=4 else'ordinary_first')
    kind[key]+=1
    rec={'source_history_edge':he,'original_return_ids':ids,'start_offset':start,'raw_stop_offset':pos,'labels':labels,'graph_edge_ids_LABEL_COMPATIBILITY_ONLY':gp,'first_contact':fc,'raw_word':full[start:pos],'actual_marker':M,
         'source_full_word':raw,'source_end_marker':R[ids[-1]][1]}
    allfound.append(rec)
    score=(len(rec['raw_word']),len(labels))
    if key not in best or score<best[key][0]:best[key]=(score,rec)
 print('histories',hist_count,'parsed_sections',parsed_count,'firstcontact_counts',dict(kind))
 for k,(s,r)in best.items():print(k,s,'labels',r['labels'],'contact',r['first_contact'],'hist',r['source_history_edge'])
 out={'scope':'ONLY fixed existing13516 six-return history edges; no new physical prefix search. Label compatibility is not realization of incoming214 history class.','histories':hist_count,'parsed_sections':parsed_count,'counts':dict(kind),'best_controls':{k:r for k,(s,r)in best.items()},'all_contact_controls':allfound}
 (W/'probe_existing_foreign_contacts.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()

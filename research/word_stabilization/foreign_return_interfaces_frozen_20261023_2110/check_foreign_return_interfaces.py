"""Exact fixed-graph return sections and finite literal foreign interfaces.
No physical trajectory-prefix tree or continuation search is executed.
"""
from pathlib import Path
from collections import defaultdict,deque,Counter
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json'
M='LLLLRLRRRRL';K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)}
DIRS=((0,1),(1,0),(0,-1),(-1,0))
def rot(p,h):
 x,y=p
 return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def trace(word):
 p=(0,0);h=0;first={};last={}
 for t,c in enumerate(word):
  if p in last and last[p][0]==c:
   return {'feasible':False,'conflict_read':t,'previous_read':last[p][1],'cell':list(p),'turn':c}
  first.setdefault(p,(c,t));last[p]=(c,t)
  h=(h+(1 if c=='R'else-1))%4;d=DIRS[h];p=(p[0]+d[0],p[1]+d[1])
 return {'feasible':True,'pose':(*p,h),'first':first,'last':last}
def literal_geometry(w):
 r=trace(w);c=trace(w+M);assert r['feasible'] and c['feasible']
 entry={p for p,(q,t)in c['first'].items()if q=='L'};assert K<=entry
 after=set(entry)
 for p,(q,t)in r['last'].items():
  if q=='R':after.add(p)
  else:after.discard(p)
 x,y,h=r['pose'];ec={(x+rot(p,h)[0],y+rot(p,h)[1])for p in K};assert ec<=after
 I=entry-K;O=after-ec;assert all(p in r['last']and r['last'][p][0]=='R'for p in O)
 assert I.isdisjoint(K)and O.isdisjoint(ec)
 return {'word':w,'raw_length':len(w),'endpoint':list(r['pose']),
         'requirements':[[*p,q=='L',t]for p,(q,t)in sorted(c['first'].items())],
         'inputs':list(map(list,sorted(I))),'outputs':list(map(list,sorted(O))),
         'recycled':list(map(list,sorted(I&O))),
         'marker_only_inputs':list(map(list,sorted(p for p in I if p not in r['first']))),
         'net_mass':len(O)-len(I),'raw_radius':max(max(map(abs,p))for p in r['first']),
         'complete_context_radius':max(max(map(abs,p))for p in c['first'])}
def control(word,cut,protected):
 r=trace(word+M);assert r['feasible']
 seed={p for p,(c,t)in r['first'].items()if c=='L'}
 B=set(seed);p=(0,0);h=0;mid=None
 for t,c in enumerate(word+M):
  assert(p in B)==(c=='L')
  if c=='L':B.remove(p)
  else:B.add(p)
  h=(h+(1 if c=='R'else-1))%4;d=DIRS[h];p=(p[0]+d[0],p[1]+d[1])
  if t+1==cut:mid=(p,h,set(B))
 raw=trace(word);assert raw['feasible']
 out={'seed':list(map(list,sorted(seed))),'entry_mass':len(seed),'raw_length':len(word),
      'raw_endpoint':list(raw['pose']),'raw_exit_mass':len(seed)+sum(1 if c=='R'else-1 for c in word),
      'including_actual_marker_exit_mass':len(B)}
 if protected:
  assert mid is not None
  ep,eh,atcut=mid;assert protected<=atcut
  future=trace(word[cut:]+M);assert future['feasible']
  ctx={(ep[0]+rot(q,eh)[0],ep[1]+rot(q,eh)[1])for q in future['first']}
  assert protected.isdisjoint(ctx)and protected<=B
  out['source_outputs_protected']=list(map(list,sorted(protected)))
  out['complete_future_context_hits']=[]
 return out

def main():
 g=json.loads(SRC.read_text());E=g['quotient_edges'];words=[x['word']for x in g['macro_words']]
 geom=[literal_geometry(w)for w in words]
 assert [(len(geom[i]['inputs']),len(geom[i]['outputs']),geom[i]['net_mass'])for i in(4,5,6)]==[(14,16,2),(15,21,6),(18,24,6)]
 P=sorted({v for u,t,v in E if t>=4});Q=sorted({u for u,t,v in E if t>=4})
 assert(len(P),len(Q),len(set(P)|set(Q)))==(35,53,88)
 te=[i for i,e in enumerate(E)if e[1]>=4];de=[i for i,e in enumerate(E)if e[1]<4]
 adj=defaultdict(list)
 for i in de:adj[E[i][0]].append(i)
 witnesses=[];records=[];labels=set()
 for s in P:
  seen={s:[]};queue=deque([s])
  while queue:
   u=queue.popleft()
   for i in adj[u]:
    v=E[i][2]
    if v not in seen:seen[v]=seen[u]+[i];queue.append(v)
  for q in Q:
   if q in seen:witnesses.append([s,q,seen[q]])
  for i in te:
   u,t,v=E[i]
   if u in seen:
    records.append([s,i]);labels.add((s,t,v))
 assert(len(witnesses),len(labels),max(len(r[2])for r in witnesses))==(1721,1578,8)
 ports=[]
 for p in P:
  out=[i for i,e in enumerate(E)if e[0]==p];bits=sorted({'L'if E[i][1]==0 else'R'for i in out})
  assert len(bits)==1 and all(E[i][1]<4 for i in out)
  ports.append({'state':p,'actual_foreign_in_edge_ids':[i for i in te if E[i][2]==p],
                'all_next_edge_ids':out,'required_actual_twelfth_marker_turn':bits[0]})
 assert Counter(p['required_actual_twelfth_marker_turn']for p in ports)=={'L':10,'R':25}
 pairs={}
 for i in(4,5,6):
  for j in(4,5,6):
   r=trace(words[i]+words[j]+M)
   if r['feasible']:pairs[f'{i}_{j}']={'feasible':True,**control(words[i]+words[j],0,set())}
   else:pairs[f'{i}_{j}']=r
 assert [k for k,v in pairs.items()if v['feasible']]==['5_4','6_4']
 protected={tuple(p)for p in geom[3]['outputs']}
 immediate={str(i):control(words[3]+words[i],len(words[3]),protected)for i in(4,5,6)}
 assert [x['entry_mass']for x in immediate.values()]==[24,25,28]
 out={'status':'AUTHOR_EXACT_FIXED_GRAPH_AND_LITERAL_RETURN_INTERFACES_PENDING_INDEPENDENT_REPLAY',
      'scope':'35-port return NFA is CONDITIONAL on the inherited214-state quotient, not a cover of all physical seven-word factors. QF/BF actual controls prove the distinction.',
      'source_graph_sha256':hashlib.sha256(SRC.read_bytes()).hexdigest(),
      'literal_geometry':geom,'original_edges':E,'dcuv_edge_ids':de,'foreign_edge_ids':te,
      'postforeign_ports':ports,'preforeign_ports':Q,'dcuv_reachability_witnesses':witnesses,
      'return_records_from_postport_and_actual_foreign_edge_id':records,
      'deduplicated_return_edges':list(map(list,sorted(labels))),
      'counts':{'source_states':214,'source_edges':993,'foreign_edges':len(te),'postforeign_ports':len(P),'preforeign_ports':len(Q),
                'connector_pairs':len(witnesses),'full_return_records':len(records),'labelled_return_edges':len(labels),
                'max_shortest_connector_edges_NOT_A_PHYSICAL_BOUND':8,'marker12_L':10,'marker12_R':25},
      'all_nine_fixed_foreign_pairs':pairs,'immediate_U_foreign_controls':immediate,
      'clean_scope_warning':'Actual untouched producer IDs survive; complete-eight unconsumability authority does NOT survive a foreign reader. Preserve old birth tags but clear clean-eight scope bits.'}
 Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out['counts']));print('positive_foreign_pairs',[(k,x['entry_mass'])for k,x in pairs.items()if x['feasible']])
if __name__=='__main__':main()

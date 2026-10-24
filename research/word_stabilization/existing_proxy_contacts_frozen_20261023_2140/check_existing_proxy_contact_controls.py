"""Fixed replay of FOUR controls already present in the frozen six-history corpus.
Checks56 exact predecessor queries, not a continuation/prefix search.
"""
from pathlib import Path
import json,hashlib,importlib.util
W=Path('/workspace/shared/langton/word_stabilization')
def module(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
p=module('proxy',W/'probe_existing_foreign_contacts.py');lit=p.lit
corpus=json.loads((W/'probe_existing_foreign_contacts.json').read_text())
assert corpus['histories']==13516 and corpus['parsed_sections']==19653
seqs=sorted({tuple(x['labels'])for x in corpus['all_contact_controls']})
assert seqs==[(0,1,2,2,5,2),(0,1,2,3,6,2),(2,2,5,1,0,0),(2,3,6,1,0,0)]
controls=[];queries=[]
def compatible(labels,bit):
 states={q:[]for q in range(214)}
 for a in labels:
  nxt={}
  for q,path in states.items():
   for r,i in p.A[(q,a)]:nxt.setdefault(r,path+[i])
  states=nxt
 for q,ids in states.items():
  if any((a==0)==(bit=='L')for u,a,v in p.G['quotient_edges']if u==q):return ids
 raise AssertionError('no label path with actual marker12')
for seq in seqs:
 r=next(x for x in corpus['all_contact_controls']if tuple(x['labels'])==seq)
 he=r['source_history_edge'];u,a,v=p.H['history_edges'][he]
 ids=p.H['history_states'][u]+[p.H['source_return_ids'][a]]
 assert ids==r['original_return_ids']
 raw=''.join(p.R[i][2]for i in ids);marker=p.R[ids[-1]][1]
 assert r['start_offset']==0 and r['raw_word']==raw and r['raw_stop_offset']==len(raw)
 assert ''.join(p.words[i]for i in seq)==raw
 tr=lit.trace(raw+marker);assert tr['feasible']
 seed={x for x,(c,t)in tr['first'].items()if c=='L'}
 ps=p.pieces(seq);fc=p.firstcontact(ps);assert fc is not None
 assert fc['earlier']['label']<4 and fc['later']['label']<4
 # Exact positions, plus direct physical raw+all12marker replay.
 B=set(seed);xy=(0,0);h=0
 for c in raw+marker:
  assert (xy in B)==(c=='L')
  if c=='L':B.remove(xy)
  else:B.add(xy)
  h=(h+(1 if c=='R'else-1))%4;dx,dy=lit.DIRS[h];xy=(xy[0]+dx,xy[1]+dy)
 gp=compatible(seq,marker[11])
 pre=[];preD=[]
 for a in range(7):
  rr=lit.trace(p.words[a]+raw+lit.M)
  ss=lit.trace(p.words[a]+p.words[0]+raw+lit.M)
  def diag(z):
   if z['feasible']:return {'feasible':True,'first_L_count':sum(c=='L'for c,t in z['first'].values())}
   return z
  pre.append(diag(rr));preD.append(diag(ss))
 assert [a for a,z in enumerate(pre)if z['feasible']]==[0]
 assert not any(z['feasible']for z in preD)
 queries.append({'labels':seq,'predecessor_cases_M11':pre,'predecessors_of_D_extended_M11':preD})
 ext=lit.trace(p.words[0]+raw+marker);assert ext['feasible']
 controls.append({'labels':seq,'source_history_edge':he,'sorted_original_return_ids':ids,
                  'source_actual_marker12':marker,'raw_length':len(raw),'seed_mass_raw_plus_marker12':len(seed),
                  'seed':list(map(list,sorted(seed))),'raw_exit_mass':len(seed)+sum(1 if c=='R'else-1 for c in raw),
                  'actual_raw_endpoint':list(lit.trace(raw)['pose']),
                  'proxy_pieces_doubled':ps,'first_contact':fc,
                  'graph_path_LABEL_AND_ENDMARKER_COMPATIBILITY_ONLY':gp,
                  'D_extended_seed_mass_marker12':sum(c=='L'for c,t in ext['first'].values())})
# Two exact repeats of the previously signed positive GRAPH cycle are not physical.
repeats={}
for ids in[(0,2,4,0,2,4),(3,0,2,4,0,2,4)]:
 z=lit.trace(''.join(p.words[i]for i in ids)+lit.M);assert not z['feasible'];repeats[str(ids)]=z
out={'status':'AUTHOR_FIXED_EXISTING_CORPUS_CONTACT_CONTROLS_AND_LEFT_ISOLATION_PENDING_INDEPENDENT_REPLAY',
     'scope':'Only13516 EXISTING six-return histories. No new prefix enumeration. All graph paths are label+endmarker-compatible ONLY, not realization of incoming214 history classes. All four controls are factor-entry or after factor-first plainD; no U-entry counterexample.',
     'source_history_sha256':hashlib.sha256((W/'shifted1_llrlrrrrlll_history6_scc2_port_quotient.json').read_bytes()).hexdigest(),
     'corpus_counts':{'six_return_edges':13516,'parsed_sections':19653,'contact_sections':8,'distinct_contact_words':4,'U_entry_contacts':0,'foreign_piece_first_contact_endpoints':0},
     'controls':controls,'fixed_predecessor_queries':queries,'query_count':56,'illegal_graph_cycle_repeats':repeats,
     'no_hit_scope':'No U-entry or foreign-endpoint first contact in this fixed corpus is not a proof of global proxy simplicity.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print([(c['labels'],c['seed_mass_raw_plus_marker12'],c['first_contact']['intersection'])for c in controls]);print('all56left queries pass')

from pathlib import Path
from fractions import Fraction as F
import json,hashlib,ast
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'word_stabilization/existing_proxy_contacts_frozen_20261023_2140';old=R/'audits/check_foreign_kinked_barrier_turn_independent.py';ns={'__file__':str(old)};exec(old.read_text().split('geometries=[]')[0],ns);W,M,walk,center,xy,meet=(ns[k]for k in('W','M','walk','center','xy','meet'));names='DCVUFQB';a=json.loads((D/'check_existing_proxy_contact_controls.json').read_text());G=json.loads((R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json').read_text());hist=json.loads((R/'word_stabilization/shifted1_llrlrrrrlll_history6_scc2_port_quotient.json').read_text());returns=sorted([s.split()for s in(R/'word_stabilization/shifted1_llrlrrrrlll.returns.tsv').read_text().splitlines()],key=lambda x:(len(x[2]),x[2],x[0],x[1]));dirs=(1j,1,-1j,-1)
def trace(w):
 p=0j;h=0;last={};first={};reads=[]
 for i,ch in enumerate(w):
  if p in last and last[p][1]==ch:return {'feasible':False,'conflict_read':i,'previous_read':last[p][0],'cell':list(xy(p)),'turn':ch}
  first.setdefault(p,ch);last[p]=(i,ch);reads.append((p,h,ch));h=(h+(1 if ch=='R'else-1))%4;p+=dirs[h]
 return {'feasible':True,'seed':{q for q,ch in first.items()if ch=='L'},'p':p,'h':h,'reads':reads}
controls=[];querycount=0
for r,qq in zip(a['controls'],a['fixed_predecessor_queries']):
 labels=r['labels'];raw=''.join(W[names[i]]for i in labels);marker=r['source_actual_marker12'];assert len(marker)==12 and marker[:11]==M
 u,edge,v=hist['history_edges'][r['source_history_edge']];ids=hist['history_states'][u]+[hist['source_return_ids'][edge]];assert ids==r['sorted_original_return_ids'];assert raw==''.join(returns[i][2]for i in ids);assert marker==returns[ids[-1]][1]
 tr=trace(raw+marker);assert tr['feasible'];seed=tr['seed'];assert sorted(map(list,map(xy,seed)))==r['seed'];black=set(seed);p=0j;h=0
 for i,ch in enumerate(raw+marker):
  if i==len(raw):assert len(black)==r['raw_exit_mass']and[*xy(p),h]==r['actual_raw_endpoint']
  assert(p in black)==(ch=='L');black.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;p+=dirs[h]
 # Integrate literal blocks, splitting Q/B only at actual fine cut56.
 p=0j;h=0;parts=[]
 for bi,lab in enumerate(labels):
  name=names[lab];subs=[W[name]]if lab<5 else[W[name][:56],W[name][56:]]
  for pi,sub in enumerate(subs):
   start=center(p,h);t=walk(sub);p+=t['p']*(-1j)**h;h=(h+t['h'])%4;parts.append(dict(a=list(xy(start)),b=list(xy(center(p,h))),label=lab,block=bi,piece=pi))
 assert parts==r['proxy_pieces_doubled'];hits=[]
 for j,b in enumerate(parts):
  for i,aa in enumerate(parts[:j]):
   hit=meet(tuple(aa['a']),tuple(aa['b']),tuple(b['a']),tuple(b['b']))
   if hit is None:continue
   if j==i+1:
    if len(hit)==3 and isinstance(hit[0],F)and hit[0]==1 and hit[1]==0:continue
    if hit==(tuple(aa['b']),):continue
   assert len(hit)==3 and isinstance(hit[0],F);hits.append((j,hit[1],i,hit))
 j,t,i,hit=min(hits);ref=r['first_contact'];assert(i,j)==(ref['earlier_piece'],ref['later_piece']);assert tuple(map(F,ref['intersection']['point']))==hit[2];assert(F(ref['intersection']['s']),F(ref['intersection']['t']))==hit[:2]
 assert parts[i]['label']<4 and parts[j]['label']<4
 path=[G['quotient_edges'][ei]for ei in r['graph_path_LABEL_AND_ENDMARKER_COMPATIBILITY_ONLY']];assert[a for u,a,v in path]==labels;assert all(v==nxt[0]for(_,_,v),nxt in zip(path,path[1:]));assert any(u==path[-1][2]and((lab==0)==(marker[11]=='L'))for u,lab,v in G['quotient_edges'])
 for key,prefix in[('predecessor_cases_M11',''),('predecessors_of_D_extended_M11',W['D'])]:
  for ai,ref in enumerate(qq[key]):
   got=trace(W[names[ai]]+prefix+raw+M);querycount+=1
   if got['feasible']:assert ref=={'feasible':True,'first_L_count':len(got['seed'])};assert key=='predecessor_cases_M11'and ai==0
   else:assert got==ref
 ext=trace(W['D']+raw+marker);assert ext['feasible']and len(ext['seed'])==r['D_extended_seed_mass_marker12']
 controls.append({'labels':''.join(names[i]for i in labels),'seed_mass':len(seed),'first_contact':[i,j,str(hit[0]),str(hit[1])], 'raw_length':len(raw)})
assert querycount==56
for ids,ref in a['illegal_graph_cycle_repeats'].items():assert trace(''.join(W[names[i]]for i in ast.literal_eval(ids))+M)==ref
manifest=D/'manifest.json';assert hashlib.sha256(manifest.read_bytes()).hexdigest()=='174b361b6b2adaa80dca554e82755c6969c12b2879e60e977dc3e236b5b59fb4'
out={'status':'PASS four actual foreign-intermediate proxy contact controls and56 exact predecessor exclusions','manifest_sha256':hashlib.sha256(manifest.read_bytes()).hexdigest(),'controls':controls,'queries':56,'analytic':'Every occurrence of one fixed word in an actual seven-word factor is at factor entry or after factor-first D: all other immediate predecessors fail, and every predecessor before D also fails. Thus these four words do not give U-entry proxy contact counterexamples. The two positive graph-cycle label repeats are physically impossible at154/157.','scope':'Independently checked four literal controls, source corpus IDs, label/endmarker graph paths and56 finite exclusions. The full13516-history absence scan was not rerun; its no-hit remains bounded author evidence, not a global theorem. No incoming214-class realization or seven-word simplicity is inferred.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(controls)

from pathlib import Path
from collections import Counter
import hashlib,json
S=Path(__file__);R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'OPPOSITE_PREHISTORY_OBSTRUCTION_MANIFEST.json';assert sha(MF)=='a692203bd8f13e5f49da7de28953895c0f220de793eea7e2338ffeea73abaea8'
for f,h in json.loads(MF.read_text())['files'].items():assert sha(D/f)==h
J=json.loads((D/'OPPOSITE_PREHISTORY_OBSTRUCTION_CHECKED.json').read_text());FJ=json.loads((D/'OPPOSITE_TRANSVERSE_FEEDBACK_CHECKED.json').read_text());assert sha(D/'OPPOSITE_TRANSVERSE_FEEDBACK_CHECKED.json')==J['source_hash']
ns={'__file__':str(S.with_name('check_transverse_contact_quotient_independent.py'))};exec(Path(ns['__file__']).read_text().split('assert {tuple(r[\'joins\'])')[0],ns);A,U,vec,xy,walk,line_hits=[ns[k]for k in('A','U','vec','xy','walk','line_hits')];results=[]
for row,src in zip(J['controls'],FJ['controls']):
 assert row['residue']==src['residue'];board={complex(*r['cell']):r['lifetime']for r in src['first_contact_full']};gens=[(complex(*a),complex(*v),b)for a,v,b in src['pure_generators']];finite={complex(*p)for p in src['pure_finite']};q=complex(*src['first_contact']['cell']);w,H=src['pure_transient'],src['pure_word'];p,h,reads=walk(q,0,w);end,hh,tail=walk(p,h,H);dr=end-p
 def ideal(q):
  bit=q in finite
  for a,v,bound in gens:
   delta=q-a
   if int(delta.real)%int(v.real):continue
   j=int(delta.real)//int(v.real)
   if delta==j*v and(bound is None or j<=bound):bit=not bit
  return bit
 diff={q for q in reads if ideal(q)!=(q in board)};segments=0
 for base in tail:
  flips=Counter({0:0})
  for a,v,b in gens:
   iv=line_hits(base,dr,a,v,b)
   if iv is not None:
    lo,hi=iv;flips[lo]+=1
    if hi is not None:flips[hi+1]+=1
  for q0 in finite^set(board):
   delta=q0-base
   if int(delta.real)%int(dr.real):continue
   k=int(delta.real)//int(dr.real)
   if k>=0 and delta==k*dr:flips[k]+=1;flips[k+1]+=1
  keys=sorted(flips);par=0
  for i,k in enumerate(keys):
   par^=flips[k]%2
   if par:
    assert i+1<len(keys);segments+=1
    for n in range(k,keys[i+1]):
     point=base+n*dr;assert ideal(point)!=(point in board);diff.add(point)
 plus={p for p in diff if p not in board};minus=diff-plus;assert sorted(map(xy,plus))==row['plus']and sorted(map(xy,minus))==row['minus'];assert all(board[p]>=0 for p in minus)
 # Independent original full precontact replay records the exact fixed last colors.
 B={complex(*q)for q in src['initial_black']};p=0j;h=1;pre_reads={};preword='';last={}
 for t in range(src['first_contact']['time']):
  c='L'if p in B else'R';preword+=c;pre_reads.setdefault(p,[]).append((t,c));last[p]=c;B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=vec[h]
 assert B==set(board)and(p,h)==(complex(*src['first_contact']['cell']),0);visited=set(pre_reads);assert sorted(map(xy,plus&visited))==row['plus_already_read']and sorted(map(xy,minus&visited))==row['minus_already_read'];first={}
 for t,q in enumerate(reads):first.setdefault(q,t)
 for q in diff:
  for i,base in enumerate(tail):
   delta=q-base
   if int(delta.real)%int(dr.real):continue
   k=int(delta.real)//int(dr.real)
   if k>=0 and delta==k*dr:first[q]=min(first.get(q,10**50),len(w)+104*k+i)
 hard=diff&visited;least=min(hard,key=lambda q:first[q]);expected=dict(cell=xy(least),offset=first[least],global_ideal_time=src['first_contact']['time']+first[least],actual_cut_black=least in board,ideal_cut_black=ideal(least),current_lifetime=board.get(least));assert expected==row['first_hard_difference'];assert(last[least]=='R')==(least in board)
 if row['residue']==[1,1]:
  assert pre_reads[159+52j]==[(47131,'R'),(47135,'L')];assert 159+51j not in visited;B={complex(*q)for q in src['initial_black']}|{159+51j};p=0j;h=1;firstadd=None;failure=None
  for t,c in enumerate(preword+w):
   if p==159+51j and firstadd is None:firstadd=t
   actual='L'if p in B else'R'
   if actual!=c:failure=dict(time=t,cell=xy(p),actual=actual,wanted=c);break
   B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=vec[h]
  assert firstadd==82998 and failure==J['single_unread_addition']['first_failure'];assert failure==dict(time=82999,cell=[159,52],actual='R',wanted='L')
 results.append(dict(residue=row['residue'],additions=len(plus),clears=len(minus),fixed_additions=len(plus&visited),fixed_clears=len(minus&visited),earliest_hard_read=expected,odd_finite_ray_intervals=segments))
out=dict(status='PASS fixed prehistory versus fixed pure future incompatibility',manifest=sha(MF),script=sha(S),controls=results,analytic_scope=['With fixed initial pose, the whole turn prefix fixes every visited physical cell initial color and its cut color. A desired future word fixes its path and first postcut read at each cell. Any mismatch at a prefix-visited first-future-read cell is immutable under ALL initial edits preserving that prefix, not merely single-bit edits.','All four complete prefix traces were independently replayed. The exact desired infinite footprint is transient positions plus104 half-rays; independent line intersections and parity endpoint sweeps enumerate every finite odd difference interval and prove the final unbounded interval even. Counts0/34,152/47,0/30,0/30 and prefix-fixed subsets agree.','The earliest hard witnesses are actual finite desired first reads at offsets29280/33280/5812/5840. In the missing-input branch, adding virgin159,51 genuinely repairs82998, then fails82999 on159,52, whose historical R47131/L47135 fixes WHITE. All unread edits leave that historical color unchanged.','These inventories are counterfactual input bit corrections on the desired read footprint, not actual ant clearing actions, permanent-output debits or a global resource. Alternative preparation, inserted excursions, altered phases and different futures remain unrestricted.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))

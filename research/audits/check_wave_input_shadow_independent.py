from pathlib import Path
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'WAVE_INPUT_RECORD_SHADOW_MANIFEST.json'
assert sha(MF)=='029c300d106719586071096ff8b3b383d18390187cf573c1c71e357a144bf7b1'
for f,h in json.loads(MF.read_text())['files'].items():assert sha(D/f)==h
ref=json.loads((D/'WAVE_INPUT_RECORD_SHADOW_CHECKED.json').read_text())
for f,h in ref['source_hashes'].items():assert sha(D/f)==h
bind=json.loads((D/'COMPLETED_DROUGHT_COUNTS_AUDIT_BINDING.json').read_text());clar=(D/'COMPLETED_DROUGHT_INTEGER_THRESHOLD_CLARIFICATION.md').read_text();assert 'integer' in clar.lower()
ns={'__file__':str(S.with_name('check_completed_drought_counts_independent.py'))};exec(Path(ns['__file__']).read_text().split('controls=[];total=0')[0],ns)
geo,xy,dot,spec,models,future,phases,V=[ns[k]for k in['geo','xy','dot','spec','models','future','phases','V']]
U=R/'causal_reduction/unit_scale';A=json.loads((U/'prepared1564_uniform_support_manifest.json').read_text());B=json.loads((U/'prepared4352_capture_manifest.json').read_text());data=[]
for name,z,i in [('1564',A['stages'][-1],1455),('4352',B['stages'][11],1687),('15324',B['stages'][13],4264)]:
 w=z['word'];h=z['heading'];qs,d,eh=geo(w,h);q=qs[i];assert eh==h and d and w[i]=='L'
 # Full Zd orbit, not primitive drift: exact determinant and divisibility.
 groups={};hits=[]
 for j,p in enumerate(qs):
  dx=int(d.real);r=int(p.real)%abs(dx);k=(int(p.real)-r)//dx;rep=(r,int(p.imag-k*d.imag));groups.setdefault(rep,[]).append((k,j))
  v=(p-q)/d
  if abs(v.imag)<1e-12 and v.real==int(v.real):hits.append([j,int(v.real),w[j]])
 assert all(k<=0 for j,k,c in hits)and min(j for j,k,c in hits if k==0)==i
 leading=[]
 for rep,rs in groups.items():
  k=max(a for a,j in rs);j=min(j for a,j in rs if a==k)
  if w[j]=='L':leading.append(j)
 positive={}
 for normal in range(4):
  delta=dot(d,normal)
  if delta>0:
   mx=max(dot(p,normal)for p in qs);diff=mx-dot(q,normal);C=-(-diff//delta);assert C==1
   positive[str(normal)]=dict(delta=delta,maximum=mx,input_projection=dot(q,normal),fringe=C,slack=delta-diff)
 rr=next(r for r in ref['word_proofs']if r['word']==name)
 assert rr['drift']==xy(d)and rr['all_same_drift_orbit_visits']==hits and rr['exact_positive_normal_inequalities']==positive and rr['leading_first_L_orbits']==len(leading)
 assert rr['word_sha256']==hashlib.sha256(w.encode()).hexdigest();data.append(dict(word=name,period=len(w),heading=h,drift=xy(d),selected_phase=i,selected_cell=xy(q),all_selected_orbit_reads=hits,leading_L_classes=len(leading),positive_bounds=positive))
# Full original-field controls, actual identity labels and entry hashes.
controls=[];total=0
for rr in ref['literal_controls']:
 name=rr['family'];n=rr['parameter'];seed,p,h,st=spec(models[name],n);assert sorted(map(xy,seed))==rr['initial_black']
 B={q:-i-1 for i,q in enumerate(sorted(seed,key=lambda p:(p.real,p.imag)))};birth={};t=0;rows=[]
 for stage,w,N in st:
  if N is None:tail=w;break
  target=next((z for z in rr['targets']if z['stage']==stage),None)
  if target:
   proof=data[0]if name=='184'else data[1]if stage=='11:wave'else data[2];q=complex(*proof['selected_cell']);d=complex(*proof['drift']);cell=p+q+(N-1)*d;owner=B[cell];due=t+(N-1)*len(w)+proof['selected_phase'];assert owner<0 or owner<t
   rec=dict(stage=stage,copies=N,block_start=t,block_pose=[xy(p),h],input_cell=xy(cell),input_owner=owner,first_block_read=due,full_entry_black_mass=len(B),full_entry_sha256=hashlib.sha256(json.dumps(sorted(map(tuple,map(xy,B))),separators=(',',':')).encode()).hexdigest(),prior_R_birth=None if owner<0 else xy(birth[owner]));assert rec==target;pending=True
  for _ in range(N):
   for c in w:
    if target and p==cell and pending:assert t==due and B[p]==owner and c=='L';pending=False
    old=B.pop(p,None);assert (old is None)==(c=='R'),(name,n,t,p)
    if old is None:B[p]=t;birth[t]=p
    h=(h+(1 if c=='R'else-1))%4;p+=V[h];t+=1
  if target:assert not pending;rows.append(rec)
 assert t==rr['physical_reads']and [xy(p),h]==rr['terminal_pose']and sorted(map(xy,B))==rr['terminal_full_black']
 tw,dr,deaths,tests=future(B,p,h);assert tw==tail==rr['terminal_word']and tw in phases and xy(dr)==rr['terminal_drift'];total+=t;controls.append(dict(family=name,parameter=n,reads=t,selected_actual_old_lifetimes=rows,full_terminal_mass=len(B),infinite_parity_tests=tests));print(name,n,'PASS',t,flush=True)
assert total==2235520==ref['total_physical_reads']
out=dict(status='PASS exact old-input record-shadow lemma and three supplied-word specializations',manifest=sha(MF),word_proofs=data,controls=controls,total_full_literal_reads=total,analytic_review=[
'For X=q_i+(N-1)d, any occurrence q_j+kd=X has k=N-1-m, with m<=0. No k<N-1 is possible, and the earliest same-cell phase is L. Thus X is actual BLACK at block entry, not a recolored or hypothetical prepared input.',
'Every current BLACK cell in a finite-seed causal orbit belongs to original support or a previously read head position. Therefore X belongs to the augmented ENTIRE initial-support/head-history hull, independently of old archive or producer, not merely the current active hull.',
'For positive delta, k<=N-1-ceil((max projection-q_i projection)/delta) implies every read cut in copy k is at or behind X. Nonpositive delta copies are dominated by the same-phase copy-zero read. The statement uses half-open read cuts; the final endpoint is deliberately excluded.',
'The three entire-word exact Zd orbit inventories have fringe1 on both positive axes, so every actual legal N-copy occurrence has records only in its first/final copies. No supplied-source specificity enters this implication.',
'For INTEGER H>=0, each endpoint window spansP-1 and contains at mostfloor((P-1)/(H+1)) completed long gaps, plus at most one between windows. N1 uses one window. At most two global boundary-crossing gaps are separate and cannot be summed independently across empty/overlapping blocks.',
'The same selected orbit argument for each j=0..N-1 gives N distinct old-at-entry consumed lifetimes per stable first-L class. Counts197/406/1439 are old-cohort requirements, not original-seed fuel; fresh production and reuse between blocks are not excluded.',
'All2235520 full literal reads, selected actual prior owners, entire entry hashes, final fields and infinite canonical parity are independently reconstructed. General block generation counts, universal record-window occurrence and canonical attraction remain open.'
],source_hashes=ref['source_hashes'],integer_threshold_binding=sha(D/'COMPLETED_DROUGHT_COUNTS_AUDIT_BINDING.json'))
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))

from pathlib import Path
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'second_foreign_short_clock_transfer_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'control_next_ports_manifest.json';assert sha(MF)=='0d8a954048dd69b8a7191a43db3cad5b2594175558b634f290b15fb9876c92ab';mf=json.loads(MF.read_text())
for k,b in [('files',D),('dependencies',R)]:
 for f,h in mf[k].items():assert sha(b/f)==h
J=json.loads((D/'control_next_ports.json').read_text());ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy=[ns[k]for k in('W','M','K','tr','rot','xy')];spell=lambda w:''.join(W[a]for a in w);refs={(r['base_control'],r['actual_next_atom']):r for r in J['all21_prescribed_next_ports']};assert set(refs)=={(b,a)for b in('UQUF','UBVF','UBUF')for a in'DCVUFQB'}
positives=[];negatives=[]
for(base,a),r in refs.items():
 prefix=spell(base);word=prefix+W[a]+M;z=tr(word);assert bool(z['bad']) == (not r['feasible'])
 if z['bad']:
  assert not r['feasible'];t,s,q,c=z['bad'];assert s<28 and t>=len(prefix);assert tr(word[:t])['last'][q]==tr(W['U'])['last'][q]==(c,s);assert r['immutable_conflict']['previous_read']==s and r['immutable_conflict']['conflict_read']==t and r['immutable_conflict']['cell']==xy(q)
  assert r['actual_next_owner']['context_tick0']==t-len(prefix)and r['actual_next_owner']['turn']==c;old=r['original_U_source_last_read'];assert old['cell']==xy(q)and old['own_tick0']==s and old['turn']==c
  if base in('UQUF','UBVF'):assert(s,q,c,t-len(prefix))==((3,-1j,'L',11)if a=='D'else(4,0j,'R',12)if a in'CV'else(1,-1+0j,'L',13))
  negatives.append((base,a,t,s,xy(q)))
 else:
  assert r['feasible']and(base,a)==('UBUF','D');seed={q for q,b in z['req'].items()if b};zb=tr(prefix+M);base_seed={q for q,b in zb['req'].items()if b};assert seed-base_seed=={1-2j}and base_seed<=seed and 1-2j not in zb['req'];assert sorted(map(xy,seed))==r['complete_seed']and len(seed)==48
  B=set(seed);p=0j;h=0;first={}
  for t,c in enumerate(word):
   first.setdefault(p,t);assert(p in B)==(c=='L');B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=rot(h)*1j
  assert len(word)==207==r['all_physical_reads']and first[1-2j]==197;positives.append(dict(base=base,next=a,seed=48,reads=207,extra=[1,-2],first_extra_read=197))
assert len(negatives)==20 and len(positives)==1
out=dict(status='PASS exactly21 prescribed complete-next-seven ports, one literal48-cell extension',manifest=sha(MF),script=sha(S),negative_count=20,positive=positives,analytic_review=['Every actual nextRAW+itsOWN actualM11 is tested on the full prescribed factor. All20 failures retain the literal firstU lastread, same physical cell and no intervening visit, including marker-owned D input at context11. UQUF/UBVF each reject allseven exactly as stated.','The sole UBUFD positive is a new48-cell finite seed, adding1,-2 to the47-cell base. The added cell is genuinely unread throughout the entire base+suppliedM11 and firstreadL197. Full207 updates replay. This is not retroactive alteration or continuation attributed to the original47-cell board.','The base suppliedM11 can physically contain a D10 RAW without supplying the OWN full marker of thatD. Therefore no complete-next-seven claim means neither physical ant termination nor language coverage. Only21 named ports are classified, not a continuation tree or arbitrary twoforeign history.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))

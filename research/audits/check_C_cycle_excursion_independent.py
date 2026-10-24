from pathlib import Path
from collections import defaultdict,Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
P=D/'C_CYCLE_EXCURSIONS_AND_STANDARD_SELF_FEEDING.md';JF=D/'C_cycle_excursion_normal_form_certificate.json'
assert sha(P).startswith('a74e13f8') and sha(JF).startswith('f93bf1fe') and sha(D/'certify_C_cycle_excursion_normal_form.py').startswith('59973088')
J=json.loads(JF.read_text())
for f,h in J['dependencies'].items():assert sha(Path(f))==h
B=json.loads((D/'active_C_entry_exit_forests_certificate.json').read_text())['base_controls']
assert sha(S.with_name('check_active_C_entry_exit_independent.json')).startswith('317e4dce')
V=[1j,1,-1j,-1];off=[-1j,-1-1j,-1,0j];xy=lambda z:[int(z.real),int(z.imag)]
def geom(w,p=0j,h=0):
 es=[]
 for t,c in enumerate(w):
  es.append((p,h,c));h=(h+(1 if c=='R' else -1))%4;p+=V[h]
 return es,p,h

def decompose(w,h0=0):
 n=len(w);E,d,h=geom(w,h=h0);assert h==h0 and d
 ax=0 if d.real else 1;delta=int(d.real if ax==0 else d.imag)
 def rep(p):
  z=int(p.real if ax==0 else p.imag);k=(z//abs(delta))*(1 if delta>0 else -1);return p-k*d,k
 def ev(t):
  k,i=divmod(t,n);p,h,c=E[i];return p+k*d,h,c
 def face(t):
  p,h,c=ev(t);return p+off[h]
 H=defaultdict(list);F=defaultdict(list)
 for t,(p,h,c) in enumerate(E):
  q,k=rep(p);H[q].append((t-k*n,t,h,c))
  q,k=rep(p+off[h]);F[q].append(t-k*n)
 for a in (H,F):
  for ls in a.values():ls.sort()
 starts={q:ls[0] for q,ls in F.items()};G={}
 for q,A in starts.items():
  t=A-1;p,h,c=ev(t);assert c=='L' and face(A)==q
  u,k=rep(face(t));rq,lift=rep(p);rs=H[rq];j=next(j for j,r in enumerate(rs) if r[0]==t-lift*n)
  if rs[0][3]=='L':continue
  assert j==1 and rs[0][2]==h
  r=rs[0][0]+lift*n;assert ev(r)==(p,h,'R') and starts[u]+k*n<=r<t
  G[q]=(u,k,r,t)
 # Restrict to intact WHITE-parent cycles only; partial white trees may end at BLACK roots.
 seen=set();cycles=[]
 for q in G:
  path=[];where={};u=q
  while u in G and u not in seen and u not in where:
   where[u]=len(path);path.append(u);u=G[u][0]
  if u in where:cycles.append(path[where[u]:])
  seen.update(path)
 out=[]
 for cy in cycles:
  assert sum(G[q][1] for q in cy)==-1
  raw=[(G[q][2]%n,G[q][3]-G[q][2],G[q][3]%n) for q in cy]
  cut=min(r for r,_,_ in raw);raw.sort(key=lambda row:(row[0]-cut)%n);parts=[]
  for i,(r,age,l) in enumerate(raw):
   a=(r-cut)%n;b=a+age;c=(raw[(i+1)%len(raw)][0]-cut)%n+(n if i==len(raw)-1 else 0)
   assert 0<=a<b<c<=n
   ew=''.join(w[(cut+t)%n] for t in range(a,b));kw=''.join(w[(cut+t)%n] for t in range(b,c))
   ee,end,hh=geom(ew);assert end==0j and hh==0 and len(ew)%4==0 and ew[0]=='R' and kw[0]=='L'
   assert all(p!=0j for p,h,c in ee[1:])
   assert (ew.count('R')-ew.count('L'))%4==0
   parts.append(dict(R_owner_phase=r,L_phase=l,start=a,end=b,excursion_word=ew,connector_word=kw,excursion_growth=ew.count('R')-ew.count('L'),connector_growth=kw.count('R')-kw.count('L')))
  assert ''.join(z['excursion_word']+z['connector_word'] for z in parts)==w[cut:]+w[:cut]
  skeleton=''.join(z['connector_word'] for z in parts)
  _,sd,sh=geom(skeleton,h=E[cut][1]);assert sd==d and sh==E[cut][1]
  out.append(dict(period_cut_phase=cut,parts=parts,geometric_skeleton=skeleton,skeleton_is_not_claimed_legal=True))
 return sorted(out,key=lambda z:z['period_cut_phase'])
summary={}
for name,z in B.items():
 dec=decompose(z['word'],z['initial_heading']);assert dec==sorted(J['base_decompositions'][name],key=lambda z:z['period_cut_phase']);summary[name]=[[len(p['excursion_word']) for p in q['parts']] for q in dec]
for row in J['representation_controls']:
 dec=decompose(B[row['name']]['word']*row['power'],row['heading']);assert row['cycle_count']==len(dec) and sorted(row['excursion_counts'])==sorted(len(z['parts']) for z in dec)
assert len(J['representation_controls'])==60
# Fresh complete blank simulation; every owner is a physical time, no periodic-class shortcut.
W=B['S104']['word'];z=J['full_blank_realization'];cuts={9977,10334,10344,10438};field={};p=0j;h=0;E=[];snap={}
for t in range(10439):
 if t in cuts:snap[t]=(dict(field),p,h)
 if t==10438:break
 owner=field.pop(p,None);c='R' if owner is None else 'L';row=dict(time=t,position=xy(p),incoming_heading=h,turn=c)
 if owner is None:field[p]=t
 else:row['actual_R_owner']=owner
 E.append(row);h=(h+(1 if c=='R' else -1))%4;p+=V[h]
assert E[10334:10438]==z['all104_events']
for s in z['states']:
 b,p,h=snap[s['time']];assert sorted(map(xy,b))==s['full_black_field'] and xy(p)==s['head'] and h==s['heading']
assert [len(snap[t][0]) for t in sorted(cuts)]==[715,758,758,770]
ns={'__file__':str(S.with_name('check_phase13_double_scatter_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Canonical source')[0],ns)
future=ns['future'];checks={}
for t,w in [(9977,W),(10334,W[45:]+W[:45])]:
 b,p,h=snap[t];fw,d,dead,tests=future(b,p,h);assert fw==w and d==-2-2j;checks[t]=tests
owned=[];matrix=Counter()
for e in E[10334:10438]:
 if e['turn']=='R':continue
 rt=e['actual_R_owner'];rrel=rt-10334;rel=e['time']-10334;source='A10' if rrel%104<10 else 'B94';target='A10' if rel<10 else 'B94';matrix[source,target]+=1
 owned.append(dict(R_time=rt,L_time=e['time'],R_relative_to_cut=rrel,L_relative_to_cut=rel,source_block=source,target_block=target,owner_period=rrel//104,cell=e['position'],age=e['time']-rt))
assert owned==z['all46_actual_owned_lifetimes'] and len(owned)==46
assert matrix=={('A10','A10'):3,('B94','A10'):2,('A10','B94'):2,('B94','B94'):39}
assert all(o['owner_period']==-1 for o in owned if o['source_block']=='B94' and o['target_block']=='A10')
for q in z['key_recycling_pairs']:
 r,l=q['R_time'],q['L_time'];assert E[r]['turn']=='R' and E[l]['actual_R_owner']==r and E[r]['position']==E[l]['position']==q['cell'];assert r-10289==q['R_relative_to_frame'] and l-10289==q['L_relative_to_frame']
A=''.join(e['turn'] for e in E[10334:10344]);assert A=='RRRRLLLLRL'==J['standard_module_words']['A10']
assert ''.join(e['turn'] for e in E[10344:10438])==J['standard_module_words']['B94']
read={complex(*e['position']) for e in E[10334:10344]};before=snap[10334][0];after=snap[10344][0];unread=set(before)-read
assert len(unread)==756 and sorted(map(xy,unread))==z['M10_complete_untouched_field']
assert all(before[q]==after[q] for q in unread)
assert sorted(map(xy,set(before)&read))==z['M10_full_input'] and sorted(map(xy,set(after)&read))==z['M10_full_local_output']
assert len(set(before)&read)==len(set(after)&read)==2
# All 46 normalized same-cell owners and twelve final-R outputs from complete histories.
outs=[]
for row in B['S104']['read_histories']:
 rs=row['reads'];assert rs[0]['c']=='R'
 for i,e in enumerate(rs):
  if e['c']=='L':
   owner=rs[i-1];age=e['canonical_time']-owner['canonical_time'];t=10289+e['t'];t+=104*((10334-t+103)//104)
   assert 10334<=t<10438 and E[t]['actual_R_owner']==t-age
 if rs[-1]['c']=='R':outs.append(rs[-1]['t'])
assert sorted(outs)==z['permanent_output_phases_all_in_B94'] and len(outs)==12 and all((t-45)%104>=10 for t in outs)
O=dict(status='PASS actual C-cycle excursion normal form and complete standard self-feeding only',proof=sha(P),certificate=sha(JF),script=sha(S),base_excursion_lengths=summary,representation_controls=60,full_blank_reads=10438,full_field_masses=[715,758,758,770],full_future_parity_checks=checks,owned_lifetimes=46,untouched_A10_black_cells=756,analytic_review=[
'The signed physical first-entry scaffold is retained with all of its actual translating-front hypotheses and full-drift quotient. For each selected WHITE edge, the R0 event is at its parent active face and precedes the L1 discovery of its child. Hence [R0,L1) lies inside the actual interval from first parent activation to first child activation. Reverse-parent traversal and full winding -1 concatenate those activation intervals over exactly P. This is a physical event partition, not a relaxed clock or repaired-path argument.',
'SAME physical position and incoming heading at R0 and L1 give a nonempty closed-pose excursion, no intermediate root read, and root BLACK on return. Alternating horizontal/vertical steps and zero displacement give length divisible by four; restored heading gives BLACK growth divisible by four, not positive. The connector includes the actual L1 update and is nonempty even with zero idle before the next R0. Full period erasure preserves only geometry, never fields, owners, or ant legality.',
'Fresh complete-word reconstruction verifies every selected cycle and interval in five supplied controls and sixty rotation/power controls. Standard has 12/88 and 8/92 decompositions, including a neutral eight-read excursion and four retained connector updates.',
'Independent literal blank simulation through10438 retains all715/758/758/770 field cells, all104 updates, all46 actual R owners, all756 untouched A10 cells, and complete infinite parity at9977 and10334. The two A10 external inputs are genuine previous-B94 lifetimes, and its two local outputs are actually consumed in B94. Every twelve full-period permanent output roots lies in B94.',
'The decomposition and standard self-feeding are not a new controller, independent-module composition law, root-budget theorem, WHITE lifetime S=1 proof, excursion-length/stock bound, or global entry result. Isolated prepared10 winding cannot be assigned to the inserted module because physical lifetime ownership changes.'
])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(summary);print(sha(S.with_suffix('.json')))

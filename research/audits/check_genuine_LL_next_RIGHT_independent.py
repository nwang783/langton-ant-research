from pathlib import Path
from itertools import product
from collections import Counter
import ast,json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
P=D/'genuine_LL_resets_fail_at_the_next_forced_boundary_RIGHT.md';A=D/'check_genuine_LL_next_RIGHT_rank_collision.json';C=D/'check_genuine_LL_next_RIGHT_rank_collision.py'
assert sha(P).startswith('43aa3be2') and sha(C).startswith('947a5bfd') and sha(A).startswith('95f93bc6')
ref=json.loads(A.read_text());base=json.loads(S.with_name('check_cyclic_LL_reactivation_independent.json').read_text());assert base['status'].startswith('PASS')
H='NESW';V=(1j,1,-1j,-1);cv=lambda w:tuple(H.index(a)for a in w);st=lambda w:''.join(H[a]for a in w);out=lambda w,r:(w[r]+(1 if r%2==0 else-1))%4
words=lambda ax:[w for n in range(5)for w in product(ax,repeat=n)]
NS=words((0,2));EW=words((1,3));ins=lambda w,d:[i for i,a in enumerate(w)if a==d];outs=lambda w,d:[i for i in range(len(w))if out(w,i)==d]
Jdom=[w for w in NS if w and w[0]==2 and len(ins(w,2))==2 and len(outs(w,3))>=2]
assert set(map(st,Jdom))=={'SSNN','SNNS','SNS','SNSN'}
xy=lambda p:[int(p.real),int(p.imag)]
def successor(hs):
 su={}
 for p,w in hs.items():
  for d,v in enumerate(V):
   q=p+v
   if q not in hs:continue
   a=outs(w,d);b=ins(hs[q],d)
   if len(a)!=len(b):return None
   su.update({(p,i):(q,j)for i,j in zip(a,b)})
 return su
def wrongpaths(hs,su):
 ans=[]
 for p,w in hs.items():
  for r in range(len(w)):
   cur=(p,r);seen={cur};path=[cur]
   while cur in su:
    cur=su[cur];path.append(cur)
    if cur[0]==p:
     if cur[1]!=r+1:ans.append(path)
     break
    if cur in seen:break
    seen.add(cur)
 return ans
count=Counter();lens=Counter();rows=[];observed=set();author=set()
for no,src in enumerate(base['necessary_inventories']):
 fixed={complex(*ast.literal_eval(p)):cv(w)for p,w in src['histories'].items()}|{1-1j:cv('SNNS'),-1j:cv('EEWW')}
 for cc in ('WEE','WEEW'):
  fixed[2-1j]=cv(cc)
  for j,e,f in product(Jdom,EW,NS):
   hs=fixed|{-2j:j,1-2j:e,2-2j:f};su=successor(hs)
   if su is None:continue
   paths=wrongpaths(hs,su);assert paths
   best=min(paths,key=lambda z:(len(z),[(p.real,p.imag,r)for p,r in z]));count[st(j)]+=1;lens[len(best)-1]+=1
   key=(no,cc,st(j),st(e),st(f));assert key not in observed;observed.add(key)
   rows.append(dict(source_inventory=no,C=cc,J=st(j),E=st(e),F=st(f),path=[[xy(p),r]for p,r in best]))
   # Verify the submitted path exactly as an ACTUAL physical first return.
   candidates=[z for z in ref['rows']if z['root']==src['root']and z['reaction']==src['kind']and z['C']==cc]
   matches=[]
   for ar in candidates:
    for v in ar['rank_collision_certificates']:
     if(v['J'],v['E'],v['F'])!=(st(j),st(e),st(f)):continue
     path=[(complex(*p),r)for p,r in v['literal_wrong_rank_path']]
     if all(a in su and su[a]==b for a,b in zip(path,path[1:])):
      assert path[0][0]==path[-1][0] and path[-1][1]!=path[0][1]+1
      assert all(p!=path[0][0]for p,r in path[1:-1]);matches.append(path)
   assert matches
assert count=={'SSNN':240,'SNNS':240,'SNS':24,'SNSN':24} and sum(count.values())==528
# No extra certificate records escape the independently generated complete product.
assert sum(len(r['rank_collision_certificates'])for r in ref['rows'])==528
# Every submitted path is realized in a unique source inventory, up to identical N-prefix tags.
for ri,ar in enumerate(ref['rows']):
 for ai,v in enumerate(ar['rank_collision_certificates']):
  path=[(complex(*p),r)for p,r in v['literal_wrong_rank_path']];found=[]
  for no,src in enumerate(base['necessary_inventories']):
   if src['root']!=ar['root']or src['kind']!=ar['reaction']:continue
   hs={complex(*ast.literal_eval(p)):cv(w)for p,w in src['histories'].items()}|{1-1j:cv('SNNS'),-1j:cv('EEWW'),2-1j:cv(ar['C']),-2j:cv(v['J']),1-2j:cv(v['E']),2-2j:cv(v['F'])}
   su=successor(hs)
   if su is not None and all(su.get(a)==b for a,b in zip(path,path[1:])):found.append(no)
  assert found
  author.add((ri,ai))
assert len(author)==528 and lens[4]==450
reports=['check_cyclic_LL_reactivation_independent.json','check_genuine_LL_nested_reader_independent.json','check_LL_post_X_RR_cap_independent.json','check_mixed_RR_closure_independent.json','check_mixed_LL_gate_independent.json','check_passive_LL_flat_cap_independent.json']
deps={}
for name in reports:
 p=S.with_name(name);assert json.loads(p.read_text())['status'].startswith('PASS');deps[name]=sha(p)
O=dict(status='PASS no genuine LL-first O/U root in the stated critical GLOBAL-M no-one-use complete-WHITE cap-four scope',proof=sha(P),author_certificate=sha(A),author_checker=sha(C),script=sha(S),signed_dependencies=deps,derived_J_domain=list(map(st,Jdom)),independent_product_counts=dict(count),shortest_witness_lengths=dict(lens),all528_paths=rows,analytic_review=[
'The signed six physical stock inventories and XY cap are necessary under the full stated main scope, independently regenerated in their signed audit. Both C=WEE/WEEW retained, with no imported corner-map iteration or completed local-control premise.',
'General mixed RR closure applied to the ACTUAL preceding LEFT, X, B and following LEFT forces A=(0,-1) EEWW because no one-use edges remain. This is a required Gamma contact, not a freely chosen exterior helper.',
'If J after A is LEFT, the critical last-LEFT gate makes it passive V. Its preceding RIGHT is the flat Y B, so the full mixed LL classification rules out a high opposite flank; this is genuinely flat-ended. The qualified passive-LL cap then demands preceding YY, contradicting the actual preceding X,B=XY. No unqualified all-passive-LL theorem is imported.',
'A has exactly two south departures, so J has exactly two S arrivals. RIGHT gives first S/R, output W with no one-use edge. Enumerating all empty/WHITE1..4 NS words under only these facts gives SSNN,SNNS,SNS,SNSN; the source4 is retained. All31 possible EW E and31 NS F words including empty are independently brute-forced, with every zero and nonzero adjacent port count.',
'All528 complete count-compatible patches have physical contiguous wrong-next-rank returns. Every author path independently checked event by event; independent shortest paths have450 length4 witnesses. There are no height, clock, phase, period or exterior filters in this rejection. A full-drift alias cannot insert a missing physical visit inside a contiguous known path; alias constraints elsewhere can only narrow this overapproximation.',
'Only genuine LL-first O/U is excluded. Flat-ended passiveVV and high-high passiveVV remain; singletonO roots, external old stock and unrestricted WHITE/controller/global-capture questions remain. Earlier weaker local networks and finite prepared controls stay valid, but their full-front continuation with this genuine Gamma source is impossible.'
]);S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(dict(count),dict(lens));print(sha(S.with_suffix('.json')))

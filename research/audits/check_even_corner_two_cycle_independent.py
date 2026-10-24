from pathlib import Path
import ast,json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'even_corner_reader_map_has_a_rank_shift_two_cycle.md';JF=D/'check_even_corner_reader_two_cycle.json'
assert sha(P).startswith('0670c785') and sha(JF).startswith('0c0cfc03') and sha(D/'check_even_corner_reader_two_cycle.py').startswith('9a4642fe')
J=json.loads(JF.read_text());ns={'__file__':str(S.with_name('check_global_max_flow2_staircase_independent.py'))};exec(Path(ns['__file__']).read_text().split('rows=[];stats=Counter()')[0],ns);cv,V,out,test=[ns[k]for k in ('cv','V','out','test')]
hs={complex(*ast.literal_eval(p)):cv(h)for p,h in J['histories'].items()};assert len(hs)==14 and all(len(w)==4 for w in hs.values()) and test(hs)[0]=='open';times={(complex(*ast.literal_eval(e)[0]),ast.literal_eval(e)[1]):t for e,t in J['injective_mod4_calendar'].items()};assert len(times)==len(set(times.values()))==56
su={};pre={}
for p,w in hs.items():
 for h,v in enumerate(V):
  if p+v not in hs:continue
  a=[i for i in range(4)if out(w,i)==h];b=[i for i,k in enumerate(hs[p+v])if k==h];assert len(a)==len(b)
  for i,j in zip(a,b):assert(p,i)not in su and(p+v,j)not in pre;su[p,i]=(p+v,j);pre[p+v,j]=(p,i)
 for i in range(4):
  x,y=int(p.real),int(p.imag);phase=2*(x%2)if(x+y)%2==0 else 3-2*(x%2)
  assert times[p,i]%4==phase
  if i:assert times[p,i]-times[p,i-1]>=4
for e,f in su.items():assert times[f]==times[e]+1
seen=set();cs=[]
for e in sorted(set(times)-set(pre),key=lambda e:(e[0].real,e[0].imag,e[1])):
 c=[];u=e
 while True:
  assert u not in seen;seen.add(u);c.append(u)
  if u not in su:break
  u=su[u]
 cs.append(c)
assert seen==set(times)
enc=lambda e:[[int(e[0].real),int(e[0].imag)],e[1]]
assert [[enc(e)for e in c]for c in cs]==J['components'];order=J['whole_component_order'];assert sorted(order)==list(range(len(cs))) and all(times[cs[a][-1]]<times[cs[b][0]]for a,b in zip(order,order[1:]))
C=2-1j;H=3-2j;G=3-1j;F=2-2j;corner=lambda p:p-V[hs[p][3]]+V[out(hs[p],2)]
assert corner(C)==H and corner(H)==C
path=[(H,2),(G,1),(C,3),(F,3),(H,3)];assert [enc(e)for e in path]==J['actual_path'] and all(su[a]==b for a,b in zip(path,path[1:]));assert times[H,3]-times[H,2]==4 and hs[H][2]==3 and hs[H][3]==1
assert ''.join('R'if i%2==0 else'L'for p,i in path[:-1])=='RLLL'
O=dict(status='PASS necessary local geometric corner two-cycle with actual forward rank shift only',proof=sha(P),certificate=sha(JF),script=sha(S),cells=14,events=56,components=len(cs),internal_edges=len(su),analytic_review=['K(p)=p-vector(incomingL3)+vector(outgoingR2) is only a displayed geometric corner-interface map. With C=WEEW and H=EWWE its two-cycle C,H,C is exact. It is not chronological succession, first-R b, a birth tree or a repeated complete role.','The actual physical path H.R2,G.L1,C.L3,F.L3,H.L3 has four updates RLLL. It advances to the NEXT H rank and changes incoming headingW toE. There is no actual event cycle, full-pose loop or newly restarted C.R0. All earlier/future ranks remain in the complete inventory.','All complete14 histories, zero ports, physical ordinals, local height/clock constraints and56 distinct mod4 times independently reconstruct. The actual known-successor components partition events and occupy disjoint whole time intervals, with all same-cell gaps>=4.','The missing physical paths between components and full-period voltage closure remain unsupplied. This necessary local all-even countercheck blocks only a geometric-map/same-role induction shortcut; it is not an attained prepared factor, front, autonomous renewal, odd-output counterexample or global exclusion.'] )
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))

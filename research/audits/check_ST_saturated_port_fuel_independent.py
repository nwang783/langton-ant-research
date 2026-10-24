from pathlib import Path
from itertools import product
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];D=ROOT/'reframe_finite_seed_2026-10-24';G=ROOT/'kernel_cycle_lift_2026-10-24'
p=SELF.with_name('check_cycle_birth_finite_fuel_independent.py');ns={'__file__':str(p)};exec(p.read_text().split('cells=')[0],ns)
ends,component,step,wvertex=[ns[k]for k in('ends','component','step','wvertex')]
xy=lambda z:(int(z.real),int(z.imag))
ser=lambda B:sorted(map(xy,B))
def comps(B):
 left=set(B);out=[]
 while left:
  q=next(iter(left));C=component(B,0,ends(q,0)[0])[1];out.append(C);left-=C
 return out
def small(B):return sum(len(C)<=2 for C in comps(B))
def ports(v):return{(v+d)/2 for d in(1+1j,1-1j,-1+1j,-1-1j)}
def boundary(C):return set().union(*(ports(v)for q in C for v in ends(q,0)))-C
W={'S':'RRRRLRLRL','T':'RRRRLLLLRLRL'};hook=-1-1j
base={'S':{hook,-1+1j,-2+2j},'T':{hook,-1,2+1j}}
connector={'S':-3+1j,'T':1+2j};star={0,1,1-1j,-1j}
E4={hook,-1j,1-1j,1};E5=E4|{-1};dim={0,1-1j}
author=json.loads((D/'st_interior_ledger_controls.json').read_text());refs={(a['current_word'],a['successor_word']):a for a in author['profiles']}
geometry={};rows=[]
# Direct word integration, without importing author pose/graph helpers.
for Y,word in W.items():
 pos=0j;h=0;reads=[];first={}
 for t,c in enumerate(word):
  reads.append((t,pos,c));first.setdefault(pos,(t,c));h=(h+(1 if c=='R'else-1))%4;pos+=1j*(-1j)**h
 assert base[Y]=={q for q,(_,c)in first.items()if c=='L'}|{hook}
 assert set(q for _,q,_ in reads[:4])==star and all(c=='R'for _,q,c in reads[:4])
 assert len(component(base[Y]|star,0,wvertex(0j,0))[1])==7
 assert set(map(frozenset,comps(base[Y])))==({frozenset({hook}),frozenset({-1+1j,-2+2j})}if Y=='S'else{frozenset({hook,-1}),frozenset({2+1j})})
 assert reads[-2][1]==pos+hook*(-1j)**h and reads[-2][2:] == ('R',)
 assert reads[-1][1]!=reads[-2][1]
 geometry[Y]={'read_geometry':[(t,xy(q),c)for t,q,c in reads],'end':[xy(pos),h],'cut4_forced':ser(base[Y]|star),'cut4_white_boundary':ser(boundary(base[Y]|star))}
 # Successor mandatory nonhook bits are genuinely unread by the entire current word.
 for Z in W:
  older={pos+q*(-1j)**h for q in base[Z]-{hook}};assert not older&{q for _,q,_ in reads}
  geometry[Y]['successor_'+Z+'_unread_old_inputs']=ser(older)
 for Z in W:
  B0=base[Y]|({connector[Y]}if Z=='T'else set());B=set(B0);p=0j;h=0;trace=[];events=[];born={q:None for q in B};captured={}
  for t in range(len(word)+1):
   C=component(B,0,wvertex(p,h))[1];assert len(C)<=7
   assert bool(C)==(0<t<len(word));captured[t]=(set(B),set(C),p,h)
   trace.append({'cut':t,'pose':[xy(p),h],'field':ser(B),'active':ser(C),'components':sorted([ser(z)for z in comps(B)])})
   if t==len(word):break
   q=p;c=word[t];old=set(C);w=wvertex(p,h)
   if c=='R':
    assert q not in B;u,v=ends(q,0);target=v if u==w else u
    prior=component(B,0,target)[1]
    if prior&old:
     assert prior==old;prior=set()
    if prior:events.append({'tick':t,'kind':'import','cells':ser(prior),'lifetimes':[(xy(z),born[z])for z in sorted(prior,key=xy)]})
    born[q]=t
   else:assert q in B;birth=born.pop(q)
   p,h,ch=step(B,p,h);assert ch==c
   new=component(B,0,wvertex(p,h))[1]
   if c=='L':
    out=old-{q}-new
    if out:
     assert component(B,0,ends(next(iter(out)),0)[0])[1]==out
     events.append({'tick':t,'kind':'emit','cells':ser(out)})
  if Y=='S':
   assert captured[5][1]=={-1+1j,-2+2j}
   assert component(captured[5][0],0,ends(hook,0)[0])[1]==E4
   assert captured[6][1]==base[Y]|(star-{0})|{-1}
   assert captured[7][1]=={-2+2j} and component(captured[7][0],0,ends(hook,0)[0])[1]==E5
   assert [e for e in events if e['kind']=='import'and e['tick']==5][0]['cells']==ser(E4)
  else:
   assert captured[8][1]=={1,1-1j,2+1j}
   assert not component(captured[8][0],0,-1+1j)[1]
   assert ports(-1+1j)=={-1,0,-1+1j,1j}
   # All unknown two ports were already white at the saturated cut4 boundary.
   assert {-1+1j,1j}<=boundary(base[Y]|star)
   assert captured[10][1]=={2+1j} and component(captured[10][0],0,ends(0,0)[0])[1]==dim
   assert not[e for e in events if e['kind']=='import'and e['tick']==8]
  q=p+hook*(-1j)**h;Cq=component(B,0,ends(q,0)[0])[1];expected={q}|({connector[Y]}if Z=='T'else set());assert Cq==expected
  lasttick=len(word)-2;lastimports=[e for e in events if e['kind']=='import'and e['tick']==lasttick]
  assert lastimports==([]if Z=='S'else[{'tick':lasttick,'kind':'import','cells':ser({connector[Y]}),'lifetimes':[(xy(connector[Y]),None)]}])
  drop=small(B0)-small(B);assert drop=={('S','S'):1,('S','T'):2,('T','S'):0,('T','T'):1}[Y,Z]
  ref=refs[Y,Z];assert drop==ref['small_component_drop']
  for a,b in zip(trace,ref['full_trace']):
   assert(a['cut'],a['pose'],a['field'],a['active'])==(b['t'],[tuple(b['pose'][0]),b['pose'][1]],list(map(tuple,b['field'])),list(map(tuple,b['active'])))
  # Literal RL preparation produces the hook, without altering any other supplied input.
  pre=(B0-{hook})|{-1j};pp=hook;hh=0
  for want in'RL':pp,hh,ch=step(pre,pp,hh);assert ch==want
  assert(pre,pp,hh)==(B0,0j,0)
  rows.append({'pair':Y+Z,'seed':ser(B0),'trace':trace,'events':events,'drop':drop,'last_component':ser(Cq)})
# Independent inverse-two-toggle computation in the successor chart.
lastforms=[]
for Z in W:
 end={hook}|({-1}if Z=='T'else set());assert not component(end,0,1-1j)[1]
 before=(end|{-1j})-{hook};assert component(before,0,-1-3j)[1]=={-1j}
 assert component(before,0,-3-1j)[1]==(set()if Z=='S'else{-1})
 lastforms.append({'successor':Z,'end':ser(end),'pre_last_R':ser(before)})
# Universal combinatorial termination inequality, not an empirical run bound.
for triple in product('ST',repeat=3):
 def drop(a,b):return int(a=='S')+int(b=='T')
 assert drop(*triple[:2])+drop(*triple[1:])>=1
files={str(D/f):hashlib.sha256((D/f).read_bytes()).hexdigest()for f in('ST_SATURATED_PORT_FUEL.md','st_interior_ledger.py','st_interior_ledger_controls.json')}
files.update({str(G/f):hashlib.sha256((G/f).read_bytes()).hexdigest()for f in('ST_LAST_PORT_NORMAL_FORM.md','check_st_last_port_normal_form.py','st_last_port_normal_form_certificate.json')})
assert files[str(D/'ST_SATURATED_PORT_FUEL.md')]=='113b6cf581e39736169deb7e56d644b8bfccd67ac42934049d6dbcba8962dd79'
assert files[str(G/'ST_LAST_PORT_NORMAL_FORM.md')]=='32c703d6ece80ffbdd4517c39d6eb06e1affe5c3897e79179e666c1eb59f06dc'
deps=['check_cap7_structure_independent','check_cap7_word_mandatory_filters_independent','check_cap7_exact_word_pairs_independent']
dep_hash={s:hashlib.sha256(SELF.with_name(s+'.json').read_bytes()).hexdigest()for s in deps}
out={'status':'PASS universal arbitrary-exterior S/T saturated-port fuel; with signed necessary reduction, every finite-support orbit has infinitely many active-w cuts of mass at least8','source_hashes':files,'signed_reduction_reports':dep_hash,'geometry':geometry,'four_complete_controls':rows,'inverse_two_toggle_forms':lastforms,'analytic_review':[
'Every block after the first inherits a specific unchanged R-born hook from its preceding RL. First-L requirements plus that hook give three distinct OLD edges. They all attach to the four forced R star writes, so cap7 pins the ENTIRE cut4 active component, not merely a subgraph or type. Every unlisted incident edge is white regardless of the distant board.',
'S first detachment and next import are the SAME exact four-edge archive. The second detachment is the exact five-edge archive. T has no ambiguity through four deletions; the next R target has all four incident cells white, two deleted and two previously certified boundary-white. It imports nothing. Its next L emits an exact straight dimer. These facts exclude all untracked earlier passive attachments.',
'The successor cut4 pins the last tooth component to singleton or corner dimer. Undoing only the last L and R shows the previous active edge was the last-L singleton and the last R imported respectively NOTHING or a COMPLETE connector singleton. No hidden attachment can be part of either saturated graph. The connector is unread during the current word, hence old at that block entry, but not necessarily original-seed material.',
'All other passive components remain literally unchanged: only R can join them and all R ports have been accounted for. The intermediate S archive is reimported and retained as a five-edge output, not erased. Complete small-component fuel K (sizes1or2) therefore drops SS1,ST2,TS0,TT1. Distinct output components cannot silently merge, since the final component equalities and all R contacts are complete.',
'Every adjacent pair of such current-block drops has sum at least1, even in an aperiodic S/T word. Finite support makes K finite at any finite tail entry; an infinite S/T tail is impossible. The first block can be discarded so the inherited-hook premise causes no initial-fringe problem.',
'The separately signed cap7 kernel and bounded nonempty excursions force infinitely many empty first returns in any sustained cap7 tail. Its exact necessary word/pair graph eventually has only binary S/T or U-only; U-only spends distinct run-entry black cells and is impossible. The present arbitrary-mixture exclusion therefore closes sustained cap7 for EVERY finite-support state, and gives infinitely many full active-w mass>=8 cuts. This is not unbounded active size, eventual translation, or standard104 capture.'
]}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print([(r['pair'],r['drop'])for r in rows])

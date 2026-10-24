from pathlib import Path
from collections import defaultdict
from itertools import product
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'FOUR_INTRINSIC_MODULE_ALL_LENGTH_CLASSIFICATION.md';JF=D/'four_intrinsic_module_language_certificate.json'
assert sha(P).startswith('bbd559db') and sha(JF).startswith('bfb6b97f') and sha(D/'certify_four_intrinsic_module_language.py').startswith('e4417704')
J=json.loads(JF.read_text())
for f,h in J['dependencies'].items():assert sha(Path(f))==h
assert sha(S.with_name('check_standard_two_module_independent.json')).startswith('71afb2dd')
ns={'__file__':str(S.with_name('check_phase13_double_scatter_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Canonical source')[0],ns);sim,future=ns['sim'],ns['future'];V=[1j,1,-1j,-1];xy=lambda z:[int(z.real),int(z.imag)]
def geo(w,h=3):
 p=0j;E=[]
 for t,c in enumerate(w):
  hi=h;h=(h+(1 if c=='R'else-1))%4;E.append(dict(t=t,p=xy(p),hi=hi,ho=h,c=c));p+=V[h]
 return E,p,h
W=json.loads((D/'active_C_entry_exit_forests_certificate.json').read_text())['base_controls']['S104']['word'];spec={'A':(45,10),'B':(55,94),'C':(13,14),'D':(27,90)};words={a:''.join(W[(i+j)%104] for j in range(n)) for a,(i,n) in spec.items()}
for a,w in words.items():
 E,d,h=geo(w);assert d==-1+1j and h==3;row=J['module_profiles'][a];assert E==row['full_events'] and w==row['word'] and len(w)==row['length'] and w.count('R')-w.count('L')==row['growth'];sources=defaultdict(list)
 for e in E:
  x,y=e['p'];sources[0,x+y].append(dict(relative_module_index=x,**e))
 assert [dict(representative=list(q),reads=sorted(es,key=lambda z:(z['relative_module_index'],z['t']))) for q,es in sorted(sources.items())]==row['complete_sources']

def finite(w,h=3):
 E,p,hh=geo(w,h);seen={};seed=set();field=set()
 for e in E:
  q=complex(*e['p']);c=e['c']
  if q in seen and seen[q]['c']==c:
   prev=seen[q];visits=[z for z in E if z['p']==e['p'] and prev['t']<=z['t']<=e['t']];assert len(visits)==2
   return dict(word=w,legal_on_some_board=False,witness=dict(cell=xy(q),first=prev,second=e,complete_visits_between=visits))
  if q not in seen and c=='L':seed.add(q);field.add(q)
  field.symmetric_difference_update({q});seen[q]=e
 z=sim(seed,len(w),h=h,expected=w);assert set(z['B'])==field and z['p']==p and z['h']==hh
 return dict(word=w,legal_on_some_board=True,initial_black=sorted(map(xy,seed)),final_black=sorted(map(xy,field)),head=xy(p),heading=hh,all_events=E)
pairs={a+b:finite(words[a]+words[b]) for a,b in product(words,repeat=2)};triples={q:finite(''.join(words[a] for a in q)) for q in ('AAB','CAB')}
assert pairs==J['all16_pair_controls'] and triples==J['two_triple_controls'];legal=[p for p,z in pairs.items() if z['legal_on_some_board']];assert legal==['AA','AB','BA','CA','CD','DC']
assert [(q,z['witness']['cell'],z['witness']['first']['t'],z['witness']['second']['t']) for q,z in triples.items()]==[('AAB',[0,-1],5,45),('CAB',[1,-1],10,50)]
for r in J['all72_rotation_controls']:
 z=finite(''.join(words[a] for a in r['word']),r['heading']);assert z['legal_on_some_board']==r['compatible'];orig=(pairs|triples)[r['word']]
 if not r['compatible']:assert (z['witness']['first']['t'],z['witness']['second']['t'])==(orig['witness']['first']['t'],orig['witness']['second']['t'])
assert len(J['all72_rotation_controls'])==72
# Whole literal blank realization, retaining all current cells and certifying future words.
z=sim(set(),10335,h=0,cuts={10302,10334});checks={}
for name,row in J['full_blank_standard_positive_controls'].items():
 field,p,h=z['snap'][row['time']];assert sorted(map(xy,field))==row['black'] and xy(p)==row['head'] and h==row['heading'];fw,d,dead,tests=future(field,p,h);assert fw==row['word']==''.join(words[a] for a in name) and d==-2-2j;checks[name]=dict(mass=len(field),tests=tests)
assert checks['CD']['mass']==750 and checks['AB']['mass']==758
succ={a:[b for b in words if a+b in legal] for a in words};assert succ==J['successor_table']=={'A':['A','B'],'B':['A'],'C':['A','D'],'D':['C']};assert [p for p in legal if p not in ('AA','CA')]==J['edges_left_after_finite_field_infinite_tail_filter']==['AB','BA','CD','DC']
# A itself remains a stable prepared full-drift word, not a WHITE wave.
E,d,h=geo(words['A']);H=defaultdict(list)
for e in E:
 x,y=e['p'];k=-x;H[0,x+y].append((e['t']-k*10,e['c']))
for rs in H.values():rs.sort();assert all(a[1]!=b[1] for a,b in zip(rs,rs[1:]))
assert sum(rs[0][1]=='L' for rs in H.values())==1
O=dict(status='PASS exact fixed four intrinsic module language all-length classification only',proof=sha(P),certificate=sha(JF),script=sha(S),literal_local_events=208,legal_pairs=legal,pair_initial_masses={q:len(pairs[q]['initial_black']) for q in legal},pair_obstructions=10,triple_obstructions=2,rotation_controls=72,whole_standard_controls=checks,analytic_review=[
'Both signed actual C-cycle decompositions are integrated in one fixed W-heading/delta(-1,1) frame. All208 local events and complete physical delta source tables reconstruct. This is only a coordinate convention; an n-module full period still has full drift n*delta and all residues.',
'All16 pairs are reconstructed from actual same-cell chronology. Six have explicit complete minimal finite boards, including genuine CA2-to6. Every other pair has two consecutive same-cell identical turns, impossible on any board. Exact AAB L5/L45 and CAB L10/L50 are similarly unconditional with no hidden intervening cell read.',
'The resulting finite necessary pair graph plus those two triple conflicts implies every AA or CA occurrence forces an A-only future. A periodically repeated compatible sequence must therefore be A alone, alternating AB, or alternating CD. A has one genuine input class and is a stable infinitely prepared wave, not a finite autonomous or WHITE controller.',
'In an actual infinite finite-field module trajectory, an A-only future is impossible by the separately signed injective distinct entry-BLACK-cell charge. The field at that future entry remains finite and includes all previously written archive. Thus AA and CA cannot occur anywhere in such an infinite tail, and the remaining pairs force AB or CD alternation from the first module. No reset or uncharged regenerated source is used.',
'Fresh literal blank replay certifies the entire750/758-cell CD/AB states and their exact infinite canonical words. The conclusion covers only these four whole modules under a common proper rotation/translation, with no inserted routers or individual reorientation. No universal language-entry, unrestricted controller/WHITE S1 theorem, general replacement-family exclusion, or global attraction follows.'
]);S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))

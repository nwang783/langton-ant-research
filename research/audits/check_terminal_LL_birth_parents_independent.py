from pathlib import Path
from collections import deque
import json,hashlib,ast
S=Path(__file__).resolve();R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();files={'terminal_LL_supplier_has_two_fixed_birth_links_and_outward_parents.md':'738876d5','terminal_LL_birth_time_unit_qualifier.md':'a0d09ddd'}
for f,h in files.items():assert sha(D/f).startswith(h)
lib=S.with_name('check_terminal_LL_portal_suppliers_independent.py');n={'__file__':str(lib)};exec(lib.read_text().split('out=dict(status=')[0],n)
V,out,cv,string,cin,cout,ref=[n[k]for k in('V','out','cv','string','cin','cout','ref')];q=1+1j;C=1+2j;RR=2+2j;H=2+1j;v=1+0j;X=2+0j;F=1+0j;P=1j;Q=1+2j;G=2+1j
xy=lambda p:[int(p.real),int(p.imag)]
def face_edges(f):return[(f+1,3),(f,0),(f+1j,1),(f+1+1j,2)]
def lower(edges,start):
 d={start:0}
 for _ in range(60):
  change=False
  for a,b,k in edges:
   if a in d and d.get(b,-10**12)<d[a]+k:d[b]=d[a]+k;change=True
  if not change:return d
 raise AssertionError('positive clock cycle')
rows=[]
for key,row in ref.items():
 if row['result']!='open':continue
 hs={complex(x,y):cv(w)for x,y,w in key};su={};edges=[]
 for p,w in hs.items():
  for j in range(len(w)-1):edges.append(((p,j),(p,j+1),4))
  for h,z in enumerate(V):
   if p+z in hs:
    for i,j in zip(cout(w,h),cin(hs[p+z],h)):su[p,i]=(p+z,j);edges.extend([((p,i),(p+z,j),1),((p+z,j),(p,i),-1)])
 # Exact actual-successor equalities determine the named event component.
 adj={}
 for a,b in su.items():adj.setdefault(a,[]).append((b,1));adj.setdefault(b,[]).append((a,-1))
 times={(q,0):0};todo=[(q,0)]
 for a in todo:
  for b,k in adj.get(a,[]):
   if b in times:assert times[b]==times[a]+k
   else:times[b]=times[a]+k;todo.append(b)
 assert {e:times[e]for e in[(H,0),(RR,1),(C,1),(q,1),(H,1),(RR,2)]}=={(H,0):-3,(RR,1):-2,(C,1):-1,(q,1):8,(H,1):9,(RR,2):10}
 bdP=[(p,cout(hs[p],h)[0])for p,h in face_edges(P)];assert[times[e]for e in bdP]==[0,1,6,-1]
 bdF=[(p,cout(hs[p],h)[0])for p,h in face_edges(F)];dist=lower(edges,(q,0));assert[dist[e]for e in bdF]==[10,11,8,13]
 # Q's earlier incoming R0 boundary edge, and G's earlier incoming H0 edge.
 assert lower(edges,(RR,0))[q,0]>=6 and su[RR,0]==(C,0)
 assert hs[RR][0]==2 and hs[H][0]==3
 assert all(cout(hs[p],h)[0]==j for p,h,j in[(RR,3,0),(C,0,0),(H,0,0),(RR,1,2)])
 # Every known later boundary departure is later in the SAME physical history.
 assert all(i>=0 for i in cout(hs[RR],3))and all(i>=0 for i in cout(hs[C],0))
 # Equal opposite-R counts identify these four C sectors with the actual portal M.
 for p in(q,C,RR,H):assert len(hs[p][::2])==2 and len(set(hs[p][::2]))==2
 rows.append(dict(v=string(hs[v]),X=string(hs[X]),H=string(hs[H]),R=string(hs[RR]),P_boundary_times=[0,1,6,-1],F_boundary_lower=[10,11,8,13],birth_P=-1,birth_F=8,birth_Q_upper=-7,birth_G_upper=-4,parent_Q_upper=-12,parent_G_upper=-9))
assert len(rows)==18
# WHITE first-L births at each remaining corner have the exact rotated parent.
# active old R0 C-face is p + off[heading], and SAME L1 turns into new face.
off=(-1j,-1-1j,-1,0j)
parents=[]
for cell,h,newface,parent in[(1+3j,2,Q,3j),(2+3j,3,Q,2+3j),(3+1j,0,G,3+0j),(3+2j,3,G,3+2j)]:
 assert cell+off[h]==parent;outdir=(h-1)%4
 assert(cell,outdir)in face_edges(newface);parents.append([xy(newface),xy(cell),h,xy(parent)])
assert C+off[hs[C][0]]==Q and q+off[hs[q][0]]==P
bp=S.with_name('check_max_C_face_birth_independent.json');b=json.loads(bp.read_text());assert b['status'].startswith('PASS')and 'decrease>=5'in b['scope']
outreport=dict(status='PASS scoped terminal-LL one-generation canonical-birth links and parent alternatives',bindings={f:sha(D/f)for f in files},dependencies={'check_terminal_LL_portal_suppliers_independent.json':sha(lib.with_suffix('.json')),'check_max_C_face_birth_independent.json':sha(bp)},all18_profiles=rows,physical_parent_alternatives=parents,analytic=[
'The actual complete WHITE cap4 portal and balanced opposite R counts put F,P,Q,G at the SAME GLOBAL maximum M. This is a checked local curl relation, not a general first-R maximum principle.',
'All four first directed P-boundary departures are exactly alpha,alpha+1,alpha+6,alpha-1; hence B(P)=alpha-1 at C.L1 with SAME R0 parentQ. All F-boundary lower times are alpha+10,alpha+11,alpha+8,alpha+13; q.L1 attains alpha+8 and its SAME R0 parent isP. Later copies cannot beat first local ranks. Thus Q->P->F are actual canonical birth links.',
'R.L1=alpha-2, and consecutive physical visits are at least FOUR GLOBAL STEPS apart, so R.R0<=alpha-6. Its incoming S boundary departure already activatesQ at<=alpha-7. R/C bottom-corner departures are later, so Q birth is at one of its two top corners. The first-L theorem gives parents(0,3)or(2,3), birth<=B(F)-20.',
'H.R0=alpha-3 has incoming W boundary edge ofG atalpha-4. H own first G departure is later; R first G departure is exactlyalpha+10. Thus only coordinate-right corners remain, with parents(3,0)or(3,2), birth<=B(F)-17. Every corner orientation and old SAME R0 face is independently reconstructed.',
'Canonical birth is earliest directed boundary departure, not a guessed cell first visit or b-map first-R. All physical lifts and possible full-drift recycling remain; strict birth-time decrease does not prohibit returning to a translated class.',
'Mandatory a0d09ddd means four time steps, not four extra local reads. Same/different components, merging Q/G ancestry, all open upper/right histories and lack of terminal-mode persistence are retained. No iteration, new b-cycle, distinct-root injection, fuel payment or whole-front exclusion follows.'
])
S.with_suffix('.json').write_text(json.dumps(outreport,indent=2)+'\n');print(outreport['status']);print(sha(S.with_suffix('.json')))

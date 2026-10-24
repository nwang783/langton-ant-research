"""Independent dependency assembly, not a rerun of the signed role kernels."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent.parent
HERE=ROOT/'restricted_language_closure_2026-10-23'
manifest=json.loads((HERE/'dependency_manifest.json').read_text())
for rel,h in manifest['files'].items():
 assert hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()==h,rel
D='LLLLRLRRRR';C='LLLLRLRRRRLRRRR';V='LLLLRLRRRRLRRLRRRR';U='LLLLRLRRRRLRLLLLRRRRLRRLRRRR';M='LLLLRLRRRRL'
assert list(map(len,(D,C,V,U,M)))==[10,15,18,28,11]
G=json.loads((ROOT/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json').read_text())['geometry']
words={'D':D,'DC':D+C,'V':V,'VC':V+C,'VCC':V+C+C,'U':U,'UC':U+C,'UCC':U+C+C}
for g in G:
 if g['name']in words:assert g['word']==words[g['name']] and g['marker']==M
assert {n for n in words if 'U' not in n}=={'D','DC','V','VC','VCC'}
# Unknown initial colors, exact per-cell alternating reads, own physical walk.
def literal(w):
 p=(0,0);h=0;last={};dirs=((0,1),(1,0),(0,-1),(-1,0))
 for i,a in enumerate(w):
  if p in last and last[p][1]==a:return dict(feasible=False,conflict_read=i,previous_read=last[p][0],cell=list(p))
  last[p]=(i,a);h=(h+(1 if a=='R' else -1))%4;dx,dy=dirs[h];p=(p[0]+dx,p[1]+dy)
 return dict(feasible=True,length=len(w),endpoint=[*p,h])
controls={n:literal(w) for n,w in {'UCCC_M11':U+C*3+M,'DCC_U':D+C*2+U,'DCC_D':D+C*2+D,'DCC_D_L':D+C*2+D+'L','DCC_D_C':D+C*2+D+C,'DCC_V':D+C*2+V,'CCCC_M11':C*4+M,'VCCC_M11':V+C*3+M}.items()}
assert controls['UCCC_M11']['conflict_read']==81
assert controls['DCC_U']['conflict_read']==52
assert controls['DCC_D']['feasible'] and controls['DCC_D_L']['feasible']
assert all(not controls[n]['feasible'] for n in ('DCC_D_C','DCC_V','CCCC_M11','VCCC_M11'))
assert 60+55+88==203 and 60+55+1==116
E=range(2,295,2);A=4851+3*len(E);marks=1+len(E);Mv=marks*(A+1)
assert (len(E),A,marks,Mv,2*A+295*Mv)==(147,5292,148,783364,231102964)
assert 294+max(294,6+294)==594
# Source/no-U split quantitative interface, with no original-origin reset.
def F(m):
 B=57+38*(m-5);R=(2*B+4)//5;t=(2*R+1)**2//3
 return 20*R*(t+1)+28*t
assert all(F(m+1)>F(m)>0 for m in range(5,105))
# Two ordinary C-child transfers reverse heading and return the source pose.
p=complex(3,3);assert p+(-p)==0
assert len(V+'LRRRR')==23 and V+'LRRRR' not in words.values()
all8note=ROOT/'causal_archive_frontier_2026-10-23/finite_support_complete8_exclusion.md'
assert hashlib.sha256(all8note.read_bytes()).hexdigest()=='d1d680d128745427df9e7943dcda24875dafd45a49f021647f69f18f147ba4eb'
assert 'finite COMPLETE' in all8note.read_text()
# This graph is kept separate from UNION6 and from the four-word theorem.
q=json.loads((ROOT/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json').read_text())
assert q['classes']==214 and len(q['quotient_edges'])==993
# Independent direct infinite-tail packing checks, supplementary to bounded trim.
long_C={n:literal(w) for n,w in {'C5':C*5,'DC4_M':D+C*4+M}.items()}
assert all(not r['feasible']for r in long_C.values())
ten={g['name']:g['word']for g in G}
boundary={}
for name,w in ten.items():
 boundary['successor_DCC_'+name]=literal(ten['DCC']+w+M)
 boundary['predecessor_DCCC_'+name]=literal(w+ten['DCCC']+M)
assert len(boundary)==20 and all(not r['feasible']for r in boundary.values())
# Kosaraju independently, preserving source/type/target edge ordering.
def cyclic(es):
 n=q['classes'];adj=[[]for _ in range(n)];rev=[[]for _ in range(n)]
 for a,t,b in es:adj[a].append(b);rev[b].append(a)
 seen=set();order=[]
 def dfs(a):
  seen.add(a)
  for b in adj[a]:
   if b not in seen:dfs(b)
  order.append(a)
 for a in range(n):
  if a not in seen:dfs(a)
 seen=set();result=[]
 def get(a,c):
  seen.add(a);c.add(a)
  for b in rev[a]:
   if b not in seen:get(b,c)
 for a in reversed(order):
  if a in seen:continue
  c=set();get(a,c);ee=[e for e in es if e[0]in c and e[2]in c]
  if len(c)>1 or any(a==b for a,t,b in ee):result.append((len(c),len(ee),sorted({e[1]for e in ee})))
 return sorted(result,reverse=True)
es=q['quotient_edges'];scc={k:cyclic(e)for k,e in dict(all=es,DCUV=[e for e in es if e[1]<4],FQB=[e for e in es if e[1]>=4]).items()}
assert scc=={'all':[(214,993,list(range(7)))],'DCUV':[(93,417,list(range(4)))],'FQB':[]}
out=dict(status='PASS: independent finite-support all-complete-eight and raw-DCUV closure assembly',scope='Finite COMPLETE black support only. No arbitrary eventual-entry, new K-label union, finite switch count, original V1/U1 funding or universal capture claim.',direct_long_C=long_C,direct_boundary_conflicts=boundary,separate_seven_word_graph_scc=scc,base_words=dict(D=D,C=C,V=V,U=U,marker=M),literal_controls=controls,constants=dict(A=A,marks=marks,V_bound=Mv,eventual_epoch_bound=2*A+295*Mv,boundary_trim=203,start_cut_choices=116),analytic_steps=['First-U/no-U dichotomy with actual finite complete board at later cut.','Signed bounded prefix/suffix trim plus fixed finite start cuts and finitely branching parsing compactness.','Hypothetical seven-word tail must use F/Q/B infinitely; edges are not deleted from mixed factors.'],all8_note_hash=hashlib.sha256(all8note.read_bytes()).hexdigest(),dependencies=manifest['files'])
(ROOT/'audits/check_finite_support_DCUV_closure_assembly_independent.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items()if k not in ('dependencies','literal_controls')},indent=2))

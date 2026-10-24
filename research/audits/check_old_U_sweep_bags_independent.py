from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__).resolve();R=S.parents[1];P=R/'old_U_contact_sweep_frontier_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=P/'manifest.json';assert sha(mf)=='5f3d0c902293d8a67c6660150f3ae704d6d06b81adaad4ac4cb34c28210230fd';m=json.loads(mf.read_text())
for f,h in m['files'].items():assert sha(P/f)==h
for f,h in m['dependencies'].items():assert sha(R/f)==h
ref=json.loads((P/'sweep_frontier.json').read_text());ns={'__file__':str(S.with_name('check_U_second_creator_bud_guards_independent.py'))};exec(Path(ns['__file__']).read_text().split('\nsource=[]')[0],ns);W,M,walk,xy=[ns[k]for k in('W','M','walk','xy')];V=(1j,1,-1j,-1);s=lambda p:int(2*p.real+p.imag);t=lambda p:int(p.real-2*p.imag)
def geom(word,p=0j,h=0):
 vertices=[p];reads=[]
 for c in word:
  reads.append((p,h,c));h=(h+(1 if c=='R'else-1))%4;p+=V[h];vertices.append(p)
 return vertices,reads,p,h
footprints=[]
for a in'DCVUFQB':
 for h in range(4):
  vs,rs,p,hh=geom(W[a],h=h);vals=list(map(s,vs));row={'atom':a,'heading':h,'actual_head_drift':list(xy(p)),'sweep_drift':s(p),'transverse_drift':t(p),'exact_fine_vertex_sweep_interval':[min(vals),max(vals)],'RAW_read_count':len(rs)};footprints.append(row)
assert footprints==ref['all28_literal_RAW_fine_vertex_sweep_intervals'];drifts={a:[z['sweep_drift']for z in footprints if z['atom']==a]for a in'DCVU'}
assert drifts=={'D':[3,1,-3,-1],'C':[1,2,-1,-2],'V':[5,5,-5,-5],'U':[4,8,-4,-8]}
rad=lambda chars:max(abs(v)for z in footprints if z['atom']in chars for v in z['exact_fine_vertex_sweep_interval']);marker=max(abs(s(p))for h in range(4)for p in geom(M,h=h)[0]);assert(rad('DCVU'),rad('FQB'),marker)==(8,14,5)
# Signed source-relative clock counts exclude terminal contact-C ENTRY, not its physical RAW.
comp=json.loads((R/'one_foreign_first_contact_compression_2026-10-24/first_contact_C_window.json').read_text());urows=[z for z in comp['all44_exact_source_target_C_window_rows']if z['source_class']=='preFOREIGN_ordinary'and z['source_atom']=='U'];assert len(urows)==4 and max(k for z in urows for k in z['allowed_C_counts_before_contact_ENTRY'])==4
bound=6*(2*8+1)*max(map(len,(W[a]for a in'DCVU')))+max(map(len,(W[a]for a in'FQB')))+len(M);assert bound==2941
controls=[]
for n in(1,10,100):
 atoms=['U','F']+['D']*n;word=''.join(W[a]for a in atoms)+M;rr=walk(word);assert rr['feasible'];seed={p for p,c in rr['req'].items()if c};B=set(seed);p=0j;h=0;blocks=[];reads=[]
 for k,body in enumerate([W[a]for a in atoms]+[M]):
  vs,rs,pp,hh=geom(body,p,h);lo=min(map(s,vs));hi=max(map(s,vs));start=len(reads)
  for q,hh0,c in rs:
   assert c==('L'if q in B else'R');B^={q};reads.append((q,hh0,c,k))
  blocks.append((lo,hi,start,len(body)));p,h=pp,hh
 last={};edges=[]
 for i,(q,hh0,c,k)in enumerate(reads):
  if i:edges.append((i-1,i,'program'))
  if q in last:edges.append((last[q],i,'cell'));assert reads[last[q]][2]!=c
  last[q]=i
 for i,j,kind in edges:
  A=blocks[reads[i][3]];BB=blocks[reads[j][3]];assert max(A[0],BB[0])<=min(A[1],BB[1])
  if kind=='cell':assert all(b[0]<=s(reads[i][0])<=b[1]for b in(A,BB))
  elif reads[i][3]!=reads[j][3]:assert all(b[0]<=s(reads[j][0])<=b[1]for b in(A,BB))
 peak=max(sum(b[3]for b in blocks if b[0]<=l<=b[1])for l in range(min(b[0]for b in blocks),max(b[1]for b in blocks)+1));assert peak<=bound
 old=next(z for z in ref['genuine_complete_finite_word_regressions']if z['n']==n);assert set(map(xy,seed))==set(map(tuple,old['complete_initial_black']))and set(map(xy,B))==set(map(tuple,old['complete_final_black']))and [*xy(p),h]==old['complete_final_pose']
 assert(len(reads),len(edges),peak)==(old['all_physical_reads'],old['actual_constraint_edges'],old['exact_maximum_read_bag'])
 controls.append({'n':n,'initial_mass':len(seed),'actual_reads':len(reads),'constraint_edges':len(edges),'max_read_bag':peak,'full_final_mass':len(B)})
X=geom(W['D']*5)[2];Y=geom(W['V']*3)[2];assert(X,Y)==(5+5j,3+9j)and s(X)==s(Y)==15 and(t(X),t(Y))==(-5,-15)
for n,z in[(1,1),(2,2),(2,1),(1,2),(5,5),(10,9)]:assert s((n-z)*(X-Y))==0 and t((n-z)*(X-Y))==10*(n-z)
out={'status':'PASS bounded path decomposition of the ACTUAL embedded old-U first-contact read graph; no finite geometry quotient','manifest':sha(mf),'all28_complete_fine_vertex_intervals':footprints,'bounds':{'ordinary_epochs':6,'heads_per_epoch_per_level':17,'ordinary_blocks':102,'all_blocks':104,'read_vertices':2941,'pathwidth':2940},'fresh_full_board_controls':controls,'abstract_two_track_displacements':{'D5':xy(X),'V3':xy(Y),'equal_sweep':15,'transverse_gap':'10(n-m)','NOT_an_ant_history':True},'analytic_review':[
'The signed preforeign oldU source window has K<=4 at terminal contact ENTRY. The terminalRAW C stays in its incoming-heading epoch and creates no later ordinary block before that RAW ends. Four priorC rotations plus one genuine foreign split yield at most6 ordinary epochs. Final actualM11 is one separately charged block, not a repeated context at every atom.',
'Exact all28 literal fine-vertex intervals include each true exit. Every ordinary entry sweep value moves by a nonzero integer of the same sign within its epoch, including its terminalC. A block meeting integer level l has entry in[l-8,l+8], so at most17 distinct entry heads per epoch. RAW maximum28, foreign74 and one actual prefix11 give2941 read-occurrence vertices per bag.',
'Each actual read vertex is assigned the entire contiguous interval of its own block. Same-cell edges share the bag at that cell sweep coordinate. Program-order edges within a block are immediate; across blocks the previous block EXIT and next block ENTRY are the same actual head, so their intervals overlap there. This specifically retains the D10 exit stub. Thus this is a genuine path decomposition, not an estimate from proxy chords.',
'Chronology follows epoch order and actual atom ticks. Sweep increases inN/E, decreases inS/W; reversing that latter order would be incorrect. Full fields and first-read bits are retained. Fresh U,F,D^n controls atn1,10,100 test every actual program and same-cell edge, but are not claimed all-n positives or oldU contacts.',
'Given an already correct embedded/coincidence certificate, color and order consistency has bounded finite frontier data. It does not supply a finite-state generator for unbounded transverse integer geometry. The two abstract D5/V3 tracks have equal sweep and gap10(n-m); endpoint equality distinguishes allA^n by suffixB^n. This is NOT an actual Langton history and does not refute a stronger ant-specific quotient. No DFA, whole-language decision, arbitrary earlierD/C/V ancestry, or capture conclusion.'
]};S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])

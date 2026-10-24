from pathlib import Path
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];p=SELF.parent/'check_serial_bridge_archive_independent.py';ns={'__file__':str(p)};exec(p.read_text().split('# Fixed local masks')[0],ns)
ends,graph,component,wvertex=[ns[x]for x in('ends','graph','component','wvertex')]
# Fine-cut checks retain the entire field and distinguish individual birth IDs.
B=set();birth={};p=0j;h=0;metric=0;gates=0;completed=[];records={}
for t in range(1000):
 w=wvertex(p,h);k=int(w.real+w.imag)%4;V,C=component(B,k,w);M=len(C)
 for q in C:
  assert max(abs(p.real-q.real),abs(p.imag-q.imag))<=M;metric+=1
 before=set(C);oldB=set(B);oldw=w;ch='L'if p in B else'R';read=p
 if ch=='L':
  b=birth.pop(read);B.remove(read)
  cuts=records.pop((read,b));assert len(cuts)==t-b and cuts[0]and cuts[-1]
  j=sum(cuts[i]and not cuts[i-1]for i in range(1,len(cuts)))
  episodes=1+sum(cuts[i]!=cuts[i-1]for i in range(1,len(cuts)));assert episodes==2*j+1
  completed.append((t-b,j))
 else:B.add(read);birth[read]=t;records[(read,t)]=[]
 h=(h+(1 if ch=='R'else-1))%4;p+=1j*(-1j)**h
 nw=wvertex(p,h);assert int(nw.real+nw.imag)%4==k
 NV,NC=component(B,k,nw)
 survivors=oldB& B
 if ch=='L':
  assert NC<=before-{read}
  if(before-{read})-NC:
   eu,ev=ends(read,k);remain=component(oldB-{read},k,eu)[0];assert ev not in remain
 else:
  assert before<=NC and oldw==nw
  added=(NC-before)-{read}
  if added:
   other=next(z for z in ends(read,k)if z!=oldw);assert added==component(oldB,k,other)[1]
 for q,b in birth.items():records[(q,b)].append(q in NC)
 gates+=1
D=ROOT/'active_w_archive_itinerary_2026-10-23';note=D/'ACTIVE_EPISODES.md';sha=hashlib.sha256(note.read_bytes()).hexdigest();assert sha=='ad3cb9f07e078bcbaaa02622004f56254b211de2ed238fa2bd031e7d5e3d5721'
stale=ROOT/'sources/kehao95-core/memory_feedback/proof/stale-memory.md'
out={'status':'PASS universal active-episode metric/gates and conditional eventual-translation criterion','note_sha256':sha,'retained_stale_memory_source_sha256':hashlib.sha256(stale.read_bytes()).hexdigest(),'fine_cut_control_updates':gates,'all_active_edge_metric_checks':metric,'completed_R_lifetimes':len(completed),'analytic':['An edge in an M-edge active component has an endpoint reachable from the cursor without using that edge, along at most M-1 diagonal edges. Two half-unit midpoint/cursor offsets give the exact infinity bound M, valid at every fine cut including consecutive R writes.','A continuous active lifetime with active mass at most M pins every head to one fixed integer square of side2M+1. The exterior field is unchanged between those cuts. More than4n^2*2^(n^2) cuts repeat the COMPLETE state, producing a bounded orbit forbidden by the retained extremal-cell escape argument. Thus H(M)=Q(2M+1) is a valid uniform episode cut bound.','R keeps w fixed and only joins the complete other-end component. L moves w across its deleted edge; all surviving old-active edges stay active unless that edge is a bridge, in which case exactly the arrival component remains. Therefore every completed dormant interval is a genuine bridge departure followed by whole-component R import.','An R lifetime born at b and consumed at d occupies exactly d-b cuts b+1 through d, active at both ends. At most J dormant episodes of at most A cuts and at most J+1 active episodes give age <=(J+1)H(M)+JA. This counts physical cuts, not compressed blocks.','At a finite-support cut T only finitely many current lifetimes exist. After their last eventual consumption, every L obeys the asserted age bound. The exact suffix predictor is then autonomous on at most2^D words; a zero-drift/rotating periodic word would be bounded and is excluded. Eventual nonzero translation follows, not a classification as104.','Contraposition yields the stated consumed-lifetime trilemma for any non-eventually-translating finite-support orbit. Arbitrarily old never-consumed passive support is irrelevant. None of the sustained bounds M,A,J is proved here.'],'scope':'Global finite-support dynamics. Conditional sufficient criterion and exact decomposition only; no sustained boundedness, capture, finite-summary replacement or original-mass age bound.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(metric,len(completed))

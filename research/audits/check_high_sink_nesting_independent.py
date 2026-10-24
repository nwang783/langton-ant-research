from pathlib import Path
from itertools import product
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();F=D/'critical_flow2_roots_cannot_have_high_flow_predecessors.md';assert sha(F)=='f59ebed0eeb02378ffc766d7d8bd014a333f44d8994c51b6cdc243579e3b9297'
H='NESW';out=lambda w:[H[(H.index(c)+(1 if i%2==0 else-1))%4]for i,c in enumerate(w)];ranks=lambda w,h,output=False:[i for i,c in enumerate(out(w)if output else w)if c==h]
allw=lambda a:[''.join(z)for n in range(1,5)for z in product(a,repeat=n)]
pred=[w for w in allw('NS')if w[0]=='N'and w.count('N')>=2 and out(w).count('E')==2];assert set(pred)=={'NNSS','NSSN','NNN','NNNN'}
left3=[w for w in allw('EW')if w[0]=='W'and w.count('E')==3 and out(w).count('N')==3];assert left3==['WEEE']
strands=[]
for u in ['WEE','WEEW']:
 h=['WEEE','NNN',u];e=[]
 for i,d in [(0,'N'),(1,'E')]:
  src=ranks(h[i],d,True);dst=ranks(h[i+1],d);assert len(src)==len(dst)
  e += [(i,a,i+1,b)for a,b in zip(src,dst)]
 assert (0,0,1,0)in e and(1,0,2,1)in e and(0,3,1,2)in e and(1,2,2,2)in e
 strands.append(dict(root=u,edges=e,first_strand=[['w',0],['q',0],['u',1]],late_strand=[['w',3],['q',2],['u',2]],nested_margins=[2,6]))
J=json.loads((D/'high_sink_nested_return_ordinal_control.json').read_text());assert J['actual_first_strand']==strands[0]['first_strand']and J['actual_third_second_strand']==strands[0]['late_strand']
LL=json.loads((D/'check_mixed_LL_zero_chord_interface.json').read_text());survivors=[]
for r in LL['necessary_open_rows']:
 h=r['histories']
 if h['Z']!='NNSS':continue
 if h['Y']!='EEWW'and len(h['B'])==h['B'].count('S'):continue
 survivors.append(h)
assert len(survivors)==7
assert sum(h['Y']!='EEWW'for h in survivors)==2
# Flat Y next-edge ordinals, rotated so its first R leaves S.
y='EWWE';assert ranks(y,'S',True)==[0,1]
outobj=dict(status='PASS critical flow2 incoming-sink nesting and exact one-flat lifespan',proof=sha(F),control=sha(D/'high_sink_nested_return_ordinal_control.json'),complete_predecessor_alphabet=pred,unique_LEFT3=left3,strands=strands,critical_LL_seven_rows=survivors,analytic_review=[
'The critical last-LEFT gate forbids a crossing as second LL, so every flow2 O/U root has RIGHT predecessor. No-one-use and cap4 give precisely two flat2 profiles, odd3->2 sink and4->2 target. This is local and imposes no global C maximum.',
'The isolated flow4 target necessarily follows RIGHT. A sink3 following RIGHT is also in an RR run, whose external LEFT endpoints are covered by signed general LRRL including flow1. Essential simplicity supplies the missing preceding LEFT by excluding3RIGHT turns. That gate excludes an O/U following LEFT without any global-height bound.',
'The remaining LEFT3 WEEE -> RIGHT sinkNNN -> O/U has literal first strand wR0,qR0,uL1 and late strand wL3,qR2,uR2. Same-cell gap>=4 gives T1w>=T1u+2 and T2w<=T2u-6, strictly nested actual physical critical LEFT intervals, impossible. No moduloP identification or input-color shortcut.',
'Filtering the signed39 mixed LL rows with last-LEFT V and no high-flow incoming crossing leaves7:three flat rows andfour passiveV/V zero-chord rows. Only the2 flat first-LL O/U cleanups remain crossing modes. Local long-U open controls remain valid but cannot satisfy the stated full critical chronology.',
'At globalM with one flat and some root, signed provider result gives G=F+d, unique root, Yflat, ell<age13<P. New adjacency u=b(G) yields T1u=T0G+1,T2u=T1G+1. Combining exact rootspan with P+ell-age13 gives T3F-T0F=P+ell. Boundary factor G.R0->F.L3 has displacement-d; unresolved exterior F.L3->G.L1 has+d. Lifespan>P is retained, not an impossibility.',
'No completed exterior, general oneuse, period/age bound, old-stock depletion or attraction conclusion follows.'
],dependencies={str(p.relative_to(R)):sha(p)for p in [R/'audits/check_mixed_RR_closure_independent.json',R/'audits/check_mixed_LL_gate_independent.json',R/'audits/check_mixed_first_track_pipeline_independent.json',R/'audits/check_critical_flat_providers_independent.json']});S.with_suffix('.json').write_text(json.dumps(outobj,indent=2)+'\n');print(outobj['status']);print(sha(S.with_suffix('.json')))

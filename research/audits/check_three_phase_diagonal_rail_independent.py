from pathlib import Path
from itertools import product
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();proof=D/'three_phase_diagonal_RIGHT_rail_forces_a_fifth_reader.md';assert sha(proof)=='5e59fc91558ad1427d7711ac1b7961017eb2bdbc304ee08de21ba9063153d9ae';J=json.loads((D/'check_three_phase_diagonal_RIGHT_rail.json').read_text())
H='NESW';vec={'N':1j,'E':1,'S':-1j,'W':-1};turn=lambda h,r:H[(H.index(h)+(1 if r%2==0 else-1))%4];ports=lambda w,d,out=False:[r for r,h in enumerate(w)if(turn(h,r)if out else h)==d]
rail={0j:'NSSN',1+1j:'NSN',2+2j:'NNN'};drift=-3-3j
assert not ports(rail[1+1j],'W',True)and len(ports(rail[0],'S'))==2
assert len(ports(rail[0],'W',True))==2 and 2+2j+drift==-1-1j and not ports(rail[2+2j],'S')
words=lambda ax:[''.join(s)for n in range(1,5)for s in product(ax,repeat=n)]
l0=[w for w in words('EW')if not ports(w,'W')and len(ports(w,'S',True))==2];l2=[w for w in words('EW')if len(ports(w,'W'))==2 and not ports(w,'S',True)];assert J['derived_helper_domains']=={'L0':l0,'L2':l2}
qq=[];routes=[]
for a,b,q in product(l0,l2,words('NS')):
 if len(ports(q,'N'))!=len(ports(b,'N',True))or len(ports(q,'E',True))!=len(ports(a,'E')):continue
 qq.append(dict(L0=a,L2=b,Q=q,N_in=len(ports(q,'N')),E_out=len(ports(q,'E',True))))
 field={0j:rail[0],-1+0j:b,-1+1j:q,1j:a};p=0j;r=2;route=[([0,0],2)]
 for i in range(4):
  h=turn(field[p][r],r);ordinal=ports(field[p],h,True).index(r);p+=vec[h];r=ports(field[p],h)[ordinal];route.append(([int(p.real),int(p.imag)],r))
 assert route==[([0,0],2),([-1,0],0),([-1,1],0),([0,1],0),([0,0],1)];routes.append(route)
assert qq==J['all_next_reader_count_completions']and len(qq)==2
assert all(z['actual_four_R_route']==[[q,r]for q,r in rt]for z,rt in zip(J['literal_rank_reversals'],routes))
w='SNNSN';assert len(ports(w,'N'))==len(ports(w,'E',True))==3 and ports(w,'N')[0]==1
out=dict(status='PASS exact full-drift three-phase RIGHT rail forces some displayed helper to exceed four reads',proof_sha256=sha(proof),checker_sha256=sha(D/'check_three_phase_diagonal_RIGHT_rail.py'),certificate_sha256=sha(D/'check_three_phase_diagonal_RIGHT_rail.json'),helper_domains={'L0':l0,'L2':l2},complete_next_helper_modes=qq,physical_routes=routes,analytic_review=['The crucial zero port is supplied by B+d=(-1,-1) using the stated FULL drift(-3,-3), not a primitive representative. All three named rail classes have complete histories, so no hidden edge arrivals are allowed.','If each displayed helper has at most four reads, its complete WHITE alternating inventory is exhaustively derived from physical incoming/outgoing counts. Odd and even helper endings are retained.','In both remaining Q modes every arrow is literal next-read first-edge ordinal, on the same physical unit square. F rank2 would reach F rank1 four updates later, contradicting actual chronological rank order without any period bound or exterior assumption.','Uncapped SNNSN satisfies the local counts but its firstN is L1, so the safe conclusion is that at least one of L0,L2,Q exceeds four. The five-read local counterprofile is not a completed rail/front. No general drift or one-flat exclusion follows.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))

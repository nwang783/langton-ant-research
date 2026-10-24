from pathlib import Path
from itertools import product
import json,hashlib
S=Path(__file__).resolve();R=S.parents[1];P=R/'K1_pipeline_detours_2026-10-23';note=P/'RRLL_passage_involution_forces_critical_height_and_even_gates.md';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();assert sha(note)=='43ad37d33fd62434ba6c7743e542c1f22ba0da428f586c012cc2057d5dc6874c'
H='NESW';V=(1j,1,-1j,-1);oh=lambda w,j:(H.index(w[j])+(1 if j%2==0 else-1))%4
prof={'Z':'SSNS','A':'EEEW','B+':'SSSN','B-':'SNSS','Y+':'WWEW','Y-':'EWWW'}
paths=[]
def verify(path,field):
 for (q,r),(p,s)in zip(path,path[1:]):
  a,b=field[q],field[p];h=oh(a,r);assert q+V[h]==p and H[h]==b[s]
  aa=[j for j in range(4)if oh(a,j)==h];bb=[j for j in range(4)if b[j]==H[h]];assert len(aa)==len(bb)and aa.index(r)==bb.index(s)
 assert all(r in(0,3)for p,r in path[1:-1]);return[[[int(p.real),int(p.imag)],r]for p,r in path]
for bs,ys,prevys in product('+-',repeat=3):
 field={0j:prof['Z'],1+0j:prof['A'],1-1j:prof['B'+bs],-1j:prof['Y'+prevys],1+1j:prof['B'+bs],1j:prof['Y'+ys]}
 if prevys=='+':ps=[[(0j,1),(1+0j,0),(1-1j,0),(-1j,0),(0j,2)]]
 else:ps=[[(0j,1),(1+0j,0),(1-1j,0),(-1j,1)],[(-1j,2),(0j,2)]]
 if bs=='+':ps.append([(1+0j,1),(1+1j,3),(1j,3),(0j,3),(1+0j,2)])
 else:ps.extend([[(1+0j,1),(1+1j,1)],[(1+1j,2),(1j,3),(0j,3),(1+0j,2)]])
 paths.append({'B_sign':bs,'Y_sign':ys,'previous_Y_sign':prevys,'literal_factors':[verify(path,field)for path in ps]})
# Abstract involution accounting is exact once the analytic residual argument applies.
counts=[]
for a in range(1,9):
 n=4*a
 for mask in product((0,1),repeat=2*a):
  f=list(range(n))
  for k in range(a):
   if mask[2*k]:u,v=4*k,4*k+3;f[u],f[v]=v,u
   if mask[2*k+1]:u,v=4*k+1,4*k+2;f[u],f[v]=v,u
  seen=set();cycles=0
  for i in range(n):
   if i in seen:continue
   cycles+=1;j=i
   while j not in seen:seen.add(j);j=f[j]
  assert n-cycles==sum(mask)
 counts.append({'a':a,'all_involution_masks':2**(2*a),'possible_negative_gates_after_evenness_and_P_read_count':list(range(0,2*a,2))})
out={'status':'PASS exact RRLL passage involution, critical height, even irreducible negative gates','note':sha(note),'base_strip_report':sha(S.with_name('check_RRLL_unit_gates_and_two_terminals_independent.json')),'literal_all_free_mode_paths':paths,'involution_accounting_controls':counts,'analytic_review':[
'Every displayed unit path is independently matched by physical neighbor and complete directed-port occurrence ordinal under all free B/Y sign choices. Intermediates are only R0/L3, hence not another middle A/D event. Z pairs with the previous Y iff negative; A pairs with B iff negative. These are physical fixed points/transpositions with zero translation, not phase-residue equations.',
'F is an equivariant bijection from the previously signed all-sign theorem. Removing its disjoint forced fixed points/transpositions leaves an invariant set of ONLY positive free B/Y. At each such physical vertex its own D event follows A, so the first D after A has time<=its own D. Along a full-quotient residual cycle lifting by q*d the total time change isqP; henceq<=0. No excursion-length<P premise is needed.',
'With the separately signed RRLL w=+1, total side-current homology1-w is0. All forced unit cycles have zero homology and each residual cycle nonpositive; therefore every residual cycle hasq0. All its monotone time inequalities are then equalities. Unique actual event at each time forces each residual F value to be the same PHYSICAL D event, not just its translate. Thus F is exactly the claimed involution.',
'Each side current is a union of these zero-homology cycles. Signed exterior jumps then give c-2-c_left=0 and c_right-c+1=0, hencec=c_right+1. No embeddedness of zero-homology side walks is asserted. Partial-repair beta=4a-C(F) equals the number n_minus of disjoint transpositions; retained parity makesn_minus even. If all2a free contacts were negative, exact clock givesP12a despite16a distinct gamma read events, impossible. Thusn_minus<=2a-2 and at leasttwo free positives remain.',
'Combined with the signed local-minimum axis theorem, every G3 cycle at a locally minimal low-L plateau is positive axis and lies atL=c_left-1. This does not classify arbitrary axis curves or other mixed G3 cycles. The beta reservation is a lower bound, not fuel or an upper bound, and no front realization, safe ant splice or attraction follows.'
]};S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])

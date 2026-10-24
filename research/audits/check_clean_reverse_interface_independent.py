from pathlib import Path
Pth=Path(__file__).resolve();S=Pth.with_name('check_exceptional_return_map_independent.py');exec(compile(S.read_text().split('# A separate full-field')[0],str(S),'exec'))
Praw=shift(odd,-4*d);Craw=shift(cap,-4*d);M=stable^after;U=stable^Craw
assert len(stable)==2216 and len(M)==32 and len(U)==27
assert V==stable^shift(stable,-d)^M
assert W^shift(M,d)^Praw==U^shift(U,d)
J=json.loads((R/'clean_reverse_interface_identity.json').read_text());assert J['U_mass']==len(U) and list(map(tuple,J['U']))==sorted(map(xy,U)) and J['finite_coboundary_identity_exact']
# For finite truncations retain the exact endpoint term, never discard it until taking a pointwise limit.
checks=[]
for n in(0,1,2,17,73):
 lhs=U.copy();rhs=shift(U,n*d)
 for i in range(n):lhs^=shift(Praw,i*d);rhs^=shift(W,i*d)^shift(M,(i+1)*d)
 assert lhs==rhs;checks.append(n)
out=dict(status='PASS fresh complete-field finite coboundary and causal reverse-front interpretation',source_sha256=hashlib.sha256((R/'clean_reverse_interface_identity.md').read_bytes()).hexdigest(),complete_R_mass=len(stable),reverse_odd_read_mass=len(M),raw_C_mass=len(Craw),U_mass=len(U),U=sorted(map(xy,U)),finite_identity_checks=checks,scope='Exact identity only. Locally finite ray summation yields the old-side limit as actual finite discrepancy XOR original half-wake XOR shifted clean causal reverse104 front. No arbitrary-cap simplification of information, capture, rank or budget conclusion.')
Pth.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])

from pathlib import Path
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'three_F_backward_ancestry_interface_2026-10-24';ns={'__file__':str(SELF)};exec((SELF.parent/'check_foreign_kinked_barrier_turn_independent.py').read_text().split('geometries=[]')[0],ns);W,M,walk,xy=[ns[k]for k in['W','M','walk','xy']]
P=json.loads((R/'returned_D_last_C_parent_reduction_2026-10-24/D_last_C_parent_reduction.json').read_text())['fourteen_remaining_genuine_DC_VC_interfaces'];parents=[];pre=[]
for z in P:
 ix=z['catalogue_id'];run=z['actual_pre_D_zero_C_word'];p=complex(*z['packet_entry'][:2]);h=z['packet_entry'][2];assert h==1;F=2-5j if ix==15 else 3-4j;ret=-1j if ix==15 else 1+0j;contact=-1-1j if ix==15 else 0j
 fp=(F-p)*1j;rp=(ret-p)*1j;qp=(contact-2*p)*1j;parents.append((ix,z['last_positive_C_full_packet'],run,xy(fp),0,xy(rp),2,xy(qp),4,2+len(run)))
 if not run:continue
 a=run[-1];pp=-1-1j if a=='D'else-1-3j;ff=F-pp;rr=ret-pp;qq=contact-2*pp
 near=ix==15 and a=='D';assert near==((ff,rr)==(3-4j,1+0j))
 if a=='D':assert qq==(1+1j if ix==15 else 2+2j)
 else:assert(ix,ff,rr,qq)==(15,3-2j,1+2j,1+5j)
 pre.append((ix,z['last_positive_C_full_packet'],run,a,xy(ff),xy(rr),xy(qq),near))
assert len(parents)==14 and len(pre)==12 and sum(z[-1]for z in pre)==6
DD=W['D']*2+M;DC=W['D']+W['C']+M;i=next(i for i,(a,b)in enumerate(zip(DD,DC))if a!=b);assert i==21 and(DD[i],DC[i])==('L','R');d=walk(W['D']*2);c=walk(W['D']+W['C']);assert(d['p'],d['h'])==(2+2j,0)and(c['p'],c['h'])==(1+2j,3)
def center(p,h):return 2*p+(-1-1j)*(-1j)**h
assert center(d['p'],d['h'])==center(c['p'],c['h'])==3+3j
A=json.loads((D/'backward_interface.json').read_text());mp=D/'manifest.json';mf=json.loads(mp.read_text());mh=hashlib.sha256(mp.read_bytes()).hexdigest();assert mh=='cd0f742e40b368939b5da769a272bedafe51a64a017a5da1fbe0cc15547e0ced'
for f in mf['files']:assert hashlib.sha256((D/f['file']).read_bytes()).hexdigest()==f['sha256']
for f,h in A['dependencies'].items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==h
out={'status':'PASS exact backward reanchor assessment, NOT a no-map or exclusion theorem','manifest_sha256':mh,'fresh14_positiveC_parent_rebasings':parents,'fresh12_immediate_N_predecessor_rebasings':pre,'DD_DC_first_mismatch':{'tick0':21,'actual':'L','hypothetical':'R','actual_owner':'following actual word tick1/read2','hypothetical_owner':'ownC-tail tick11/read12'},'analytic_review':[
'Every retained older DC/VC base has headingE and sourceclock-1. Normalizing it rotates foreignE toN, returnedW toS and changes sourceage3to4. The outgoing first-contact owner remains the actual laterD with atomic offset2+Nrunlength. Strictly earlier time is not a closed typed recurrence.',
'The six D15 precedingD near-matches reproduce C75 head poses, but contact is olderD END, whose actual outgoing atom is laterD. That older packet is plainD in a zero-C N-run, not a DC source with C1. SubstitutingC changes actual read21, physical head/heading, fine length and Cclock despite identical corrected endpoints.',
'D30 precedingD rebase puts contact at laterD midpoint beyond olderD END; D15 precedingV puts it at olderV END with outgoing laterD. Neither permits importing the older atom source-contact catalogue. All actual frame changes and normal increments are explicit.',
'This establishes failure only of the displayed direct reanchoring/substitution. It neither rules out a future enlarged history-preserving ancestry map nor excludes or attains any of the14 necessary interfaces.'
],'scope':mf['scope'],'dependencies':A['dependencies']}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])

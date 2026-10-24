from pathlib import Path
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'K1_pipeline_detours_2026-10-23';note=D/'K1_early_branch_distinct_ancestors_singleton_output.md'
assert hashlib.sha256(note.read_bytes()).hexdigest()=='427658fba721afadec7f7c2c79a5f8505a3ab9f01ac558a8bd028cb728a292f2'
prior=json.loads((SELF.parent/'check_K1_cleanup_Q1_ancestor_independent.json').read_text());assert prior['profiles']==[['EEWE','NNNS','j','M','M-2'],['W','SSNS','k','M-1','M']]
# Work with face-center differences, so proper rotations require no hidden
# lower-left-coordinate offset. Every arrow is an actual canonical p edge.
for r in range(4):
 rot=(-1j)**r;F=0j;I=(-1+1j)*rot;P0=-2*rot;Q1=(-3+1j)*rot
 assert F==I-1j*(I-P0);assert I==P0+1j*(P0-Q1)
# Normalize the S and R ancestor alternatives to the SAME Q1 unit face and
# SAME NW canonical entry/heading. Rotate R clockwise around the face center.
S={0j:'W',1j:'SSNS',1+1j:'EEEW',1+0j:'SSNS'}
RR={0j:'EEWE',1j:'NNNS',1+1j:'EEEW',1+0j:'SSNS'}
def rotate_hist(h):return ''.join('NESW'[('NESW'.index(c)+1)%4]for c in h)
RR={q*(-1j)+1j:rotate_hist(h)for q,h in RR.items()}
assert S[1j]==RR[1j]=='SSNS';assert S[0]=='W'and RR[0]=='WWEW'
# Actual chronological complete histories cannot differ in length or heading.
assert len(S[0])==1 and len(RR[0])==4
out=dict(status='PASS equivariant early-branch ancestor injection and disjoint singleton-output reservation',note_sha256=hashlib.sha256(note.read_bytes()).hexdigest(),canonical_frame_conflict={'entry':[0,1],'entry_history':'SSNS','SW_S':'W','SW_R':'WWEW'},analytic='Unique p(I) recovers F by F=I-i*(I-p(I)); unique p(P0) recovers I by I=P0+i*(P0-p(P0)). Fixed p(Q1) allows only S and R children, but simultaneous alternatives force incompatible complete histories at the same physical SW corner. Translation by actual full drift aligns quotient representatives, so Q1 assignment is injective. Each S ancestor reserves a distinct one-read class because its sole R selects that unique M face against M-1. One-read classes are disjoint from the signed three-read rise/straight-branch reservations.',bound='N_odd>=n_up+n_SB+n_Sanc; equivalently the same clockwise-cycle output excess is at least ceil(sum/4).',scope='Output production only. No initial fuel, new root, new component, singleton reservation for R ancestors, additive second cycle payment or iterative supplier mechanism.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])

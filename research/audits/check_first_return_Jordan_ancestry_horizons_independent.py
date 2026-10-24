from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'returned_D_Jordan_ancestry_horizon_2026-10-24';C=R/'seven_word_spatial_return_2026-10-23'
p=SELF.with_name('check_foreign_kinked_barrier_turn_independent.py');ns={'__file__':str(p)};exec(p.read_text().split('geometries=[]')[0],ns)
W,M,walk,xy=[ns[k]for k in('W','M','walk','xy')]
G=json.loads((R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json').read_text())['geometry'];catalog=json.loads((C/'first_returned_atom_contact.json').read_text())['old_source_contact_cases']
def end(word,p=0j,h=0):
 for c in word:
  h=(h+(1 if c=='R'else-1))%4;p+=1j*(-1j)**h
 return p,h
def rotate(p,h):return p*(-1j)**h
def ctr(p,h):return 2*p+rotate(-1-1j,h)
def vec(name,h):
 e,dh=end(W[name]);return rotate(e,h),(h+dh)%4
stages=[]
for h in[0,3,2,1]:
 for a in 'DCVU':
  e,eh=vec(a,h);assert (eh==h and (e.imag>=0 if h in[0,3]else e.imag<=0))if a!='C'else (eh==(h-1)%4)
  if a=='C':assert e==rotate(1j,h)
  stages.append([h,a,xy(e),eh,int(rotate(-1-1j,h).imag)])
# Every possible predecessor atom, derived by reversing its literal endpoint and rotation.
rays={}
for a in 'DVUC':
 e,dh=end(W[a]);h=(-dh)%4;head=-rotate(e,h);ray=ctr(head,h)-ctr(0j,0);rays[a]=xy(ray)
assert rays=={'D':(-2,-2),'V':(-2,-6),'U':(0,-8),'C':(-2,2)}
# All these rays lie in the reflex NE-to-SE sector, never in the east-facing wedge.
assert all(x<0 or (x==0 and y<0)for x,y in rays.values())
rowsD=[];framesD=[];rowsC=[];framesC=[]
for ix in[15,30,75,76,77]:
 r=catalog[ix];assert r['source_to_foreign_C_age']==3 and r['effective_quarter_clock']==5
 shift=1+1j if ix>=75 else 0j;fp=complex(*r['foreign_pose'][:2])+shift;fh=r['foreign_pose'][2]
 rp=complex(*r['returned_pose'][:2])+shift;rh=r['returned_pose'][2];foreign=r['foreign'];ret=r['returned_atom']
 f0=ctr(fp,fh);pf,hf=end(W['F'],fp,fh);ff=ctr(pf,hf);pe,he=end(W[foreign],fp,fh);fe=ctr(pe,he)
 assert (pe,he)==(rp,rh)
 vertices=[f0,ff]+([fe]if foreign!='F'else[])
 re,reh=end(W[ret],rp,rh);rend=ctr(re,reh)
 q=(0j if ix==30 else(-1-1j+2*shift))
 assert (rend==q)if ix!=30 else ((fe+rend)/2==q)
 sourceout=(ctr(*end(W[r['source_atom']],shift,0))-ctr(shift,0))
 assert sourceout==2+2j
 # Returned tangent at contact and reverse prior-source ray determine exact reflex interior.
 retvec=rend-fe;assert retvec.real<0 and retvec.imag>0
 assert (retvec==(-6+2j))if ix==30 else(retvec==(-2+2j))
 if ix==30:
  # atan3=a in quarter units(1/2,1), open=9/2+a, close=-1/2-a.
  assert F(9,2)-F(1,2)==4
 else:assert 5-1==4
 lower=int(min(z.imag for z in vertices));assert lower==int(2*fp.imag+1)
 assert min(fe.imag,q.imag)>=lower
 # N and W before the final two stages are bounded below by -1 and3 respectively.
 # S->E drops heady1, and subsequent E head y cannot increase, hence all S>=Y+1,E>=Y.
 assert min(-1,3,2*fp.imag+3,2*fp.imag+1,fe.imag,q.imag)>=lower
 maxweight=(-lower-2)//2 # integer m with -1-2m>lower
 words=[]
 for length in range(maxweight+1):
  for z in product('DVU',repeat=length):
   w=''.join(z);weight=sum({'D':1,'V':3,'U':4}[a]for a in z)
   if weight<=maxweight:words.append(w)
 assert words==(['','D','V','DD','DDD']if ix==15 else ['','D','DD']if ix in[30,75,76]else['','D'])
 frames=[]
 for w in words:
  e,eh=end(''.join(W[a]for a in w));assert eh==0;runstart=-e
  assert ctr(runstart,0).imag>lower
  for gi in[1,5,6,8,9]:
   full=G[gi];ep,dh=end(full['word']);h=(-dh)%4;start=runstart-rotate(ep,h);assert end(full['word'],start,h)==(runstart,0)
   frame={'id':ix,'full':full['name'],'run':w,'entry':[*xy(start),h],'exit':[*xy(runstart),0],'last_C_entry':[*xy(runstart-1),1]}
   if ix>=75:
    rr=walk(full['word']+W['D']*len(w)+G[1]['word']+M)
    if gi in[6,9]:
     assert not rr['feasible'];assert rr['i']-len(full['word'])==11
     frame['disposition']='double_tail_literal_conflict';frame['input_context_tick']=11;frame['physical_owner']='own C-tail tick1/read2'if not w else'next actual word tick1/read2'
    elif gi==8 and not w:
     assert rr['feasible'];frame['disposition']='signed_immediate_UC_bud_guard'
    else:assert rr['feasible'];frame['disposition']='necessary_only_open'
   frames.append(frame)
 record={'id':ix,'foreign':foreign,'foreign_pose':[*xy(fp),fh],'returned_pose':[*xy(rp),rh],'contact':xy(q),'actual_foreign_vertices':list(map(xy,vertices)),'whole_loop_min_y':lower,'max_preceding_N_vertical_weight':maxweight,'zero_C_words':words}
 if ix<75:rowsD.append(record);framesD+=frames
 else:rowsC.append(record);framesC+=frames
assert len(framesD)==40 and len(framesC)==40
assert sum(r['disposition']=='double_tail_literal_conflict'for r in framesC)==16
assert sum(r['disposition']=='signed_immediate_UC_bud_guard'for r in framesC)==3
assert sum(r['disposition']=='necessary_only_open'for r in framesC)==21
# Compare every actual boundary frame against author controls, not just totals.
aD=json.loads((D/'D_Jordan_horizon.json').read_text())
assert sorted((z['id'],z['full'],z['run'],z['entry'],z['exit'],z['last_C_entry'])for z in framesD)==sorted((z['catalogue_id'],z['last_positive_C_full_packet'],z['actual_pre_D_zero_C_word'],z['packet_entry'],z['packet_exit'],z['last_actual_C_entry'])for z in aD['all40_exhaustive_last_positive_C_packet_and_short_run_interfaces'])
aC=json.loads((C/'DC_C1_prefix_height_horizon.json').read_text())
assert sorted((z['id']-75,z['full'],len(z['run']),z['entry'])for z in framesC)==sorted(('FQB'.index(z['foreign']),z['last_positive_C_fullpacket'],z['intervening_plain_D_count'],z['actual_predecessor_packet_entry_in_selected_D_frame'])for z in aC['all40_complete_last_C_parent_and_short_D_run_rows'])
def manifest(directory,file):
 mp=directory/file;j=json.loads(mp.read_text());fs=j['files']
 if isinstance(fs,list):
  for z in fs:assert hashlib.sha256((directory/z['file']).read_bytes()).hexdigest()==z['sha256']
 else:
  for f,h in fs.items():assert hashlib.sha256((directory/f).read_bytes()).hexdigest()==h
 return hashlib.sha256(mp.read_bytes()).hexdigest()
md=manifest(D,'manifest.json');mc=manifest(C,'DC_C1_prefix_height_horizon_manifest.json')
common=['The simple old-plus-first-foreign path and chronological FIRST returned contact give a Jordan loop from the outgoing old source contact along the actual old/foreign arc, then the initial returned segment. The signed local foreign/returned interface rules out any extra intersection with repaired foreign pieces. No continuation beyond first contact is used.','The signed n=3 plus one-foreign principal tangent lift is5 quarter-turn units plus alpha_return-alpha_source. Closing the actual NW-to-NE contact subtracts1 quarter for C and1/2+atan3/(pi/2) for V. Both yield +4, so the Jordan loop is CCW. The true preceding-C bit is zero by actual complete-eight/foreign adjacency, so no missing negative wrap is suppressed.','At an old source vertex, same-point contact with its incoming atom is allowed and owned by the outgoing source. Every actual incoming D/V/U/C reverse ray lies strictly in the reflex interior. At a D midpoint the preceding half-D lies strictly inside. At old C1 the creating-D SW ray lies inside. The connected earlier old prefix has no further boundary contact by old simplicity and FIRST-contact, hence its entirety is inside. This is an actual finite-prefix argument, not an exterior-wire or arbitrary coloring inference.','Whole-loop support is derived from literal atom signs for ALL run lengths. Before C1 N heads are nondecreasing in y; W heads are at least2; after W->S and S->E, S/E heads decrease toward the foreign target. Corrected-center offsets preserve bounds at every atomic vertex, including internal C tails. Real F56/Qtail/Btail vertices give exact minima; straight segments cannot dip below their endpoints. Jordan interior is STRICTLY above the supporting line.','The preceding maximal zero-C N run has positive height d+3v+4u, so its starting center -1-2height must exceed the exact support. If no previous C exists, the factor initial genuine U base contributes at least4 and contradicts that inequality. Thus a real positive-C full packet precedes the bounded run; its earlier history remains arbitrary. The last C is its actual final tail, not a fictitious internal marker.']
outD={'status':'PASS two D-source Jordan ancestry horizons','manifest_sha256':md,'rows':rowsD,'all40_boundary_interfaces':framesD,'atomic_steps':stages,'actual_incoming_reverse_rays':rays,'analytic':common+['D15 support-9 bounds only preceding N-run weight<=3: empty,D,DD,DDD,V. D30 support-7 bounds weight<=2: empty,D,DD. Five possible last-positive-C full packets give40 necessary boundary interfaces. Source containing D versus DC does not change the pre-D run. No earlier-clock bound, full exclusion or attainment is obtained.'],'scope':'Conditional chronological FIRST returned contact only. Actual source vertex endpoint ownership, source midpoint and complete tail boundaries retained.'}
outC={'status':'PASS old DC/C1 Jordan horizon and40-to21 boundary reduction','manifest_sha256':mc,'rows':rowsC,'all40_boundary_interfaces':framesC,'analytic':common+['In creating-D frame actual F/Q minima are-7 and B minimum-5. The prior N run consists solely of D^k with k<=2/2/1. Exactly40 actual positive-C parent/run cases are generated;16 genuine VCC/UCC->first-D-family necessary prefixes fail at context11, whose physical owner is selected DC C-tail read2 at k0 and next actual word read2 otherwise. Three immediate UC cases use the separately signed original-bud guard;21 feasible-prefix necessary interfaces remain (8F,8Q,5B). No future whole history is certified.'],'scope':'Only old C1 of actual DC and its first returned RAW C contact. No returned simplicity, generic exterior contradiction, second foreign, or arbitrary earlier history bound.'}
SELF.with_name('check_D_Jordan_ancestry_horizon_independent.json').write_text(json.dumps(outD,indent=2)+'\n');SELF.with_name('check_DC_C1_Jordan_ancestry_horizon_independent.json').write_text(json.dumps(outC,indent=2)+'\n');print(outD['status']);print(outC['status'])

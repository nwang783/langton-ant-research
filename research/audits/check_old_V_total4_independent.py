from pathlib import Path
from fractions import Fraction
from collections import Counter
import json,hashlib,math
R=Path('/workspace/shared/langton');S=Path(__file__);D=R/'old_V_all_tail_total4_r_FOREIGN_MISS_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(D/'manifest.json')=='bcda0612afb86085b5fdb3d77409f4de8f4dd89c6aed2a09c74770845b27d0a8'
for f,h in json.loads((D/'manifest.json').read_text())['files'].items():assert sha(D/f)==h
ref=json.loads((D/'V_K4.json').read_text())
for f,h in ref['dependencies'].items():assert sha(R/f)==h
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns)
W,M,K,tr,rot,center,xy,cross=[ns[x]for x in ['W','M','K','tr','rot','center','xy','cross']]
G={a:tr(W[a])for a in W};C={a:tr(W[a]+M)for a in W};I={a:{p for p,b in C[a]['req'].items()if b and p not in K}for a in W}
assert [len(I[a])for a in'DCVUFQB']==[1,0,2,5,14,15,18]
def po(p,h):return[*xy(p),h]
def ex(a,p,h):return p+rot(h)*G[a]['p'],(h+G[a]['h'])%4
def touch(a,p,h,tag,anyread=False):
 q=(tag-p)/rot(h)
 return q in K or(q in C[a]['req']if anyread else C[a]['req'].get(q)is False)
# Rebuild the two outgoing-owned rational contact boxes, not target-only tests.
angles=json.loads((R/'one_foreign_first_contact_compression_2026-10-24/first_contact_C_window.json').read_text())['all44_exact_source_target_C_window_rows']
vs=[x for x in angles if x['source_class']=='preFOREIGN_ordinary'and x['source_atom']=='V'];assert len(vs)==4
geos=[];boxes=[];a=center(0j,0);u=center(G['V']['p'],G['V']['h'])-a
for row in vs:
 if 4 not in row['allowed_C_counts_before_contact_ENTRY']:continue
 A=row['contact_atom'];c=center(0j,2);v=center(rot(2)*G[A]['p'],(2+G[A]['h'])%4)-c;den=cross(u,v);assert den
 corners=[(a+s*u-c-t*v)/2 for s in[0,1]for t in[0,1]]
 bounds=[(math.floor(min(p.real for p in corners)),math.ceil(max(p.real for p in corners))),(math.floor(min(p.imag for p in corners)),math.ceil(max(p.imag for p in corners)))]
 boxes.append((A,bounds))
 for x in range(bounds[0][0],bounds[0][1]+1):
  for y in range(bounds[1][0],bounds[1][1]+1):
   if(x+y+2)%2:continue
   q=c+2*complex(x,y)-a;s=Fraction(cross(q,v),den);t=Fraction(cross(q,u),den)
   if 0<=s<1 and 0<t<=1:geos.append((A,x,y,2,str(s),str(t)))
assert geos==[(r['actor'],*r['ENTRY'],r['old_source_outgoing_s'],r['new_positive_t'])for r in ref['all2_outgoing_owned_K4_target_geometries']]
field={0j,1+0j,2+0j,2+1j,2+2j};births=[]
for src in ['V','VC','VCC']:
 z=tr(''.join(W[a]for a in src));ek={z['p']+rot(z['h'])*k for k in K}
 for tag in field:assert z['last'][tag]==G['V']['last'][tag] and z['last'][tag][0]=='R'and tag not in ek
 assert z['last'][-1-1j]==('L',2);births.append((src,[(xy(q),z['last'][q])for q in sorted(field,key=lambda p:(p.real,p.imag))]))
def NW(p):
 x,y=map(int,(p.real,p.imag));ans=[];Y=y-4
 # Every coefficient in the y equation is nonnegative. W-U is solved exactly.
 for dn in range(max(0,Y+1)):
  for vn in range(max(0,Y//3+1)):
   for un in range(max(0,Y//4+1)):
    rem=Y-dn-3*vn-4*un
    for vw in range(max(0,rem+1)):
     dw=rem-vw;num=1+dn+vn-dw-3*vw-x
     if num>=0 and num%4==0:ans.append(dict(N_D=dn,N_V=vn,N_U=un,W_D=dw,W_V=vw,W_U=num//4))
 return ans
rows=[];kept=[];count=Counter();models=[]
for n in range(5):
 h=(-n)%4
 for A in 'FQB':
  for slot in sorted(I[A],key=lambda p:(p.real,p.imag)):
   p=-rot(h)*slot;e,eh=ex(A,p,h)
   if(int(p.real+p.imag)+h)%2:typ='sector'
   elif n==0:assert p.imag<=3 and(p.imag<3 or p.real!=1);typ='N0'
   elif n==1:
    ms=NW(p)
    if ms:
     assert len(ms)==1
     if p==2+5j:assert ms==[dict(N_D=1,N_V=0,N_U=0,W_D=0,W_V=0,W_U=0)];assert tr(W['D']+W['C']+W[A]+M)['bad'];typ='DCFORE'
     else:assert(A,p)==('Q',-3+4j)and ms==[dict(N_D=0,N_V=0,N_U=0,W_D=0,W_V=0,W_U=1)];assert tr(W['C']+W['U']+W['Q']+M)['bad'];typ='CU'
     models.append((A,po(p,h),ms))
    else:typ='noNW'
   elif n==2:
    if any(touch(A,p,h,q)for q in field):typ='held'
    else:
     kept.append((A,po(p,h)))
     if p==-5+1j:typ='new39'
     elif p==-3+3j:typ='new36'
     else:assert A in'QB'and p==-4;typ='hole'
   elif n==3:assert eh==3 and e.real<=0;typ='futureW'
   else:assert eh==2 and e.imag<0;typ='futureS'
   rows.append((A,po(p,h),xy(slot),po(e,eh),typ));count[typ]+=1
assert len(rows)==235 and len(models)==4 and len(kept)==8
refrows={(r['FOREIGN'],tuple(r['ENTRY']),tuple(r['r_true_input'])):r for r in ref['all235_actual_FOREIGN_r_TRUE_input_roles']}
for A,p,slot,e,typ in rows:
 rr=refrows[(A,tuple(p),tuple(slot))];assert rr['actual_FOREIGN_RAW_EXIT']==e
 assert typ=='sector'if rr['route']=='sector'else typ!='sector'
 if typ!='sector' and p[2]==3 and rr['true_source_ENTRY_to_FOREIGN_ENTRY_C_age']==1:assert NW(complex(*p[:2]))==rr['all_exact_N_C_W_endpoint_count_models']
assert sorted((a,tuple(p))for a,p in kept)==sorted((r['FOREIGN'],tuple(r['ENTRY']))for r in ref['all8_n2_source_field_compatible_FOREIGN_r_retirement_rows'])
# Every possible ordinary new-tag current loss, including marker inputs.
new=[];srows=[]
for ap,slot,tick,tag in[(-5+1j,-4+1j,39,-1+0j),(-3+3j,-4+2j,36,1+1j)]:
 for A in 'FQB':
  e,eh=ex(A,ap,2);ek={G[A]['p']+rot(G[A]['h'])*k for k in K}
  assert ap-slot==tag and G[A]['last'][slot]==('R',tick)and slot not in ek and eh==0
  assert e.imag>tag.imag-1 and e.imag+1>tag.imag+1
  for reader in'DVU':
   assert all(q.imag>=1 for q in I[reader]);assert all(q.real>=-1 for q in I[reader])
  assert(tag-0j)/rot(2)in K;new.append((A,po(ap,2),xy(tag),tick,po(e,eh)))
 for A in 'DVU':
  for q in I[A]:
   p=tag+q;e,eh=ex(A,p,2);assert eh==2
   # zero-S vector is (-D-V,-D-3V-4U).
   poss=[]
   for v in range(max(0,int(e.real)+1)):
    d=int(e.real)-v;rem=int(e.imag)-d-3*v
    if rem>=0 and rem%4==0:poss.append((d,v,rem//4))
   assert not poss;srows.append((xy(tag),A,po(p,2),po(e,eh)))
assert len(new)==6 and len(srows)==16
# C has zero external input: 3 external exit-K sites first R, 2 already entry-K first L.
cg=G['C'];ek={cg['p']+rot(cg['h'])*k for k in K};assert len(ek-K)==3 and len(ek&K)==2
assert all(cg['req'][q]is False for q in ek-K)and all(cg['req'][q]is True for q in ek&K)
# Earliest post-source RAW-END BLACK at g, explicitly allowing CORE final R writes.
g=-1-1j;hold={0j,1+0j,2+0j};orig=[];sur=[];oc=Counter()
for n in range(3):
 h=(-n)%4
 for A in 'DCVU':
  for q,(c,tick)in G[A]['last'].items():
   if c!='R':continue
   p=g-rot(h)*q;e,eh=ex(A,p,h)
   if(int(p.real+p.imag)+h)%2:typ='sector'
   elif G[A]['req'][q]:typ='earlierBLACK'
   elif any(touch(A,p,h,t,True)for t in hold):typ='held'
   else:
    sur.append((n,A,po(p,h),po(e,eh)))
    if n==0:assert p.imag<3;typ='N0'
    elif n==1:assert p.imag<4;typ='W1'
    elif A=='C':typ='completes3'
    else:assert e.imag<0;typ='S2'
   orig.append((n,A,po(p,h),xy(q),tick,po(e,eh),typ));oc[typ]+=1
assert len(orig)==108
rr={(r['preFOREIGN_ENTRY_clock'],r['writer'],tuple(r['ENTRY']),tuple(r['physical_final_R_slot'])):r for r in ref['all108_CORE_inclusive_preFOREIGN_physical_first_BLACK_hole_origins']}
for n,A,p,q,tick,e,typ in orig:
 z=rr[(n,A,tuple(p),tuple(q))];assert z['R_tick0']==tick and z['RAW_EXIT']==e
assert sorted((n,A,tuple(p),tuple(e))for n,A,p,e in sur)==sorted((r['preFOREIGN_ENTRY_clock'],r['writer'],tuple(r['ENTRY']),tuple(r['RAW_EXIT']))for r in ref['all_source_hole_origin_survivor_cuts'])
for A in'QB':assert C[A]['reads'][18][0]==(-3+1j)and C[A]['reads'][18][2]=='L'and C[A]['req'][-3+1j]and -4-(-3+1j)==g
for A,p in[('D',1+0j),('V',3+0j),('U',4+1j)]:assert ex(A,p,3)==(1j,3)
reg=[]
for r in ref['all2_structurally_chosen_failed_whole_prefix_return_regressions']:
 z=tr(''.join(W[a]for a in r['structurally_endpoint_chosen_whole_word'])+M);assert z['bad'];reg.append([*z['bad'][:2],xy(z['bad'][2]),z['bad'][3]])
review=[
'The old V source is a genuine pre-FIRST-FOREIGN V/VC/VCC in an actual U-entry G8 factor. Source r minimum5 and the n2 five-tag bounds are used ONLY before that foreign, including actual own-C tails. The signed 8d68 SAME-identity full-packet/internal-RAW lift is necessary for funding-cut CORE arguments.',
'Foreign TRUE inputs remain possible retirements until independently excluded; simultaneous held-tag inputs are not treated as color contradictions. Entry CORE and first-WHITE are the only five-tag field cuts. All235 true-input roles at n0..4 are rebuilt.',
'Age1 arithmetic is complete by the nonnegative y equation; the four solutions invoke actual DC-to-FOREIGN or CU conflicts, never an incorrect prepared RAW C-to-FOREIGN prohibition. n3/4 endpoint cuts preserve real marker ownership.',
'Six n2 rows use genuinely NEW foreign R39/R36 outputs. N/W support and all16 S marker-inclusive input exits exclude their first CURRENT loss before target. C cannot capture an external CURRENT tag because its three external EXIT-CORE sites first read WHITE; the remaining two are already ENTRY-CORE.',
'The hole proof starts strictly after executed source V L2. Earliest later BLACK RAW cut includes all108 physical final-R/CORE origins. An earlier first-L would require an earlier BLACK cut. Any independent anchor touch contradicts preforeign CURRENT, including marker-only CURRENT loss; physical death need not have happened at RAW exit. The only S2 births either complete at clock3 or exit below foreign y0.',
'Only after COMPLETE foreign MISS is established is conditional signed277 applied: any strictly earlier postforeign r loss has TOTAL K3 and exit(0,1,W). One remaining C forces negative x, incompatible with target D/C(0,0,S). Global-first simplicity licenses this earlier-loss application; no through-contact or arbitrary-tail simplicity follows.',
'Exact scope is only old-V TOTAL ordinary clock4. No A cleanup, beta, fixed-third mask, postforeign age or other total-clock closure is imported.'
]
out=dict(status='PASS scoped old-V arbitrary-ordinary-tail TOTAL4 foreign-MISS and closure',manifest=sha(D/'manifest.json'),geometries=geos,foreign_role_counts=dict(count),all235_roles=rows,new_foreign_tags=new,all16_S_loss_exits=srows,physical_hole_origin_counts=dict(oc),all108_physical_origins=orig,surviving_hole_origin_guards=sur,regression_first_conflicts=reg,analytic_review=review,dependencies=ref['dependencies'])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print('report',sha(S.with_suffix('.json')));print(count,oc)

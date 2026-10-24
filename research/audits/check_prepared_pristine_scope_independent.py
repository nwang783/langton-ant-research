from pathlib import Path
from fractions import Fraction as F
import hashlib,json
S=Path(__file__).resolve();R=S.parents[1];P=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();read=lambda p:json.loads(p.read_text());m=read(P/'PREPARED_PRISTINE_RECORD_SCOPE_MANIFEST.json')
for p,h in m.items():assert sha(P/p)==h
assert m['PREPARED_FAMILIES_PRISTINE_RECORD_SCOPE.md']=='bf0e6cd94644faf22eab7c2057641309fdf47287d7075a59bf29b1b577898f4c'
ref=read(P/'PREPARED_PRISTINE_RECORD_SCOPE_CHECKED.json');J=read(R/'causal_reduction/unit_scale/prepared1564_uniform_support_manifest.json');V=(1j,1,-1j,-1)
def geom(w,h,p=0j):
 q=[]
 for c in w:q.append(p);h=(h+(1 if c=='R'else -1))%4;p+=V[h]
 return q,p,h
def dot(q,n):return int(q.real)*n[0]+int(q.imag)*n[1]
def val(a,N):return a[0]*N+a[1]
def intersect(a,b):
 if a is None or b is None:return None
 lo=max(a[0],b[0]);hi=b[1]if a[1]is None else a[1]if b[1]is None else min(a[1],b[1]);return None if hi is not None and lo>hi else(lo,hi)
def positive_domain(a,b,lo=1):
 # Exact integers N>=lo satisfying a*N+b>=0.
 if a==0:return (lo,None)if b>=0 else None
 if a>0:return(max(lo,-((-(-b))//a)),None)
 hi=(-b)//a;return(lo,hi)if hi>=lo else None
def equality(a,b):
 if a==0:return(1,None)if b==0 else None
 x=F(-b,a);return(int(x),int(x))if x.denominator==1 and x>=1 else None
# Independent general two-coordinate affine encounter solver. All eight supplied witness slopes
# happen to produce integer affine copy coefficients; nonintegral constants are excluded exactly.
wave=J['stages'][-1];wq,we,wh=geom(wave['word'],wave['heading'],-6-6j);dr=we+6+6j;assert dr==14+14j
witnesses=[]
for z in ref['wave184']:
 q=z['cell'];found=[]
 for si,s in enumerate(J['stages'][:-1]):
  rr,de,he=geom(s['word'],s['heading']);starts=[s['start_x_N_constant'],s['start_y_N_constant']];tm=s['start_time_N_constant'];cnt=s['count_N_constant']
  for phase,p in enumerate(rr):
   pos=[int(p.real),int(p.imag)];dv=[int(de.real),int(de.imag)]
   if s['kind']=='H':
    ax=next(i for i in(0,1)if dv[i]);other=1-ax;ja=F(q[ax][0]-starts[ax][0],dv[ax]);jb=F(q[ax][1]-starts[ax][1]-pos[ax],dv[ax]);assert ja.denominator==1
    if jb.denominator!=1:continue
    ja,jb=int(ja),int(jb);dom=equality(starts[other][0]+dv[other]*ja-q[other][0],starts[other][1]+pos[other]+dv[other]*jb-q[other][1]);dom=intersect(dom,positive_domain(ja,jb));dom=intersect(dom,positive_domain(cnt[0]-ja,cnt[1]-jb-1));clock=(tm[0]+len(rr)*ja,tm[1]+len(rr)*jb+phase)
   else:
    ja=jb=0;dom=intersect(equality(starts[0][0]-q[0][0],starts[0][1]+pos[0]-q[0][1]),equality(starts[1][0]-q[1][0],starts[1][1]+pos[1]-q[1][1]));clock=(tm[0],tm[1]+phase)
   if dom is not None:found.append(dict(stage=si,phase=phase,copy=(ja,jb),time=clock,domain=dom,turn=s['word'][phase]))
 assert len(found)==1 and found[0]['domain']==(1,None)and found[0]['turn']=='R'
 f=found[0];expected=z['last_read'];assert all(json.loads(json.dumps(f[k]))==expected[k]for k in f)
 n=z['normal'];a=dot(dr,n);mx=max(dot(p,n)for p in wq);maximum=(a,mx-a)if a>0 else(0,mx)
 # Final wave endpoint is also no farther than the same read-envelope.
 end=(a,dot(-6-6j,n));diff=(maximum[0]-end[0],maximum[1]-end[1]);assert diff[0]>=0 and val(diff,1)>=0
 bw=tuple(sum(q[j][u]*n[j]for j in(0,1))for u in(0,1));margin=(bw[0]-maximum[0],bw[1]-maximum[1]);assert margin[0]>=0 and val(margin,1)>0 and list(margin)==z['strict_margin']
 witnesses.append(dict(normal=n,unique_pre_wave_read=f,strict_projection_margin=margin))
# Independent complete182 reference and exact affine stage poses.
G={-1j,1+1j,2+2j,1+3j};B=set(G);p=0j;h=1;A=''
for t in range(182):
 c='L'if p in B else'R';A+=c;B.symmetric_difference_update({p});h=(h+(1 if c=='R'else -1))%4;p+=V[h]
assert(p,h)==(5+1j,1)
H=read(R/'recovered_bundle/ant_global/root/standard.json')['word'];assert len(H)==104
poses=[((0,0),(0,0),1),((2,-1),(2,0),0),((-2,0),(6,-4),3),((-10,5),(-2,0),2),((-6,0),(-6,8),1)];counts=[(1,-4),(2,-5),(4,-6),(2,-7),(3,-4)];parts=[61,71,61,71,14]
norms=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
results=[]
for si,((xa,xb),(ya,yb),heading)in enumerate(poses):
 qa,pa,ha=geom(A,heading);qh,ph,hh=geom(H,ha,pa);dd=ph-pa;assert hh==ha;ra,rb=counts[si];qp,pp,hp=geom(H[:parts[si]],ha,pa)
 ex=(xa+ra*int(dd.real),xb+rb*int(dd.real)+int(pp.real));ey=(ya+ra*int(dd.imag),yb+rb*int(dd.imag)+int(pp.imag))
 if si<4:assert(ex,ey,hp)==poses[si+1]
 else:assert(ex,ey,hp)==((0,0),(0,2),1)
 for n in norms:
  slope=dot(dd,n)
  if slope<=0:continue
  cert=next(z for z in ref['twenty_cell_forward_blockers']if z['stage']==si and z['normal']==list(n));w=cert['persistent_black_witness'];wa=complex(w[0][0],w[1][0]);wb=complex(w[0][1],w[1][1])
  if si<4:
   (nxa,nxb),(nya,nyb),nh=poses[si+1];assert wa==complex(nxa,nya)and wb-complex(nxb,nyb)in {g*(-1j)**(nh-1)for g in G}
  else:assert wa==0 and wb==2j
  margins=[]
  for points,j in((qa,(0,0)),(qh,(ra,rb-4))):
   # Last read copy of first R_i-3 periods is j=R_i-4. Positive slope bounds all earlier copies.
   for q in points:
    aa=complex(xa,ya)+j[0]*dd;bb=complex(xb,yb)+q+j[1]*dd;mf=(dot(wa-aa,n),dot(wb-bb,n));assert mf[0]>=0 and val(mf,10)>0;margins.append(mf)
  assert min(val(mf,10)for mf in margins)==cert['minimum_margin_at_k10'];assert list(map(list,margins))==cert['all_affine_margins'];results.append(dict(stage=si,normal=n,margin_min_k10=min(val(mf,10)for mf in margins),min_affine_slope=min(a for a,b in margins)))
assert len(results)==15
signed20=S.with_name('check_twenty_cell_sustained_cap_independent.json');s20=read(signed20);assert s20['note_sha256']=='45e327d689431f873fc791f5e3955edad080b8d7a6ed23a54232c06b9089e6de';assert s20['source_stage_separation_inequalities']==6832
bound=5*(182+104)+5*3*104+sum(parts)+775+104;assert bound==4147 and 8*bound==33176
clar=P/'DEFECT_SPLIT_TIMING_CLARIFICATION.md';assert sha(clar)=='4a1411fd70a6c709decee0b4a7acc10a62b4e2ee2c8760fc7a9c99437e1a50ee'
out=dict(status='PASS exact prepared-family pristine-record scope separation, not a universal record budget',note_sha256=m['PREPARED_FAMILIES_PRISTINE_RECORD_SCOPE.md'],source184_sha256=sha(R/'causal_reduction/unit_scale/prepared1564_uniform_support_manifest.json'),signed20_report_sha256=sha(signed20),all8_wave_blockers=witnesses,all15_feedback_blockers=results,guard_avoiding_time_cut_upper_bound=bound,direction_marked_upper_bound=8*bound,timing_clarification_sha256=sha(clar),analytic_review=[
'Fresh affine encounter reconstruction across all fifteen producer stages finds EXACTLY ONE universal last-R read for each supplied184 witness, not merely a sampled last writer. Every wave read and its terminal endpoint lies strictly behind that still-black cell in its assigned one of eight normals. Hence no pristine supporting half-plane in those eight directions during the entire N-period1564 wave. The rest of the184 trajectory is not counted.',
'The20 all-k execution and complete-field separation are bound to the signed6832-inequality source audit; every next-stage initial port remains current/unread through the preceding stage, and R60 remains current through stage4 endpoint e. Exact affine stage endpoints and fifteen strict blockers are rebuilt. For positive-drift normals the last copy of the first R_i-3 periods bounds all earlier reads; all margins are positive at k10 with nonnegative slopes.',
'For nonpositive drift normals, every later full or partial H phase is no farther than its first-period counterpart, so cannot be a strict historical record. This is a position-record argument, not a pristine/color claim. The union of first182+104 cuts and last3H+partial cuts per stage contains every possible pristine record before e. Windows are half-open update-index cut intervals; stage endpoints belong to the next window, avoiding an off-by-one omission.',
'Recovery [e,e+775) and the next104 cuts are allowed in full. Thereafter any strict record phase with positive projection must belong to the complete signed outward catalog for that rotated standard heading. Actual H future plus a fully pristine forward half-plane forces agreement on that phase exact old-side first-read guard. Thus such later pristine records are not guard-avoiding. Nonpositive normals have no new records after the allowed first period.',
'The loose uniform4147 time-cut/33176 direction-marked bound applies ONLY to the complete20 prepared family, and the zero-pristine wave claim ONLY to the184 wave. Neither proves a universal pristine-record budget or attraction; both original long-wait/resource countercontrols remain valid.',
'The separate defect-split timing clarification is bound:308/310 are chosen phase45 guard entries, while exact standard word/full-state onset is262/264. No earlier signed physical control is altered.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print('184',[(z['normal'],z['strict_projection_margin'])for z in witnesses]);print('20',len(results),'bound',bound)

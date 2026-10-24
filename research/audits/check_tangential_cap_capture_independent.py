from pathlib import Path
from itertools import product
import json,hashlib
S=Path(__file__);R=S.parent.parent;P=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=P/'TANGENTIAL_CAP_CAPTURE_MANIFEST.json';m=json.loads(mf.read_text())
for f,h in m['files'].items():assert sha(P/f)==h
assert m['files']['TANGENTIAL_CAP_CAPTURE.md']=='c29ebf3d6ab2b90c0d85c3dedc0a745147bb0d8bb4085f7d54299dbd21577ede'
z=json.loads((P/'TANGENTIAL_CAP_CAPTURE_CERTIFICATE.json').read_text());ref=json.loads((P/'TANGENTIAL_CAP_CAPTURE_CHECKED.json').read_text());V=(1j,1,-1j,-1);xy=lambda p:[int(p.real),int(p.imag)];cx=lambda p:complex(*p);cross=lambda p,q:int(p.real*q.imag-p.imag*q.real)
def mul(p,v):
 if cross(p,v):return None
 a,b=(int(p.real),int(v.real))if v.real else(int(p.imag),int(v.imag))
 return a//b if a%b==0 else None
def geom(w,p=0j,h=0):
 rr=[]
 for a in w:rr.append((p,h,a));h=(h+(1 if a=='R'else-1))%4;p+=V[h]
 return rr,p,h
def replay(B,p,h,w):
 B=set(B);rr,p,h=geom(w,p,h)
 for q,hh,a in rr:assert(q in B)==(a=='L');B.symmetric_difference_update({q})
 return B,p,h,rr
def tail(B,p,h,w):
 rr,end,eh=geom(w,p,h);d=end-p;assert len(w)==104 and eh==h and d!=0;tests=0
 for i,(q,hh,a)in enumerate(rr):
  toggles=[];changes={0}
  for j,(r,_,_)in enumerate(rr):
   k=mul(r-q,d)
   if k is not None and(k>0 or(k==0 and j<i)):toggles.append(k);changes.add(k)
  for b in B:
   k=mul(b-q,d)
   if k is not None and k>=0:changes|={k,k+1}
  for k in changes:assert((q+k*d in B)^(sum(l<=k for l in toggles)%2))==(a=='L');tests+=1
 return rr,d,tests
seed=set(map(cx,z['seed_six']));a0=cx(z['cap_base']);d=cx(z['wake_drift']);W,H,F,T=[z[k]for k in('launch_word','wake_word','common_post_contact_word','common_tail_word')];assert(len(seed),len(W),len(H),len(F),len(T))==(6,234,104,2184,104)
assert seed=={1j,2j,3j,2+4j,3+2j,3+3j} and a0==5-4j and z['initial_pose']==[[1,1],2]
E,p,h,launch=replay(seed,1+1j,2,W);Q,dd,tests=tail(E,p,h,H);assert len(E)==50 and d==dd==2-2j and Q[45][0]==a0 and H[45]=='R';M=set();P45=set()
for i,(q,hh,c)in enumerate(Q):M.symmetric_difference_update({q});P45.symmetric_difference_update({q})if i<45 else None
assert len(M)==32 and H.count('R')-H.count('L')==12
pref=[];hits=[]
for q,hh,c in launch:
 k=mul(q-a0,d)
 if k is not None:assert k<0;pref.append(k)
for i,(q,hh,c)in enumerate(Q):
 k=mul(a0-q,d)
 if k is not None:assert k>=0 and 104*k+i>=45;hits.append([i,k,104*k+i])
assert sorted(set(pref))==ref['prefix_cap_ray_indices']and hits==ref['cap_phase_hits']and min(r[2]for r in hits)==45
CF,en,eh=geom(F,0j,Q[45][1]);TF,te,th=geom(T,en,eh);td=te-en;assert(en,eh,td,th)==(6+14j,3,2+2j,3)
rays=[]
for name,points,lo in(('source',E,11),('wake',M,12)):
 for q in sorted(points,key=lambda q:(q.real,q.imag)):
  b=q-a0;u=-d
  for x,hh,c in CF:
   k=mul(x-b,u);assert k is None or k<lo
  den=cross(u,td);assert den!=0
  for x,hh,c in TF:
   delta=x-b;kn=cross(delta,td);jn=cross(delta,u)
   if kn%den or jn%den:continue
   k,j=kn//den,jn//den;assert k<lo or j<0
  rays.append({'cohort':name,'base':xy(b),'backward_parameter_min':lo})
assert rays==ref['all_K11plus']['complete_parameter_difference_rays']and len(rays)==82
controls=[];consumed11=None;records11=None;unread=None
for K,row in enumerate(z['finite_controls']):
 assert row['K']==K;a=a0+K*d;Tcontact=279+104*K;word=W+H*K+H[:45]+row['post_contact_word'];rr,end,ehh=geom(word,1+1j,2);B=seed|{a};birth={q:('initial',q)for q in B};cohort=None;cons=[];records=[];best=2
 for t,(q,hh,c)in enumerate(rr):
  if q.real+q.imag<best:
   best=int(q.real+q.imag)
   if all(b.real+b.imag>best for b in B):records.append((t,q,hh,best))
  if t==Tcontact:
   assert q==a and a in B;cohort=dict(birth);assert len(B)==58+12*K
   formula={0j}
   for e in E:formula.symmetric_difference_update({e-a0-K*d})
   for e in P45:formula.symmetric_difference_update({e-a0})
   for j in range(1,K+1):
    for e in M:formula.symmetric_difference_update({e-a0-j*d})
   assert formula=={b-a for b in B}
  assert(q in B)==(c=='L')
  if c=='L':
   old=birth.pop(q);B.remove(q)
   if cohort is not None and cohort.get(q)==old:cons.append((t-Tcontact,q-a,old))
  else:B.add(q);birth[q]=('R',t)
 assert B==set(map(cx,row['full_final_black']))and[xy(end),ehh]==row['final_pose']and len(word)==row['certificate_time'];tq,tdd,nt=tail(B,end,ehh,row['tail_word']);assert xy(tdd)==row['tail_drift'];controls.append({'K':K,'certificate_time':len(word),'delay':len(row['post_contact_word']),'mass':len(B),'tail_drift':xy(tdd),'tail_tests':nt})
 if K==11:
  assert row['post_contact_word']==F and row['tail_word']==T and end-a==en and ehh==eh and len(B)==356;assert len(cons)==113 and sum(old[0]=='R'for _,_,old in cons)==112 and cons[0]==(0,0j,('initial',a));assert min(old[1]-Tcontact for _,_,old in cons if old[0]=='R')==-910 and max(t for t,_,_ in cons)==1872
  unread={q for q,b in cohort.items()if birth.get(q)==b};assert len(unread)==77
  for b in unread:
   for q,hh,c in tq:assert(k:=mul(b-q,tdd))is None or k<0
  assert [v[3]for v in records]==list(range(0,-20,-1));records11=records;consumed11=cons;whole11=word+T*3
  for offset,relative,old in cons:
   if old[0]!='R':continue
   candidates=[]
   for i,(q,hh,c)in enumerate(Q):
    s=mul(a0+relative-q,d)
    if s is not None and(s<0 or s==0 and i<45):candidates.append((104*s+i-45,i,s))
   rel,i,s=max(candidates);assert 11+s>=0 and H[i]=='R'and rel==old[1]-Tcontact
# Whole future record geometry and explicit nonstandard words at every actual pristine SW record.
assert min([q.real+q.imag for q,_,_ in launch]+[q.real+q.imag for q,_,_ in Q]+[1+q.real+q.imag for q,_,_ in CF+TF])==-19
for t,q,h,lev in records11:
 for i in range(104):
  w=T[i:]+T[:i];assert any(whole11[t+j]!=w[j%104]for j in range(min(312,len(whole11)-t)))
assert max(c['delay']for c in controls)==2184 and 234+2184+375*2==3168
out={'status':'PASS all-K seven-cell tangential cap family captures, with complete field/lifetime and family-only pristine bounds','manifest_sha256':sha(mf),'dependencies':m['files'],'finite_full_controls':controls,'unread_all_parameter_rays':rays,'K11_contact_consumptions':[[t,xy(q),[o[0],o[1]if o[0]=='R'else xy(o[1])]]for t,q,o in consumed11],'record_levels':[r[3]for r in records11],'family_only_bad_pristine_timecuts':3168,'analytic_review':[
'The literal six-cell launch234,50-cell whole tail field and exact104 all-future parity are independently replayed. Every launch/cap-ray and tail/cap phase congruence is reconstructed, proving first unread initial cap at279+104K for ALL K>=0, not extrapolating finite tests.',
'At each of twelve anchor cuts the COMPLETE actual contact board equals {0} XOR shifted50-entry field XOR32 translated odd masks XOR the45-phase prefix. The formula follows directly by symmetric-difference evolution for every K. For K>=11 the difference from K11 is contained in50 rays with index>=11 and32 rays with index>=12; every one is independently disjoint from all2184 common reads AND all104 infinite final phase rays with exact nonnegative integer parameter signs.',
'Full future coupling uses only differences on never-read cells, retaining all old material. All K0..11 final fields/poses and infinite-tail parity checked. For K>=11 full postcontact word2184 and final drift2,2 transfer analytically; no minimal-onset claim.',
'The113 consumed contact identities are traced literally,112 genuinely wake-R-born and one original cap. Each consumed wake identity has an all-K last-prior-H R formula whose phase index remains nonnegative for K>=11; no earlier source/prefix birth can supersede it. Remaining cohort77 atK11 never touches the future tail, and parameter differences are unread, giving12K-55 unread forever and finalmass12K+224.',
'Tangential H preserves x+y; common final tail increases it. Complete launch/phase/common-prefix support gives minimum-19. Initial blacks all have level>=1 and cap at1 remains current before first lower crossing, so the20 levels0..-19 are genuine strict pristine SW records, not just head records. Every one fails all104 cyclic standard words by explicit finite differences.','All family histories consist of arbitrary pieces total<=234+2184 plus TWO standard-word pieces, so signed interior-record lemma gives3168 guard-avoiding pristine TIME cuts, or25344 directionmarked. This is only the exact seven-cell family, not arbitrary mass7 boards, a universal budget, noncapture or an attraction proof.'
]};S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S),sha(S.with_suffix('.json')))

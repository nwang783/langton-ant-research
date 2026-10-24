from pathlib import Path
import json,hashlib
S=Path(__file__);R=S.parent.parent;P=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=P/'TWO_TIP_CAP_CAPTURE_MANIFEST.json';m=json.loads(mf.read_text())
for f,h in m['files'].items():assert sha(P/f)==h
bp=S.with_name('check_tangential_cap_capture_independent.py');ns={'__file__':str(bp)};exec(bp.read_text().split('seed=set')[0],ns);geom,replay,tail,mul,cross,cx,xy=[ns[k]for k in('geom','replay','tail','mul','cross','cx','xy')]
z=json.loads((P/'TWO_TIP_CAP_CAPTURE_CERTIFICATE.json').read_text());base=json.loads((P/'TANGENTIAL_CAP_CAPTURE_CERTIFICATE.json').read_text());ref=json.loads((P/'TWO_TIP_CAP_CAPTURE_CHECKED.json').read_text());seed=set(map(cx,base['seed_six']));W,H=base['launch_word'],base['wake_word'];a0=5-4j;d=2-2j;E,p,h,launch=replay(seed,1+1j,2,W);Q,dd,tests=tail(E,p,h,H);assert dd==d;M=set()
for q,hh,ch in Q:M.symmetric_difference_update({q})
assert(len(E),len(M))==(50,32);seen=set();outputs=[];delays=[]
for block,stored in zip(z['variants'],ref['variants']):
 off=cx(block['offset']);assert off not in seen and off in(1,-1j,1+1j);seen.add(off);b0=a0+off
 for q,_,_ in launch:assert(k:=mul(q-b0,d))is None or k<0
 hits=[]
 for i,(q,_,_)in enumerate(Q):
  k=mul(b0-q,d)
  if k is not None:assert k>=0 and 104*k+i>45;hits.append(104*k+i)
 assert min(hits)=={1:60,-1j:46,1+1j:75}[off]==stored['first_unperturbed_second_cap_phase']
 controls=[]
 for k,row in enumerate(block['finite_controls']):
  assert row['K']==k;a=a0+k*d;b=a+off;initial=seed|{a,b};assert len(initial)==8;F,T=row['post_contact_word'],row['tail_word'];assert T in{H[i:]+H[:i]for i in range(104)};word=W+H*k+H[:45]+F;B,en,eh,rr=replay(initial,1+1j,2,word);contact=279+104*k
  assert rr[contact][0]==a and rr[contact][2]=='L'and all(q not in(a,b)for q,_,_ in rr[:contact]);assert B==set(map(cx,row['full_final_black']))and[xy(en),eh]==row['final_pose'];tq,td,nt=tail(B,en,eh,T);assert xy(td)==row['tail_drift'];delays.append(len(F));controls.append(dict(K=k,delay=len(F),full_mass=len(B),tail_tests=nt))
  if k!=11:continue
  CF,cp,ch=geom(F,0j,rr[contact][1]);TF,tp,th=geom(T,cp,ch);v=tp-cp;assert v==2+2j and th==ch
  checked=[]
  for name,pts,lo in(('source',E,11),('wake',M,12)):
   for q in pts:
    origin=q-a0;u=-d
    for x,_,_ in CF:assert(j:=mul(x-origin,u))is None or j<lo
    den=cross(u,v)
    for x,_,_ in TF:
     delta=x-origin;kn,jn=cross(delta,v),cross(delta,u)
     if kn%den or jn%den:continue
     kk,jj=kn//den,jn//den;assert kk<lo or jj<0
    checked.append((name,xy(origin),lo))
  assert len(checked)==82
  secondreads=[i for i,(q,_,_)in enumerate(CF)if q==off]
  for i,(q,_,_)in enumerate(TF):
   j=mul(off-q,v)
   if j is not None and j>=0:secondreads.append(len(F)+104*j+i)
  first=min(secondreads,default=None);assert first=={1:None,-1j:1857,1+1j:86}[off]
  assert (len(F),xy(cp),ch)=={1:(2184,[6,14],3),-1j:(2184,[6,12],3),1+1j:(2392,[8,16],3)}[off]
  assert min([q.real+q.imag for q,_,_ in launch+Q]+[1+q.real+q.imag for q,_,_ in CF+TF])==-19
  # Actual full-field pristine-record test, not a head-only minimum.
  live=set(initial);best=2;records=[]
  for t,(q,_,chh)in enumerate(rr):
   lev=int(q.real+q.imag)
   if lev<best:
    best=lev
    if all(x.real+x.imag>lev for x in live):records.append(lev)
   assert(q in live)==(chh=='L');live.symmetric_difference_update({q})
  assert records==list(range(-1 if off==-1j else 0,-20,-1));assert len(records)==stored['all_K11plus']['SW_pristine_record_cuts'];assert stored['all_K11plus']['normalized_final_pose']==[xy(cp),ch]
 outputs.append(dict(offset=xy(off),literal_controls=controls,all_parameter_difference_rays=len(checked),second_cap_first_read=first,K11_pristine_SW_levels=records))
assert seen=={1,-1j,1+1j}and len(delays)==36 and max(delays)==13104
out={'status':'PASS all-K capture for exactly three specified eight-cell two-tip cap families','manifest_sha256':sha(mf),'dependencies':m['files'],'variants':outputs,'family_only_bad_pristine_timecuts':234+13104+2*375,'analytic_review':['Both original cap cells lie outside every precontact launch/read ray. Complete independent replay of all36 K0..11 controls, every final black field/pose and exact infinite104 ray parity. Tail words are cyclic copies of the signed standard word, not merely arbitrary period104.','At main contact the full field is signed one-cap B_K XOR the fixed offset singleton. Thus the offset cancels from K-versus11 differences. All50 source rays(index>=11) and32 backward wake rays(index>=12) independently miss every finite continuation and every infinite final read ray for EACH variant. Exact integer intersection equations preserve nonnegative domains. This proves all K>=11 without discarding any archive.','Second cap is never read for east, read1857 for south, read86 for northeast, relative to the main actual L. All three initial caps are genuinely pre-funded unread inputs; south/northeast are productive, not decorative.','Full K11 board scans independently confirm20/19/20 pristine SW records and minimum-19; launch and tangent H preserve the all-K support argument, final drift raises x+y. Later translates cannot create lower records.','Maximum sufficient postcontact certificate delay13104 plus arbitrary launch234 and two standard pieces gives14088 guard-avoiding pristine TIME cuts only in these three exact families. No earliest-onset, all-two-cap classification, mass-only universal budget, recurrence, or attraction assertion.']};S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S),sha(S.with_suffix('.json')))

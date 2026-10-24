"""Four opposite pure interfaces and literal24-cell remote feedback, without cropping."""
from pathlib import Path
import json,hashlib
# Reuse only the already frozen arithmetic/parity definitions, not its executed suite.
exec(Path('check_transverse_first_contact_quotient.py').read_text().split('out=[];class_words={}')[0])
refs=json.loads((P/'OPPOSITE_TRANSVERSE_JOIN_PROBES.json').read_text())['records'];pure=json.loads((P/'PURE_OPPOSITE_INTERFACES_PROBES.json').read_text());diffs=json.loads((P/'IDEAL_OPPOSITE_TRANSVERSE_QUOTIENT_PROBES.json').read_text());clockwise=json.loads((P/'TRANSVERSE_FIRST_CONTACT_QUOTIENT_CHECKED.json').read_text())['controls'];outputs=[]
def phase_at_onset(certword,certcut,onset):
 sh=(onset-certcut)%104;return certword[sh:]+certword[:sh]
def relevant_at_entry(board,p,h,F,H,start):
 B=dict(board);deaths={};initial=set(B.values())
 for j,ch in enumerate(F+H*2):
  old=B.pop(p,None);assert(old is None)==(ch=='R')
  if old is None:B[p]=start+j;h=(h+1)%4
  else:deaths[old]=start+j;h=(h-1)%4
  p=add(p,DXY[h])
 w,dr,tail,tests=future(B,p,h);assert w==H
 deaths.update({i:start+len(F)+208+t for i,t in tail.items()})
 return {q for q,i in board.items()if i in deaths},deaths,tests
for ref,pr,di in zip(refs,pure,diffs):
 joins=ref['joins'];rvec=[100,30,150,60,100];poses=[((0,0),1)];entries=[0]
 for i,j in enumerate(joins):
  o,h=poses[-1];v=rot(add(Q[j],(2*rvec[i],2*rvec[i])),h-1);poses.append((add(o,v),(Qh[j]+h-1)%4));entries.append(entries[-1]+182+104*rvec[i]+j)
 seed={add(o,rot(g,h-1))for o,h in poses for g in G};assert len(seed)==24 and seed==set(map(tuple,ref['seed']))
 z,h5=poses[-1];assert h5==0;res=(sum(z)%4,(z[0]-z[1])%4);assert list(res)==pr['residue']
 contact=ref['first_contact'];c=contact['time'];q=tuple(contact['cell']);rr,phi=divmod(c-entries[-1]-182,104)
 hits=[]
 for i,v in enumerate(Q):
  v=add(z,rot(v,3))
  for wi,w in enumerate(W):
   delta=(w[0]-w[1])-(v[0]-v[1])
   if delta%4:continue
   j=delta//(-4);pt=add(v,(-2*j,2*j));dd=sub(pt,w)
   if dd[0]==dd[1] and dd[0]%2==0:hits.append(dict(time=104*j+i,phase=i,period=j,cell=pt,old_W_index=wi))
 hits.sort(key=lambda x:(x['time'],x['old_W_index']));assert hits[0]['time']==104*rr+phi and tuple(hits[0]['cell'])==q
 fringe=set(C)
 for v in Q[:phi]:
  if v in fringe:fringe.remove(v)
  else:fringe.add(v)
 finite={add(add(z,(-2*rr,2*rr)),rot(v,3))for v in fringe};generators=[(w,(2,2),None)for w in W]+[(add(z,rot(w,3)),(-2,2),rr-1)for w in W]
 def ideal_initial(p):
  b=p in finite
  for a,v,bound in generators:
   dx,dy=sub(p,a)
   if dx%v[0]==0 and dy==(dx//v[0])*v[1]and(bound is None or dx//v[0]<=bound):b=not b
  return b
 # Exact complete pure model future.
 PF=pr['transient'];PH=phase_at_onset(pr['tail'],pr['cut'],pr['exact_onset']);assert len(PF)==pr['exact_onset'];pp=q;hh=0;changes=set()
 for t,ch in enumerate(PF):
  b=ideal_initial(pp)^(pp in changes);assert b==(ch=='L')
  if pp in changes:changes.remove(pp)
  else:changes.add(pp)
  hh=(hh+(-1 if b else 1))%4;pp=add(pp,DXY[hh])
 pdr,ptests=infinite_tail(generators,finite^changes,pp,hh,PH);assert pdr==tuple(pr['drift'])and PF[-1]!=PH[-1]
 # The actual finite board, with ALL previously written loop strips.
 F=ref['contact_future_word'];H=phase_at_onset(ref['tail_word'],ref['certification_cut'],ref['exact_onset']);pre=''.join(A+U*rvec[i]+U[:j]for i,j in enumerate(joins));llen=c-len(pre);pre+=A+U*((llen-182)//104)+U[:(llen-182)%104];assert len(pre)==c
 actual=pre+F+H*2;B={v:-i-1 for i,v in enumerate(sorted(seed))};p=(0,0);h=1;first={};births={};deaths={};target_visits=[];Bcontact=None;Bdiff=None;firstdiff=None;cutposes={};idealword=PF+PH*((max(len(F),len(PF))-len(PF))//104+5)
 for t,ch in enumerate(actual):
  if list(p)==di['mismatch']['cell']:target_visits.append(t)
  if p in seed and p not in first:first[p]=t
  if t==c:Bcontact=dict(B);assert p==q and h==0 and B[p]==contact['lifetime']
  if t>=c and firstdiff is None and ch!=idealword[t-c]:
   firstdiff=dict(time=t,relative=t-c,cell=p,heading=h,actual=ch,ideal=idealword[t-c],current_lifetime=B.get(p),reads_through_discrepancy=list(target_visits));Bdiff=dict(B)
  if t in(c,c+len(PF),c+di['mismatch']['offset'],c+len(F)):cutposes[t]=[p,h]
  old=B.pop(p,None);assert(old is None)==(ch=='R')
  if old is None:B[p]=t;births[t]=p;h=(h+1)%4
  else:deaths[old]=t;h=(h-1)%4
  p=add(p,DXY[h])
 fw,fd,tail,tests=future(B,p,h);assert fw==H;deaths.update({i:len(actual)+t for i,t in tail.items()})
 for i,(o,hh0)in enumerate(poses):
  for g in G:assert first[add(o,rot(g,hh0-1))]==entries[i]+firstG[g]
 assert max(first.values())<c and firstdiff['relative']==di['mismatch']['offset']
 assert list(firstdiff['cell'])==di['mismatch']['cell']and firstdiff['actual']==di['mismatch']['expected']and firstdiff['ideal']==di['mismatch']['actual']
 Cr1={v for v,i in Bcontact.items()if i in deaths};Cr2={v for v,i in Bdiff.items()if i in deaths}
 item=dict(joins=joins,residue=res,initial_black=sorted(seed),poses=poses,port_entries=entries,all_initial_first_reads=[dict(cell=v,time=first[v])for v in sorted(seed)],last_initial_read=max(first.values()),first_contact=contact,old_phase=src['W'][hits[0]['old_W_index']]['phase'],incoming_phase=phi,all_past_first_hits=hits,pure_generators=generators,pure_finite=sorted(finite),pure_transient=PF,pure_word=PH,pure_exact_delay=len(PF),pure_tail_pose=[pp,hh],pure_tail_drift=pdr,pure_ray_tests=ptests,actual_transient=F,actual_word=H,actual_exact_delay=len(F),actual_exact_onset=c+len(F),actual_tail_drift=fd,first_discrepancy=firstdiff,first_contact_full=[dict(cell=v,lifetime=i,death=deaths.get(i))for v,i in sorted(Bcontact.items())],first_contact_relevant=sorted(Cr1),discrepancy_full=[dict(cell=v,lifetime=i,death=deaths.get(i))for v,i in sorted(Bdiff.items())],discrepancy_relevant=sorted(Cr2),full_terminal_black=[dict(cell=v,lifetime=i,death=deaths.get(i))for v,i in sorted(B.items())],terminal_pose=[p,h],actual_full_future_ray_tests=tests,physical_updates=len(actual))
 if firstdiff['actual']=='L':
  identity=firstdiff['current_lifetime'];assert identity>=0 and identity<c and identity in Bcontact.values();bi=next(i for i in range(5)if entries[i]<=identity<entries[i+1]);assert bi==2
  item['feedback_lifetime']=dict(cell=firstdiff['cell'],birth=identity,death=firstdiff['time'],age=firstdiff['time']-identity,birth_stage=bi,already_black_at_first_contact=True)
  remain=F[firstdiff['relative']:];matches=[cw for cw in clockwise if cw['postcontact_word']==remain and cw['canonical_word']==H];assert matches
  cw=matches[0];assert firstdiff['heading']==0
  cb={tuple(v['cell']):v['lifetime']for v in cw['full_contact_black']};cq=tuple(cw['first_contact']['cell']);CC,cd,ct=relevant_at_entry(cb,cq,2,cw['postcontact_word'],cw['canonical_word'],cw['first_contact']['time'])
  normalized={sub(v,firstdiff['cell'])for v in Cr2};expectedC={rot(sub(v,cq),2)for v in CC};assert normalized==expectedC
  item['clockwise_second_interface']=dict(residue=cw['residue'],source_joins=cw['joins'],rotation=2,remaining_delay=len(remain),whole_relevant_mass=len(Cr2),whole_normalized_relevant=sorted(normalized),exact_word_match=True)
  assert firstdiff['relative']>len(PF);item['canonical_word_moves_before_feedback']=firstdiff['relative']-len(PF)
 else:
  assert firstdiff['actual']=='R'and firstdiff['ideal']=='L'
  assert firstdiff['reads_through_discrepancy']==[firstdiff['time']]
  assert firstdiff['cell']==add(z,rot((3,6),3))
  assert (3,6)==add(W[6],(-2,-2)) and src['W'][6]['phase']==89
  item['missing_ideal_input']=dict(incoming_source_cell=[3,6],ideal_W_phase=89,ideal_period=-1,actual_first_physical_read=firstdiff['time'],actual_initially_white=True)
 assert F[-1]!=H[-1]
 for preword,tailword in [(PF,PH),(F,H)]:
  joined=preword+tailword*2
  assert joined.find(A[:33])==-1
 item['no_encountered_G_prefix33_in_either_future']=True
 outputs.append(item)
 print(res,'pure',len(PF),'actual',len(F),'difference',firstdiff,'relevance',len(Cr1),len(Cr2),'feedback',item.get('feedback_lifetime'),'second',item.get('clockwise_second_interface',{}).get('remaining_delay'),flush=True)
report=dict(status='AUTHOR opposite quotient and actual remote-feedback certificates; independent audit requested',scope='Four pure opposite two-wake interfaces capture. Four literal24-cell histories reach them but later diverge because their complete archive differs; three consume genuine stage2 R lifetimes and then exactly enter signed clockwise source futures. No ideal-to-finite whole-future substitution, autonomous regeneration or all-parameter claim.',source_hashes={f:hashlib.sha256((P/f).read_bytes()).hexdigest()for f in ['OPPOSITE_TRANSVERSE_JOIN_PROBES.json','PURE_OPPOSITE_INTERFACES_PROBES.json','IDEAL_OPPOSITE_TRANSVERSE_QUOTIENT_PROBES.json','TRANSVERSE_FIRST_CONTACT_QUOTIENT_CHECKED.json']},controls=outputs)
(P/'OPPOSITE_TRANSVERSE_FEEDBACK_CHECKED.json').write_text(json.dumps(report,indent=2)+'\n')

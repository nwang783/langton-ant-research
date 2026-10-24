from pathlib import Path
from itertools import product
import hashlib,json
S=Path(__file__);R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'OPPOSITE_TRANSVERSE_FEEDBACK_MANIFEST.json';assert sha(MF)=='01b4c6f92822034907127a431c454d10eb991880dc4a571f7fc08b0f97ca9fa4'
for f,h in json.loads(MF.read_text())['files'].items():assert sha(D/f)==h
J=json.loads((D/'OPPOSITE_TRANSVERSE_FEEDBACK_CHECKED.json').read_text())
for f,h in J['source_hashes'].items():assert sha(D/f)==h
ns={'__file__':str(S.with_name('check_transverse_contact_quotient_independent.py'))};exec(Path(ns['__file__']).read_text().split('assert {tuple(r[\'joins\'])')[0],ns)
A,U,Q,W,C,G,firstG,heads,vec,xy,order,walk,ideal_tail,verify=[ns[k]for k in('A','U','Q','W','C','G','firstG','heads','vec','xy','order','walk','ideal_tail','verify')]
CW=json.loads((D/'TRANSVERSE_FIRST_CONTACT_QUOTIENT_CHECKED.json').read_text())['controls'];cwcache={}
def cwrelevant(cw):
 key=tuple(cw['residue'])
 if key in cwcache:return cwcache[key]
 B={complex(*r['cell']):r['lifetime']for r in cw['full_contact_black']};initial=dict(B);p=complex(*cw['first_contact']['cell']);h=2;dead=set();word=cw['postcontact_word']+cw['canonical_word']*2;ct=cw['first_contact']['time']
 for i,c in enumerate(word):
  assert(c=='L')==(p in B)
  if c=='L':dead.add(B.pop(p));h=(h-1)%4
  else:B[p]=ct+i;h=(h+1)%4
  p+=vec[h]
 hw,dr,tail,checks=verify(B,p,h);assert hw==cw['canonical_word'];dead|=set(tail);relevant={p for p,i in initial.items()if i in dead};cwcache[key]=relevant;return relevant
res=[];seen=set();total=0
assert {tuple(r['joins'])for r in J['controls']}=={(61,71,61,a,b)for a,b in product((61,71),repeat=2)}
for r in J['controls']:
 joins=r['joins'];periods=[100,30,150,60,100];poses=[(0j,1)];entries=[0]
 for j,k in zip(joins,periods):
  o,h=poses[-1];poses.append((o+(-1j)**(h-1)*(Q[j]+k*(2+2j)),(heads[j]+h-1)%4));entries.append(entries[-1]+182+104*k+j)
 seed={o+(-1j)**(h-1)*g for o,h in poses for g in G};assert len(seed)==24 and sorted(map(xy,seed))==r['initial_black'];assert [[xy(p),h]for p,h in poses]==r['poses']and entries==r['port_entries'];z,hh=poses[-1];assert hh==0;residue=(int(z.real+z.imag)%4,int(z.real-z.imag)%4);assert list(residue)==r['residue'];seen.add(residue)
 hits=[]
 for i,q in enumerate(Q):
  v=z+1j*q
  for wi,w in enumerate(W):
   delta=int(w.real-w.imag-v.real+v.imag)
   if delta%4:continue
   k=delta//(-4);p=v+k*(-2+2j);dd=p-w
   if dd.real==dd.imag and int(dd.real)%2==0:hits.append(dict(time=104*k+i,phase=i,period=k,cell=xy(p),old_W_index=wi))
 hits.sort(key=lambda v:(v['time'],v['old_W_index']));assert hits==r['all_past_first_hits'];hit=hits[0];kk,phi=hit['period'],hit['phase'];ct=entries[-1]+182+hit['time'];q=complex(*hit['cell']);assert ct==r['first_contact']['time']and phi==r['incoming_phase']and U[phi]=='R'
 fringe=set(C)
 for p in Q[:phi]:fringe.symmetric_difference_update({p})
 finite={z+kk*(-2+2j)+1j*p for p in fringe};gens=[(w,2+2j,None)for w in W]+[(z+1j*w,-2+2j,kk-1)for w in W];assert sorted(map(xy,finite))==r['pure_finite'];assert [[xy(a),xy(v),b]for a,v,b in gens]==r['pure_generators']
 def initial(p):
  bit=p in finite
  for a,v,bound in gens:
   dd=p-a
   if int(dd.real)%int(v.real):continue
   k=int(dd.real)//int(v.real)
   if dd==k*v and(bound is None or k<=bound):bit=not bit
  return bit
 PF,PH=r['pure_transient'],r['pure_word'];assert len(PF)==r['pure_exact_delay']and PF[-1]!=PH[-1];p=q;h=0;changes=set()
 for c in PF:
  bit=initial(p)^(p in changes);assert bit==(c=='L');changes.symmetric_difference_update({p});h=(h+(-1 if bit else 1))%4;p+=vec[h]
 assert [xy(p),h]==r['pure_tail_pose'];pdr,pt=ideal_tail(gens,finite^changes,p,h,PH);assert xy(pdr)==r['pure_tail_drift']
 pre=''.join(A+U*k+U[:j]for j,k in zip(joins,periods));assert len(pre)==entries[-1];l=ct-len(pre);pre+=A+U*((l-182)//104)+U[:(l-182)%104];assert len(pre)==ct
 F,H=r['actual_transient'],r['actual_word'];word=pre+F+H*2;assert F[-1]!=H[-1]and ct+len(F)==r['actual_exact_onset'];B={p:-i-1 for i,p in enumerate(sorted(seed,key=order))};p=0j;h=1;deaths={};births={};first={};firstdiff=None;snaps={};visited=set();target=complex(*r['first_discrepancy']['cell']);targetvisits=[]
 for t,c in enumerate(word):
  if p==target:targetvisits.append(t)
  if p in seed:first.setdefault(p,t)
  if t==ct:assert p==q and h==0 and B[p]==r['first_contact']['lifetime'];snaps['contact']=dict(B)
  if t>=ct and firstdiff is None:
   k=t-ct;ideal=PF[k]if k<len(PF)else PH[(k-len(PF))%104]
   if c!=ideal:
    firstdiff=dict(time=t,relative=k,cell=xy(p),heading=h,actual=c,ideal=ideal,current_lifetime=B.get(p),reads_through_discrepancy=targetvisits[:]);snaps['diff']=dict(B);assert firstdiff==r['first_discrepancy'];assert(p in visited)==(c=='L')
  visited.add(p);assert(c=='L')==(p in B),(residue,t)
  if c=='L':deaths[B.pop(p)]=t;h=(h-1)%4
  else:B[p]=t;births[t]=p;h=(h+1)%4
  p+=vec[h]
 assert len(word)==r['physical_updates'];total+=len(word);hw,dr,tail,checks=verify(B,p,h);assert hw==H and xy(dr)==r['actual_tail_drift'];deaths.update({i:len(word)+v for i,v in tail.items()});assert[xy(p),h]==r['terminal_pose']
 for label,key in [('contact','first_contact_full'),('diff','discrepancy_full'),('terminal','full_terminal_black')]:
  board=B if label=='terminal'else snaps[label];assert [dict(cell=xy(p),lifetime=i,death=deaths.get(i))for p,i in sorted(board.items(),key=lambda pi:order(pi[0]))]==r[key]
 for ei,(o,h0)in zip(entries,poses):
  for g in G:assert first[o+(-1j)**(h0-1)*g]==ei+firstG[g]
 assert max(first.values())==r['last_initial_read']<ct;assert all(i in deaths and deaths[i]<ct for i in range(-24,0));rels={key:{p for p,i in board.items()if i in deaths}for key,board in snaps.items()};assert sorted(map(xy,rels['contact']))==r['first_contact_relevant'];assert sorted(map(xy,rels['diff']))==r['discrepancy_relevant']
 if firstdiff['actual']=='L':
  ident=firstdiff['current_lifetime'];assert ident>=0 and ident in snaps['contact'].values()and births[ident]==target and deaths[ident]==firstdiff['time'];stage=next(i for i in range(5)if entries[i]<=ident<entries[i+1]);assert stage==2;assert r['feedback_lifetime']==dict(cell=xy(target),birth=ident,death=firstdiff['time'],age=firstdiff['time']-ident,birth_stage=2,already_black_at_first_contact=True)
  remain=F[firstdiff['relative']:];cw=next(c for c in CW if c['postcontact_word']==remain and c['canonical_word']==H);crel=cwrelevant(cw);cq=complex(*cw['first_contact']['cell']);norm={p-target for p in rels['diff']};assert norm=={-(p-cq)for p in crel};sc=r['clockwise_second_interface'];assert len(norm)==sc['whole_relevant_mass']and sorted(map(xy,norm))==sc['whole_normalized_relevant'];assert list(cw['residue'])==sc['residue']and len(remain)==sc['remaining_delay'];assert firstdiff['heading']==0;assert xy(dr)==[-a for a in cw['canonical_drift']];assert firstdiff['relative']-len(PF)==r['canonical_word_moves_before_feedback']
 else:
  assert firstdiff['actual']=='R'and firstdiff['ideal']=='L'and targetvisits[0]==firstdiff['time'];assert target==z+1j*(3+6j);assert W[5+8j]==89;assert target==z+1j*((5+8j)-(2+2j));assert firstdiff['current_lifetime']is None;contributors=[]
  for a,v,bound in gens:
   delta=target-a
   if int(delta.real)%int(v.real):continue
   k=int(delta.real)//int(v.real)
   if delta==k*v and(bound is None or k<=bound):contributors.append((a,v,k))
  assert target not in finite and contributors==[(z+1j*(5+8j),-2+2j,-1)]
 for f,w in[(PF,PH),(F,H)]:assert A[:33]not in f+w*2
 res.append(dict(residue=residue,first_contact=ct,pure_delay=len(PF),actual_onset=ct+len(F),first_discrepancy=firstdiff,full_relevant_sizes=[len(rels['contact']),len(rels['diff'])],second_source=r.get('clockwise_second_interface'),actual_reads=len(word),pure_checks=pt,finite_checks=checks));print(residue,'PASS',len(word),flush=True)
assert total==345102 and seen=={(1,1),(1,3),(3,1),(3,3)}
out=dict(status='PASS four pure opposite comparisons and four named full-field finite feedback circuits',manifest=sha(MF),script=sha(S),actual_reads=total,controls=res,analytic_scope=['The opposite slope uniquely fixes each integer incomingperiod from the full104x12 oldwake ray inventory; the globalminimum proves earliest contact, not a bounded past scan. All bi-infinite oldrays, half-infinite incomingrays and exact finite fringe are retained. Independent normal-coordinate ray intervals and parity breakpoints certify all four ideal infinite futures.','All four24-cell seeds and five-stage entries are independently reconstructed. Every actual update, whole first-contact/discrepancy/terminal board, lifetime birth/death, initial-port first read and final all-future parity are checked. All24 original lifetimes retire before first contact.','Three later discrepancies are real stage2 R-born BLACK inputs present already at first contact. The remaining complete word, heading and entire future-relevant contact set equal rotated signed clockwise sources, independently reconstructed from their full finite fields and all-future fates. Local window agreement alone is not used; all additional actual archive remains in the full future test.','The fourth discrepancy is an actual first-ever WHITE visit. Exactly one infinite-past comparison ray contributes a false BLACK bit: incoming W89 period-1. No actual black lifetime exists there. This is a missing-input branch, not an old-cohort consumption.','The canonical-looking pieces before feedback are not actual capture certificates. None of the consumed standalone-output bits was actually permanent in these whole finite futures. These four named circuits all capture; no all-parameter feedback, arbitrarily many stages, autonomous regeneration, or universal capture result follows.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))

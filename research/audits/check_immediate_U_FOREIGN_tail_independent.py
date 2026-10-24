from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'immediate_U_FOREIGN_ordinary_tail_simplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF).startswith('488cf215')
mf=json.loads(MF.read_text())
for f,h in mf['files'].items():assert sha(D/f)==h
for f,h in mf['dependencies'].items():assert sha(R/f)==h
ref=json.loads((D/'immediate_U_tail_join.json').read_text());assert ref['dependencies']==mf['dependencies']
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,rot,center,xy,cross,meet,pieces=[ns[k]for k in['W','M','K','tr','rot','center','xy','cross','meet','pieces']];V=(1j,1,-1j,-1)
def simple(seq):
 ps=pieces(seq);contacts=[]
 for j,(c,d)in enumerate(ps):
  for i,(a,b)in enumerate(ps[:j]):
   h=meet(a,b,c,d)
   if h is not None:assert j==i+1 and b==c and h[0]!='OVERLAP'and h==(1,0),(seq,i,j,h);contacts.append((i,j,str(h[0]),str(h[1])))
 return ps,contacts
local=[]
for A in'FQB':
 assert W[A][:11]==M;simple('U'+A)
 for b in'DCVU':
  ps,co=simple('U'+A+b);rr=next(z for z in ref['all12_foreign_firstordinary_local_pairs']if z['source_foreign']==A and z['first_ordinary']==b);assert [[xy(p),xy(q)]for p,q in ps]==[[z['a'],z['b']]for z in rr['pieces']];local.append((A,b,co))
joins=[]
for a in'DCVU':
 for b in'DCVU':
  ps=pieces(a+b);u=ps[0][1]-ps[0][0];v=ps[1][1]-ps[1][0];assert cross(u,v)!=0 or(u.real*v.real+u.imag*v.imag)>0;simple(a+b);joins.append((a,b,xy(u),xy(v)))
assert len(joins)==16
for a in'DCVUFQB':assert(W[a]+M)[:11]==M
assert len(W['D'])==10 and all((W['D']+W[a])[:11]==M for a in'DCVUFQB')and(W['D']+M)[:11]==M
controls=[]
for rr in ref['all9_complete_physical_positive_controls']:
 seq=rr['labels'];w=''.join(W[a]for a in seq)+M;tt=tr(w);assert tt['bad']is None;seed={p for p,b in tt['req'].items()if b};assert sorted(map(xy,seed))==rr['complete_seed'];B=set(seed);p=0j;h=0;reads=[];cuts=[];ends={};off=0
 for i,a in enumerate(seq):off+=len(W[a]);ends[off]=[i,a]
 for t,c in enumerate(w):
  assert(p in B)==(c=='L');B.symmetric_difference_update({p});reads.append(dict(tick0=t,cell=xy(p),turn=c));h=(h+(1 if c=='R'else-1))%4;p+=V[h]
  if t+1 in ends or t+1==len(w):cuts.append(dict(actual_read_count=t+1,boundary=ends.get(t+1),pose=[*xy(p),h],complete_BLACK=sorted(map(xy,B))))
 assert reads==rr['all_actual_reads']and cuts==rr['all_real_RAW_and_M_cuts'];ps,co=simple(seq);assert [[xy(p),xy(q)]for p,q in ps]==[[z['a'],z['b']]for z in rr['pieces']];controls.append(dict(labels=seq,seed_mass=len(seed),full_reads=len(w),all_full_cut_masses=[len(z['complete_BLACK'])for z in cuts],pieces=len(ps),legal_adjacent_contacts=co))
reports={f:json.loads((R/f).read_text())for f in mf['dependencies']if f.startswith('audits/')};assert all(z['status'].startswith('PASS')for z in reports.values())
review=[
'The selected initial actual plain U is itself a complete G8 factor with arbitrary complete prepared entry field. Actual following FOREIGN first11 supplies its real M. FIRST and GLOBAL first contact are relative to this selected factor, not to all earlier physical history, which is not drawn.',
'Every individual word/repaired FOREIGN piece is injective; the direct three initial prefixes,12 FOREIGN/b1 local joins and16 ordinary joins have only true endpoint adjacency and no reverse overlap. The Q-tail/U codirected point is retained.',
'If a later nonadjacent contact exists, chronological earliest ordinary actor and first positive onset have the earlier selected path simple by definition. New ENTRY repeats were already preceding executed END contacts. Old vertices belong to outgoing pieces: U EXIT belongs FOREIGN prefix, Q/B kink belongs tail, FOREIGN EXIT belongs b1 except its legitimate initial adjacency. No terminal or collinear loophole remains.',
'The unique preFOREIGN old atomic source is plain U, so signed907 exhausts that class; signed8da exhausts proper original FOREIGN pieces; signeda213 exhausts all postFOREIGN ordinary outgoing owners including EXIT aliases, leading CC and terminal DCC. Their SAME actual factor, real final M and stopped first-contact hypotheses agree. No old preFOREIGN D/C/V exclusion is required.',
'Any truncation at an earlier actor has a real M supplied by subsequent actual RAWs; D10 plus next actual firstL supplies the eleventh read, including when that L lies in the stipulated final M. The marker is NEVER drawn as a new D or asserted to supply a further complete word.',
'All nine complete positive fields and every RAW/M cut replay independently, including true terminal CC/DCC and VCCV erosion. The conclusion is only auxiliary OPEN proxy simplicity for actual U A ordinary*+M with one immediate first FOREIGN. Fine ant-path simplicity, output permanence, arbitrary G7 or secondFOREIGN composition do not follow.'
]
out=dict(status='PASS special immediate plain-U FIRST-FOREIGN arbitrary ordinary-tail proxy simplicity',manifest=sha(MF),local_pairs=local,ordinary_joins=joins,real_marker_providers=7,D10_spill_sources=8,full_positive_controls=controls,analytic_review=review,dependencies=mf['dependencies'])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))

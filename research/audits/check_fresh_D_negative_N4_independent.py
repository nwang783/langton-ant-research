from pathlib import Path
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'fresh_D_negative_N4_common_guard_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF).startswith('42f41838');mf=json.loads(MF.read_text())
for f,h in mf['files'].items():assert sha(D/f)==h
for f,h in mf['dependencies'].items():assert sha(R/f)==h
ref=json.loads((D/'negative_N4_common.json').read_text());assert ref['dependencies']==mf['dependencies']
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,rot,center,xy,meet,pieces=[ns[k]for k in['W','M','K','tr','rot','center','xy','meet','pieces']];V=(1j,1,-1j,-1);G={a:tr(W[a])for a in W};CTX={a:tr(W[a]+M)for a in W};ports=[]
for a in'DVU':
 for q,b in CTX[a]['req'].items():
  if not b or q in K:continue
  p=2-q;e=p+G[a]['p'];assert e.imag>=0;ports.append((a,xy(q),[*xy(p),0],[*xy(e),G[a]['h']]))
assert len(ports)==8
for a,q,p,e in ports:
 rr=next(x for x in ref['all8_marker_inclusive_N4_first_CURRENT_loss_ports']if x['first_CURRENT_loss_actor']==a and x['true_input']==q);assert rr['ENTRY']==p and rr['RAW_EXIT']==e
# A prior C cannot absorb an external CURRENT tag: no true input and the actual capture sites.
c=G['C'];ek={c['p']+rot(c['h'])*k for k in K};assert not [q for q,b in CTX['C']['req'].items()if b and q not in K];assert len(ek-K)==3 and all(c['req'][q]is False for q in ek-K);assert len(ek&K)==2 and all(c['req'][q]is True for q in ek&K)
old=json.loads((R/'original_F_piece_firstpost_DC_2026-10-24/F_piece_DC.json').read_text())['fresh_D_common_entry_reserve'];assert old==ref['source_only_retained_qualified_common_interface']
qualified=json.loads((R/'audits/check_F_DC_partial_qualification_independent.json').read_text());assert qualified['status'].startswith('PASS ONLY')and 'sourceD common reserve'in' '.join(qualified['analytic_review'])
r=ref['selected_actual_UQ_control'];seq=r['actual_complete_RAW_labels'];raw=''.join(W[a]for a in seq);actual=raw+W['C'][:12];assert len(raw)==558 and len(actual)==570 and actual[len(raw):len(raw)+11]==M;literal=tr(actual);assert literal['bad']is None
seed={complex(*q)for q in r['complete_seed']};assert len(seed)==80 and seed=={q for q,b in literal['req'].items()if b};B={q:['initial',xy(q)]for q in seed};p=0j;h=0;reads=[];cuts=[];end={};off=0;poses={0:(p,h)}
for i,a in enumerate(seq):off+=len(W[a]);end[off]=[i,a]
for t,c in enumerate(actual):
 oldid=B.get(p);assert (oldid is not None)==(c=='L');reads.append(dict(tick0=t,cell=xy(p),turn=c,prior_identity=oldid))
 if c=='L':del B[p]
 else:B[p]=['new_R',t]
 h=(h+(1 if c=='R'else-1))%4;p+=V[h];poses[t+1]=(p,h)
 if t+1 in end or t+1 in[569,570]:
  g=-9-3j;cuts.append(dict(actual_read_count=t+1,boundary=end.get(t+1),pose=[*xy(p),h],complete_BLACK=sorted(map(xy,B)),common_BLACK=g in B,common_identity=B.get(g),common_CURRENT=g in B and(g-p)/rot(h)not in K))
assert reads==r['all570_actual_reads']and cuts==r['all_completed_RAW_and_partial_cuts'];assert poses[122]==(-7-3j,2)and raw[122:132]==W['D']and seq[:6]=='UQDDDD';assert seq[6:].count('C')==4
p0,h0=poses[122];pt,ht=poses[558];assert((pt-p0)/rot(h0),(ht-h0)%4)==(2-2j,0);assert((-9-3j)-p0)/rot(h0)==2;assert CTX['C']['req'][2j]is False and CTX['C']['reads'][12][0]==2j
assert p==-9-3j and p in B and B[p]==['new_R',130];assert all(e['cell']!=[-9,-3]for e in reads[131:]);assert all(c['common_CURRENT']and c['common_identity']==['new_R',130]for c in cuts if c['boundary']and c['actual_read_count']>=132)
probe=tr(raw+W['C']+W['D']+W['U']+W['F']+M);assert probe['bad']==(570,130,-9-3j,'R')
ps=pieces(seq)
for j,(a,b)in enumerate(ps):
 for i,(c,d)in enumerate(ps[:j]):
  m=meet(c,d,a,b)
  assert m is None or(j==i+1 and m==(1,0))
out=dict(status='PASS qualified fresh-D N4 negative-y common reserve and genuine570-read control',manifest=sha(MF),all8_firstloss_ports=ports,control=dict(seed=80,actual_reads=570,source_ENTRY=122,birth=130,target_ENTRY=558,target_relative=[2,-2,0],first_failed_requested_read=570,whole_cut_masses=[(c['actual_read_count'],len(c['complete_BLACK']))for c in cuts]),analytic_review=[
'Only the separately retained fresh-D common-through-C3 sublemma of qualified45abc is imported. Original143d universal F-pair/full84 remains rejected. A real preceding seven-atom RAW and a simple executed ordinary source-prefix are essential; earlier FOREIGN before the fresh D is allowed, none after.',
'After the four ordinary turns, any earlier same-clock N4 loss must occur in a D/V/U base whose eight true external input/marker capture exits all have y>=0. Subsequent N bases increase y. A further C would change clock/heading and cannot precede the stipulated N4 negative-y cut.',
'C itself cannot silently capture a CURRENT external identity: I0, three external EXIT-CORE first-WHITE sites, and two already ENTRY-CORE sites exhaust the interface. Marker-only loss is counted at the actual earlier RAW exit, not delayed to its later physical L.',
'Full80-cell prelaid board and all570 actual reads/RAW and partial cuts reconstruct. Source fourth S-D has a real preceding D; actual source-entry clock to target is4, birth130 survives SAME/CURRENT, and candidate C5 ownR12 at570 requires WHITE at that cell. The real lastU M11 is supplied, but C5 is not completed.',
'Special signed488 applies to the actual UQ ordinary completed prefix+realM, supplying its simple-source premise without generalG7 or secondFOREIGN scope. Direct proxy intersections independently confirm the named control. No all-C5 family exclusion, physical termination or through-target persistence is inferred.'
],dependencies=mf['dependencies'])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))

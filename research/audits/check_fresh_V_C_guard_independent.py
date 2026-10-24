from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'fresh_V_C_port_endpoint_guard_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF).startswith('4f0ab145');mf=json.loads(MF.read_text())
for f,h in mf['files'].items():assert sha(D/f)==h
for f,h in mf['dependencies'].items():assert sha(R/f)==h
ref=json.loads((D/'fresh_V_C.json').read_text());assert ref['dependencies']==mf['dependencies']
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy,meet,pieces=[ns[k]for k in['W','M','K','tr','rot','xy','meet','pieces']];V=(1j,1,-1j,-1);G={a:tr(W[a])for a in W};CTX={a:tr(W[a]+M)for a in W};C=2+1j;held={0j,1+0j,C}
for q,t in[(0j,4),(1+0j,9),(C,7)]:assert G['V']['last'][q]==('R',t)and(q-G['V']['p'])/rot(G['V']['h'])not in K
rows=[];ct=Counter()
for h in range(4):
 for A in'DVU':
  for q,black in CTX[A]['req'].items():
   if not black or q in K:continue
   p=C-rot(h)*q;bad=[]
   for g in held:
    loc=(g-p)/rot(h);ff=next(([e[2],j]for j,e in enumerate(CTX[A]['reads'])if e[0]==loc),None)
    if loc in K or ff and ff[0]=='R':bad.append([xy(g),xy(loc),loc in K,ff])
   if(int(p.real+p.imag)+h)%2:route='sector'
   elif bad:route='held_field'
   elif h==0:assert p.imag<0;route='N0_below_actual_sourceV_EXIT_y3'
   else:assert h==3 and A=='U'and p==3+2j;route='W1_below_actual_minimum_head_y4'
   rr=next(z for z in ref['all32_early_first_C_CURRENT_loss_rows']if z['first_C_loss_actor']==A and z['clock_heading']==h and z['input']==xy(q));assert rr['route']==route and rr['ENTRY']==[*xy(p),h]
   tick=next(j for j,e in enumerate(CTX[A]['reads'])if e[0]==q);assert rr['actual_first_L']['context_tick0']==tick
   if route=='held_field':assert {str(z)for z in bad}=={str([z['SAME_held'],z['local'],z['reason']=='ENTRY_CORE',z['first']])for z in rr['held_r_B_first_C_conflicts']}
   rows.append([A,h,xy(q),[*xy(p),h],route]);ct[route]+=1
assert len(rows)==32 and ct==dict(sector=16,held_field=11,N0_below_actual_sourceV_EXIT_y3=4,W1_below_actual_minimum_head_y4=1)
ends=[]
for h in[0,3]:
 for A in'DVU':
  for q,b in CTX[A]['req'].items():
   if not b or q in K:continue
   p=C-rot(h)*q;e=p+rot(h)*G[A]['p'];assert e.imag>=1
   rr=next(z for z in ref['all16_N4_W5_first_loss_RAW_exit_bounds']if z['heading']==h and z['first_loss_actor']==A and z['input']==xy(q));assert rr['ENTRY']==[*xy(p),h]and rr['RAW_EXIT']==[*xy(e),(h+G[A]['h'])%4];ends.append([A,h,xy(q),xy(e)])
assert len(ends)==16
c=G['C'];ek={c['p']+rot(c['h'])*k for k in K};assert not[q for q,b in CTX['C']['req'].items()if b and q not in K];assert len(ek-K)==3 and all(c['req'][q]is False for q in ek-K)and len(ek&K)==2 and all(c['req'][q]is True for q in ek&K)
r=ref['actual_mixed_V_control'];labels=r['nominal_labels'];nominal=''.join(W[A]for A in labels)+M;assert tr(nominal)['bad']==(509,117,-7-4j,'R');actual=nominal[:509];trace=tr(actual);assert trace['bad']is None;seed={complex(*q)for q in r['complete_seed']};assert len(seed)==73 and seed=={q for q,b in trace['req'].items()if b};B={q:['initial',xy(q)]for q in seed};p=0j;h=0;reads=[];cuts=[];endsmap={};off=0;poses={0:(p,h)}
for i,A in enumerate(labels):
 off+=len(W[A])
 if off<=509:endsmap[off]=[i,A]
for t,c in enumerate(actual):
 assert(p in B)==(c=='L');old=B.get(p);reads.append(dict(tick0=t,cell=xy(p),turn=c,prior_identity=old))
 if c=='L':del B[p]
 else:B[p]=['new_R',t]
 h=(h+(1 if c=='R'else-1))%4;p+=V[h];poses[t+1]=(p,h)
 if t+1 in endsmap or t+1==509:
  n=t+1;cuts.append(dict(actual_read_count=n,boundary=endsmap.get(n),context_complete_marked_RAW_cut=n in endsmap and n+11<=509 and actual[n:n+11]==M,pose=[*xy(p),h],complete_BLACK=sorted(map(xy,B)),V_C_BLACK=-7-4j in B,V_C_identity=B.get(-7-4j),V_C_outside_actual_pose_CORE=(-7-4j-p)/rot(h)not in K))
assert reads==r['all509_actual_reads']and cuts==r['all_RAW_body_and_context_marked_cuts'];assert poses[110]==(-5-3j,2)and nominal[110:128]==W['V'];assert poses[493]==(-9-2j,1)and(poses[493][0]-poses[110][0])/rot(2)==4-1j;assert (-7-4j-poses[110][0])/rot(2)==C
assert B[-7-4j]==['new_R',117]and all(z['cell']!=[-7,-4]for z in reads[118:]);assert actual[493:504]==M and actual[493:503]==W['D']and actual[503:509]==W['U'][:6]
assert next(z for z in cuts if z['actual_read_count']==493)['context_complete_marked_RAW_cut'];assert not next(z for z in cuts if z['actual_read_count']==503)['context_complete_marked_RAW_cut']
assert CTX['D']['reads'][16][0]==2+2j and CTX['D']['reads'][16][2]=='R';assert 493+16==503+6==509 and p==-7-4j
# Verify only the actually marked prefix geometry, never the body-only D/U extension.
off=0;markedlabels=''
for A in labels:
 if off+len(W[A])>493:break
 markedlabels+=A;off+=len(W[A])
assert off==493 and markedlabels[-1]=='C';ps=pieces(markedlabels)
for j,(a,b)in enumerate(ps):
 for i,(c,d)in enumerate(ps[:j]):
  m=meet(c,d,a,b);assert m is None or(j==i+1 and m==(1,0))
out=dict(status='PASS fresh V C-tag throughC3 and late N4/W5 nonpositive-y reserve, with precise509-read partial control',manifest=sha(MF),script=sha(S),early_counts=dict(ct),all32_roles=rows,all16_late_exit_bounds=ends,actual_control=dict(seed=73,reads=509,source_entry=110,source_birth=117,last_context_marked_cut=493,body_only_D_exit=503,first_failed_requested_read=509,requested_D_context_tick=16,actual_U_tick=6),analytic_review=[
'Fresh SAME r throughC4 and B throughC3 are used only at a hypothetical first C loss no later thanC3. Exact32 roles give16sector,11 independently CURRENT CORE/WHITE conflicts,four negative N0 heads and one low W1 U. Actual creating V exits(1,3,N), so N0 is too low and the first W1 head is at leasty4. Simultaneous TRUE inputs are retained, not called intrinsic color failures.',
'BeyondC3 no further r/B persistence is imported. All eight N4 first-loss RAW exits have y>=1; remainingN cannot reach y<=0. To reachW5 after N4 requires the real C5 raisingy once, and W bases cannot lower it. All eight W5 first-loss exits also have y>=1. Marker absorption is counted at the real RAW exit, not postponed to physical deletion.',
'C has no external BLACK inputs. Its three external exitCORE sites are first-WHITE, while two other sites already belong to entryCORE; neither admits an external CURRENT identity without contradiction. Thus no silentC loss escapes the table.',
'The complete73-cell prelaid seed and every509 actual read, identity and full field independently replay. Fresh second S-facing V starts110 and C-tagR117 at(-7,-4) is untouched thereafter. Cut493 is genuinely marked because its M is actual D10 plus U firstL. It is W5(4,-1) relative to the source and carries the SAME CURRENT tag.',
'Physical D body ends503 but its own fullM is unavailable. Requested D context16 is exactly next actual U tick6/read7 at509 and fails on BLACK R117. The 509-read actual ant prefix remains legal; the next actual turn would be L. No D/U proxy, marked status, completedU or nextFOREIGN is inferred from the partial body.',
'Signed488 and direct rational geometry are applied only through the actual marked prefix endingC5 plus its realM. The portable theorem retains SIMPLE executed ordinary source-prefix and no FOREIGN after the freshV; earlier arbitrary history is allowed. No full-output seal, mixed-rail exhaustive C5 exclusion, secondFOREIGN transfer or capture follows.'
],dependencies=mf['dependencies'])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(MF));print(sha(S.with_suffix('.json')))

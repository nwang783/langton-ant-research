from pathlib import Path
import json,hashlib
P=Path(__file__).resolve();S=P.with_name('check_U1_young3_shadow_independent.py');exec(compile(S.read_text().split('rows=[];cases=[]')[0],str(S),'exec'))
B=ROOT/'core_periodicity_new/three_C_shadow_cone_frozen_20261023_1256';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['file']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_three_C_shadow_cone.json').read_text());r=1-1j;own=[];pred=[];effects=[]
assert all(not(z.real>=0 and z.imag>=1)for z in K)
for s in ids:
 assert r not in G[s][2]and r not in G[s][3]|G[s][4]
 se,sh=G[s][:2];cs=counts[s]
 assert sh==(-cs)%4
 if cs==0:assert sh==0 and se.imag>=1
 if cs==1:assert sh==3 and se.real<=1
 for z,bit in G[s][2].items():
  if z.real>=0 and z.imag>=1:
   pos=1-z.imag+(z.real-1)*1j;assert rotation(r-pos,-1)==z
   if bit:assert z in G[s][3]
   effects.append((s,xy(z),bit,(*xy(pos),1)))
 for p in ids:
  c=counts[p];ph=(-G[p][1])%4;pp=-rotation(G[p][0],ph)
  slots=[z for z in G[p][4]if pp+rotation(z,ph)==r];assert len(slots)==1
  if s==ids[0]:pred.append((p,(*xy(pp),ph),xy(slots[0]),c+3))
  for a in ids:
   for z in G[a][3]:
    for n in range(c+cs,c+4):
     rem=c+3-n
     if n<oldages[a,z]or counts[a]>rem:continue
     h=(c-n)%4;pos=r-rotation(z,h);end=pos+rotation(G[base[a]][0],h);before=n-c-cs
     if h==0:
      assert(c,n,cs,before)==(2,2,0,0)and pos==1-4j and se.imag>pos.imag
      reason='source-to-clearer zero-C north cone'
     elif h==3:
      assert n-c==1 and pos.real>=2 and pos.imag<=0
      if cs==0:assert before==1 and se.imag+1>pos.imag;reason='source-to-clearer one-C north/west cone'
      else:assert cs==1 and before==0 and pos.real>se.real;reason='source-to-clearer zero-C west cone'
     elif h==2:
      assert rem==1 and end.imag<=-1
      # Includes the consumer attached C, if any. One S->E C drops y one.
      assert end.imag-1<=-2;reason='postbase one-C south/east endpoint y<=-2'
     elif h==1:
      assert rem==0 and counts[a]==0 and end.real>=1;reason='postbase zero-C east endpoint x>=1'
     own.append(dict(predecessor=p,source=s,consumer=a,input=list(xy(z)),shadow_age_at_first_consumer=n,consumer_pose=[*xy(pos),h],base_endpoint=list(xy(end)),remaining_C=rem,reason=reason))
key=lambda q:(q['predecessor'],q['source'],q['consumer'],tuple(q['input']),q['shadow_age_at_first_consumer'])
AA={key(q):q for q in J['all_retirement_cases']};BB={key(q):q for q in own};assert AA.keys()==BB.keys()and len(BB)==1176
for k,q in BB.items():
 for field in('consumer_pose','base_endpoint','remaining_C'):assert q[field]==AA[k][field]
AE={(q['target_packet'],tuple(q['local_cell']),bool(q['before_black']),tuple(q['relative_B_pose']))for q in J['target_before_cell_consequences']};assert set(effects)==AE
assert sum(not e[2]for e in effects)==97 and sum(e[2]for e in effects)==14
for a in ids:assert G[a][2][1+1j]is False and G[a][2][2+1j]is False
result=dict(status='PASS independent universal three-C predecessor-shadow cone',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),predecessors=pred,retirement_cases=own,white_avoidances=97,black_origin_cases=14,scope='Noninitial marked A(0,0,N), later marked B(X<=0,Y>=-1,E), exact source-included/target-excluded three C. The preceding packet fresh residual(1,-1) remains current at age3+cP. No target/source old-input survival, funding or record premise; first-factor boundary exception is essential. No global confinement or capture.')
P.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print({k:v for k,v in result.items()if k!='retirement_cases'})

#!/usr/bin/env python3
"""Finite retained inverse-corner selector; no cap search, no launch inference from bulk only."""
from pathlib import Path
from collections import defaultdict,Counter
import json,runpy,time,hashlib
ROOT=Path(__file__).parent;C=runpy.run_path(str(ROOT/'certify_prepared_travelling_wave.py'));E=C['E'];N=json.loads((ROOT/'prepared_wave_five_band_normal_form.json').read_text());J=json.loads((ROOT/'prepared_travelling_wave_certificate.json').read_text());T=json.loads(Path('/workspace/shared/langton/causal_reduction/unit_scale/retained_inverse_corner_contracts.json').read_text());B={tuple(j)for j in N['full_black_orbit_profiles']};cap={tuple(q)for q in N['finite_XOR_cap']};V=E['V'];G=defaultdict(list);p=tuple(J['wave_pose'][0]);h=J['wave_pose'][1]
for i,ch in enumerate(J['word']):
 x,y=p;j=(x-y,x%14);G[j].append((x-x%14)//14);h=(h+(-1 if ch=='L'else 1))%4;v=V[h];p=(p[0]+v[0],p[1]+v[1])
G={j:min(v)for j,v in G.items()}
def future_read(q):
 x,y=q;j=(x-y,x%14);return j in G and(x-x%14)//14>=G[j]
def bulk(q):return(q[0]-q[1],q[0]%2)in B
def wavecolor(q):return bulk(q)^(q in cap)
def color(q,rows,F):return bulk(q)^(q in F)
C['cert_parallel'].__globals__['color']=color;I=T['I'];unique={}
for r in T['cases']:
 key=(r['inverse_word'],tuple(r['inverse_output_E_start'][0]),r['inverse_output_E_start'][1],tuple(r['inverse_output_E_end'][0]),r['inverse_output_E_end'][1]);unique.setdefault(key,r)
result=[];success=[];started=time.time()
for key,r in unique.items():
 hi=r['inverse_output_E_start'][1];D=tuple(r['inverse_output_E_end'][0]);assert r['inverse_output_E_start'][0]==[0,0]and r['inverse_output_E_end'][1]==1
 pp=(0,0);hh=hi
 for ch in I:
  hh=(hh+(-1 if ch=='L'else 1))%4;v=V[hh];pp=(pp[0]+v[0],pp[1]+v[1])
 fi=pp;assert hh==hi and fi[0]==-fi[1]
 prefix=I*30+r['inverse_word']
 for residue in range(7):
  n=105+residue;qout=(-14+2*n,-16+2*n);tr=(qout[0]-D[0],qout[1]-D[1]);q=(tr[0]-30*fi[0],tr[1]-30*fi[1]);start=q;h=hi;seen={};flip=set();bad=None
  for k,ch in enumerate(prefix):
   want=ch=='L'
   if q in seen:
    if(seen[q]^(q in flip))!=want:bad={'kind':'INTERNAL_ALTERNATION','at':k,'cell':q};break
   else:
    seen[q]=want
    if future_read(q)and wavecolor(q)!=want:bad={'kind':'FIXED_WAVE_COLOR','at':k,'cell':q,'required':ch,'actual_wave':'L'if wavecolor(q)else'R'};break
   E['toggle'](flip,q);h=(h+(-1 if want else 1))%4;v=V[h];q=(q[0]+v[0],q[1]+v[1])
  row={'source_index':r['index'],'source_signature':r['source_signature'],'wave_residue':residue,'output_I_pose':[list(qout),1],'input_I_pose':[list(start),hi],'status':None}
  if bad:row.update(status='REJECTED',conflict=bad);result.append(row);continue
  assert q==qout and h==1
  edits={q for q,w in seen.items()if wavecolor(q)!=w};F=cap^edits^flip
  # Exact inverse-H future-ray initial requirements.
  groups=defaultdict(list);pp=q;hh=h
  for i,ch in enumerate(I):
   x,y=pp;t=x-y;a=x%2;groups[t,a].append(((x-a)//2,i,ch,(a,a-t)));hh=(hh+(-1 if ch=='L'else 1))%4;v=V[hh];pp=(pp[0]+v[0],pp[1]+v[1])
  assert pp==(q[0]+2,q[1]+2)and hh==h
  mismatch=set()
  for j,g in groups.items():
   g.sort(key=lambda z:(-z[0],z[1]));mn=min(z[0]for z in g);mx=max(z[0]for z in g);cc=g[0][3]
   assert bulk(cc)==(g[0][2]=='L')
   for z in range(mn,mx):
    qq=(cc[0]+2*z,cc[1]+2*z);first=next(a for a in g if a[0]<=z)
    if color(qq,{},F)!=(first[2]=='L'):mismatch.add(qq)
   for qq in F:
    if(qq[0]-qq[1],qq[0]%2)==j and(qq[0]-cc[0])//2>=mx:mismatch.add(qq)
  blocked=[qq for qq in mismatch if qq in seen or future_read(qq)]
  if blocked:row.update(status='REJECTED',conflict={'kind':'TAIL_FIXED_OR_PREFIX','cells':sorted(blocked)})
  else:
   edits^=mismatch;F^=mismatch;cert=C['cert_parallel']({},F,q,h,I);assert cert;assert all(not future_read(qq)for qq in edits);row.update(status='COMPATIBLE_SUPPLIED_BRIDGE',initial_wave_XOR_edits=sorted(edits),certificate=cert);success.append(row)
  result.append(row)
report={'scope':'Fixed171 retainedinversecorner contracts, deduplicated byexactnormalizedword/poses; 30incomingI periods and seven mature1564 phases. No newcapscan. A compatiblebridge is not a connected launch until joining currentinversehead is checked; rejectedmaturephases do not classify near-kernel placements.','source_contract_sha256':hashlib.sha256(Path('/workspace/shared/langton/causal_reduction/unit_scale/retained_inverse_corner_contracts.json').read_bytes()).hexdigest(),'records':len(T['cases']),'distinct_normalized_contracts':len(unique),'outcomes':dict(Counter(x['status']for x in result)),'results':result,'successes':success,'elapsed_seconds':time.time()-started};(ROOT/'inverse_corner_wave_bridge_selector.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items()if k not in['results','successes']},indent=2));print('SUCCESSES',success)

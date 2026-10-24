#!/usr/bin/env python3
"""Independent causal-front first-read reconstruction of supplied inverse completion."""
from pathlib import Path
from collections import defaultdict
import json,runpy,hashlib
ROOT=Path(__file__).parent;C=runpy.run_path(str(ROOT/'certify_prepared_travelling_wave.py'));E=C['E'];A=json.loads(Path('/workspace/shared/langton/causal_reduction/unit_scale/LLR_inverse_completion_certificate.json').read_text());N=json.loads((ROOT/'prepared_wave_five_band_normal_form.json').read_text());J=json.loads((ROOT/'prepared_travelling_wave_certificate.json').read_text());BULK={tuple(j)for j in N['full_black_orbit_profiles']};FWD={j for j in BULK if -28<=j[0]<=-18};LAST={(t+26,a)for t,a in FWD};OTHER=BULK-LAST;start=tuple(A['forward_entry_pose'][0]);h0=A['forward_entry_pose'][1];phase=55;tr=(0,-26);ref=(E['PH'][phase][0]+tr[0],E['PH'][phase][1]+tr[1]);copy=E['along'](start,ref,E['d']);assert copy is not None and E['HD'][phase]==h0;tau=phase+104*copy;rows=defaultdict(set);past={}
for i,q in enumerate(E['PH']):
 q=(q[0]+tr[0],q[1]+tr[1]);j,k=E['old_orbit'](q);th=k+(tau-i-1)//104
 if th in rows[j]:rows[j].remove(th)
 else:rows[j].add(th)
 past[j]=max(past.get(j,-10**9),th)
rows={j:sorted(r)for j,r in rows.items()if r}
def baseline(q):return(E['old_orbit'](q)[0]in OTHER)^E['row_color'](q,rows)
def color(q,rows,F):return(E['old_orbit'](q)[0]in OTHER)^E['row_color'](q,rows)^(q in F)
C['cert_parallel'].__globals__['color']=color
# Derive initial demands for finiteprelude, including allsamecellalternation.
seen={};flip=set();p=start;h=h0;word=A['forward_prelude_word'];prefixreads=[]
for i,ch in enumerate(word):
 prefixreads.append(p);want=ch=='L'
 if p in seen:assert(seen[p]^(p in flip))==want
 else:seen[p]=want
 E['toggle'](flip,p);h=(h+(-1 if want else 1))%4;v=E['V'][h];p=(p[0]+v[0],p[1]+v[1])
assert [list(p),h]==A['forward_wave_pose'];F={q for q,w in seen.items()if baseline(q)!=w};after=F^flip
# Infer every finite eligibility/ray mismatch of w atprefixend.
G=defaultdict(list);pp=p;hh=h
for i,ch in enumerate(J['word']):
 x,y=pp;t=x-y;a=x%14;k=(x-a)//14;G[t,a].append((k,i,ch,(a,a-t)));hh=(hh+(-1 if ch=='L'else 1))%4;v=E['V'][hh];pp=(pp[0]+v[0],pp[1]+v[1])
mismatch=set()
for j,g in G.items():
 g.sort(key=lambda z:(-z[0],z[1]));mn=min(z[0]for z in g);mx=max(z[0]for z in g);c=g[0][3];oj,kc=E['old_orbit'](c);hi=mx+2
 for th in rows.get(oj,[]):hi=max(hi,(th-kc)//-7+3)
 for q in after:
  if(q[0]-q[1],q[0]%14)==j:hi=max(hi,(q[0]-c[0])//14+2)
 for n in range(mn,hi+1):
  first=next(z for z in g if z[0]<=n);q=(c[0]+14*n,c[1]+14*n)
  if color(q,rows,after)!=(first[2]=='L'):mismatch.add(q)
 q=(c[0]+14*(hi+100),c[1]+14*(hi+100));assert color(q,rows,after)==(g[0][2]=='L')
assert not mismatch&seen.keys();F^=mismatch;after^=mismatch;cert=C['cert_parallel'](rows,after,p,h,J['word']);assert cert
past_overlap=[];erasures=[]
for q in F:
 j,k=E['old_orbit'](q)
 if baseline(q):erasures.append(q)
 if j in past and k<=past[j]:past_overlap.append(q)
# Independent completefuture wordactualcolor replay control (finite onlyadditionalcheck).
ff=set(F);pp=start;hh=h0
for ch in word+J['word']*2:
 assert color(pp,rows,ff)==(ch=='L');E['toggle'](ff,pp);hh=(hh+(-1 if ch=='L'else 1))%4;v=E['V'][hh];pp=(pp[0]+v[0],pp[1]+v[1])
report={'scope':'Fresh finite launch cap on genuineincomingBcausalHfront plusfourpreexistingfullstandardbands. No connectedfiniteproducer ofthosebands claimed.','source_completion_sha256':hashlib.sha256(Path('/workspace/shared/langton/causal_reduction/unit_scale/LLR_inverse_completion_certificate.json').read_bytes()).hexdigest(),'incoming_H_phase':phase,'incoming_H_copy':copy,'incoming_tau':tau,'entry_pose':[list(start),h0],'prelude_word':word,'prelude_read_t_hull':[min(x-y for x,y in prefixreads),max(x-y for x,y in prefixreads)],'wave_pose':A['forward_wave_pose'],'launch_cap':sorted(F),'launch_cap_mass':len(F),'cap_t_hull':[min(x-y for x,y in F),max(x-y for x,y in F)],'cap_u_hull':[min(x+y for x,y in F),max(x+y for x,y in F)],'erased_baseline_black_cells':sorted(erasures),'strict_incoming_past_read_overlap':sorted(past_overlap),'all_cap_cells_in_last_writer_strip':all(-2<=x-y<=8 for x,y in F),'all_future_wave_certificate':cert,'fresh_additions_only':not erasures and not past_overlap};(ROOT/'fresh_1564_launch_cap.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

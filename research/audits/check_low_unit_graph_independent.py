"""Literal complex-coordinate reconstruction of frozen low packet graphs."""
from pathlib import Path
from collections import Counter
import json,hashlib
B=Path('/workspace/shared/langton');R=B/'core_periodicity_new/low_summary_frozen_20261023_0648';G=json.loads((R/'literal_residual_geometry.json').read_text())['geometry'];dirs=(1j,1,-1j,-1);L=-18;W=8;results=[]
for k in(3,5):
 J=json.loads((R/f'v1_k{k}.json').read_text());D=json.loads((R/f'literal_factor_dfa_k{k}.json').read_text());U=json.loads((R/f'low_k{k}_unit.json').read_text());nd=len(D['transitions']);phase=J['phase'];assert U['original_controls']==4*nd
 raw=(R/f'low_k{k}_unit.dat').read_text().split();n,m=map(int,raw[:2]);E=[tuple(map(int,raw[2+4*i:6+4*i])) for i in range(m)];assert len(raw)==2+4*m and E==list(map(tuple,U['edges'])) and n==len(U['nodes'])
 actions={};maxoff=-999;maxdelta=0
 for h in range(4):
  for a in D['keep']:
   g=G[a];z=0j;heading=dirs[(h+phase)%4]
   for c in g['word']:heading*=(-1j if c=='R' else 1j);z+=heading
   dq=round(z.real+z.imag);dh=(dirs.index(heading)-h-phase)%4;c=g['name'].count('C');actions[h,a]=(c,dq,dh);maxdelta=max(maxdelta,abs(dq))
   for xy in g['inputs']+g['outputs']:
    q=complex(*xy)*(-1j)**(h+phase);off=round(q.real+q.imag);maxoff=max(maxoff,off);assert L+off<=J['initial_bound']
 for a in J['actions']:
  h,p,c,dq,dh=a[:5];assert (c,dq,dh)==actions[h,p] and L<=a[6]
 assert maxdelta<=W and all(L<=q for q in J['old_core_limits'])
 expected={(h,d,a) for h in range(4) for d,row in enumerate(D['transitions']) for a,to in zip(D['keep'],row) if to>=0}
 observed=set();edgeuse=Counter();privateuse=Counter()
 for p in U['packet_expansions']:
  h,d=p['source'];a=p['packet'];key=h,d,a;assert key in expected and key not in observed;observed.add(key)
  c,dq,dh=actions[h,a];to=D['transitions'][d][D['keep'].index(a)];target=[(h+dh)%4,to];assert p['target']==target and p['head_delta']==dq and p['C_count']==c
  ids=p['unit_edges'];assert len(ids)==max(1,abs(dq));u=h*nd+d;weight=change=0
  for j,eid in enumerate(ids):
   edgeuse[eid]+=1;x,y,delta,w=E[eid];assert x==u;assert delta==(-1 if dq>0 else 1 if dq<0 else 0);assert w==(c if j==0 else 0);weight+=w;change+=delta;u=y
   if j<len(ids)-1:assert u>=4*nd;privateuse[u]+=1
  assert u==target[0]*nd+target[1] and weight==c and change==-dq
 assert observed==expected and edgeuse==Counter(range(m)) and privateuse==Counter(range(4*nd,n))
 for h in range(4):
  for d in range(nd):assert U['nodes'][h*nd+d]==dict(heading=h,dfa=d)
 results.append(dict(window=k,packet_transitions=len(expected),unit_vertices=n,unit_edges=m,private_vertices=n-4*nd,cutoff=L,boundary_width=W,maximum_input_output_offset=maxoff,initial_high_threshold=J['initial_bound']))
out=dict(status='PASS independent literal packet geometry and all private unit chains',controls=results,scope='Exact heading/DFA low-counter graph; no high residual transactions below the proved cutoff. No integrated record exclusion.',manifest_sha256=hashlib.sha256((R/'manifest.json').read_bytes()).hexdigest());Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

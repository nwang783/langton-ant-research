from pathlib import Path
import hashlib,json
S=Path(__file__);R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'WRITTEN_WAKE_PORT_OBSTRUCTION_MANIFEST.json';assert sha(MF)=='bb06d7cacf5b95d8769a6c74c93cc571cb9774623a6ee231858140e2c2875644'
for f,h in json.loads(MF.read_text())['files'].items():assert sha(D/f)==h
J=json.loads((D/'WRITTEN_WAKE_PORT_OBSTRUCTION_CHECKED.json').read_text())
ns={'__file__':str(S.with_name('check_return_permanent_debt_independent.py'))};exec(Path(ns['__file__']).read_text().split('def check_case')[0],ns);verify=ns['verify_future']
G={-1j,1+1j,1+3j,2+2j};B={q:-i-1 for i,q in enumerate(sorted(G,key=lambda q:(q.real,q.imag)))};p=0j;h=1;vec=(1j,1,-1j,-1);xy=lambda q:[int(q.real),int(q.imag)];A='';U='';Q=[];first={}
for t in range(286):
 if t==182:B0=dict(B);p0=p;h0=h
 if t<182 and p not in first:first[p]=dict(cell=xy(p),black=p in B,first=t)
 if t>=182:Q.append(p)
 ch='L'if p in B else'R'
 if ch=='L':B.pop(p);h=(h-1)%4
 else:B[p]=t;h=(h+1)%4
 if t<182:A+=ch
 else:U+=ch
 p+=vec[h]
assert(A,U,list(map(xy,Q)))==(J['A'],J['U'],J['Q']);vw,vd,vf,vt=verify(B0,p0,h0);assert vw==U and vd==2+2j
C={q for q,i in B0.items()if i in vf};P0=set(B0)-C
assert len(C)==13 and len(P0)==23 and len(first)==58;assert sorted(map(xy,C))==J['C'] and sorted(map(xy,P0))==J['launch_permanent'];assert list(first.values())==J['first']
def ray(q,r):
 d=q-r
 return int(d.real)//2 if d.real==d.imag and int(d.real)%2==0 else None
W={}
for i,q in enumerate(Q):
 if U[i]=='L':continue
 later=[104*k+j for j,r in enumerate(Q)if(k:=ray(q,r))is not None and k>=0 and 104*k+j>i]
 if not later:W[q]=i
assert [{'cell':xy(q),'phase':i}for q,i in W.items()]==J['W'] and len(W)==12
# Full-class uniqueness and all past copies disjoint from every current/future read.
for q in W:
 for z in W:
  assert q==z or ray(q,z)is None
 for r in Q:
  k=ray(q,r);assert k is None or k<=0
for q in P0:
 for r in Q:assert (k:=ray(q,r))is None or k<0
for q in C:
 assert not any((k:=ray(q,z))is not None and k<0 for z in W)
onfull=lambda q:any(ray(q,z)is not None for z in W)
onpast=lambda q:q in C or any((k:=ray(q,z))is not None and k<0 for z in W)
req=sorted(first.values(),key=lambda z:z['first']);g0=-1j
maxoffset=max((complex(*f['cell'])-g0).__mul__((-1j)**r).real+(complex(*f['cell'])-g0).__mul__((-1j)**r).imag for f in req for r in range(4));minimum=min(q.real+q.imag for q in list(C)+Q+list(W));maxW=max(q.real+q.imag for q in W)
assert(maxoffset,minimum,maxW)==(13,6,15);assert maxW-4*6+maxoffset==4<minimum

def failure(o,r,on):
 for f in req:
  q=o+(-1j)**r*complex(*f['cell']);b=on(q)
  if b!=f['black']:return dict(first_read=f['first'],cell=xy(q),wanted_black=f['black'],actual_black=b)
 raise AssertionError('unexpected compatible launch')
bulk={(z['rotation'],tuple(z['origin'])):z for z in J['bulk']};motifs=[]
for r in range(4):
 for anchor in W:
  o=anchor-(-1j)**r*g0;z=bulk[r,tuple(xy(o))];assert failure(o,r,onfull)==z['first_failure'];hits=sum(onfull(o+(-1j)**r*g)for g in G);assert hits==z['blackhits']
  if hits==4:motifs.append((r,xy(o)));assert onfull(o)
assert motifs==[(1,[6,3])]
rows={(z['phase'],z['rotation'],tuple(z['origin'])):z for z in J['finite_cases']};seen=set();changes=set();latest=0
for phi in range(104):
 on=lambda q:onpast(q)^(q in changes)
 anchors=C|set(Q[:phi])|{q+j*(2+2j)for q in W for j in range(-5,0)}
 for a in anchors:
  if not on(a):continue
  for r in range(4):
   o=a-(-1j)**r*g0;key=(phi,r,tuple(xy(o)));assert key not in seen;seen.add(key);f=failure(o,r,on);assert f==rows[key]['first_failure'];latest=max(latest,f['first_read'])
 assert on(Q[phi])==(U[phi]=='L');changes.symmetric_difference_update({Q[phi]})
assert seen==set(rows) and len(seen)==33568 and latest==32;assert(C^changes)=={q+2+2j for q in C}|set(W);assert not ({q+2+2j for q in C}&set(W));assert max(q.real+q.imag for q in P0)==11
controls=[]
for K in(0,1,7,31):
 BB=dict(B0);p=p0;h=h0;fringe=set(C)
 for t in range(104*(K+1)):
  if t>=104*K:
   expected=P0|{q+j*(2+2j)for q in W for j in range(K)}|{q+K*(2+2j)for q in fringe};assert set(BB)==expected;fringe.symmetric_difference_update({Q[t%104]})
  ch='L'if p in BB else'R';assert ch==U[t%104]
  if ch=='L':BB.pop(p);h=(h-1)%4
  else:BB[p]=182+t;h=(h+1)%4
  p+=vec[h]
 controls.append(dict(K=K,phases=104,full_terminal_mass=len(BB),pose=[xy(p),h]))
assert controls==[dict(K=z['K'],phases=z['checked_phases'],full_terminal_mass=z['full_terminal_mass'],pose=z['terminal_pose'])for z in J['controls']]
out=dict(status='PASS exact settled-standard all-position G-launch prefix33 obstruction and qualified full finite-field transfer',manifest=sha(MF),script=sha(S),bulk_cases=48,fringe_cases=33568,last_failure=32,all_black_motif=motifs,cutoff=dict(maxW=15,maxoffset=13,omitted_anchor_j=-6,exposure_upper=4,fringe_minimum=6),controls=controls,analytic_review=['The literal complete4-cell source and all-future ray parity independently yield13 future inputs,23 permanent launch cells,12 distinct permanent full-drift output classes. All older output copies miss every U read; one-period full fringe XOR closes exactly. Thus the settled comparison field is genuine, not a cropped motif or guessed stationary phase.','Any placement matching prefix33 must map its tick1 initiallyBLACK cell to an actualBLACK anchor. Every such anchor is in the enumerated finite C/phase-read/last5W union or a pastW copy j<=-6. At the latter, every full182-exposure coordinate sum is<=4<6, where settled field equals the bi-infinite wake. Therefore48 quotient and33568 exact fringe failures exhaust ALL poses, not merely bounded origin scans.','The unique complete4BLACK motif exists, rotated at origin6,3 modulo2,2, but its requiredWHITE initial head isBLACK. Whites are essential. All104 phases and4 rotations, including active fringe, fail by update32.','Full finite boards equal P0 union W[0,K) union shiftedFphi at every K>=0 by exact disjoint closure. Compared to the shifted settledfield, all possible differences P0/negativeW have sum<=11. Prefix33 exposures entirely inx+y>=12 therefore inherit the obstruction, with all archives retained.','No claim excludes the launch cap, altered/superposed wakes, extra ports, clearing routes or different protocols. The paid28-cell concatenations remain valid. This is one exact regeneration-interface obstruction, not controller/capture classification.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))

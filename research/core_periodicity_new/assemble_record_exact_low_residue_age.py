"""Exact-low Δtransverse-profile assembly with current(height,residue,age).
CLI DELAYED_GEOMETRY.json RESIDUE.ports PREFIX CUTOFF WIDTH.
Compact OPS output; JSON stores actual arcs and summary-generation provenance,
not millions of repeated summary arcs.
"""
from pathlib import Path
import json,sys,hashlib
src,ports,out=map(Path,sys.argv[1:4]);L,W=map(int,sys.argv[4:6]);S=json.loads(src.read_text());D=json.loads(Path(S['dfa_file']).read_text());G=json.loads(Path('chronology_dcuv/literal_residual_geometry.json').read_text())['geometry'];age={(a,x,y):r for a,x,y,r in json.loads(Path('chronology_dcuv/counted_input_age_rules_complete.json').read_text())};nd=len(D['transitions']);keep=D['keep'];phase=S['phase'];F=S['initial_bound'];H=S['height_cap'];mod=4;places=[(z,tr)for z in range(F+1,H+1)for tr in range(z%2,mod,2)];pidx={p:i for i,p in enumerate(places)};m=len(places);acts={(v[0],v[1]):v for v in S['actions']};assert L<=min(v[6]for v in S['actions']);assert W>=max(abs(v[3])for v in S['actions'])
def rot(p,h):x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def coord(p):x,y=rot(p,phase);return x+y,x-y
assert all(L+coord(rot(v,h))[0]<=F for h in range(4)for a in keep for k in ['inputs','outputs']for v in G[a][k])
positions=[];ix={}
for h in range(4):
 for q in range(L+1,S['old_core_limits'][h]+1):
  if(q-h)%2:continue
  for d in range(nd):
   for tr in range(h%2,mod,2):ix[h,q,d,tr]=len(positions);positions.append([h,q,d,tr,'high'])
nhigh=len(positions);f=ports.open();fmt,np,ne,ni,mm=next(f).split();np,ne,ni,mm=map(int,[np,ne,ni,mm]);assert fmt=='RESIDUE_PORTS'and mm==mod;initialports=list(map(int,next(f).split()));assert len(initialports)==ni;portrows=[];pix={};lpix={}
for p in range(np):
 h,d,dep=map(int,next(f).split());assert 0<=dep<W and(L-dep-h)%2==0;portrows.append([h,d,dep]);lpix[h,d,dep]=p
 for tr in range(h%2,mod,2):pix[p,tr]=len(positions);positions.append([h,L-dep,d,tr,'low',p])
ops=[];opix={}
def intern(c,I,O):
 key=(c,tuple(I),tuple(O))
 if key not in opix:opix[key]=len(ops);ops.append([c,I,O])
 return opix[key]
zero=[intern(c,[0]*(5*m),[0]*m)for c in range(5)]
def op(h,q,tr,a):
 I=[0]*(5*m);O=[0]*m;c=G[a]['name'].count('C')
 for v in G[a]['inputs']:
  dz,dt=coord(rot(v,h));z=q+dz
  if z>F:
   assert z<=H;k=pidx[z,(tr+dt)%mod]
   for j in range(age[a,*v]+1):I[5*k+j]+=1
 for v in G[a]['outputs']:
  dz,dt=coord(rot(v,h));z=q+dz
  if z>F:assert z<=H;O[pidx[z,(tr+dt)%mod]]+=1
 return intern(c,I,O)
actual=[]
for p,(h,q,d,tr,_)in enumerate(positions[:nhigh]):
 for k,a in enumerate(keep):
  dd=D['transitions'][d][k]
  if dd<0:continue
  v=acts[h,a];c,dq,dh=v[2:5]
  if q>v[6]:continue
  h2=(h+dh)%4;q2=q+dq;tr2=(tr+coord(rot(G[a]['endpoint'][:2],h))[1])%mod
  to=ix[h2,q2,dd,tr2]if q2>L else pix[lpix[h2,dd,L-q2],tr2]
  actual.append([p,to,a,op(h,q,tr,a)])
for pp,(h,d,dep)in enumerate(portrows):
 q=L-dep
 for k,a in enumerate(keep):
  dd=D['transitions'][d][k]
  if dd<0:continue
  v=acts[h,a];c,dq,dh=v[2:5];q2=q+dq
  if q2<=L:continue
  for tr in range(h%2,mod,2):
   tr2=(tr+coord(rot(G[a]['endpoint'][:2],h))[1])%mod;actual.append([pix[pp,tr],ix[(h+dh)%4,q2,dd,tr2],a,zero[c]])
initial=[p for p,v in enumerate(positions[:nhigh])if v[2]==D['initial_class']]+[pix[p,tr]for p in initialports for tr in range(portrows[p][0]%2,mod,2)]
goals=[];a=S['target'];ai=keep.index(a);c,I,O=ops[op(0,0,0,a)]
for d,row in enumerate(D['transitions']):
 if row[ai]>=0:goals.append([ix[0,0,d,0],I])
nedges=len(actual)+2*ne
N={'format':'record_exact_low_residue_age_ops_v1','source_file':str(src.resolve()),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'ports_file':str(ports.resolve()),'ports_sha256':hashlib.sha256(ports.read_bytes()).hexdigest(),'cutoff':L,'boundary_width':W,'modulus':mod,'places':places,'age_cap':4,'positions':positions,'high_controls':nhigh,'low_port_rows':portrows,'operations':ops,'zero_operator_ids':zero,'initial_controls':initial,'goal_requirements':goals,'actual_transitions':actual,'summary_profiles':ne,'transition_count':nedges,'summary_layout':'After actual transitions, each port profile row produces two arcs in source transverse residue order h%2 then h%2+2. Arc packet=-1, target residue=(source+profile delta)%4, operator=zero_operator_ids[profile C].','scope':'Current high(height,transverse residue modulo4,C-age) multiset with exact low-height and transverse-residue excursion summaries. Full colors/context noninterference is not enforced outside the summary; no physical ant sufficiency or independently signed assembly.'}
out.with_suffix('.json').write_text(json.dumps(N,separators=(',',':')))
with out.with_suffix('.dat').open('w')as g:
 g.write(f'OPS {m} {len(positions)} {nedges} {len(initial)} {len(goals)} {len(ops)}\n');g.write(' '.join(map(str,initial))+'\n')
 for p,r in goals:g.write(' '.join(map(str,[p]+r))+'\n')
 for c,I,O in ops:g.write(' '.join(map(str,[c]+I+O))+'\n')
 for e in actual:g.write(' '.join(map(str,e))+'\n')
 for _ in range(ne):
  p,q,dt,c=map(int,next(f).split());h=portrows[p][0];hh=portrows[q][0]
  for tr in range(h%2,mod,2):
   tr2=(tr+dt)%mod;assert tr2%2==hh%2;g.write(f'{pix[p,tr]} {pix[q,tr2]} -1 {zero[c]}\n')
f.close();out.with_suffix('.weights').write_text(' '.join(str(2**(z-F))for z,tr in places for j in range(5))+'\n');print({'places':m,'controls':len(positions),'high_controls':nhigh,'low_controls':len(positions)-nhigh,'actual_edges':len(actual),'summary_arcs':ne*2,'operators':len(ops),'initial_controls':len(initial),'goals':len(goals)})

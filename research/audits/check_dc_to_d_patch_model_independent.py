#!/usr/bin/env python3
"""Rebuild exact anchored patch abstraction from literal ant reads; no author imports."""
import json,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];A=ROOT/'audits';W=ROOT/'word_stabilization';C=ROOT/'core_periodicity_new'
raws=['LLLLRLRRRR','LLLLRLRRRRLLLLRLRRRRLRRRR','LLLLRLRRRRLLLLRLRRRRLRRRRLLLLRLRRRRLRRRR','LLLLRLRRRRLLLLRLRRRRLRRRRLLLLRLRRRRLRRRRLLLLRLRRRRLRRRR','LLLLRLRRRRLRRLRRRR','LLLLRLRRRRLRRLRRRRLLLLRLRRRRLRRRR','LLLLRLRRRRLRRLRRRRLLLLRLRRRRLRRRRLLLLRLRRRRLRRRR'];mark='LLLLRLRRRRL'

def xy(z):return int(z.real),int(z.imag)
def walk(w):
 z=0j;d=1j;first={};seen={};flips=set()
 for c in w:
  assert seen.get(z)!=c
  first.setdefault(z,c=='L');seen[z]=c;flips.symmetric_difference_update({z});d*=(-1j if c=='R' else 1j);z+=d
 return z,(1j,1,-1j,-1).index(d),first,flips

def rotation(z,h):return z*((-1j)**(h%4))
def main():
 g=[]
 for w in raws:
  end,h,fr,fl=walk(w);g.append((end,h,walk(w+mark)[2],fl))
 macro=json.loads((W/'seven_sub_dcv_port_quotient.json').read_text())['macro_words']
 assert [r['word'] for r in macro]==raws and all(r['end_marker']==mark for r in macro)
 ordinary={tuple(map(int,line.split()[:5])) for line in (W/'seven_sub_dcv_star4_kernel.tsv').read_text().splitlines()}
 protected={tuple(map(int,line.split()[:7])) for line in (W/'dcv_protected_patch2_kernel.tsv').read_text().splitlines()}
 q=2+3j;target=2+2j;keep=(0,1,4,5,6);src=1;dst=0
 assert q in g[src][3] and walk(raws[src])[2].get(q)==False # source's q sole RAW R in this case
 assert g[dst][2][q-target] # target first requires black
 P=sorted(g[src][2],key=xy);ids={z:i for i,z in enumerate(P)}
 poses=set()
 for a in keep:
  for h in range(4):
   for local in g[a][2]:
    for global_ in P:
     origin=global_-rotation(local,h);x,y=xy(origin)
     if (x+y-h)%2==0:poses.add((x,y,h))
 poses=sorted(poses);where={p:i for i,p in enumerate(poses)};OUT=len(poses)
 def denied(a,b,point,h,protected_cell):
  key=(a,b,*xy(point),h%4)
  return key in ordinary or (*key,*xy(protected_cell)) in protected
 rows=[];reentry=set()
 for sid,(x,y,h) in enumerate(poses):
  p=complex(x,y)
  for a in keep:
   end,dh,req,flip=g[a];nextp=p+rotation(end,h);nexth=(h+dh)%4
   dest=where.get((*xy(nextp),nexth),OUT)
   k=v=f=0
   for z in P:
    local=rotation(z-p,-h)
    if local in req:
     k|=1<<ids[z]
     if req[local]:v|=1<<ids[z]
    if local in flip:f|=1<<ids[z]
   goal=a==dst and p==target and h==0
   qlocal=rotation(q-p,-h)
   allowed=qlocal not in req and not denied(src,a,p,h,q) and not denied(a,dst,rotation(target-p,-h),-h,qlocal)
   if allowed or goal:rows.append([sid,dest,k,v,f,int(goal),a])
   oldh=(h-dh)%4;oldp=p-rotation(end,oldh)
   if (*xy(oldp),oldh) not in where:reentry.add(sid)
 startp,starth,req,flip=g[src];initial=sum(int(req[z]^(z in flip))<<ids[z] for z in P)
 start=[where.get((*xy(startp),starth),OUT),(1<<len(P))-1,initial]
 data=json.loads((C/'protected_patch_source.json').read_text())
 for k,actual in [('n',len(P)),('points',[list(xy(z)) for z in P]),('poses',[list(v) for v in poses]),('out',OUT),('start',start),('transitions',rows),('reentry',sorted(reentry)),('keep',list(keep))]:assert data[k]==actual,k
 dat=A/'dc_to_d_patch_independent.dat'
 lines=[f'{len(P)} {OUT+1} {len(rows)} {len(reentry)}',' '.join(map(str,start))]+[' '.join(map(str,r)) for r in rows]+[' '.join(map(str,sorted(reentry)))]
 dat.write_text('\n'.join(lines)+'\n')
 assert dat.read_bytes()==(C/'protected_patch_source.dat').read_bytes()
 out=dict(status='PASS independent literal abstraction reconstruction',patch_cells=len(P),near_poses=OUT,abstract_states=(OUT+1)*(1<<len(P)),transitions=len(rows),reentry_poses=len(reentry),start=start,dependency_hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [W/'seven_sub_dcv_star4_kernel.tsv',W/'dcv_protected_patch2_kernel.tsv',C/'protected_patch_source.json',C/'protected_patch_source.dat']})
 Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

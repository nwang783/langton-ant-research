#!/usr/bin/env python3
"""Rebuild exact anchored patch abstraction from literal ant reads; no author imports."""
import json,hashlib,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];A=ROOT/'audits';W=ROOT/'word_stabilization';C=ROOT/'core_periodicity_new'
raws=['LLLLRLRRRR','LLLLRLRRRRLLLLRLRRRRLRRRR','LLLLRLRRRRLLLLRLRRRRLRRRRLLLLRLRRRRLRRRR','LLLLRLRRRRLLLLRLRRRRLRRRRLLLLRLRRRRLRRRRLLLLRLRRRRLRRRR','LLLLRLRRRRLRRLRRRR','LLLLRLRRRRLRRLRRRRLLLLRLRRRRLRRRR','LLLLRLRRRRLRRLRRRRLLLLRLRRRRLRRRRLLLLRLRRRRLRRRR'];mark='LLLLRLRRRRL'

# Fixed HB-approved expanded alphabet; never infer proof scope from metadata.
u='LLLLRLRRRRLRLLLLRRRRLRRLRRRR';c='LLLLRLRRRRLRRRR'
raws=raws+[u,u+c,u+c+c]
def validate_profile(data):
 profile=Path(data['resource_profile_file']);assert hashlib.sha256(profile.read_bytes()).hexdigest()==data['resource_profile_sha256']
 j=json.loads(profile.read_text())
 # HB all-ten, HH post-DCCC, and the independently replayed recurrent boundary restart.
 approved_keeps={tuple(range(10)),(0,1,2,4,5,6,7,8,9),(0,1,4,5,6,7,8,9)}
 assert tuple(j['keep']) in approved_keeps
 trusted={'macro_words':'e5e44c59f20c81e45db81a3b8a9ee53279f0ad70534a9191f43441692c0bc9e8','geometry':'f0dcedd2135a954dbb315feafc1ce3ae5b8a54a46ea69595d5c7c3fafc160ebd','ordinary':'c17fe5c0480078446c66bfd7f8655cd69158fb3a70203e81032b3ed05e3e42d6','protected':'edd8d83e17ddaa220c17960315c235ca90fa2fde9045007efabf824d580f74fd'}
 assert set(j['files'])==set(trusted)
 for k,h in trusted.items():
  r=j['files'][k];assert r['sha256']==h==hashlib.sha256(Path(r['path']).read_bytes()).hexdigest()
 assert 'case'not in data
 return tuple(j['keep'])

def xy(z):return int(z.real),int(z.imag)
def walk(w):
 z=0j;d=1j;first={};seen={};flips=set()
 for c in w:
  assert seen.get(z)!=c
  first.setdefault(z,c=='L');seen[z]=c;flips.symmetric_difference_update({z});d*=(-1j if c=='R' else 1j);z+=d
 return z,(1j,1,-1j,-1).index(d),first,flips

def rotation(z,h):return z*((-1j)**(h%4))
def main(path):
 path=path.resolve()
 data=json.loads(path.read_text())
 keep=validate_profile(data)
 if 'case' in data:
  c=data['case'];frozen=json.loads((W/'dcv_conditional_confinement_optimized.json').read_text())['unproved_bad_transfers'];assert c==frozen[data['case_index']-1]
  data=dict(data,source=c['source_packet'],target=c['target_packet'],target_pose=c['target_pose'],protected_q=c['source_output'])
 g=[]
 for w in raws:
  end,h,fr,fl=walk(w);g.append((end,h,walk(w+mark)[2],fl))
 macro=json.loads((W/'seven_sub_dcvu_port_quotient.json').read_text())['macro_words']
 assert [r['word'] for r in macro]==raws and all(r['end_marker']==mark for r in macro)
 ordinary={tuple(map(int,line.split()[:5])) for line in (W/'seven_sub_dcvu_patch2_kernel.tsv').read_text().splitlines()}
 protected={tuple(map(int,line.split()[:7])) for line in (C/'chronology_dcuv/protected_patch2.tsv').read_text().splitlines()}
 q=complex(*data['protected_q']);target=complex(*data['target_pose'][:2]);th=data['target_pose'][2];src=data['source'];dst=data['target']
 assert src in keep and dst in keep and th in range(4)
 K={z for z,black in walk(mark)[2].items() if black}
 entry={z for z,black in g[src][2].items() if black};end,dh,req,fl=g[src]
 endcore={end+rotation(z,dh) for z in K}
 outputs=(entry^fl)-endcore
 targetinput=rotation(q-target,-th)
 assert q in outputs
 assert targetinput in {z for z,black in g[dst][2].items() if black}-K
 P=[complex(*z) for z in data['points']];assert len(set(P))==len(P) and P==sorted(P,key=xy)
 ids={z:i for i,z in enumerate(P)}
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
   goal=a==dst and p==target and h==th
   qlocal=rotation(q-p,-h)
   allowed=qlocal not in req and not denied(src,a,p,h,q) and not denied(a,dst,rotation(target-p,-h),(th-h)%4,qlocal)
   if allowed or goal:rows.append([sid,dest,k,v,f,int(goal),a])
   oldh=(h-dh)%4;oldp=p-rotation(end,oldh)
   if (*xy(oldp),oldh) not in where:reentry.add(sid)
 startp,starth,req,flip=g[src];initial=sum(int(req[z]^(z in flip))<<ids[z] for z in P if z in req)
 known=sum(1<<ids[z] for z in P if z in req)
 start=[where.get((*xy(startp),starth),OUT),known,initial]
 assert (*xy(target),th) in where and sum(row[5] for row in rows)==1
 member=[]
 for k,actual in [('n',len(P)),('points',[list(xy(z)) for z in P]),('poses',[list(v) for v in poses]),('out',OUT),('start',start),('transitions',rows),('reentry',sorted(reentry)),('keep',list(keep))]:assert data[k]==actual,k
 dat=A/'dcuv_patch_replays'/path.with_suffix('.dat').name;dat.parent.mkdir(exist_ok=True)
 lines=[f'{len(P)} {OUT+1} {len(rows)} {len(reentry)}',' '.join(map(str,start))]+[' '.join(map(str,r)) for r in rows]+[' '.join(map(str,sorted(reentry)))]
 dat.write_text('\n'.join(lines)+'\n')
 assert dat.read_bytes()==path.with_suffix('.dat').read_bytes()
 out=dict(status='PASS independent literal abstraction reconstruction',source=src,target=dst,target_pose=[*xy(target),th],protected_q=list(xy(q)),frozen_bad_list_index_zero_based=(member[0] if member else None),patch_cells=len(P),near_poses=OUT,abstract_states=(OUT+1)*(1<<len(P)),transitions=len(rows),reentry_poses=len(reentry),start=start,dependency_hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [W/'seven_sub_dcvu_patch2_kernel.tsv',C/'chronology_dcuv/protected_patch2.tsv',path,path.with_suffix('.dat')]})
 dat.with_suffix('.model_check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':
 for arg in sys.argv[1:]:main(Path(arg))

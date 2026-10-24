from pathlib import Path
import json,hashlib
from check_dcuv_producer_model_independent import geometry,rotation,xy,walk,raws,ordinary,protected,ROOT
D=ROOT/'core_periodicity_new/chronology_dcuv/recurrent8_counted';ids=[0,1,4,5,6,7,8,9];mp={v:i for i,v in enumerate(ids)};cc=[0,1,0,1,2,0,1,2]
count={tuple(map(int,l.split()[:8]))for l in(D/'closure.tsv').read_text().splitlines()};needed=set()
for a in ids:
 for q in geometry[a]['outputs']:
  for b in(7,8,9):
   for z in(-1+4j,2j,3j):
    assert z in geometry[b]['inputs']
    for h in range(4):
     p=q-rotation(z,h);r=(a,b,*xy(p),h,*xy(q))
     if(sum(xy(p))+h)%2==0 and r[:5]not in ordinary and r not in protected:needed.add((mp[a],mp[b],*r[2:]))
assert needed=={tuple(map(int,l.split()))for l in(D/'targets1188.tsv').read_text().splitlines()}and len(needed)==1188

def kin(a,p,h,k):
 if k==4:return True
 remaining=k-cc[a]
 if remaining<0:return False
 if remaining>=2:return True
 end,dh,_,_=walk(raws[ids[a]]);offset=-.5-.5j;delta=rotation(p+rotation(offset,h)-end-rotation(offset,dh),-dh);x,y=xy(delta);assert delta==complex(x,y)
 if remaining==0:return x>=0 and y>=x and(x+y)%2==0 and(x!=0 or y%4==0)
 x-=1;y-=1;return y>=0 and x<=y and(x+y)%2==0 and(y!=0 or x%4==0)
results=[]
for r in sorted(needed):
 a,b,x,y,h,qx,qy=r;reasons=[]
 for k in range(4):
  reason='count/heading'if k<cc[a]or(h+k)%4 else('kinematic'if not kin(a,complex(x,y),h,k)else'counted clause')
  assert reason!='counted clause'or(*r,k)in count,(r,k)
  reasons.append(reason)
 assert(*r,4)not in count
 results.append(dict(query=r,low_exclusions=reasons,overflow_excluded=False))
controls=[]
for w,expected in[('LLLLRLRRRR',1+1j),('LLLLRLRRRRLRRRR',1+1j),('LLLLRLRRRRLRRLRRRR',1+3j),('LLLLRLRRRRLRLLLLRRRRLRRLRRRR',4j)]:
 end,h,_,_=walk(w);offset=-.5-.5j;z=end+rotation(offset,h)-offset;assert z==expected;controls.append(dict(word=w,center_increment=xy(z)))
out=dict(status='PASS all4752 low-count queries excluded; all1188 overflow queries remain',queries=results,center_controls=controls,scope='Complete recurrent-eight packet intervals; count includes the source packet C count and all strict-intermediate C macros, excludes the target packet. No upper bound on C or global U-fuel conclusion.',hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[D/'closure.tsv',D/'targets1188.tsv',Path(__file__)]})
(ROOT/'audits/dcuv_counted_replay/queries.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])

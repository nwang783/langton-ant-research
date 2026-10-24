"""Exact finite n5 nonproper contact diagnostic. OPEN survivors are retained."""
import json
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parent
# Reuse small exact geometry helpers; this module's separate signed claim is unchanged.
ns={'__file__':str(ROOT/'check_four_C_center_contact_gate.py')};exec((ROOT/'check_four_C_center_contact_gate.py').read_text().split('# Canonical first-contact geometry')[0],ns)
G,K,IDS,NEW,COUNTED,HB,VECTORS,outputs,contexts=[ns[x] for x in ['G','K','IDS','NEW','COUNTED','HB','VECTORS','outputs','contexts']]
rot,add,sub,det,closed_contact,zero_reach=[ns[x] for x in ['rot','add','sub','det','closed_contact','zero_reach']]

def one_reach(p,target,h):
    X,Y=rot(sub(target,p),-h)
    if Y<1:return None
    for y in range(Y):
        for x in range(y+1):
            if zero_reach((0,0),(x,y),0) and zero_reach((x,y+1),(X,Y),3):
                return (x,y)
    return None

roles=[]
for source in IDS:
    count=G[source]['name'].count('C');atom=G[source]['name'][0]
    roles.append({'atom':atom,'source':source,'p':(0,0),'h':0,'shift':0,'remaining':count})
    p,h=tuple(G[ns['base'](source)]['endpoint'][:2]),0
    for j in range(count):
        roles.append({'atom':'C','source':source,'p':p,'h':h,'shift':j,'remaining':count-j})
        p,h=add(p,rot((0,1),h)),(h-1)%4

geo=[]
center=(F(-1,2),F(-1,2))
for a,u in VECTORS.items():
 for b,bb in VECTORS.items():
    v=rot(bb,3);correction=sub(center,rot(center,3));corners=[add(correction,(s*u[0]-t*v[0],s*u[1]-t*v[1])) for s in (0,1) for t in (0,1)]
    for x in range(int(min(z[0] for z in corners)),int(max(z[0] for z in corners))+1):
     for y in range(int(min(z[1] for z in corners)),int(max(z[1] for z in corners))+1):
      if (x+y+3)%2:continue
      w=sub(add((x,y),rot(center,3)),center);den=det(u,v);s,t=F(det(w,v),den),F(det(w,u),den)
      if 0<=s<1 and 0<t<=1 and not(0<s<1 and 0<t<1):geo.append({'a':a,'b':b,'p':(x,y),'h':3,'s':s,'t':t})
assert len(geo)==24

results=[]
for gi,g in enumerate(geo):
 a,b,p=g['a'],g['b'],g['p']
 forced=[];input_slots=[]
 for o in outputs[a]:
    local=rot(sub(o,p),1)
    if local in K or contexts[b].get(local) is False:forced.append(tuple(o))
    elif local in [tuple(q) for q in (G[0 if b=='D' else 4 if b=='V' else 7]['inputs'] if b!='C' else [])]:input_slots.append(tuple(o))
 hard=[];survivors={}
 for o in forced:
    remaining=[];why=Counter()
    for ri,r in enumerate(roles):
     if r['atom']!=a:continue
     source=r['source'];full_o=add(r['p'],rot(o,r['h']))
     assert list(full_o) in G[source]['outputs'],(r,o,full_o)
     for n in range(6):
      h=(-n)%4
      for consumer in IDS:
       for inp in G[consumer]['inputs']:
        cp=sub(o,rot(inp,h));fp=add(r['p'],rot(cp,r['h']));fh=(r['h']+h)%4;age=n+r['shift']
        key=(NEW[source],NEW[consumer],*fp,fh,*full_o,min(age,5));hb=(source,consumer,*fp,fh,*full_o)
        if n<r['remaining']:reason='BEFORE_FULL_SOURCE_EXIT'
        elif (sum(fp)+fh)%2:reason='WRONG_SECTOR'
        elif hb in HB:reason='HB'
        elif key in COUNTED:reason='COUNT5'
        elif closed_contact(a,consumer,cp,h):reason='EARLIER_CLOSED_CONTACT'
        elif b!='C' and n+G[consumer]['name'].count('C')>5:reason='FULL_CONSUMER_NOT_FINISHED'
        else:
            bs=ns['base'](consumer);end=add(cp,rot(G[bs]['endpoint'][:2],h));left=5-n
            if left==0 and not(h==3 and zero_reach(end,p,3)):reason='ZERO_C_CONE'
            elif left==1 and not((h-1)%4==3 and one_reach(end,p,h) is not None):reason='ONE_C_CONE'
            else:
                reason='OPEN';remaining.append({'role_index':ri,'source':source,'output':o,'age':n,'full_age':age,'consumer':consumer,'input':inp,'pose':(*cp,h),'base_exit':(*end,h),'C_left':left})
        why[reason]+=1
    if not remaining:hard.append(o)
    else:survivors[str(o)]=remaining
 results.append({'geometry_index':gi,'geometry':g,'forced_source_slots':forced,'input_only_source_slots':input_slots,'hard_slots':hard,'open_clearers_by_slot':survivors})


def enc(x):
 if isinstance(x,F):return str(x) if x.denominator!=1 else int(x)
 if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [enc(z) for z in x]
 return x
out=ROOT/'chronology_dcuv/five_C_center_touch.probe.json';out.write_text(json.dumps(enc(results),indent=2)+'\n')
for row in results:
 print(row['geometry_index'],row['geometry']['a'],row['geometry']['b'],row['geometry']['p'],'forced',row['forced_source_slots'],'hard',row['hard_slots'],'open', {k:len(v) for k,v in row['open_clearers_by_slot'].items()})
print('ELIMINATED',sum(bool(r['hard_slots']) for r in results),'of',len(results))

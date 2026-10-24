#!/usr/bin/env python3
"""Exact outward-record first-L obstruction for arbitrary macro choices.
This independently builds internally feasible macro inventories. It does not
search finite trajectories or assume a finite substitution/controller.
"""
from itertools import product
from collections import defaultdict
import json,time
D=((0,1),(1,0),(0,-1),(-1,0))

def turn_path(w):
    p=(0,0);h=0;reads=[];last={};first_left=[]
    for t,c in enumerate(w):
        if p in last and last[p]==c:return None
        if p not in last and c=='L':first_left.append((t,p))
        last[p]=c;reads.append(p);h=(h+(1 if c=='R' else -1))%4
        dx,dy=D[h];p=p[0]+dx,p[1]+dy
    return {'word':w,'reads':reads,'first_left':first_left,'end':p,'heading':h,'charge':w.count('R')-w.count('L')}

def rotate(p,h):
    x,y=p
    for _ in range(h):x,y=y,-x
    return x,y

def owners(z,a,images):
    aa,bb=a;norm=aa*aa+bb*bb;result=set()
    for v in images:
        for h in range(4):
            for p in v['reads']:
                x,y=rotate(p,h);dx,dy=z[0]-x,z[1]-y
                nx,ny=dx*aa+dy*bb,dy*aa-dx*bb
                if nx%norm or ny%norm:continue
                c=(nx//norm,ny//norm)
                if (c[0]+c[1]+h)%2==0:result.add((c[0],c[1],h))
    return sorted(result)

def inventory(k):
    grouped=defaultdict(list)
    for bits in product('RL',repeat=k):
        data=turn_path(''.join(bits))
        if data and data['heading'] in [1,3] and sum(z*z for z in data['end'])>1:
            grouped[data['end'],data['heading']].append(data)
    cases=[]
    for (a,h),us in sorted(grouped.items()):
        if h!=1:continue
        vs=grouped.get(((-a[0],-a[1]),3),[])
        if not vs:continue
        rows=[]
        for u in us:
            certificates=[]
            for t,z in u['first_left']:
                own=owners(z,a,us+vs)
                if all(c[1]>=0 for c in own):
                    certificates.append({'phase':t,'cell':z,'owners':own,'private':all(c[:2]==(0,0) for c in own)})
            rows.append({'R_image':u['word'],'forward_witnesses':certificates})
        cases.append({'scale':a,'R_images':[u['word'] for u in us],'L_images':[v['word'] for v in vs],
                      'max_charges':[max(u['charge'] for u in us),max(v['charge'] for v in vs)],
                      'front_record_excluded':all(row['forward_witnesses'] for row in rows),'R_certificates':rows})
    return {'length':k,'cases':cases}

if __name__=='__main__':
    start=time.monotonic();data=[inventory(k) for k in [3,5,7,9]]
    result={'status':'exact finite ownership certificates; global implication separately proved','results':data,'seconds':time.monotonic()-start}
    open(__file__.replace('.py','.json'),'w').write(json.dumps(result,indent=2)+'\n')
    for row in data:
        print(row['length'],len(row['cases']),'scales; record excluded', [r['scale'] for r in row['cases'] if r['front_record_excluded']])

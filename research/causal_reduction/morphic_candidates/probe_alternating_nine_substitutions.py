#!/usr/bin/env python3
"""Exact finite conflicts for two alternating scale-three turn substitutions.
A finite survivor is UNKNOWN, never an infinite or finite-seed certificate.
"""
import itertools,json,hashlib,time,argparse
from pathlib import Path
D=((0,1),(1,0),(0,-1),(-1,0))
def footprint(w):
    x=y=h=0; seen={}
    for t,c in enumerate(w):
        if (x,y) in seen and seen[x,y]==c:return None
        seen[x,y]=c;h=(h+(1 if c=='R' else -1))%4
        dx,dy=D[h];x+=dx;y+=dy
    return (x,y),h

def inventory():
    a=[];b=[];ga=[];gb=[]
    for z in itertools.product('LR',repeat=9):
        w=''.join(z);f=footprint(w)
        x=y=h=0
        for c in w:
            h=(h+(1 if c=='R' else -1))%4;dx,dy=D[h];x+=dx;y+=dy
        if ((x,y),h)==((3,0),1):ga.append(w)
        if ((x,y),h)==((-3,0),3):gb.append(w)
        if f==((3,0),1):a.append(w)
        if f==((-3,0),3):b.append(w)
    assert len(a)==len(b)==9
    assert len(ga)==len(gb)==24
    return a,b,ga,gb

def trial(u,v,root,cap):
    sub={'R':u,'L':v};k=len(u)
    assert u[0]==root if root=='R' else v[0]==root
    # Build only enough levels to cover the requested prefix. Each level is a
    # true prefix of the next because the root is prolongable.
    w=root
    while len(w)<cap:w=''.join(sub[c] for c in w)
    x=y=h=0;seen={};fuel=0;third=0
    for t,c in enumerate(w[:cap]):
        if (x,y) in seen:
            old,ot,count=seen[x,y]
            if old==c:return {'status':'CONFLICT','time':t,'previous_time':ot,'cell':[x,y],'turn':c,'fuel_before_conflict':fuel}
            third+=count>=2
        else:count=0;fuel+=c=='L'
        seen[x,y]=(c,t,count+1);h=(h+(1 if c=='R' else -1))%4
        dx,dy=D[h];x+=dx;y+=dy
    return {'status':'UNKNOWN','tested':cap,'fuel':fuel,'third_or_later_events':third,'endpoint':[x,y,h]}

def main(cap):
    st=time.monotonic();a,b,ga,gb=inventory();phases=list(itertools.product(a,b));inner_phases=list(itertools.product(ga,gb));records=[];survivors=[];count={'phase_pairs':0,'rooted_cases':0,'CONFLICT':0,'UNKNOWN':0};latest=None
    for i,(u,v) in enumerate(phases):
        sub={'R':u,'L':v}
        for j,(s,t) in enumerate(inner_phases):
            count['phase_pairs']+=1
            U=''.join(sub[c] for c in s);V=''.join(sub[c] for c in t)
            assert footprint(U) is None or footprint(U)==((9,0),1)
            for root in 'RL':
                if {'R':U,'L':V}[root][0]!=root:continue
                count['rooted_cases']+=1;r=trial(U,V,root,cap);count[r['status']]+=1
                record={'outer_phase':i,'inner_phase':j,'root':root,**r};records.append(record)
                if r['status']=='UNKNOWN':survivors.append({**record,'outer':[u,v],'inner':[s,t],'composite':[U,V]})
                elif latest is None or r['time']>latest['time']:latest={**record,'outer':[u,v],'inner':[s,t]}
    out={'scope':'Two length-nine heading-preserving real-scale3 substitutions alternated between levels; only the composite length81 fixed point is required to be ant legal. The inner images may be internally ant-illegal. Outer images must be internally alternating because both symbols occur. Both prolongable roots tested. Prefix survivors remain UNKNOWN.','cap':cap,'R_images':a,'L_images':b,'phase_options':phases,'inner_phase_options':inner_phases,'inner_R_images':ga,'inner_L_images':gb,'counts':count,'latest_conflict':latest,'survivors':survivors,'records':records,'records_sha256':hashlib.sha256(json.dumps(records,sort_keys=True).encode()).hexdigest(),'seconds':time.monotonic()-st}
    p=Path(__file__).with_suffix('.json');p.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('records','phase_options','inner_phase_options','inner_R_images','inner_L_images','R_images','L_images')},indent=2))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--cap',type=int,default=6561);args=p.parse_args();main(args.cap)

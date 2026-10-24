#!/usr/bin/env python3
"""Finite exhaustive family plus a proved all-length signed-mass rejection.
A bounded prefix is never accepted as a positive realizability certificate.
"""
from search_turtle_substitutions import spec,trial
from itertools import product
from collections import defaultdict
from pathlib import Path
import json,time,hashlib

def run(k,limit=20000):
    start=time.monotonic();by=defaultdict(list)
    for bits in product('LR',repeat=k):
        w=''.join(bits);s=spec(w)
        if s:
            p,h,m=s
            if p[0]**2+p[1]**2>1 and h in[1,3]:by[p,h].append(w)
    total=mass=failed=0;maxfail=-1;record=None;surv=[];digest=hashlib.sha256();counts=defaultdict(lambda:[0,0,0])
    for (p,h),us in by.items():
        if h!=1:continue
        norm=p[0]**2+p[1]**2
        for u in us:
            if u[0]!='R':continue
            q=u.count('R')-u.count('L')
            for v in by.get(((-p[0],-p[1]),3),[]):
                total+=1;counts[norm][0]+=1;r=v.count('R')-v.count('L')
                if r==-q and (q<0 or q*q<=norm):
                    mass+=1;counts[norm][1]+=1;result={'rejected':'symmetric signed mass','q':q}
                else:
                    result=trial(u,v,limit)
                    if 'failure_time' in result:
                        failed+=1;counts[norm][2]+=1
                        if result['failure_time']>maxfail:maxfail=result['failure_time'];record={'R':u,'L':v,'scale':p,**result}
                    else:surv.append({'R':u,'L':v,'scale':p,**result})
                digest.update(json.dumps([u,v,p,result],sort_keys=True).encode()+b'\n')
    return {'length':k,'candidate_pairs':total,'signed_mass_rejections':mass,'finite_alternation_rejections':failed,'unresolved':surv,'latest_alternation_failure_time':maxfail,'latest_failure_example':record,'counts_by_scale_norm_squared':dict(counts),'all_candidate_record_sha256':digest.hexdigest(),'elapsed_seconds':time.monotonic()-start}

if __name__=='__main__':
    out=[]
    for k in [3,5,7,9,11,13,15,17]:
        r=run(k);out.append(r);print(json.dumps({k:v for k,v in r.items()if k not in ['counts_by_scale_norm_squared','unresolved']})+' unresolved='+str(len(r['unresolved'])),flush=True)
        (Path(__file__).resolve().parent/'short_selfsimilar_exclusion.json').write_text(json.dumps({'scope':'Uniform geometric turn substitutions, expanding nonzero complex scale, lengths3..17 odd. Analytic mass filter plus explicit finite failures; no accepted candidate.','results':out},indent=2)+'\n')

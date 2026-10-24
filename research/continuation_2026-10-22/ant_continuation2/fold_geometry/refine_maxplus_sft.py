"""Counterexample-guided search using exact finite-field SFT witnesses.

Only a final complete SFT pass can certify a candidate.  Nontermination,
weight drift or a complexity cap is recorded as an unresolved search.
"""
from pathlib import Path
import argparse
import json
import time
import numpy as np

from verify_maxplus_sft import ROOT, DATA, rot, run, context_data,head_index


def representation(black,pose,port=None):
    centers={(x-dx,y-dy) for x,y in black for dx in (-1,0,1) for dy in (-1,0,1)}
    out={head_index(pose[2],port):pose[1]}
    for x,y in centers:
        p=sum(1<<((dy+1)*3+dx+1) for dy in (-1,0,1) for dx in (-1,0,1)
              if (x+dx,y+dy) in black)
        assert p
        out[p]=max(out.get(p,-10**10),y)
    return out


def constraint(c,data):
    d=data[c['macro']];h=c['heading'];y0=c['start_y']
    black=set(map(tuple,c['initial_black']))
    toggled={(x,y+y0) for x,y in (rot(p,h) for p in d['odd_visits'])}
    pre=representation(black,(0,y0,h),d.get('source'))
    post=representation(black^toggled,c['post_head'],d.get('target'))
    return (np.array(list(pre),dtype=np.int64),np.array(list(pre.values()),dtype=np.int64),
            np.array(list(post),dtype=np.int64),np.array(list(post.values()),dtype=np.int64))


def relax(w,rows,maxpasses):
    w=np.array(w,dtype=np.int64)
    for it in range(maxpasses):
        old=w.copy()
        for pi,py,qi,qy in rows:
            top=np.max(w[pi]+py)
            w[qi]=np.minimum(w[qi],top-qy)
        if np.array_equal(w,old):
            return w.tolist(),True,it+1
        # Adding a common constant to all nonzero-pattern and head weights
        # changes E by that constant and leaves every transition inequality.
        shift=int(np.max(w[1:]))
        w[1:]-=shift
    return w.tolist(),False,maxpasses


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--weights',default=str(ROOT/'ant_continuation2/maxplus/sample_potential.json'))
    p.add_argument('--rounds',type=int,default=100)
    p.add_argument('--passes',type=int,default=2000)
    p.add_argument('--output',default=str(Path(__file__).with_name('maxplus_sft_refinement.json')))
    p.add_argument('--contexts')
    p.add_argument('--zero',action='store_true')
    p.add_argument('--port-head',action='store_true')
    args=p.parse_args()
    raw=json.loads(Path(args.weights).read_text());w=raw['weights']
    data=DATA if args.contexts is None else context_data(args.contexts,args.port_head)
    nports=1 if not args.port_head else 1+max(max(d['source'],d['target']) for d in data.values())
    if args.port_head and len(w)==516:w=w[:512]+w[512:]*nports
    contexts=[] if args.contexts is not None else raw.get('counterexamples',[]).copy()
    if args.zero:w=[0]*(512+4*nports);contexts=[]
    rows=[constraint(c,data) for c in contexts]
    logs=[];started=time.time();status='round limit reached; unresolved';tested_weights=w.copy()
    def save():
        out={'status':status,'weights':w,'contexts':len(contexts),'counterexamples':contexts,
             'templates':args.contexts,'port_head':args.port_head,'tested_weights':tested_weights,
             'log':logs,'elapsed_seconds':time.time()-started}
        Path(args.output).write_text(json.dumps(out,indent=2)+'\n')
    for iteration in range(args.rounds):
        tested_weights=w.copy()
        try:
            result=run(w,False,data,args.port_head)
        except ValueError as e:
            status='complexity cap; unresolved: '+str(e);save();print(status,flush=True);break
        fresh=result['counterexamples']
        log={k:v for k,v in result.items() if k not in ('counterexamples','status')}
        log.update({'iteration':iteration,'witnesses':len(fresh),'pattern_weight_range':
                    [min(w[1:512]),max(w[1:512])],'head_weight_range':[min(w[512:]),max(w[512:])]})
        if not args.port_head:log['head_weights']=w[512:]
        logs.append(log)
        print(log,flush=True)
        if not fresh:
            status='certified by exact finite-field SFT verification';save();break
        contexts.extend(fresh);rows.extend(constraint(c,data) for c in fresh)
        w,stable,passes=relax(w,rows,args.passes)
        log['relaxation_stable']=stable;log['relaxation_passes']=passes
        save()
        if not stable:
            status='relaxation pass cap; unresolved';save();print(status,flush=True);break
    else:save()
    print({'status':status,'contexts':len(contexts),'elapsed':time.time()-started},flush=True)


if __name__=='__main__':main()

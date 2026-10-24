"""Author-side complete flat-language and selected-prefix parity controls.
An independent replay must not import these constructors or this algorithm.
"""
import collections,itertools,json,pathlib,time
from flat_forced_seed import *


def decorate_with(model,source,child_index,U,V,cycle_length=1):
    """Replace one identity physical child by a lower recursive hairpin SCC."""
    phys=list(model.physical);images=[list(w) for w in model.images]
    old=images[source][child_index];h,turn=phys[old]
    assert turn==1
    # The canonical hairpin has parent R@N; rotating headings gives R@h.
    first=len(phys)
    def rot(s):return 2*((s//2+h)%4)+(s%2)
    for j in range(cycle_length):phys.append((h,1));images.append([])
    for j in range(cycle_length):
        images[first+j]=[rot(s) for s in word_states(U)]+[first+(j+1)%cycle_length]+[rot(s) for s in word_states(V,1)]
    images[source][child_index]=first
    return Model(phys,images,model.root)


def two_cycle():
    physical=standard_physical()+[(0,1),(0,1)];images=[[s] for s in range(8)]+[[],[]]
    images[8]=[9]+word_states('RRRR',1);images[9]=[8]
    return Model(physical,images,8)


def check(model,result,compiled,maxdepth=6,maxexponent=3):
    schemes=model.schemes();literal={};walk_coverage=0;prior_checks=0;maxleaf=0
    def instance(scheme,ns):
        chunks,t=scheme;path=[];j=0
        for cyc,es in chunks:
            path.extend(es*(ns[j] if cyc else 1))
            if cyc:j+=1
        return tuple(path)
    coverage=collections.Counter()
    for c,sch in zip(compiled,schemes):
        # Bounded language coverage uses depth rather than an arbitrary exponent
        # cap: no cycle can repeat more times than the target depth.
        for ns in itertools.product(range(maxdepth+1),repeat=len(c['variables'])):
            path=instance(sch,ns)
            if len(path)<=maxdepth:coverage[path]+=1
        for ns in itertools.product(range(maxexponent+1),repeat=len(c['variables'])):
            path=instance(sch,ns);r=len(path)
            if r not in literal:literal[r]=model.literal(r)
            reads=literal[r];index=0;s=model.root
            @functools.lru_cache(None)
            def length(s,r):return 1 if not r else sum(length(t,r-1) for t in model.images[s])
            p=(0,0)
            for d,e in enumerate(path):
                assert e.source==s
                index+=sum(length(t,r-d-1) for t in model.images[s][:e.index])
                p=(p[0]+e.offset[0],p[1]+e.offset[1]);s=e.target
            assert reads[index][0]==p and reads[index][2]==s==c['terminal']
            value=sum(q==p for q,turn,state in reads[:index])%2
            vals=dict(zip(c['variables'],ns));assert c['prior'].eval(**vals)==bool(value),(path,ns,value)
            required=reads[index][1]^value
            assert c['black'].eval(**vals)==bool(required)
            prior_checks+=1;maxleaf=max(maxleaf,len(reads))
    walks=[()]
    for d in range(maxdepth+1):
        for path in walks:
            assert coverage[path]==1,(path,coverage[path]);walk_coverage+=1
        walks=[path+(e,) for path in walks for e in model.phi[path[-1].target if path else model.root]]
    assert sum(coverage.values())==walk_coverage
    return dict(exact_walk_cover_checks=walk_coverage,selected_prior_parity_checks=prior_checks,
                largest_literal_block=maxleaf,max_scheme_cycles=max(len(c['variables']) for c in compiled),
                nontrivial_scc_sizes=sorted(len(c) for c in model.components if len(c)>1))


def main():
    start=time.monotonic();records=[]
    base=right_five_flat()
    # The rooted R5 image's first square child is R@E.
    models=[('two_state_recursive_cycle',two_cycle()),
            ('quadratic_nested_axial',decorate_with(base,8,1,'RRLRRRRL','LLRLLRLL')),
            ('quadratic_nested_oblique',decorate_with(base,8,1,'LRLLLLRRRRLRRL','RLRRLL',2)),
            ('cubic_mixed_recursive',None)]
    q=decorate_with(base,8,1,'RRLRRRRL','LLRLLRLL')
    # Its newly added axial SCC has a first R child, hence accepts another
    # rotated oblique recursive state beneath it.
    models[-1]=(models[-1][0],decorate_with(q,9,0,'LRLLLLRRRRLRRL','RLRRLL',2))
    for name,model in models:
        print('BEGIN',name,flush=True);result,compiled,relations,machines,shift=compile_requirements(model)
        assert not result['possible']
        extra=check(model,result,compiled)
        records.append(dict(name=name,result=result,checks=extra))
        print('RESULT',name,json.dumps(extra),flush=True)
    out=dict(records=records,seconds=time.monotonic()-start,
             scope='Author-side extended exact all-walk scheme and literal selected-prior parity controls. No independent signoff and no new accepted ant model.')
    (HERE/'extended_controls.json').write_text(json.dumps(out,indent=2)+'\n')
    print('DONE',out['seconds'],flush=True)
if __name__=='__main__':main()

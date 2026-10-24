#!/usr/bin/env python3
"""Independent literal controls for the analytic finite-order Perron obstruction."""
from fractions import Fraction
from itertools import product
from collections import Counter
import json,random,hashlib
from pathlib import Path
D=(1j,1,-1j,-1)
S=[(u,v) for u in range(4) for v in range(4) if (u-v)%2]
SI={s:i for i,s in enumerate(S)}
def tr(u,v):
    assert (v-u)%4 in (1,3)
    return 1 if (v-u)%4==1 else -1

def pal(k,v):
    ans=[]
    for bits in product((0,1),repeat=k):
        w=tuple(((v+j)%2)+2*b for j,b in enumerate(bits))
        if sum((D[z] for z in w),0j)==D[v]:ans.append(w)
    return ans

def weight(z,X,Y):return X**int(z.real)*Y**int(z.imag)

def run():
    rng=random.Random(826503)
    records=[]; checks=0
    for k in (5,9,13):
      domains=[pal(k,v) for v in range(4)]
      for rep in range(8):
        phi=[rng.choice(dom) for dom in domains]
        G=[w[-1] for w in phi]
        chi=[]; offsets=[]
        for u,v in S:
          prev=G[u]; row=[]; off=[]; z=0j
          for b in phi[v]:
            row.append(SI[prev,b]);off.append(z);z+=D[b];prev=b
          assert z==D[v]
          chi.append(row);offsets.append(off)
        words=[[v] for v in range(4)]
        typed=[[i] for i in range(8)]
        occ=[Counter({0j:(1 if u%2==0 else -1)*tr(u,v)}) for u,v in S]
        Gr=list(range(4))
        for r in range(4):
          for si,(u,v) in enumerate(S):
            prev=Gr[u]; literal=[]; z=0j; C=Counter()
            for b in words[v]:
              literal.append(SI[prev,b]);C[z]+=(1 if prev%2==0 else -1)*tr(prev,b)
              z+=D[b];prev=b
            assert literal==typed[si]
            assert z==D[v] and prev==Gr[v]
            assert {z:c for z,c in C.items() if c}=={z:c for z,c in occ[si].items() if c}
            for X,Y in ((Fraction(4),Fraction(5)),(Fraction(7,2),Fraction(9,2))):
              gam=(2/(Y+1),2/(X+1),-2*Y/(Y+1),-2*X/(X+1))
              kap=1-2/(X+1)-2/(Y+1); total=0;z=0j
              for state in typed[si]:
                a,b=S[state];d=(1 if a%2==0 else -1)*tr(a,b)
                g=gam[b]*weight(D[b],X,Y)-gam[a]-d
                assert g==kap+(4 if (a,b) in ((2,1),(3,0)) else 0)
                assert g>0;total+=weight(z,X,Y)*g;z+=D[b]
              boundary=gam[Gr[v]]*weight(D[v],X,Y)-gam[Gr[u]]
              assert total==boundary-sum((weight(z,X,Y)*c for z,c in C.items()),Fraction(0))
              checks+=1
          if r<3:
            words=[sum((list(phi[b]) for b in w),[]) for w in words]
            typed=[sum((chi[t] for t in w),[]) for w in typed]
            new=[]
            for si in range(8):
              out=Counter()
              for t,p in zip(chi[si],offsets[si]):
                for z,c in occ[t].items():out[z+p]+=c
              new.append(out)
            occ=new;Gr=[G[z] for z in Gr]
        records.append({'length':k,'images':phi,'last_map':G,'max_depth':3})
    result={'status':'PASS independent pair lift, exact Laurent occupation and positive clock telescoping',
      'models':len(records),'depth_state_checks':len(records)*4*8,'rational_clock_checks':checks,
      'scope':'Geometric controls only. The all-length contradiction is analytic, not inferred from these depths.',
      'records':records}
    out=Path(__file__).with_suffix('.json');out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='records'}))
if __name__=='__main__':run()

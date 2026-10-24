from pathlib import Path
import json,hashlib
SELF=Path(__file__).resolve();S=SELF.with_name('check_exceptional_return_map_independent.py');exec(compile(S.read_text().split('author=json.loads')[0],str(S),'exec'))
P=SELF;U=ROOT/'causal_reduction/unit_scale';J=json.loads((U/'old_side_fresh_cap_embedding_controls.json').read_text());F={complex(*q)for q in J['cap']};e=-d
M=set()
for q in Q:M.symmetric_difference_update({q})
assert len(M)==32
idx=lambda z,q: (int((z-q).real)//2 if (z-q).real==(z-q).imag and int((z-q).real)%2==0 else None)
past=lambda z:any((k:=idx(z,q))is not None and k<0 for q in Q)
causal=lambda z:sum((k:=idx(z,q))is not None and k<0 for q in M)%2
assert not any(past(q)for q in F)and p in F
# Fresh reverse history and complete stable replay, independently regenerated above.
bb=set(base);pp=p;hh=h;inverse=set()
for _ in range(10):
 z=pp-dirs[hh];inverse.add(z);hh=(hh+(-1 if z in bb else 1))%4;bb.symmetric_difference_update({z});pp=z
maxold=max(int(z.real)for z in set(A)|base|inverse)
_,_,_,incomingreads,_=run(base,p,h,104);maxold=max(maxold,max(int(z.real)for z in incomingreads))
T0=max(1,(maxold-min(int(z.real)for z in F))//2+1);assert T0==J['effective_T0']
ideal=[];tog=set();pp=r;hh=rh
for i in range(600):
 c='L'if bool(causal(pp))^(pp in F)^(pp in tog)else'R';ideal.append((pp,hh,c));tog.symmetric_difference_update({pp});hh=(hh+(1 if c=='R'else-1))%4;pp+=dirs[hh]
controls=[]
for row in J['controls']:
 n,T=row['n'],row['T'];FT=shift(F,T*e);initial=base|FT|{head+(11+n)*d};assert len(initial)==14+len(F)and min(z.real for z in FT)>maxold
 elapsed=52262+208*n+104*T;actual,pos,heading,_,word=run(initial,p,h,elapsed);pred=FT^shift(stable,-n*e)
 for j in range(n):pred^=shift(W,j*d)
 for j in range(-n,T):pred^=shift(M,j*e)
 assert actual==pred and(pos,heading)==(r+T*e,rh)
 for z,ih,c in ideal:
  assert (pos,heading)==(z+T*e,ih);got='L'if pos in actual else'R';assert got==c;actual.symmetric_difference_update({pos});heading=(heading+(1 if c=='R'else-1))%4;pos+=dirs[heading]
 controls.append(dict(n=n,T=T,initial_mass=len(initial),section_time=elapsed,section_mass=len(pred),matched_future=600))
out=dict(status='PASS independent full-field fresh-cap embedding controls and analytic ray separation',note_sha256=hashlib.sha256((U/'old_side_fresh_cap_embedding.md').read_bytes()).hexdigest(),T0=T0,controls=controls,scope='Any finite F disjoint from entire reverse strict-past READ set embeds after a large opposite longitudinal translate. Exact finite original mass14+|F|, only each fixed finite continuation lifts. Original archive retained and recedes locally; no all-future convergence or arbitrary edits to reverse-read past.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)

from pathlib import Path
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'global_biexterior_2026-10-23';prior=R/'audits/check_biexterior_return_independent.py';ns={'__file__':str(prior)};exec(prior.read_text().split('stats=Counter()')[0],ns);exterior,rectangles,inside,xy,dirs=(ns[k]for k in('exterior','rectangles','inside','xy','dirs'))
def step(B,p,h):
 ch='L'if p in B else'R';B.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;return p+dirs[h],h,ch
B=set();p=0j;h=0;checks=0;mass_control=[]
for t in range(1001):
 ext=exterior(B,p,h)
 if 7<=t<=10:mass_control.append(dict(t=t,p=xy(p),h=h,mass=len(B),exterior=list(ext)))
 if t==1000:break
 p,h,ch=step(B,p,h);new=exterior(B,p,h)
 if ch=='L'and all(ext):assert all(new)
 if ch=='R'and not all(ext):assert not all(new)
 checks+=1
assert[(r['mass'],r['exterior'])for r in mass_control]==[(5,[True,True]),(6,[True,False]),(7,[True,False]),(6,[True,True])]
assert mass_control[0]['p']==[0,1]and mass_control[-1]['p']==[-1,-1]
# Delete only complete separated exterior rectangles, and compare the stopping
# predicate itself at every actual state, not only turn words.
couplings=[]
for rad in(1,2,3):
 A={complex(x,y)for x in range(-rad,rad+1)for y in range(-rad,rad+1)};outer={complex(10+x,10+y)for x in range(2)for y in range(2)}|{complex(-10-x,12+y)for x in range(2)for y in range(2)}
 for h0 in range(4):
  full=A|outer;local=set(A);p=0j;h=h0;rr=next(r for r in rectangles(full)if inside(p,r));assert rr[4]==frozenset(A);t=0
  while True:
   a,b=exterior(full,p,h),exterior(local,p,h);assert a==b
   if all(a):break
   p1,h1,ch1=step(full,p,h);p2,h2,ch2=step(local,p,h);assert(p1,h1,ch1)==(p2,h2,ch2);p,h=p1,h1;t+=1
   assert full==local|outer and not local&outer
  couplings.append((rad,h0,t,len(local)))
note=D/'stateful_return_interface_addendum.md';assert hashlib.sha256(note.read_bytes()).hexdigest()=='5d4261a6cc2837eb8f365fcb111c4e3e0e17264e8fdf23b4206b09a2db74730d'
out={'status':'PASS exact bi-exterior event interface, intrinsic full-interior response and mass-growth control','note_sha256':hashlib.sha256(note.read_bytes()).hexdigest(),'one_step_checks':checks,'separated_full_field_couplings':couplings,'mass_growth_control':mass_control,'analytic':'Adding both white edges cannot lose infinity, and the moving w traverses the new edge. Deleting cannot enlarge a finite component; moving z stays in its old finite component. For a head inside fixed R, every possible enclosing black dual cycle is contained in R, not a different separated rectangle. Deleting exterior black cells therefore preserves BOTH finite/infinite statuses and the first-return stopping predicate, by first-difference induction; if the head exits R, it exits the entire rectangle union. Restore the unchanged exterior exactly. The time-zero normalizer is idempotent and take-one-step-then-normalize is a positive-time total full-state map.','scope':'No finite summary, mass descent, arbitrary exterior perturbation, global rank or capture. Exterior deletion is a proof coupling only, under explicit separated-rectangle/cycle-containment hypotheses.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(couplings)

from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];p=SELF.parent/'check_actual_zipper_spiral_independent.py';ns={'__file__':str(p)};exec(p.read_text().split('for q in (')[0],ns)
make,step,graph,ends,connected,rank,wvertex,phys=[ns[x]for x in('make','step','graph','ends','connected','rank','wvertex','phys')];component=ns['ns']['component'];controls=[]
for q in(1,2,3,4,8,12):
 vs,cs,runs=make(q,4);n=len(cs);d=vs[-1]-vs[-2];normalized=lambda z:(z-vs[-1])/d
 assert all(normalized(a).real<=-4 and normalized(b).real<=-4 for a,b in runs[:-1])
 spiralword=''.join('R'*(0 if i==0 else 1+int((vs[i+1]-vs[i])/(vs[i]-vs[i-1])==1j))+'L'for i in range(n))
 temp=set(cs);p=1+1j;h=1
 for c in spiralword:p,h,a=step(temp,p,h);assert a==c
 rod={p+i*(1j*(-1j)**h)for i in range(2*n+1)};assert not rod&set(cs)
 B=set(cs)|rod;initial=set(B);labels={z:'initial'for z in B};p=1+1j;h=1;kw=int(wvertex(p,h).real+wvertex(p,h).imag)%4
 assert len(B)==3*n+1 and rank(B,kw)==0 and component(B,kw,wvertex(p,h))[1]==B
 def run(word,label,ordinary=False):
  global p,h
  dead=[]
  for c in word:
   assert('L'if p in B else'R')==c
   if ordinary:
    for kk in(0,2):assert not connected(B-{p}if c=='L'else B,kk,*ends(p,kk))
   if c=='L':dead.append((p,labels.pop(p)))
   else:labels[p]=label
   p,h,a=step(B,p,h);assert a==c
  return dead
 a=run(spiralword,'spiral',True);b=run('LRRL'*n+'L','rod',True);assert len(a)+len(b)==3*n+1 and all(z=='initial'for _,z in a+b)
 S={z for z,l in labels.items()if l=='spiral'};R={z for z,l in labels.items()if l=='rod'};assert(len(S),len(R))==(n+q-2,2*n)
 assert not component(B,kw,wvertex(p,h))[1]
 # Complete marked graph at first output: carrying component plus disjoint1/2-edge stars.
 todo=set(B);large=None
 while todo:
  e=next(iter(todo));V,E=component(B,kw,ends(e,kw)[0]);todo-=E
  if E&R:assert R<=E and len(E&S)==1 and len(E)==2*n+1;large=E
  else:assert E<=S and len(E)<=2
 assert large is not None
 run('RRRRL','reset');assert len(component(B,kw,wvertex(p,h))[1])==2*n+1
 dead=run('LRRL'*n+'L','second',True);co=Counter(l for z,l in dead);assert co=={'rod':2*n,'spiral':1}
 assert len(B)==3*n+q and len({z for z,l in labels.items()if l=='spiral'})==n+q-3 and not component(B,kw,wvertex(p,h))[1]
 controls.append({'q':q,'n':n,'entry_mass':3*n+1,'first_length':6*n+q-1,'first_gain':q-3,'second_length':4*n+1,'second_gain':-1,'consumed_first_R':dict(co),'final_mass':len(B),'full_paired_forests_on_both_ordinary_pieces':True})
D=ROOT/'actual_zipper_spiral_2026-10-23';note=D/'mixed_spiral_rod_ownership.md';sha=hashlib.sha256(note.read_bytes()).hexdigest()
out={'status':'PASS all-q mixed spiral/rod w-routing and exact ownership; paired-forest assertions verified only for listed fixed controls','note_sha256':sha,'controls':controls,'analytic':['The signed spacing4 spiral endpoint formulas put every nonfinal run at normalized x<=-4 when the last endpoint is0 and last directionE; their written arms remain at x<=-3. The final-run teeth have roots x<=-1, with only the last tooth ending at(-1,-1). This holds uniformly for every q, including the empty earlier-run case q1.','The appended odd rod begins at the final extreme and its old w staircase is in x>=0. Its output also stays there except the initial tip(-1,-1), so its only contact with any earlier spiral output is the last tooth. This proves both that the originally supplied rod does not change the spiral trace and that the rod w routing has no remote shortcut.','The retained exact odd-rod rules execute(LRRL)^nL, resetRRRRL and the reverse output staircase. At the near end the last spiral tooth supplies an immediate r0 L, with no intervening write or connector. The resulting cursor root is isolated from every other spaced output star, so the second ordinary epoch is maximal.','The first epoch consumes all3n+1 original inputs and writes n+q-2 spiral plus2n rod outputs. Its complete w output graph is one2n+1 carrying path containing exactly one spiral tooth, plus disjoint1/2-edge spiral stars. The next ordinary epoch consumes all2n rod outputs and that one tooth, with no reset or same-epoch consumption. Thus the mixed application of the signed marked-path lemma has spiral-only load mu<=2.','The all-parameter claim here concerns literal w-routing and lifetime ownership. Complete opposite-graph forest/event assertions were checked at every update for the listed q values but are not promoted to an additional all-q theorem absent a separate dual-contact proof.'],'scope':'Finite charged gaining/carrying family, first gain q-3 and second gain-1. Not gain-bearing positive-positive regeneration, all-future limitation or global cubic sharpness.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha)

from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'actual_zipper_spiral_2026-10-23'
ns={'__file__':str(SELF.parent/'check_cycle_birth_finite_fuel_independent.py')};exec(Path(ns['__file__']).read_text().split('cells=')[0],ns)
ends,graph,component,rank,connected,step,wvertex=[ns[x]for x in('ends','graph','component','rank','connected','step','wvertex')]
xy=lambda p:(int(p.real),int(p.imag))
phys=lambda p:complex(2*p.real+2*p.imag+1,2*p.real-2*p.imag+1)
def cells(vs):return {(phys(a)+phys(b))/4 for a,b in zip(vs,vs[1:])}
def input_stitch(q):
 c=[0j]
 for i in range(q):
  for _ in range(12*((i+2)//2)):c.append(c[-1]+1j**i)
 v=[0j]
 for a,b in zip(c,c[1:]):
  e=b-a;dx=e.real-e.imag;dy=e.real+e.imag;v.extend([v[-1]+dx,v[-1]+dx+1j*dy])
 es=[b-a for a,b in zip(v,v[1:])];cr=lambda a,b:round(a.real*b.imag-a.imag*b.real);tr=[cr(a,b)for a,b in zip(es,es[1:])];st=set()
 for i in range(1,len(v)-2):
  if tr[i-1]==tr[i]==1:st|=cells([v[i]+es[i-1],v[i+1]+es[i-1]])
 v.append(v[-1]+es[-1]*(-1j));es.append(es[-1]*(-1j));word='L'+''.join('R'*(1+cr(a,b))+'L'for a,b in zip(es,es[1:]))
 return cells(v),st,word
results=[]
for q in(3,5):
 f=D/f'chronological_stitched_return_witness_q{q}.json';a=json.loads(f.read_text());B={complex(*p)for p in a['initial_black_cells']};initial=set(B);p=complex(*a['initial_pose'][0]);h=a['initial_pose'][1];k=int(wvertex(p,h).real+wvertex(p,h).imag)%4
 P,C,word=input_stitch(q);assert P.isdisjoint(C) and P|C<=B;G=B-P-C
 assert dict(input=len(P),stitch=len(C),guide=len(G))==a['initial_partition'];assert word==a['stages'][0]['word'];assert [rank(B,l)for l in(k,2-k)]==[1,0]
 lives={x:('input'if x in P else'stitch'if x in C else'guide',0,x)for x in B};born1=set();t=0;peak=len(B);summaries=[];initialPdeath=set();initialCdeath=set()
 for stage in a['stages']:
  name=stage['stage'];start=len(B);death=Counter();eventR=[0,0];eventL=[0,0];ex=[];r=0;count=Counter();born=set()
  assert (xy(p),h)==(tuple(stage['entry_pose'][0]),stage['entry_pose'][1])
  for j,ch in enumerate(stage['word']):
   assert (p in B)==(ch=='L');count[ch]+=1
   test=B-{p}if ch=='L'else B;ev=[connected(test,l,*ends(p,l))for l in(k,2-k)]
   t+=1
   if ch=='R':
    r+=1;lives[p]=(name,t,p);born.add(lives[p]);eventR=[u+int(v)for u,v in zip(eventR,ev)]
    if name=='first_R':born1.add(lives[p])
   else:
    life=lives.pop(p);death[life[0]]+=1;eventL=[u+int(v)for u,v in zip(eventL,ev)]
    if r>=3 or ev[0]:ex.append((j+1,r,ev[0],life[0],xy(p)))
    if name in('first_R','second_R'):assert r<=2 and not ev[0] and life not in born
    if name=='first_R':assert life[0]=='input';initialPdeath.add(p)
    if name=='second_R'and life[0]=='stitch':initialCdeath.add(p)
    r=0
   p,h,actual=step(B,p,h);assert actual==ch;peak=max(peak,len(B))
   # Incremental event identity is checked against full graph ranks at each stage.
  assert stage['word'].endswith('L') and r==0
  assert count=={'R':stage['R'],'L':stage['L']}
  assert (eventR,eventL,len(ex))==(stage['births_w_z'],stage['erasures_w_z'],stage['w_exceptional_blocks'])
  assert dict(death)==stage['deaths_by_origin'];assert len(B)-start==stage['gain'];assert [rank(B,l)for l in(k,2-k)]==stage['ranks_after']
  assert (xy(p),h)==(tuple(stage['exit_pose'][0]),stage['exit_pose'][1])
  if name=='transport_R':assert born1<=set(lives.values()) and len(ex)==2 and [z[1]for z in ex]==[1,4] and(p,h)==(3j,0)
  summaries.append(dict(stage=name,reads=len(stage['word']),L=count['L'],R=count['R'],gain=len(B)-start,births_w_z=eventR,erasures_w_z=eventL,exceptions=ex,deaths=dict(death)))
 assert initialPdeath==P and initialCdeath==C and not born1&set(lives.values())
 assert B=={complex(*p)for p in a['final_black_cells']}and(xy(p),h)==(tuple(a['final_pose'][0]),a['final_pose'][1]);assert len(B)==a['final_mass']and peak==a['max_mass']and t==a['T']
 assert Counter(v[0]for v in lives.values())==a['final_origin_counts']
 assert {(complex(*q0),cl,t0,complex(*q1))for q0,(cl,t0,q1)in a['final_lifetime_labels']}=={(q0,*v)for q0,v in lives.items()}
 assert not component(B,k,wvertex(p,h))[1];left=set(B);comps=[]
 while left:
  q0=next(iter(left));edges=component(B,k,ends(q0,k)[0])[1];left-=edges;comps.append(len(edges))
 assert sorted(comps,reverse=True)==[z['mass']for z in a['final_w_components']]
 assert not B&P and not B&C and len(B&G)==4
 # Check maximality beyond final stated epoch directly, without seed additions.
 bb=set(B);pp=p;hh=h;following=''
 for _ in range(5):pp,hh,ch=step(bb,pp,hh);following+=ch
 assert following=='RRRRL'
 # The optional actual predecessor is not falsely called a bridge.
 pp=1j;hh=2;pre=initial|{pp};assert pp not in initial
 assert connected(pre-{pp},k,*ends(pp,k));pp,hh,ch=step(pre,pp,hh);assert(pre,pp,hh,ch)==(initial,1+1j,1,'L')
 results.append(dict(q=q,witness_sha256=hashlib.sha256(f.read_bytes()).hexdigest(),initial_partition=a['initial_partition'],stages=summaries,total_reads=t,final_mass=len(B),final_origins=dict(Counter(v[0]for v in lives.values())),final_w_component_masses=sorted(comps,reverse=True),next_word=following,scope='Literal finite full board only; no all-q claim'))
note=D/'chronological_stitched_return.md';sha=hashlib.sha256(note.read_bytes()).hexdigest();assert sha=='f7c4a02972bd386a8a2908cd1f2a89d868a203949e4dc77265cf079cc336d1bb'
assert results[1]['witness_sha256']=='55ea923b2aef195bceb026bc3a64d246d6e96b88d002973eb59bbb0147a60d27'
out={'status':'PASS actual positive-positive chronological complete first-R recycling, q3 and q5 literal controls','note_sha256':sha,'controls':results,'analytic':['Every listed seed cell is installed before the first update, and no later board completion occurs. I independently reconstructed the input staircase and its charged stitch cells, then simulated the actual entire board and every lifetime; the remaining seed is the complete guide, including its initial w cycle.','The first epoch is w-ordinary and graph-event-free, with positive gain. Its immediately following transport begins with an actual old-cycle r1 L, making the first epoch maximal. All first-R lifetimes survive transport unchanged. Transport ends with r4 L at the actual favorable inner pose, not a reset teleport.','The second epoch is w-ordinary, consumes all first-R lifetimes, all charged old stitches and exactly two transport-R lifetimes, with no own-stage R death. It has positive gain. Its final active w component is empty, forcing the next RRRRL, so it too is maximal. Many opposite-graph births/erasures are present and explicitly counted.','The guide is charged and largely destroyed, final stitches/input cells are WHITE and the full output is fragmented. The optional actual L predecessor is a w-cycle erasure, not a bridge. Nothing establishes an all-q family, recurrence, unbounded bounded-renewal gain, or a noncapturing finite seed.'],'scope':'Independently replayed exact q3 and q5 witnesses. Author additional finite q7/q9/q15 controls and all-q routing are not needed or inferred by this audit.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print([(r['q'],r['initial_partition'],r['total_reads'],r['final_mass'])for r in results])

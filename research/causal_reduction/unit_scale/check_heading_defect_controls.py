"""Literal/circuit positive and negative controls for heading-defect models."""
from pathlib import Path
import itertools,json,random,collections
import check_heading_defect_backward_window as s
P=Path(__file__).resolve().parent

def literal(images,W,h):
 word=''.join(a[2] for row in images for a in row);rr,e,hh=s.s.old.old.core.trace(word,(0,0),h)
 last={};I=set();bad=[]
 for t,(q,g,c) in enumerate(rr):
  if q in last and last[q][1]==c:bad.append((q,last[q][0],t))
  if q not in last and c=='L':I.add(q)
  last[q]=(t,c)
 return dict(legal=not bad,length=len(word),input_mass=len(I),output_mass=sum(c=='R' for t,c in last.values()),read_cells=len(last),first_conflict=bad[:1])

def circuit_check(cut,choice):
 names,C,groups,domains,W,h0,bc=s.build(cut)
 values={names[f'x{r}_{j}_{k}']:choice[r][j]==k for r in range(7) for j in range(52) for k in range(8)}
 images=[[d[choice[r][j]] for j,d in enumerate(row)] for r,row in enumerate(domains)]
 states=[images[0][0][0]]+[a[1] for row in images for a in row]
 assert all(a[0]==states[r*52+j] for r,row in enumerate(images) for j,a in enumerate(row))
 values.update({names[f'h{j}']:bool(b) for j,b in enumerate(states)})
 possible=True
 for a,(q,ev) in enumerate(sorted(groups.items())):
  good=[]
  for initial in [False,True]:
   color=initial;v={names[f'input{a}']:color};ok=True
   for b,(event,xs) in enumerate(sorted(ev.items())):
    active=any(values[x] for x in xs);v[names[f'a{a}_{b}']]=active
    if active:
     if color!=(event[3]=='L'):ok=False
     color=not color
    v[names[f'b{a}_{b}']]=color
   if ok:good.append(v)
  if not good:possible=False
  else:values.update(good[0])
 z=literal(images,W,(h0+2*states[0])%4);assert possible==z['legal']
 if possible:
  assert C[16380]==bc
  assert all(any(values[abs(v)]==(v>0) for v in c) for c in C[:16380]+C[16381:])
 return dict(cut=cut,choices=choice,**z)

def main():
 z=json.loads((P/'heading_defect_pairs/cut1_root0_free.result.json').read_text())
 result=[];mix=[];rng=random.Random(312104)
 for cut in [0,1]:
  names,C,groups,domains,W,h0,bc=s.build(cut)
  result.append(circuit_check(cut,[[0]*52 for _ in range(7)]))
  for r in range(16):
   states=[rng.randrange(2) for _ in range(365)]
   choice=[[4*states[52*a+j]+(rng.randrange(1,4) if states[52*a+j+1] else 0) for j in range(52)] for a in range(7)]
   result.append(circuit_check(cut,choice))
  if cut==1:
   pchoice=[next(k for k,a in enumerate(d) if list(a)==z['images'][j]) for j,d in enumerate(domains[0])]
   for bits in itertools.product([0,1],repeat=7):
    choice=[pchoice if b else [0]*52 for b in bits]
    images=[[d[choice[r][j]] for j,d in enumerate(row)] for r,row in enumerate(domains)]
    rec=literal(images,W,h0);assert rec['legal'];rec['bits']=bits
    assert rec['input_mass']==97-sum(bits)
    assert rec['output_mass']==13+3*sum(bits)
    mix.append(rec)
   for bits in [(1,)*7,(0,1,0,1,0,1,0),(1,0,1,0,1,0,1)]:result.append(circuit_check(cut,[pchoice if b else [0]*52 for b in bits]))
 out=dict(circuit_controls=len(result),circuit_legal=sum(v['legal'] for v in result),records=result,binary_mixture_controls=mix)
 (P/'heading_defect_local_classification/controls.json').write_text(json.dumps(out,indent=2)+'\n')
 print(out['circuit_controls'],out['circuit_legal'],'mixed',len(mix))
if __name__=='__main__':main()

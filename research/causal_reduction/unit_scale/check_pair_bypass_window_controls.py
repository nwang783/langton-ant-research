from pathlib import Path
import json,random
import check_pair_bypass_local_window as s
P=Path(__file__).resolve().parent

def test(cut,choice):
 names,C,groups,word,h=s.build(cut)
 values={names[f'x{r}_{j}_{k}']:choice[r][j]==k for r in range(7) for j in range(52) for k in range(3)}
 images=[[s.s.PAL[word[2*j:2*j+2]][choice[r][j]] for j in range(52)] for r in range(7)]
 w=''.join(a for row in images for a in row);rr,e,hh=s.s.old.core.trace(w,(0,0),h)
 last={};literal=True;I=set();black=set();read=set()
 for q,hh,c in rr:
  if q in last and last[q]==c:literal=False
  if q not in last and c=='L':I.add(q)
  last[q]=c;read.add(q)
 black={q for q,c in last.items() if c=='R'}
 # Each free entry cell has exactly two possible initial bits. Enumerate
 # those two, not boards or controller assignments.
 circuit=True
 for a,(q,ev) in enumerate(sorted(groups.items())):
  good=[]
  for start in [False,True]:
   b=start;v={names[f'input{a}']:start};ok=True
   for j,(event,xs) in enumerate(sorted(ev.items())):
    active=any(values[x] for x in xs);v[names[f'a{a}_{j}']]=active
    if active:
     if b!=(event[3]=='L'):ok=False
     b=not b
    v[names[f'b{a}_{j}']]=b
   if ok:good.append(v)
  if not good:circuit=False
  else:values.update(good[0])
 assert circuit==literal
 central=any(choice[3])
 if circuit:
  # Omit only the central-bypass clause for the identity positive control.
  cc=C[:1456]+C[1457:];assert len(C[1456])==104
  assert all(any(values[abs(v)]==(v>0) for v in z) for z in cc)
 return dict(cut=cut,length=len(w),legal=literal,central_bypass=central,input_mass=len(I),output_mass=len(black),read_cells=len(read),choices=choice)

def main():
 rng=random.Random(1045252);records=[]
 for cut in [0,1]:
  records.append(test(cut,[[0]*52 for _ in range(7)]))
  for n in range(24):
   choices=[[0]*52 for _ in range(7)]
   for k in rng.sample(range(364),n+1):choices[k//52][k%52]=rng.choice([1,2])
   records.append(test(cut,choices))
 out=dict(controls=len(records),legal=sum(z['legal'] for z in records),records=records)
 (P/'pair_bypass_local_window/controls.json').write_text(json.dumps(out,indent=2)+'\n')
 print(out['controls'],out['legal']);print([{k:v for k,v in z.items() if k!='choices'} for z in records if z['legal']])
if __name__=='__main__':main()

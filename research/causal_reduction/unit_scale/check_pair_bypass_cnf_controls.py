from pathlib import Path
import random,json
import synthesize_pair_bypass_scaffold as s
from check_pair_bypass_scaffold import histories
P=Path(__file__).resolve().parent

def evaluate(cut,choices):
 names,C,groups,rails,conflicts,word,h=s.build(cut,'free',False)
 images=[s.PAL[word[2*j:2*j+2]][choices[j]] for j in range(52)]
 literal=histories(''.join(images),h)
 # With choices fixed, every active-event bit and every post-read bit is
 # deterministic once the one free input bit on an orbit is selected.
 values={names[f'x{j}_{k}']:choices[j]==k for j in range(52) for k in range(3)}
 possible=True
 for a,(orbit,ev) in enumerate(sorted(groups.items())):
  accepted=[]
  for initial in [False,True]:
   color=initial;v={names[f'input{a}']:color};ok=True
   for b,(event,xs) in enumerate(sorted(ev.items())):
    active=any(values[x] for x in xs);v[names[f'a{a}_{b}']]=active
    if active:
     if color!=(event[3]=='L'):ok=False
     color=not color
    v[names[f'b{a}_{b}']]=color
   if ok:accepted.append(v)
  if not accepted:possible=False
  else:values.update(accepted[0])
 assert possible==(literal['status']=='LEGAL_PREPARED_PERIODIC')
 if possible:assert all(any(values[abs(x)]==(x>0) for x in c) for c in C)
 return dict(cut=cut,choices=choices,length=len(''.join(images)),legal=possible,conflicts=len(literal['conflicts']))

def main():
 r=random.Random(912601);records=[]
 for cut in [0,1]:
  records.append(evaluate(cut,[0]*52))
  for j in range(12):
   choices=[0]*52
   for p in r.sample(range(52),j+1):choices[p]=r.choice([1,2])
   records.append(evaluate(cut,choices))
  for j in range(12):records.append(evaluate(cut,[r.randrange(3) for _ in range(52)]))
 out=dict(controls=len(records),legal=sum(v['legal'] for v in records),records=records)
 (P/'pair_bypass_simultaneous/controls.json').write_text(json.dumps(out,indent=2)+'\n')
 print(out['controls'],out['legal'])
if __name__=='__main__':main()

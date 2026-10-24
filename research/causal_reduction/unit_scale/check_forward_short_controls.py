from pathlib import Path
import json,random
import synthesize_multirail_short_refinement as s
P=Path(__file__).resolve().parent

def align(word):
 states={0:[]}
 for c in s.H:
  states={n+len(w):ks+[k] for n,ks in states.items() for k,w in enumerate(s.core.dom[c]) if word.startswith(w,n)}
 return states[len(word)]

def test(choice,mode='free'):
 names,C,groups,rails,conflicts,inp=s.build(s.H,mode)
 values={names[f'x{j}_{k}']:choice[j]==k for j,c in enumerate(s.H) for k in range(len(s.core.dom[c]))}
 values[names['TRUE']]=True
 values.update({r['selector']:False for r in rails})
 word=''.join(s.core.dom[c][choice[j]] for j,c in enumerate(s.H));rr,e,h=s.core.trace(word,(0,0),3);assert(e,h)==((-2,-2),3)
 by={}
 for t,(q,h,c) in enumerate(rr):by.setdefault(s.key(q),[]).append((t+len(word)*(q[0]//2),c))
 bad=False;I=set()
 for q,hs in by.items():
  hs.sort();bad|=any(a[1]==b[1] for a,b in zip(hs,hs[1:]))
  if hs[0][1]=='L':I.add(q)
 possible=True
 for a,(orb,ev) in enumerate(sorted(groups.items())):
  valid=[]
  for init in [False,True] if mode=='free' else [False]:
   color=init;v={names[f'input{a}']:color};ok=True
   for b,(event,xs) in enumerate(sorted(ev.items())):
    active=any(values[x] for x in xs);v[names[f'a{a}_{b}']]=active
    if active:
     if color!=(event[3]=='L'):ok=False
     color=not color
    v[names[f'b{a}_{b}']]=color
   if ok:valid.append(v)
  if not valid:possible=False
  else:values.update(valid[0])
 assert possible==(not bad and (mode=='free' or not I))
 if possible:assert all(any(values[abs(x)]==(x>0) for x in c) for c in C)
 return dict(mode=mode,choice=choice,word=word,legal=possible,input_black_classes=sorted(I),length=len(word))

def main():
 Q=json.loads((P/'forward108_prepared_control.json').read_text())['word'];qc=align(Q)
 records=[test([0]*104,'rails'),test(qc)]
 rng=random.Random(104108)
 for n in range(24):
  c=[0]*104
  for j in rng.sample(range(104),n+1):c[j]=rng.randrange(1,10)
  records.append(test(c))
 out=dict(controls=len(records),legal=sum(z['legal'] for z in records),Q_alignment=qc,records=records)
 (P/'forward_short_multirail/controls.json').write_text(json.dumps(out,indent=2)+'\n');print(out['controls'],out['legal'])
if __name__=='__main__':main()

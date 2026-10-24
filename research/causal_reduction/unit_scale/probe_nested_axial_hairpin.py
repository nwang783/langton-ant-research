"""Targeted one-child hierarchy inside the signed axial hairpin, not a length scan."""
from pathlib import Path
import sys,json,hashlib
sys.path.insert(0,str(Path(__file__).parents[2]/'computability'/'flat_exact_validator'))
from macro_forced_seed import MacroModel,physical_trace
P=Path(__file__).parent
U='RRLRRRRL';V='LLRLLRLL';W=U+'R'+V

def states(word,h):
 out=[]
 for c in word:
  out.append(2*h+(c=='L'));h=(h+(1 if c=='R' else -1))%4
 return out

def build(j):
 bases=[(h,t) for h in range(4) for t in 'RL'];images=[[s] for s in range(8)]
 b=8;c=9;h=physical_trace(W,0)[0][j][2]
 turn=physical_trace(W,0)[0][j][1]
 bases += [(0,'R'),(h,'L' if turn else 'R')]
 bi=states(W,0);bi[8]=b;bi[j]=c
 cw=W.translate(str.maketrans('RL','LR')) if turn else W
 ci=states(cw,h);ci[8]=c
 images += [bi,ci]
 return MacroModel(bases,images,b)

def check(model,r):
 reads=model.literal(r);last={};I=set();B=set()
 for t,(p,turn,s) in enumerate(reads):
  if p not in last:
   if turn:I.add(p);B.add(p)
  elif last[p][1]==turn:
   return dict(depth=r,length=len(reads),conflict=dict(cell=p,previous=last[p],current=[t,turn,s]))
  if p in B:B.remove(p)
  else:B.add(p)
  last[p]=[t,turn,s]
 return dict(depth=r,length=len(reads),input_mass=len(I),output_mass=len(B),support=len(last))

def main():
 rows=physical_trace(W,0)[0];out=[]
 for j,(p,t,h) in enumerate(rows):
  if h%2:
   m=build(j);checks=[]
   for r in range(7):
    z=check(m,r);checks.append(z)
    if 'conflict' in z:break
   out.append(dict(child_index=j,child_offset=p,child_heading=h,child_turn='L' if t else 'R',ray=[0,(-2 if h==1 else 2)*(-1 if t else 1)],checks=checks))
 result=dict(scope=__doc__,cases=out,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
 (P/'nested_axial_hairpin_probe.json').write_text(json.dumps(result,indent=2)+'\n')
 for x in out:print(x)
if __name__=='__main__':main()

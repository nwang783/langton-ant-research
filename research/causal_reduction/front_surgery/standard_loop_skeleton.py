"""Extract an exact chronological backbone and its seven deleted loop words."""
import json
from loop_decoration_solver import ROOT,walk

def skeleton():
 w=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];st=[]
 for i,c in enumerate(w):
  if st and st[-1][0]==c:
   a,ix=st.pop();ix.append(i)
   if len(ix)<4:st.append((a,ix))
  else:st.append((c,[i]))
 ids=[i for c,ix in st for i in ix];base=''.join(w[i] for i in ids);loops={};old=-1
 for j,i in enumerate(ids):
  if i>old+1:loops[j]=w[old+1:i]
  old=i
 assert old+1==len(w)
 assert all(walk(v)[1]==(0,0,0) for v in loops.values())
 assert ''.join(loops.get(i,'')+c for i,c in enumerate(base))==w
 return base,loops,w

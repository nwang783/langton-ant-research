"""Fresh fine-step ant DFS; no saved image palette or author search imports.
Identity/nine macro endpoints are checked directly against earlier actual poses.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];J=json.loads((ROOT/'causal_reduction/unit_scale/probe_occurrence_transport.json').read_text())
results=[]
for rootturn in ['R','L']:
 states=0;fine=0;latest=0;maxmac=0;visited=[]
 def macro(i,positions,headings,turns,colors,macros):
  global states,fine,latest,maxmac
  states+=1;maxmac=max(maxmac,i);latest=max(latest,len(turns));assert i<1000
  if i==0:
   coarse_turn=rootturn;target_h=1j*(-1j if rootturn=='R'else 1j);target_p=target_h
  else:
   assert positions[-1]==positions[i]and headings[-1]==headings[i]
   coarse_turn=turns[i];target_h=headings[i+1];target_p=positions[i+1]
  sign=1 if coarse_turn=='R'else -1
  for length in ([9]if i==0 else[1,9]):
   def walk(j,excess,ps,hs,ts,board,word):
    global fine
    fine+=1
    if j==length:
     if excess==sign and ps[-1]==target_p and hs[-1]==target_h:
      visited.append((tuple(macros+[word]),len(ts)))
      macro(i+1,ps,hs,ts,board,macros+[word])
     return
    p=ps[-1];h=hs[-1]
    choices=[('L'if board[p]else'R')]if p in board else['R','L']
    if not ts:choices=[c for c in choices if c==rootturn]
    for c in choices:
     s=1 if c=='R'else -1
     if abs(sign-excess-s)>length-j-1:continue
     nh=h*(-1j if c=='R'else 1j);np=p+nh;nb=dict(board);nb[p]=(c=='R')
     walk(j+1,excess+s,ps+[np],hs+[nh],ts+[c],nb,word+c)
   walk(0,0,positions,headings,turns,colors,'')
 macro(0,[0j],[1j],[],{},[])
 assert(states,latest,maxmac)==(53,39,7)
 data=json.dumps(visited,separators=(',',':')).encode()
 results.append(dict(root=rootturn,complete_macro_nodes=states,fine_search_nodes=fine,last_macro_boundary=latest,largest_coarse_index=maxmac,accepted_macro_history_sha256=hashlib.sha256(data).hexdigest()))
out=dict(status='PASS controller-free occurrence-dependent identity/nine unit self-embedding exclusion',results=results,scope='Equal actual coarse/fine positions AND incoming headings, each macro length1 or9 and charge equal to its coarse turn, at least one9. Normalize at the first9; arbitrary initial coloring. No eventual offsets, unit rotations, other lengths, or heading-free extension.',note='The DFS branches only on genuinely unknown current cell colors and directly tests endpoints/charge; no precomputed image palette or controller consistency is assumed.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

"""Necessary finite-type languages for arbitrary k9,a3 inflations.
No nonempty output is an existence certificate.
"""
import json,pathlib,itertools,collections,time
from search_complementary_roots import D
HERE=pathlib.Path(__file__).resolve().parent

def feasible(word):
 x=y=h=0;last={}
 for c in word:
  p=x,y
  if last.get(p)==c:return False
  last[p]=c;h=(h+(1 if c=='R'else-1))%4;dx,dy=D[h];x+=dx;y+=dy
 return True

def run(order):
 r=next(z for z in json.load(open(HERE/'free_inflations_k9.json'))['results']if z['scale']==[3,0]);words=r['images']['R']+r['images']['L'];colors='R'*9+'L'*9
 allowed={z for z in itertools.product(range(18),repeat=order)if feasible(''.join(words[i]for i in z))};history=[]
 while True:
  states={z[:-1]for z in allowed}|{z[1:]for z in allowed};out=collections.defaultdict(list)
  for z in allowed:out[z[:-1]].append((z[1:],colors[z[-1]],z[-1]))
  def accepts(w,initial_symbol=None):
   ss={s for s in states if ''.join(colors[i]for i in s)==w[:order-1]and(initial_symbol is None or s[0]==initial_symbol)}
   for c in w[order-1:]:
    ss={v for s in ss for v,d,i in out[s]if d==c}
    if not ss:return False
   return bool(ss)
  root=[i for i,w in enumerate(words)if w[0]==colors[i]and accepts(w,i)]
  new={z for z in allowed if accepts(''.join(words[i]for i in z))}
  history.append(dict(edges=len(allowed),states=len(states),roots=root,next_edges=len(new)));print('ROUND',order,history[-1],flush=True)
  if new==allowed or not new:break
  allowed=new
 return dict(order=order,words=words,colors=colors,history=history,allowed=sorted(new),status='NECESSARY_LANGUAGE_NONEMPTY'if new and root else'EXCLUDED_BY_EMPTY_ROOT_OR_LANGUAGE')
if __name__=='__main__':
 import sys
 order=int(sys.argv[1])if len(sys.argv)>1 else 2
 result=run(order);(HERE/f'renormalized_macro_grammar_order{order}.json').write_text(json.dumps(result,indent=2))

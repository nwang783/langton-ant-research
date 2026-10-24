from pathlib import Path
from collections import defaultdict,deque,Counter
import ast,json
base=Path(__file__).parent;L={'__file__':str(base/'explore_two_flat_pair_reader_closure.py')};exec((base/'explore_two_flat_pair_reader_closure.py').read_text().split('stats=Counter();answers=[]')[0],L)
V,out,cnt,fp=L['V'],L['out'],L['cnt'],L['fp'];j=json.loads((base/'check_LL_cyclic_supplier_reactivation_modes.json').read_text());a=next(a for r in j['roots']if r['root']=='EWWE'for a in r['cyclic_necessary_profiles']if a['kind']=='P');fixed={ast.literal_eval(p):h for p,h in a['histories'].items()}|{(1,-1):'SNNS',(2,-1):'WEEW'}
def val(hs):
 eq={}
 for p,h in hs.items():
  ia='NS'if sum(p)%2==0 else'EW';oa='EW'if sum(p)%2==0 else'NS'
  for d in oa:eq[p,d]=cnt(h,d,'out')
  for d in ia:
   q=p[0]-V[d][0],p[1]-V[d][1];n=cnt(h,d,'in')
   if(q,d)in eq:assert eq[q,d]==n
   eq[q,d]=n
 adj=defaultdict(list)
 for(p,d),f in eq.items():
  c,l=fp(p,d);adj[l].append((c,f));adj[c].append((l,-f))
 values={(0,-1):0};qu=deque(values)
 while qu:
  p=qu.popleft()
  for q,w in adj[p]:
   if q in values:assert values[q]==values[p]+w
   else:values[q]=values[p]+w;qu.append(q)
 return values
rs=json.loads((base/'explore_even_nested_reader_last_supplier_square.json').read_text())['rows'][0]['open']
res=[]
for r in rs:
 if not all(len(r[n])%2==0 for n in'FGH'):continue
 hs=fixed|{(2,-2):r['F'],(3,-1):r['G'],(3,-2):r['H']};vs=val(hs);p=(3,-2);h=r['H'];c=fp(p,out(h,0))[0]if h else None
 levels={n:vs[fp(p0,out(hs[p0],0))[0]]for n,p0 in [('F',(2,-2)),('G',(3,-1))]}
 res.append(r|dict(H_firstR_C=vs[c]if c else None,F_G_levels=levels,H_C_faces={str(q):vs[q]for q in[(3,-2),(2,-3)]}))
for r in res:print(r)

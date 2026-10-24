"""Connected prepared49 even portal with initial head OUTSIDE all four
WHITE target cells; every target R0 arrival has an actual physical supplier.
NOT a complete WHITE translating front/controller or period-field equality.
"""
from pathlib import Path
from collections import Counter,defaultdict
import json
base=Path(__file__).parent;j=json.loads((base/'check_prepared_F48_even_one_use_portal.json').read_text());H='NESW';V={'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
seed={tuple(p)for p in j['initial_black']}|{(0,-1)};word='L'+j['word'];black=set(seed);p=(0,-1);h='E';hist=defaultdict(list);edges=Counter();tr=[]
for t,w in enumerate(word):
 a='L'if p in black else'R';assert a==w;oldp=p;oldh=h;before=sorted(black)
 if p in black:black.remove(p)
 else:black.add(p)
 h=H[(H.index(h)+(1 if a=='R'else-1))%4];p=p[0]+V[h][0],p[1]+V[h][1];edges[oldp,p]+=1
 e=dict(t=t,cell=oldp,incoming=oldh,turn=a,black_before=before,black_after=sorted(black),next_cell=p,next_incoming=h);tr.append(e);hist[oldp].append(e)
assert len(word)==49 and len(seed)==13 and len(black)==16 and(p,h)==((0,2),'N')and p in black
for q,w in{(0,0):'NNSS',(1,0):'EE',(1,1):'SN',(0,1):'EWWE'}.items():
 assert q not in seed and ''.join(e['incoming']for e in hist[q])==w
 # Now every incoming read has its genuine preceding actual edge, including rank0.
 for e in hist[q]:assert e['t']>0 and tr[e['t']-1]['next_cell']==q
assert edges[(1,2),(1,1)]==1 and edges[(1,0),(1,-1)]==1 and max(map(len,hist.values()))==4
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,word=word,initial_black=sorted(seed),start=[(0,-1),'E'],end=[p,h],mass=[len(seed),len(black)],final_black=sorted(black),trace=tr,target_histories={str(q):dict(incoming=''.join(e['incoming']for e in hist[q]),turns=''.join(e['turn']for e in hist[q]),times=[e['t']for e in hist[q]])for q in[(0,0),(1,0),(1,1),(0,1)]},factor_max_reads=4,every_target_R0_physically_supplied=True,warning='Extra initialBLACK cell(0,-1) suppliesZ.R0 through a BLACK-firstL. The full outside history is NOT WHITE; no front/quotient translation or immediate repetition claimed.'),indent=2)+'\n');print('PASS preparedF49: external BLACK entry,all12WHITEtargetarrivals supplied,13->16,max4')

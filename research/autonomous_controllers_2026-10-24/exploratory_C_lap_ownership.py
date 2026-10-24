from collections import defaultdict
from pathlib import Path
import json
from check_extremal_read_coupling import event_word,quotient
from check_all_cut_wave_interfaces import WORDS
from certify_active_C_entry_exit_forests import active_C
D=[(0,1),(1,0),(0,-1),(-1,0)]

def build(w,h0=0):
 E,d,_=event_word(w,h=h0)
 cut=(max(e['t'] for e in E if e['c']=='L')+1)%len(w)
 h=E[cut]['hi'];p=E[cut]['p'];w=w[cut:]+w[:cut]
 chunks=w.split('L')[:-1];assert w.endswith('L');ks=list(map(len,chunks));N=len(ks)
 assert set(ks)<=set([0,1,2,4]);opts=[i for i,k in enumerate(ks) if k in (0,4)]
 H=defaultdict(list);meta={};chosen={i:int(ks[i]==4) for i in opts};cursor=[]
 def ev(i,j,p,kind,var=None):
  q,k=quotient(p,d);x={'block':i,'slot':j,'p':p,'class':q,'lift':k,'order':(i-N*k,j),'kind':kind,'var':var}
  H[q].append(x);return x
 for i,k in enumerate(ks):
  a=active_C(p,h);cursor.append((p,h,a))
  if i in opts:
   pp,hh=p,h;ee=[]
   for j in range(4):
    ee.append(ev(i,j,pp,'R',i));hh=(hh+1)%4;pp=(pp[0]+D[hh][0],pp[1]+D[hh][1])
   assert (pp,hh)==(p,h);meta[i]=ee
  else:
   for j in range(k):
    ev(i,j,p,'R');h=(h+1)%4;p=(p[0]+D[h][0],p[1]+D[h][1])
  ev(i,4,p,'L');h=(h-1)%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 for hs in H.values():hs.sort(key=lambda e:e['order'])
 return dict(word=w,cut=cut,drift=d,heading=E[cut]['hi'],position=E[cut]['p'],ks=ks,optional=opts,chosen=chosen,histories=H,cursors=cursor)

def constraints(z,white=True):
 cons=[];bad=[]
 def con(q,typ,es,target):
  cons.append({'class':q,'type':typ,'vars':[e['var'] for e in es], 'target':target})
 for q,hs in z['histories'].items():
  mm=[j for j,e in enumerate(hs) if e['var'] is None]
  if not mm:
   con(q,'all_optional',hs,'<=1');continue
  a=mm[0];b=mm[-1]
  con(q,'prefix_'+hs[a]['kind'],hs[:a],0 if hs[a]['kind']=='R' else (1 if white else '<=1'))
  for x,y in zip(mm,mm[1:]):
   pair=hs[x]['kind']+hs[y]['kind'];es=hs[x+1:y]
   if pair=='RR':bad.append({'class':q,'type':'mandatory_RR','events':[hs[x],hs[y]]})
   con(q,pair,es,1 if pair=='LL' else 0)
  con(q,'suffix_'+hs[b]['kind'],hs[b+1:],0 if hs[b]['kind']=='R' else '<=1')
 return cons,bad

def propagate(z,white=True):
 cons,bad=constraints(z,white);vals={};proof=[]
 if bad:return False,vals,[bad[0]],cons
 while True:
  change=False
  for j,c in enumerate(cons):
   known=sum(vals.get(v,0) for v in c['vars']);unknown=[v for v in c['vars'] if v not in vals];t=c['target'];cap=1 if t=='<=1' else t
   if known>cap or (t!='<=1' and known+len(unknown)<cap):
    return False,vals,proof+[{'conflict':j,'constraint':c,'known':known,'unknown':unknown}],cons
   forced=None
   if known==cap:forced=0
   elif t!='<=1' and known+len(unknown)==cap:forced=1
   if forced is not None:
    for v in set(unknown):
     vals[v]=forced;proof.append({'constraint':j,'var':v,'value':forced});change=True
  if not change:break
 return True,vals,proof,cons

if __name__=='__main__':
 W={**WORDS,'M10':'RRRRLLLLRL','F80':json.loads(Path('prepared80_budget_falsifier_independent_confirmation.json').read_text())['word']}
 for n,w in W.items():
  z=build(w)
  for white in [False,True]:
   ok,v,pr,c=propagate(z,white)
   print(n,'white',white,'L',len(z['ks']),'lapvars',len(z['optional']),'constraints',len(c),'ok',ok,'forced',len(v),'free',len(z['optional'])-len(v),'steps',len(pr),'bad',pr[-1] if not ok else '')
   if not white:
    assert ok
    assert all(z['chosen'][k]==v[k] for k in v)
    assert all((sum(z['chosen'][v] for v in c0['vars'])<=1 if c0['target']=='<=1' else sum(z['chosen'][v] for v in c0['vars'])==c0['target']) for c0 in c)

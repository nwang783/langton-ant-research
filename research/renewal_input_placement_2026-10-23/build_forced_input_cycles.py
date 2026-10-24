"""Explicit translated cycle witnesses for old-input exceptional updates.
The all-N theorem uses these finite witnesses and affine copy eligibility,
not an inference from the measured examples or an infinite background.
"""
from probe_renewal_input_ages import *
from collections import Counter
OUT=Path(__file__).parent
V=((0,1),(1,0),(0,-1),(-1,0))

def deterministic_trace(word,p,h):
 out=[]
 for t,c in enumerate(word):
  out.append((p,h,c));h=(h+(1 if c=='R'else -1))%4;d=V[h];p=(p[0]+d[0],p[1]+d[1])
 return out,p,h

def infer_input(word,p,h):
 tr,end,eh=deterministic_trace(word,p,h);first={};last={};B=set()
 for t,(q,hh,c) in enumerate(tr):
  if q in last:assert c!=last[q]
  else:
   first[q]=c
   if c=='L':B.add(q)
  last[q]=c
 return B,tr,end,eh

def graph_path(G,q):
 s,t=endpoints(q,G.k);todo=deque([s]);par={s:None}
 while todo:
  v=todo.popleft()
  if v==t:break
  for u,e in G.g.get(v,{}).items():
   if e==q or u in par:continue
   par[u]=(v,e);todo.append(u)
 if t not in par:return None
 path=[]
 while t!=s:t,e=par[t];path.append(e)
 return path[::-1]

def word_data(which):
 fn='prepared_travelling_wave_certificate.json'if which==1564 else'second_prepared_wave_certificate.json'
 W=json.loads((ROOT/'nonlinear_global_budget_2026-10-23'/fn).read_text())['word']
 p,h=((-6,-6),0)if which==1564 else((-2,3),3)
 tr,end,eh=deterministic_trace(W,p,h);assert eh==h;d=(end[0]-p[0],end[1]-p[1])
 return W,p,h,tr,d

def occurrences(q,tr,d):
 occ=[]
 for i,(p,h,c)in enumerate(tr):
  delta=(q[0]-p[0],q[1]-p[1])
  if delta[0]*d[1]!=delta[1]*d[0]:continue
  a=None
  for j in(0,1):
   if d[j]:
    if delta[j]%d[j]:break
    z=delta[j]//d[j]
    if a is not None and a!=z:break
    a=z
  else:
   assert a is not None;occ.append({'copy_offset':a,'slot':i,'turn':c,'relative_time':a*len(tr)+i})
 return sorted(occ,key=lambda x:x['relative_time'])

def read_certificate(q,cut,tr,d,first_copy_only=False):
 occ=occurrences(q,tr,d)
 if first_copy_only:occ=[x for x in occ if x['copy_offset']>=0]
 assert occ
 prior=[x for x in occ if x['relative_time']<cut]
 if prior:
  w=prior[-1];assert w['turn']=='R',(q,cut,w)
  mode='last_prior_R'
 else:
  w=occ[0];assert w['turn']=='L',(q,cut,w)
  mode='first_future_L'
 return {'cell':q,'mode':mode,'witness':w,'complete_occurrences':occ}

def make_cycle(q,path,slot,kcopy,tr,d,first_only=False):
 # Normalize by actual period index so one template translates with d.
 cells=[q]+path;cs=[(x-kcopy*d[0],y-kcopy*d[1])for x,y in cells]
 target=occurrences(cs[0],tr,d)
 if first_only:target=[x for x in target if x['copy_offset']>=0]
 assert target and target[0]['relative_time']==slot and target[0]['turn']=='L'
 rr=[read_certificate(z,slot,tr,d,first_only)for z in cs]
 aa=[r['witness']['copy_offset']for r in rr]
 return {'slot':slot,'target_cell':cs[0],'cycle_cells':cs,'edge_count':len(cs),'first_copy_only':first_only,'left_fringe':0 if first_only else max(0,-min(aa)),'right_fringe':max(0,max(aa)),'black_edge_read_certificates':rr}

def build(which,N=5,mature=2):
 W,p,h,tr,d=word_data(which);B0,_,_,_=infer_input(W*N,p,h)
 B=set(B0);G=FullGraph(B,wwhich(p,h));birth={q:None for q in B};res={};r=0
 for t,c in enumerate(W*N):
  q=p;slot=t%len(W);kp=t//len(W)
  assert('L'if q in B else'R')==c
  if c=='R':r+=1;birth[q]=t;G.add(q)
  else:
   if kp in (0,mature)and birth[q]is None:
    path=graph_path(G,q)
    if path is not None:
     res[(kp,slot)]=make_cycle(q,path,slot,kp,tr,d,first_only=kp==0)
   G.delete(q);del birth[q];r=0
  p,h=step(B,p,h)
 core=[v for (kp,s),v in res.items()if kp==mature]
 # Re-create universal core certificates rather than first-copy truncated lists.
 core=[make_cycle(tuple(z['target_cell']),[tuple(q)for q in z['cycle_cells'][1:]],z['slot'],0,tr,d,False)for z in core]
 core_slots={z['slot']for z in core}
 startup=[v for(kp,s),v in res.items()if kp==0 and s not in core_slots]
 overrides=[res[(0,z['slot'])]for z in core if z['left_fringe']>0 and (0,z['slot'])in res]
 corehist=Counter((z['left_fringe'],z['right_fringe'])for z in core)
 startuphist=Counter(z['right_fringe']for z in startup)
 out={'word_length':len(W),'word_sha256':hashlib.sha256(W.encode()).hexdigest(),'start_pose':[word_data(which)[1],word_data(which)[2]],'drift':d,'w_lattice':wwhich(word_data(which)[1],word_data(which)[2]),'core_count':len(core),'core_fringe_hist':{str(k):v for k,v in sorted(corehist.items())},'startup_extra_count':len(startup),'startup_right_fringe_hist':dict(startuphist),'startup_override_count':len(overrides),'startup_override_right_fringe_hist':dict(Counter(z['right_fringe']for z in overrides)),'core':core,'startup_extra':startup,'startup_overrides':overrides}
 return out

if __name__=='__main__':
 out={str(which):build(which)for which in(1564,4352)}
 (OUT/'forced_input_cycle_templates.json').write_text(json.dumps(out,indent=2)+'\n')
 for w,d in out.items():print(w,{k:v for k,v in d.items()if k not in('core','startup_extra')},flush=True)

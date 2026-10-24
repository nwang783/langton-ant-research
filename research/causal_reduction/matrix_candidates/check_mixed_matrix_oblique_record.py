"""Frozen geometric/chronological certificate; no discovery-program imports."""
import itertools,json,pathlib,hashlib,collections
V=(1j,1,-1j,-1);targets=(2+5j,3+2j,-2-5j,-3-2j)
def ell(z):return int(-2*z.real+3*z.imag)
dom=[];extrema=[];prefixes=[]
for d,target in enumerate(targets):
 words=[];vals=[];details=[]
 for bits in itertools.product((0,1),repeat=9):
  w=tuple(((d%2 if j%2==0 else 1-d%2)+2*b) for j,b in enumerate(bits))
  if sum((V[z] for z in w),0j)!=target:continue
  q=0j;vv=[]
  for z in w:vv.append(ell(q));q+=V[z]
  words.append(w);vals.extend(vv);details.append(vv)
 dom.append(words);extrema.append([min(vals),max(vals)]);prefixes.append(details)
assert list(map(len,dom))==[4,20,4,20]
assert extrema==[[0,10],[-7,7],[-10,0],[-7,7]]
assert all(w[-1]==0 for w in dom[0])
records=[];hist=collections.Counter();survivors=[];east_survivors=[]
def check(w):
 q=0j;h=0;colors={};last={};turns=''
 for t,d in enumerate(w):
  delta=(d-h)%4;assert delta in(1,3)
  wanted=int(delta==3);present=colors.get(q,0 if ell(q)>=0 else None)
  if present is not None and present!=wanted:
   return dict(read=t,cell=[int(q.real),int(q.imag)],linear_height=ell(q),required='RL'[wanted],available='RL'[present],previous_local_read=last.get(q),turn_prefix=turns)
  colors[q]=1-wanted;last[q]=t;turns+='RL'[wanted];q+=V[d];h=d
 return None
for i,u in enumerate(dom[1]):
 if check(u) is None:east_survivors.append(i)
 for j,v in enumerate(dom[2]):
  conflict=check(u+v)
  if conflict is None:survivors.append([i,j])
  else:hist[conflict['read']]+=1;records.append(dict(east=i,south=j,**conflict))
assert len(records)+len(survivors)==80 and not survivors
p=pathlib.Path(__file__);raw=json.dumps(records,sort_keys=True,separators=(',',':')).encode()+b'\n';p.with_suffix('.records.json').write_bytes(raw)
out=dict(matrix=[[3,2],[2,5]],radix=9,covector=[-2,3],determinant=11,domain_counts=list(map(len,dom)),domains=dom,proper_prefix_extrema=extrema,proper_prefix_values=prefixes,east_survivors=east_survivors,pairs=80,conflicts=len(records),histogram=dict(hist),latest=max(hist),survivors=survivors,records_sha256=hashlib.sha256(raw).hexdigest())
p.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in('domains','proper_prefix_values')}))

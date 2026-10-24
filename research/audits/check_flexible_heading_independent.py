from pathlib import Path
S=Path(__file__).with_name('check_heading_defect_classification_independent.py');exec(compile(S.read_text().split('ctrl=json.loads')[0],str(S),'exec'))
coarse=trace(REV,h=3)[0];N=728
control=json.loads((U/'flexible_heading_backward/controls.json').read_text())
def pose(i):
 k,j=divmod(i,104);x,y,h,c=coarse[j];return(x-2*k,y-2*k),h,c
out=[]
for mode in ('heading','square'):
 names={};C=[];groups=defaultdict(lambda:defaultdict(list));gates=[];initial={};domains={};pairs={};pres={};monos={};bad=[]
 def var(s):
  if s not in names:names[s]=len(names)+1
  return names[s]
 if mode=='heading':
  heads={i:var(f'h{i}')for i in range(-1,N+2)}
  for i in range(-1,N):
   p,h,c=pose(i);pair=c+pose(i+1)[2];dom=[(eps,w)for eps in (0,1)for w in pal[pair][str(eps)]['flip']];domains[i]=dom
   xs=[var(f'x{i}_{k}')for k in range(6)];b=var(f'pair{i}');pairs[i]=xs;pres[i]=b
   C.extend([[-x,-y]for x,y in combinations(xs,2)]);C.extend([[-x,b]for x in xs]);C.append(xs+[-b])
   for k,(eps,w)in enumerate(dom):
    x=xs[k];C.extend([[-x,heads[i]if eps else-heads[i]],[-x,heads[i+2]]]);rr,e,eh=trace(w,p,(h+2*eps)%4);assert(e,eh)==(pose(i+2)[0],(pose(i+2)[1]+2)%4)
    backward=rr[1][:2]!=pose(i+1)[0]
    if 312<=i<416 and backward:bad.append(x)
    for j,(xx,yy,hh,t)in enumerate(rr):groups[xx,yy][i,j,t].append(x)
  for i in range(-1,N-1):C.append([-pres[i],-pres[i+1]])
  for i in range(N):
   m=var(f'mono{i}');xs=[var(f'z{i}_{eps}')for eps in(0,1)];monos[i]=(m,xs);C.extend([[-xs[0],-xs[1]],[-xs[0],m],[-xs[1],m],[xs[0],xs[1],-m],[-m,-pres[i-1]],[-m,-pres[i]],[m,pres[i-1],pres[i]]])
   p,h,c=pose(i)
   for eps,x in enumerate(xs):
    w=c if eps==0 else('L'if c=='R'else'R');rr,e,eh=trace(w,p,(h+2*eps)%4);assert(e,eh)==pose(i+1)[:2]
    C.extend([[-x,heads[i]if eps else-heads[i]],[-x,-heads[i+1]]])
    for j,(xx,yy,hh,t)in enumerate(rr):groups[xx,yy][i,j,t].append(x)
 else:
  for i in range(N):
   p,h,c=pose(i);dom=[c,c+('L'if c=='R'else'R')*4];domains[i]=dom;xs=[var(f'x{i}_{k}')for k in(0,1)];pairs[i]=xs;C.extend([xs,[-xs[0],-xs[1]]])
   if 312<=i<416 and i%104!=31:bad.append(xs[1])
   for k,w in enumerate(dom):
    rr,e,eh=trace(w,p,h);assert(e,eh)==pose(i+1)[:2]
    for j,(xx,yy,hh,t)in enumerate(rr):groups[xx,yy][i,j,t].append(xs[k])
 C.append(bad)
 for a,(q,events)in enumerate(sorted(groups.items())):
  prev=var(f'input{a}');initial[q]=prev
  for b,(ev,xs)in enumerate(sorted(events.items())):
   active=var(f'a{a}_{b}');nxt=var(f'b{a}_{b}');C.extend([[-x,active]for x in xs]);C.append(xs+[-active]);C.append([-active,prev if ev[-1]=='L'else-prev])
   for vp,va,vb in product((False,True),repeat=3):
    if vb!=(vp!=va):C.append([(-q if v else q)for q,v in zip((prev,active,nxt),(vp,va,vb))])
   gates.append((q,ev,xs,prev,active,nxt));prev=nxt
 folder,tag=('flexible_heading_backward','flexible_heading')if mode=='heading'else('unit_square_flexible_classification','square');O=U/folder
 A=json.loads((O/(tag+'.architecture.json')).read_text());res=json.loads((O/(tag+'.result.json')).read_text());nv,actual=cnfread(O/(tag+'.cnf'));assert nv==len(names)and canon(C)==canon(actual)
 assert A['coarse_word']==REV and len(groups)==len(A.get('cells',A.get('physical_cells')))
 if mode=='heading':assert A['palettes']==pal and A['backward_selectors']==bad
 proof=json.loads(subprocess.run([str(ROOT/'causal_reduction/morphic_candidates/check_drat'),str(O/(tag+'.cnf')),str(O/(tag+'.rup'))],capture_output=True,text=True,check=True).stdout);assert proof['valid']and proof['RAT']==proof['deletions']==0
 for key,ext in(('cnf_sha256','.cnf'),('rup_sha256','.rup')):assert hashlib.sha256((O/(tag+ext)).read_bytes()).hexdigest()==res[key]
 free=list((canon(C)-canon([bad])).elements());controls=control[mode+'_controls'];nc=0
 for row in controls:
  vals={v:False for v in names.values()};rr=[];word=''
  if mode=='heading':
   til=dict(row['tiling']);assert all(i+1 not in til for i in til);i=-1 if-1 in til else 0;start=i;p0,h0,_=pose(i);eps=row['initial_flip'];h0=(h0+2*eps)%4
   while i<N:
    vals[heads[i]]=bool(eps);p,h,c=pose(i)
    if i in til:
     k=3*eps+til[i];ee,w=domains[i][k];assert ee==eps;vals[pairs[i][k]]=True;vals[pres[i]]=True;endidx=i+2;endeps=1
    else:
     assert i>=0 and i-1 not in til;m,xs=monos[i];vals[m]=True;vals[xs[eps]]=True;w=c if eps==0 else('L'if c=='R'else'R');endidx=i+1;endeps=0
    reads,e,eh=trace(w,p,(h+2*eps)%4);assert(e,eh)==(pose(endidx)[0],(pose(endidx)[1]+2*endeps)%4);rr+=reads;word+=w;vals[heads[endidx]]=bool(endeps);i=endidx;eps=endeps
  else:
   chosen=set(row['square_indices']);p0,h0,_=pose(0)
   for i in range(N):
    k=int(i in chosen);vals[pairs[i][k]]=True;w=domains[i][k];rr+=trace(w,pose(i)[0],pose(i)[1])[0];word+=w
  assert trace(word,p0,h0)[0]==rr
  hist=defaultdict(list)
  for x,y,h,c in rr:hist[x,y].append(c)
  legal=all(all(a!=b for a,b in zip(v,v[1:]))for v in hist.values());inp={q for q,v in hist.items()if v[0]=='L'}
  vals.update({v:q in inp for q,v in initial.items()});got=defaultdict(list)
  for q,ev,xs,prev,ac,nxt in gates:
   vals[ac]=any(vals[x]for x in xs);vals[nxt]=vals[prev]!=vals[ac]
   if vals[ac]:got[q].append(ev[-1])
  assert dict(got)==dict(hist)
  sat=all(any(vals[abs(z)]==(z>0)for z in cl)for cl in free)
  assert sat==legal==row['literal_legal']and len(inp)==row['input_mass']and len(word)==row['length'];nc+=1
 out.append(dict(mode=mode,variables=nv,clauses=len(C),cells=len(groups),proof=proof,controls=nc))
# Exhaustive geometric recut: each nonbackward flip consists of the two coarse physical moves then a four-move square. A following coarse move and repeated source color force the unique five-read unit-pose image.
recuts=[]
for pair in pal:
 for eps in(0,1):
  coarsepair,ce,ch=trace(pair);first=coarsepair[1][:2]
  for w in pal[pair][str(eps)]['flip']:
   rr,e,eh=trace(w,h=2*eps)
   if rr[1][:2]!=first:continue
   assert rr[2][:2]==ce and all(rr[k][:2]!=ce for k in(3,4,5))
   for nxt in'RL':
    follow='L'if nxt=='R'else'R';five=w[2:]+follow
    if five[0]==five[4]:continue
    expected=nxt+('L'if nxt=='R'else'R')*4
    assert five==expected;assert trace(five,ce,ch)[1:]==trace(nxt,ce,ch)[1:];recuts.append((pair,eps,w,nxt,five))
assert len(recuts)==16
result=dict(status='PASS independent arbitrary-alignment heading tiling CNFs, RUPs, physical controls and exact recut',note_sha256=hashlib.sha256((U/'flexible_heading_defect_classification.md').read_bytes()).hexdigest(),circuits=out,recut_cases=len(recuts),scope='Six-read minimal heading-flip tiles and monomers, arbitrary nonoverlap alignment and input colors. Eventually only inverse104 or phase31 prepared108; finite support impossible by negative turn excess. Does not combine ten-read bypasses and does not assert forward reversal.')
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(result)

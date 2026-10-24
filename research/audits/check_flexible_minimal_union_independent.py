from pathlib import Path
S=Path(__file__).with_name('check_heading_defect_classification_independent.py');exec(compile(S.read_text().split('ctrl=json.loads')[0],str(S),'exec'))
coarse=trace(REV,h=3)[0];N=728
control={'heading_controls':json.loads((U/'flexible_minimal_union/controls.json').read_text())['controls']}
bypass={}
for pair in pal:
 coarsepair,e,h=trace(pair);mid=coarsepair[1][:3];words=[]
 for w in map(''.join,product('RL',repeat=10)):
  rr,ee,hh=trace(w)
  if(ee,hh)==(e,h)and all(r[:3]!=mid for r in rr):words.append(w)
 assert len(words)==2
 bypass[pair]=words
def pose(i):
 k,j=divmod(i,104);x,y,h,c=coarse[j];return(x-2*k,y-2*k),h,c
out=[]
for mode in ('heading',):
 names={};C=[];groups=defaultdict(lambda:defaultdict(list));gates=[];initial={};domains={};pairs={};pres={};monos={};bad=[]
 def var(s):
  if s not in names:names[s]=len(names)+1
  return names[s]
 if mode=='heading':
  heads={i:var(f'h{i}')for i in range(-1,N+2)}
  for i in range(-1,N):
   p,h,c=pose(i);pair=c+pose(i+1)[2];dom=[]
   for eps in (0,1):
    dom += [(eps,1,w)for w in pal[pair][str(eps)]['flip']]
    dom += [(eps,0,(('L'if w[0]=='R'else'R')+w[1:])if eps else w)for w in bypass[pair]];domains[i]=dom
   xs=[var(f'x{i}_{k}')for k in range(10)];b=var(f'pair{i}');pairs[i]=xs;pres[i]=b
   C.extend([[-x,-y]for x,y in combinations(xs,2)]);C.extend([[-x,b]for x in xs]);C.append(xs+[-b])
   for k,(eps,outsign,w)in enumerate(dom):
    x=xs[k];C.extend([[-x,heads[i]if eps else-heads[i]],[-x,heads[i+2]if outsign else-heads[i+2]]]);rr,e,eh=trace(w,p,(h+2*eps)%4);assert(e,eh)==(pose(i+2)[0],(pose(i+2)[1]+2*outsign)%4)
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
 folder,tag='flexible_minimal_union','minimal_union';O=U/folder
 A=json.loads((O/(tag+'.architecture.json')).read_text());res=json.loads((O/(tag+'.result.json')).read_text());nv,actual=cnfread(O/(tag+'.cnf'));assert nv==len(names)and canon(C)==canon(actual)
 assert A['coarse_word']==REV and len(groups)==len(A.get('cells',A.get('physical_cells')))
 if mode=='heading':assert A['palettes']==pal and A['backward_selectors']==bad
 proof=json.loads(subprocess.run([str(ROOT/'causal_reduction/morphic_candidates/check_drat'),str(O/(tag+'.cnf')),str(O/(tag+'.rup'))],capture_output=True,text=True,check=True).stdout);assert proof['valid']and proof['RAT']==proof['deletions']==0
 for key,ext in(('cnf_sha256','.cnf'),('rup_sha256','.rup')):assert hashlib.sha256((O/(tag+ext)).read_bytes()).hexdigest()==res[key]
 free=list((canon(C)-canon([bad])).elements());controls=control[mode+'_controls'];nc=0
 for row in controls:
  vals={v:False for v in names.values()};rr=[];word=''
  if mode=='heading':
   til=dict(row['tiles']);assert all(i+1 not in til for i in til);i=-1 if-1 in til else 0;start=i;p0,h0,_=pose(i);eps=row['initial_flip'];h0=(h0+2*eps)%4
   while i<N:
    vals[heads[i]]=bool(eps);p,h,c=pose(i)
    if i in til:
     k=5*eps+til[i];ee,outsign,w=domains[i][k];assert ee==eps;vals[pairs[i][k]]=True;vals[pres[i]]=True;endidx=i+2;endeps=outsign
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

DM=json.loads((U/'flexible_minimal_union/domain_manifest.json').read_text());levels=defaultdict(set)
for i in range(104):
 row=DM['phases'][i];assert row['phase']==i and row['pair']==pose(i)[2]+pose(i+1)[2]
 assert [(r['incoming_sign'],r['outgoing_sign'],r['word'])for r in row['domain']]==domains[i]
 for eps,delta,w in domains[i]:
  rr,e,eh=trace(w,pose(i)[0],(pose(i)[1]+2*eps)%4)
  assert (e,eh)==(pose(i+2)[0],(pose(i+2)[1]+2*delta)%4)
  if len(w)==10:assert rr[1][:2]!=pose(i+1)[0]
  for x,y,h,c in rr:levels[x-y,x%2].add(x//2)
assert max(max(v)-min(v)for v in levels.values())==4 and [cl for cl,v in levels.items()if max(v)-min(v)==4]==[(1,1)]
result=dict(status='PASS independent mixed minimal tiling CNF, physical chronology and monotone RUP',note_sha256=hashlib.sha256((U/'flexible_minimal_union_obstruction.md').read_bytes()).hexdigest(),circuits=out,union_span=4,span4_orbit=[1,1],scope='Arbitrary nonoverlapping mixed six-read heading flips and ten-read bypass resets, shared actual headings, arbitrary initial colors and complete crossing tiles. Finite-word UNSAT does not require full radius-four history. With separately signed recut/square theorem, every infinite schedule eventually V/P108, impossible from finite support. No forward reversal or broader palette/scaffold claim.')
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(result)

from pathlib import Path
S=Path(__file__).with_name('check_pair_bypass_local_independent.py');exec(compile(S.read_text().split('controls=json.loads')[0],str(S),'exec'))
O=U/'pair_bypass_flexible_tiling';A=json.loads((O/'flexible.architecture.json').read_text());res=json.loads((O/'flexible.result.json').read_text());coarse,_,_=walk(REV,(0,0),3);assert A['coarse_word']==REV and A['palettes']==pal
names={};C=[];groups=defaultdict(lambda:defaultdict(list));blocks={};N=728

def var(s):
 if s not in names:names[s]=len(names)+1
 return names[s]
def pose(i):
 k,j=divmod(i,104);x,y,h,c=coarse[j];return(x-2*k,y-2*k),h,c
sels={};prs={};monos={}
for i in range(-1,N):
 xs=[var(f'x{i}_{k}')for k in(0,1)];b=var(f'pair{i}');sels[i]=xs;prs[i]=b
 for x0,x1,bv in product((False,True),repeat=3):
  # At most one image; explicit OR relation uses the supplied four-clause normal form.
  pass
 C.extend([[-xs[0],-xs[1]],[-xs[0],b],[-xs[1],b],[xs[0],xs[1],-b]])
for i in range(-1,N-1):C.append([-prs[i],-prs[i+1]])
for i in range(N):
 m=var(f'mono{i}');monos[i]=m
 C.extend([[-m,-prs[i-1]],[-m,-prs[i]],[m,prs[i-1],prs[i]]])
 pos,h,c=pose(i);rr,_,_=walk(c,pos,h);blocks[i,-1]=rr
 for j,(x,y,hh,t)in enumerate(rr):groups[x,y][i,j,t].append(m)
for i,xs in sels.items():
 pos,h,c=pose(i);pair=c+pose(i+1)[2]
 for k,w in enumerate(pal[pair][1:]):
  rr,e,eh=walk(w,pos,h);assert(e,eh)==walk(pair,pos,h)[1:];blocks[i,k]=rr
  for j,(x,y,hh,t)in enumerate(rr):groups[x,y][i,j,t].append(xs[k])
central=[x for i in range(312,416)for x in sels[i]];C.append(central);initial={};gates=[]
for a,(cell,events)in enumerate(sorted(groups.items())):
 prev=var(f'input{a}');initial[cell]=prev
 for b,(ev,xs)in enumerate(sorted(events.items())):
  ac=var(f'a{a}_{b}');nxt=var(f'b{a}_{b}');C.extend([[-x,ac]for x in xs]);C.append(xs+[-ac]);C.append([-ac,prev if ev[-1]=='L'else-prev])
  for bp,ba,bn in product((False,True),repeat=3):
   if bn!=(bp!=ba):C.append([(-lit if bit else lit)for lit,bit in zip((prev,ac,nxt),(bp,ba,bn))])
  gates.append((cell,ev,xs,prev,ac,nxt));prev=nxt
n2,cc=readcnf(O/'flexible.cnf');assert len(names)==n2==30889 and len(C)==len(cc)==104237 and canon(C)==canon(cc)
assert list(map(list,sorted(groups)))==A['physical_cells']and len(groups)==274
levels=defaultdict(set)
for i in range(104):
 pos,h,c=pose(i)
 for w in[c]+pal[c+pose(i+1)[2]][1:]:
  for x,y,hh,t in walk(w,pos,h)[0]:levels[x-y,x%2].add(x//2)
assert max(max(v)-min(v)for v in levels.values())==3
assert {tuple(row['orbit']):(row['minimum'],row['maximum'])for row in A['horizon']}=={cl:(min(v),max(v))for cl,v in levels.items()}
for key,fn in [('cnf_sha256','flexible.cnf'),('rup_sha256','flexible.rup')]:assert hashlib.sha256((O/fn).read_bytes()).hexdigest()==res[key]
pr=subprocess.run([str(ROOT/'causal_reduction/morphic_candidates/check_drat'),str(O/'flexible.cnf'),str(O/'flexible.rup')],capture_output=True,text=True,check=True);proof=json.loads(pr.stdout);assert proof['valid']and proof['RUP']==764 and proof['RAT']==proof['deletions']==0
controls=json.loads((O/'controls.json').read_text())['controls'];outcontrols=[];free=canon(C)-canon([central])
for row in controls:
 chosen=dict(row['bypasses']);assert all(i+1 not in chosen for i in chosen)
 rr=[];fine='';start=-1 if -1 in chosen else 0;startpos,starth,_=pose(start)
 for i in range(-1,N):
  if i in chosen:pos,h,c=pose(i);w=pal[c+pose(i+1)[2]][chosen[i]+1]
  elif i>=0 and i-1 not in chosen:pos,h,c=pose(i);w=c
  else:continue
  rr+=walk(w,pos,h)[0];fine+=w
 assert walk(fine,startpos,starth)[0]==rr
 literal=defaultdict(list)
 for x,y,h,c in rr:literal[x,y].append(c)
 first={q for q,v in literal.items()if v[0]=='L'};legal=all(all(a!=b for a,b in zip(v,v[1:]))for v in literal.values())
 vals={}
 for i,xs in sels.items():
  for k,x in enumerate(xs):vals[x]=chosen.get(i)==k
  vals[prs[i]]=i in chosen
 for i,m in monos.items():vals[m]=i not in chosen and i-1 not in chosen
 vals.update({v:q in first for q,v in initial.items()});actual=defaultdict(list)
 for q,ev,xs,prev,ac,nxt in gates:
  vals[ac]=any(vals[x]for x in xs);vals[nxt]=vals[prev]!=vals[ac]
  if vals[ac]:actual[q].append(ev[-1])
 assert dict(actual)==dict(literal)
 sat=all(any(vals[abs(z)]==(z>0)for z in clause)for clause in free)
 assert sat==legal==row['literal_legal']and len(fine)==row['length']and len(first)==row['input_mass']
 outcontrols.append(dict(bypasses=len(chosen),length=len(fine),legal=legal,input_mass=len(first)))
out=dict(status='PASS independent flexible complete-boundary tiling, full physical CNF and RUP replay',note_sha256=hashlib.sha256((U/'flexible_pair_bypass_rigidity.md').read_bytes()).hexdigest(),variables=len(names),clauses=len(C),physical_cells=len(groups),proof=proof,controls=outcontrols,scope='Arbitrary nonoverlapping minimal ten-read pair bypasses at every inverse104 coarse index, no fixed pairing or periodicity, arbitrary entry colors. Optional complete boundary tiles -1/727 included and monomers exactly uncovered indices. Central bypass impossible, hence none starting>=312 in one-sided inverse schedule. Forward reversal gives eventual identity only. No larger/different palette, overlapping tiles or arbitrary trajectory exclusion.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k!='controls'})

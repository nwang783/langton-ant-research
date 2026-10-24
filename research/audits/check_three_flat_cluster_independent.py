from pathlib import Path
from collections import Counter,deque
from itertools import product
import hashlib,json,time
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'three_flat_cluster_between_high_ends_has_a_rank_collision.md';C=D/'check_three_flat_cluster_between_high_ends.json';J=json.loads(C.read_text());assert sha(P).startswith('b71c5709')and sha(C).startswith('53f57fbf')
ns={'__file__':str(S.with_name('check_two_flat_pair_gate_independent.py'))};exec(S.with_name('check_two_flat_pair_gate_independent.py').read_text().split('summary=Counter();row_results=')[0],ns);words,ports,audit,rotate,dv,xy=[ns[k]for k in('words','ports','audit','rotate','dv','xy')]
FW={'X':'NNSS','Y':'NSSN'};LW={'O':'WEE','U':'WEEW','V':'WWEE'}
def admissible(gs,fs,ls):
 if gs==(0,0):return False
 for i in range(2):
  if gs[i]==2 and(fs[i],*ls[i],fs[i+1])not in[('Y','O','V','X'),('Y','U','V','X'),('Y','V','V','Y')]:return False
  if gs[i]==0:
   if i and ls[i-1][-1]!='V':return False
   if i==0 and ls[1][0]!='V':return False
  if gs[i]==1:
   other=1-i
   if gs[other]==0:
    if ls[i]!=('V',):return False
   else:
    # e597's complete five-corner window first excludes passive current V;
    # c957 then excludes singleton U and gives the exact O island.
    if ls[i]!=('O',)or fs[i]!='Y':return False
    if i and ls[i-1][-1]!='V':return False
    if i==0 and ls[1][0]!='V':return False
 return True
refs={(tuple(r['gaps']),tuple(r['flat_words']),tuple(tuple(x)for x in r['left_words']),r['sink'],r['source']):r for r in J['rows']};used=set();summary=Counter();gapstats={};start=time.time();rows=[]
for gs in product(range(3),repeat=2):
 gc=Counter()
 for fs in product('XY',repeat=3):
  for letters in product('OUV',repeat=sum(gs)):
   ls=(tuple(letters[:gs[0]]),tuple(letters[gs[0]:]))
   if not admissible(gs,fs,ls):continue
   for nb,nsrc in product((3,4),repeat=2):
    key=(gs,fs,ls,nb,nsrc);assert key in refs and key not in used;used.add(key);ref=refs[key];spec=[('R','N'*nb,'sink'),('L','WWEE','Vcap')]
    for i,f in enumerate(fs):
     spec.append(('R',FW[f],'flat'))
     if i<2:spec.extend(('L',LW[a],'middle')for a in ls[i])
    spec.extend([('L','WWEE','Vcap'),('R','EWE'if nsrc==3 else'EWEW','source')]);p=-1-1j;ci=0;nodes=[]
    for j,(turn,w,role)in enumerate(spec):
     w=w if j==0 else rotate(w,ci-(0 if role=='flat'else 1));co=(ci+(1 if turn=='R'else-1))%4;nodes.append(dict(cell=xy(p),turn=turn,history=w,role=role,ci='NESW'[ci],co='NESW'[co]));p+=dv[co];ci=co
    assert nodes==ref['nodes'];fixed={complex(*z['cell']):z['history']for z in nodes};assert len(fixed)==len(nodes);pts=set(fixed)
    while True:
     cand={q+v for q in pts for v in dv}-pts;add={q for q in cand if sum(q+v in pts for v in dv)>=2}
     if not add:break
     pts|=add
    pts=sorted(pts,key=lambda z:(z.real,z.imag));assert list(map(xy,pts))==ref['closure_cells'];adj={p:[(p+v,k)for k,v in enumerate(dv)if p+v in pts]for p in pts};ds={p:[fixed[p]]if p in fixed else words[int(p.real+p.imag)%2][:]for p in pts}
    def reduce(ds):
     queue=deque(ds)
     while queue:
      p=queue.popleft()
      for q,k in adj[p]:
       vals={ports(w,p,k)for w in ds[p]};keep=[w for w in ds[q]if ports(w,q,(k+2)%4)in vals]
       if not keep:return None
       if len(keep)<len(ds[q]):ds[q]=keep;queue.append(q)
     return ds
    ct=Counter()
    def search(ds):
     ds=reduce(ds)
     if ds is None:return
     undec=[p for p in pts if len(ds[p])>1]
     if undec:
      p=min(undec,key=lambda p:len(ds[p]))
      for w in ds[p]:search(ds|{p:[w]})
      return
     hs={p:w[0]for p,w in ds.items()};kind=audit(hs);assert kind=='skipped_rank';ct[kind]+=1
    dd=reduce(ds)
    if dd is None:ct['PRIMARY_PORT']=1
    else:search(dd)
    assert dict(ct)==ref['counts'];assert not ref['open_sample'];summary.update(ct);gc.update(ct);gc['primaries']+=1;rows.append(dict(key=[gs,fs,ls,nb,nsrc],counts=dict(ct)))
 gapstats[str(gs)]=dict(gc)
assert len(used)==len(refs)==120 and summary==J['summary']and summary=={'PRIMARY_PORT':24,'skipped_rank':37344}
qual=D/'flat_cluster_passive_V_primary_coverage_clarification.md';assert sha(qual).startswith('8b2be096')
out=dict(status='PASS exact three-flat cluster with high endpoints, with mandatory explicit five-corner dependency',mandatory_primary_coverage_qualifier=sha(qual),proof=sha(P),certificate=sha(C),script=sha(S),primary_count=120,counts=dict(summary),gaps=gapstats,independently_rebuilt_rows=rows,analytic_review=['Scope complete WHITE cap4 critical GLOBAL-M b-circle, no one-use edges, EXACT three consecutive flat RIGHTs with nearest outside RIGHTs high sink/source. Signed RR/root-island/mixed-LL rules force one outside passiveV at each end; no high-to-flat RR or mixed high/flat LL cap is silently allowed.','Each internal LEFT run has length0..2 by essential simplicity;00 gives three RIGHT turns and a unit square. LL rows are exactly Y,O/U,V,X or Y,V,V,Y; adjacentRR requires both neighboring LEFTs V.','Important explicit dependency: a singleton gap not touchingRR has both outer LEFT neighbors and flat RIGHT endpoints, so signed e597889e five-corner constant-two cover applies. Its surviving rows have current LEFT only O/U, excluding passiveV. Then c957 excludes singletonU and gives V,Y,O,X-or-Y,V. c957 alone would not exclude a passive singletonV. This closes the apparent omitted(1,1)V,V case without an invented root premise.','Independent regeneration gives exactly120 primary physical stencils. Closure adds every two-neighbor corner; all empty and1..4 WHITE histories on its actual axis are retained. Exact port arc consistency and recursive assignment exhaust all completions, including zero-port constraints.24 primaries are count-empty; every37344 completion has a physical next-rank collision. No stream height, positive clock or critical-side filter is used after the stated primary implications.','This is not a three-flat sliding-window exclusion when outside RIGHTs are other flats. It does not contradict the all-k open RRLL strip and does not by itself bound larger flat clusters, require four total flats, or prove one-use/front/global attraction.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')));print(time.time()-start)

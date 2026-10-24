from pathlib import Path
import hashlib,json
S=Path(__file__).resolve();R=S.parents[1];D=R/'two_track_UCC_F_return_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();man=D/'manifest.json';assert sha(man)=='bcd968da47b1434133ad7d121b53b7e20e0820bc5cb00d9d7535c5577675b2a4'
for p,h in json.loads(man.read_text())['files'].items():assert sha(D/p)==h
ref=json.loads((D/'DV_rail_core_guard.json').read_text())
for p,h in ref['dependencies'].items():assert sha(R/p)==h
ns={'__file__':str(S.with_name('check_U_second_creator_bud_guards_independent.py'))};exec(Path(ns['__file__']).read_text().split('\nsource=[]')[0],ns);W,M,K,walk,xy=[ns[k]for k in('W','M','K','walk','xy')]
g=-1+0j

def trace(w,p=0j,h=0):
 rr=[];last={};req={};conflict=None
 for i,c in enumerate(w):
  rr.append((p,h,c))
  if p not in last:req[p]=c=='L'
  elif last[p][0]==c and conflict is None:conflict=(i,last[p][1],p,c)
  last[p]=(c,i);h=(h+(1 if c=='R'else -1))%4;p+=1j*(-1j)**h
 return dict(p=p,h=h,reads=rr,last=last,req=req,conflict=conflict)

def field_geom(w):
 t=trace(w);endK={t['p']+k*(-1j)**t['h']for k in K};out={p for p,(c,i)in t['last'].items()if c=='R'and p not in endK};return t,endK,out
src,sk,so=field_geom(W['U']+2*W['C']);assert(src['p'],src['h'])==(-1+5j,2)and src['last'][g]==('L',1)and g not in sk|so
geom={}
for a in'DVF':
 t,ek,oo=field_geom(W[a]);ctx=trace(W[a]+M);assert ctx['conflict']is None;assert all(ctx['req'].get(k)is True for k in K)
 # Every old core identity is read and deleted at the beginning of each actual full word.
 assert {p for p,h,c in t['reads'][:6]}==K
 assert all(next(c for p,h,c in t['reads']if p==k)=='L'for k in K)
 geom[a]=(t,ek,oo)
 assert sorted(list(xy(q)) for q in oo)==sorted(ref['exact_plain_full_geometries'][a]['outputs'])
assert geom['D'][2]=={2+0j}and geom['V'][2]=={0j,1j,1+0j,2+0j,2+1j,2+2j}
south=[];north=[]
for a in'DV':
 t,ek,oo=geom[a]
 for o in sorted(oo,key=lambda z:(z.real,z.imag)):
  ps=g+o;pn=g-o;en=pn+t['p'];assert ps.real>-1 or(ps.real==-1 and ps.imag in(0,1));assert en.imag>=1
  south.append([a,xy(o),xy(ps)]);north.append([a,xy(o),xy(pn),xy(en)])
assert len(south)==len(north)==7
# Exact integer elimination: x equation dY+vY=dX+vX-3; y equation dY+3vY=dX+3vX-9.
# Subtraction gives vY=vX-3 and then dY=dX, hence vX>=3.
ft=geom['F'][0];assert(ft['p'],ft['h'])==(-4-2j,2);assert min(p.imag for p,h,c in ft['reads'])==-2
# Symbolic affine formulas checked coefficientwise at basis, inequalities follow dX>=0,vX>=3.
for d,v in((0,3),(1,3),(0,4)):
 fp=complex(-1-d-v,5-d-3*v);fe=fp-ft['p'];loc=-(g-fp);eloc=g-fe
 assert loc==complex(-d-v,5-d-3*v)and loc.imag<=-4 and loc not in K
 assert eloc==complex(d+v-4,d+3*v-7)and eloc.imag>=2 and eloc not in K
 assert fe+complex(d+v-3,d+3*(v-3))==-2j
ut=trace(W['U']);assert next((i,c)for i,(p,h,c)in enumerate(ut['reads'])if p==-1+2j)==(13,'L')and -1+2j not in K
controls=[]
for row in ref['genuine_complete_finite_prefix_controls']:
 X,Y=row['X'],row['Y'];dx,vx=X.count('D'),X.count('V');assert Y.count('D')==dx and Y.count('V')==vx-3
 word=W['U']+2*W['C']+''.join(W[a]for a in X)+W['F']+''.join(W[a]for a in Y)
 t=trace(word);assert t['conflict']is None and(t['p'],t['h'])==(-2j,0)
 part=word+W['U'][:13];q=trace(part);assert q['conflict']is None;B={complex(*z)for z in row['complete_initial_black']};assert B=={p for p,b in q['req'].items()if b};initial=set(B);deletion=[]
 for i,(p,h,c)in enumerate(q['reads']):
  assert (p in B)==(c=='L')
  if p in B:B.remove(p)
  else:B.add(p)
  if p==g:deletion.append((i,c))
 assert(q['p'],q['h'])==(g,3)and g not in B and deletion==[(1,'L')]
 full=trace(word+W['U']+M);assert full['conflict']==(len(word)+13,1,g,'L')
 rejs={}
 for a in'DCVUFQB':
  candidate=W[a]+M;actual=W['U'][:13]+'R';k=next(i for i,c in enumerate(actual)if candidate[i]!=c);rejs[a]=k
 assert rejs==row['all7_impossible_at_current_marker_by_actual_prefix']
 if not dx:assert len(word)+13==36*vx+73
 controls.append(dict(X=X,Y=Y,seed_mass=len(initial),successful_reads=len(part),conflict_tick=len(word)+13,final_mass=len(B),rejections=rejs))
out=dict(status='PASS exact all-length all-order UCC D/V-S F D/V-N attempted-U core-hole exclusion',manifest=sha(man),south7=south,north7=north,actual_prefix_controls=controls,analytic_review=[
'Endpoint elimination is exact for arbitrary finite order: dY=dX, vY=vX-3, vX>=3. No run cap or candidate search is used in the proof.',
'The genuine U entry core includes g=(-1,0); actual L1 deletes it, both source C tails miss it and it is outside full UCC exitK/O. At a full cut, a black cell outside currentK whose original identity was deleted must have a last-R export in some intervening true full O. Independently recomputed O is every actual last-R cell outside exitK. Each complete packet reads/deletes all entryK within its first six reads, so a core-carried identity cannot silently become external without a tested last-R export. This is not intermediate physical-WHITE permanence.',
'All seven S full-output alignments are excluded by x<=-1 and the first-entry y5 lock. The foreign entry local g has y<=-4, below every RAW read and outside entryK; foreign exit relative y>=2 is outsideK. Thus F cannot write g or preserve an untested core identity.',
'All seven N full-output origins complete with y>=1, while remaining N D/V steps increase y and target enters y=-2. Consequently g is white outside targetK and contradicts its genuine RAW L13/read14 external input. No postforeign age theorem is invoked.',
'Five complete finite boards independently replay all full prefixes and attempted U ticks0..12; g has exactly the source L1 read and remains WHITE at attempted U13. Actual nextR excludes all seven RAW+actualM continuations at that marker. No completed U chord, actual contact or infinite continuation is claimed.',
'Scope only the named UCC,X_S,F,Y_N,U(0,-2,N) family with plain D/V rails. Other connectors, U rails, C additions, other target poses and attraction remain open.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(controls)

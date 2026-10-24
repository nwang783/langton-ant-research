"""Colored global-record model with exact low returns, transverse-mod4 and Q.

CLI FAR_HEIGHT_DFA.json RESIDUE_PORTS PORT_SCC.json PREFIX.
The base far model must use the same low cutoff and DFA as the port compiler.
Low SCC quotient is exact here because every low step preserves colors and Q;
no age bits are included in this pilot. Discovery-only until audited.
"""
from pathlib import Path
import sys,json,hashlib,math
src,portfile,sccfile,out=map(Path,sys.argv[1:5]);B=json.loads(src.read_text());S=json.loads(Path(B['base_model_file']).read_text());D=json.loads(Path(B['literal_dfa_file']).read_text());G=json.loads(Path(D['geometry_file']).read_text())['geometry'];C=json.loads(sccfile.read_text());assert B['lower_cutoff']==-18 and len(C['class_map'])>0
L=B['lower_cutoff'];phase=S['target_global_phase'];Sval=S['record_threshold'];F=(Sval-S['initial_token_weight']-1)//2;nb=S['n'];nq=max(1,(max(B['height_upper_bounds'])+8-F).bit_length());near=list(map(tuple,S['poses']));nnear=len(near);fc=B['far_controls'];nd=len(D['transitions'])
def rot(p,h):x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def coord(p):x,y=rot(p,phase);return x+y,x-y
offsets={}
for h in range(4):
 for a in B['keep']:
  dq,dt=coord(rot(G[a]['endpoint'][:2],h));mi=max(coord(rot(p,h))[0]for p in G[a]['inputs']);mo=max(coord(rot(p,h))[0]for p in G[a]['outputs']);mc=max(coord(rot(p[:2],h))[0]for p in G[a]['requirements']);offsets[h,a]=(dq,dt,mi,mo,mc)
assert L+max(v[4]for v in offsets.values())<min(coord(p)[0]for p in S['points'])
assert L+max(v[2]for v in offsets.values())<=F and L+max(v[3]for v in offsets.values())<=F
with portfile.open()as f:
 name,np_,ne,ni,mod=f.readline().split();np_,ne,ni=map(int,[np_,ne,ni]);assert name=='RESIDUE_PORTS'and int(mod)==4
 initial_ports=list(map(int,f.readline().split()));ports=[tuple(map(int,f.readline().split()))for _ in range(np_)]
assert len(C['class_map'])==2*np_ and C['ports_file']==str(portfile.resolve())
pidx={p:i for i,p in enumerate(ports)};cl=C['class_map'];nc=C['components']
desc=[]
for geo,d in B['position_map']:
 if geo==B['geometric_initial_control']:desc.append(('init',))
 elif geo==B['geometric_dummy_goal']:desc.append(('goal',))
 elif geo<nnear:
  x,y,h=near[geo];q,t=coord((x,y));desc.append(('near',h,q,d,t%4,x,y))
 else:
  h,q=fc[geo-nnear];desc.append(('low'if q is None else'far',h,q,d))
positions=[('init',),('goal',)];ids={}
for p,z in enumerate(desc):
 if z[0]not in['near','far']:continue
 ts=[z[4]]if z[0]=='near'else list(range(z[2]%2,4,2))
 for tr in ts:ids[p,tr]=len(positions);positions.append((z[0],p,tr))
lowoff=len(positions)
for c in range(nc):positions.append(('low_scc',c))
# Guarded-reset engines reserve their final control for the legacy OUT/reentry
# convention. Keep an explicit UNUSED sentinel, never a real low component.
positions.append(('unused_out',))
def lowid(h,d,depth,tr):
 assert 0<=depth<8 and tr%2==(L-depth)%2
 p=pidx[h,d,depth];r=(tr-((L-depth)%2))//2;return lowoff+cl[2*p+r]
logical=[];init_dest=set()
for p,z in enumerate(desc):
 if z[0]in['near','far']:
  ts=[z[4]]if z[0]=='near'else list(range(z[2]%2,4,2))
  # The normalized initial prefix starts far, never at a near packet.
  if z[0]=='far'and z[3]==D['initial_class']:
   for tr in ts:init_dest.add(ids[p,tr])
for p in initial_ports:
 h,d,depth=ports[p]
 for tr in range((L-depth)%2,4,2):init_dest.add(lowid(h,d,depth,tr))
for dst in sorted(init_dest):logical.append((0,dst,0,0,0,0,0,0,99,None))
for a,b,c in C['condensation_edges']:
 if a!=b:logical.append((lowoff+a,lowoff+b,0,0,0,0,0,0,99,None))
for ei,e in enumerate(B['transitions']):
 a=e[8]
 if a==99:continue
 zs,zt=desc[e[0]],desc[e[1]];assert zs[0]in['near','far','low']
 if zs[0]=='low'and zt[0]=='low':continue
 h=zs[1];dq,dt,mi,mo,mc=offsets[h,a]
 if zs[0]=='low':
  assert zt[0]in['near','far']and not e[7];q=zt[2]-dq;depth=L-q;assert 0<=depth<8
  assert e[2:7]==[0,0,0,0,0]
  ts=range(q%2,4,2)
 else:q=zs[2];ts=[zs[4]]if zs[0]=='near'else range(q%2,4,2)
 for tr in ts:
  fr=lowid(h,zs[3],L-q,tr)if zs[0]=='low'else ids[e[0],tr]
  if e[7]:to=1
  elif zt[0]=='low':
   hh=(h+G[a]['endpoint'][2])%4;q2=q+dq;assert q2<=L
   to=lowid(hh,zt[3],L-q2,(tr+dt)%4)
  else:
   to=ids.get((e[1],(tr+dt)%4))
   if to is None:continue
  logical.append((fr,to,*e[2:9],(q+mi,q+mo)))
# Every strict produced output lies below a finite historical-height cap.
cap=max([F]+[data[1]for *_,goal,a,data in logical if data is not None and not goal]);qrange=cap-F+1;nq=max(1,(qrange-1).bit_length());qmask=((1<<nq)-1)<<nb;allq=(1<<nq)-1
def intervals(lo,hi):
 while lo<=hi:
  size=lo&-lo if lo else 1<<((hi-lo+1).bit_length()-1)
  while size>hi-lo+1:size//=2
  mask=allq^(size-1);yield mask,lo&mask;lo+=size
E=[]
for fr,to,k,v,flip,clear,reset,goal,a,data in logical:
 if data is None:E.append([fr,to,k,v,flip,clear,reset,goal,a]);continue
 ih,oh=data;imin=max(0,ih-F)
 if imin>=qrange:continue
 if goal:
  for km,kv in intervals(imin,qrange-1):E.append([fr,to,k|(km<<nb),v|(kv<<nb),flip,clear,reset,goal,a])
  continue
 o=max(0,oh-F);assert o<qrange
 for km,kv in intervals(max(imin,o),qrange-1):E.append([fr,to,k|(km<<nb),v|(kv<<nb),flip,clear,reset,0,a])
 for km,kv in intervals(imin,min(o-1,qrange-1)):E.append([fr,to,k|(km<<nb),v|(kv<<nb),flip,clear|qmask,reset|(o<<nb),0,a])
n=nb+nq
N=dict(format='guarded_reset_exact_low_color_Q_v1',n=n,out=len(positions)-1,positions=positions,start=[0,(1<<n)-1,0],transitions=E,reentry=[],keep=B['keep'],base_model_file=str(src.resolve()),base_model_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),ports_file=str(portfile.resolve()),ports_sha256=hashlib.sha256(portfile.read_bytes()).hexdigest(),low_scc_file=str(sccfile.resolve()),low_scc_sha256=hashlib.sha256(sccfile.read_bytes()).hexdigest(),points=S['points'],color_bits=nb,Q_bits=nq,Q_initial=F,Q_cap=cap,Q_shift=nb,low_cutoff=L,scope='Discovery model retaining literal residual colors, exact high head height, heading, packet DFA, head transverse residue modulo4 and exact historical residual Q. All low packet contexts miss the patch and have no high residual effects; exact residue-aware port summaries are collapsed only along color/Q identity strong components. Initial high residual Q isF. No minimum-age bits, current high-token counts, unretained low colors or record exclusion are claimed.')
out.with_suffix('.json').write_text(json.dumps(N,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f'{n} {len(positions)} {len(E)} 0\n');f.write(' '.join(map(str,N['start']))+'\n')
 for e in E:f.write(' '.join(map(str,e))+'\n')
 f.write('\n')
print(dict(bits=n,color_bits=nb,Q_bits=nq,Q_range=[F,cap],positions=len(positions),edges=len(E),low_components=nc,logical_edges=len(logical)))

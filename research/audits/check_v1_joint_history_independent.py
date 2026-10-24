"""Independent literal masks, signed age-two queries, affine conflict and controls."""
from pathlib import Path
import json,hashlib
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
B=ROOT/'core_periodicity_new/v1_joint_history_frozen_20261023_1112';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f.get('frozen',f.get('file'))).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_v1_dc_age3_joint_history.json').read_text());ids=(0,1,4,5,6,7,8,9);mp={a:i for i,a in enumerate(ids)};cc=dict(zip(ids,(0,1,0,1,2,0,1,2)))
core={z for z,c in walk(mark)[2].items()if c};G={}
for a in ids:
 end,h,_,flip=walk(raws[a]);req=walk(raws[a]+mark)[2];black={z for z,c in req.items()if c}
 G[a]=(sorted(black-core,key=xy),sorted((black^flip)-{end+rotation(z,h)for z in core},key=xy),end,h,req)
height=lambda z:int(z.real+z.imag)
assert [height(o)-1 for o in G[1][1]]==J['source_output_heights_minus_H']
masks=[]
for a,offset,ages in ((4,-2,(2,3)),(7,-4,(3,3,5,5,5))):
 rows=[]
 for p,age in zip(G[a][0],ages):
  lev=offset+height(rotation(p,1));f28=28+2*lev>=26;f30=30+2*lev>=26
  rows.append(dict(slot=list(xy(p)),height_minus_H=lev,minimum_produced_age=age,entry_forbidden_I28=f28,entry_forbidden_I30=f30,pre_DC_I28=f28 and age>=3,pre_DC_I30=f30 and age>=3))
 masks.append(dict(helper=a,inputs=rows))
assert masks==J['helper_input_masks']
F={tuple(map(int,l.split()[:8]))for l in (B/'04_01_closure.tsv').read_text().splitlines()};queries=[];keep=[]
for a in ids:
 for i,o in enumerate(G[a][1]):
  rhs=1+int(o.real-o.imag)
  if rhs<0 or rhs%2:continue
  query=(mp[a],mp[4],int(o.real),int(o.imag)+3,2,*xy(o),2)
  row=dict(source=a,output_index=i,output=list(xy(o)),cone_rhs=rhs,count5_query=list(query),count5_excluded=query in F)
  queries.append(row)
  if query not in F:keep.append(row)
assert queries==J['young_critical_origin_queries'] and keep==J['young_critical_survivors']
assert [(r['source'],r['output'],r['cone_rhs'])for r in keep]==[(4,[0,1],0),(6,[0,1],0)]
def reads(word,p=0j,h=0):
 out=[]
 for t,ch in enumerate(word):
  out.append((t,p,ch));h=(h+(1 if ch=='R'else-1))%4;p+=(1j,1,-1j,-1)[h]
 return out,p,h
# VCC's start is 25+10g. The first following D exists precisely for g>=1.
assert all(w[:2]==mark[:2]for w in raws)
fixed=raws[6]+raws[4]+raws[0]+mark[:2]
r,_,_=reads(fixed);hits=[(t,c)for t,p,c in r if p==-1]
assert hits==[(1,'L'),(77,'L')]
assert [list(z)for z in hits]==J['all_g_conflict']['fixed_block_hits']
# Show the whole geometric family closes at the same goal with exactly3 Cs,
# but do not use bounded samples as the proof of the affine contradiction.
for g in (0,1,2,7,41):
 word=raws[1]+raws[0]*g+raws[6]+raws[4]+raws[0]*g
 _,p,h=reads(word);assert(p,h)==(1j,1)
 if g:
  rr,_,_=reads(word+mark[:2]);q=complex(1-g,1+g);hit=[(t,c)for t,z,c in rr if z==q]
  assert (26+10*g,'L')in hit and(102+10*g,'L')in hit
  assert not any(26+10*g<t<102+10*g for t,c in hit)
controls=[]
for case in J['literal_controls']:
 seq=case['word'];word=''.join(raws[a]for a in seq)+mark
 _,_,req,_=walk(word);seed={z for z,c in req.items()if c};assert core<=seed
 assert sorted(map(xy,seed))==list(map(tuple,case['seed']))and len(seed)==case['mass']
 board=set(seed);res={z:(None,None)for z in seed-core};p=0j;h=0;clock=0;t=0
 for j,a in enumerate(seq):
  I,O,end,dh,need=G[a]
  assert board==set(res)|{p+rotation(z,h)for z in core}
  assert not(set(res)&{p+rotation(z,h)for z in core})
  assert all((p+rotation(z,h)in board)==c for z,c in need.items())
  ins=[p+rotation(z,h)for z in I];birth=[res[z][0]for z in ins];age=[None if res[z][1]is None else clock-res[z][1]for z in ins]
  rec=case['records'][j]
  assert [*xy(p),h]==rec['pose']and clock==rec['C']and list(map(xy,ins))==list(map(tuple,rec['input_cells']))
  assert [i if i is not None else 'entry'for i in birth]==rec['input_birth_packets'] and age==rec['input_ages']
  for z in ins:del res[z]
  for z in O:
   target=p+rotation(z,h);assert target not in res;res[target]=(j,clock)
  for ch in raws[a]:
   assert ch==('L'if p in board else'R');board.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;p+=(1j,1,-1j,-1)[h];t+=1
  clock+=cc[a]
 for ch in mark:
  assert ch==('L'if p in board else'R');board.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;p+=(1j,1,-1j,-1)[h];t+=1
 assert t==case['reads_including_marker'];controls.append(dict(packets=seq,seed_mass=len(seed),literal_steps=t))
out=dict(status='PASS independent literal sources, signed clauses, affine repeated-read obstruction and full ordered-identity controls',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),age_two_queries=len(queries),surviving_young_sources=keep,all_g_at_least_one_conflict=hits,literal_controls=controls,scope='Conditional DC-to-V exact-age3 branch; older support and I30 seven-live requirement are analytic. V source remains possible; no V1/global closure.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

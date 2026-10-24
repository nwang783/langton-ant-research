"""Exact cone count enumeration and literal forced-prefix reconstruction."""
import itertools,json,hashlib
from pathlib import Path
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
B=ROOT/'core_periodicity_new/young_U_vcc_prefix_frozen_20261023_1026';j=json.loads((B/'young_U_vcc_forced_prefix.json').read_text());m=json.loads((B/'manifest.json').read_text())
for f in m['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
K={q for q,b in walk(mark)[2].items()if b};center=-.5-.5j
ends={a:walk(raws[a])[:2]for a in(0,1,4,5,6,7,8,9)}
# Reconstruct heading-center additivity for each base plus one C.
for base,combined in((0,1),(4,5),(7,8)):
 e,h=ends[combined];v=e+rotation(center,h)-center-ends[base][0];assert v==1+1j and h==3
source_head=-1+0j;source_h=3;end,h=ends[6];post=source_head+rotation(end,source_h);posth=(source_h+h)%4;assert(post,posth)==(-5+0j,1)
remaining=center-(post+rotation(center,posth));assert remaining==5-1j
zero=remaining-rotation(1+1j,posth);assert zero==4
solutions=[]
# The nonnegative identity d+2e+2f+b+2c=2 bounds b..f<=2 and a<=4.
for ns in itertools.product(range(5),repeat=6):
 a,b,c,d,e,f=ns
 pre=a*ends[0][0]+b*ends[4][0]+c*ends[7][0];after=d*ends[0][0]+e*ends[4][0]+f*ends[7][0]
 if rotation(pre,1)+after!=zero:continue
 assert d+2*e+2*f+b+2*c==2 and max(b,c,d,e,f)<=2
 run=[0]*a+[4]*b+[7]*c;tail=[0]*d+[4]*e+[7]*f
 assert run and len(set(run))==1 and len(set(tail))<=1
 word=run[:-1]+[{0:1,4:5,7:8}[run[-1]]]+tail;solutions.append((ns,word))
assert len(solutions)==5
assert {tuple(w)for ns,w in solutions}=={tuple(r['strict_word'])for r in j['all_five_nonnegative_solutions']}
records=[]
def literal(seq):
 q=0j;h=0;seen={};seed=set();times=[];poses=[];t=0;board=None
 for i,a in enumerate(seq):
  poses.append([*xy(q),h]);word=raws[a]+(mark if i==len(seq)-1 else'')
  for turn in word:
   if q in seen and seen[q][1]==turn:return False,{'time':t,'cell':xy(q),'turn':turn,'previous':seen[q]},seed,poses
   if q not in seen and turn=='L':seed.add(q)
   seen[q]=(t,turn);h=(h+(1 if turn=='R'else-1))%4;q+=(1j,1,-1j,-1)[h];t+=1
 return True,None,seed,poses
for ns,w in solutions:
 ok,bad,seed,poses=literal([6]+w+[7]);author=next(r for r in j['all_five_literal_records']if r['strict_word']==w);assert ok==author['feasible']
 if bad:
  a=author['conflict'];assert(bad['time'],bad['cell'],bad['turn'],bad['previous'])==(a['time'],tuple(a['cell']),a['turn'],tuple(a['previous']))
 records.append({'strict':w,'feasible':ok,'conflict':bad})
assert [r['strict']for r in records if r['feasible']]==[[5,0]]
expected=K|{3j,1+2j,-1+2j,4,2-1j,3-1j};assert len(expected)==11
for consumer in(7,8,9):
 ok,bad,seed,poses=literal([6,5,0,consumer]);assert ok and seed==expected and poses==[[0,0,0],[0,4,2],[-1,0,1],[0,-1,1]]
# Derive exact residual masks and source postfield; no helper may be invented.
def geom(a):
 end,h,_,flip=walk(raws[a]);req=walk(raws[a]+mark)[2];black={z for z,b in req.items()if b};O=(black^flip)-{end+rotation(z,h)for z in K};return black-K,O,req
I,O,req=geom(6);helper=-1+2j;assert helper not in O and helper not in req
Ivc,Ovc,reqvc=geom(5);physical={4j+rotation(z,2)for z in Ivc};assert physical=={1j,helper}
B0=set(expected);p=0j;h=0
for t,ch in enumerate(raws[6]+raws[5]+raws[0]+raws[7]+mark):
 assert(ch=='L')==(p in B0);B0.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;p+=(1j,1,-1j,-1)[h]
 if t+1==66:
  core={p+rotation(z,h)for z in K};assert(p,h)==(-1+1j,2)and core<=B0 and physical<=core
out={'status':'PASS independent exact one-C cone classification and literal older-helper contact','five_alternatives':records,'unique_strict_word':[5,0],'positive_raw_plus_marker_lengths':[len(raws[6]+raws[5]+raws[0]+raws[a]+mark)for a in(7,8,9)],'older_helper':xy(helper),'actual_core_time':66,'manifest_sha256':hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),'scope':'Only source VCC supplying both lower U inputs at exact C-age3; no fresh-root assumption, no U bound, no exclusion of the positive word.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

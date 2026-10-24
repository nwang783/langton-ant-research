"""Classify every literal recorded window; require complete exact source job coverage."""
import gzip,json,hashlib,collections
from pathlib import Path
from blank_collision_operator import H,geometry
P=Path(__file__).parent
phases={H[i:]+H[:i]:i for i in range(104)};assert len(phases)==104
geom={}
for word,i in phases.items():
 for h in range(4):
  _,end,eh=geometry((0,0),h,word);geom[(i,h)]=(end,eh)
counts=collections.Counter();hist=collections.Counter();bad=[];anchors=windows=0;sha=hashlib.sha256()
with gzip.open(P/'TWO_BLACK_WORD_JOBS.jsonl.gz','rt')as jf,open(P/'TWO_BLACK_WORD_ALL_FIXED_OUTPUT.txt')as rf,gzip.open(P/'TWO_BLACK_FIXED_WORD_ANNOTATIONS.jsonl.gz','wt')as out:
 for jline,rline in zip(jf,rf,strict=True):
  j=json.loads(jline);parts=rline.split();assert int(parts[0])==j['id']==anchors
  assert len(parts[1:])==len(j['windows']);ann=[]
  for raw,winfo in zip(parts[1:],j['windows'],strict=True):
   time,pose,disp,word=raw.split(':');time=int(time);pose=tuple(map(int,pose.split(',')));disp=tuple(map(int,disp.split(',')))
   assert time==winfo['time'] and len(word)==104 and set(word)<=set('LR')
   assert abs(disp[0])==abs(disp[1])==2 and disp[2]==0
   if winfo['kind']=='terminal':assert disp[:2]==tuple(j['terminal_drift'])
   phase=phases.get(word)
   if phase is None:bad.append([j['id'],time,winfo['kind'],word])
   else:assert geom[(phase,pose[2])]==(disp[:2],pose[2])
   row=dict(kind=winfo['kind'],time=time,pose_before=pose,actual_displacement=disp[:2],heading_restored=True,canonical_phase=phase,actual_word=word)
   ann.append(row);counts[winfo['kind']]+=1;hist[(winfo['kind'],phase)]+=1;windows+=1
  record=dict(id=j['id'],source=j['source'],kind=j['kind'],index=j['index'],initial_black=j['cells'],windows=ann)
  encoded=json.dumps(record,separators=(',',':'));out.write(encoded+'\n');sha.update((encoded+'\n').encode());anchors+=1
meta=json.loads((P/'TWO_BLACK_ALL_FIXED_RUN_META.json').read_text());assert meta['complete_process'] and meta['returncode']==0
assert(anchors,windows)==(102488,217233)
assert not bad,bad[:5]
result=dict(status='AUTHOR complete finite fixed-window annotation; independent audit pending',anchors=anchors,windows=windows,window_counts=dict(counts),noncanonical_windows=bad,
 canonical_reference_word=H,canonical_phase_histogram=[dict(kind=k[0],phase=k[1],count=v)for k,v in sorted(hist.items())],
 complete_jsonl_uncompressed_sha256=sha.hexdigest(),fixed_reads=3437614232,
 execution=meta,scope='All source-listed family anchors, slabs, and2432 singleton parent terminal hints; dynamically searched direct certB leaves NOT included.',
 canonical_budget_unconditional=False)
(P/'TWO_BLACK_FIXED_WORD_ANNOTATIONS_CHECKED.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(anchors=anchors,windows=windows,counts=dict(counts),noncanonical=len(bad))))

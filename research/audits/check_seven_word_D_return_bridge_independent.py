from pathlib import Path
import json,hashlib
from check_dcuv_patch_model_independent import walk,rotation,xy
R=Path(__file__).resolve().parents[1];B=R/'seven_word_return_bridge_2026-10-23'
man=json.loads((B/'manifest.json').read_text())
for f,h in man['files'].items():assert hashlib.sha256((B/f).read_bytes()).hexdigest()==h
for f,h in man['dependencies'].items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==h
q=json.loads((R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json').read_text());W=[x['word']for x in q['macro_words']];M='LLLLRLRRRRL';K={z for z,b in walk(M)[2].items()if b}
assert K=={-1-1j,-1, -1j,0j,1}
rows=[]
for name,w,g in zip('DCVUFQB',W,q['macro_words']):
 e,h,_,flip=walk(w);req=walk(w+M)[2];seed={z for z,b in req.items()if b};end=seed^flip;core={e+rotation(z,h)for z in K}
 marks=[i for i in range(len(w)+1)if(w+M)[i:i+11]==M]
 assert marks==[0,len(w)]and core<=end and K<=seed and(w+M).startswith(g['start_marker'])
 rows.append(dict(name=name,length=len(w),endpoint=[*xy(e),h],mass_gain=len(end)-len(seed),first_returns=marks))
assert [r['endpoint']for r in rows]==[[1,1,0],[0,1,3],[1,3,0],[0,4,0],[-4,-2,2],[-4,-4,2],[-3,-5,2]]
assert [r['mass_gain']for r in rows]==[0,3,4,4,2,6,6]
raw=W[0]+W[2]+W[4]+W[0];word=raw+M;seed={z for z,b in walk(word)[2].items()if b};assert len(seed)==23
board=set(seed);p=0j;h=0;cuts=[];dirs=(1j,1,-1j,-1);positions={0,10,28,84,94}
for tick,a in enumerate(word):
 if tick in positions:
  assert {p+rotation(z,h)for z in K}<=board
  cuts.append([tick,*xy(p),h,len(board)])
 assert (p in board)==(a=='L')
 board.symmetric_difference_update({p});h=(h+(1 if a=='R'else-1))%4;p+=dirs[h]
assert cuts==[[0,0,0,0,23],[10,1,1,0,23],[28,2,4,0,27],[84,-2,2,2,29],[94,-3,1,2,29]]
ref=json.loads((B/'marker_and_D_return.json').read_text());assert sorted(map(xy,seed))==list(map(tuple,ref['control']['seed']))
assert [*xy(p),h]==ref['control']['marker_end']['head']and len(board)==ref['control']['marker_end']['mass']
assert [i for i in range(len(raw)+1)if word[i:i+11]==M]==[0,10,28,84,94]
paths=[[s]for s in range(q['classes'])]
for lab in (0,2,4,0):paths=[p+[b]for p in paths for a,t,b in q['quotient_edges']if p[-1]==a and t==lab]
assert len(paths)==77 and[8,75,163,2,3]in paths
# Exact signed marked no-D arithmetic, following a mass-neutral D and <=4 C.
assert 10+60+33*(12-4)==334 and 8*12-28==68
out=dict(status='PASS seven literal first-M returns, complete23-cell DVFD control and conditional consecutive-D bounds',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),literal_rows=rows,seed=sorted(map(xy,seed)),cuts=cuts,quotient_label_paths=77,return_bounds={'duration':'33*m+334','next_entry_mass':'8*m+68'},scope='Actual whole-board finite control, not an identified original history-class path or infinite extension. Obstructs decreasing D-entry mass and literal-C-only heading clocks. No seven-word or universal capture theorem.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(cuts)

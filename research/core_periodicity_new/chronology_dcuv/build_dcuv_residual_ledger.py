"""Literal five-core residual ledger, allowing input/output overlap.
No recurrent packet pruning and no transfer exclusion is performed.
"""
import json,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parent;src=ROOT.parent.parent/'word_stabilization/seven_sub_dcvu_port_quotient.json';J=json.loads(src.read_text());dirs=((0,1),(1,0),(0,-1),(-1,0))
def trace(word):
 p=(0,0);h=0;first={};last={};odd=set()
 for phase,turn in enumerate(word):
  assert last.get(p)!=turn
  first.setdefault(p,(turn,phase));last[p]=turn;odd.symmetric_difference_update({p});h=(h+(1 if turn=='R'else-1))%4;p=(p[0]+dirs[h][0],p[1]+dirs[h][1])
 return p,h,first,last,odd
def rot(p,h):x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h]
core={p for p,(c,t)in trace('LLLLRLRRRRL')[2].items()if c=='L'};geometry=[]
for index,macro in enumerate(J['macro_words']):
 p,h,_,last,odd=trace(macro['word']);req=trace(macro['word']+macro['end_marker'])[2];before={q for q,(c,t)in req.items()if c=='L'};newcore={tuple(p[j]+rot(q,h)[j]for j in(0,1))for q in core};after=before^odd;ins=before-core;outs=after-newcore
 assert core<=before and newcore<=after
 assert all(last.get(q)=='R'for q in outs)
 geometry.append({'packet':index,'name':macro['name'],'word':macro['word'],'marker':macro['end_marker'],'endpoint':[*p,h],'inputs':sorted(ins),'outputs':sorted(outs),'recycled':sorted(ins&outs),'requirements':[[*q,c=='L',t]for q,(c,t)in sorted(req.items())],'raw_odd':sorted(odd),'mass_change':len(outs)-len(ins)})
result={'status':'LITERAL IDENTITY ONLY; no transfer exclusion or recurrent-type pruning claimed','source_file':str(src),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'core':sorted(core),'geometry':geometry,'kept_packet_types':list(range(len(geometry))),'update':'Remove every input token first, then install a fresh producer label at every output, including input/output intersections.'}
(ROOT/'literal_residual_geometry.json').write_text(json.dumps(result,indent=2))
print(json.dumps({'packets':len(geometry),'inputs':sum(len(g['inputs'])for g in geometry),'outputs':sum(len(g['outputs'])for g in geometry),'intersections':[(g['name'],g['recycled'])for g in geometry if g['recycled']]}))

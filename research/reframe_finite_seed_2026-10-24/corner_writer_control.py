"""Literal full-field controls for cap-six corner preservation and forced overlap."""
from active_flight import *
from pathlib import Path
import json
OUT=Path(__file__).parent
D={(-1,1),(-1,2)};STAR={(0,-1),(1,-1),(1,0)};CORNER={(-2,1),(-2,2)};SINGLE={(-1,0)}
def replay(B,n):
 B=set(B);p=(0,0);h=0;cuts=[];word=''
 for t in range(n+1):
  C=comp(B,1,cursor(p,h));cuts.append({'t':t,'pose':[p,h],'field':sorted(B),'active_component':sorted(C)})
  if t<n:word+='L'if p in B else'R';p,h=step(B,p,h)
 return cuts,word
c,w=replay(D,10);assert w=='RRRRLRLRRL';assert c[-1]['pose']==[(-1,3),0];assert set(map(tuple,c[-1]['field']))==STAR|CORNER|SINGLE;assert max(len(a['active_component'])for a in c)==6
assert comp(STAR|CORNER|SINGLE,1,ends(next(iter(CORNER)),1)[0])==CORNER
assert comp(STAR|CORNER|SINGLE,1,ends((-1,0),1)[0])==SINGLE
assert comp(STAR|CORNER|SINGLE,1,ends((0,-1),1)[0])==STAR
NEXT={(-2,4),(-2,5)};cc,ww=replay(D|NEXT,14);assert cc[10]['pose']==[(-1,3),0]and len(cc[14]['active_component'])==8
# Through the first block the paid next module remains passive and unchanged.
for a,b in zip(c,cc):
 assert a['pose']==b['pose']and a['active_component']==b['active_component']
 assert set(map(tuple,b['field']))==set(map(tuple,a['field']))|NEXT
out={'status':'AUTHOR_ACTUAL_FINITE_BOARD_CONTROLS_PENDING_AUDIT','one_block':{'seed':sorted(D),'word':w,'cuts':c},'prepaid_two_block_attempt':{'seed':sorted(D|NEXT),'word_prefix':ww,'cuts':cc},'resource_net':{'same_oriented_corner':0,'singleton':1,'three_star':1},'scope':'One genuine writer block; no repeatable compiler. Identical translated second block fails its full-component profile at fourth R.'}
(OUT/'corner_writer_controls.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS: actual cap6 writer; prepaid repeat forced mass8 atcut14')

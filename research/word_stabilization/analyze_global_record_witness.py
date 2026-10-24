"""Decode and independently inspect the literal visible prefix before first OUT.
Reports exact alternating-read conflicts and high initial-input funding outside patch.
Not a claim that an OUT witness is physically realizable.
"""
from pathlib import Path
import json,sys
f=Path(sys.argv[1]);w=Path(sys.argv[2]);out=Path(sys.argv[3]);J=json.loads(f.read_text());B=Path(__file__).resolve().parents[1]/'core_periodicity_new';G=json.loads((B/'chronology_dcuv/literal_residual_geometry.json').read_text());geo=G['geometry'];W=json.loads(Path(J['potential_file']).read_text());v=W['values'];ph=J['target_global_phase'];I=J['initial_token_weight'];S=J['record_threshold'];points=set(map(tuple,J['points']))
def rot(q,h):x,y=q;return [(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def at(p,q):z=rot(q,p[2]);return p[0]+z[0],p[1]+z[1]
def value(q):z=rot(q,ph);return I+2*(v['ax']*z[0]+v['ay']*z[1])
rows=[]
for line in w.read_text().splitlines():
 if not line.startswith('WITNESS'):continue
 _,s,m,a=line.split();s,m,a=map(int,(s,m,a));rows.append({'pose_id':s,'pose':J['poses'][s]if s<len(J['poses'])else'INIT'if s==J['initial_control_pose']else'OUT','mask':m,'packet':a if a<2**63 else -1})
req0={};parity=set();produced={};initial_core=set();funds=[];conflicts=[];events=[]
for ri,r in enumerate(rows):
 if r['pose']=='INIT':continue
 if r['pose']=='OUT':break
 p=r['pose'];a=r['packet'];g=geo[a]
 if not initial_core:
  initial_core={at(p,q)for q in G['core']};req0.update({q:1 for q in initial_core})
 for z in g['requirements']:
  q=at(p,z[:2]);b=int(z[2])^(q in parity)
  if q in req0 and req0[q]!=b:conflicts.append({'row':ri,'packet':a,'cell':q,'required_initial':b,'previous':req0[q],'retained':q in points})
  else:req0[q]=b
 inputs={at(p,q)for q in g['inputs']};outputs={at(p,q)for q in g['outputs']}
 for q in inputs:
  if q not in produced:
   ev={'row':ri,'packet':a,'cell':q,'activation':value(q),'high':value(q)>=S,'retained':q in points};events.append(ev)
   if ev['high']:funds.append(ev)
  produced.pop(q,None)
 for q in outputs:produced[q]=ri
 parity^={at(p,q)for q in g['raw_odd']}
O={'model':str(f.resolve()),'witness':str(w.resolve()),'threshold':S,'rows':rows,'visible_prefix_conflicts':conflicts,'visible_prefix_initial_inputs':events,'visible_prefix_high_funding':funds,'refinement_cells':sorted({tuple(e['cell'])for e in conflicts+funds if not e['retained']}),'status':'Abstract path only; analysis stops at first OUT.'};out.write_text(json.dumps(O,indent=2)+'\n');print(json.dumps({k:O[k]for k in ['threshold','visible_prefix_conflicts','visible_prefix_high_funding','refinement_cells']},indent=2))

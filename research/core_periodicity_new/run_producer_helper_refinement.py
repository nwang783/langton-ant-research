"""Bounded CEGAR discovery on10 auxiliary protected transfers. NO theorem from H202 alone."""
from pathlib import Path
import json,subprocess,os,re
P=Path(__file__).resolve().parent;W=P.parent/'word_stabilization';OUT=P/'producer_helper_refinement';OUT.mkdir(exist_ok=True);rows=[(1,4,2,6,2,2,3),(1,4,3,5,2,3,2),(1,5,3,5,2,3,2),(4,4,-3,0,1,0,0),(4,4,1,3,2,1,0),(4,4,5,2,3,2,2),(4,5,1,3,2,1,0),(5,4,-3,0,1,0,0),(5,4,2,8,2,2,5),(5,4,3,7,2,3,4)];H={tuple(map(int,l.split()))for l in(P/'producer_labels_hypothesis_202.tsv').read_text().splitlines()};summary=[]
def cmd(args,out,timeout=180):
 try:
  r=subprocess.run(args,cwd=P,capture_output=True,text=True,timeout=timeout,env={**os.environ,'PRODUCER_LABEL_ALLOW_WIDE':'1'});Path(str(out)+'.txt').write_text(r.stdout);Path(str(out)+'.log').write_text(r.stderr);return r.stdout
 except subprocess.TimeoutExpired as e:
  Path(str(out)+'.txt').write_text('TIMEOUT');Path(str(out)+'.log').write_text((e.stderr or b'').decode()if isinstance(e.stderr,bytes)else e.stderr or'');return'TIMEOUT'
def witness(model,pre):
 text=cmd([str(P/'protected_patch_bdd_labels_witness'if 'producer_label_classes'in model else P/'protected_patch_bdd_witness'),str(pre)+'.dat','2000000'],str(pre)+'_witness');path=[]
 for l in text.splitlines():
  if not l.startswith('WITNESS'):continue
  _,s,c,a=l.split();s,c,a=map(int,(s,c,a));path.append({'pose':model['poses'][s]if s<model['out']else None,'color':c,'packet_id':a})
 if path:Path(str(pre)+'_witness.json').write_text(json.dumps(path,indent=2))
 return path,text
for ci,row in enumerate(rows,1):
 pre=OUT/f'case{ci:02d}';cmd(['python',str(P/'generate_protected_transfer_patch.py'),*map(str,row),str(pre),'both'],str(pre)+'_gen');B=json.loads(pre.with_suffix('.json').read_text());rec={'case':ci,'tuple':row,'base_variables':B['n'],'rounds':[]};summary.append(rec);Q=[];model=B;current=pre
 for roundi in range(5):
  path,text=witness(model,current)
  if not path:rec['rounds'].append({'round':roundi,'status':'BASE_OR_WITNESS_CAP','text':text.splitlines()[:1]});break
  cmd(['python',str(P/'analyze_patch_witness_labels.py'),str(pre)+'.json',str(current)+'_witness.json'],str(current)+'_analysis');ev=json.loads(Path(str(current)+'_witness.labels.json').read_text());new=[]
  for e in ev:
   q=tuple(e['cell'])
   if not e['outer_to_goal']and tuple(e['tuple'])in H and q not in Q and q not in new:new.append(q)
  if not new:rec['rounds'].append({'round':roundi,'status':'WITNESS_WITHOUT_NEW_TRACKED_H_TRANSFER','watched':Q,'events':ev});break
  Q+=new[:max(0,5-len(Q))]
  if not Q or(roundi and not new)or len(Q)>5:break
  exact=OUT/f'case{ci:02d}_r{roundi}_exact';quot=OUT/f'case{ci:02d}_r{roundi}_quotient';s=cmd(['python',str(P/'add_protected_producer_labels.py'),str(pre)+'.json',str(exact),str(P/'producer_labels_hypothesis_202.tsv'),';'.join(f'{x},{y}'for x,y in Q),str(W/'dcv_anchored_signed41.tsv')],str(exact)+'_gen');s=cmd(['python',str(P/'quotient_protected_producer_labels.py'),str(exact)+'.json',str(quot)],str(quot)+'_gen')
  if not quot.with_suffix('.json').exists():rec['rounds'].append({'round':roundi,'status':'MODEL_ERROR','text':s});break
  model=json.loads(quot.with_suffix('.json').read_text());current=quot;s=cmd([str(P/'protected_patch_bdd_labels'),str(quot)+'.dat','2000000',str(quot)+'.bdd'],quot);rr={'round':roundi,'watched':list(Q),'variables':model['n'],'result':s.strip()};rec['rounds'].append(rr)
  if'EXHAUSTED_NO_HIT'in s:
   v=cmd(['python',str(P/'verify_protected_patch_bdd_labels.py'),str(quot)+'.dat',str(quot)+'.bdd'],str(quot)+'_verify');rr['verification']=v.strip();break
  if'ABSTRACT_WITNESS'not in s:break
  if len(Q)==5:break
  (OUT/'summary.json').write_text(json.dumps(summary,indent=2))
 (OUT/'summary.json').write_text(json.dumps(summary,indent=2));print(json.dumps(rec),flush=True)

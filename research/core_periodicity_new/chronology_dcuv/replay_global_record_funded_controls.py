from pathlib import Path
import json,subprocess,hashlib,collections
R=Path(__file__).resolve().parents[1];D=R/'chronology_dcuv';out=D/'global_record_controls';out.mkdir(exist_ok=True);C=json.load(open(D/'record_head_offset_search/funded_record_controls15.json'))['controls'];results=[]
for a,h in sorted(set((c['target_type'],c['target_global_phase'])for c in C)):
 for allow in [False,True]:
  p=out/f't{a}h{h}_{"allow"if allow else"reject"}';cmd=['python',str(R/('generate_resource_global_record_control.py'if allow else'generate_resource_global_record.py')),str(D/'profile_recurrent8.json'),str(D/'record_head_offset_search/head_1_1.json'),str(a),str(h),str(p),'context','all'];subprocess.run(cmd,check=True,stdout=subprocess.DEVNULL)
  J=json.load(open(p.with_suffix('.json')));heads={tuple(p):i for i,p in enumerate(J['poses'])};edges=collections.defaultdict(list)
  for t in J['transitions']:edges[t[0]].append(t)
  for control in [c for c in C if(c['target_type'],c['target_global_phase'])==(a,h)]:
   board=set(map(tuple,control['initial_black_seed']));state=0
   for cell in J['origin_cells']:
    if tuple(cell['cell'])in board:state|=(2 if cell['watched']else 1)<<cell['offset']
   assert state&J['start'][1]==J['start'][2]
   sid=heads.get(tuple(control['initial_head_pose']),J['out']);init=next(t for t in edges[J['initial_control_pose']]if t[1]==sid);state=((state^init[4])&~init[5])|init[6];blocked=None;accepted=False
   for i,step in enumerate(control['records']):
    actual=heads.get(tuple(step['pose']),J['out'])
    if sid==J['out']and actual!=J['out']:assert actual in J['reentry'];sid=actual
    assert sid==actual
    if sid==J['out']:continue # actual hidden packets miss every retained cell
    matches=[t for t in edges[sid]if t[8]==step['packet']and state&t[2]==t[3]]
    if not matches:blocked=i;break
    assert len(matches)==1,(control['control'],i,len(matches));t=matches[0];state=((state^t[4])&~t[5])|t[6];sid=t[1]
    if t[7]:assert i==len(control['records'])-1;accepted=True
   if allow:assert accepted and blocked is None,(control['control'],blocked)
   else:assert blocked is not None and not accepted,(control['control'],'funding not detected')
   results.append({'control':control['control'],'target':a,'phase':h,'allow_funding':allow,'accepted':accepted,'first_blocked_step':blocked,'model_file':str(p.with_suffix('.json'))})
obj={'status':'All funded controls accepted when activation cuts disabled and rejected with cuts enabled','count':len(C),'results':results};(out/'funded_replay.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({'count':len(C),'checks':len(results),'status':'PASS'}))

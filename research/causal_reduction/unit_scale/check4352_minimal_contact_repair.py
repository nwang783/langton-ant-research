"""Complete length<=9 exact-pose inventory at the supplied old-bit contact.
Only lengths1,5,9 are geometrically possible; first turn is forced L.
Every internally legal candidate fails its SECOND read on the owned white cell.
"""
from pathlib import Path
from itertools import product
import json,hashlib
from check_prepared1564_router_geometry import trace
from probe4352_return_end_limit import L,A
import inverse4352_tail_completion as T
P=Path(__file__).resolve().parent
q=(14,-7);owned=(14,-8);target=((14,-6),0)
launch=[]
for i,p,h,c in list(trace(L['forward_prelude_word'],tuple(L['forward_entry_pose'][0]),L['forward_entry_pose'][1]))[:-1]:
 if p==owned:launch.append([i,h,c])
assert launch==[[5209,0,'L'],[5213,2,'R'],[5217,0,'L']]
assert not T.future_read(owned)
return_prefix=list(trace((A['word']*2)[:17353],(117,111),0))
assert all(p!=owned for i,p,h,c in return_prefix[:-1])
assert(return_prefix[-1][1],return_prefix[-1][2])==(q,3)
manifest=json.loads((P/'prepared4352_two_phase_manifest.json').read_text())
mins=[]
for s in manifest['stages'][12:14]:
 base=(s['start_x_N_constant'][1],s['start_y_N_constant'][1]);a=s['start_x_N_constant'][0]+s['start_y_N_constant'][0]
 rows=list(trace(s['word'],base,s['heading']));du=sum(rows[-1][1])-sum(base)
 low=min(sum(p)for _,p,_,_ in rows[:-1]);cm,cc=s['count_N_constant']
 if du<0:a+=du*cm;low+=du*(cc-1)
 assert a>=0 and a+low>sum(owned)
 mins.append({'kind':s['kind'],'read_lower_u_M_constant':[a,low],'minimum_M_ge_1':a+low})
inventories=[]
for n in(1,5,9):
 records=[];legal=[]
 for rest in product('RL',repeat=n-1):
  word='L'+''.join(rest);rr=list(trace(word,q,3))
  if(rr[-1][1],rr[-1][2])!=target:continue
  last={};conflict=None
  for i,p,h,c in rr[:-1]:
   if p in last and last[p][1]==c:conflict={'read':i,'cell':p,'previous_read':last[p][0],'turn':c};break
   last[p]=(i,c)
  record={'word':word,'internal_conflict':conflict}
  if conflict is None:
   legal.append(word);assert rr[1][1]==owned and rr[1][3]=='L'
   record['inherited_conflict']={'read':1,'cell':owned,'required':'L','actual':'R','last_launch_read':5217}
  records.append(record)
 inventories.append({'length':n,'geometric_count':len(records),'internally_legal':legal,'records':records})
assert[inventories[i]['geometric_count']for i in range(3)]==[0,2,18]
assert inventories[1]['internally_legal']==['LLLLR']
assert set(inventories[2]['internally_legal'])=={'LLRRRRLLR','LLLRRRRLR','LLLLRLLLL'}
out={'scope':__doc__,'status':'NO PHYSICAL EXACT-POSE REPAIR THROUGH LENGTH9','contact':[q,3],'target_pose':target,'owned_white_cell':owned,'launch_history':launch,'owned_cell_whole_future4352_unread':True,'later_stage_minima':mins,'fixed_extra_return_prefix_reads':17353,'inventory':inventories,'manifest_sha256':hashlib.sha256((P/'prepared4352_two_phase_manifest.json').read_bytes()).hexdigest(),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(P/'prepared4352_minimal_contact_repair.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k!='inventory'})

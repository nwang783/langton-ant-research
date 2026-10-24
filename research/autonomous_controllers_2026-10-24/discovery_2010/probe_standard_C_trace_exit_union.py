import sys,itertools,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from certify_C_trace_lap_ownership import build,uniform_propagation,verify_assignment,realize,WORDS
from certify_exit_component_turn_flux import analyze
z=build(WORDS['S104']);p=uniform_propagation(z,False);free=sorted(set(z['optional'])-p['values'].keys());rows=[]
for bits in itertools.product([0,1],repeat=len(free)):
 vals=p['values']|dict(zip(free,bits))
 try:a=verify_assignment(z,vals,False)
 except AssertionError:continue
 s=analyze(a['word'],z['heading']);cross=s['all_actual_cross_component_steps'];first=[e for e in cross if e['source_first_read'] and e['source_turn']=='R'];n=len(s['components'])
 connected={0}
 while True:
  new=connected|{e['source_component']for e in first if e['target_component']in connected}|{e['target_component']for e in first if e['source_component']in connected}
  if new==connected:break
  connected=new
 row={'bits':bits,**a,'components':[(c['O'],c['I'])for c in s['components']],'cross_count':len(cross),'first_R_crosses':len(first),'union_connected':len(connected)==n};rows.append(row)
 print(row)
Path(__file__).with_suffix('.json').write_text(json.dumps({'free':free,'fixed':p['values'],'valid':rows},indent=2)+'\n')
print('TOTAL',len(rows))

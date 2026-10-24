"""Add the signed latest-output joint clock to an exact-low colored/Q model.
CLI MODEL.json PORT_SCC.json WATCHED_CELLS.json PREFIX.
Only a simultaneous use of every watched cell as an age4 residual input is
guarded. Reads do not retire this aggregate latest-output clock.
"""
from pathlib import Path
import sys,json,hashlib
src,sc,wp,out=map(Path,sys.argv[1:5]);J=json.loads(src.read_text());C=json.loads(sc.read_text());B=json.loads(Path(J['base_model_file']).read_text());S=json.loads(Path(B['base_model_file']).read_text());G=json.loads(Path(json.loads(Path(B['literal_dfa_file']).read_text())['geometry_file']).read_text())['geometry'];watched=set(map(tuple,json.loads(wp.read_text())));rules={(a,x,y):r for a,x,y,r in json.loads(Path('chronology_dcuv/counted_input_age_rules_complete.json').read_text())};oldn=J['n'];mask=7<<oldn
def rot(p,h):x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def physical(p):
 z=J['positions'][p]
 if z[0]!='near':return None
 pose=B['poses'][z[1]];assert pose is not None;return pose
cm={(a,b):c for a,b,c in C['condensation_edges']};positive=set(C['positive_cycle_components']);E=[];stats=dict(reset=0,guard=0,aged=0,unchanged=0,low_mature_loops=0)
def emit(e,c,reset,need):
 if reset:
  z=e[:];z[5]|=mask;z[6]|=c<<oldn
  if need:z[2]|=mask;z[3]|=4<<oldn
  E.append(z);stats['reset']+=1;return
 if need:
  z=e[:];z[2]|=mask;z[3]|=4<<oldn;E.append(z);stats['guard']+=1;return
 if c==0:E.append(e[:]);stats['unchanged']+=1;return
 if c>=4:
  z=e[:];z[5]|=mask;z[6]|=4<<oldn;E.append(z);stats['aged']+=1;return
 for age in range(5):
  z=e[:];z[2]|=mask;z[3]|=age<<oldn;z[5]|=mask;z[6]|=min(4,age+c)<<oldn;E.append(z)
 stats['aged']+=1
for e in J['transitions']:
 a=e[8];zs,zt=J['positions'][e[0]],J['positions'][e[1]]
 if a==99:
  c=cm[zs[1],zt[1]]if zs[0]==zt[0]=='low_scc'else 0;emit(e,c,False,False);continue
 c=G[a]['name'].count('C');pose=physical(e[0]);reset=need=False
 if pose is not None:
  x,y,h=pose
  def at(p):u,v=rot(p,h);return x+u,y+v
  outputs={at(p)for p in G[a]['outputs']};upper={at(p)for p in G[a]['inputs']if rules[a,*p]>=4}
  reset=bool(outputs&watched);need=watched<=upper
 emit(e,c,reset,need)
for p,z in enumerate(J['positions']):
 if z[0]=='low_scc'and z[1]in positive:
  emit([p,p,0,0,0,0,0,0,104],4,False,False);stats['low_mature_loops']+=1
N={k:v for k,v in J.items()if k not in['transitions','start']};N.update(format='guarded_reset_exact_low_joint_upper_clock_v1',n=oldn+3,start=[J['start'][0],J['start'][1]|mask,J['start'][2]|(4<<oldn)],transitions=E,base_model_file=str(src.resolve()),base_model_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),clock_shift=oldn,clock_bits=3,clock_initial=4,watched_cells=sorted(watched),clock_stats=stats,scope=J['scope']+' A latest-output C clock for any watched cell is added. It resets on ANY watched output and never retires on reads. Only simultaneous upper residual inputs of ALL watched cells require age4. Exact low summaries age it by their attained saturated C maximum, and positive-C low SCCs have an attained mature4 self loop. Valid ages0..4 are invariant; codes5..7 are unused.')
out.with_suffix('.json').write_text(json.dumps(N,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f'{N["n"]} {len(J["positions"])} {len(E)} 0\n');f.write(' '.join(map(str,N['start']))+'\n')
 for e in E:f.write(' '.join(map(str,e))+'\n')
 f.write('\n')
print(dict(bits=N['n'],positions=len(J['positions']),edges=len(E),stats=stats))

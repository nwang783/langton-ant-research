from pathlib import Path
import json,sys,collections
path=Path(sys.argv[1]);J=json.loads(path.read_text());B=json.loads(Path(J['base_model_file']).read_text());G=json.loads((Path(__file__).resolve().parents[1]/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json').read_text())['geometry'];n=B['n'];cell=complex(*J['watched_cell']);groups=collections.defaultdict(list)
for e,(ei,age,new)in zip(J['transitions'],J['edge_cases']):groups[ei].append(e)
poses=J['poses'];checks=0;upper0=[-1+4j,2j,3j]
for ei,e in enumerate(B['transitions']):
 p,to,k,v,f,c,r,goal,a=e;pose=poses[p];g=G[a];cc=g['name'].count('C');upper=False;out=set();touch=set()
 if pose is not None:
  x,y,h=pose;z=complex(x,y);rr=(-1j)**h;out={z+complex(*q)*rr for q in g['outputs']};touch={z+complex(*q[:2])*rr for q in g['requirements']};upper=a in [7,8,9]and cell in {z+q*rr for q in upper0}
 for age in range(5):
  s=v|(age<<n);matches=[ee for ee in groups[ei]if(s&ee[2])==ee[3]];expected=not upper or age==4;assert bool(matches)==expected,(ei,age,upper)
  if expected:
   want=cc if cell in out else 4 if cell in touch else min(4,age+cc);outcolor=((v^f)&~c)|(r&c)
   for ee in matches:
    dest=((s^ee[4])&~ee[5])|(ee[6]&ee[5]);assert dest==outcolor|(want<<n),(ei,age,want,dest);assert ee[0:2]==e[0:2]and ee[7:]==e[7:]
  checks+=1
assert J['start'][2]>>n==4 and J['start'][1]>>n==7
O={'status':'PASS local separate complex-coordinate age replay','edge_age_checks':checks,'base_edges':len(B['transitions']),'new_edges':len(J['transitions']),'scope':'Exact transition semantics on reachable ages0..4 only; independent audit remains separate.'};path.with_suffix('.local_age_check.json').write_text(json.dumps(O,indent=2));print(json.dumps(O))

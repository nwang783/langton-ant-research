"""CEGAR by adding exact high-height age-multiset resources, never a count cap.
CLI FULL_HEIGHT_PETRI.json OUTDIR LABEL_CAP.
"""
from pathlib import Path
import sys,json,subprocess
src,directory=map(Path,sys.argv[1:3]);limit=int(sys.argv[3]);directory.mkdir(exist_ok=True);J=json.loads(src.read_text());S=json.loads(Path(J['source_file']).read_text());G=json.loads(Path('chronology_dcuv/literal_residual_geometry.json').read_text())['geometry'];ages={(a,x,y):r for a,x,y,r in json.loads(Path('chronology_dcuv/counted_input_age_rules_complete.json').read_text())};phase=S['phase'];F=J['initial_bound'];selected={h for _,r in J['goal_requirements']for h,x in zip(J['places'],r)if x};summ=[]
def rot(p,h):x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def ht(p):return sum(rot(p,phase))
def replay(lines):
 M={};path=[];p=int(next(x for x in lines if x.startswith('start ')).split()[1]);assert p in J['initial_controls']
 for raw in [s for s in lines if s.startswith('EDGE ')]+[None]:
  if raw is not None:
   ei,fr,to,a=map(int,raw.split()[1:5]);assert p==fr;assert J['transitions'][ei][:3]==[fr,to,a]
  else:ei=None;fr=p;to=None;a=S['target'];assert any(pp==p for pp,_ in J['goal_requirements'])
  h,q=J['poses'][J['positions'][fr][0]];c=G[a]['name'].count('C');req=[];put=[]
  if q is not None:
   req=[(q+ht(rot(v,h)),ages[a,*v])for v in G[a]['inputs']if q+ht(rot(v,h))>F]
   put=[q+ht(rot(v,h))for v in G[a]['outputs']if q+ht(rot(v,h))>F]
  for z,r in sorted(req,key=lambda x:-x[1]):
   row=M.setdefault(z,[]);cand=[k for k,x in enumerate(row)if x>=r]
   if not cand:return {'status':'FULL_AGE_DEFICIT','height':z,'needed_age':r,'available_ages':sorted(row),'packet_index':len(path),'word':[v['packet']for v in path]+[a],'path':path}
   k=min(cand,key=lambda k:row[k]);row.pop(k)
  path.append({'edge':ei,'packet':a,'pose':[h,q]})
  for z in M:M[z]=[min(4,x+c)for x in M[z]]
  for z in put:M.setdefault(z,[]).append(c)
  p=to
 return {'status':'FULL_AGE_WITNESS','word':[v['packet']for v in path],'path':path,'max_actual_count':max(map(len,M.values()),default=0)}
for rnd in range(len(J['places'])+1):
 p=directory/f'round{rnd:02d}';subprocess.run([sys.executable,'build_record_height_age_petri.py',str(src),str(p),','.join(map(str,sorted(selected)))],check=True)
 with p.with_suffix('.txt').open('w')as fo,p.with_suffix('.log').open('w')as fe:subprocess.run(['./record_height_age_petri_backward',str(p.with_suffix('.dat')),str(limit),str(p.with_suffix('.basis'))],stdout=fo,stderr=fe,check=True)
 lines=p.with_suffix('.txt').read_text().splitlines();rec={'round':rnd,'heights':sorted(selected),'status':lines[0],'prefix':str(p)};summ.append(rec)
 if lines[0].startswith('status AGE_PETRI_WITNESS'):
  r=replay(lines);p.with_suffix('.replay.json').write_text(json.dumps(r,indent=2)+'\n');rec.update({k:v for k,v in r.items()if k not in ['path','word']})
  if r['status']=='FULL_AGE_DEFICIT':assert r['height']not in selected;selected.add(r['height'])
 (directory/'summary.json').write_text(json.dumps(summ,indent=2)+'\n');print(json.dumps(rec),flush=True)
 if not lines[0].startswith('status AGE_PETRI_WITNESS')or r['status']=='FULL_AGE_WITNESS':break

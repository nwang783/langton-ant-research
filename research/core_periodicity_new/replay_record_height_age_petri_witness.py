"""Replay a resource witness with separate current token birth-C timestamps.
CLI ORIGINAL_HEIGHT_PETRI.json WITNESS.txt OUTPUT.json [PRUNED.edge_ids].
Ignores printed count vectors and independently derives every slot from geometry.
"""
from pathlib import Path
import sys,json,hashlib
src,txt,out=map(Path,sys.argv[1:4]);J=json.loads(src.read_text());S=json.loads(Path(J['source_file']).read_text());G=json.loads(Path('chronology_dcuv/literal_residual_geometry.json').read_text())['geometry'];ages={(a,x,y):r for a,x,y,r in json.loads(Path('chronology_dcuv/counted_input_age_rules_complete.json').read_text())};ids=list(map(int,Path(sys.argv[4]).read_text().split()))if len(sys.argv)>4 else None;phase=S['phase'];F=J['initial_bound'];M={};C=0;rows=[];lines=txt.read_text().splitlines();p=int(next(x for x in lines if x.startswith('start ')).split()[1]);assert p in J['initial_controls'];start=p;peak=0

def rot(p,h):x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def ht(p):return sum(rot(p,phase))
for raw in [s for s in lines if s.startswith('EDGE ')]+[None]:
 if raw is not None:
  ei,fr,to,a=map(int,raw.split()[1:5]);ei=ids[ei]if ids is not None else ei;assert p==fr;assert J['transitions'][ei][:3]==[fr,to,a]
 else:ei=None;fr=p;to=None;a=S['target'];assert any(pp==p for pp,_ in J['goal_requirements'])
 h,q=J['poses'][J['positions'][fr][0]];c=G[a]['name'].count('C');req=[];put=[];cons=[]
 if q is not None:
  req=[(q+ht(rot(v,h)),ages[a,*v])for v in G[a]['inputs']if q+ht(rot(v,h))>F]
  put=[q+ht(rot(v,h))for v in G[a]['outputs']if q+ht(rot(v,h))>F]
 for z,r in sorted(req,key=lambda x:-x[1]):
  row=M.setdefault(z,[]);eligible=[k for k,birth in enumerate(row)if C-birth>=r];assert eligible,(len(rows),a,z,r,[C-b for b in row])
  k=max(eligible,key=lambda k:row[k]);birth=row.pop(k);cons.append({'height':z,'required_age':r,'actual_age':C-birth})
 rows.append({'edge':ei,'packet':a,'pose':[h,q],'C_before':C,'consumed':cons,'outputs':put})
 # Outputs are born at producer START, so their age is c at the next start.
 for z in put:M.setdefault(z,[]).append(C)
 C+=c;p=to;peak=max(peak,max(map(len,M.values()),default=0))
R={'status':'PASS_FULL_CURRENT_HEIGHT_AGE_MULTISET','source_file':str(src.resolve()),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'witness_file':str(txt.resolve()),'witness_sha256':hashlib.sha256(txt.read_bytes()).hexdigest(),'packets_before_goal':len(rows)-1,'total_C_before_goal':rows[-1]['C_before'],'peak_count_per_height':peak,'word_including_goal':[r['packet']for r in rows],'rows':rows,'scope':'Actual finite-control path in the height/C-age resource overapproximation, with exact unbounded token multiplicities. No transverse coordinate, HB producer role or literal ant legality is asserted.'};out.write_text(json.dumps(R,indent=2)+'\n');print({k:v for k,v in R.items()if k not in ['rows','word_including_goal']})

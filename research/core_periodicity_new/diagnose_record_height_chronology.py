from pathlib import Path
import json,sys
src,model,out=map(Path,sys.argv[1:4]);J=json.loads(src.read_text());M=json.loads(model.read_text());S=json.loads(Path(M['source_file']).read_text());G=json.loads(Path('chronology_dcuv/literal_residual_geometry.json').read_text())['geometry'];phase=S['phase'];q=0;bad=[];rows=[]
def rot(p,h):x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
for k in range(len(J['rows'])-1,-1,-1):
 row=J['rows'][k];h,stored=row['pose'];a=row['packet']
 if k<len(J['rows'])-1:q-=sum(rot(rot(G[a]['endpoint'][:2],h),phase))
 ok=q==stored if stored is not None else q<=M['low_cutoff']
 r={'packet_index':k,'packet':a,'heading':h,'stored_height':stored,'actual_height':q,'low_cutoff':M['low_cutoff'],'matches':ok};rows.append(r)
 if not ok:bad.append(r)
R={'status':'EXACT_HEIGHT_CHRONOLOGY'if not bad else'LOW_BIN_HEIGHT_CHRONOLOGY_FAIL','mismatches':len(bad),'first_mismatch':min(bad,key=lambda x:x['packet_index'])if bad else None,'actual_height_range':[min(r['actual_height']for r in rows),max(r['actual_height']for r in rows)],'rows':list(reversed(rows))};out.write_text(json.dumps(R,indent=2)+'\n');print({k:v for k,v in R.items()if k!='rows'})

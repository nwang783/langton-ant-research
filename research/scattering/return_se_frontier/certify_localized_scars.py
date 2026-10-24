"""Four exact complete-field rejoins and all-parameter scar transparency."""
import sys,json,gzip,hashlib
from pathlib import Path
R=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(R/'scattering/fixed_core_rectangle'))
from bivariate import A
sys.path.insert(0,str(R/'continuation_2026-10-22/ant_continuation'))
from ant_exact import W,plan,multiple,canonical_source
M=(1,0,100);N=(1,1,200);SE=(2,-2)
TFILE=R/'continuation_2026-10-22/ant_continuation2/planar_structure/exceptional_rectangle_template.json'
def c(v):return (0,0,v)
def sn(a,b):return A.add(A.scale(N,a),c(b))
def odd(word,h):
 qs,_,p,eh=plan(word,(0,0),h);o=set()
 for q in qs:o.symmetric_difference_update({q})
 return o,p,eh,qs

def main():
 data=json.loads((HERE/'parallel_model_discovery.json').read_text());cert=json.loads((HERE/'parallel_model_certificate.json').read_text())
 source={r['phase']:r for r in cert['records']};old={r['phase']:r for r in json.loads((R/'scattering/retained_frontier/localized_scars.json').read_text())['rows']}
 fresh,_,_,_=plan(W,(0,0),2);rows=[];scarpoints={}
 for r in (13,14,27,89):
  row=next(q for q in data if q['r']==r and q['mature']);bound=source[r]
  assert row['capture']==bound['local_capture'] and row['phase']==bound['word_phase']
  assert row['pose']==bound['local_pose'] and row['tail_word']==W[bound['word_phase']:]+W[:bound['word_phase']]
  word=gzip.open(HERE/row['word_file'],'rt').read();assert hashlib.sha256(word.encode()).hexdigest()==bound['word_sha256']
  flips,p,h,reads=odd(word,2);assert list(p)==row['pose'][0] and h==row['pose'][1]
  phase=row['phase'];_,rp,rh=canonical_source(0,phase);k=multiple((p[0]-rp[0],p[1]-rp[1]),SE);assert k is not None and h==rh
  geo=104*k+phase;ref=W*k+W[:phase];other,ep,eh,rreads=odd(ref,2);assert (ep,eh)==(p,h)
  assert all(-200<=x-y<=200 for x,y in reads+rreads)
  S={fresh[r]}^flips^other
  # Exact global field difference. Both executions start from the same full
  # field except the retained toggle; every background term cancels.
  expected={(-15-x,29-y) for x,y in old[r]['scar_base']};assert S==expected
  physical=sorted((-62+x,2+y) for x,y in S)
  assert row['capture']-geo==old[r]['time_delay']=={13:20,14:120,27:132,89:32}[r]
  assert A.negative(A.sub(c(geo),A.scale(A.add(M,c(7)),104)))
  tailqs,_,drift,th=plan(row['tail_word'],(0,0),h);assert drift==SE and th==h
  for q in S:
   for v in tailqs:
    j=multiple((q[0]-p[0]-v[0],q[1]-p[1]-v[1]),SE);assert j is None or j<0
  assert max(abs(-60+x+y) for x,y in reads)<=82
  # The unchanged remote c,d are absent during the altered local words too.
  local_u_upper=A.add(A.scale(M,-4),c(-64+bound['source_u_bounds'][1]))
  c_u=A.add(A.scale(N,4),c(22));d_z=A.add(A.scale(N,4),c(49))
  assert A.negative(A.sub(local_u_upper,c_u))
  assert A.negative(A.sub(c(82),d_z))
  assert max(x-y for x,y in physical)-400<98
  scarpoints[r]=[(A.add(A.scale(M,-2),c(x)),A.add(A.scale(M,2),c(y))) for x,y in physical]
  rows.append(dict(phase=r,scar_base=physical,scar_size=len(S),local_checkpoint=row['capture'],geometric_reference_time=geo,time_delay=old[r]['time_delay'],join_before_segment8=True))
 T=json.loads(TFILE.read_text());assert T['segments'][7]['count']==[1,7] and T['segments'][7]['word']==W;p=A.point(0,0);h=0;elapsed=c(0);checks=0;middle=None
 for i,s in enumerate(T['segments']):
  word=s['word'];assert word and set(word)<={'R','L'}
  qs,_,end,eh=plan(word,(0,0),h)
  count=A.add(A.scale(N,s['count'][0]),c(s['count'][1])) if s['type']=='periods' else None
  if count is not None:assert A.nonneg(A.sub(count,A.ONE)) and eh==h
  if i>=8:
   for q in set(qs):
    bp=A.translate_local(q,p,0)
    for points in scarpoints.values():
     for target in points:
      if count is None:assert A.no_point_collision(bp,target)
      else:assert not A.ray_membership(target,bp,end,count)
      checks+=1
  if count is None:p=A.translate_local(end,p,0);elapsed=A.add(elapsed,c(len(word)))
  else:p=A.padd(p,(A.scale(count,end[0]),A.scale(count,end[1])));elapsed=A.add(elapsed,A.scale(count,len(word)))
  h=eh
  if i==8:middle=(p,h,T['segments'][9]['word'])
 assert elapsed==A.add(A.scale(N,728),c(200304)) and p==(sn(-2,-58),sn(2,98)) and h==0
 for label,start,heading,word in [('middle_SE',*middle),('final_NW',p,h,T['infinite_tail_word'])]:
  qs,_,end,eh=plan(word,(0,0),heading);assert eh==heading and end==((2,-2) if label=='middle_SE' else (-2,2))
  for q in set(qs):
   bp=A.translate_local(q,start,0)
   for points in scarpoints.values():
    for target in points:
     k=A.line_coordinate(A.psub(target,bp),end);assert k is None or A.negative(k);checks+=1
 result=dict(status='four global field rejoins and permanent scar invisibility',domain='m>=100,n>=m+100',full_five_cell_capture='728n+200304+delta_r',full_five_cell_pose=[['-2n-58','2n+98'],0],scar_read_nonincidences=checks,rows=rows,template_sha256=hashlib.sha256(TFILE.read_bytes()).hexdigest())
 (HERE/'localized_scars_certificate.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()

"""All-parameter invisibility of four localized scars to the old rectangle chain."""
import json,sys,hashlib
from pathlib import Path
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'scattering/fixed_core_rectangle'))
from bivariate import A
M=(1,0,100);N=(1,1,200)
OLD=ROOT/'continuation_2026-10-22/ant_continuation2/planar_structure/exceptional_rectangle_template.json'

def c(v):return (0,0,v)
def scalar(a,b):return A.add(A.scale(N,a),c(b))
def norm(q,typ):return A.add(q[0],q[1]) if typ=='z' else A.sub(q[0],q[1])

def main():
 T=json.loads(OLD.read_text());S=json.loads((HERE/'localized_scars.json').read_text())['rows'];O={r['phase']:r for r in json.loads((HERE/'ordinary_interfaces.json').read_text())['rows']}
 assert [r['phase'] for r in S]==[13,14,27,89]
 for k in A.STATS:A.STATS[k]=0
 inputs={'a':(scalar(-2,-33),scalar(2,41)),'c':(scalar(2,8),scalar(-2,-14)),'d':(scalar(2,8),scalar(2,41))}
 scars={r['phase']:[(A.add(A.scale(M,-2),c(x)),A.add(A.scale(M,2),c(y))) for x,y in r['scar_base']] for r in S}
 # The finite core recovery ends before the reference a-hit and cannot read
 # any remote marker. Bounds come from the separately replayed source rows.
 for row in S:
  r=row['phase'];o=O[r]
  assert row['source_age']==o['source_age'] and row['outgoing_phase']==o['tail_phase']
  assert row['join_pose_base']==o['capture_pose_constant']
  assert row['source_recovery']==o['capture_time_coefficients_n_m_constant'][2]-70738-r
  assert row['time_delay']==r+row['source_recovery']-104*row['geometric_period_shift']-row['outgoing_phase']
  assert row['time_delay']=={13:20,14:120,27:132,89:32}[r]
  assert row['scar_translation_per_m']==[-2,2]
  lower=A.add(A.scale(M,-4),c(o['finite_prefix_u_bounds']['lower'][1]));upper=c(o['finite_prefix_u_bounds']['upper']);zu=c(o['finite_prefix_z_upper'])
  assert A.negative(A.sub(norm(inputs['a'],'u'),lower))
  assert A.negative(A.sub(upper,norm(inputs['c'],'u')))
  assert A.negative(A.sub(zu,norm(inputs['d'],'z')))
  # At W0 time208n+70738, a is phase72 of epoch n+5.
  distance=A.add(A.scale(A.sub(N,M),104),c(592-104*row['geometric_period_shift']-row['outgoing_phase']))
  assert A.nonneg(A.sub(distance,A.ONE))
  assert max(row['u_range_base'])-4*100<98 and max(row['z_range'])<71
  assert o['finite_prefix_u_bounds']['upper']<=98 and o['finite_prefix_z_upper']<=71
  assert row['changed_read_z_absmax']<=82
 base=A.point(0,0);h=0;records=[];checks=0;middle=None;elapsed=c(0)
 for i,s in enumerate(T['segments']):
  word=s['word'];assert word and set(word)<={'R','L'}
  qs,_,end,eh=A.plan(word,(0,0),h)
  count=A.add(A.scale(N,s['count'][0]),c(s['count'][1])) if s['type']=='periods' else None
  if count is not None:assert A.nonneg(A.sub(count,A.ONE)) and eh==h
  if i>=6:
   for r,points in scars.items():
    for q in qs:
     p=A.translate_local(q,base,0)
     for target in points:
      if count is None:assert A.no_point_collision(p,target)
      else:assert not A.ray_membership(target,p,end,count)
      checks+=1
  if count is None:base=A.translate_local(end,base,0)
  else:base=A.padd(base,(A.scale(count,end[0]),A.scale(count,end[1])))
  h=eh;elapsed=A.add(elapsed,c(len(word)) if count is None else A.scale(count,len(word)));records.append(dict(segment=i,pose=[base,h],time=elapsed))
  if i==8:middle=(base,h,T['segments'][9]['word'])
 # Both the two-remote intermediate parent and the full rectangle must be
 # protected forever, not just for the finite corridor displayed in T.
 assert middle is not None
 assert elapsed==A.add(A.scale(N,728),c(200304))
 assert base==(scalar(-2,-58),scalar(2,98)) and h==0
 for label,p,heading,word in [('middle_SE',*middle),('final_NW',base,h,T['infinite_tail_word'])]:
  qs,_,end,eh=A.plan(word,(0,0),heading);assert eh==heading
  assert end==((2,-2) if label=='middle_SE' else (-2,2))
  for r,points in scars.items():
   for q in qs:
    bp=A.translate_local(q,p,0)
    for target in points:
     k=A.line_coordinate(A.psub(target,bp),end);assert k is None or A.negative(k);checks+=1
 out=dict(status='all four localized scars are invisible to both complete old-parent futures',domain='m>=100,n>=m+100',variables='u=m-100>=0,v=n-m-100>=0',read_scar_checks=checks,statistics=A.STATS.copy(),source_template_sha256=hashlib.sha256(OLD.read_bytes()).hexdigest(),scar_sha256=hashlib.sha256((HERE/'localized_scars.json').read_bytes()).hexdigest(),phases=[r['phase'] for r in S],time_delays={str(r['phase']):r['time_delay'] for r in S},full_five_cell_capture_time_base=[728,200304],records=records)
 (HERE/'scar_transparency.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

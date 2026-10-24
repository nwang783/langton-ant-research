"""All21 ordinary clean-front channels with complete old-history interfaces."""
import sys,json,hashlib
from pathlib import Path
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'))
from ant_exact import W,P,D,step,plan,canonical_source,certify_period,avoids_old_tail
SOURCE=ROOT/'continuation_2026-10-22/ant_continuation/one_bit_certificate_restored.json'
BASE=(40,-52);M0=100
u=lambda p:p[0]-p[1];z=lambda p:sum(p)
def rotate(p,j):
 for _ in range(j%4):p=p[1],-p[0]
 return p

def main():
 I=json.loads((HERE/'clean_interface.json').read_text());assert I['stationary_archive_upper']=={'u':97,'z':71} and I['complete_model_discrepancy_global_u_upper']==97
 assert I['source_halfplane_u_lower']==-200 and I['fresh_phases'][-2:]==[75,89]
 S=json.loads(SOURCE.read_text());incoming,_,_,_=plan(W,(0,0),2);rows=[]
 for r in I['fresh_phases']:
  if r==72:continue
  age=S['thresholds'][r];assert age<M0
  R=next(x for x in S['cases'] if x['n']==age and x['r']==r)
  B,p,h=canonical_source(age,r);assert p==incoming[r] and p not in B;B.add(p);reads=[];word=[]
  for _ in range(R['steps']):reads.append(p);p,h,ch=step(B,p,h);word.append(ch)
  assert list(p)==R['position'] and h==R['heading'] and hashlib.sha256(repr(sorted(B)).encode()).hexdigest()==R['field_sha256']
  tw=W[R['phase']:]+W[:R['phase']];cert=certify_period(B,p,h,tw);assert cert and list(cert['drift'])==R['tail']['drift']
  assert avoids_old_tail(set(reads),p,h,tw,age)
  tailreads,_,end,eh=plan(tw,p,h);drift=(end[0]-p[0],end[1]-p[1]);assert eh==h and u(drift)>=0
  # The infinite older canonical deposits are proved invisible by the helper;
  # all actual reads also stay in the globally correct clean half-plane.
  post_min=min(map(u,reads+tailreads));assert post_min>=-200 and 92+4*M0+post_min>97
  CB,cp,ch=canonical_source(0,R['phase']);turns=(h-ch)%4;cp=rotate(cp,turns);shift=(p[0]-cp[0],p[1]-cp[1]);clean={(rotate(q,turns)[0]+shift[0],rotate(q,turns)[1]+shift[1]) for q in CB};assert certify_period(clean,p,h,tw)
  # Retain the whole stationary E_n and all extra old canonical deposits.
  # H_m,n = E_n XOR translate_O(B_age XOR C_out) XOR older deposits.
  archive_u_const=max(97-4*M0,92+max(map(u,B|clean)),92+max(map(u,D))-4*(age+1))
  archive_z_upper=max(71,-12+max(map(z,B|clean)),-12+max(map(z,D)))
  prefix_u_const=max(98,92+max(map(u,reads)),92+max(map(u,incoming)))
  prefix_z_upper=max(71,-12+max(map(z,reads)),-12+max(map(z,incoming)))
  ex=plan(tw[:(72-R['phase'])%104],p,h)[2];E=(BASE[0]+ex[0],BASE[1]+ex[1]);parity=[v%2 for v in E]
  if drift==(-2,-2):classification='SW: all remaining remote corners missed'
  elif drift==(2,-2) and parity!=[0,0]:classification='SE: exceptional c parity excluded'
  elif drift==(2,2) and parity!=[0,1]:classification='NE: exceptional d parity excluded'
  elif drift==(2,-2):classification='remaining SE exceptional c branch'
  elif drift==(2,2):classification='remaining NE exceptional d branch'
  else:raise AssertionError(drift)
  bounds={}
  if u(drift)==0:bounds['u']=[4,92+min(map(u,tailreads)),92+max(map(u,tailreads))]
  if z(drift)==0:bounds['z']=[-12+min(map(z,tailreads)),-12+max(map(z,tailreads))]
  rows.append(dict(phase=r,core_ray_base=[BASE[0]+incoming[r][0],BASE[1]+incoming[r][1]],source_age=age,source_record_field_sha256=R['field_sha256'],capture_time_n_m_constant=[416,104,146044+r+R['steps']],capture_pose_constant=[[BASE[0]+p[0],BASE[1]+p[1]],h],translation_per_m=[2,-2],tail_phase=R['phase'],outgoing_drift=drift,post_core_u_lower_m=[4,92+post_min],full_prefix_u_upper_m=[4,prefix_u_const],full_prefix_z_upper=prefix_z_upper,archive_u_upper_m=[4,archive_u_const],archive_z_upper=archive_z_upper,tail_fixed_normals=bounds,exceptional_ray_base=E,exceptional_translation_per_m=[2,-2],classification=classification))
 easy=[x['phase'] for x in rows if not x['classification'].startswith('remaining')]
 assert easy==[15,28,29,32,38,45,55,56,60,61,62,71]
 assert [x['phase'] for x in rows if x['classification']=='remaining NE exceptional d branch']==[46,47,57]
 out=dict(status='all21 ordinary complete-history clean-front transfers with archive interfaces',domain='m>=100,n-m>=100',proposed_easy_mass5_phases=easy,rows=rows,source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),interface_sha256=hashlib.sha256((HERE/'clean_interface.json').read_bytes()).hexdigest(),scope='Full three-cell q+a+core parents certified. Recurrence exclusions additionally need sector and incidence-shape coupling; phase72 remains open here.')
 (HERE/'ordinary_interfaces.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

"""Complete stationary-archive bounds and exact corner-sector obstructions."""
import json,gzip,hashlib,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1];SRC=ROOT/'scattering/far_se_core/last_frontier';OLD=ROOT/'scattering/far_sw_core'
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'))
from ant_exact import W,P,D,plan,multiple
PH=[13,14,15,27,28,29,32,38,45,46,47,55,56,57,60,61,62,70,71,72,75,89];FAVORABLE=[14,28,32,38,46,56,60,62,70,72]
def rot(q,r):
 for _ in range(r%4):q=(q[1],-q[0])
 return q
def plus(p,q):return tuple(a+b for a,b in zip(p,q))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 model=json.loads((SRC/'parallel_model_certificate.json').read_text());trans=json.loads((OLD/'return_transfers.json').read_text());bridge=json.loads((HERE/'bridge.json').read_text());caps=json.loads((HERE/'fixed_caps.json').read_text());assert trans['model_certificate_sha256']==bridge['model_certificate_sha256']==sha(SRC/'parallel_model_certificate.json') and bridge['fixed_caps_sha256']==sha(HERE/'fixed_caps.json')
 TFILE=ROOT/'continuation_2026-10-22/ant_continuation2/planar_structure/exceptional_rectangle_template.json';assert sha(TFILE)=='16246ec40cbdd4ad94c35698992582b27a942dc7d539683f1b3684892cd5687d';T=json.loads(TFILE.read_text());qreads=plan(T['segments'][2]['word'],(-31,-6),3)[0];assert (min(x-y for x,y in qreads),max(x-y for x,y in qreads))==(-82,56)
 assert max(map(sum,qreads))-800<=35
 assert (min(map(sum,plan(T['segments'][0]['word'],(0,0),0)[0])),max(map(sum,plan(T['segments'][0]['word'],(0,0),0)[0])))==(-21,35)
 assert max(map(sum,plan(W,(-15,10),3)[0]))==-5
 assert max(map(sum,plan(W,(6,-43),1)[0]))-400<=35
 rows=[]
 for mr in model['records']:
  r=mr['phase']
  if r in (13,14,27,89):continue
  word=gzip.open(SRC/f'word_r{r}_mature1.txt.gz','rt').read();assert hashlib.sha256(word.encode()).hexdigest()==mr['word_sha256'];qs,_,mp,mh=plan(word,(0,0),0);assert [list(mp),mh]==mr['local_pose'];local=[plus((6,-43),rot(q,1)) for q in qs];us=[-82,56]+[x-y for x,y in local];zs=[35]+[sum(q)-400 for q in local]
  if r in [28,60,61,70,75]:
   br=next(t for t in bridge['rows'] if t['phase']==r);cap=next(t for t in caps['rows'] if t['phase']==r)
   # Include the local partial phase and the whole NE flight, not merely
   # the fixed cap word, in every claimed archive bound.
   extra,_,_,_=plan((W[mr['word_phase']:]+W[:mr['word_phase']])[:(-mr['word_phase'])%104],mp,mh)
   physical=[plus((6,-43),rot(q,1)) for q in extra];us += [x-y for x,y in physical];zs += [sum(q)-400 for q in physical]
   cp,ch=cap['start'];flight=plan(W,tuple(cp),ch)[0];us += [x-y for x,y in flight];zs += [max(map(sum,flight))-4]
   word=gzip.open(HERE/f'word_r{r}.txt.gz','rt').read();assert len(word)==cap['capture'] and hashlib.sha256(word.encode()).hexdigest()==cap['word_sha256'];rs,_,p,h=plan(word,tuple(cp),ch);assert [list(p),h]==cap['pose'];us += [x-y for x,y in rs];zs += list(map(sum,rs));phase=cap['tail_phase'];target=(0,1);translation='fixed actual pose'
  else:
   tr=next(t for t in trans['rows'] if t['phase']==r);p=plus((6,-43),rot(mp,1));h=(mh+1)%4;phase=mr['word_phase'];assert [list(p),h]==tr['pose_constant'];target=tuple(tr['exceptional_target_parity']);translation='(-2m,-2m)'
  skip=(-phase)%104;extra,_,p,h=plan((W[phase:]+W[:phase])[:skip],p,h);us += [x-y for x,y in extra];zs += [sum(q)-(400 if translation!='fixed actual pose' else 0) for q in extra]
  tail,_,end,eh=plan(W,p,h);d=tuple(a-b for a,b in zip(end,p));assert eh==h
  assert [j for j,q in enumerate(tail) if not any((k:=multiple((v[0]-q[0],v[1]-q[1]),d)) is not None and (k>0 or (k==0 and i<j)) for i,v in enumerate(tail))]==PH
  assert [r for r in PH if sum(tail[r])%2==sum(target)%2]==FAVORABLE
  raypar=tuple(v%2 for v in tail[72]);core=[plus(p,rot(q,h-2)) for q in P];archive_u=[min(us+[x-y for x,y in core]),max(us+[x-y for x,y in core])];archive_z=max(zs+[sum(q)-(400 if translation!='fixed actual pose' else 0) for q in core]);mismatch=raypar!=target
  rows.append(dict(phase=r,drift=d,phase_zero_pose_constant=[p,h],pose_translation=translation,complete_finite_prefix_u_bounds=[min(us),max(us)],complete_archive_u_bounds=archive_u,complete_archive_z_upper=archive_z,tail_u_base_bounds=[min(x-y for x,y in tail),max(x-y for x,y in tail)],tail_z_base_bounds=[min(map(sum,tail)),max(map(sum,tail))],remaining_corner_parity=target,exceptional_ray_parity=raypar,exceptional_mismatch=mismatch))
 excluded=[r['phase'] for r in rows if r['exceptional_mismatch']];assert excluded==[28,32,38,46,47,55,57,60,61,71]
 out=dict(status='ten exact favorable-sector parity exclusions plus four inherited scar exclusions',domain='m>=100,n-m>=100; recurrence takes m fixed then divergent remote ages and exposed gaps',rows=rows,parity_excluded_phases=excluded,scar_excluded_phases=[13,14,27,89],total_recurrence_excluded_phases=sorted(excluded+[13,14,27,89]),remaining_phases=[15,29,45,56,62,70,72,75],bridge_sha256=sha(HERE/'bridge.json'),old_transfer_sha256=sha(OLD/'return_transfers.json'),old_scar_sha256=sha(OLD/'return_scars.json'),scope='No exclusion yet for a matching exceptional corner in the eight remaining classes.')
 (HERE/'mass5_interfaces.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

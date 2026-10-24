"""Four global rejoins on the NE return, protected by a fixed z gap."""
import json,gzip,hashlib,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1];SOURCE=ROOT/'scattering/far_se_core/last_frontier'
sys.path.insert(0,str(ROOT/'scattering/fixed_core_rectangle'))
from bivariate import A
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'))
from ant_exact import W,plan,multiple,canonical_source
M=(1,0,100);N=(1,1,200);C=lambda v:(0,0,v);NW=(-2,2)
TFILE=ROOT/'continuation_2026-10-22/ant_continuation2/planar_structure/exceptional_rectangle_template.json'
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def odd(word):
 qs,_,p,h=plan(word,(0,0),0);s=set()
 for q in qs:s.symmetric_difference_update({q})
 return s,p,h,qs

def main():
 I=json.loads((HERE/'return_interface.json').read_text());P=json.loads((SOURCE/'parallel_model_certificate.json').read_text());assert I['old_SE_rail_offset']==[3,-77]
 old={r['phase']:r for r in json.loads((SOURCE/'localized_scars_certificate.json').read_text())['rows']};model={r['phase']:r for r in P['records']};fresh,_,_,_=plan(W,(0,0),0);rows=[];zmax=-10**9
 for r in (13,14,27,89):
  row=model[r];word=gzip.open(SOURCE/f'word_r{r}_mature1.txt.gz','rt').read();assert hashlib.sha256(word.encode()).hexdigest()==row['word_sha256']
  flips,p,heading,reads=odd(word);assert [list(p),heading]==row['local_pose'];phase=row['word_phase'];_,rp,rh=canonical_source(0,phase);rp=(-rp[0],-rp[1]);rh=(rh+2)%4
  k=multiple((p[0]-rp[0],p[1]-rp[1]),NW);assert k is not None and heading==rh
  geo=104*k+phase;other,end,eh,refreads=odd(W*k+W[:phase]);assert (end,eh)==(p,heading)
  assert all(-200<=x-y<=200 for x,y in reads+refreads)
  S={fresh[r]}^flips^other;assert {(37+x,25+y) for x,y in S}=={tuple(q) for q in old[r]['scar_base']}
  delay=len(word)-geo;assert delay=={13:20,14:120,27:132,89:32}[r]
  assert A.negative(A.sub(C(geo),A.scale(A.add(M,C(7)),104)))
  lo=49+row['source_z_bounds'][0];hi=49+row['source_z_bounds'][1]
  assert A.negative(A.sub(A.add(A.scale(N,-4),C(-74)),C(lo)))
  assert A.negative(A.sub(C(hi),A.add(A.scale(N,4),C(22))))
  local_z_upper=A.add(A.scale(M,-4),C(-37-row['source_u_bounds'][0]));assert A.negative(A.sub(local_z_upper,A.add(A.scale(N,4),C(49))))
  qs,_,d,eh=plan(W[phase:]+W[:phase],(0,0),heading);assert d==NW and eh==heading
  for target in S:
   for q in qs:
    j=multiple((target[0]-p[0]-q[0],target[1]-p[1]-q[1]),NW);assert j is None or j<0
  physical=sorted((6+y,-43-x) for x,y in S);upper=max(x+y for x,y in physical)-400;zmax=max(zmax,upper)
  rows.append(dict(phase=r,scar_base=physical,scar_translation_per_m=[-2,-2],scar_size=len(S),time_delay=delay,reference_join_time=geo))
 T=json.loads(TFILE.read_text());assert I['source_template_sha256']==h(TFILE);p=A.point(0,0);heading=0;minimum=10**9
 for i,s in enumerate(T['segments']):
  assert s['type'] in ('finite','periods') and s['word'] and set(s['word'])<={'R','L'};qs,_,d,eh=plan(s['word'],(0,0),heading)
  count=None if s['type']=='finite' else A.add(A.scale(N,s['count'][0]),C(s['count'][1]))
  if i>=4:
   if count is not None:assert sum(d)==0
   for x,y in qs:
    z=A.add(A.add(p[0],p[1]),C(x+y));assert z[:2]==(0,0);minimum=min(minimum,z[2])
  if count is None:p=A.translate_local(d,p,0)
  else:p=A.padd(p,(A.scale(count,d[0]),A.scale(count,d[1])))
  heading=eh
 qs,_,d,eh=plan(T['infinite_tail_word'],(0,0),heading);assert sum(d)==0 and eh==heading
 for x,y in qs:
  z=A.add(A.add(p[0],p[1]),C(x+y));assert z[:2]==(0,0);minimum=min(minimum,z[2])
 assert minimum==-93 and zmax<minimum
 out=dict(status='four exact global rejoins; scars invisible to q, q+a, and full rectangle futures',domain='m>=100,n-m>=100',rows=rows,scar_z_upper_at_m100=zmax,all_reference_reads_after_segment3_z_lower=minimum,full_five_cell_capture='728n+200304+delta_r',interface_sha256=h(HERE/'return_interface.json'),model_certificate_sha256=h(SOURCE/'parallel_model_certificate.json'),source_template_sha256=h(TFILE))
 (HERE/'return_scars.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

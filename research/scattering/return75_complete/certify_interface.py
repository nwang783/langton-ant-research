"""Complete-history transfer, support geometry, and forced final rectangle."""
import sys,json,gzip,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1];CAP=HERE.parent/'blank_return_cap';ORD=HERE.parent/'ordinary_reverse_interface'
sys.path.insert(0,str(HERE.parent/'fixed_core_rectangle'));from bivariate import A
from ant_exact import W,P,D,plan,step,canonical_source
sys.path.insert(0,str(CAP));from discover import initial
C=lambda v:(0,0,v);N=(1,0,200);lin=lambda a,b:A.add(A.scale(N,a),C(b))
def main():
 mp=CAP/'manifest.json';assert hashlib.sha256(mp.read_bytes()).hexdigest()=='2827291464278a15841e21a0430de38d18f990f01827f7adb0d43cfb5dbe9237';mf=json.loads(mp.read_text())['files']
 for fn in ['bridge.json','fixed_caps.json','word_r75.txt.gz','discover.py']:assert hashlib.sha256((CAP/fn).read_bytes()).hexdigest()==mf[fn]
 bridge=next(r for r in json.loads((CAP/'bridge.json').read_text())['rows'] if r['phase']==75);assert bridge['capture_time_m_k_constant']==[208,208,82515] and bridge['final_pose']==[[46,-37],1] and bridge['final_phase']==55
 old=json.loads((ORD/'certificate_r75.json').read_text());assert hashlib.sha256((ORD/'certificate_r75.json').read_bytes()).hexdigest()==bridge['packet_certificate_sha256'];tp=ORD/'template_r75.json';assert hashlib.sha256(tp.read_bytes()).hexdigest()==old['template_sha256'];T=json.loads(tp.read_text());base=A.point(0,0);h=2;old_z=[];old_u=[]
 for s in T['segments']:
  w=s['word'];assert w and set(w)<={'R','L'} and s['type'] in ['finite','periods'];qs,_,d,eh=plan(w,(0,0),h);count=C(1) if s['type']=='finite' else A.add(A.scale((1,0,100),s['count'][0]),C(s['count'][1]))
  if s['type']=='periods':assert len(w)==104 and eh==h
  for q in qs:
   p=A.padd(base,A.point(*q))
   for p in [p,tuple(A.add(v,A.scale(A.sub(count,C(1)),e)) for v,e in zip(p,d))]:
    z=A.add(*p);u=A.sub(*p);assert z[:2]==(0,0);old_z.append(z[2]);assert A.nonneg(A.add(u,C(18)));old_u.append(u)
  base=tuple(A.add(v,A.scale(count,e)) for v,e in zip(base,d));h=eh
 assert base==(A.add(A.scale((1,0,100),2),C(51)),A.add(A.scale((1,0,100),-2),C(19))) and h==0
 blank=set();p=(0,0);h=0;br=[]
 for _ in range(9977):br.append(p);p,h,ch=step(blank,p,h)
 assert p==(-15,10) and h==3
 F,p,h=initial(75);cap_start=p;word=gzip.open(CAP/'word_r75.txt.gz','rt').read();cap_reads=[]
 for c in word:cap_reads.append(p);p,h,ch=F.step(p,h);assert c==ch
 assert (p,h)==((46,-37),1)
 incoming=plan(W,cap_start,1)[0];blank_leg=plan(W,(-15,10),3)[0]
 # All actual baseline black cells are initial bits or previously read cells.
 # Neither the mature SW flight nor the returned NE flight changes u.
 q1=plan(W,(0,0),2)[0][75];input_u=[-25+sum(q1),-23]
 actual_u_lower=min([min(x-y for x,y in br),min(x-y for x,y in blank_leg),min(old_z)-25,min(x-y for x,y in incoming),min(x-y for x,y in cap_reads)]+input_u)
 actual_u_upper=max([max(x-y for x,y in br),max(x-y for x,y in blank_leg),max(old_z)-25,max(x-y for x,y in incoming),max(x-y for x,y in cap_reads)]+input_u)
 actual_prefix_z_upper=max(max(map(sum,br)),max(map(sum,blank_leg)),13-4*100,max(map(sum,incoming))-4,max(map(sum,cap_reads)))
 model_u=[x-y for x,y in F.changes]+[b[0]-b[1] for b,d,lo,hi in F.rays];difference_u_lower=min(actual_u_lower,min(model_u));assert difference_u_lower>=-250
 assert [actual_u_lower,actual_u_upper]==[-86,82] and [min(model_u),max(model_u)]==[-38,81] and actual_prefix_z_upper==51 and [min(old_z),max(old_z)]==[-61,77]
 CB,cp,ch=canonical_source(0,55);assert ch==1
 outgoing_core_u=[46+(x-cp[0])-(-37+y-cp[1]) for x,y in CB];assert max(outgoing_core_u)<250
 qC=(lin(2,24),lin(-2,-12));qA=(lin(-2,-35),lin(2,109));qD=(lin(2,24),lin(2,109))
 assert A.nonneg(A.sub(A.sub(*qC),C(actual_u_upper+1))) and A.nonneg(A.sub(C(actual_u_lower-1),A.sub(*qA))) and A.nonneg(A.sub(A.add(*qD),C(actual_prefix_z_upper+1)))
 parent=json.loads((HERE/'parent_certificate.json').read_text());cycle=json.loads((HERE/'cycle_certificate.json').read_text())
 assert parent['capture_time']==list(lin(104,49815)) and parent['capture_pose']==[[list(lin(2,53)),list(lin(-2,27))],0] and parent['tail_phase']==0
 assert cycle['capture_time']==list(lin(520,133554)) and cycle['capture_pose']==[[list(lin(-2,-67)),list(lin(2,72))],3] and cycle['tail_phase']==0 and cycle['D_never_read']
 assert cycle['prefix_z_lower']==parent['prefix_z_lower']==-51 and cycle['prefix_z_upper']==137
 assert all(A.nonneg(A.sub(C(difference_u_lower-1),tuple(u))) for u in cycle['tail_u_values'])
 # Every parent finite-prefix write has u>=75,z<=87; this also bounds its
 # stationary archive, independently of the subsequent NW flight length.
 tp=HERE/'template_parent.json';assert hashlib.sha256(tp.read_bytes()).hexdigest()==parent['template_sha256'];T=json.loads(tp.read_text());base=A.point(46,-37);h=1
 for s in T['segments']:
  qs,_,d,eh=plan(s['word'],(0,0),h);count=C(1) if s['type']=='finite' else lin(*s['count_n'])
  for q in qs:
   p=A.padd(base,A.point(*q))
   for q in [p,tuple(A.add(v,A.scale(A.sub(count,C(1)),e)) for v,e in zip(p,d))]:assert A.nonneg(A.sub(A.sub(*q),C(75))) and A.nonneg(A.sub(C(87),A.add(*q)))
  base=tuple(A.add(v,A.scale(count,e)) for v,e in zip(base,d));h=eh
 assert base==(lin(2,53),lin(-2,27)) and h==0
 q72=A.padd(base,A.point(*plan(W[:72],(0,0),h)[2]));epoch=lin(2,40);assert tuple(A.add(v,A.scale(epoch,d)) for v,d in zip(q72,(-2,2)))==qA
 # Include the exact outgoing phase0 canonical core in the old archive bound.
 core_us=[]
 for x,y in P:
  p=A.padd(base,A.point(-x,-y));u=A.sub(*p);assert A.nonneg(A.sub(u,C(difference_u_lower)));core_us.append(u)
 out=dict(status='exact complete two-age phase75 parent/cycle transfer and recurrence interface',domain='m,k>=100 independently; N=m+k>=200',baseline_actual_u_bounds=[actual_u_lower,actual_u_upper],baseline_model_u_bounds=[min(model_u),max(model_u)],baseline_actual_prefix_z_upper=actual_prefix_z_upper,complete_discrepancy_u_lower=difference_u_lower,parent_prefix_bounds={'u_lower':75,'z_upper':87},parent_capture_time_N_constant=[312,132330],cycle_capture_time_N_constant=[728,216069],cycle_capture_pose=[['-2N-67','2N+72'],3],cycle_tail_phase=0,first_C_time_N_constant=[312,81284],first_A_time_N_constant=[520,136562],forced_A=[['-2N-35','2N+109']],D_never_read=True,source_old_prefix_z_bounds=[min(old_z),max(old_z)],parent_certificate_sha256=hashlib.sha256((HERE/'parent_certificate.json').read_bytes()).hexdigest(),cycle_certificate_sha256=hashlib.sha256((HERE/'cycle_certificate.json').read_bytes()).hexdigest(),scope='The initial z>=-250 interface protects the whole finite prefix. The separate u lower support bound protects the final SW tail after it leaves that half-plane.')
 (HERE/'interface.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

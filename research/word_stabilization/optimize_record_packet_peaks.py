from pathlib import Path
import json,sys,time,hashlib
import numpy as np
R=Path(__file__).resolve().parents[1];D=R/'core_periodicity_new/chronology_dcuv';src=Path(sys.argv[1]);out=Path(sys.argv[2]);J=json.loads(src.read_text());v=J['values'];G=json.loads((D/'literal_residual_geometry.json').read_text())['geometry'];K=J['kept_packet_types'];ki={a:i for i,a in enumerate(K)};A=np.array(J['record_head_offsets']['A'],dtype=np.int32);direction=v['ax'],v['ay'];inventory=json.loads((D/'transfer_inventory.json').read_text())['protected_survivors']
def rot(z,h):x,y=z;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def L(z):return direction[0]*z[0]+direction[1]*z[1]
lo=np.array([2*L(rot(G[a]['endpoint'][:2],h))+A[(h+G[a]['endpoint'][2])%4]for a in K for h in range(4)],dtype=np.int32);T=lo.copy();data=[]
for r in inventory:
 a,b,x,y,rh,*q=r['tuple']
 if a not in ki or b not in ki:continue
 for ph in range(4):
  bh=(ph+rh)%4;data.append((ki[a]*4+ph,ki[b]*4+bh,ph,bh,2*L(rot((x,y),ph))))
si,ti,sh,th,delta=np.asarray(data,dtype=np.int32).T
# Count only rows touching coordinate z when optimizing it.
def count(t):return int(np.count_nonzero((t[ti]>A[th])&(delta+t[ti]>A[sh])&(delta+t[ti]>t[si])))
history=[];start=time.time()
for round in range(10):
 before=count(T)
 for z in range(len(T)):
  mask=(si==z)|(ti==z);ss,tt,hh,bb,dd=si[mask],ti[mask],sh[mask],th[mask],delta[mask];best=None;bv=None
  for val in range(int(lo[z]),int(lo[z])+101):
   T[z]=val;n=int(np.count_nonzero((T[tt]>A[bb])&(dd+T[tt]>A[hh])&(dd+T[tt]>T[ss])))
   if best is None or n<best:best=n;bv=val
  T[z]=bv
 after=count(T);history.append({'round':round,'before':before,'after':after,'T':T.tolist()});print(history[-1],flush=True)
 if after>=before:break
for ia,a in enumerate(K):
 for h in range(4):
  peak=int(T[ia*4+h])
  for i,q in enumerate(G[a]['outputs']):v[f'w_{a}_{i}_{h}']=peak-2*L(rot(q,h))
  for i,q in enumerate(G[a]['inputs']):v[f'u_{a}_{i}_{h}']=peak-2*L(rot(q,h))
J['status']='RECORD-ONLY bounded coordinate discovery, no event exclusions';J['record_peak_optimization']={'source':str(src),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'core_offsets':A.tolist(),'peak_lower_bounds':lo.tolist(),'peak_upper_slack':100,'history':history,'remaining_count':count(T),'seconds':time.time()-start,'not_claimed':'No global numerical optimum; no individual transfer inequalities; no no-hit theorem.'};out.write_text(json.dumps(J,indent=2)+'\n')

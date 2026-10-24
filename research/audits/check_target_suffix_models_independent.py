"""Conditional exact reconstruction of reverse suffix flags and prophecy products."""
from pathlib import Path
from itertools import product
from collections import defaultdict
import json,sys,subprocess
from check_producer_quotient_model_independent import ROOT,W,OUT,digest,relation,geometry,signed,ordinary,protected,check as producer_check
from check_protected_patch_model_independent import main as base_check,rotation,xy

def resolve(name,parent):
 p=Path(name);return p if p.is_absolute()else(parent/p).resolve()
def cells(B):
 p=complex(*B['target_pose'][:2]);h=B['target_pose'][2];q=complex(*B['protected_q'])
 return [p+rotation(z,h)for z in sorted(geometry[B['target']]['inputs'],key=xy)if p+rotation(z,h)!=q]
def dat_check(path,J):
 lines=[f"{J['n']} {J['out']+1} {len(J['transitions'])} {len(J['reentry'])}",' '.join(map(str,J['start']))]+[' '.join(map(str,r))for r in J['transitions']]+[' '.join(map(str,J['reentry']))]
 assert path.with_suffix('.dat').read_text()=='\n'.join(lines)+'\n'
def finish(path,J,kind,inputs):
 result={'status':'PASS conditional '+kind+' semantics; hypothesis closure NOT asserted','model':str(path.relative_to(ROOT)),'variables':J['n'],'transitions':len(J['transitions']),'sha256':{str(p.relative_to(ROOT)):digest(p)for p in [path,path.with_suffix('.dat'),*inputs]}}
 if path.with_suffix('.bdd').exists():
  dest=OUT/(path.stem+'.invariant.json');checker='check_guarded_clear_bdd64_invariant_independent'if kind=='reverse-target'else'check_guarded_reset_bdd64_invariant_independent'
  subprocess.run([str(ROOT/'audits'/checker),str(path.with_suffix('.dat')),str(path.with_suffix('.bdd')),str(dest)],check=True)
  result['invariant']=json.loads(dest.read_text());result['sha256'][str(path.with_suffix('.bdd').relative_to(ROOT))]=digest(path.with_suffix('.bdd'))
 (OUT/(path.stem+'.model_check.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result));return result
def reverse(path):
 J=json.loads(path.read_text());bp=resolve(J['base_model_file'],path.parent);B=json.loads(bp.read_text());base_check(bp)
 hp=resolve(J['candidate_hypothesis_file'],path.parent);ep=resolve(J['extra_guard_file'],path.parent);H=relation(hp);E=relation(ep);assert E<=signed;forbidden=protected|E|H
 for key,p in [('base_model',bp),('candidate_hypothesis',hp),('extra_guard',ep)]:assert J[key+'_sha256']==digest(p)
 assert H=={tuple(r)for r in J['candidate_hypotheses']};Q=cells(B);assert J['target_flag_cells']==[list(xy(q))for q in Q]
 assert all(list(xy(q))in B['points']for q in Q);n=B['n'];flags=((1<<len(Q))-1)<<n
 target=complex(*B['target_pose'][:2]);th=B['target_pose'][2];b=B['target'];expected=[];goals=[]
 for sid,to,k,v,f,g,a in B['transitions']:
  if g:goals.append((sid,k,v));continue
  x,y,h=B['poses'][sid];p=complex(x,y);mask=k;value=v^(f&k);clear=0
  for j,q in enumerate(Q):
   local=rotation(q-p,-h);row=(a,b,*xy(rotation(target-p,-h)),(th-h)%4,*xy(local));bit=1<<(n+j)
   if row in forbidden:mask|=bit
   if local in geometry[a]['context']:clear|=bit
  expected.append([to,sid,mask,value,f,clear,0,a])
 expected.extend([r,B['out'],0,0,0,0,0,99]for r in B['reentry'])
 sp,sk,sv=B['start'];expected.append([sp,sp,sk,sv,0,0,1,100]);assert len(goals)==1;gp,gk,gv=goals[0]
 assert J['transitions']==expected and J['start']==[gp,gk|flags,gv|flags] and J['n']==n+len(Q) and J['base_n']==n and J['out']==B['out']+1 and J['reentry']==[]
 for field in ['points','poses','keep','source','target','target_pose','protected_q']:assert J[field]==B[field]
 dat_check(path,J);return finish(path,J,'reverse-target',[bp,hp,ep])
def prophecy(path):
 J=json.loads(path.read_text());fp=resolve(J['forward_model_file'],path.parent);F=json.loads(fp.read_text())
 if F.get('format')in['guarded_xor_reset_producer_quotient_v1','guarded_xor_reset_v1']:producer_check(fp,False)
 elif all(len(t)==7 for t in F['transitions']):base_check(fp)
 else:raise AssertionError('Unsupported forward format; needs its own independent reconstruction')
 hp=resolve(J['prophecy_hypothesis_file'],path.parent);ep=resolve(J['prophecy_signed_file'],path.parent);H=relation(hp);E=relation(ep);assert E<=signed;forbidden=protected|E|H
 for key,p in [('forward_model',fp),('prophecy_hypothesis',hp),('prophecy_signed',ep)]:assert J[key+'_sha256']==digest(p)
 assert H=={tuple(r)for r in J['prophecy_hypotheses']}
 assert {tuple(r)for r in J['candidate_hypotheses']}==H|{tuple(r)for r in F.get('candidate_hypotheses',[])}
 Q=cells(F);n=F['n'];mask=(1<<n)-1;nb=len(Q);assert nb<=2 and J['prophecy_cells']==[list(xy(q))for q in Q] and J['prophecy_offset']==n and J['n']==n+nb
 assert all(list(xy(q))in F['points']for q in Q)
 for field in ['start','points','poses','out','reentry','keep','source','target','target_pose','protected_q']:assert J[field]==F[field]
 assert len(J['transitions'])==len(J['prophecy_branches']);groups=defaultdict(list)
 for t,m in zip(J['transitions'],J['prophecy_branches']):groups[m['forward_transition']].append((t,m))
 assert set(groups)==set(range(len(F['transitions'])))
 target=complex(*F['target_pose'][:2]);th=F['target_pose'][2];b=F['target']
 for ti,t in enumerate(F['transitions']):
  if len(t)==7:sid,to,k,v,f,g,a=t;rm=rv=0
  else:sid,to,k,v,f,rm,rv,g,a=t
  actual=set()
  for tt,m in groups[ti]:
   ss,dd,kk,vv,ff,rr,zz,gg,aa=tt;assert(ss,dd,kk&mask,vv&mask,ff,rr&mask,zz&mask,gg,aa)==(sid,to,k,v,f,rm,rv,g,a)
   assert bool(m['outer_goal'])==bool(g)
   for before in range(1<<nb):
    if before&(kk>>n)==vv>>n:
     after=(before&~(rr>>n))|(zz>>n);actual.add((before,after))
  if g:expected={((1<<nb)-1,(1<<nb)-1)}
  else:
   x,y,h=F['poses'][sid];p=complex(x,y);constraints=[]
   for q in Q:
    local=rotation(q-p,-h);row=(a,b,*xy(rotation(target-p,-h)),(th-h)%4,*xy(local));constraints.append((local in geometry[a]['context'],row[:5]in ordinary or row in forbidden))
   expected=set()
   for before,after in product(range(1<<nb),repeat=2):
    if all((not((before>>j)&1)if touch else((before>>j)&1)==((after>>j)&1))and(not forbid or not((after>>j)&1))for j,(touch,forbid)in enumerate(constraints)):expected.add((before,after))
  assert actual==expected,(ti,actual,expected)
 dat_check(path,J);return finish(path,J,'forward-prophecy-product',[fp,hp,ep])
if __name__=='__main__':
 for arg in sys.argv[1:]:
  p=Path(arg).resolve();J=json.loads(p.read_text());(reverse if J['format']=='guarded_xor_clear_reverse_target_v1'else prophecy)(p)

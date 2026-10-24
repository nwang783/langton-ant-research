#!/usr/bin/env python3
"""Explore exact changed endpoint back-reflection closure, retaining every wake."""
from pathlib import Path
from collections import defaultdict,Counter
import runpy,json,hashlib,time,argparse
ROOT=Path(__file__).parent
C=runpy.run_path(str(ROOT/'changed_endpoint_catalog.py'))
for k in ['old_orbit','initial_color','certify','parse_rows','add_threshold','toggle','advance','incoming','channels_for','solve','V','d']:
 globals()[k]=C[k]

def append_return(rows,cap,channel,result):
 base_profile_count=len(cap_profiles(rows));rows,F,p,h,tau,phi=incoming(rows,cap,channel);p,h,read=advance(rows,F,p,h,result['entry']);assert[list(p),h]==result['pose'];assert certify(rows,F,p,h,result['tail_word']);rr=parse_rows(rows);odd=set();pp=p;hh=h
 for ch in result['tail_word']:
  toggle(odd,pp);hh=(hh+(-1 if ch=='L'else 1))%4;v=V[hh];pp=(pp[0]+v[0],pp[1]+v[1])
 assert hh==h and(pp[0]-p[0],pp[1]-p[1])==(-d[0],-d[1])
 for q in odd:
  j,k=old_orbit(q);add_threshold(rr,j,k)
 profiles={j for j,r in rr.items()if len(r)%2};assert len(profiles)==base_profile_count+24
 out=set(F)
 for(t,a),r in rr.items():
  r=set(r)
  if len(r)%2:toggle(r,0)
  st=sorted(r);assert len(st)%2==0
  for lo,hi in zip(st[::2],st[1::2]):
   for k in range(lo+1,hi+1):toggle(out,(a-2*k,a-2*k-t))
 normalized={j:[0]for j in profiles};crit=defaultdict(set)
 for j,r in rr.items():crit[j].update(r)
 for q in F|out:
  j,k=old_orbit(q);crit[j].update([k-1,k,k+1])
 for j in profiles:crit[j].update([-1,0,1])
 rr={j:sorted(r)for j,r in rr.items()};checks=0
 for(t,a),ks in crit.items():
  ks.update([min(ks)-1,max(ks)+1])
  for k in ks:
   q=(a-2*k,a-2*k-t);assert initial_color(q,rr,F)==initial_color(q,normalized,out);checks+=1
 return normalized,out,checks

def cap_profiles(rows):return{j for j,r in rows.items()if len(r)%2}
def state_meta(rows,cap):
 obj={'profiles':sorted(cap_profiles(rows)),'cap':sorted(cap)};raw=json.dumps(obj,separators=(',',':')).encode();return {**obj,'state_sha256':hashlib.sha256(raw).hexdigest(),'profile_count':len(obj['profiles']),'cap_mass':len(cap),'cap_t_hull':[min(x-y for x,y in cap),max(x-y for x,y in cap)]}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--max-caps',type=int,default=12);ap.add_argument('--limit',type=int,default=300000);args=ap.parse_args();original=json.loads((ROOT/'endpoint_catalog_results.json').read_text())['results'];changed=json.loads((ROOT/'changed_endpoint_catalog_results.json').read_text());queue=[];out={'scope':'Literal complete-field endpoint return closure only. No old-side scattering or finite initial itinerary automatically supplied.','states':[],'edges':[],'resource_max_caps':args.max_caps};seen={};start=time.time()
 for c in changed['cap_results']:
  src=next(r for r in original if r['channel']==c['normalization']['source_channel']);rows,cap,meta=C['normalized_endcap'](src)
  for r in c['results']:
   if r.get('drift')!=[2,2]:continue
   nr,nc,checks=append_return(rows,cap,r['channel'],r);m=state_meta(nr,nc);edge={'from_original_source':src['channel'],'incoming_return_type':r['channel'],'to_state':m['state_sha256'],'normalization_checks':checks};out['edges'].append(edge)
   if m['state_sha256']not in seen:
    seen[m['state_sha256']]=len(out['states']);node={**m,'status':'PENDING','channel_count':None,'results':[]};out['states'].append(node);queue.append((nr,nc,node))
  print('INITIAL',src['channel'],'to',m['state_sha256'],m['profile_count'],m['cap_mass'],m['cap_t_hull'],flush=True)
 while queue and sum(s['status']!='PENDING'for s in out['states'])<args.max_caps:
  rows,cap,node=queue.pop(0);chs=channels_for(rows,cap);node['channel_count']=len(chs);node['status']='RUNNING';print('NODE',node['state_sha256'],node['profile_count'],node['cap_mass'],node['cap_t_hull'],'channels',len(chs),flush=True)
  for i,ch in enumerate(chs):
   r=solve(rows,cap,ch,args.limit);node['results'].append(r)
   if i%10==0 or r.get('drift')==[2,2]:print('RESULT',i+1,'/',len(chs),r,flush=True)
   if r.get('drift')==[2,2]:
    nr,nc,checks=append_return(rows,cap,ch,r);m=state_meta(nr,nc);out['edges'].append({'from_state':node['state_sha256'],'incoming_return_type':ch,'to_state':m['state_sha256'],'normalization_checks':checks})
    if m['state_sha256']not in seen:
     seen[m['state_sha256']]=len(out['states']);nn={**m,'status':'PENDING','channel_count':None,'results':[]};out['states'].append(nn);queue.append((nr,nc,nn))
   out['elapsed_seconds']=time.time()-start;(ROOT/'endpoint_return_closure_results.json').write_text(json.dumps(out,indent=2)+'\n')
  node['status']='COMPLETE';node['outcomes']={str(k):v for k,v in Counter(tuple(r.get('drift',[]))for r in node['results']).items()};print('DONE NODE',node['state_sha256'],node['outcomes'],flush=True)
 out['status']='CLOSED_WITH_NO_UNKNOWN'if not queue and all(r['status']=='CERTIFIED'for s in out['states']for r in s['results'])else'INCOMPLETE';out['elapsed_seconds']=time.time()-start;(ROOT/'endpoint_return_closure_results.json').write_text(json.dumps(out,indent=2)+'\n');print('DONE',out['status'],len(out['states']),len(queue),out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()

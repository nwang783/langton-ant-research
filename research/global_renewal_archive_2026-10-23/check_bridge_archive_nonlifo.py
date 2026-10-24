"""Literal42-update blank-board witness for bridge-component archive non-LIFO.
Archives store their entire edge-lifetime set, not final-XOR or frozen loops.
"""
from check_renewal_archive import *
OUT=Path(__file__).parent
def run():
 B=set();p=(0,0);h=0;k=wwhich(p,h);birth={};archives=[];states=[];word='';events=[]
 for t in range(43):
  active=component(B,k,cursors(p,h)[1]);ids={birth[q]for q in active}
  states.append({'time':t,'p':p,'h':h,'B':sorted(B),'active_w_edges':sorted(active)})
  for a in archives:
   if a.get('return_time') is None and set(a['lifetimes'])&ids:
    # No dormant edge can be modified before the active component touches it.
    assert all(q in B and birth[q]==b for q,b in a['cell_birth_pairs'])
    a['return_time']=t
  if t==42:break
  q=p;oldw=cursors(p,h)[1];L=q in B;word+='L'if L else'R'
  if not L:birth[q]=t
  p,h=step(B,p,h)
  if L:
   del birth[q]
   if not connected(B,k,*endpoints(q,k)):
    C=component(B,k,oldw)
    if C:
     # Full departed component is exactly dormant in the new state.
     assert C.isdisjoint(component(B,k,cursors(p,h)[1]))
     a={'birth_state':t+1,'cut_cell':q,'cells':sorted(C),'lifetimes':sorted(birth[q]for q in C),'cell_birth_pairs':sorted((q,birth[q])for q in C),'return_time':None}
     archives.append(a)
  events.append({'update':t,'turn':word[-1],'cell':q,'next_pose':[p,h]})
 old=next(a for a in archives if a['birth_state']==17)
 assert old['cells']==[(1,-1),(1,0)] and old['return_time']==42
 newer=[next(a for a in archives if a['birth_state']==t)for t in (18,32,33)]
 assert all(a['return_time'] is None for a in newer)
 assert newer[0]['cells']==[(-1,1),(0,1)]
 assert newer[1]['cells']==[(-2,0)]
 assert newer[2]['cells']==[(-3,-2),(-3,-1)]
 return {'status':'exact component/lifetime nonLIFO witness PASS','scope':__doc__,'word42':word,'older_archive':old,'newer_archives_still_dormant_at42':newer,'archives':archives,'events':events,'states':states}
if __name__=='__main__':
 out=run();(OUT/'bridge_archive_nonlifo.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k not in ('states','events','archives')},indent=2))

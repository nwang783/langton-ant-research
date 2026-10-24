"""Named whole-field controls for metric, R-import/L-departure and archive growth.
No search and no finite controls used to infer the universal clock theorem.
"""
import sys,json,hashlib
from pathlib import Path
ROOT=Path('/workspace/shared/langton');OUT=Path(__file__).parent
sys.path.insert(0,str(ROOT/'renewal_input_placement_2026-10-23'))
from probe_renewal_input_ages import FullGraph,produce,wwhich,cursors,endpoints
from build_forced_input_cycles import vertices

def edges(G,s,skip=None):
 seen={s};todo=[s];E=set()
 for v in todo:
  for u,q in G.g.get(v,{}).items():
   if q==skip:continue
   E.add(q)
   if u not in seen:seen.add(u);todo.append(u)
 return E

def run(name,B,p,h,word,watch):
 B=set(B);k=wwhich(p,h);G=FullGraph(B,k);history={};r=0;counts=dict(metric_pairs=0,consumed_R_lifetimes=0,R_imports=0,L_archival_departures=0,ordinary_archive_inheritances=0,committed_watch_reattachments=0);deaths=[];maxC=0
 protected=None;d0=None;witness=set();temporary=[];block_R=[];watch_peak=0;arm_peak=0;watch_ledgers=[]
 for t,c in enumerate(word):
  w=cursors(p,h)[1];C=edges(G,w);maxC=max(maxC,len(C))
  assert c==('L'if p in B else'R'),(name,t,p,h,c)
  for q in C:
   assert max(abs(p[0]-q[0]),abs(p[1]-q[1]))<=len(C)
   counts['metric_pairs']+=1
  for q,a in history.items():
   active=q in C
   if not a['runs']or a['runs'][-1][0]!=active:a['runs'].append([active,0])
   a['runs'][-1][1]+=1
   if active:a['max_active_mass']=max(a['max_active_mass'],len(C))
  q=p;u,v=endpoints(q,k);other=v if u==w else u;assert w in(u,v)
  nb=c=='L'and other in vertices(edges(G,w,skip=q),k)
  ordinary=c=='L'and r<=2 and not nb
  if protected is None and watch in B and watch not in C:
   protected=edges(G,endpoints(watch,k)[0]);d0=len(protected);witness=set()
  if c=='L':
   if q in history:
    a=history.pop(q);assert a['runs'][0][0]and a['runs'][-1][0]
    assert sum(n for b,n in a['runs'])==t-a['birth']
    dr=[n for b,n in a['runs']if not b];ar=[n for b,n in a['runs']if b]
    assert len(ar)==len(dr)+1
    deaths.append({'death':t,'age':t-a['birth'],'active_cut_total':sum(ar),'dormant_cut_total':sum(dr),'dormant_episodes':len(dr),'max_active_run':max(ar),'max_dormant_run':max(dr,default=0),'max_active_mass':a['max_active_mass']});counts['consumed_R_lifetimes']+=1
   B.remove(q);G.delete(q);h=(h-1)%4
  else:
   B.add(q);G.add(q);h=(h+1)%4;r+=1;block_R.append(q);history[q]={'birth':t,'runs':[],'max_active_mass':0}
  D=((0,1),(1,0),(0,-1),(-1,0));p=(p[0]+D[h][0],p[1]+D[h][1]);wn=cursors(p,h)[1];N=edges(G,wn)
  new=N-C-({q}if c=='R'else set());lost=C-N-({q}if c=='L'else set())
  if c=='L':
   assert not new and N<=C-{q}
   if lost:assert not nb;counts['L_archival_departures']+=1
  else:
   assert not lost and q in N
   if new:
    beforeV=vertices(C,k)|{w};assert other not in beforeV
    assert edges(G,other,skip=q)==new;counts['R_imports']+=1
   if protected is not None and watch not in C and watch in N:temporary.append((q,len(N)))
  if c=='L':
   if ordinary and protected is not None and watch in B:
    assert watch not in N
    archive=edges(G,endpoints(watch,k)[0]);assert protected<=archive
    if temporary:
     for e in block_R:assert e in archive;witness.add(e)
     assert len(C)>=d0+len(witness)+1
    assert witness<=archive and len(archive)>=d0+len(witness)
    counts['ordinary_archive_inheritances']+=1;counts['committed_watch_reattachments']+=len(temporary)
    protected=archive;watch_peak=max(watch_peak,counts['committed_watch_reattachments']);arm_peak=max(arm_peak,len(witness));watch_ledgers.append({'t':t,'base_mass':d0,'current_archive_mass':len(archive),'retained_distinct_R_arms':len(witness)})
   if not ordinary or watch not in B:protected=None;d0=None;witness=set()
   temporary=[];block_R=[];r=0
 return{'name':name,'updates':len(word),'initial_watch_cell':watch,'counts':counts,'max_complete_active_w_mass':maxC,'max_watch_reattachments_cumulative':watch_peak,'max_retained_R_arm_charge_in_one_ordinary_epoch':arm_peak,'watch_ledgers':watch_ledgers,'R_lifetime_death_itineraries':deaths}

def main():
 out=[];s=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text());I={tuple(q)for q in s['seed']};F={(-2,1),(-1,1),(0,1),(1,1),(1,0),(1,-1),(2,-2),(2,-3),(1,-4),(1,-5),(1,-6)}
 out.append(run('fixed24 infinite-standard cap, first8periods',I|F,(0,0),3,s['word']*8,(1,-6)))
 for rr in(1,3,8):
  out.append(run('odd rod two-epoch r'+str(rr),{(x,0)for x in range(2*rr+1)},(0,0),1,'LRRL'*rr+'L'+'RRRRL'+'LRRL'*rr,(rr,0)))
 sys.path.insert(0,str(ROOT/'actual_zipper_spiral_2026-10-23'))
 import check_spiral as sp,check_collector as cc,check_detoured_collector as dc
 B,p,h,vs,path,word=sp.setup(8,8);collector=cc.cells_of(dc.detoured(8,8));connector=cc.cells_of([(0,0),(-1,0),(-1,-1),(0,-1)])
 B|=collector|connector;out.append(run('charged joined detoured collector q8scale8',B,p,h,word,min(collector)))
 B,p,h,W,R,m,prep=produce(1564,1);out.append(run('original184 N1 actual first1564 wave',B,p,h,W,(-1,-15)))
 result={'status':'PASS named complete-board metric, lifetime age decomposition, exact R imports/L archival departures and protected ordinary-archive growth','scope':'Finite controls only; universal active-episode clock and itinerary implication are analytic','controls':out}
 (OUT/'active_itinerary_controls.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({'status':result['status'],'controls':[{k:v for k,v in a.items()if k not in('watch_ledgers','R_lifetime_death_itineraries')}for a in out]},indent=2))
if __name__=='__main__':main()

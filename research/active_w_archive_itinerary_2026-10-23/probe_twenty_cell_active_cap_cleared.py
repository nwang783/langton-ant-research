"""Targeted20-cell controls through exact full future w-frontier clearance.
Each individual finite input gets an infinite-H certificate and all-future cap;
no all-parameter component cap is inferred from the examples.
"""
from probe_twenty_cell_active_cap import *
from build_forced_input_cycles import deterministic_trace,occurrences
J=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text());H=J['word'];I={tuple(q)for q in J['seed']};tr,_,_=deterministic_trace(H,(0,0),3);d=(-2,-2)
K={tuple(q)for q in json.loads((ROOT/'standard_unread_cap_2026-10-23/standard_w_frontier_certificate.json').read_text())['frontier_K']}
def normal(E,p,r):return{rot((x-p[0],y-p[1]),-r)for x,y in E}
def sh(E,j):return{(x-2*j,y-2*j)for x,y in E}

def cleared(n):
 poses=[((0,0),1),((n-1,n),0),((-n,3*n-4),3),((-5*n+5,-n),2),((-3*n,-3*n+8),1)]
 B=set()
 for p,h in poses:B|={(p[0]+v[0],p[1]+v[1])for z in G0 for v in[rot(z,h-1)]}
 p=(0,0);h=1;k=wwhich(p,h);G=FullGraph(B,k);rawcap=624*n-742;cap=rawcap;aligned=False;end=cap+208;maxC=0;firstmax=None;tailpose=None;tailB=None;M=None;Nc=None;exclusions=0;t=0
 while t<end:
  C=edges(G,cursors(p,h)[1])
  if len(C)>maxC:maxC=len(C);firstmax=t
  if t==rawcap and not aligned:
   tmp=set(B);pp=p;hh=h;word=''
   for z in range(104):
    cc='L'if pp in tmp else'R';word+=cc
    if cc=='L':tmp.remove(pp);hh=(hh-1)%4
    else:tmp.add(pp);hh=(hh+1)%4
    dd=((0,1),(1,0),(0,-1),(-1,0))[hh];pp=(pp[0]+dd[0],pp[1]+dd[1])
   phases=[j for j in range(104)if word==H[j:]+H[:j]];assert len(phases)==1
   delta=(-phases[0])%104;cap=rawcap+delta;end=cap+208;aligned=True
  if t==cap and aligned:
   tailpose=(p,h);tailB=normal(B,p,h-3);assert I<=tailB
   for q in tailB-I:
    assert not any(z['copy_offset']>=0 for z in occurrences(q,tr,d)),(n,q)
    exclusions+=1
  if t>=cap and aligned:assert('L'if p in B else'R')==H[(t-cap)%104]
  q=p
  if q in B:B.remove(q);G.delete(q);h=(h-1)%4
  else:B.add(q);G.add(q);h=(h+1)%4
  D=((0,1),(1,0),(0,-1),(-1,0));p=(p[0]+D[h][0],p[1]+D[h][1]);t+=1
  if t==cap+208:
   p0,h0=tailpose;NB=normal(B,p0,h0-3);assert sh(K,2)<=NB
   E=NB-sh(K,2);M=min(sum(v)for v in vertices(E,0));Nc=max(2,(6-M)//8+1);end=cap+104*(Nc+2)
 out={'n':n,'original_mass':20,'retained_first_standard_entry_time':rawcap,'phase0_capture_time':cap,'capture_pose':tailpose,'captured_normalized_full_mass':len(tailB),'all_future_unread_extra_cells_certified':exclusions,'normalized_archive_vertex_sum_min':M,'sufficient_clearance_period':Nc,'verified_physical_updates':end,'max_complete_active_w_mass_before_clearance_and_two_periods':maxC,'first_max_cut':firstmax,'all_future_active_w_mass_after_clearance':42,'rigorous_entire_future_active_w_mass_bound_for_THIS_input':max(maxC,42),'scope':'Each specific finite input gets full all-future H ray exclusion and exact clearance; no all-n cap inferred'}
 return out
if __name__=='__main__':
 out=[cleared(n)for n in(20,40,80)]
 (OUT/'twenty_cell_active_cap_cleared_probe.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

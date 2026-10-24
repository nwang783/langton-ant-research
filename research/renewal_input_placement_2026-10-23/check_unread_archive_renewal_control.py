"""Same actual finite word/read history, different complete renewal flags.
The larger field is reached from the retained original184-cell finite seed.
"""
from build_forced_input_cycles import *
OUT=Path(__file__).parent

def run(N=3):
 B,p,h,W,R,sm,prep=produce(1564,N);full0=set(B);pose=(p,h)
 small,tr,_,_=infer_input(W*N,p,h);small0=set(small);reads={q for q,hh,c in tr};extra=full0-small0
 assert small0<=full0 and not extra&reads
 k=wwhich(p,h);G=FullGraph(B,k);S=FullGraph(small,k);r=0;diff=[];largest=None
 for t,(q,hh,c)in enumerate(tr):
  assert(q,hh)==(p,h)
  assert B==small|extra
  if c=='R':G.add(q);S.add(q);r+=1
  else:
   big=G.nonbridge(q);little=S.nonbridge(q);assert not little or big
   if big and not little:
    pa=graph_path(G,q);assert pa is not None
    z={'t':t,'period':t//len(W),'slot':t%len(W),'q':q,'r':r,'shortest_bypass_edges':len(pa),'extra_edges_in_bypass':sum(e in extra for e in pa),'bypass_radius_L1':max(abs(e[0]-q[0])+abs(e[1]-q[1])for e in pa),'cycle_cells':[q]+pa}
    diff.append({a:b for a,b in z.items()if a!='cycle_cells'})
    if largest is None or len(pa)>largest['shortest_bypass_edges']:largest=z
   G.delete(q);S.delete(q);r=0
  p,h=step(B,p,h)
  if q in small:small.remove(q)
  else:small.add(q)
 assert B==small|extra
 return {'scope':__doc__,'N':N,'R':R,'original_seed_mass':sm,'preparation_steps':prep,'wave_entry_pose':pose,'full_entry_mass':len(full0),'minimal_entry_mass':len(small0),'unread_archive_mass':len(extra),'entire_word_length':len(W)*N,'different_w_renewal_flags':len(diff),'first_difference':diff[0],'largest_nonlocal_cycle':largest,'differences':diff,'full_entry_board':sorted(full0),'minimal_entry_board':sorted(small0),'unread_extra_board':sorted(extra)}

if __name__=='__main__':
 out=run();(OUT/'unread_archive_renewal_control.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k not in('full_entry_board','minimal_entry_board','unread_extra_board','differences','largest_nonlocal_cycle')},indent=2));print('max', {k:v for k,v in out['largest_nonlocal_cycle'].items()if k!='cycle_cells'})

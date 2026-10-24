"""Only the first reimport and following ordinary epoch of the fixed family."""
from check_detoured_collector import detoured
from check_collector import cells_of,component
from check_spiral import *

def check(q):
 B,p,h,vs,cells,w=setup(q,8);B|=cells_of(detoured(q,8))|cells_of([(0,0),(-1,0),(-1,-1),(0,-1)])
 for c in w:
  assert('L'if p in B else'R')==c;p,h=step(B,p,h)
 F=len(B);word='';r=0;blocks=[]
 for t in range(15):
  c='L'if p in B else'R';word+=c
  if c=='R':r+=1
  else:
   wb=connected(B-{p},0,*endpoints(p,0));zb=connected(B-{p},1,*endpoints(p,1));before=len(component(B,0,cursors(p,h)[1]))
  p,h=step(B,p,h)
  if c=='L':
   blocks.append({'time':t+1,'r':r,'w_nonbridge':wb,'z_nonbridge':zb,'active_before':before,'active_after':len(component(B,0,cursors(p,h)[1])),'mass_after':len(B)});r=0
 assert word=='RRRRLLLLRLRRRRL'
 assert [b['r']for b in blocks]==[4,0,0,0,1,4]
 assert [b['active_after']for b in blocks]==[F+3,F+2,3,2,0,0]
 assert [b['w_nonbridge']for b in blocks]==[True,False,False,False,False,False]
 assert [b['z_nonbridge']for b in blocks]==[True,False,False,False,False,True]
 return {'q':q,'archive_mass_before_reimport':F,'prefix':word,'blocks':blocks}

if __name__=='__main__':
 out=[check(q)for q in(1,2,3,4,8,16,32)]
 Path(__file__).with_name('collector_first_reimport_controls.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out[-1],indent=2))

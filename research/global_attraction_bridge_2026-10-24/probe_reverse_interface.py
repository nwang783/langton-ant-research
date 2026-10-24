import json
from pathlib import Path
from blank_collision_operator import D,C,H
P=Path(__file__).parent
B={(-47,-28)};p=(0,0);h=0;seen=set();word=[];cuts={};new=[]
for t in range(64200+7994+104):
 if t in(9977,10393,62655,64200,72194):cuts[t]=dict(black=sorted(B),pose=[p,h],mass=len(B))
 if t>=64200 and p not in seen:
  new.append(dict(time=t,offset=t-64200,cell=p,heading=h,dist_to_hit=abs(p[0]-20)+abs(p[1]+22)))
 if t==64200:print('hit',p,h,'mass',len(B),'seen',len(seen))
 seen.add(p);a='L'if p in B else'R';word.append(a);B^={p};h=(h+(1 if a=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
w=''.join(word);assert w[:9977]==C and w[9977:10393]==H*4
A=w[10393:62655];V=w[62655:62759];assert w[62655:64200]==V*14+V[:89]
print('first new',new[:12]);print('nearest',[r for r in new if r['dist_to_hit']<=6][:15]);print('A len',len(A),'V',V,'endpoint',cuts[72194]['pose'])
(P/'REVERSE_INTERFACE_DISCOVERY.json').write_text(json.dumps(dict(initial_black=[(-47,-28)],cuts=cuts,stable_word=A,reverse_word=V,post_hit_word=w[64200:72194],terminal_word=w[72194:],new_cells=new,whole_word=w),indent=2)+'\n')

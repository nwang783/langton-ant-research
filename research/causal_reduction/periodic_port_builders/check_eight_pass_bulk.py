import collections,json,pathlib
D=((0,1),(1,0),(0,-1),(-1,0));A='LRLLRRRRLLRL';B='RRRLLLLRLLLLRLLLLRRRRLRRRRLR';S='RLLR';W='LLRLRRRRLRRRRLLLLRLL'
P=pathlib.Path(__file__).resolve().parent
passes=[(A,(0,0,1)),(S,(0,8,3)),(B,(0,2,1)),(W,(0,8,1)),(A,(0,0,1)),(S,(0,10,3)),(B,(0,2,1)),(S,(-1,9,3))]
field=[513,519];original=field[:];out=[]
for w,entry in passes:
 x,y,h=entry;assert (x+y+h)%2==1;rr=[]
 for t,c in enumerate(w):rr.append((x,y,t,c));h=(h+(1 if c=='R'else-1))%4;dx,dy=D[h];x+=dx;y+=dy
 drift=x-entry[0];assert drift in(-2,2)and(y,h)==entry[1:]
 groups=collections.defaultdict(list)
 for x,y,t,c in rr:
  q=x%2;k=(x-q)//drift;groups[q,y].append((-k,t,c))
 after=field[:];hist=[]
 for(q,y),v in sorted(groups.items()):
  s=''.join(c for k,t,c in sorted(v));assert (s[0]=='L')==bool(field[q]>>y&1);assert all(a!=b for a,b in zip(s,s[1:]));after[q]=(after[q]|1<<y)if s[-1]=='R'else(after[q]&~(1<<y));hist.append([q,y,s])
 out.append(dict(word=w,entry=entry,drift=drift,input=field,output=after,histories=hist));field=after
assert field==original
assert [sum((-1)**y*((m>>y)&1)for y in range(12))%4 for m in field]==[0,0]
assert sum(m.bit_count()for m in field)==6
# New six-column board increments and fixed-port row charges.
for y in range(12):
 gain=3*(((field[0]>>y)&1)-((field[1]>>y)&1))
 port=2*(int(2>y)-int(1>y))+int(2==y)-int(1==y)
 assert (gain-port)%4==0
(P/'eight_pass_bulk_certificate.json').write_text(json.dumps(dict(passes=out,bulk_restored=True,new_mass=18,repeat_growth=3),indent=2));print('PASS eight stable bulk passes and necessary sector/charge constraints; no caps supplied')

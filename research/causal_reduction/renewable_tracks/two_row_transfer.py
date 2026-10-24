"""Discover exact return transfers of two-row input words; no all-width claim."""
from two_row_right_cap import *
def run_transfers(mask,M,steps=2000):
 D=set()
 for j in range(M):
  if mask>>(2*j)&1:D.add((j,-1))
  if mask>>(2*j+1)&1:D.add((j,0))
 x=y=0;h=1;word=[];out=[]
 for t in range(steps):
  c=((y==0 and x<0)^((x,y) in D));word.append('L' if c else 'R')
  if (x,y) in D:D.remove((x,y))
  else:D.add((x,y))
  h=(h+(-1 if c else 1))%4;dx,dy=((0,1),(1,0),(0,-1),(-1,0))[h];x+=dx;y+=dy
  if y < -1 or y>4:return out,'EXIT'
  if (x,y,h)==(0,0,1):
   reg=lambda a,b: (b==0 and (a<=-2 or a==0))or(b==1 and a<=0)or(b in (2,3) and a<=-1)
   guard={p for p in D if reg(*p)}=={(0,0),(0,1),(-1,2)} and not any(b==4 and a<0 for a,b in D)
   if guard:
    output=sum(1<<(2*a+(b-3)) for a,b in D if a>=0 and b in(3,4))
    out.append(dict(input=mask,output=output,word=''.join(word),input_mass=mask.bit_count(),output_mass=output.bit_count()))
    return out,'W_GUARD'
  # Same exact escape guards as main discovery script.
  if y==0 and h==0 and x<=-2 and not any((b==0 and a<=x)or(b==-1 and a<=x-1) for a,b in D):return out,'S_ESCAPE'
  if y==0 and h==1 and x<=-2:
   q=x;reg=lambda a,b:(b==0 and (a<=q-2 or a==q))or(b==1 and a<=q)or(b in(2,3) and a<=q-1)
   if {p for p in D if reg(*p)}=={(q,1),(q-1,2)}:return out,'W_ESCAPE'
 return out,'UNKNOWN'
if __name__=='__main__':
 M=int(sys.argv[1]) if len(sys.argv)>1 else 8;t0=time.time();C=Counter();trans=[];unknown=[]
 for mask in range(1<<(2*M)):
  out,st=run_transfers(mask,M);C[st]+=1;trans.extend(out)
  if st=='UNKNOWN':unknown.append(mask)
 unique={d['word']:d for d in trans};stats=dict(M=M,counts=dict(C),transfers=len(trans),distinct_words=len(unique),unknown=unknown,seconds=time.time()-t0)
 (HERE/f'two_row_transfers_{M}.json').write_text(json.dumps(dict(stats=stats,transfers=trans),indent=2));print(json.dumps(stats,indent=2))

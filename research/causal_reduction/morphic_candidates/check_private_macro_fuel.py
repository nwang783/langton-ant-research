"""Exact finite ownership tests for arbitrary geometric image choices."""
import json,pathlib,collections,sys
from search_complementary_roots import D
HERE=pathlib.Path(__file__).resolve().parent

def reads(w):
 x=y=h=0;out=[]
 for c in w:
  out.append((x,y,c));h=(h+(1 if c=='R'else-1))%4;dx,dy=D[h];x+=dx;y+=dy
 return out

def rot(x,y,h):
 for _ in range(h):x,y=y,-x
 return x,y

def ownership(a,b,images):
 norm=a*a+b*b;templates=[]
 for w in images:
  for x,y,c in reads(w):
   for h in range(4):
    X,Y=rot(x,y,h);templates.append((X,Y,h))
 def owners(x,y):
  out=set()
  for X,Y,h in templates:
   dx,dy=x-X,y-Y;n=a*dx+b*dy;m=a*dy-b*dx
   if n%norm or m%norm:continue
   p,q=n//norm,m//norm
   if (p+q+h)%2==0:out.add((p,q))
  return sorted(out)
 return owners

def check(r):
 a,b=r['scale'];opts=r['images'];owner=ownership(a,b,opts['R']+opts['L']);report=[]
 for w in opts['R']:
  first={}
  for x,y,c in reads(w):first.setdefault((x,y),c)
  cells=[]
  for p,c in first.items():
   if c=='L':
    os=owner(*p);cells.append(dict(cell=p,owners=os,private=os==[(0,0)],forward=all(y>=0 for x,y in os)))
  report.append(dict(word=w,cells=cells,private=any(z['private']for z in cells),forward=any(z['forward']for z in cells)))
 return dict(scale=[a,b],all_R_private=all(z['private']for z in report),all_R_forward=all(z['forward']for z in report),R_images=report)

if __name__=='__main__':
 out=[]
 for k in (3,5,7,9):
  p=HERE/f'free_inflations_k{k}.json'
  if not p.exists():continue
  for r in json.loads(p.read_text())['results']:
   z=check(r);z.update(k=k,previous_status=r['status']);out.append(z)
   if r['status']not in('NONINCREASING_SCALE_MASS','EXHAUSTED'):print(k,r['scale'],r['status'],'private',z['all_R_private'],'forward',z['all_R_forward'],flush=True)
 (HERE/'private_macro_fuel.json').write_text(json.dumps(out,indent=2))

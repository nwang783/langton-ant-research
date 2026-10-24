"""All-age fixed local return, retaining three complete semi-infinite rails."""
import sys,json,gzip,hashlib
from pathlib import Path
from certify_strip_model import HERE,ROOT,SRC
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'));from ant_exact import W,P,D,step,plan,certify_period
sys.path.insert(0,str(HERE.parent/'transverse'));from crossing import Field,tail,plus

def initial():
 S=json.loads((HERE/'strip_model.json').read_text());B=set(P)^set(map(tuple,S['packet_cells']));p0=(2,24);entry=(-70,130)
 B.symmetric_difference_update({plus(p0,(-x,-y)) for x,y in P});B.symmetric_difference_update({plus(entry,q) for q in P})
 rays=[(plus(q,(-2,2)),(-2,2),0,None) for q in D]+[(plus(p0,(-x,-y)),(-2,2),0,None) for x,y in D]+[(plus(plus(entry,q),(-2,2)),(-2,2),0,None) for q in D]
 return Field(rays,B),entry,2

def main():
 F,p,h=initial();B=set(F.changes)
 for base,d,lo,hi in F.rays:
  for j in range(200):B.symmetric_difference_update({plus(base,(j*d[0],j*d[1]))})
  assert base[0]-base[1]+200*(d[0]-d[1])<-250
 word=gzip.open(HERE/'local_return_word.txt.gz','rt').read();assert len(word)==18304 and set(word)<={'R','L'};us=[];zs=[]
 for c in word:
  us.append(p[0]-p[1]);zs.append(sum(p));bp,bh=p,h;p,h,ch=step(B,p,h);ip,ih,ic=F.step(bp,bh);assert ch==c and (p,h,ch)==(ip,ih,ic)
 assert p==(90,-26) and h==0;tw=W[8:]+W[:8];f=certify_period(B,p,h,tw);i=tail(F,p,h,tw);assert f and i and tuple(f['drift'])==(2,-2)
 qs,_,end,eh=plan(tw,p,h);assert eh==h;tu=[q[0]-q[1] for q in qs];tz=list(map(sum,qs));assert min(us+tu)>=-200 and min(zs+tz)>=-100 and max(zs+tz)<=100
 phase0,h0=plan(tw[:96],p,h)[2:];q72=plan(W[:72],phase0,h0)[2];assert phase0==(90,-28) and h0==2 and q72==(98,-30)
 out=dict(status='exact full local return throughout the common half-plane/strip',capture=18304,pose=[p,h],phase=8,drift=[2,-2],prefix_u_bounds=[min(us),max(us)],prefix_z_bounds=[min(zs),max(zs)],whole_future_u_lower=min(us+tu),whole_future_z_bounds=[min(zs+tz),max(zs+tz)],outgoing_phase_zero=[phase0,h0],phase72_base=q72,strip_model_sha256=hashlib.sha256((HERE/'strip_model.json').read_bytes()).hexdigest(),word_sha256=hashlib.sha256(word.encode()).hexdigest())
 (HERE/'local_return.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

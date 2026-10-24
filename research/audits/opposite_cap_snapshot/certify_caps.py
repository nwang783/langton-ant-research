"""Literal finite cap kernels and exact infinite-rail tail certificates."""
import json,gzip,hashlib,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'))
from ant_exact import W,P,D,step,plan,certify_period
sys.path.insert(0,str(HERE.parent/'transverse'));from crossing import Field,tail,rotate,plus

def blank():
 B=set();p=(0,0);h=0
 for _ in range(9977):p,h,_=step(B,p,h)
 assert p==(-15,10) and h==3
 return p,B^{plus(p,rotate(q,1)) for q in P}

def initial(row):
 O,E=blank();cap=tuple(row['start'][0]);assert row['start'][1]==1
 rays=[(plus(O,rotate(q,1)),(-2,-2),0,None) for q in D]+[(plus(cap,plus(rotate(q,3),(-2,-2))),(-2,-2),0,None) for q in D]
 return Field(rays,E^{plus(cap,rotate(q,3)) for q in P}),cap,1

def main():
 source=json.loads((HERE/'cap_discovery.json').read_text());assert [r['r'] for r in source]==[29,32,56,71];rows=[]
 for row in source:
  r=row['r'];infinite,p,h=initial(row);assert [list(p),h]==row['start'];B=set(infinite.changes)
  for base,d,lo,hi in infinite.rays:
   assert lo==0 and hi is None
   for j in range(100):B.symmetric_difference_update({plus(base,(j*d[0],j*d[1]))})
   assert sum(base)+100*sum(d)<-250
  mass=len(B);word=gzip.open(HERE/row['word_file'],'rt').read();assert word and set(word)<={'R','L'} and len(word)==row['capture'];reads=[]
  for expected in word:
   reads.append(p);bp,bh=p,h;p,h,ch=step(B,p,h);ip,ih,ic=infinite.step(bp,bh);assert (p,h,ch)==(ip,ih,ic) and ch==expected
  assert [list(p),h]==row['pose'];phase=row['tail']['phase'];tw=W[phase:]+W[:phase];fproof=certify_period(B,p,h,tw);iproof=tail(infinite,p,h,tw);assert fproof and iproof and list(fproof['drift'])==row['tail']['drift']
  qs,_,end,eh=plan(tw,p,h);d=tuple(end[i]-p[i] for i in range(2));assert eh==h;zb=[min(map(sum,reads)),max(map(sum,reads))];assert zb==row['prefix_z_bounds'];permanent=sum(d)>=0
  assert zb[0]>=-123
  if permanent:assert min(map(sum,qs))>=-123
  expected={29:(416,[-73,-32],1,0,[2,2]),32:(416,[-78,-29],1,0,[2,2]),56:(4264,[11,-26],1,8,[-2,-2]),71:(8112,[-20,45],1,97,[-2,2])}[r]
  assert (len(word),list(p),h,phase,list(d))==expected
  rows.append(dict(phase=r,start=row['start'],capture=len(word),pose=[p,h],tail_phase=phase,drift=d,finite_kernel_mass=mass,prefix_z_bounds=zb,entire_future_z_lower=min(zb[0],min(map(sum,qs))) if permanent else None,permanent_halfplane_transfer=permanent,word_sha256=hashlib.sha256(word.encode()).hexdigest()))
 assert [r['phase'] for r in rows if r['permanent_halfplane_transfer']]==[29,32,71]
 out=dict(status='four exact cap kernels; three permanent transfers and one prefix-only transfer',rows=rows,scope='Phase56 returns southwest below the comparison half-plane, so its model tail does not establish actual capture.')
 (HERE/'caps.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

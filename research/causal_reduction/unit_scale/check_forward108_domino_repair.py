"""Disconnected but exactly owned H / LR / forward108 bulk repair interface.
All pieces are scheduled once per D=(2,2), in that order. This certifies
color histories ONLY; three pose-to-pose connectors remain missing.
"""
from pathlib import Path
import collections,json,hashlib
import certify_short_refinement_rup as core
P=Path(__file__).resolve().parent
H=json.loads((P/'short_refinement_scaffold_inputs.json').read_text())['H']
Q=json.loads((P/'forward108_prepared_control.json').read_text())['word']
D=(2,2)
def trace(w,p,h):return core.trace(w,p,h)
def orbit(p):return(p[0]-p[1],p[0]%2)
# Coordinates x are sometimes odd; use -(x//2), NOT (-x)//2.
def group(rows):
 by=collections.defaultdict(list)
 for i,(p,h,c) in enumerate(rows):by[orbit(p)].append((-(p[0]//2),i,p,h,c))
 for a in by:by[a].sort()
 return by

def main():
 hb=group(trace(H,(0,10),1)[0]);rb=group(trace('LR',(-1,6),2)[0]);qb=group(trace(Q,(0,0),1)[0])
 # Within ties H precedes repair precedes Q. These integer inequalities
 # place every H read before repair/Q and both repair reads before Q.
 hq=max(hb[a][-1][0]-qb[a][0][0] for a in hb.keys()&qb.keys())
 hr=max(hb[a][-1][0]-rb[a][0][0] for a in hb.keys()&rb.keys())
 rq=max(rb[a][-1][0]-qb[a][0][0] for a in rb.keys()&qb.keys())
 t=max(0,rq);l=max(0,hq,t+hr)
 starts=[(2*l,10+2*l,1),(-1+2*t,6+2*t,2),(0,0,1)]
 words=[H,'LR',Q];hist=collections.defaultdict(list);endpoints=[]
 for kind,(w,(x,y,h)) in enumerate(zip(words,starts)):
  rr,e,g=trace(w,(x,y),h);endpoints.append((*e,g))
  for i,(q,hh,c) in enumerate(rr):hist[orbit(q)].append((-(q[0]//2),kind,i,q,hh,c))
 for a,vv in hist.items():
  vv.sort();assert vv[0][-1]=='R',(a,vv)
  assert all(a[-1]!=b[-1] for a,b in zip(vv,vv[1:])),(a,vv)
 output=sorted(a for a,v in hist.items() if v[-1][-1]=='R')
 missing=[dict(start=endpoints[0],target=starts[1]),dict(start=endpoints[1],target=starts[2]),dict(start=endpoints[2],target=(starts[0][0]+2,starts[0][1]+2,starts[0][2]))]
 out=dict(scope=__doc__,drift=D,heading_order='N,E,S,W',inequalities=dict(l_at_least=hq,l_minus_t_at_least=hr,t_at_least=rq),chosen_l=l,chosen_t=t,words=words,starts=starts,endpoints=endpoints,read_classes=len(hist),output_black_classes=output,partial_turn_charge=sum(w.count('R')-w.count('L') for w in words),histories=[dict(orbit=a,events=v) for a,v in sorted(hist.items())],missing_connectors=missing,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
 (P/'forward108_domino_repair.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k not in ['words','histories','output_black_classes','source_sha256']})
if __name__=='__main__':main()

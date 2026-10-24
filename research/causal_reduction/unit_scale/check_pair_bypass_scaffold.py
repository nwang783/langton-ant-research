"""Literal single minimal pair bypasses in the actual inverse104 context.
Only one pair is replaced, in either disjoint pairing alignment. Complete
bi-infinite orbit histories are reconstructed; no finite-prefix acceptance.
"""
from pathlib import Path
import collections,json,hashlib
P=Path(__file__).resolve().parent
D=[(0,1),(1,0),(0,-1),(-1,0)]
def trace(w,h):
 x=y=0;rows=[]
 for t,c in enumerate(w):
  rows.append((t,(x,y),h,c))
  h=(h+(1 if c=='R' else -1))%4
  dx,dy=D[h];x+=dx;y+=dy
 return rows,(x,y),h

def histories(w,h):
 rows,end,hh=trace(w,h)
 assert end==(-2,-2) and hh==h
 g=collections.defaultdict(list)
 for t,(x,y),q,c in rows:
  a=(x-y,x%2);g[a].append((t+len(w)*(x//2),t,(x,y),q,c))
 bad=[]
 for a,rr in sorted(g.items()):
  rr.sort()
  for u,v in zip(rr,rr[1:]):
   if u[-1]==v[-1]:bad.append(dict(orbit=a,earlier=u,later=v))
 return dict(word=w,length=len(w),start_heading=h,end=end,final_heading=hh,
             status='LEGAL_PREPARED_PERIODIC' if not bad else 'ILLEGAL_PERIODIC',
             input_black_classes=[a for a,rr in sorted(g.items()) if rr[0][-1]=='L'],
             output_black_classes=[a for a,rr in sorted(g.items()) if rr[-1][-1]=='R'],
             read_classes=len(g),charge=w.count('R')-w.count('L'),conflicts=bad,
             complete_histories=[dict(orbit=a,events=rr) for a,rr in sorted(g.items())])

def main():
 z=json.loads((P/'short_refinement_scaffold_inputs.json').read_text())
 V=z['reverse104'];pal=json.loads((P/'minimal_pair_bypass_geometry.json').read_text())['inventories']
 base,_,_=trace(V,3);cases=[]
 for cut in [0,1]:
  W=V[cut:]+V[:cut];h=base[cut][2]
  for phase in range(0,104,2):
   pair=W[phase:phase+2]
   for b in pal[pair][1:]:
    word=W[:phase]+b+W[phase+2:]
    out=histories(word,h);out.update(cyclic_cut=cut,pair_phase=phase,original_pair_phase=(phase+cut)%104,coarse_pair=pair,bypass=b)
    cases.append(out)
 summary=dict(total=len(cases),counts=dict(collections.Counter(z['status'] for z in cases)),survivors=[{k:v for k,v in z.items() if k not in ['complete_histories','conflicts']} for z in cases if z['status']=='LEGAL_PREPARED_PERIODIC'])
 out=dict(scope=__doc__,summary=summary,cases=cases,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
 (P/'pair_bypass_scaffold.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(summary,indent=2))
if __name__=='__main__':main()

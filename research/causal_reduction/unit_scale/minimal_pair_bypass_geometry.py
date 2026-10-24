"""Complete first geometric bypass of a two-turn coarse corner.
Not an arbitrary longer unit-image palette: the intermediate coarse POSE is
never reached, so the signed unit-pose refinement obstructions do not apply.
"""
from pathlib import Path
import collections,itertools,json,hashlib
P=Path(__file__).resolve().parent
D=[1j,1+0j,-1j,-1+0j]

def trace(w):
 q=0j;h=0;rows=[];known={}
 for t,c in enumerate(w):
  p=(int(q.real),int(q.imag));rows.append((p,h,c))
  if known.get(p)==c:return rows,None,None
  known[p]=c;h=(h+(1 if c=='R' else -1))%4;q+=D[h]
 return rows,(int(q.real),int(q.imag)),h

def raw_trace(w):
 q=0j;h=0;rows=[]
 for c in w:
  rows.append(((int(q.real),int(q.imag)),h,c))
  h=(h+(1 if c=='R' else -1))%4;q+=D[h]
 return rows,(int(q.real),int(q.imag)),h

def periodic(w):
 rows,e,h=raw_trace(w)
 if h!=0:return dict(status='NOT_HEADING_PRESERVING',endpoint=e,heading=h)
 dx,dy=e
 if dx==dy==0:return dict(status='ZERO_DISPLACEMENT')
 assert dx!=0
 # Spatial class: normal dy*x-dx*y, plus x mod |dx|.
 g=collections.defaultdict(list)
 for t,(p,hh,c) in enumerate(rows):
  x,y=p;a=(dy*x-dx*y,x%abs(dx));l=(x-a[1])//dx
  g[a].append((t-l*len(w),t,p,c))
 bad=[]
 for a,v in g.items():
  v.sort()
  for aa,bb in zip(v,v[1:]):
   if aa[-1]==bb[-1]:bad.append(dict(orbit=a,earlier=aa,later=bb))
 return dict(status='LEGAL_PREPARED_PERIODIC' if not bad else 'ILLEGAL_PERIODIC',
             word=w,length=len(w),drift=e,charge=w.count('R')-w.count('L'),
             input_black_classes=sorted(a for a,v in g.items() if v[0][-1]=='L'),
             output_black_classes=sorted(a for a,v in g.items() if v[-1][-1]=='R'),
             read_classes=len(g),complete_histories=[dict(orbit=a,events=v) for a,v in sorted(g.items())],conflicts=bad)

def main():
 records=[];inventories={};counts={}
 for pair in ['RR','RL','LR','LL']:
  coarse,e,h=raw_trace(pair);mid=coarse[1][:2];pal=[];count={}
  for n in [2,6,10]:
   geom=[];legal=[]
   for bits in itertools.product('RL',repeat=n):
    w=''.join(bits);rr,ee,hh=raw_trace(w)
    if (ee,hh)!=(e,h) or any((p,g)==mid for p,g,c in rr):continue
    geom.append(w)
    r,a,b=trace(w)
    if a is not None:legal.append(w)
   count[n]=dict(geometric=geom,internally_legal=legal)
   if n<10:assert not geom
   else:assert len(geom)==len(legal)==2;pal=legal
  counts[pair]=count;inventories[pair]=[pair]+pal
  for w in pal:
   rr,ee,hh=raw_trace(w);assert len({p for p,g,c in rr})==10
   I=sorted(p for p,g,c in rr if c=='L');O=sorted(p for p,g,c in rr if c=='R')
   records.append(dict(coarse_pair=pair,word=w,endpoint=e,final_heading=h,
                       avoided_intermediate_pose=[mid[0],mid[1]],
                       input_black=I,output_black=O,read_support=sorted(p for p,g,c in rr),
                       complete_XOR=sorted(p for p,g,c in rr),
                       source_first_turn=w[0],endpoint_read_events=[dict(time=t,heading=g,turn=c) for t,(p,g,c) in enumerate(rr) if p==e],
                       intermediate_cell_reads=[dict(time=t,heading=g,turn=c) for t,(p,g,c) in enumerate(rr) if p==mid[0]],
                       raw_reads=rr))
 controls=[]
 for pair in ['RL','LR']:
  for a,b in itertools.product(inventories[pair],repeat=2):
   out=periodic(a+b);out.update(coarse_pair=pair,images=[a,b]);controls.append(out)
 out=dict(scope=__doc__,inventories=inventories,complete_length_controls=counts,
          primitive_records=records,two_occurrence_periodic_controls=controls,
          source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
 (P/'minimal_pair_bypass_geometry.json').write_text(json.dumps(out,indent=2)+'\n')
 print('palettes',inventories)
 print('repeat controls',collections.Counter(z['status'] for z in controls))
 for z in controls:
  if z['status']=='LEGAL_PREPARED_PERIODIC':print({k:z[k] for k in ['coarse_pair','images','length','drift','charge','input_black_classes','output_black_classes']})
if __name__=='__main__':main()

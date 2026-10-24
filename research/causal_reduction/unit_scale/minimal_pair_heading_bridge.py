"""Minimal position-preserving, heading-flipping two-turn bridges.
No larger pose-preserving palette: the coarse pair endpoint heading is
opposite, and the next minimal two-read pair resets it. Complete local
fields and actual inverse104 single-defect contexts are retained.
"""
from pathlib import Path
import itertools,collections,json,hashlib
import certify_short_refinement_rup as core
P=Path(__file__).resolve().parent
S=json.loads((P/'short_refinement_scaffold_inputs.json').read_text())

def fields(w,h=0):
 rows,e,hh=core.trace(w,(0,0),h);last={};I=set();bad=[]
 for t,(q,g,c) in enumerate(rows):
  if q in last and last[q][1]==c:bad.append((q,last[q][0],t,c))
  if q not in last and c=='L':I.add(q)
  last[q]=(t,c)
 return dict(word=w,initial_heading=h,endpoint=e,final_heading=hh,reads=rows,
             input_black=sorted(I),output_black=sorted(q for q,tc in last.items() if tc[1]=='R'),
             read_support=sorted(last),complete_XOR=sorted(q for q in last if sum(a[0]==q for a in rows)%2),conflicts=bad)

def periodic(w,h):
 rows,e,hh=core.trace(w,(0,0),h);assert(e,hh)==((-2,-2),h)
 by=collections.defaultdict(list)
 for t,(q,g,c) in enumerate(rows):by[(q[0]-q[1],q[0]%2)].append((t+len(w)*(q[0]//2),t,q,g,c))
 bad=[]
 for a,rr in sorted(by.items()):
  rr.sort()
  for u,v in zip(rr,rr[1:]):
   if u[-1]==v[-1]:bad.append(dict(orbit=a,earlier=u,later=v))
 return dict(word=w,start_heading=h,length=len(w),charge=w.count('R')-w.count('L'),status='ILLEGAL' if bad else 'LEGAL_PREPARED',
             read_classes=len(by),input_black_classes=sorted(a for a,rr in by.items() if rr[0][-1]=='L'),
             output_black_classes=sorted(a for a,rr in by.items() if rr[-1][-1]=='R'),
             complete_histories=[dict(orbit=a,events=rr) for a,rr in sorted(by.items())],conflicts=bad)

def old_alignment(word,coarse):
 # Literal word membership in the old exact-pose1/5/9 concatenation language;
 # geometry follows automatically for its supplied fixed-pose images.
 states={0}
 for c in coarse:states={n+len(v) for n in states for v in S['local_images'][c] if word.startswith(v,n)}
 return len(word) in states

def main():
 pal={};primitives=[]
 for pair in ['RR','RL','LR','LL']:
  rows,e,h=core.trace(pair,(0,0),0);pal[pair]={}
  for eps in [0,1]:
   hh=2*eps;words=[]
   for n in [2,6]:
    cur=[]
    for ss in itertools.product('RL',repeat=n):
     w=''.join(ss);rr,ee,g=core.trace(w,(0,0),hh)
     if(ee,g)!=(e,(h+2)%4):continue
     f=fields(w,hh);assert not f['conflicts'] and len(f['read_support'])==6
     cur.append(w);f.update(coarse_pair=pair,incoming_flip=eps,outgoing_flip=1);primitives.append(f)
    if n==2:assert not cur
    else:assert len(cur)==3;words=cur
   reset=[]
   for ss in itertools.product('RL',repeat=2):
    w=''.join(ss)
    if core.trace(w,(0,0),hh)[1:]==(e,h):reset.append(w)
   assert len(reset)==1
   pal[pair][eps]=dict(reset=reset[0],flip=words)
 cases=[];V=S['reverse104'];base,_,_=core.trace(V,(0,0),3)
 for cut in [0,1]:
  W=V[cut:]+V[:cut];start=base[cut][1]
  # Put the bridge away from the period cut. For the last pair, use the
  # cyclic cut two letters later; same literal infinite context.
  for phase in range(0,104,2):
   local=W[phase:]+W[:phase];rr,_,_=core.trace(W,(0,0),start);h=rr[phase][1]
   p0,p1=local[:2],local[2:4]
   for bridge in pal[p0][0]['flip']:
    # Local h differs from normalized N by a proper rotation; turn words
    # and the reset rule are unchanged.
    reset=pal[p1][1]['reset'];word=bridge+reset+local[4:]
    z=periodic(word,h);z.update(cut=cut,pair_phase=phase,bridge=bridge,reset=reset,coarse_word=local,old_unit_alignment=old_alignment(word,local))
    cases.append(z)
 summary=dict(total=len(cases),counts=dict(collections.Counter((z['status']+' old='+str(z['old_unit_alignment'])) for z in cases)),
              survivors=[{k:v for k,v in z.items() if k not in ['complete_histories','conflicts']} for z in cases if z['status']=='LEGAL_PREPARED'])
 out=dict(scope=__doc__,palettes=pal,primitives=primitives,summary=summary,cases=cases,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
 (P/'minimal_pair_heading_bridge.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(summary,indent=2))
if __name__=='__main__':main()

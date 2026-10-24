"""One targeted prepared-wake rewriter architecture, not a free period scan.
Refine each reverse104 read by one legal pose-preserving length1/5/9 word.
Input is the complete mature104 wake profile; output is FREE. Charge is not
preserved by every image. A model is only a periodic bulk interface, no cap.
"""
from pathlib import Path
import sys,json,time,itertools,collections,hashlib
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parents[1]/'periodic_classification_new'))
from probe_one_a_local_constraints import mkconfig,mkcontext,mksolver,inc,parse,solve,getmodel,modelstr,reason,conj,disj
from synthesize_axis_compact_clock import values
from probe_perpendicular_highway_wake import H
from certify_highway_wake_reflector import trace
from search_heading_transport import legal_image
wake=set(map(tuple,json.loads((P/'shifted_reverse104_bulk.json').read_text())['wake_black_classes']))
rev=''.join('L'if c=='R'else'R'for c in H[::-1])
dom={}
for c,target in [('R',(1,0,1)),('L',(-1,0,3))]:
 dom[c]=[w for n in[1,5,9]for z in itertools.product('RL',repeat=n)if legal_image(w:=''.join(z),target)]
def key(p):return(p[0]-p[1],p[0]%2)
def build(translation,kind,timeout=30000):
 start=(-1+translation[0],translation[1]);coarse,endpoint,eh=trace(rev,start,3)
 lines=['(set-logic QF_UF)',f'(set-option :timeout {timeout})','(set-option :produce-models true)']
 add=lambda x:lines.append('(assert '+x+')')
 events=collections.defaultdict(lambda:collections.defaultdict(list))
 for j,(p,h,c)in enumerate(coarse):
  choices=dom[c]if kind=='all'else[w for w in dom[c]if w.count('R')-w.count('L')==(1 if c=='R'else-1)]if kind=='charge'else[c]
  for k,w in enumerate(choices):
   name=f'x{j}_{k}';lines.append(f'(declare-fun {name} () Bool)')
   rows,e,g=trace(w,p,h);assert (e,g)==trace(c,p,h)[1:]
   for i,(q,hh,cc)in enumerate(rows):
    orbit=key(q);long=(q[0]-q[0]%2)//2
    events[orbit][long,j,i,cc].append(name)
  xs=[f'x{j}_{k}'for k in range(len(choices))];add(disj(xs))
  for a,b in itertools.combinations(xs,2):add(f'(not (and {a} {b}))')
 if kind!='identity':add(disj([f'(not x{j}_0)'for j in range(104)]))
 for k,(orbit,ev)in enumerate(sorted(events.items())):
  ev=sorted(ev.items());prev='true'if orbit in wake else'false'
  for i,((long,j,slot,c),xs)in enumerate(ev):
   active=disj(xs);bit=f'b{k}_{i}';lines.append(f'(declare-fun {bit} () Bool)')
   add(f'(=> {active} '+(prev if c=='L'else f'(not {prev})')+')')
   add(f'(= {bit} (xor {prev} {active}))');prev=bit
 return '\n'.join(lines)+'\n',coarse,events

def run(translation,kind):
 text,coarse,events=build(translation,kind);tag=f'reverse_wake_refine_{translation[0]}_{translation[1]}_{kind}';base=P/tag;base.with_suffix('.smt2').write_text(text)
 ctx=mkcontext(mkconfig());s=mksolver(ctx);inc(ctx,s);parse(ctx,s,text.encode());st=time.monotonic();ans=solve(ctx,s)
 out=dict(scope=__doc__,translation=translation,kind=kind,result={1:'SAT_BULK_ONLY',-1:'UNSAT_FAMILY',0:'UNKNOWN'}[ans],seconds=time.monotonic()-st,orbit_classes=len(events),event_slots=sum(map(len,events.values())),timeout_ms=30000)
 if ans==0:out['reason']=reason(ctx,s).decode()
 if ans==1:
  mt=modelstr(ctx,getmodel(ctx,s)).decode();base.with_suffix('.model').write_text(mt);v=values(mt);chosen=[]
  for j,(p,h,c)in enumerate(coarse):
   choices=dom[c]if kind=='all'else[w for w in dom[c]if w.count('R')-w.count('L')==(1 if c=='R'else-1)]if kind=='charge'else[c]
   a=[w for k,w in enumerate(choices)if v[f'x{j}_{k}']];assert len(a)==1;chosen+=a
  w=''.join(chosen);rr,e,h=trace(w,(-1+translation[0],translation[1]),3);assert(e,h)==((-3+translation[0],-2+translation[1]),3)
  prof=collections.defaultdict(list)
  for j,(q,h,c)in enumerate(rr):prof[key(q)].append((j+len(w)*(q[0]//2),c))
  for a,r in prof.items():
   r.sort();assert (r[0][1]=='L')==(a in wake);assert all(x[1]!=y[1]for x,y in zip(r,r[1:]))
  output=wake^{a for a,r in prof.items()if len(r)%2}
  out.update(word=w,images=chosen,length=len(w),charge=w.count('R')-w.count('L'),output_black_classes=sorted(output),literal_orbit_checks=len(prof))
 out['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();base.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out,flush=True)
if __name__=='__main__':
 run((0,0),'identity');run((1,6),'charge');run((1,6),'all')

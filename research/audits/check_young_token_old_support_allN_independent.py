from pathlib import Path
from collections import Counter
from fractions import Fraction
import hashlib,json
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];D=ROOT/'renewal_input_placement_2026-10-23';mp=ROOT/'causal_reduction/unit_scale/prepared1564_uniform_support_manifest.json';J=json.loads(mp.read_text());assert hashlib.sha256(mp.read_bytes()).hexdigest()=='90fcf1a66046418c38d07f7e935ea80cf873751aefae69a4b07af89ba3bd8399'
p=SELF.parent/'check_serial_bridge_archive_independent.py';ns={'__file__':str(p)};exec(p.read_text().split('# Fixed local masks')[0],ns);ends,graph,component,wvertex=[ns[k]for k in('ends','graph','component','wvertex')]
def tr(w,h):
 p=0j;out=[]
 for ch in w:out.append((p,h,ch));h=(h+(1 if ch=='R'else-1))%4;p+=1j*(-1j)**h
 return out,p,h
stages=[]
for i,s in enumerate(J['stages']):
 word=s['word'][:126]if i==15 else s['word'];tt,delta,eh=tr(word,s['heading']);stages.append((s,tt,delta,eh))
 if i<15:
  if s['kind']=='H':assert len(word)==104 and eh==s['heading']and abs(delta.real)==2 and abs(delta.imag)==2
  else:assert s['count_N_constant']==[0,1]
  nxt=J['stages'][i+1];cnt=s['count_N_constant'];assert[nxt['start_time_N_constant'][k]-s['start_time_N_constant'][k]for k in(0,1)]==[len(word)*c for c in cnt]
  assert[nxt['start_x_N_constant'][k]-s['start_x_N_constant'][k]for k in(0,1)]==[int(delta.real)*c for c in cnt]
  assert[nxt['start_y_N_constant'][k]-s['start_y_N_constant'][k]for k in(0,1)]==[int(delta.imag)*c for c in cnt]
  assert nxt['heading']==eh
s,tt,de,eh=stages[-1];assert de-6-6j==3-17j and eh==0 and s['word'][126]=='L';now=(24024,91873);beta=(21112,80557);target=3-17j
assert wvertex(target,0)==7-35j and int((5-33j).real+(5-33j).imag)%4==0
k=0
C={-2-16j,-1-17j,-1-16j,-19j,-18j,1-19j,1-18j,1-17j,2-19j,2-18j,2-17j}
cycle=[3-17j,2-17j,1-18j,-18j,-1-17j,-1-16j,-1-15j,-1-14j,-1-13j,-1-12j,-11j,1-11j,2-12j,3-13j,4-14j,5-15j,5-16j,4-17j]
u,v=ends(target,k);u,v=(u,v)if u==5-33j else(v,u);assert v==7-35j
verts=set(graph(C,k));assert len(C)==len(verts)==11 and component(C,k,u)[1]==C and v not in verts
ports=set()
for z in verts:
 for diag in(1+1j,1-1j,-1+1j,-1-1j):
  cell=(z+diag)/2
  if z in ends(cell,k):ports.add(cell)
assert len(ports)==31 and target in ports
cg=graph(set(cycle),k);assert len(cg)==len(cycle)==18 and all(len(es)==2 for es in cg.values())and component(set(cycle),k,u)[1]==set(cycle)
queries=ports|set(cycle);assert len(queries)==42
# Exact integer half-lines/equalities, no bounded parameter sampling.
def ge(dom,a,b):
 if dom is None:return None
 lo,hi=dom
 if a==0:return dom if b>=0 else None
 if a>0:lo=max(lo,-(b//a))
 else:
  bound=b//(-a);hi=bound if hi is None else min(hi,bound)
 return None if hi is not None and lo>hi else(lo,hi)
def eq(dom,a,b):return ge(ge(dom,a,b),-a,-b)
def dominates(a,b,dom):
 d=(a[0]-b[0],a[1]-b[1]);lo,hi=dom
 return d[0]*lo+d[1]>=0 if d[0]>=0 else hi is not None and d[0]*hi+d[1]>=0
def families(q):
 result=[]
 for si,(s,tt,delta,eh)in enumerate(stages):
  sx,sy,st=[s[a]for a in('start_x_N_constant','start_y_N_constant','start_time_N_constant')]
  for i,(p,h,ch)in enumerate(tt):
   dom=(1,None)
   if s['kind']=='H':
    a=Fraction(-sx[0],int(delta.real));b=Fraction(int(q.real)-sx[1]-int(p.real),int(delta.real));assert a.denominator==1
    if b.denominator!=1:continue
    a,b=int(a),int(b);dom=eq(dom,sy[0]+a*int(delta.imag),sy[1]+int(p.imag)+b*int(delta.imag)-int(q.imag))
    dom=ge(dom,a,b);cnt=s['count_N_constant'];dom=ge(dom,cnt[0]-a,cnt[1]-b-1)
    time=(st[0]+104*a,st[1]+104*b+i);copy=(a,b)
   else:
    dom=eq(dom,sx[0],sx[1]+int(p.real)-int(q.real));dom=eq(dom,sy[0],sy[1]+int(p.imag)-int(q.imag));time=(st[0],st[1]+i);copy=(0,0)
   if dom is not None:result.append((si,i,ch,copy,time,dom))
 return result
ref=json.loads((D/'all_n_young_token_old_support_certificate.json').read_text());rqueries={complex(*r['cell']):r for r in ref['queries']};results={};nfamily=0
for q in queries:
 fs=families(q);nfamily+=len(fs);refset={(f['stage'],f['slot'],f['turn'],tuple(f['copy_N_constant']),tuple(f['time_N_constant']),tuple(f['domain_N']))for f in rqueries[q]['families']};assert set(fs)==refset
 if not fs:results[q]=(False,None,None);continue
 eligible=[f for f in fs if f[5][0]==1];winner=max(eligible,key=lambda f:sum(f[4]));assert winner[5]==(1,None)
 for f in fs:assert dominates(winner[4],f[4],f[5])
 ch=winner[2];time=winner[4];young=ch=='R'and dominates(time,(beta[0],beta[1]+1),(1,None))
 if ch=='R'and not young:assert dominates(beta,time,(1,None))
 assert rqueries[q]['young']==young
 assert rqueries[q]['last_read']['time_N_constant']==list(time)
 results[q]=(young,ch,time)
assert nfamily==226
assert all(results[q][0]for q in C)and all(not results[q][0]for q in ports-C-{target})
for q in cycle:assert results[q][1]=='R'and dominates(results[q][2],beta,(1,None))
assert results[-1-15j][2]==beta and results[target][2]==(24024,91857)
assert tuple(now[i]-results[target][2][i]for i in(0,1))==(0,16)
assert tuple(now[i]-beta[i]for i in(0,1))==(2912,11316)
# Independent finite literal ownership check for a NON-discovery parameter, using the complete184 seed.
N=2;B={complex(x[0]*N+x[1],y[0]*N+y[1])for x,y in J['seed_families']};assert len(B)==184;birth={q:-1 for q in B};p0=J['initial_pose'];p=complex(p0['x_N_constant'][0]*N+p0['x_N_constant'][1],p0['y_N_constant'][0]*N+p0['y_N_constant'][1]);h=p0['heading'];t=0
for si,(s,tt,delta,eh)in enumerate(stages):
 cnt=s['count_N_constant'][0]*N+s['count_N_constant'][1]if s['kind']=='H'else 1
 word=s['word'][:126]if si==15 else s['word']
 assert p==complex(s['start_x_N_constant'][0]*N+s['start_x_N_constant'][1],s['start_y_N_constant'][0]*N+s['start_y_N_constant'][1])and h==s['heading']and t==s['start_time_N_constant'][0]*N+s['start_time_N_constant'][1]
 for _ in range(cnt):
  for ch in word:
   assert('L'if p in B else'R')==ch
   if ch=='L':B.remove(p);del birth[p]
   else:B.add(p);birth[p]=t
   h=(h+(1 if ch=='R'else-1))%4;p+=1j*(-1j)**h;t+=1
assert(p,h,t)==(target,0,now[0]*N+now[1])
young={q for q in B-{target}if birth[q]>beta[0]*N+beta[1]};assert component(young,k,u)[1]==C
for q,(yy,ch,time)in results.items():
 if time is not None:
  assert(q in B)==(ch=='R')
  if ch=='R':assert birth[q]==time[0]*N+time[1]
sha=hashlib.sha256((D/'YOUNG_TOKEN_OLD_SUPPORT.md').read_bytes()).hexdigest();assert sha=='195ea0ed9e56fafc9625973aa095cfa66792bb81ea8ac894d0f7dc06601099c7'
out={'status':'PASS all-N young-token / indispensable old-cycle-support countercontrol','note_sha256':sha,'source_manifest_sha256':hashlib.sha256(mp.read_bytes()).hexdigest(),'literal_stage_count':16,'query_cells':42,'exact_read_families':226,'closed_strict_young_component_edges':11,'complete_incident_ports':31,'simple_cycle_edges':18,'independent_full_seed_control_N':N,'independent_literal_reads':t,'current_time_N_constant':now,'target_birth_N_constant':results[target][2],'exact_maximin_cycle_birth_N_constant':beta,'deleted_age':16,'necessary_oldest_cycle_support_age_N_constant':[2912,11316],'analytic':['Every stage word is reconstructed geometrically, with exact affine start/end pose and clock continuity. All standard flights have drift +/-2 and integral copy slopes, so no congruence class is silently removed. Each of226 possible read families is solved over its entire exact integer N domain; the chosen winner is eligible for all N>=1 and dominates every family on that family domain. The all-N claim does not come from the finite control.','The11 strict-young component edges are connected, omit the opposite target endpoint, and have exactly31 incident physical cell ports. Each other port is proven white or old at every N, except the deliberately removed target. Thus the ENTIRE strict-young graph has no bypass, regardless of remote archives. Unread original cells have birth-1 and cannot be strict-young.','The18-edge simple cycle is wholly black with every current birth>=beta, including an exact-beta edge. Combined with the strict-young no-bypass upper certificate, max over cycles through the target of minimum edge birth equals beta exactly. This accounts for every possible alternative cycle, not merely the displayed witness.','The consumed R-born lifetime always has age16, while every supporting cycle needs a current lifetime of age>=2912N+11316. Initial complete mass remains184 and the retained family is bi-standard. Hence no finite bound depending only on initial mass and consumed-token age can control required cycle-support age.'],'scope':'A genuine finite all-N family; no infinite anomalous orbit, capture counterexample, monotone support-age law or arbitrary-word classification.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(t)

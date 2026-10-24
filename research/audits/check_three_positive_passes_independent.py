from pathlib import Path
from collections import defaultdict,Counter
import json,gzip,hashlib
S=Path(__file__).resolve();R=S.parents[1];P=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=json.loads((P/'THREE_PASS_AUTHOR_MANIFEST.json').read_text())
for f,h in mf['files'].items():assert sha(P/f)==h,(f,sha(P/f))
cert=json.loads((P/'THREE_POSITIVE_PASSES_CERTIFICATE.json').read_text());ref=json.loads((P/'THREE_POSITIVE_PASSES_CHECKED.json').read_text());regen=json.loads((P/'REGENERATION_BOUNDARY_CHECKED.json').read_text());V=(1j,1,-1j,-1)
xy=lambda q:(int(q.real),int(q.imag));cells=lambda a:set(map(tuple,a));cp=lambda p:complex(*p)
def ends(e,lat):
 x,y=e;v=[(2*x+a,2*y+b)for a in(-1,1)for b in(-1,1)if(2*x+a+2*y+b)%4==lat];assert len(v)==2;return tuple(v)
class G:
 def __init__(self,B,lat):
  self.lat=lat;self.adj=defaultdict(dict)
  for q in B:self.add(q)
 def add(self,q):
  u,v=ends(q,self.lat);assert v not in self.adj[u];self.adj[u][v]=q;self.adj[v][u]=q
 def remove(self,q):
  u,v=ends(q,self.lat);assert self.adj[u][v]==q;del self.adj[u][v];del self.adj[v][u]
 def component(self,u,skip=None):
  seen={u};todo=[u];es=set()
  for v in todo:
   for w,q in self.adj[v].items():
    if q==skip:continue
    es.add(q)
    if w not in seen:seen.add(w);todo.append(w)
  return seen,es
 def connected_without(self,q,skip):
  u,v=ends(q,self.lat);return v in self.component(u,q if skip else None)[0]
 def rank(self,B):
  rest=set(B);C=0;verts=set()
  while rest:
   q=next(iter(rest));vs,es=self.component(ends(q,self.lat)[0]);rest-=es;verts|=vs;C+=1
  return len(B)-len(verts)+C
 def edge_components(self,B):
  rest=set(B);cs=[]
  while rest:
   q=next(iter(rest));es=self.component(ends(q,self.lat)[0])[1];rest-=es;cs.append(es)
  return cs

def current_cursors(p,h):return xy(2*p+(1-1j)*(-1j)**h),xy(2*p+(-1-1j)*(-1j)**h)
def digest(B):return hashlib.sha256(json.dumps(sorted(B),separators=(',',':')).encode()).hexdigest()
stream=gzip.open(P/'THREE_POSITIVE_PASSES_FULL_COMPONENTS.jsonl.gz','rt');results=[]
for c,r,rg in zip(cert['cases'],ref['cases'],regen['cases']):
 q=c['q'];assert q==r['q']==rg['q'];B=cells(c['initial_black']);baseline=cells(c['baseline_black']);extra=cells(c['additional_initial_black']);assert not(baseline&extra)and B==baseline|extra and len(B)==len(c['initial_black'])
 p=cp(c['initial_pose'][0]);h=c['initial_pose'][1];assert(p,h)==(1+1j,1);w,z=current_cursors(p,h);graphs=[G(B,sum(w)%4),G(B,sum(z)%4)];assert [g.rank(B)for g in graphs]==[2,0]
 birth={x:('baseline'if x in baseline else'added',-1)for x in B};born={};seen=set();firstextra={x:None for x in extra};t=0;runR=0;stages=[];componenthash=hashlib.sha256();maxactive=[0,0]
 assert c['baseline_prefix_word']==''.join(s['word']for s in c['stages'][:3])
 def checkcut():
  w,z=current_cursors(p,h);comps=[g.component(u)[1]for g,u in zip(graphs,(w,z))];rr=json.loads(next(stream));assert rr=={'q':q,'cut':t,'pose':[list(xy(p)),h],'full_active_w':[list(x)for x in sorted(comps[0])],'full_active_z':[list(x)for x in sorted(comps[1])]}
  componenthash.update((json.dumps(rr,separators=(',',':'))+'\n').encode())
  for i,x in enumerate(comps):maxactive[i]=max(maxactive[i],len(x))
 for si,stage in enumerate(c['stages']):
  nm=stage['name'];rs=r['stages'][si];assert nm==rs['name'];m0=len(B);entry=[list(xy(p)),h];rankin=[g.rank(B)for g in graphs];deaths=Counter();be=[0,0];de=[0,0];events=[];counts=Counter();born[nm]=set()
  for j,ch in enumerate(stage['word']):
   checkcut();e=xy(p);assert ch==('L'if e in B else'R'),(q,nm,j,e);counts[ch]+=1;seen.add(e)
   if e in extra and firstextra[e]is None:firstextra[e]=t
   if si<3:assert e not in extra
   if ch=='L':
    cyc=[g.connected_without(e,True)for g in graphs];ex=runR>=3 or cyc[0]
    if ex:events.append({'offset':j,'r':runR,'cell':list(e),'w_nonbridge':cyc[0]})
    if si in(0,2,4):assert not ex and runR<=2
    origin,b=birth.pop(e);deaths[origin]+=1;B.remove(e)
    for i,g in enumerate(graphs):g.remove(e);de[i]+=int(cyc[i])
    h=(h-1)%4;runR=0
   else:
    cyc=[g.connected_without(e,False)for g in graphs];B.add(e);birth[e]=(nm,t);born[nm].add((e,t))
    for i,g in enumerate(graphs):g.add(e);be[i]+=int(cyc[i])
    h=(h+1)%4;runR+=1
   p+=V[h];t+=1
  assert runR==0 and stage['word'][-1]=='L';active_labels={(e,b)for e,(o,b)in birth.items()}
  if si==0:assert deaths=={'baseline':counts['L']}
  if si==1:assert born[c['stages'][0]['name']]<=active_labels and len(events)==2
  if si==2:assert not(born[c['stages'][0]['name']]&active_labels)
  if si==3:assert born[c['stages'][2]['name']]<=active_labels and len(events)==2 and(xy(p),h)==((2,4),1)
  n=c['n'];assert n==12*((q+1)//2)**2
  if si==4:
   assert deaths=={'second_positive_ordinary':2*n+3*q-7,'added':q-1};assert counts=={'L':2*n+4*q-8,'R':2*n+5*q-10}
  own={'name':nm,'duration':len(stage['word']),'entry_pose':entry,'exit_pose':[list(xy(p)),h],'R':counts['R'],'L':counts['L'],'gain':len(B)-m0,'deaths_by_origin':dict(deaths),'w_exceptions':events,'cycle_births_w_z':be,'cycle_erasures_w_z':de,'ranks_in':rankin,'ranks_out':[g.rank(B)for g in graphs],'full_field_sha256':digest(B),'full_field':[list(x)for x in sorted(B)]}
  assert own==rs,(q,nm,'stage mismatch');stages.append({k:v for k,v in own.items()if k not in('full_field','w_exceptions')})
 checkcut();assert componenthash.hexdigest()==r['full_component_stream_sha256'];assert t+1==r['full_component_cut_count'];assert [[list(x),firstextra[x]]for x in sorted(extra)]==r['additional_initial_cell_first_reads']
 assert [list(x)for x in sorted(B)]==r['full_final_field']and[list(xy(p)),h]==r['final_pose'];assert [[list(x),o,b]for x,(o,b)in sorted(birth.items())]==r['full_final_lifetime_labels']
 second=born['second_positive_ordinary'];remaining=second&{(e,b)for e,(o,b)in birth.items()};assert len(remaining)==5 and [[list(e),b]for e,b in sorted(remaining)]==r['remaining_second_lifetimes']
 assert len([e for e,(o,b)in birth.items()if o=='added'])==len([e for e,(o,b)in birth.items()if o=='baseline'])==3
 assert len(B)==len(c['initial_black'])+q+6 and t==20*n+21*q+56 and len(extra)==2*n+15*q-8 and len(c['initial_black'])==6*n+6*q+35
 # Reconstruct ALL one-unit missing edges connecting two third-cohort degree-one tips.
 A3={e for e,(o,b)in birth.items()if o=='third_positive_ordinary'};degree=Counter(v for e in A3 for v in ends(e,graphs[0].lat));tips=[v for v,d in degree.items()if d==1];joins=set()
 for i,u in enumerate(tips):
  for v in tips[i+1:]:
   if abs(u[0]-v[0])==abs(u[1]-v[1])==2:
    e=((u[0]+v[0])//4,(u[1]+v[1])//4)
    if e not in A3:assert set(ends(e,graphs[0].lat))=={u,v};joins.add(e)
 assert len(joins)==q-1 and not(joins&B)and not(joins&seen) and joins==cells(rg['next_direct_stitches'])
 # Exact repeated protocol is not a reusable block: evaluate minimum first-read obligations.
 pp=p;hh=h;first=set();bad=[]
 for j,ch in enumerate(c['stages'][3]['word']+c['stages'][4]['word']):
  e=xy(pp)
  if e not in first:
   first.add(e)
   if (e in B)!=(ch=='L'):bad.append({'offset':j,'cell':list(e),'required':ch,'current':'L'if e in B else'R'})
  hh=(hh+(1 if ch=='R'else-1))%4;pp+=V[hh]
 assert bad==rg['pose_compatible_repetition']['minimal_first_read_guard_violations']and min(z['offset']for z in bad)==1
 cs=graphs[0].edge_components(B);assert {frozenset(x)for x in cs}=={frozenset(map(tuple,z['edges']))for z in rg['complete_final_w_components']}
 # Actual following RRL has w-nonbridge L, proving the third epoch's RIGHT boundary.
 assert c['following_exception_word']=='RRL'
 for j,ch in enumerate('RRL'):
  e=xy(p);assert ch==('L'if e in B else'R')
  if ch=='R':B.add(e);[g.add(e)for g in graphs];h=(h+1)%4
  else:assert graphs[0].connected_without(e,True);B.remove(e);[g.remove(e)for g in graphs];h=(h-1)%4
  p+=V[h]
 results.append({'q':q,'initial_mass':len(c['initial_black']),'extra_mass':len(extra),'duration':t,'complete_cut_count':t+1,'max_active_w_z':maxactive,'stage_summaries':stages,'second_R_remaining':len(remaining),'next_direct_stitches':sorted(joins),'repeated_protocol_first_guard_failure':bad[0]});print('verified q',q,'duration',t,flush=True)
assert not stream.read();stream.close()
out={'status':'PASS four literal finite three-positive-ordinary-pass controls, NOT all-q or regeneration','source_bindings':mf['files'],'cases':results,'analytic_scope':[
'Every initial black cell is included before time0. Extra guide and stitch cells are physically unread during the original entire two-positive-pass prefix, and independently both complete graph checks retain every required ordinary w bridge. No word-preservation shortcut establishes topology.',
'Each literal read, all stage fields, every fine-cut COMPLETE w/z active component, all cycle births/erasures and genuine R-lifetime ownership were independently replayed without importing discovery geometry. All five stages follow the same moving ant. Second return reaches the actual third-entry pose, not a reset.',
'The first R cohort survives the first charged return and is fully consumed in the second ordinary epoch. The complete second R cohort survives the second return; the third ordinary epoch consumes exactly all but five of it plus q-1 old charged stitches and nothing else. Every positive stage has gainq-2; r<=2 and w bridge at each L. Third is preceded by the final exceptional R4L of the second return and ends before actual nonbridge RRL. Thus it is a maximal ordinary epoch, not a favorable subinterval.',
'The third stage has substantial opposite-graph births/erasures and may create a w cycle while every L stays w-bridge. No paired-forest claim is made. All surviving old and R-born material stays in the complete field.',
'Only the four supplied q3/5/7/9 seeds are certified. Almost all added guide lifetimes are spent, with three remaining old-cycle cells. The next direct q-1 stitches are white and unread, and exact pose-compatible return-word repetition fails at read2. This does not exclude another repair/route; it does not supply repeatable regeneration, an all-q construction, asymptotic gain, infinite countertrajectory or attraction theorem.'
]};S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])

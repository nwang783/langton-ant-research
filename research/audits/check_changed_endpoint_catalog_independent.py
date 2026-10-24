from pathlib import Path
from collections import defaultdict,Counter
import json,hashlib
P=Path(__file__).resolve();S=P.with_name('check_endpoint_catalog_independent.py');exec(compile(S.read_text().split('reports=json.loads')[0],str(S),'exec'))
original=json.loads((R/'endpoint_catalog_results.json').read_text());backs={tuple(r['channel']):r for r in original['results']if r['drift']==[2,2]}
report=json.loads((R/'changed_endpoint_catalog_results.json').read_text());capsup={tuple(c['normalization']['source_channel']):c for c in report['cap_results']};assert set(capsup)==set(backs)
def replay(rays,finite,p,h,length,record=False):
 path=[];word=[]
 for _ in range(length):
  if record:path.append(p)
  c='L'if color(p,rays,finite)else'R';word.append(c);finite.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=dirs[h]
 return p,h,path,''.join(word)
def make_changed(ch):
 oldrow=backs[ch];rays,p,h,_,_=background(ch);F=set(cap);p,h,_,_=replay(rays,F,p,h,oldrow['entry']);assert [list(xy(p)),h]==oldrow['pose'];assert certify(rays,F,p,h,oldrow['tail_word'])[0]
 odd=set();pp=p;hh=h
 for c in oldrow['tail_word']:
  odd.symmetric_difference_update({pp});hh=(hh+(1 if c=='R'else-1))%4;pp+=dirs[hh]
 assert pp-p==-d and hh==h
 rr={cl:set(v)for cl,v in rays.items()}
 for q in odd:
  cl,k=old(q);rr.setdefault(cl,set()).symmetric_difference_update({k})
 oddclasses={cl for cl,v in rr.items()if len(v)%2};assert len(oddclasses)==48
 # Independently evaluate finite difference from the normalized threshold at EVERY level between min/max thresholds.
 norm={cl:[0]for cl in oddclasses};C=set(F)
 for (t,a),v in rr.items():
  if not v:continue
  lo=min(min(v),0);hi=max(max(v),0)
  for k in range(lo,hi+1):
   if(sum(k<=b for b in v)%2)^((t,a)in oddclasses and k<=0):C.symmetric_difference_update({complex(a-2*k,a-2*k-t)})
 meta=capsup[ch]['normalization'];assert C=={complex(*q)for q in meta['cap']};assert odd=={complex(*q)for q in meta['returned_odd_read_mask']};assert oddclasses==set(map(tuple,meta['odd_profiles']));assert len(C)==meta['mass']
 assert hashlib.sha256(json.dumps(sorted(map(xy,C)),separators=(',',':')).encode()).hexdigest()==meta['cap_sha256']
 assert [min(int(q.real-q.imag)for q in C),max(int(q.real-q.imag)for q in C)]==meta['t_hull']
 return norm,C

def newchannels(rows,C):
 cs={old(q)[0]for q in C};lo=min(t for t,a in cs)+18;hi=max(t for t,a in cs)+28
 return [(delta,a)for delta in range(lo,hi+1)if delta%2==0 for a in(0,1)if not({(t+delta,(b+a)%2)for t,b in rclasses}&rows.keys())and({(t+delta,(b+a)%2)for t,b in rclasses}&cs)]
def incoming(rows,C,ch):
 delta,a=ch;tr=complex(a,a-delta);rs=[q+tr for q in reads]
 hits=[(104*n+i,q,i)for q in C for i,s in enumerate(rs)if(n:=along(q,s,d))is not None]
 tau,p,phi=min(hits,key=lambda z:z[0]);assert sum(t==tau for t,_,_ in hits)==1
 rr={cl:set(v)for cl,v in rows.items()}
 for i,q in enumerate(rs):
  cl,k=old(q);rr.setdefault(cl,set()).symmetric_difference_update({k+(tau-1-i)//104})
 return {cl:sorted(v)for cl,v in rr.items()if v},p,heads[phi],tau,phi
results=[];nchecks=0;steps=0;width=None
for source in sorted(backs):
 rows,C=make_changed(source);chs=newchannels(rows,C);sup={tuple(r['channel']):r for r in capsup[source]['results']};assert set(chs)==set(sup);counts=Counter();records=[]
 for n,ch in enumerate(chs):
  rr,p,h,tau,phi=incoming(rows,C,ch);incomingword=H[phi:]+H[:phi];assert certify(rr,set(),p,h,incomingword)[0];assert not certify(rr,{p+1000000*d},p,h,incomingword)[0]
  r=sup[ch];F=set(C);pp=p;hh=h;p,h,path,trace=replay(rr,F,p,h,r['entry'],True);steps+=r['entry']
  assert [list(xy(p)),h]==r['pose'];assert len(F)==r['finite_XOR_mass'];digest=hashlib.sha256(json.dumps(sorted(map(xy,F)),separators=(',',':')).encode()).hexdigest();assert digest==r['finite_XOR_sha256'];assert trace[-208:]==r['tail_word']*2
  ok,nc=certify(rr,F,p,h,r['tail_word']);assert ok,(source,ch);nchecks+=nc
  # Exact K uses actual ten-read past and ten-read future seam.
  hist=''.join(H[(tau-10+j)%104]for j in range(10));prev=hist not in factor10;kc=0
  _,_,_,tail10=replay(rr,set(F),p,h,10)
  for c in trace+tail10:
   hist=(hist+c)[-10:];b=hist not in factor10;kc+=prev and b;prev=b
  assert kc==r['K_total'];hull=[min(int(q.real-q.imag)for q in path),max(int(q.real-q.imag)for q in path)];assert hull==r['reaction_read_t_hull']
  counts[tuple(r['drift'])]+=1;records.append(dict(channel=ch,entry=r['entry'],drift=r['drift'],K=kc,whole_field_hash=digest,future_critical_checks=nc))
  if source==(34,1)and ch==(50,0):
   assert r['entry']==23296 and(p,h)==(71+11j,0)
   ext={59+11j,66+4j,67+3j,68+2j} # replace below with exact signed coordinates
   ext={complex(59,-11),complex(66,-4),complex(67,-3),complex(68,-2)}
   assert all(color(q,rr,F)for q in ext)
   _,_,tailpath,_=replay(rr,set(F),p,h,104,True);th=[min(int(q.real-q.imag)for q in tailpath),max(int(q.real-q.imag)for q in tailpath)];assert th==[56,66]
   # A fixed old extreme is an actual black and untouched by incoming/reaction/outgoing strips.
   oldext=[q for q in C if int(q.real-q.imag)==-82 and color(q,rows,C)];assert oldext and all(q not in path for q in oldext)
   allnorms={t for(t,a),v in rr.items()if len(v)%2}|{int(q.real-q.imag)for q in F if color(q,rr,F)}
   assert min(allnorms)==-82 and max(allnorms)==70
   width=dict(source=source,incoming=ch,old_hull=[-82,56],new_hull=[-82,70],permanent_new_blacks=sorted(map(xy,ext)),old_extremes=sorted(map(xy,oldext)),outgoing_read_hull=th,K=kc,scope='Supplied infinite changed endpoint, not a finite-seed itinerary or repeatability claim.')
  if(n+1)%20==0:print(source,n+1,'PASS',flush=True)
 assert len(chs)=={(-12,0):80,(26,0):68,(34,1):64}[source]
 assert counts=={(-12,0):{(-2,-2):15,(2,-2):41,(-2,2):23,(2,2):1},(26,0):{(-2,-2):48,(2,-2):18,(-2,2):1,(2,2):1},(34,1):{(-2,-2):25,(2,-2):35,(-2,2):3,(2,2):1}}[source]
 results.append(dict(source=source,cap_mass=len(C),channels=len(chs),output_counts={str(k):v for k,v in counts.items()},results=records))
assert width and sum(r['channels']for r in results)==212
out=dict(status='PASS independently reconstructed changed fields, exhaustive second channels and all future certificates',note_sha256=hashlib.sha256((R/'changed_endpoint_catalog_and_width_control.md').read_bytes()).hexdigest(),literal_updates=steps,future_critical_checks=nchecks,controls=424,results=results,width_control=width,scope='All212 explicitly supplied changed infinite-endpoint states capture. Original catalogue is not reset/reused. Fourteen-level widening is one real local response, not an arbitrary finite-seed itinerary, repeatability or amortized-width impossibility.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k!='results'})

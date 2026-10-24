#!/usr/bin/env python3
"""Exact changed endcaps, after each of three back-reflecting first-endcap reactions.
All inherited half-rays and complete changed XOR fields retained. No iteration claim.
"""
from pathlib import Path
from collections import defaultdict,Counter
import runpy,json,hashlib,time,argparse
ROOT=Path(__file__).parent
E=runpy.run_path(str(ROOT/'endpoint_catalog.py'))
H,PER,V,d,PH,HD=(E[x]for x in ['H','PER','V','d','PH','HD'])
old_orbit,along,row_color,initial_color,certify=(E[x]for x in ['old_orbit','along','row_color','initial_color','certify'])
FACTORS,ROTATIONS,RORB=(E[x]for x in ['FACTORS','ROTATIONS','RORB'])
def toggle(F,q):
 if q in F:F.remove(q)
 else:F.add(q)
def add_threshold(rows,j,k):
 r=rows.setdefault(j,set());toggle(r,k)
 if not r:del rows[j]
def parse_rows(rows):return{j:set(rr)for j,rr in rows.items()}
def advance(rows,F,p,h,n):
 read=[]
 for _ in range(n):
  read.append(p);ch='L'if initial_color(p,rows,F)else'R';toggle(F,p);h=(h+(-1 if ch=='L'else 1))%4;v=V[h];p=(p[0]+v[0],p[1]+v[1])
 return p,h,read

def normalized_endcap(result):
 rows,F,p,h,tau,phi=E['make_initial'](result['channel'])
 p,h,read=advance(rows,F,p,h,result['entry']);assert [list(p),h]==result['pose']
 assert certify(rows,F,p,h,result['tail_word'])
 rows=parse_rows(rows);pp=p;hh=h;odd=set()
 for ch in result['tail_word']:
  toggle(odd,pp);hh=(hh+(-1 if ch=='L'else 1))%4;v=V[hh];pp=(pp[0]+v[0],pp[1]+v[1])
 assert hh==h and (pp[0]-p[0],pp[1]-p[1])==(-d[0],-d[1]);assert len(odd)>0
 # At infinite clean escape, append EVERY outgoing odd read copy i>=0.
 for q in odd:
  j,k=old_orbit(q);add_threshold(rows,j,k)
 odd_profiles={j for j,rr in rows.items()if len(rr)%2};assert len(odd_profiles)==48
 # Fixed canonical backward rays k<=0. Collect exact finite coboundary.
 cap=set(F)
 for j,rr in rows.items():
  ts=set(rr)
  if len(rr)%2:toggle(ts,0)
  assert len(ts)%2==0
  if not ts:continue
  tt=sorted(ts)
  # XOR half-rays k<=b; two endpoints b0<b1 produce b0<k<=b1.
  t,a=j
  for lo,hi in zip(tt[::2],tt[1::2]):
   for k in range(lo+1,hi+1):toggle(cap,(a-2*k,a-2*k-t))
 base_rows={j:[0]for j in odd_profiles}
 # Verify all critical intervals and finite exceptions exactly, not a horizon test.
 critical=defaultdict(set)
 for j,rr in rows.items():critical[j].update(rr)
 for q in F|cap:
  j,k=old_orbit(q);critical[j].update([k-1,k,k+1])
 for j in odd_profiles:critical[j].update([-1,0,1])
 checks=0
 rr={j:sorted(v)for j,v in rows.items()}
 for (t,a),ks in critical.items():
  ks.update([min(ks)-1,max(ks)+1])
  for k in ks:
   q=(a-2*k,a-2*k-t);assert initial_color(q,rr,F)==initial_color(q,base_rows,cap);checks+=1
 return base_rows,cap,{'source_channel':result['channel'],'odd_profiles':sorted(odd_profiles),'cap':sorted(cap),'mass':len(cap),'t_hull':[min(x-y for x,y in cap),max(x-y for x,y in cap)],'normalization_checks':checks,'cap_sha256':hashlib.sha256(json.dumps(sorted(cap),separators=(',',':')).encode()).hexdigest(),'returned_odd_read_mask':sorted(odd)}

def channels_for(rows,cap):
 profiles=set(rows);corb={old_orbit(q)[0]for q in cap};lo,hi=min(t for t,a in corb),max(t for t,a in corb)
 out=[]
 for delta in range(lo+18,hi+29):
  if delta%2:continue
  for a in [0,1]:
   read={(t+delta,(b+a)%2)for t,b in RORB}
   if read.isdisjoint(profiles)and read&corb:out.append((delta,a))
 return out

def incoming(rows,cap,channel,with_cap=True):
 delta,a=channel;tr=(a,a-delta);rel=[(x+tr[0],y+tr[1])for x,y in PH];hits=[]
 for q in cap:
  for i,s in enumerate(rel):
   n=along(q,s,d)
   if n is not None:hits.append((n*PER+i,q,i))
 tau,p,phi=min(hits);rs=parse_rows(rows)
 for i,s in enumerate(rel):
  j,k=old_orbit(s);add_threshold(rs,j,k+(tau-i-1)//PER)
 return{j:sorted(v)for j,v in rs.items()},set(cap)if with_cap else set(),p,HD[phi],tau,phi

def solve(rows,cap,channel,limit):
 rows,F,p,h,tau,phi=incoming(rows,cap,channel);hist=''.join(H[(tau-10+j)%PER]for j in range(10));bad0=hist not in FACTORS;K=0;recent='';attempts=0;tlo=thi=p[0]-p[1]
 for t in range(limit+1):
  if t>=208 and t%104==0 and recent[:104]==recent[104:]and recent[104:]in ROTATIONS:
   word=recent[104:];attempts+=1;cert=certify(rows,F,p,h,word)
   if cert:
    ff=set(F);pp=p;hh=h;history=hist;extra=0;prev=bad0
    for _ in range(10):
     ch='L'if initial_color(pp,rows,ff)else'R';history=(history+ch)[-10:];bad=history not in FACTORS;extra+=bad and prev;prev=bad;toggle(ff,pp);hh=(hh+(-1 if ch=='L'else 1))%4;v=V[hh];pp=(pp[0]+v[0],pp[1]+v[1])
    return {'channel':channel,'status':'CERTIFIED','entry':t,'pose':[list(p),h],**cert,'tail_word':word,'K_total':K+extra,'finite_XOR_mass':len(F),'finite_XOR_sha256':hashlib.sha256(json.dumps(sorted(F),separators=(',',':')).encode()).hexdigest(),'reaction_read_t_hull':[tlo,thi],'attempts':attempts}
  if t==limit:break
  tlo=min(tlo,p[0]-p[1]);thi=max(thi,p[0]-p[1]);ch='L'if initial_color(p,rows,F)else'R';hist=(hist+ch)[-10:];bad=hist not in FACTORS;K+=bad and bad0;bad0=bad;recent=(recent+ch)[-208:];toggle(F,p);h=(h+(-1 if ch=='L'else 1))%4;v=V[h];p=(p[0]+v[0],p[1]+v[1])
 return {'channel':channel,'status':'UNKNOWN','limit':limit,'K_observed':K,'finite_XOR_mass':len(F),'reaction_read_t_hull':[tlo,thi],'attempts':attempts}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--limit',type=int,default=300000);args=ap.parse_args();started=time.time();original=json.loads((ROOT/'endpoint_catalog_results.json').read_text())['results'];back=[r for r in original if r.get('drift')==[2,2]];out={'scope':'Exact changed-endcap local scattering; all48 half-wake profiles and full changed cap retained. No two-cap repeatability or finite-family transfer claim.','cap_results':[]}
 for source in back:
  rows,cap,meta=normalized_endcap(source);chs=channels_for(rows,cap);print('CAP',source['channel'],meta['mass'],meta['t_hull'],'CHANNELS',len(chs),flush=True);capout={'normalization':meta,'channel_count':len(chs),'controls':0,'results':[]};out['cap_results'].append(capout)
  for i,ch in enumerate(chs):
   rr,ff,p,h,tau,phi=incoming(rows,cap,ch,False);word=H[phi:]+H[:phi];assert certify(rr,ff,p,h,word);q=(p[0]+1000000*d[0],p[1]+1000000*d[1]);
   # pick first fresh read along a full future period
   pp=p;hh=h
   for turn in word:
    cand=(pp[0]+1000000*d[0],pp[1]+1000000*d[1])
    if not initial_color(cand,rr,ff):q=cand;break
    hh=(hh+(-1 if turn=='L'else 1))%4;v=V[hh];pp=(pp[0]+v[0],pp[1]+v[1])
   assert not initial_color(q,rr,ff);assert certify(rr,{q},p,h,word)is None;capout['controls']+=2
   r=solve(rows,cap,ch,args.limit);capout['results'].append(r)
   if i%10==0 or r.get('entry',0)>40000:print(i+1,'/',len(chs),r,flush=True)
   out['elapsed_seconds']=time.time()-started;(ROOT/'changed_endpoint_catalog_results.json').write_text(json.dumps(out,indent=2)+'\n')
  print('DONE CAP',source['channel'],Counter(tuple(r.get('drift',[]))for r in capout['results']),flush=True)
 print('DONE',time.time()-started,flush=True)
if __name__=='__main__':main()

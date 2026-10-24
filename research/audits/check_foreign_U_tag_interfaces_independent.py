from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'foreign_U_port_interfaces_2026-10-23';data=json.loads((D/'foreign_U_ports.json').read_text());manifest=json.loads((D/'manifest.json').read_text())
for f,h in manifest['files'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
for f,h in data['dependencies'].items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==h
W={a:r['word']for a,r in zip('DCVUFQB',json.loads((R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json').read_text())['macro_words'])};M='LLLLRLRRRRL';K={-1-1j,-1,-1j,0,1};L={0,1j,1,1+1j};Z={1,1+1j,2,2+1j};dirs=(1j,1,-1j,-1)
def walk(w):
 p=0j;h=0;odd=set();req={};reads={}
 for i,a in enumerate(w):
  c=(a=='L')^(p in odd);assert p not in req or req[p]==c;req[p]=c;reads.setdefault(p,[]).append((i,a));odd.symmetric_difference_update({p});h=(h+(1 if a=='R'else-1))%4;p+=dirs[h]
 return p,h,odd,req,reads
def xy(q):return[int(q.real),int(q.imag)]
def points(s):return sorted(map(xy,s))
def at(q,p,h):return p+q*(-1j)**h
def inv(q,p,h):return(q-p)*(1j)**h
def derive(w):
 p,h,odd,req,reads=walk(w+M);ep,eh,rawodd,_,rawreads=walk(w);I={q for q,c in req.items()if c}-K;O=({q for q,c in req.items()if c}^rawodd)-{at(q,ep,eh)for q in K};return dict(w=w,p=ep,h=eh,I=I,O=O,white={q for q,c in req.items()if not c},ctx=set(req),reads=reads,rawreads=rawreads)
G={a:derive(w)for a,w in W.items()};G8={a:derive(W[a[0]]+W['C']*(len(a)-1))for a in('D','DC','V','VC','VCC','U','UC','UCC')}
for a in('U','UC','UCC'):
 assert L|Z<=G8[a]['O'];assert all(rs[-1][1]=='R'and all(t<28 for t,ch in rs)for q,rs in G8[a]['rawreads'].items()if q in L|Z)
marks={r['name']:{complex(*q[:2])for q in r['raw_marks']}for r in json.loads((R/'word_stabilization/no_d_packet_fuel_marks.json').read_text())['packets']}
def oldcenter(p,h):
 c=2*p+at(-1-1j,0,h)
 if c.real==-1 and -1<=c.imag<=7:assert(p,h)==(-1+3j,2);return True
 return False
results={}
for title,held,target in [('star',L,L),('intact_cycle',L|Z,Z)]:
 rows=[];cases={}
 for a in'FQB':
  g=G[a];only=g['I']-set(g['rawreads']);assert len(only)==1;q0=next(iter(only));assert g['reads'][q0][0]==(len(g['w'])+1,'L');assert q0==at(-1,g['p'],g['h'])and q0 in marks[a+'C']
  for tag in sorted(target,key=lambda z:(z.real,z.imag)):
   for slot in sorted(g['I'],key=lambda z:(z.real,z.imag)):
    for h in range(4):
     p=tag-at(slot,0,h);core={at(q,p,h)for q in K};white={at(q,p,h)for q in g['white']};reason='sector'if(int(p.real+p.imag)+h)%2 else'held_core'if held&core else'held_before_white'if held&white else'entry_repeats_old_U_center'if oldcenter(p,h)else'candidate'
     rows.append((a,*xy(p),h,*xy(tag),*xy(slot),reason))
     if reason!='candidate':continue
     tags=held&{at(q,p,h)for q in g['I']};raw=[];spill=[]
     for q in tags:
      local=inv(q,p,h);rr=g['rawreads'].get(local,[])
      if rr:raw.append((q,local,g['reads'][local][0][0],len(rr)%2==0))
      else:spill.append(q)
     cases[a,*xy(p),h]=dict(tags=tags,raw=raw,spill=spill,fuel=held&{at(q,p,h)for q in marks[a]})
 ref=data['interfaces'][title];rrows=[(r['foreign'],*r['pose'],*r['aligned_tag'],*r['input_slot'],r['reason'])for r in ref['rows']];assert sorted(rows)==sorted(rrows)
 assert len(rows)==752 and len(cases)==(69 if title=='star' else 29)
 for refg in ref['gates']:
  c=cases[refg['foreign'],*refg['pose']];assert points(c['tags'])==refg['held_input_tags'];assert points(c['spill'])==sorted(r['cell']for r in refg['marker_spillover']);assert points(c['fuel'])==refg['base_fuel_marks_hitting_held']
  rr=sorted((tuple(xy(q)),tuple(xy(local)),t,black)for q,local,t,black in c['raw']);ar=sorted((tuple(z['cell']),tuple(z['foreign_local_cell']),z['first_L_phase'],z['raw_exit_black'])for z in refg['raw_retirements']);assert rr==ar
 if title=='star':
  assert Counter((a,len(c['raw']),len(c['spill']))for(a,x,y,h),c in cases.items())==Counter({(a,1,0):16 for a in'FQB'})+Counter({(a,2,0):3 for a in'FQB'})+Counter({(a,0,1):4 for a in'FQB'})
  assert all(not c['fuel']and all(not rr[3]for rr in c['raw'])for c in cases.values())
  assert {local for c in cases.values()for q,local,t,b in c['raw']}=={-1+2j,-2+2j,-3+3j,-4+3j,-5+2j,-5+1j}
 else:
  assert all(2<=len({q for q,l,t,b in c['raw']}&Z)<=3 and len(c['tags']&Z)<=3 for c in cases.values())
  assert {(a,x,y,h)for(a,x,y,h),c in cases.items()if c['fuel']}=={('F',3,-2,1),('B',0,-2,2)}
 results[title]=dict(rows=len(rows),counts=dict(Counter(r[-1]for r in rows)),gates=len(cases))
post={};n=0
for a,g in G8.items():
 for tag in L:
  for slot in g['I']:
   for h in range(4):
    n+=1;p=tag-at(slot,0,h)
    if(int(p.real+p.imag)+h)%2 or L&{at(q,p,h)for q in K|g['white']}:continue
    post[a,*xy(p),h]=p,h
assert n==368 and len(post)==24
assert set(post)=={(r['packet'],*r['pose'])for r in data['postreturn']['gates']}
controls=data['postreturn']['prepared_suffix_controls'];assert len(controls)==72
for c in controls:
 a=c['foreign'];b=c['returned_packet'];p=complex(*c['foreign_pose'][:2]);h=c['foreign_pose'][2];g=G[a];assert not L&{at(q,p,h)for q in g['ctx']};assert at(g['p'],p,h)==complex(*c['returned_pose'][:2])and(h+g['h'])%4==c['returned_pose'][2]
 w=W[a]+G8[b]['w']+M;req=walk(w)[3];seed={at(q,p,h)for q,v in req.items()if v}|L;assert points(seed)==c['prepared_seed'];board=set(seed);first={}
 for i,ch in enumerate(w):
  assert(p in board)==(ch=='L')
  if p in L and p not in first:first[p]=(i,ch)
  board.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;p+=dirs[h]
 assert len(first)==1 and all(i>=len(W[a])and ch=='L'for i,ch in first.values())
out=dict(status='PASS necessary genuine-U tag interfaces and prepared-only foreign return controls',manifest_sha256=hashlib.sha256((D/'manifest.json').read_bytes()).hexdigest(),interfaces=results,postreturn_rows=n,postreturn_gates=len(post),prepared_suffix_controls=len(controls),analytic='Earlier eight-history simplicity is used only at the foreign ENTRY center; the only cut repeats the creating-U endpoint at a nonadjacent physical pose. Foreign raw star erosion is confined to six common-prefix ports, at most two tags, all white at raw exit; marker spillover is successor phase1/core absorption. Conditional same-D-free-factor freshness eliminates AC marker gates and two intact-cycle gates only. All 72 suffixes have prepared black tags, NOT certified genuine U ancestry.',scope='No reachable-ancestry assertion for surviving gates, no extension of clean-eight permanence, no global foreign budget or capture theorem.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(results)

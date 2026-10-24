from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import hashlib,json
SELF=Path(__file__).resolve();ns={'__file__':str(SELF.parent/'check_U_first_helper_ports_independent.py')};exec((SELF.parent/'check_U_first_helper_ports_independent.py').read_text().split('rows=[];gates=[];adjacent_rejects=[]')[0],ns)
globals().update({k:ns[k]for k in('ROOT','G','IDS','xy','rotation','chords','meet','pt','edge','cross')})
B=ROOT/'core_periodicity_new/U_cohort_first_touch_clock_frozen_20261023_2017';man=json.loads((B/'manifest.json').read_text())
for p,h in man['files'].items():assert hashlib.sha256((B/p).read_bytes()).hexdigest()==h
W=-1+3j
# Angle values in units pi/4 are (rational integer part, coefficient of alpha_V).
def turn(a,b):
 k=b[0]-a[0];c=b[1]-a[1];lo=min(k+c,k+2*c);hi=max(k+c,k+2*c)
 choices=[(k+8*m,c)for m in range(-4,5)if lo+8*m>=-4 and hi+8*m<=4 and not(c==0 and abs(k+8*m)==4)]
 assert len(choices)==1,(a,b,choices);return choices[0]
def angle(v):
 x,y=xy(v);assert abs(x)==abs(y)and x
 return((1 if x>0 and y>0 else 3 if x<0<y else 5 if x<0 and y<0 else 7),0)
def on(q,a,b):return cross(q-a,b-a)==0 and min(a.real,b.real)<=q.real<=max(a.real,b.real)and min(a.imag,b.imag)<=q.imag<=max(a.imag,b.imag)
def paths(adj,a,b):
 todo=[(a,[a])]
 while todo:
  v,p=todo.pop()
  if v==b:yield p;continue
  for z in adj[v]:
   if z not in p:todo.append((z,p+[z]))
rows=[];cases={};adjacent=[]
for s in(7,8,9):
 O=G[s]['O'];sc=chords(s);adj={}
 for q in O:
  a,b=edge(q);adj.setdefault(a,[]).append(b);adj.setdefault(b,[]).append(a)
 for a in IDS:
  for h in range(4):
   for q in sorted(O,key=xy):
    for i in sorted(G[a]['I'],key=xy):
     p=q-rotation(i,h);I={p+rotation(x,h)for x in G[a]['I']};ctx={p+rotation(x,h)for x in G[a]['ctx']};cc=chords(a,p,h);key=(s,a,*xy(p),h)
     if(sum(xy(p))+h)%2:why='wrong_sector'
     elif ctx&(O-I):why='other_current_cohort_identity_in_context'
     else:
      bad=False
      for j,x in enumerate(sc):
       for k,y in enumerate(cc):
        hit=meet(*x,*y)
        if hit and not(j==len(sc)-1 and k==0 and(p,h)==(G[s]['end'],G[s]['h'])and hit=={pt(x[1])}):bad=True
      if bad:why='past_source_chord_contact'
      else:
       why='mixed_first_touch_clock_gate'
       if key not in cases:
        valid=[];aa=(1,0)if a in(0,1)else(0,1)if a in(4,5,6)else(2,0)
        for E in adj:
         if not on(E,*cc[0]):continue
         for path in paths(adj,E,W):
          if len(path)<2:continue
          seg=list(zip(path,path[1:]));okay=True
          for j,(u,v)in enumerate(seg):
           hit=meet(*cc[0],u,v)
           if hit and not(j==0 and hit=={pt(E)}):okay=False
           for k,(x,y)in enumerate(sc):
            if k==0:x=W
            hit=meet(x,y,u,v)
            if hit and not(k==0 and j==len(seg)-1 and hit=={pt(W)}):okay=False
           for k,(x,y)in enumerate(seg):
            if k>j+1 and meet(u,v,x,y):okay=False
          if not okay:continue
          angles=[(aa[0]-2*h,aa[1])]+[angle(v-u)for u,v in seg]+[(2,0)];ts=[turn(x,y)for x,y in zip(angles,angles[1:])];cl=(sum(x for x,y in ts),sum(y for x,y in ts));constant=(cl[0]+aa[0]-2,cl[1]+aa[1]);assert constant[1]==0 and constant[0]%2==0;off=constant[0]//2
          ages=[n for n in(4-off,-4-off)if n>=0 and n%4==(-h)%4];assert len(ages)==1
          valid.append(dict(E=xy(E),path=list(map(xy,path)),turns=ts,offset=off,n=ages[0]))
        assert valid,key;ages={v['n']for v in valid};assert len(ages)==1;n=ages.pop();assert n<=s-7+5
        cases[key]=dict(source=s,consumer=a,head=[*xy(p),h],consumed=sorted(map(xy,I&O)),outside=sorted(map(xy,I-O)),age=n,bridges=valid)
     rows.append((key,xy(q),xy(i),why))
counts=Counter(r[-1]for r in rows);assert counts==dict(wrong_sector=1656,other_current_cohort_identity_in_context=1529,past_source_chord_contact=42,mixed_first_touch_clock_gate=85);assert len(cases)==56
ref=json.loads((B/'U_cohort_first_touch_clock.json').read_text());key=lambda r:(r['source'],r['consumer'],*r['head'])
assert{key(r):r['forced_C_age']for r in ref['first_touch_clock_cases']}=={k:r['age']for k,r in cases.items()}
# Independently discovered paths and all their exact angles agree, not merely one author-selected bridge.
for r in ref['first_touch_clock_cases']:
 mine=cases[key(r)]['bridges'];assert{(tuple(map(tuple,v['path'])),v['n'])for v in mine}=={(tuple(map(tuple,v['path'])),v['forced_C_age'])for v in r['bridges']}
Y0={q for a in IDS for q in G[a]['O']if q.imag==0};assert Y0=={0j,1,2};assert all(q.imag>=0 for a in IDS for q in G[a]['O']);assert all(G[a]['h']==0 and G[a]['end'].imag>0 for a in(0,4,7))
old=[];excluded=Counter();blocked=[]
for key0,r in cases.items():
 s,a,x,y,h=key0;p=complex(x,y);O=G[s]['O'];n=r['age'];c=s-7
 if a not in(7,8,9):continue
 I={p+rotation(i,h)for i in G[a]['I']}
 if -1+2j in I&O:excluded['recycled_q']+=1;continue
 if len(I&O)>3:excluded['max_three']+=1;continue
 upper={p+rotation(i,h)for i in(-1+4j,2j,3j)}-O;w=[]
 for q in upper:
  v=rotation(q-G[s]['end'],-G[s]['h'])
  if n-5<c or(n-5==c and(v.imag<0 or v.imag==0 and v not in Y0)):w.append(q)
 assert w,key0;old.append(dict(source=s,consumer=a,head=[x,y,h],age=n,witnesses=sorted(map(xy,w))))
 if any(q in G[s]['ctx']for q in w):blocked.append(key0)
assert len(old)==27 and excluded==dict(recycled_q=10,max_three=3);assert len(blocked)==9
assert{key(r):set(map(tuple,r['witnesses']))for r in old}=={key(r):{tuple(v['cell'])for v in r['witnesses_current_at_source_entry']}for r in ref['U_oldness_cases']}
out=dict(status='PASS complete U-cohort first-touch exact clocks and precreator upper support',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),counts=dict(counts),cases=list(cases.values()),U_exclusions=dict(excluded),older_upper_cases=old,optional_source_context_exclusions=blocked,analytic='Before first cohort touch all output-edge identities are held. Exact path/source-tail/consumer-base intersection tests give a Jordan bridge via the live-edge barrier and U-entry simplicity. Exact symbolic principal turns cancel atan(3), giving one nonnegative heading-compatible clock per pose. All sources first-touch within five Cs after their full exit. For U consumers upper min5 plus the complete same-clock forward output frontier forces a precreator current upper. Nine such witnesses lie in source complete context and hence cannot survive through source, excluding those first-touch poses.',scope='First touch only, complete retained factor. No untouched entry origin grouping, original historical-component separation, arbitrary later-use clock or global U budget.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(counts);print('poses',len(cases),'older',len(old),'context exclusions',len(blocked));print(blocked)

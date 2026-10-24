from pathlib import Path
from collections import defaultdict,Counter
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];U=ROOT/'causal_reduction/unit_scale';R=ROOT/'nonlinear_global_budget_2026-10-23';D=(1j,1,-1j,-1);xy=lambda z:(int(z.real),int(z.imag))
J=json.loads((U/'prepared1564_noncrossing_R100_N3.json').read_text());plan=json.loads((U/'prepared1564_noncrossing_router_plan.json').read_text());launch=json.loads((U/'prepared1564_fresh_launch_cap.json').read_text());H=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];W=json.loads((R/'prepared_travelling_wave_certificate.json').read_text())['word'];seed={complex(*z)for z in J['initial_seed']};assert len(seed)==184
words=[]
for s in J['segments']:
 kind=s['kind']
 if kind=='H':w=H*s['count']
 elif kind=='router':w=next(z['word']for z in plan['routers']if z['index']==s['index'])
 elif kind=='H-prefix':w=H[:55]
 elif kind=='launch':w=launch['forward_prelude']
 elif kind=='wave':w=W*s['count']
 else:raise AssertionError(kind)
 assert len(w)==s['end_time']-s['start_time'];words.append(w)
word=''.join(words);assert len(word)==96439
p=33+70j;h=3;field=set(seed);need={};last={};tick=0;segments=[];allhits=Counter();wave_start=None
for s,w in zip(J['segments'],words):
 if s['kind']=='wave':wave_start=tick
 for c in w:
  if p not in need:need[p]=c=='L'
  else:assert last[p]!=c
  assert(p in field)==(c=='L'),(tick,xy(p),c)
  last[p]=c;allhits[p]+=1;field.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=D[h];tick+=1
 assert [list(xy(p)),h]==s['end_pose']and len(field)==s['mass']
 segments.append({'kind':s['kind'],'start':s['start_time'],'end':tick,'mass':len(field)})
minimal={z for z,b in need.items()if b};assert minimal==seed
assert(p,h)==(36+36j,0)and len(field)==11117
fieldhash=hashlib.sha256(json.dumps(sorted(map(xy,field)),separators=(',',':')).encode()).hexdigest();assert fieldhash==J['final_black_sha256']
# True ten-turn inverse history of THIS finite seed, not an assumed standard prefix.
back=set(seed);q=33+70j;hh=3;reverse=[]
for _ in range(10):
 q-=D[hh];post=q in back;reverse.append('R'if post else'L');hh=(hh+(-1 if post else 1))%4;back.symmetric_difference_update({q})
history=''.join(reverse[::-1]);allowed={(H*2)[i:i+10]for i in range(104)};assert len(allowed)==84
ext=history+word;bad=[ext[i:i+10]not in allowed for i in range(len(word)+1)];K=[bad[i]and bad[i+1]for i in range(len(word))]
# Independent packed-window detector.
allowedbits={int(''.join('1'if c=='L'else'0'for c in z),2)for z in allowed};state=int(''.join('1'if c=='L'else'0'for c in history),2);oldbad=state not in allowedbits;k2=0
for c in word:
 state=((state<<1)|(c=='L'))&1023;newbad=state not in allowedbits;k2+=oldbad and newbad;oldbad=newbad
assert k2==sum(K)
for s in segments:s['actual_K']=sum(K[s['start']:s['end']])
assert wave_start==91747
out={'status':'PASS independent complete184-cell seven-flight three-wave-period sample','R':100,'wave_periods':3,'source_sha256':hashlib.sha256((U/'prepared1564_noncrossing_R100_N3.json').read_bytes()).hexdigest(),'router_plan_sha256':hashlib.sha256((U/'prepared1564_noncrossing_router_plan.json').read_bytes()).hexdigest(),'whole_word_sha256':hashlib.sha256(word.encode()).hexdigest(),'initial_mass':len(seed),'minimal_first_L_mass':len(minimal),'unused_initial_black':len(seed-minimal),'raw_reads':len(word),'actual_inverse_history':history,'actual_K':sum(K),'wave_segment_K':sum(K[wave_start:]),'wave_segment_bad10_starting_after_launch':sum(bad[wave_start+1:]),'wave_start_time':wave_start,'wave_start_mass':J['segments'][-2]['mass'],'final_mass':len(field),'final_pose':[36,36,0],'final_black_sha256':fieldhash,'max_reads_one_cell':max(allhits.values()),'segments':segments,'scope':'One supplied complete finite seed and exact finite three-wave episode. No all-parameter family, eventual capture or noncapture, or fixed-mass unbounded-defect conclusion is inferred.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

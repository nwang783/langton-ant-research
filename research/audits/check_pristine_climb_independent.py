"""Independent copied-board BFS and concatenation replay, using complex poses."""
import json,pathlib,itertools
P=pathlib.Path('/workspace/shared/langton');old=json.loads((P/'computability/check_three_row_climb.json').read_text())
def catalog(S):
 queue=[(0j,1j,0,{},'')];out=[];nodes=0
 while queue:
  p,h,s,b,w=queue.pop();nodes+=1
  if p.imag==1:
   if s==S:out.append(w)
   continue
  assert len(w)<4*S+2
  choices=[b[p]] if p in b else ([0] if p.imag>=0 else [0,1])
  for bit in choices:
   hh=h*(1j if bit else -1j);ss=s+(hh==-1j)
   if ss>S:continue
   bb=b.copy();bb[p]=1-bit;queue.append((p+hh,hh,ss,bb,w+('L' if bit else 'R')))
 return sorted(out),nodes
def replay(w):
 p=0j;h=1j;b={};S=0;times=[]
 for t,c in enumerate(w):
  bit=int(c=='L')
  if p in b:
   if b[p]!=bit:return False,t,None
  elif p.imag>=0 and bit:return False,t,None
  b[p]=1-bit;h*=1j if bit else -1j;p+=h;S+=h==-1j;times.append((int(p.imag),S,t+1))
 return True,len(w),{'x':int(p.real),'y':int(p.imag),'north':h==1j,'south':S,'heights':times}
cats={};counts=[]
for S in range(1,5):
 words,nodes=catalog(S);assert words==sorted(old['catalogs'][str(S)]['words']);cats[S]=words;counts.append({'S':S,'words':len(words),'nodes':nodes})
assert [x['words'] for x in counts]==[1,1,4,16]
checks=[]
for a in itertools.product(range(1,5),repeat=3):
 if sum(a)>6:continue
 for parts in itertools.product(*(cats[s] for s in a)):
  ok,t,_=replay(''.join(parts));assert not ok;checks.append(t)
assert len(checks)==92 and max(checks)==27
w=old['witness']['word'];ok,t,result=replay(w);assert ok and result['y']==3 and result['south']==7 and result['north'];assert all(y<3 for y,s,t in result['heights'][:-1]);assert t==34
# Two-row cost2 cannot occur; a 3-south prefix gives equality.
assert not replay(cats[1][0]*2)[0]
two=[a+b for S,T in [(1,2),(2,1)] for a in cats[S] for b in cats[T] if replay(a+b)[0]];assert two and all(replay(w)[2]['south']==3 for w in two)
out={'status':'PASS','catalogs':counts,'three_crossing_combinations':len(checks),'latest_conflict_read':max(checks),'costs':{'1':1,'2':3,'3':7},'seven_south_witness':w,'witness_length':t}
(P/'audits/pristine_climb_independent.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
# Bind the standard-tail upper-bound witness from its complete finite seed.
std=json.loads((P/'recovered_bundle/ant_global/root/standard.json').read_text());bb={complex(-x,-y) for x,y in std['seed']};p=0j;h=1+0j;assert std['heading']==3 and max(q.imag for q in bb)==6
observed=[];headings=[]
for t in range(61+104):
 if t==61:
  assert (p,h)==(complex(2,7),1j) and all(q.imag<7 for q in bb)
  entry=p;count={1j:0,1+0j:0,-1j:0,-1+0j:0}
 c='L' if p in bb else 'R';assert c==std['word'][t%104]
 if t<61:assert p.imag<7
 bb.symmetric_difference_update({p});h*=1j if c=='L' else -1j;p+=h
 if t>=61:observed.append(c);count[h]+=1
assert (p,h)==(complex(4,9),1j) and list(count.values())==[27,27,25,25]
record=json.loads((P/'computability/pristine_standard_record.json').read_text());assert ''.join(observed)==record['period_word'];assert record['phase']==61 and record['period_counts']==list(count.values())
out['standard_record']={'phase':61,'entry':[2,7,0],'exit':[4,9,0],'direction_counts':[27,27,25,25]}
(P/'audits/pristine_climb_independent.json').write_text(json.dumps(out,indent=2)+'\n')
print('Standard strict-record witness PASS')

"""Finite exact drift-orbit certificates, not simulations of long powers."""
from pathlib import Path
import json,math
W='LLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLRLRLLRRRRLLRLLRRRRLLRRRRLLRLRRRRLRLLLLRRRRLRRLRRRRLLLLRLRRRRLRRRR'
def tr(w):
 p=(0,0);h=0;reads=[];last={}
 for t,c in enumerate(w):
  if last.get(p)==c:raise AssertionError(('literal conflict',t,p,c))
  last[p]=c;reads.append((p,c,t));h=(h+(1 if c=='R'else-1))%4;dx,dy=((0,1),(1,0),(0,-1),(-1,0))[h];p=(p[0]+dx,p[1]+dy)
 return reads,p,h
def off(p,r,d):
 x,y=p[0]-r[0],p[1]-r[1]
 if x*d[1]!=y*d[0]:return None
 if d[0]:return x//d[0] if x%d[0]==0 else None
 return y//d[1] if y%d[1]==0 else None
def cert(name,w):
 _,_,h=tr(w);power=4//math.gcd(h,4);s=w*power;reads,d,h=tr(s);assert h==0 and d!=(0,0);classes=[]
 for p,c,t in reads:
  for cls in classes:
   k=off(p,cls['representative'],d)
   if k is not None:cls['visits'].append([k,t,c]);break
  else:classes.append({'representative':p,'visits':[[0,t,c]]})
 for cls in classes:
  cls['visits'].sort(key=lambda z:(-z[0],z[1]));letters=[z[2]for z in cls['visits']];assert all(a!=b for a,b in zip(letters,letters[1:]));cls['first']=letters[0];cls['min_offset']=min(z[0]for z in cls['visits']);cls['max_offset']=max(z[0]for z in cls['visits'])
 fuel=[c for c in classes if c['first']=='L'];assert fuel
 # For each selected drift class and integer j>=max_offset, all reads at rep+j*d occur in a finite group whose first read is L.
 # Distinct classes and j give distinct cells. Hence an infinite power needs infinitely many initial black cells.
 return {'name':name,'word':w,'restoring_power':power,'restored_word':s,'drift':d,'classes':classes,'first_L_classes':len(fuel),'scope':'Every infinite power requires infinitely many entry-black cells, by its exact first-read drift classes.'}
q=json.load(open('direct_mono_rrrlrllrrrr_history4_scc0_context2_port_quotient.json'))
words={'V18':q['macro_words'][39]['word'],'T16':q['macro_words'][33]['word'],'U28':'LLLLRLRRRRLRLLLLRRRRLRRLRRRR'}
out={'tails':[cert(n,w)for n,w in words.items()],'standard_cycles':[]}
for p,cycle in [('direct_mono_lrrlrrrrlrl_history4_scc0_context2_residual0_residual0',[1,6,5]),('direct_mono_rrrlrllrrrr_history4_scc0_context2_residual0',[3,16,14])]:
 q=json.load(open(p+'_port_quotient.json'));s=''.join(q['macro_words'][a]['word']for a in cycle);assert len(s)==104;phases=[i for i in range(104)if (W+W)[i:i+104]==s];assert phases;_,d,h=tr(s);assert h==0 and d!=(0,0);out['standard_cycles'].append({'source':p,'cycle':cycle,'word':s,'canonical_W_phase':phases,'drift':d})
Path('staged_two_cell_periodic_certificates.json').write_text(json.dumps(out,indent=2));print([(z['name'],z['restoring_power'],z['drift'],z['first_L_classes'])for z in out['tails']]);print(out['standard_cycles'])

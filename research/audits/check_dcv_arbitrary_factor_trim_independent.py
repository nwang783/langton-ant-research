"""Independent boundary identities and complete short-factor trim controls."""
from pathlib import Path
from itertools import product
import json,hashlib
P=Path(__file__).resolve().parents[1];W={'D':'LLLLRLRRRR','C':'LLLLRLRRRRLRRRR','V':'LLLLRLRRRRLRRLRRRR'};M=W['D']+'L'
def raw(w):return ''.join(W[c]for c in w)
def trace(w):
 p=0j;h=1j;last={};initial=set()
 for t,c in enumerate(w):
  if p in last and last[p][1]==c:return None
  if p not in last and c=='L':initial.add(p)
  last[p]=(t,c);h*=(-1j if c=='R'else 1j);p+=h
 return p,h,last,initial
assert trace(W['C']*5)is None and trace(W['C']*4+M)is None and trace(W['V']+W['C']*3+M)is None
end,h,last,_=trace(W['D']);assert last[end]==(6,'R')
assert trace(raw('DCCD'))is not None and trace(raw('DCCD')+'L')is not None and trace(raw('DCCD')+'LL')is None
terminal_controls=[]
for A in'DV':
 for k in range(5):
  name=A+'C'*k;ok=trace(raw('DCC'+name))is not None;assert ok==(name=='D');terminal_controls.append({'packet':name,'DCC_predecessor_raw_feasible':ok})
packets=['D','DC','DCC','DCCC','V','VC','VCC'];keep={'D','DC','V','VC','VCC'}
for p in packets:
 assert trace(raw('DCC'+p)+M)is None
 assert trace(raw(p+'DCCC')+M)is None
count=exception=0;hist={};maxtrim=0
for n in range(1,10):
 accepted=0
 for letters in product('DCV',repeat=n):
  word=''.join(letters);lit=raw(word);tr=trace(lit)
  if tr is None:continue
  accepted+=1;count+=1
  lead=len(word)-len(word.lstrip('C'));assert lead<=4
  rest=word[lead:]
  if not rest:assert len(lit)<=60;continue
  groups=[]
  for c in rest:
   if c in'DV':groups.append(c)
   else:groups[-1]+=c
  terminal=groups.pop();assert len(terminal)-1<=4;suffix=len(raw(terminal))
  if groups and groups[-1]=='DCC':assert terminal=='D';groups[-1]='DC';suffix+=15;exception+=1
  assert suffix<=78
  extra=3*lead;prefix=15*lead
  if groups and groups[0]=='DCCC':groups.pop(0);prefix+=55;extra+=9
  assert extra<=21 and prefix+suffix<=193 and all(g in keep for g in groups)
  maxtrim=max(maxtrim,prefix+suffix)
  # The original trajectory supplies the marker, not an invented language suffix.
  available=lit+('L'if word.endswith('D')else'');at=prefix
  for g in groups:
   assert available[at:at+len(raw(g))+11]==raw(g)+M
   at+=len(raw(g))
  assert at+suffix==len(lit)
 hist[n]=accepted
note=P/'word_stabilization/dcv_arbitrary_factor_cubic_trim.md'
out={'status':'PASS corrected arbitrary D/C/V finite-factor trim','legal_factors_through_9_macros':count,'by_length':hist,'standalone_D_exceptions':exception,'largest_observed_total_trim':maxtrim,'terminal_controls':terminal_controls,'uniform_trim_steps':193,'entry_mass_extra':21,'bound':'193+f(m+21), with the signed recurrent cubic f','note_sha256':hashlib.sha256(note.read_bytes()).hexdigest(),'scope':'Literal boundary identities give the all-length proof; bounded factor enumeration is a control only.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'kernel_cycle_lift_2026-10-24';p=SELF.with_name('check_cycle_birth_finite_fuel_independent.py');ns={'__file__':str(p)};exec(p.read_text().split('cells=')[0],ns)
ends,component,step,wvertex=[ns[k]for k in('ends','component','step','wvertex')]
def xy(z):return(int(z.real),int(z.imag))
def ports(v):return{(v+dd)/2 for dd in[1+1j,1-1j,-1+1j,-1-1j]}
def verts(B):return{v for q in B for v in ends(q,0)}
J=json.loads((R/'reframe_finite_seed_2026-10-24/cap7_turn_word_quotient.json').read_text());author=json.loads((D/'cap7_word_budget_filters_certificate.json').read_text());refs={z['word']:z for z in author['first_return_unit_propagation']};rows=[];ct=Counter();positive=[]
for word in J['word_counts']:
 p=0j;h=0;pose=[];last={};seed=set();bad=None
 for t,ch in enumerate(word):
  pose.append((p,h))
  if p in last and ch==last[p][1]:bad={'status':'NO_LITERAL_WORD_COLOR','cell':xy(p),'previous':last[p],'next':(t,ch)};break
  if p not in last and ch=='L':seed.add(p)
  last[p]=(t,ch);h=(h+(1 if ch=='R'else-1))%4;p+=1j*(-1j)**h
 if bad is not None:row={'word':word,**bad}
 else:
  pose.append((p,h));B=set(seed);fields=[];active=[]
  for t,(p,h)in enumerate(pose):
   fields.append(set(B));active.append(component(B,0,wvertex(p,h))[1])
   if t<len(word):assert(p in B)==(word[t]=='L');B.symmetric_difference_update({p})
  row={'word':word,'seed':sorted(map(xy,seed)),'max_active':max(map(len,active))}
  badend=next((t for t in[0,len(word)]if active[t]),None)
  overflow=next((t for t,C in enumerate(active)if len(C)>7),None)
  if badend is not None:row.update(status='NO_EMPTY_ENDPOINT',cut=badend,mandatory_component=sorted(map(xy,active[badend])))
  elif overflow is not None:row.update(status='NO_CAP7_MANDATORY_COMPONENT',cut=overflow,mandatory_component=sorted(map(xy,active[overflow])))
  else:
   # Rebuild the optional sound propagation, retaining arbitrary unread variables.
   Rset=set(last);FB=set();FW=set();log=[]
   for t in[0,len(word)]:
    for q in ports(wvertex(*pose[t]))-Rset:FW.add(q)
   change=True
   while change:
    change=False
    for t,(p,h)in enumerate(pose):
     B=fields[t]|FB;C=component(B,0,wvertex(p,h))[1];assert len(C)<=7
     for q in set.union(*(ports(v)for v in verts(C)|{wvertex(p,h)}))-Rset-FB-FW:
      Cnew=component(B|{q},0,wvertex(p,h))[1]
      if len(Cnew)>7:FW.add(q);change=True;log.append(('white',t,xy(q)))
    for t in range(1,len(word)):
     P=ports(wvertex(*pose[t]));B=fields[t]|FB
     if P&B:continue
     choices=P-Rset-FW;assert choices
     if len(choices)==1:
      q=next(iter(choices))
      if q not in FB:FB.add(q);change=True;log.append(('black',t,xy(q)))
   assert not FB
   p,h=pose[-1];w=wvertex(p,h);tips={w+a+b*1j for a in[-2,2]for b in[-2,2]};U=set()
   for v in tips:U|=component(fields[-1],0,v)[1]
   u,v=ends(p,0);first=v if u==w else u
   status='TRAP_MASS'if len(U)>3 else'TRAP_SATURATED_NONFIRST'if len(U)==3 and first not in verts(U)else'OPEN'
   row.update(status=status,exit_pose=[xy(p),h],mandatory_final=sorted(map(xy,fields[-1])),neighbor_union=sorted(map(xy,U)),first_tip_in_union=first in verts(U),forced_unread_black=[],propagation_log=log)
   if status=='OPEN':
    assert not active[0]and not active[-1]and all(active[t]for t in range(1,len(word)))
    B=set(seed);p=0j;h=0
    for t,ch in enumerate(word):
     assert component(B,0,wvertex(p,h))[1]==active[t];p,h,c=step(B,p,h);assert c==ch
    assert B==fields[-1]and not component(B,0,wvertex(p,h))[1]
    positive.append({'word':word,'complete_seed':sorted(map(xy,seed)),'initial_mass':len(seed),'final_mass':len(B),'max_active':max(map(len,active))})
 assert row['status']==refs[word]['status'];ct[row['status']]+=1;rows.append(row)
assert ct=={'NO_LITERAL_WORD_COLOR':5,'NO_EMPTY_ENDPOINT':2,'NO_CAP7_MANDATORY_COMPONENT':13,'TRAP_MASS':11,'TRAP_SATURATED_NONFIRST':4,'OPEN':23}
assert{z['word']for z in positive}==set(author['remaining_words']);assert all(not z.get('forced_unread_initial_black')for z in refs.values())
files=['CAP7_WORD_MANDATORY_FIELD_FILTERS.md','check_cap7_word_budget_filters.py','cap7_word_budget_filters_certificate.json'];hashes={f:hashlib.sha256((D/f).read_bytes()).hexdigest()for f in files};assert hashes[files[0]]=='21a49f905213542c69b0d5be6d48d0dbdd0f6b1d1e567701ee6ebf0c75ae9e0c'
out={'status':'PASS supplied58-word mandatory-field filters;23 actual finite first-return minimal-seed controls, NO continuation closure','source_hashes':hashes,'classification_counts':dict(ct),'all58_independent_rows':rows,'23_finite_positive_controls':positive,'kernel_coverage_report':hashlib.sha256(SELF.with_name('check_cap7_structure_independent.json').read_bytes()).hexdigest(),'analytic_review':[
'For each fixed literal word, an actual initial board consists of exactly the first-L minimal seed plus arbitrary black cells NEVER read by the word. Its field at every cut is the minimal toggled field union that unchanged unread exterior. This equality, not a guessed clean profile, makes all computed black components mandatory subsets.',
'Equal repeated reads conflict independently of exterior. Mandatory black at an empty endpoint and mandatory active mass>7 cannot be repaired by adding unread black. The5/2/13 exclusions are finite-word impossibilities under the exact first-return/cap assumptions.',
'Independently repeated optional unit propagation only forces an unread bit white when setting it black already causes cap overflow, or black when it is the sole remaining possible incident edge at a required nonempty cut. These are sound necessary clauses, not a decision procedure. No unread BLACK bit is newly forced on these58 words.',
'The final mandatory neighbor-component union gives11 mass>3 and4 mass3/nonfirst cases. By the separately signed EMPTY-cursor general budget law, any realization must exceed cap7 within9 more updates. Extra unread edges either increase imported mass or cannot supply the missing first-tip connection without increasing it. These15 words may occur once but cannot continue as a sustained cap7 tail.',
'All23 remaining words are separately replayed from their complete minimal first-L seeds with nonempty interior, empty endpoints and active cap7. Thus finite prefix existence is established here, but continuation compatibility, fuel, arbitrary profile families and cap7 exit remain OPEN. The full154million-profile language is not materialized and word spelling is not treated as a complete component profile.'
]}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(dict(ct))

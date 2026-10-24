from pathlib import Path
from collections import Counter
import hashlib,json
from fractions import Fraction
P=Path(__file__).resolve();S=P.with_name('check_U1_young3_shadow_independent.py');exec(compile(S.read_text().split('rows=[];cases=[]')[0],str(S),'exec'))
B=ROOT/'core_periodicity_new/C_first_W_crossing_frozen_20261023_1424';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_C_first_W_crossing.json').read_text());D=ROOT/'core_periodicity_new';C5={tuple(map(int,l.split()[:8]))for l in(D/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv').read_text().splitlines()};mp={a:i for i,a in enumerate(ids)}
q=1+2j;goal=1+0j;assert rotation(q-goal,-3)==2 and G[4][2][2]is False
# Exact general closed-segment test, including endpoints and collinear overlap.
def det(a,b):return int(a.real*b.imag-a.imag*b.real)
def meet(a,b,c,d):
 ab=b-a;cd=d-c;den=det(ab,cd)
 if den:return 0<=Fraction(det(c-a,cd),den)<=1 and 0<=Fraction(det(c-a,ab),den)<=1
 if det(c-a,ab):return False
 return all(max(min(x,y),min(z,w))<=min(max(x,y),max(z,w))for x,y,z,w in[(a.real,b.real,c.real,d.real),(a.imag,b.imag,c.imag,d.imag)])
roles=[]
for src in ids:
 pp=G[base[src]][0];hh=0
 for j in range(counts[src]):
  out=pp+rotation(q,hh);assert out in G[src][4];roles.append((src,pp,hh,j,out,counts[src]-j));pp+=rotation(1j,hh);hh=(hh-1)%4
assert len(roles)==7;cases=[]
for ri,(src,sp,sh,shift,output,remaining)in enumerate(roles):
 for gap in range(6):
  h=(-gap)%4;age=gap+shift
  for dst in ids:
   for slot in G[dst][3]:
    pos=q-rotation(slot,h);rel=sp+rotation(pos,sh);query=(mp[src],mp[dst],*xy(rel),(sh+h)%4,*xy(output),min(5,age))
    if gap<remaining:why='CONSUMER_BEFORE_FULL_SOURCE_EXIT'
    elif gap+counts[dst]>5:why='CONSUMING_FULL_PACKET_CANNOT_FINISH_BEFORE_TARGET'
    elif(int(pos.real+pos.imag)+h)%2:why='WRONG_SECTOR'
    elif query in C5:why='SIGNED_COUNT5_EXCLUDED'
    else:
     end=pos+rotation(G[base[dst]][0],h);c0=2*pos+rotation(-1-1j,h);c1=2*end+rotation(-1-1j,h)
     if meet(-1-1j,1+1j,c0,c1):assert shift==1 and gap==4;why='EARLIER_CLOSED_CENTER_CONTACT'
     elif gap==4:assert shift==1 and h==0 and end.imag>=2;why='ONE_REMAINING_C_N_TO_W_STAYS_ABOVE_TARGET'
     else:assert gap==5 and dst==7 and end.real<1 and end.imag>0;why='FINAL_W_ZERO_CONE_CANNOT_REACH_TARGET'
    cases.append(dict(role_index=ri,atomic_entry_C_gap_to_consumer=gap,consumer=dst,input=xy(slot),query=query,reason=why))
key=lambda r:(r['role_index'],r['atomic_entry_C_gap_to_consumer'],r['consumer'],tuple(r['input']))
auth={key(r):r for r in J['all_966_consumer_options']};assert len(cases)==len(auth)==966
for r in cases:
 a=auth[key(r)];assert r['reason']==a['reason']and r['query']==tuple(a['full_source_counted_query'])
cnt=Counter(r['reason']for r in cases);assert cnt['EARLIER_CLOSED_CENTER_CONTACT']==12 and cnt['ONE_REMAINING_C_N_TO_W_STAYS_ABOVE_TARGET']==12 and cnt['FINAL_W_ZERO_CONE_CANNOT_REACH_TARGET']==14
assert all(rotation(G[a][0],h).imag>=0 for a in(0,4,7)for h in(0,3))and all(rotation(G[a][0],3).real<0 for a in(0,4,7))
out=dict(status='PASS independent seven-role shifted-clock inventory and all-word first-contact contradiction',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),cases=cases,reason_counts=dict(cnt),scope='Actual C atom inside complete-eight factor to V(1,0,W), entryCgap5, cannot be FIRST auxiliary center self-contact. Full consumer must finish before target V base; existing overflow clauses retained as overflow. No arbitrary atomic language, unconditional crossing/5C-return exclusion, word-depth bound or global capture.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k!='cases'})

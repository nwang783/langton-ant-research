from pathlib import Path
from collections import Counter
P=Path(__file__).resolve();S=P.with_name('check_C_first_W_contact_independent.py');exec(compile(S.read_text().split('roles=[]')[0],str(S),'exec'))
B=ROOT/'core_periodicity_new/D_first_W5_gate_frozen_20261023_1437';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_D_first_W5_clearance_gate.json').read_text());HB={tuple(map(int,l.split()[:7]))for l in(D/'chronology_dcuv/protected_patch2.tsv').read_text().splitlines()}
def zero_reach(p,target,h):
 z=rotation(target-p,-h);x,y=xy(z)
 return x>=0 and y>=0 and any(y-x-2*v>=0 and(y-x-2*v)%4==0 for v in range(x+1))
rows=[];late=[];buds=[]
for src in(0,1):
 assert 2 in G[src][4]
 for n in range(6):
  h=(-n)%4
  for dst in ids:
   for slot in G[dst][3]:
    pos=2-rotation(slot,h);hb=(src,dst,*xy(pos),h,2,0);query=(mp[src],mp[dst],*xy(pos),h,2,0,n)
    if n<counts[src]:why='BEFORE_SOURCE_FULL_EXIT'
    elif(int(pos.real+pos.imag)+h)%2:why='SECTOR'
    elif hb in HB:why='SIGNED_HB'
    elif query in C5:why='SIGNED_COUNT5'
    else:
     e=pos+rotation(G[base[dst]][0],h);c0=2*pos+rotation(-1-1j,h);c1=2*e+rotation(-1-1j,h)
     if meet(-1-1j,1+1j,c0,c1):assert n>=3;why='EARLIER_CLOSED_CONTACT'
     elif n+counts[dst]>5:why='FULL_TAIL_ENDS_AFTER_LATER_V_BASE'
     else:
      end=pos+rotation(G[dst][0],h);eh=(h+G[dst][1])%4
      if n+counts[dst]==5 and not zero_reach(end,1,3):why='ZERO_C_RETURN_IMPOSSIBLE'
      elif n==3:
       assert dst in(4,5)and pos==1j and h==1
       bud=e+rotation(1-1j,h);assert e==3 and bud==2-1j and rotation(bud-1,-3)in K;why='NEW_V_BASE_EXIT_BUD_CURRENT_IN_TARGET_CORE';buds.append((src,dst,xy(pos),n,xy(bud)))
      else:
       assert n==5 and dst in(4,7)and(end,eh)==(1,3);why='LAST_CLOCK_DIRECT_PREDECESSOR_GATE';late.append((src,dst,xy(pos),xy(slot)))
    rows.append((src,dst,n,xy(slot),xy(pos),why))
auth={(r['source_full'],r['consumer_full'],r['source_age'],tuple(r['input'])):r for r in J['queries']};assert len(rows)==len(auth)==276
for src,dst,n,slot,pos,why in rows:assert auth[src,dst,n,slot]['reason']==why and tuple(auth[src,dst,n,slot]['consumer_pose'])==(*pos,(-n)%4)
assert len(buds)==len(late)==4 and {(dst,pos,slot)for src,dst,pos,slot in late}=={(4,(4,-1),(1,2)),(7,(5,0),(0,3))}
out=dict(status='PASS independent complete D-first W5 old-output clearance and second-generation bud gate',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),cases=rows,reason_counts=dict(Counter(r[-1]for r in rows)),bud_rejections=buds,late_gates=late,scope='Given actual D-base to V(1,0,W) proper crossing at entry gap5 and no earlier nonadjacent CLOSED contact, the old D output must retire in immediately preceding V(4,-1,W) or U(5,0,W). The age3 alternatives fail by atomic exit-bud persistence through two Cs. Necessary gate only; no attainability or exclusion of surviving five-C history, no root/fuel/global claim.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k!='cases'})

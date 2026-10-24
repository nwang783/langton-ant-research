"""Independent two-identity predecessor shielding and full source/atomic clock conversion."""
from pathlib import Path
SELF=Path(__file__).resolve();S=SELF.with_name('check_five_C_center_touch_independent.py');exec(compile(S.read_text().split('primary=0;hardcases=0;gate=[]')[0],str(S),'exec'))
B=ROOT/'core_periodicity_new/atomic_three_C_pose_boundary_frozen_20261023_1607';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_atomic_three_C_pose_boundary.json').read_text());incoming=[];r=1-1j;q=-1-2j;target=-1+0j
for src in ids:
 for j in range(counts[src]+1):
  ep,eh,_,_=walk(raws[base[src]]+C*j);ph=(-eh)%4;pp=-rotation(ep,ph);previous='C'if j else'D'if base[src]==0 else'V'if base[src]==4 else'U'
  ri=len(incoming);incoming.append((src,j,ep,eh,pp,ph,previous))
assert len(incoming)==15 and sum(z[-1]=='D'for z in incoming)==2
assert rotation(q-target,-1)==2 and G[0][2][2]is False and rotation(r-target,-1)==1+2j
# Complete following marker of a consumer does not read the protected bud at B.
assert 1+2j not in walk(mark)[2]
ref={(x['incoming_role_index'],x['C_after_A'],x['consumer_full'],tuple(x['consumer_input'])):x for x in J['all1196_q_first_consumer_queries']};tally=Counter();checked=0
for ri,(src,j,ep,eh,pp,ph,previous)in enumerate(incoming):
 if previous=='D':assert pp==-1-1j and ph==0;continue
 oq=rotation(q-pp,-ph);orb=rotation(r-pp,-ph);assert oq in G[src][4]and orb in G[src][4]
 if j==0:assert oq==(1j if previous=='V'else -1+2j)
 else:
  a,ah,_,_=walk(raws[base[src]]+C*(j-1));assert a+rotation(2,ah)==oq
 for n in range(4):
  h=(-n)%4
  for dst in ids:
   for inp in G[dst][3]:
    cp=q-rotation(inp,h);rel=rotation(cp-pp,-ph);dh=(h-ph)%4;hb=(src,dst,*xy(rel),dh,*xy(oq));cq=(mp[src],mp[dst],*xy(rel),dh,*xy(oq),min(j+n,5));lr=rotation(r-cp,-h);end=cp+rotation(G[base[dst]][0],h)
    if n<counts[src]-j:why='CONSUMER_BEFORE_CONTAINING_FULL_SOURCE_EXIT'
    elif(int(cp.real+cp.imag)+h)%2:why='SECTOR'
    elif hb in HB:why='SIGNED_HB'
    elif cq in C5:why='SIGNED_COUNT5'
    elif lr in G[dst][2]:why='PROTECTED_INCOMING_BUD_IN_COMPLETE_CONSUMER_CONTEXT'
    elif n+counts[dst]>3:why='CONSUMER_FULL_TAIL_ENDS_AFTER_D_TARGET_FULL_ENTRY'
    elif n==3 and not zero_reach(end,target,h):why='EXACT_ZERO_C_E_ENDPOINT_CONE_IMPOSSIBLE'
    elif n==2 and not one(end,target,h):why='EXACT_ONE_C_S_TO_E_ENDPOINT_CONE_IMPOSSIBLE'
    else:raise AssertionError(('OPEN',ri,n,dst,xy(inp),xy(end)))
    row=ref[ri,n,dst,xy(inp)];assert row['reason']==why and tuple(row['HB_key'])==hb and tuple(row['count5_key'])==cq and tuple(row['consumer_pose'])==(*xy(cp),h)and tuple(row['producer_pose'])==(*xy(pp),ph)
    checked+=1;tally[why]+=1
assert checked==1196 and dict(tally)==J['counts']['query_reasons']
# Prior D must be factor-first: its incoming atomic bud is forced WHITE at target.
assert target-(-1-1j)==1j and rotation(-2j-target,-1)==2+1j
assert all(G[x][2][2+1j]is False for x in(0,1))
# Reconstruct every actual source-A common(2,0) role and all45 upper-input exclusions.
upper=[];fullroles=[]
for src in ids:
 for j in range(counts[src]+1):
  if j==0:a=0j;ah=0;shift=0
  else:a,ah,_,_=walk(raws[base[src]]+C*(j-1));shift=j-1
  fo=a+rotation(2,ah);assert fo in G[src][4];fullroles.append((src,a,ah,shift,fo))
  bp=a+rotation(target,ah);bh=(ah+1)%4
  for dst in(7,8,9):
   assert bp+rotation(3j,bh)==fo;cq=(mp[src],mp[dst],*xy(bp),bh,*xy(fo),3+shift);assert cq in C5;upper.append(cq)
assert len(upper)==45 and set(upper)=={tuple(x['count5_key'])for x in J['U_target45_minimum_age_cases']}
assert walk(C+mark)[2][3j]is False
ends=[]
for src in(0,4,7):
 for inp in G[src][3]:
  cp=2-rotation(inp,1);ep=cp+rotation(G[src][0],1);assert ep.real>=2;ends.append((src,xy(inp),xy(cp),xy(ep)))
assert len(ends)==8
out=dict(status='PASS universal actual-atomic three-C left-pose boundary law',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),actual_predecessor_roles=15,nonD_predecessor_roles=13,shielded_first_consumer_cases=checked,reasons=dict(tally),actual_source_common_roles=len(fullroles),upper_input_queries=len(upper),E_base_endpoints=ends,scope='Actual atomic A0N to B(-1,0,E), entry gap3, inside a complete recurrent-eight factor: B is D/V only and A has factor-entry C clock, with exactly the three stated boundary alternatives. Terminal D uses only its actual raw and marker. No first-contact, outgoing-A-type or funding premise; no arbitrary atomic-word extension or capture.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)

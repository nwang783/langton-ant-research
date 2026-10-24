"""Exact all-age U core-port retirement gate. No path search or age cutoff."""
from pathlib import Path
import json,hashlib,collections
W=Path(__file__).resolve().parent;GP=W/'chronology_dcuv/literal_residual_geometry.json';J=json.loads(GP.read_text());G=J['geometry'];K=set(map(tuple,J['core']));IDS=[0,1,4,5,6,7,8,9]
P=set(map(tuple,G[7]['inputs']));r=(-1,0)
def rot(p,h):
 x,y=p;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def atoms(a,p,h):
 out=[]
 for kind in[0 if a in[0,1]else 4 if a in[4,5,6]else 7]+['C']*G[a]['name'].count('C'):
  c=add((2*p[0],2*p[1]),rot((-1,-1),h));v=(2,2)if kind in[0,'C']else(2,6)if kind==4 else(0,8);e=add(c,rot(v,h));out.append(dict(atom=kind,head=[*p,h],start=c,end=e))
  if kind=='C':p=add(p,rot((0,1),h));h=(h-1)%4
  else:p=add(p,rot(G[kind]['endpoint'][:2],h))
 return out,(*p,h)
rows=[]
for a in IDS:
 for h in range(4):
  for slot in G[a]['inputs']:
   v=rot(slot,h);p=r[0]-v[0],r[1]-v[1];row=dict(packet=a,head=[*p,h],input_slot=slot)
   if(sum(p)+h)%2:row['reason']='wrong_sector'
   else:
    ctx={add(p,rot(z[:2],h))for z in G[a]['requirements']}|{add(p,rot(z,h))for z in K};hit=sorted(ctx&P)
    if hit:row.update(reason='protected_final_input_context',hits=hit)
    else:
     A,en=atoms(a,p,h);row.update(atomic_chords=A,raw_exit=en)
     if en==(0,0,0):
      assert a in[0,4,7]and h==0 and tuple(A[-1]['end'])==(-1,-1)
      row['reason']='MUST_BE_IMMEDIATE_PREDECESSOR'
     else:
      # All other cases put the future goal ENTRY center strictly inside an earlier U base.
      assert a in[7,8,9]and(*p,h)==(-2,-1,1)
      assert tuple(A[0]['start'])==(-5,-1)and tuple(A[0]['end'])==(3,-1)
      assert -5 < -1 < 3
      row['reason']='earlier_base_contains_future_entry_center'
   rows.append(row)
assert len(rows)==92
cnt=dict(collections.Counter(q['reason']for q in rows));assert cnt==dict(MUST_BE_IMMEDIATE_PREDECESSOR=3,wrong_sector=46,protected_final_input_context=40,earlier_base_contains_future_entry_center=3)
last=[q for q in rows if q['reason']=='MUST_BE_IMMEDIATE_PREDECESSOR']
assert[(q['packet'],q['head'])for q in last]==[(0,[-1,-1,0]),(4,[-1,-3,0]),(7,[0,-4,0])]
for a in[7,8,9]:
 assert P==set(map(tuple,G[a]['inputs']))and r in K
 assert all(tuple(t[:2])not in P for t in G[a]['requirements']if t[3]<11)
apps=[]
for a in[8,9]:
 O={add((1,5),rot(z,2))for z in G[a]['outputs']};assert r in O and(0,-1)in O
 assert{(-1,1),(-1,4),(0,2),(0,3)}<=O and(-1,2)not in O
 raw=[]
 for q in last:
  p=q['head'];I={add(p[:2],rot(z,p[2]))for z in G[q['packet']]['inputs']}
  raw.append(dict(helper=q['packet'],head=p,also_consumes_other_core_spare=(0,-1)in I))
 assert[rr['also_consumes_other_core_spare']for rr in raw]==[False,True,True]
 apps.append(dict(source=a,head=[1,5,2],co_born_goal_inputs=[[-1,1],[-1,4],[0,2],[0,3]],older_goal_q=[-1,2],mandatory_core_outputs=[[-1,0],[0,-1]],last_helper_options=raw))
D=[GP,Path(__file__).resolve(),W/'U_entry_simplicity_frozen_20261023_1616/manifest.json']
O=dict(status='AUTHOR_EXACT_CORE_PORT_GATE_PENDING_INDEPENDENT_AUDIT',scope='Actual complete-eight factor with simple corrected-center path. All five future U inputs remain current after a boundary at which (-1,0) is a current residual. Its first retirement must be the goal immediate predecessor D/V/U in the exact three poses. Necessary gate only; no attainment, U budget or capture.',protected_final_inputs=sorted(P),core_identity_cell=r,counts=cnt,cases=rows,older_q_four_cohort_applications=apps,dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(W/'chronology_dcuv/U_core_identity_last_helper.json').write_text(json.dumps(O,indent=2)+'\n');print(json.dumps(cnt,indent=2))

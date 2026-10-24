"""Compact no-matching-needed consequence of the signed simultaneous birth law."""
from pathlib import Path
import json,hashlib
W=Path(__file__).resolve().parent;S=W/'chronology_dcuv/delayed_height_probe/u1_k5_exact_low_residue_age.unfolded.json';J=json.loads(S.read_text());LP=W/'chronology_dcuv/literal_residual_geometry.json';G=json.loads(LP.read_text())['geometry'];HP=W/'chronology_dcuv/protected_patch2.tsv';HB={tuple(map(int,l.split()[:7]))for l in HP.read_text().splitlines()};word=J['word_including_goal'];phase=1;F=-10;mod=4
assert len(word)==350 and word[-1]==7
rot=lambda p,h:((p[0],p[1]),(p[1],-p[0]),(-p[0],-p[1]),(-p[1],p[0]))[h%4]
def coord(p):x,y=rot(p,phase);return x+y,x-y
h,H,tr=J['initial_pose'];C=0;outputs=[];rows=[]
for k,a in enumerate(word):
 row=dict(step=k,packet=a,pose=[h,H,tr],C=C);rows.append(row);assert row['pose']==J['rows'][k]['pose']and C==J['rows'][k]['C_before']
 if k<len(word)-1:
  for oi,s in enumerate(G[a]['outputs']):
   dz,dt=coord(rot(s,h));outputs.append(dict(step=k,packet=a,heading=h,slot=s,output_index=oi,height=H+dz,residue=(tr+dt)%mod,C=C))
 dx,dy,dh=G[a]['endpoint'];dz,dt=coord(rot((dx,dy),h));H+=dz;tr=(tr+dt)%mod;h=(h+dh)%4;C+=G[a]['name'].count('C')
goal=rows[-1];assert goal['pose']==[0,0,0]and goal['C']==122
origins={}
for s in G[7]['inputs']:
 dz,dt=coord(rot(s,0));height=dz;residue=dt%mod;assert height>F
 age_min=5 if tuple(s)in((-1,4),(0,2),(0,3))else 3;L=[]
 for u in outputs:
  age=goal['C']-u['C']
  if(u['height'],u['residue'])!=(height,residue)or age<age_min:continue
  dh=(-u['heading'])%4;x,y=rot(s,dh);ox,oy=u['slot'];tup=(u['packet'],7,ox-x,oy-y,dh,ox,oy)
  if tup in HB:continue
  L.append(dict(**u,age=age,protected_transfer=tup))
 origins[str(tuple(s))]=dict(target_slot=s,height=height,residue=residue,min_age=age_min,eligible_outputs=L,eligible_ages=sorted({u['age']for u in L}),birth_steps=sorted({u['step']for u in L}))
a=origins[str((-1,1))];q=origins[str((-1,2))];c=origins[str((0,2))]
assert q['eligible_ages']==[11,14,15]and a['eligible_ages']==[18,19,22,23]and c['eligible_ages']==[18,19,22,23]
assert max(q['eligible_ages'])<min(a['eligible_ages'])and max(q['eligible_ages'])<min(c['eligible_ages'])
assert min(q['birth_steps'])>max(a['birth_steps'])and min(q['birth_steps'])>max(c['birth_steps'])
O=dict(status='AUTHOR_ALL_ORIGIN_CHOICES_BLOCKED_BY_SIGNED_U_JOINT_ORDER',scope='One saved packet word at its given phase/initial pose under no entry black identities above H=-10. All earlier outputs are allowed as origins even if already consumed. No fixed greedy matching, age-bin choice, full counted-kernel clause or generic search cap is used. Not closure of U1 funding.',word_including_goal=word,strict_packets=349,initial_pose=J['initial_pose'],phase=phase,modulus=mod,initial_high_cutoff=F,initial_high_tokens=0,goal=goal,origins=origins,contradiction='Aq<=15<18<=min(Aa,Ac), contradicting signed Aq>=min(Aa,Ac). Equivalently every q birth is later than every a/c birth.',dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[S,LP,HP,Path(__file__).resolve()]})
T=W/'chronology_dcuv/delayed_height_probe/u1_k5_joint_origin_obstruction.json';T.write_text(json.dumps(O,indent=2)+'\n');print({s:v['eligible_ages']for s,v in origins.items()});print(T)

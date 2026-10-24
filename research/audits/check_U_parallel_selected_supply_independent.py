from pathlib import Path
from collections import Counter
import hashlib,json
SELF=Path(__file__).resolve();ns={'__file__':str(SELF.parent/'check_U_first_helper_ports_independent.py')};exec((SELF.parent/'check_U_first_helper_ports_independent.py').read_text().split('rows=[];gates=[];adjacent_rejects=[]')[0],ns)
globals().update({k:ns[k]for k in('ROOT','G','IDS','xy','rotation','chords','meet','pt','edge')})
B=ROOT/'core_periodicity_new/U_parallel_selected_supply_frozen_20261023_2026';man=json.loads((B/'manifest.json').read_text())
for p,h in man['files'].items():assert hashlib.sha256((B/p).read_bytes()).hexdigest()==h
selected={0:1j,1:1j,4:1+2j,5:1+2j,6:3j,7:3j,8:3j,9:3j};L={0j,1j,1,1+1j};O=G[7]['O'];rows=[];gates=[]
for s in(7,8,9):
 assert O<=G[s]['O'];sc=chords(s)
 for a in IDS:
  assert selected[a]in G[a]['I']
  for h in(0,2):
   for q in sorted(O,key=xy):
    p=q-rotation(selected[a],h);ctx={p+rotation(i,h)for i in G[a]['ctx']};cc=chords(a,p,h)
    if(sum(xy(p))+h)%2:why='wrong_sector'
    elif ctx&L:why='permanent_left_star_context'
    else:
     bad=False
     for j,x in enumerate(sc):
      for k,y in enumerate(cc):
       hit=meet(*x,*y)
       if hit and not(j==len(sc)-1 and k==0 and(p,h)==(G[s]['end'],G[s]['h'])and hit=={pt(x[1])}):bad=True
     if bad:why='past_source_chord_contact'
     else:
      why='arm_to_plain_D_exact_age6';assert(a,p,h,q)==(0,1+3j,2,1+2j);gates.append((s,a,*xy(p),h))
    rows.append(dict(source=s,consumer=a,head=[*xy(p),h],source_base_output=xy(q),reason=why))
counts=Counter(r['reason']for r in rows);assert counts==dict(wrong_sector=192,permanent_left_star_context=231,past_source_chord_contact=6,arm_to_plain_D_exact_age6=3)
ref=json.loads((B/'U_parallel_selected_supply.json').read_text());key=lambda r:(r['source'],r['consumer'],tuple(r['head']),tuple(r['source_base_output']))
assert{key(r):r['reason']for r in rows}=={key(r):r['reason']for r in ref['rows']}
W=-1+3j;path=[1+5j,3+3j,1+1j,W];qs=[1+2j,1+1j,1j];consumer=chords(0,1+3j,2)[0]
for s in(7,8,9):
 sc=chords(s)
 for i,(u,v)in enumerate(zip(path,path[1:])):
  assert{u,v}==set(edge(qs[i]));assert meet(*consumer,u,v)==({pt(path[0])}if i==0 else set())
  for j,(x,y)in enumerate(sc):
   if j==0:x=W
   assert meet(x,y,u,v)==({pt(W)}if j==0 and i==2 else set())
# Exact diagonal-angle units pi/4: final D is SW, bridge SE/SW/NW, source tangent N.
angles=[5,7,5,3,2];turns=[(b-a+3)%8-3 for a,b in zip(angles,angles[1:])];assert turns==[2,-2,-2,-1]and sum(turns)==-3
assert [n for n in(2+4,2-4)if n>=0]==[6]
out=dict(status='PASS universal U-base parallel distinguished supply: only arm to plain D at exact age6',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),counts=dict(counts),rows=rows,gates=gates,bridge=list(map(xy,path)),bridge_ids=list(map(xy,qs)),closing_turns_pi_over_4=turns,forced_full_source_entry_C_age=6,analytic='The arm remains current by identity assumption and the other two bridge edges are permanent U left-star IDs. Direct source partial-U/C-tail and final D-base intersections plus current-edge barrier and U-entry simplicity give a Jordan loop without any whole-cohort first-touch premise. Total turn(n-2)pi/2 forces6. One arm per source can be spent once; U-base outputs supply no parallel V/U distinguished input. C-tail outputs remain separately charged.',scope='Any same-factor U-family BASE output to a parallel/antiparallel distinguished input. Not all-input supply, original component separation, independent U-birth bound or capture.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(counts)

from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];D=ROOT/'core_periodicity_new';B=D/'plain_U_first_touch_merger_frozen_20261023_2002';m=json.loads((B/'manifest.json').read_text())
for p,s in m['files'].items():assert hashlib.sha256((B/p).read_bytes()).hexdigest()==s
ns={'__file__':str(SELF.parent/'check_U_first_helper_ports_independent.py')};exec((SELF.parent/'check_U_first_helper_ports_independent.py').read_text().split('rows=[];gates=[];adjacent_rejects=[]')[0],ns)
G=ns['G'];chords=ns['chords'];meet=ns['meet'];pt=ns['pt'];rotation=ns['rotation'];xy=ns['xy'];raws=ns['raws'];walk=ns['walk'];R=G[7]['O'];z=2+4j;fp=4j;rows=[];startup=[]
def end(a,p,h):return(p+rotation(G[a]['end'],h),(h+G[a]['h'])%4)
def bad_past(a,p,h,b,bp,bh):
 old=chords(b,bp,bh);new=chords(a,p,h);be,he=end(b,bp,bh)
 for i,x in enumerate(old):
  for j,y in enumerate(new):
   hit=meet(*x,*y)
   if hit and not(i==len(old)-1 and j==0 and(p,h)==(be,he)and hit=={pt(x[1])}):return True
 return False
for first in G:
 if first in(7,8,9):
  star={fp+q for q in(0j,1j,1+0j,1+1j)}
  for goal in(0,1):assert star&{2+3j+rotation(q,3)for q in G[goal]['ctx']}
  startup.append(dict(first=first,reason='permanent_star'));continue
 assert z in{fp+q for q in G[first]['O']}
 base=0 if first<2 else 4;p=fp;h=0
 for tick,ch in enumerate(raws[first]):
  if tick>=len(raws[base]):assert p!=z
  h=(h+(1 if ch=='R'else-1))%4;p+=(1j,1+0j,-1j,-1+0j)[h]
 for goal in(0,1):
  gp=2+3j;gh=3;assert z in{gp+rotation(q,gh)for q in ns['K']};assert z not in{gp+rotation(q,gh)for q in G[goal]['I']}
  for a in G:
   for h in range(4):
    for k,i in enumerate(sorted(G[a]['I'],key=xy)):
     p=z-rotation(i,h);ep,eh=end(a,p,h);ctx={p+rotation(q,h)for q in G[a]['ctx']}
     if(sum(xy(p))+h)%2:reason='wrong_sector'
     elif ctx&R:reason='unchanged_source_U_output_in_context'
     elif bad_past(a,p,h,7,0j,0)or bad_past(a,p,h,first,fp,0):reason='past_source_or_first_successor_chord'
     elif bad_past(goal,gp,gh,a,p,h):reason='future_first_helper_chord'
     else:
      assert h==3 and p.imag in(4,5)and ep.imag>=5;reason='clock1_head_too_low_or_clock5_exit_too_high'
     rows.append(dict(first=first,goal=goal,consumer=a,head=(*xy(p),h),slot=k,reason=reason))
 startup.append(dict(first=first,reason='guard_unretirable',guard=xy(z)))
counts=Counter(r['reason']for r in rows);assert counts==dict(wrong_sector=460,unchanged_source_U_output_in_context=350,past_source_or_first_successor_chord=20,future_first_helper_chord=33,clock1_head_too_low_or_clock5_exit_too_high=57)
ref=json.loads((B/'plain_U_first_touch_merger.json').read_text());key=lambda r:(r['first'],r['goal'],r['consumer'],tuple(r['head']),r['slot'])
assert{key(r):r['reason']for r in rows}=={key(r):r['reason']for r in ref['guard_clearer_rows']}
zero=[];turn=[]
for a in(0,4,7):
 assert G[a]['h']==0 and G[a]['end'].imag>0;w=rotation(G[a]['end'],3);assert w.imag>=0;zero.append((a,G[a]['end'].imag,w.imag))
for a in(1,5,8):assert G[a]['h']==3 and G[a]['end'].imag>=2;turn.append((a,G[a]['end'].imag))
out=dict(status='PASS plain-U reset component first-touch imports an outside component',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),counts=dict(counts),startup=startup,rows=rows,zero_C_y_bounds=zero,turn_y_bounds=turn,analytic='Signed six-gate law leaves D/DC(2,3,W),age5. Its actual immediate source successor is at(0,4,N). U-family successor permanent star blocks target; D/V-family successor fresh z(2,4) must retire strictly before target because it is target core. All old nine U outputs remain current. Complete context and actual source/F/future-target chord tests retain exact full-pose adjacent endpoints. Remaining clearers all W,y4/5,exit y>=5. At C1 entries have y>=6 after N zero runs plus one N-to-W positive-C packet; at C5 positive tails overshoot while W zero runs cannot lower exit y to3. Hence no guard retirement.',scope='Reset genealogy immediately before genuine plain U, so its component has exactly nine fresh outputs. First touch, if any, must import outside support. Not arbitrary historical components, UC/UCC, post-merger evolution or global U budget.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(counts)

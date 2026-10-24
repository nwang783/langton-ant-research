from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import hashlib,json
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
SELF=Path(__file__).resolve();D=ROOT/'core_periodicity_new';B=D/'U_recycled_q_consumer_frozen_20261023_1954';m=json.loads((B/'manifest.json').read_text())
for r in m['files']:assert hashlib.sha256((B/r['file']).read_bytes()).hexdigest()==r['sha256']
for p,s in m['dependencies'].items():assert hashlib.sha256((D/p).read_bytes()).hexdigest()==s
ns={'__file__':str(SELF.parent/'check_U_first_helper_ports_independent.py')};exec((SELF.parent/'check_U_first_helper_ports_independent.py').read_text().split('rows=[];gates=[];adjacent_rejects=[]')[0],ns)
G=ns['G'];chords=ns['chords'];meet=ns['meet'];pt=ns['pt'];q=-1+2j;AA=-1+3j;BB=-3+5j;star={0j,1j,1+0j,1+1j};source=(-1-1j,-1+7j);rows=[];surv=[]
for s in G:
 for h in range(4):
  for k,i in enumerate(sorted(G[s]['I'],key=xy)):
   p=q-rotation(i,h);cc=chords(s,p,h);ctx={p+rotation(z,h)for z in G[s]['ctx']}
   if(sum(xy(p))+h)%2:reason='wrong_sector'
   elif ctx&star:reason='permanent_source_L_star_context'
   elif meet(*cc[0],*source):
    reason='consumer_base_contacts_source_U';assert all((p,h)!=(G[a]['end'],G[a]['h'])for a in(7,8,9))
   elif s in(7,8,9):reason='signed_recycled_q_cannot_feed_U'
   else:
    assert s in(4,5)and p==-1+5j and h==2 and i==3j;reason='exact_V_consumer';assert cc[0][1]==BB
    assert meet(*cc[0],BB,AA)=={pt(BB)};assert{p+rotation(z,h)for z in G[s]['I']}=={q,-2+3j};surv.append((s,xy(p),h))
   rows.append(dict(consumer=s,head=(*xy(p),h),input_slot=k,reason=reason))
counts=Counter(r['reason']for r in rows);assert counts==dict(wrong_sector=46,permanent_source_L_star_context=35,consumer_base_contacts_source_U=5,signed_recycled_q_cannot_feed_U=4,exact_V_consumer=2)
ref=json.loads((B/'02_U_recycled_q_consumer.json').read_text());print('author reasons',ref['counts'])
# Compare exact placements in each category, allowing prose-only reason labels.
ours={(r['consumer'],tuple(r['head']),r['input_slot']):r['reason']for r in rows};assert len(ours)==92
for r in ref['all_92_consumer_alignments']:
 k=(r['consumer'],tuple(r['head']),r['input_slot']);assert k in ours
 if r['reason']in counts:assert ours[k]==r['reason']
for s in(7,8,9):
 for j,(x,y)in enumerate(chords(s)):
  if j==0:x=AA
  assert meet(x,y,BB,AA)==({pt(AA)}if j==0 else set())
# Units pi/4; V alpha variable between1 and2. Closing joins are3-alpha and3.
closing=(-1,6);open_angle=(1,-2);assert closing[0]+open_angle[0]==0 and closing[1]+open_angle[1]==4
assert[n for n in range(20)if 2*n+4 in(-8,8)]==[2]
out=dict(status='PASS exact V/VC consumer and age2 of genuine U recycled-q',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),counts=dict(counts),all_rows=rows,survivors=surv,forced_Cgap=2,selected_helper=(-2,3),selected_helper_latest_relative_birth=-1,analytic='Current q edge and automatic U-entry simplicity close the source-midpoint to V-base-exit arc. Literal source partial U/C tails and consumer base avoid the edge except endpoints. Exact alpha cancellation gives n*pi/2+pi and n2. Selected helper has produced minimum3, so if produced its full birth is at most source−1 and the same ID is already current at source entry. At factor-first creator it is a separate unconsumed singleton entry root, giving a genuine merger. Later creators need not have separate components.',scope='Not q permanence: signed actual UCC-to-V age2 control realizes the gate. No arbitrary later-creator component separation or global event bound.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],dict(counts))

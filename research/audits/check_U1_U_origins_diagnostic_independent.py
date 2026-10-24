from pathlib import Path
from collections import Counter
import hashlib,json
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
SELF=Path(__file__).resolve();D=ROOT/'core_periodicity_new';B=D/'U1_U_origins_diagnostic_frozen_20261023_1930';man=json.loads((B/'manifest.json').read_text())
for f in man['files']:assert hashlib.sha256((B/f['file']).read_bytes()).hexdigest()==f['sha256']
for f,sha in man['dependencies'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==sha
M=json.loads((D/'atomic_core_record_interface_frozen_20261023_1359/04_root_out.json').read_text());weights=json.loads(Path(M['potential_file']).read_text())['values'];assert hashlib.sha256(Path(M['potential_file']).read_bytes()).hexdigest()==M['potential_sha256']
H=lambda z:int(z.real+z.imag);A=[H(rotation(-1+1j,h))+weights[f'c{h}']for h in range(4)];assert A==[0,22,20,10]
K={q for q,b in walk(mark)[2].items()if b};G={};peaks={};enlarged={};C=raws[1][len(raws[0]):]
for s in(7,8,9):
 e,h,_,flip=walk(raws[s]);req=walk(raws[s]+mark)[2];bl={q for q,b in req.items()if b};I=bl-K;O=(bl^flip)-{e+rotation(q,h)for q in K};G[s]=(I,O,set(req)|K)
 for phase in range(4):
  peak=max(2*H(rotation(e,phase))+A[(phase+h)%4],*(2*H(rotation(o,phase))+weights[f'w_{s}_{j}_{phase}']for j,o in enumerate(sorted(O,key=xy))))
  peaks[s,phase]=peak;prefix=[];p=0j;hh=phase
  for atom in[raws[7]]+[C]*(s-7):
   ep,dh,_,_=walk(atom);p+=rotation(ep,hh);hh=(hh+dh)%4;prefix.append(2*H(p)+A[hh])
  enlarged[s,phase]=max(peak,*prefix)
assert peaks=={(a,h):v for a,h,v in M['created_peaks']if a in(7,8,9)}
def chords(s,p,h):
 out=[]
 for atom in[raws[7]]+[C]*(s-7):
  first=2*p+rotation(-1-1j,h);e,dh,_,_=walk(atom);p+=rotation(e,h);h=(h+dh)%4;out.append((first,2*p+rotation(-1-1j,h)))
 return out
def det(x,y):return int(x.real*y.imag-x.imag*y.real)
def on(q,a,b):return det(q-a,b-a)==0 and ((q-a).conjugate()*(q-b)).real<=0
def touch(ab,cd):
 a,b=ab;c,d=cd;x=det(b-a,c-a);y=det(b-a,d-a);z=det(d-c,a-c);w=det(d-c,b-c)
 return x*y<0 and z*w<0 or any((on(c,a,b),on(d,a,b),on(a,c,d),on(b,c,d)))
goal=chords(7,0j,0);goalI=sorted(G[7][0],key=xy);star={0j,1j,1+0j,1+1j};rows=[];needed=set();mp={s:i for i,s in enumerate((0,1,4,5,6,7,8,9))}
for s in(7,8,9):
 for o in sorted(G[s][1],key=xy):
  for slot,i in enumerate(goalI):
   for h in range(4):
    p=i-rotation(o,h);phase=(h+1)%4;height=H(rotation(p,1));entry=2*height+A[phase];created=2*height+peaks[s,phase];new=2*height+enlarged[s,phase]
    row=dict(source=s,output=xy(o),input=xy(i),pose=(*xy(p),h),entry=entry,created=created,enlarged=new)
    if(sum(xy(p))+h)%2:reason='wrong_sector'
    elif{p+rotation(q,h)for q in star}&G[7][2]:reason='permanent_source_L_star_meets_goal_complete_context'
    elif o in(2+0j,2+1j):reason='signed_original_U1_east_pair_origin_exclusion'
    elif max(entry,created)>=30:reason='old_source_record_already_funds_goal'
    elif any(touch(a,b)for a in chords(s,p,h)for b in goal):reason='source_atomic_chord_contacts_later_goal'
    else:
     ages=[k for k in(3,4)if slot<2 and k%4==h]+[5];v=rotation(-p,-h);keys=[(mp[s],mp[7],*xy(v),(-h)%4,*xy(o),age)for age in ages];row.update(ages=ages,keys=keys);needed.update(keys);reason='pending'
    row['reason']=reason;rows.append(row)
found=set()
with(D/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv').open()as f:
 for line in f:
  q=tuple(map(int,line.split()[:8]))
  if q in needed:found.add(q)
for r in rows:
 if r['reason']=='pending':
  r['allowed']=[a for a,k in zip(r['ages'],r['keys'])if k not in found];r['reason']='necessary_origin_template_not_attainment'if r['allowed']else'signed_count5_excludes_all_possible_age_classes';r['survives_atomic']=bool(r['allowed'])and max(r['entry'],r['enlarged'])<30
ref=json.loads((B/'02_U1_U_origins_after_permanence.json').read_text());refs={(r['source'],tuple(r['source_output']),tuple(r['goal_input']),tuple(r['source_pose'])):r for r in ref['all_alignments']}
for r in rows:
 a=refs[r['source'],r['output'],r['input'],r['pose']];assert r['reason']==a['reason']and(r['entry'],r['created'],r['enlarged'])==(a['source_entry'],a['source_created'],a['source_enlarged'])
 if'allowed'in r:assert r['allowed']==a['unexcluded_count_classes']and r['survives_atomic']==a['also_survives_enlarged_history']
counts=Counter(r['reason']for r in rows);assert len(rows)==720 and counts==ref['counts'];keep=[r for r in rows if r['reason']=='necessary_origin_template_not_attainment'];assert len(keep)==36 and sum(r['survives_atomic']for r in keep)==30
r=next(r for r in keep if r['source']==7 and r['pose']==(-2,4,2)and r['input']==(-1,2));assert r['output']==(-1,2)and(r['entry'],r['created'],r['enlarged'])==(22,14,14)
out=dict(status='PASS necessary individual U1 U-origin diagnostic, not attainment',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),counts=dict(counts),original_survivors=36,atomic_survivors=30,all_rows=rows,scope='Complete literal masks, full-source original entry/creation scores and separately enlarged history; exact count3/4 and overflow5 only. No joint ledger, physical word, funding closure, U/component bound or original11/13 upgrade.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(dict(counts))

from pathlib import Path
from collections import Counter,defaultdict
from fractions import Fraction
import hashlib,json
P=Path(__file__).resolve();S=P.with_name('check_U1_young3_shadow_independent.py');exec(compile(S.read_text().split('rows=[];cases=[]')[0],str(S),'exec'))
B=ROOT/'core_periodicity_new/atomic_crossing_retirement_frozen_20261023_1429';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_atomic_crossing_early_retirement.json').read_text());D=ROOT/'core_periodicity_new';X=json.loads((D/'atomic_crossing_contexts_frozen_20261023_1414/02_atomic_center_crossing_contexts.json').read_text());ind=json.loads(P.with_name('check_atomic_crossing_contexts_independent.json').read_text());owncross={(r[0],r[1],tuple(r[2])):r for r in ind['crossings']}
C5={tuple(map(int,l.split()[:8]))for l in(D/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv').read_text().splitlines()};HB={tuple(map(int,l.split()[:7]))for l in(D/'chronology_dcuv/protected_patch2.tsv').read_text().splitlines()};mp={a:i for i,a in enumerate(ids)}
def det(a,b):return int(a.real*b.imag-a.imag*b.real)
def intersect(a,b,c,d):
 u=b-a;v=d-c;den=det(u,v)
 if den:return 0<=Fraction(det(c-a,v),den)<=1 and 0<=Fraction(det(c-a,u),den)<=1
 if det(c-a,u):return False
 return all(max(min(x,y),min(z,w))<=min(max(x,y),max(z,w))for x,y,z,w in[(a.real,b.real,c.real,d.real),(a.imag,b.imag,c.imag,d.imag)])
def zeroreach(end,target,h):
 z=rotation(target-end,-h);dx,dy=xy(z)
 if dx<0 or dy<0:return False
 # Solve dy-dx=2V+4U, D=dx-V>=0 exactly without a run-length cutoff.
 return any(dy-dx-2*v>=0 and(dy-dx-2*v)%4==0 for v in range(dx+1))
queries=[];results=[]
for ci,c in enumerate(X['crossings']):
 typ=c['first_atom']
 if typ not in('V','U'):continue
 tx,ty,th=c['later_pose'];N=3 if th==1 else 5;target=complex(tx,ty);srcbase=4 if typ=='V'else 7;d0=2*G[srcbase][0]
 cr=owncross[typ,c['later_atom'],(tx,ty,th)];forced={complex(*z)for z in cr[5]};assert forced=={complex(*z)for z in c['strict_prior_retirement_outputs']}
 remains=defaultdict(list)
 for output in sorted(forced,key=xy):
  remains[output]=[]
  for src in range(srcbase,srcbase+3):
   assert output in G[src][4]
   for age in range(N+1):
    h=(-age)%4
    for dst in ids:
     for slot in G[dst][3]:
      pos=output-rotation(slot,h);hk=(src,dst,*xy(pos),h,*xy(output));ck=(mp[src],mp[dst],*xy(pos),h,*xy(output),min(age,5))
      if age<counts[src]:reason='BEFORE_SOURCE_FULL_EXIT'
      elif(int(pos.real+pos.imag)+h)%2:reason='SECTOR'
      elif hk in HB:reason='SIGNED_HB'
      elif ck in C5:reason='SIGNED_COUNT5'
      else:
       a=-1-1j;b=a+d0;cc=2*pos+rotation(-1-1j,h);dd=cc+2*rotation(G[base[dst]][0],h)
       if intersect(a,b,cc,dd):assert age in(3,5);reason='EARLIER_CLOSED_CHORD_CONTACT'
       elif c['later_atom']!='C'and age+counts[dst]>N:reason='CONSUMER_TAIL_ENDS_AFTER_LATER_BASE'
       else:
        end=pos+rotation(G[dst][0],h);eh=(h+G[dst][1])%4
        if age+counts[dst]==N and eh==th and not zeroreach(end,target,th):reason='ZERO_C_TO_CROSSING_IMPOSSIBLE'
        else:reason='UNRESOLVED_NONCONTACT_RETIRER';remains[output].append((src,age,dst,xy(slot)))
      queries.append((ci,src,xy(output),age,dst,xy(slot),reason,hk,ck))
 hard=sorted(xy(z)for z,opts in remains.items()if not opts);assert hard
 results.append(dict(crossing_index=ci,hard_slots=hard,entry_gap=N))
auth={(q['crossing_index'],q['source_full'],tuple(q['source_output']),q['full_source_age'],q['consumer_full'],tuple(q['input'])):q for q in J['queries']};assert len(queries)==len(auth)==47610
for row in queries:
 q=auth[row[:6]];assert row[6]==q['reason']and row[7]==tuple(q['HB_key'])and row[8]==tuple(q['count5_key'])
ac={c['crossing_index']:c for c in J['cases']};assert len(results)==38
for r in results:assert r['hard_slots']==sorted(map(tuple,ac[r['crossing_index']]['hard_slots']))
out=dict(status='PASS independent complete V/U source cohort first-retirement and earlier-contact theorem',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),queries=len(queries),query_reasons=dict(Counter(q[6]for q in queries)),crossings=results,scope='Proper V/U-first crossings at exact entry-C3(E)/5(W) force an earlier nonadjacent CLOSED source-chord contact. Every full-source tail and internal-C-target exception retained. No word/box cutoff, no arbitrary-gap or endpoint/touch/overlap exclusion, no fresh-root/beta/fuel/global theorem.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k!='crossings'})

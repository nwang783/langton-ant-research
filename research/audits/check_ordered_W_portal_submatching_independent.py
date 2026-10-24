from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];p=SELF.parent/'check_ordered_W_archive_transport_independent.py';ns={'__file__':str(p)};exec(p.read_text().split('ports=dict')[0],ns)
walk,W,M,xy,names,raw,ctx,I,O,why=[ns[x]for x in('walk','W','M','xy','names','raw','ctx','I','O','why')];D=ROOT/'seven_word_spatial_return_2026-10-23';portal={'V':1j,'VCC':1j,'U':-1+2j,'UCC':-1+2j};cc=Counter();kept=[];cuts=[]
for s in names:
 for o in O[s]:
  for c in'DVU':
   for i in I[c]:
    entry=o+i;r=why(s,c,o,entry,2,2)
    if r:cc[r]+=1;continue
    if c=='V'and i==3j:
     assert s in portal and o==portal[s];kept.append((s,xy(o),xy(entry)));cc['portal']+=1;continue
    assert s in('VCC','UCC')and raw[s]['h']==2
    delta=entry-raw[s]['p']
    if delta.real>0 or delta.imag>0:r='Scone'
    elif c=='D':assert delta==-2j;r='unchanged_x_multiple4'
    else:
     assert c=='U'and delta in(0,-1-1j);word=''.join(W[n]for n in s)+(''if delta==0 else W['D'])+W['U'];rr=walk(word+M);assert not rr['feasible']and rr['i']<len(word);r='literal_RAW';cuts.append((s,xy(delta),rr['i'],xy(rr['q'])))
    cc[r]+=1
assert cc=={'sector':264,'COUNT5':266,'portal':4,'Scone':4,'unchanged_x_multiple4':2,'literal_RAW':4}
assert set(kept)=={('V',(0,1),(0,4)),('VCC',(0,1),(0,4)),('U',(-1,2),(-1,5)),('UCC',(-1,2),(-1,5))}
orders=[]
for s in('V','U'):
 for c in('V','U'):
  earlier=portal[s]*1j;later=raw[s]['p']*1j+portal[c]*1j;diff=later-earlier
  assert diff.real<=-3 and diff.imag>=0;orders.append((s,c,int(-diff.real),int(diff.imag)))
vis=[]
for f,p in [('F',2-5j),('Q',4-5j),('B',5-4j)]:
 tr=walk(W[f]+W['C']+M);ct={p+q*(-1j)for q in tr['req']};assert min(q.real for q in ct)==-3
 for o in O['V']:
  q=-5+2j+o*(-1j);assert q not in ct;vis.append((f,xy(o),xy(q)))
assert len(vis)==18 and max(q.imag for q in O['V'])==2
assert (-5+2j)+raw['V']['p']*(-1j)==-2+1j
assert (-6+1j)+raw['V']['p']*(-1j)==-3+0j
assert next((i,c)for i,(q,h,c)in enumerate(ctx['V']['reads'])if q==3j)==(19,'L')and len(raw['V']['reads'])==18
mp=D/'ordered_W_portal_submatching_manifest.json';mh=hashlib.sha256(mp.read_bytes()).hexdigest();assert mh=='23f62a2c925b627cc2fa5e3efa244390c5ba5ddd18a2ef810b8f2ff485940a13'
mf=json.loads(mp.read_text())
for f,h in mf['files'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
for f,h in mf['dependencies'].items():assert hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h
control=SELF.parent/'check_W_seal_withdrawal_controls_independent.json';assert json.loads(control.read_text())['status'].startswith('PASS')
out={'status':'PASS weakened all-length W portal submatching, NOT rejected at-most-one seal','manifest_sha256':mh,'classification':dict(cc),'four_retained_portals':kept,'four_RAW_conflicts':cuts,'all_length_order_d_constant_pairs':orders,'eighteen_output_visibility_checks':vis,'independent_positive_control_report_sha256':hashlib.sha256(control.read_bytes()).hexdigest(),'analytic':['The full544 actual output/input roles retain all FOUR plain/boundary V-A/U-q portals. No arbitrary N/W/S portion of a plain source history is removed. Every other survivor is a completed double-tail source already facing normalized S, with no remaining C; the ten exclusions therefore use a genuinely exhaustive single-stage cone or unique zero-C word.','Potential W portal sites strictly decrease in x along their source order. Between adjacent potential portal sources only plain D bases can occur; all four type pairs have x decrease at least3 plus d. A consuming E-V head is portal minus(3,0), while E heads strictly increase in x. Actual consumed portals are therefore a once-only REVERSE partial matching, not a complete stack or at-most-one transfer.','For a W head(-A,1+B), portal-consuming E V enters(-A-4,1+B) or(-A-5,B). Its outputs have local y<=2, hence physical x at most-A-2 or-A-3. Since future context minx=-3, only V-family A1 can be visible; signed first-W-D forces exactly earlier prefixD and B1. All six actual outputs at(-5,2,E) miss all three future contexts. This endpoint argument does not constrain or omit intervening S runs.','Every nonportal output has no old-eight external consumer under the signed young-transfer and present age2 inventory. The ordered residual ledger includes core absorption, so these identities stay current. Signed direct future site disjointness then preserves them physically through foreign, returned RAW C and marker. Unused portals are retained as well; arbitrarily many different portals may be spent.','The portal is plain V input(0,3), whose actual first L is context tick19, NEXT word RAW phase2. Its consuming V exits(-A-1,B,E) or(-A-2,B-1,E), with A>=1, so exit x<=-2 whereas foreign entry x is2/4/5. It cannot be the last E packet: the physical retirement occurs in a later E word before foreign entry. The identity can enter active core before that read. This residual I/O matching does not delete core, WHITE guard, delayed-marker or functional color effects. Each consuming V also spends a distinct older selected input only by the separately signed transport bottleneck.'],'scope':'Exactly the three necessary old-C first-return interfaces, arbitrary stage lengths, ONE foreign and returned rawC. No seal, contraction, at-most-one spending, second foreign, whole-state quotient or capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])

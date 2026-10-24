from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__).resolve();R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
files={'PHYSICAL_LAST_SPINE_TERMINAL_EXCURSIONS.md':'a19a9940d5eb4967f658ae010143c7c47793a7810b5c73fd275632d6b7620ef5','certify_physical_last_spine_excursions.py':'239cb873e77b18a19d0df023a98266fa8419039231f1557f45e3f7ee05d0b0fb','physical_last_spine_excursions_certificate.json':'dfe766eaa05aee756d7e187c815452ce987ea205c1fc6aafea35c8d6b75cf125'}
for f,h in files.items():assert sha(D/f)==h
J=json.loads((D/'physical_last_spine_excursions_certificate.json').read_text())
for f,h in J['dependencies'].items():assert sha(D/f)==h
lib=S.with_name('check_exit_component_flux_independent.py');ns={'__file__':str(lib)};exec(lib.read_text().split('base={};summaries={}')[0],ns);analyze,V,xy,future,phases=[ns[k]for k in('analyze','V','xy','future','phases')]
def decomposition(w,h):
 a=analyze(w,h);P=a['P'];E=a['E'];d=a['d'];lab=a['labels'];res=[]
 def at(t):k,i=divmod(t,P);return E[i][0]+k*d
 for c in a['comp']:
  cyc=c['cycle'];start=a['edges'][cyc[0]][3];t=start;rows=[];selected=0;used=[]
  for q in cyc:
   target,nu,lam,i,gap=a['edges'][q];assert i==t%P and gap>0;u=t+1;v=t+gap;selected+=1 if w[i]=='R'else-1;assert at(u)==at(v)and(gap-1)%4==0
   marks=[j for j in range(u,v+1)if at(j)==at(v)];parts=[]
   for f,g in zip(marks,marks[1:]):
    ww=''.join(w[z%P]for z in range(f,g));assert(g-f)%4==0 and (E[f%P][1]-E[g%P][1])%4 in(0,2)
    parts.append(dict(start=f,end=g,length=g-f,word=ww,charge=ww.count('R')-ww.count('L'),incoming_heading=E[f%P][1],return_heading=E[g%P][1],component_event_counts={str(k):v for k,v in Counter(lab[z%P]for z in range(f,g)).items()}))
   ww=''.join(w[z%P]for z in range(u,v));assert sum(x['length']for x in parts)==gap-1
   rows.append(dict(selected_source_time=t,target_arrival_time=u,target_last_time=v,terminal_word=ww,length=gap-1,charge=ww.count('R')-ww.count('L'),target_position=xy(at(v)),component_event_counts={str(k):v for k,v in Counter(lab[z%P]for z in range(u,v)).items()},consecutive_same_physical_cell_returns=parts));used.extend(range(t,v));t=v
  assert t==start+P and used==list(range(start,start+P)) and at(t)==at(start)+d
  assert selected+sum(z['charge']for z in rows)==w.count('R')-w.count('L')
  res.append(dict(basin=c['cid'],O=c['O'],I=c['I'],period_interval=[start,t],selected_actual_turn_charge=selected,terminal_excursions=rows))
 return res
base={};rotations=[]
for n,z in J['base_controls'].items():
 rows=decomposition(z['word'],z['heading']);assert xy(analyze(z['word'])['d'])==z['drift'];base[n]=rows
 for r,rr in zip(rows,z['spine_partitions']):
  for k in('basin','O','I','period_interval','selected_actual_turn_charge'):assert r[k]==rr[k]
  for row,au in zip(r['terminal_excursions'],rr['terminal_excursions']):
   for k,val in row.items():assert val==au[k],(n,k)
 for h in range(4):
  rr=decomposition(z['word'],h);sig=lambda zz:[(r['O'],r['I'],[(e['length'],e['charge'])for e in r['terminal_excursions']])for r in zz]
  assert sig(rr)==sig(rows);rotations.append(dict(name=n,heading=h,partitions=len(rr),signatures=sig(rr)))
assert len(rotations)==20
small=next(c for c in base['S104']if c['O']==4);assert[e['length']for e in small['terminal_excursions']]==[0,0,4,96]
long=small['terminal_excursions'][-1];assert long['component_event_counts']=={'1':10,'0':86};assert[(x['length'],x['charge'])for x in long['consecutive_same_physical_cell_returns']]==[(8,-2),(76,8),(8,0),(4,4)]
# Fresh whole empty-seed trajectory, preserving every original physical birth ID.
lit=J['literal_standard'];cuts={int(k):z for k,z in lit['full_fields'].items()};B={};p=0j;h=0;ev=[];whole=[];tails=[]
for t in range(max(cuts)+1):
 if t in cuts:
  z=cuts[t];assert z['head']==xy(p)and z['heading']==h and z['full_BLACK']==sorted(map(xy,B));whole.append((t,len(B),xy(p),h))
 if t in(9977,10289):
  tw,dr,dead,tests=future(B,p,h);assert tw==J['base_controls']['S104']['word']and tw in phases;tails.append((t,len(B),xy(dr),tests))
 if t==max(cuts):break
 c='L'if p in B else'R';z=dict(time=t,position=xy(p),heading=h,turn=c)
 if c=='L':z['R_owner']=B.pop(p)
 else:B[p]=t
 ev.append(z);h=(h+(1 if c=='R'else-1))%4;p+=V[h]
assert ev[10320:10416]==lit['all96_terminal_reads']and ev[10320:10328]==lit['negative_first_return']and ev[10404:10412]==lit['neutral_later_first_return']
assert ''.join(z['turn']for z in ev[10289:10393])==J['base_controls']['S104']['word'];assert [ev[t]['R_owner']for t in[10320,10322,10323,10324,10325]]==[10316,10242,10295,10296,10321]
assert ev[10320]['position']==[-24,2]and ev[10320]['heading']==2 and ev[10328]['heading']==0 and ev[10328]['position']==[-24,2]
assert all(ev[t]['position']!=[-24,2]for t in range(10321,10328));assert [(t,m)for t,m,p,h in whole[:2]]==[(10320,758),(10328,756)]
report=dict(status='PASS all-cap physical last-spine whole-period decomposition and actual WHITE standard negative elementary terminal return',bindings=files,dependencies=J['dependencies'],five_full_partitions=base,all20_rotations=rotations,fresh_blank_read_count=len(ev),complete_field_cuts=whole,full_future_checks=tails,negative_owners=[(t,ev[t]['R_owner'])for t in[10320,10322,10323,10324,10325]],analytic_review=[
'For each selected physical last edge, actual last-target time minus last-source time is positive. Signed embedded primitive cycle has total voltage+1, so its positive gaps telescope to exactly P. Consistently lifted final times therefore partition the ENTIRE actual period for EACH spine, irrespective of basin membership.',
'Removing the initial actual departure from a gap leaves the actual trajectory from its arrival at the target to its last read of that SAME physical cell. Position closes, but heading may differ by180degrees. Alternating horizontal/vertical moves and equal signed displacement give length divisible by4. Splitting at all physical returns is unique and keeps every read; no fixed word, age or multiplicity cap is used.',
'GLOBAL growth is selected actual R/L signs plus all terminal-excursion charges. Effective geometric spine turning zero cannot replace actual selected turns without recording the incoming heading differences. Different spines partition the same period and cannot be added as disjoint basin budgets.',
'Independent complete histories/full-drift last arrows reconstruct five supplied words and20 rotations. Standard4-output spine has terminal lengths0,0,4,96; its96 contains ALL86 events of the other basin. Consecutive root returns have lengths8,76,8,4 and charges-2,8,0,4.',
'Fresh EMPTY-seed simulation reconstructs all10416 reads and complete fields at five cuts. Negative LRLLLLRR at10320..10327 is a same-position elementary return, incomingS toN, field758to756. All five L owners are actual earlier R identities, four already BLACK at the entry cut and one internal. Exact full-field infinite104 tests at9977/10289 certify the actual translating context, not only a cropped eight-word factor.',
'Only elementary last-spine-return positivity is refuted inside an actual WHITE translator. The whole96 aggregate remains+10; no assertion about other aggregate positivity, a four-output per-component minimum, existence of two WHITE spines, or general classification follows. Prepared long-wave negative aggregates retain their BLACK-first inputs and passive backgrounds.'
])
S.with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n');print(report['status']);print(sha(S.with_suffix('.json')));print(whole,tails)

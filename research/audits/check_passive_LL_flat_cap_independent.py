from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__);D=S.parents[1]/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'passive_LL_notches_are_preceded_by_a_YY_flat_RR_cap.md';Q=D/'passive_LL_RR_cap_requires_flat_endpoints.md';F=D/'check_passive_LL_preceding_RR_cap.json';assert sha(P).startswith('b9c0a9e7')and sha(Q).startswith('12769efd')and sha(F).startswith('6cfb8be3')and sha(D/'check_passive_LL_preceding_RR_cap.py').startswith('46d4bdb1');J=json.loads(F.read_text())
ns={'__file__':str(S.with_name('check_cyclic_LL_reactivation_independent.py'))};exec(Path(ns['__file__']).read_text().split('mapped=')[0],ns);pts,reduce,NS,EW,cv,string,test= [ns[k]for k in('pts','reduce','NS','EW','cv','string','test')];fixed={0j:cv('NNSS'),1j:cv('EEWW'),1+0j:cv('EWWE'),1+1j:cv('SNNS')};ds={p:[fixed[p]]if p in fixed else(NS[:]if int(p.real+p.imag)%2==0 else EW[:])for p in pts};ct=Counter();opened=[]
def rec(ds):
 ds=reduce(ds)
 if ds is None:return
 und=[p for p in pts if len(ds[p])>1]
 if und:
  p=min(und,key=lambda p:len(ds[p]))
  for w in ds[p]:rec(ds|{p:[w]})
  return
 hs={p:w[0]for p,w in ds.items()};answer,_=test(hs);ct[answer]+=1
 if answer=='open':opened.append({str((int(p.real),int(p.imag))):string(w)for p,w in hs.items()})
rec(ds);assert sum(ct.values())==3320 and dict(ct)=={'skipped':3127,'clock':190,'open':3};assert sorted(opened,key=str)==sorted(J['open'],key=str)
for r in opened:
 assert(r['(2, 2)'],r['(2, 0)'],r['(2, 1)'])==('NSSN','NNSS','WWEE')and r['(1, 2)']in('EWW','EWWE')
 # B first S arrives from north U; hypothetical LEFT U would arrive fromT to the east.
 assert r['(1, 1)'][0]=='S'and r['(1, 2)'][0]=='E'and r['(2, 2)'][0]=='N'
 assert ns['out'](cv(r['(2, 2)']),0)==1 # firstR east, not west toU.
 if r['(1, 2)']=='EWW':assert r['(1, 2)'].count('E')==1
cyclic=[r for r in opened if r['(1, 2)']=='EWWE'];assert len(cyclic)==1
O={'status':'PASS flat-ended passiveVV LL notch has a precedingYY flatRR cap, mandatory endpoint scope retained','proof':sha(P),'mandatory_scope_qualification':sha(Q),'certificate':sha(F),'script':sha(S),'independent_counts':dict(ct),'all_three_local_inventories':opened,'unique_cyclic_inventory':cyclic[0],'analytic_review':['The exact fixed flat-Y flanks are retained while every unknown3x3 cell has EMPTY or every completeWHITE1..4 physical-axis history. Independent port propagation and physical rank/clock/global-face checker reconstruct all3320 completions and three open inventories. This is a complete local cover, not a factor or attained front.','The cyclic predecessor of actual B incomingS must be physicalU immediately north. U firstR E departsS. A hypothetical LEFT U needs T immediatelyeast to departW; actual T firstR N departsE, so that role is impossible. Therefore U isRIGHT incomingE. EWW has exactlyone incomingE use and is forbidden by nooneuse; only EWWE flatY survives. Full-drift quotient aliases do not change any physical incoming direction or complete ordinal count.','The conclusion applies ONLY to FLAT-ended passiveVV pairs. Mandatory12769efd withdraws the unqualified section3 sentence. The distinct high-high zero-chordVV joints in the signed mixedLL/high-run tables remain live; no mixedflat/high row or all-highRR elimination is inferred.','Assignment to the immediate precedingYY cap is injective by its following physical cyclic contacts, equivariantly under full drift. No fuel, age bound, completefront exclusion or owner charge follows.']};S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))

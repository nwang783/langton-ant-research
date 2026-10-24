from pathlib import Path
from itertools import product
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'one_use_input_flow3_sources_cannot_launch_a_crossing_v2.md';JF=D/'check_one_use_input_flow3_launches_v2.json';assert sha(P)=='4d2981d9ecce52eaf12d19074a201a435743102967c2fe5dba3ac1ec530051ac'and sha(JF).startswith('2f39224b')and sha(D/'check_one_use_input_flow3_launches_v2.py').startswith('ad66b00b');J=json.loads(JF.read_text());ns={'__file__':str(S.with_name('check_one_use_capped_flow3_independent.py'))};exec(Path(ns['__file__']).read_text().split('rr=[]')[0],ns);cv,V,out,test,network=[ns[k]for k in('cv','V','out','test','network')]
# Complete cap4 RIGHT E-first words derive the endpoint flow alternatives.
source=[];sink=[]
for n in range(1,5):
 for z in product('EW',repeat=n-1):
  w='E'+''.join(z);h=cv(w);fi=w.count('E');fo=sum(out(h,r)==2 for r in range(n))
  if fo==3 and fi!=3:source.append((w,fi))
  if fi==3 and fo!=3:sink.append((w,fo))
assert source==[('EWE',2),('EWWW',1)]and sink==[('EEE',2),('EEWE',1)]
def witness(hs,row):
 ev,su,pr=network(hs);path=[(complex(*p),r)for p,r in row['certificate']['path']];assert all(su[a]==b for a,b in zip(path,path[1:]))and path[0][0]==path[-1][0]and path[-1][1]!=path[0][1]+1
ct=Counter()
for Z in['SSNS','SSS']:
 for n in range(5):
  for z in product('EW',repeat=n):
   w=''.join(z);hs={1+1j:cv('SNNN'),1j:cv('EWWW'),0j:cv(Z),1+0j:cv(w)};ans,wit=test(hs);assert ans in('port','skipped');ct['port'if ans=='port'else'rank']+=1
   if ans=='skipped':row=next(r for r in J['RLR_five_literal_failures']if r['Z']==Z and r['D']==w);witness(hs,row)
assert ct==J['RLR_all62_counts']==dict(port=57,rank=5)
rt=Counter();opens=[]
for Z,B in product(['NNS','NNSN'],['SSNS','SSS']):
 for Y in(['EEW','EEWE']if B=='SSNS'else['EWW','EWWE','EEWW']):
  hs={0j:cv(Z),1+0j:cv('EWWW'),1-1j:cv(B),-1j:cv(Y)};row=next(r for r in J['RR_full_endpoint_rows']if(r['Z'],r['B'],r['Y'])==(Z,B,Y));ans,wit=test(hs);assert ans in('port','skipped','open');kind={'skipped':'rank'}.get(ans,ans);assert kind==row['result'];rt[kind]+=1
  if kind=='rank':witness(hs,row)
  elif kind=='open':
   ev,su,pr=network(hs);path=[(0j,0),(1+0j,0),(1-1j,0),(-1j,2),(0j,1)];assert all(su[a]==b for a,b in zip(path,path[1:]));opens.append((Z,B,Y))
assert rt==J['RR_all10_counts']==dict(port=6,rank=1,open=3)
O=dict(status='PASS v2 ONLY: GLOBAL-M cap4 one-use-input flow3 launch is RR; crossing LEFT3 needs odd2to3 source',proof=sha(P),certificate=sha(JF),script=sha(S),endpoint_sources=source,endpoint_sinks=sink,RLR_counts=ct,RR_counts=rt,RR_profiles=opens,analytic_review=[
'CompleteE-first cap4 RIGHT ports yield exactly source2to3EWE/source1to3EWWW and sink3to2EEE/sink3to1EEWE. No input3/output4 or4to3 case is missing. Signed f008 GLOBAL-M RR/RLR geometric reduction retains one-use endpoints and gives the all-length premise.',
'Independent62 full reader products give57 port mismatches and5 actual wrong-next-rank paths. Both output1 andoutput2 RLR sinks are covered; the latterWEW/WEWW path skipsB.L1, andWWWE skipsY.R2. All paths return to the SAME physical cell and complete known ports, so no missing exterior or full-drift alias can repair them.',
'The ten RR outerLEFT products give6 port failures,1 literal rank failure and3 necessaryopens, including passive flow2 endpoint with odd incomingLEFT andodd sink. Everyopen has the actualfourR firstreturn. Onlyv2 bookkeeping/source is bound; v1 is expressly unsigned.',
'At GLOBALM a one-use-input source cannot feed the crossingLEFT3, so any LEFT3 has odd2to3 source. This is only role necessity, not an additive output injection, originalfuel charge or universal boundarycoverage. Higherreader shields outsidecap4, unknownexterior connectors, generalcontrollers andcapture remainopen.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))

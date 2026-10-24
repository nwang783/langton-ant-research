from pathlib import Path
import hashlib,json
S=Path(__file__).resolve();R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();note=D/'TWO_RETURN_ORDINAL_COLLISION_EXCLUSION.md';assert sha(note)=='383f0205900eb3a0659d02509ae11ec2fe3435976554bfe6e245aefdeac3504a';assert sha(D/'check_two_return_ordinal_collision.py')=='73fe2610d5088997a3b7814b7d54912fd035777d1d2372d25095d073cc42248e';jp=D/'two_return_ordinal_collision.json';assert sha(jp)=='1aaa5b50fda6bde78bb819a96bd19ac113a4addb0d68312bf59ef971d8051fa1';ref=json.loads(jp.read_text());V=(1j,1,-1j,-1);heads='NESW';dr=2-2j;pts=[complex(r,t-r)for t in range(-1,4)for r in(0,1)];hist=['W','','N','SS','WE','WWE','SNN','SSNS','EEWE','WWEW'];ix={p:i for i,p in enumerate(pts)};Q=2+2j
quot=lambda p:(p-(int(p.real)//2)*dr,int(p.real)//2)
def arrival(p,h,ordinal):
 r,k=quot(p);i=ix[r];rs=[j for j,c in enumerate(hist[i])if heads.index(c)==h];return(i,rs[ordinal],k)
def outgoing(i,j):return(heads.index(hist[i][j])+(1 if j%2==0 else-1))%4
rows=[]
for wo,ni,duration in[(1,0,20),(2,2,4)]:
 p=Q-1;i,j,k=arrival(p,3,wo);path=[]
 while True:
  assert p!=Q;h=heads.index(hist[i][j]);ho=outgoing(i,j);path.append(dict(physical_cell=[int(p.real),int(p.imag)],class_index=i,complete_rank=j,incoming_heading=h,outgoing_heading=ho,turn='R'if j%2==0 else'L',full_drift_lift=k));dst=p+V[ho];ord=[a for a in range(len(hist[i]))if outgoing(i,a)==ho].index(j)
  if dst==Q:assert ho==0 and ord==ni;break
  ri,rk=quot(dst);assert ri in ix;ti=ix[ri];target=[a for a,c in enumerate(hist[ti])if heads.index(c)==ho];assert len(target)==sum(outgoing(i,a)==ho for a in range(len(hist[i])));p=dst;i=ti;j=target[ord];k=rk;assert len(path)<24
 assert len(path)+1==duration and path==next(z for z in ref['returns']if z['outgoing_W_ordinal']==wo)['internal_events'];rows.append(dict(outgoing_ordinal=wo,incoming_ordinal=ni,duration=duration,physical_return_path=path))
out=dict(status='PASS one named24-event OPEN prefix has no alternating upper completion at any cap',note_sha256=sha(note),open_interface_report_sha256=sha(S.with_name('check_cap4_multiply_F_open_independent.json')),independently_generated_returns=rows,analytic_review=[
'The two return paths are regenerated from only the ten complete lower histories and physical ordinal matching, not copied from supplied paths. Starting at Q=(2,2) W departure ordinal1 or2, every interior successor is forced, no interior cell is Q, and the first return is N arrival ordinal0 after20 steps or ordinal2 after4. Full drift lifts and actual headings agree at every step.',
'Because these are returns to the SAME physical Q with no intervening read, they force complete-rank n0=w1+1 and n2=w2+1. If firstN wereR, previousW departure would beL and therefore an earlierN, impossible. FirstN isL/W and, immediately following secondW, is thirdW. Then n2=n0+1 skips the mandatory middleN. This argument uses neither WHITE firstness nor any visit/period/width bound.',
'The previously signed24-event partial port/clock assignment remains correct: it did not specify Q or all missing phases. This new proof excludes a full alternating completion of that particular prefix. It does not exclude its larger coarse lower-boundary case, any arbitrary multiply-used F circle, or all216 remaining growth-eight diagonal interfaces.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])

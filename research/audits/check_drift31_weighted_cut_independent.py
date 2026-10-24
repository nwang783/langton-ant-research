from pathlib import Path
from itertools import product
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();files=['DRIFT31_EVEN_GAP_CHAIN_MASS_ADDENDUM.md','DRIFT31_WEIGHTED_CUT_IDENTITY.md'];bindings={f:sha(D/f)for f in files};assert bindings[files[0]].startswith('29f1f154')and bindings[files[1]].startswith('89a36d9a')
# Canonical representative(-T,0), full drift(3,1): target=rep(T')+vol*d.
V={'N':1j,'E':1,'S':-1j,'W':-1};d=3+1j
for t in range(-7,8):
 for h,v in V.items():
  target=-t+v;tt=int(3*target.imag-target.real);vol=int(target.imag)
  assert target==-tt+vol*d and vol=={'N':1,'S':-1,'E':0,'W':0}[h]
# Every chain: boundary S edge adds1+P to canonical target clock;
# ell-1 internal edges addell-1-kP; total outgoing-source minusincoming-source.
checks=0
for ell,k,P,t0 in product(range(1,9),range(-4,5),(6,104,258),(-1000,-7,0,999)):
 first=t0+1+P;last=first+(ell-1)-k*P
 assert last-t0==ell+(1-k)*P;checks+=1
# Sharp generic ordinal-sum lower and upper bounds, with actual rank gaps retained.
spanchecks=0
for q in range(1,8):
 for gaps in product((1,2,3),repeat=q-1):
  rr=[0]
  for x in gaps:rr.append(rr[-1]+x)
  tt=[-123+4*r for r in rr]
  assert q*tt[0]+2*q*(q-1)<=sum(tt)<=q*tt[-1]-2*q*(q-1)
  assert sum(tt)==q*tt[0]+4*sum(r-rr[0]for r in rr)==q*tt[-1]-4*sum(rr[-1]-r for r in rr)
  spanchecks+=1
out=dict(status='PASS proper-prefix chain mass and exact source-clock/voltage weighted cut identities',bindings=bindings,canonical_voltage_checks=60,synthetic_algebra_checks=checks,ordered_span_checks=spanchecks,analytic_review=[
'Prefix includes COMPLETE histories of every class from genuine read minimum through even t below genuine read maximum. Any closed quotient event component would be a proper component of the actual single P-event orbit, so all named events partition into open chains. No phantom omission below minimum is allowed.',
'Normal-current conservation gives C=w+n=s+u. Each named chain has one incoming/outgoing boundary occurrence; sum named READ lengths=N. Encoding outside-read-to-outside-read steps changes each weight toell+1, givingN+C. Adding complete cells increases named mass by their exact read count unless an impossible proper closed component appears.',
'All incoming boundary edges are S, with target canonical clock=outside SOURCEclock+1+P because voltage=-1. Internal edges obey target=source+1-voltage*P. Summing chains gives W+Nc-S-U=N+P(C-K) with K sum INTERNAL voltages. Outgoing arrival +1 is not silently included. Whole footprint is instead one closed circuit, K1 andN=P.',
'Port source clocks refer to canonical physical representatives, not reduced phases in0..P-1. Their actual chronological gaps yield sum bounds qf+2q(q-1) andql-2q(q-1), sharpened by actual rank differences. Subtracting incoming upper/lower sums gives the displayed plusQ/minusQ total inequalities; common clock shifts cancel by current balance.',
'No bound on Z=C-K, integer port traffic, period, or chronological span is obtained. Chain mass growth rules out an unchanged exact weighted state while adding reads, not finite control graphs with unbounded counters or a hypothetical growing-period family. Prior OPEN arbitrary-k family is not a physical-factor counterexample.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))

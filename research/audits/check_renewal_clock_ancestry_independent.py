from pathlib import Path
from bisect import bisect_right
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];p=SELF.parent/'check_serial_bridge_archive_independent.py';ns={'__file__':str(p)};exec(p.read_text().split('# Fixed local masks')[0],ns);component,ends,connected,wvertex,step=[ns[x]for x in('component','ends','connected','wvertex','step')]
B=set();p=0j;h=0;birth={};r=0;starts=[];entry=[];ex=[];lives=[];nu=[0]
for t in range(2000):
 c='L'if p in B else'R';kw=int(wvertex(p,h).real+wvertex(p,h).imag)%4
 exceptional=False
 if c=='R':birth[p]=t;r+=1
 else:
  exceptional=r>=3 or connected(B-{p},kw,*ends(p,kw));lives.append((birth.pop(p),t));r=0
 p,h,a=step(B,p,h);assert a==c
 nu.append(nu[-1]+int(exceptional))
 if exceptional:
  ex.append(t);starts.append(t+1);entry.append(len(component(B,kw,wvertex(p,h))[1]))
for i in range(len(starts)-1):assert starts[i+1]-starts[i]<=3*entry[i]+5
checked=0
for b,d in lives:
 if b<starts[0]or d>=starts[-1]:continue
 i=bisect_right(starts,b)-1;j=bisect_right(starts,d)-1;lag=nu[d+1]-nu[b]
 assert j-i+1<=lag+1
 assert d-b<=sum(3*entry[k]+5 for k in range(i,j+1));checked+=1
note=ROOT/'active_w_archive_itinerary_2026-10-23/RENEWAL_ANCESTRY.md';sha=hashlib.sha256(note.read_bytes()).hexdigest();assert sha=='5be1abe10476099095be730b7603b4857c6e1229bd6891c4ee9ea8e0dedbcc6c'
out={'status':'PASS entry-active renewal gap and conditional bounded-renewal-ancestry translation criterion','note_sha256':sha,'fine_control_updates':2000,'exceptional_updates':len(ex),'complete_epoch_gap_checks':len(starts)-1,'weighted_lifetime_checks':checked,'analytic':['After a proper post-exceptional L cut, every ordinary L consumes a different bridge of the COMPLETE entry active component. All temporary R imports are discarded on the departure side by exact inheritance. Thus at most c ordinary blocks, each at most3 updates, precede the next exceptional block of at most5 updates: gap<=3c+5. If no exceptional block existed, this finite old-edge supply and the at-most-four-R rule would be contradicted.','Epochs are actual cut intervals[s_i,s_(i+1)), with s_i=tau_i+1. For birth update b and death update d, nu(d+1)-nu(b) counts exceptional L updates in[b,d]. Birth is R, so no birth-boundary ambiguity. The death can itself be exceptional, only making the upper count j+1 conservative. The intersected epoch lengths cover the full lifetime, yielding the displayed weighted bound.','Beginning after the first exceptional L removes the only initial partial-epoch convention. Under eventual renewal-entry mass cap M and consumed renewal lag cap J, age<=(J+1)(3M+5), despite arbitrarily large dormant archives or intermediate active R imports.','After finitely many checkpoint-current lifetimes have their final future consumption, every later L obeys this age bound. The retained exact suffix predictor therefore yields eventual nonzero translation, not104. Conversely non-eventual translation requires unbounded renewal-entry masses in every tail or, when those masses are eventually bounded, unbounded renewal lags among late-born consumed lifetimes.'],'scope':'Universal finite-support conditional reduction. Neither sustained mass cap nor token-lag cap is proved; no archive quotient, original-root budget, periodic-word classification or capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(len(ex),checked)

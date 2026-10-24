from pathlib import Path
import sys,json,hashlib
ROOT=Path('/workspace/shared/langton');OUT=Path(__file__).parent
sys.path.insert(0,str(OUT))
from probe_stitched_continuation import final
from synthesize_third_return import get_history,joins

def sha(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
out=[]
for q in(3,5,7,9):
 _,_,_,base=final(q)
 new=json.loads((OUT/f'parallel_third_q{q}.json').read_text())
 initial=set(map(tuple,base['initial']));extras=set(map(tuple,new['extra']));history=get_history(base)
 assert not(extras&set(history))and not(initial&extras)
 n=12*((q+1)//2)**2
 third=new['third_word'][:-4]
 stages=[dict(name='first_positive_ordinary',word=base['words'][0],gain=q-2),dict(name='first_charged_return',word=base['words'][1],gain=9-q),dict(name='second_positive_ordinary',word=base['words'][2],gain=q-2),dict(name='second_charged_return',word=new['return_word'],gain=3-q),dict(name='third_positive_ordinary',word=third,gain=q-2)]
 assert len(third)==4*n+9*q-18
 out.append(dict(q=q,n=n,initial_pose=base['entry'],initial_black=sorted(initial|extras),baseline_black=sorted(initial),additional_initial_black=sorted(extras),baseline_prefix_word=''.join(base['words']),stages=stages,following_exception_word='RRL',expected=dict(initial_mass=6*n+6*q+35,extra_mass=2*n+15*q-8,total_duration=20*n+21*q+56,net_gain=q+6,second_R_lifetimes=2*n+3*q-2,second_R_consumed_in_third=2*n+3*q-7,second_R_remaining=5,third_ordinary_L=2*n+4*q-8,third_ordinary_R=2*n+5*q-10)))
certificate=dict(status='AUTHOR literal finite constructions, independent audit requested',scope='Exactly q=3,5,7,9. No all-q theorem, no self-regeneration, no infinite trajectory or attraction conclusion.',cases=out)
(OUT/'THREE_POSITIVE_PASSES_CERTIFICATE.json').write_text(json.dumps(certificate,indent=2)+'\n')
print([(x['q'],x['expected'])for x in out])

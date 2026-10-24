import sys,json,collections
sys.path.insert(0,'/workspace/shared/langton/autonomous_controllers_2026-10-24')
from certify_active_C_entry_exit_forests import analyze,active_C,circuits
from check_extremal_read_coupling import event_word,quotient
Z=json.load(open('/workspace/shared/langton/autonomous_controllers_2026-10-24/active_C_entry_exit_forests_certificate.json'))['base_controls']
for name,z in Z.items():
 E,d,h=event_word(z['word']);P=len(E);H=collections.defaultdict(list)
 for e in E:
  for side in [0,1]:
   c=active_C(e['p'],(e['hi']+side*2)%4);q,k=quotient(c,d);H[q].append((e['t']-k*P,e,side,k))
 first={q:min(es,key=lambda e:e[0]) for q,es in H.items()};F={};roots=[]
 for v,(t,e,side,k) in first.items():
  assert side==1,(name,v,t,e)
  c=active_C(e['p'],e['hi']);q,l=quotient(c,d);assert first[q][0]+(l-k)*P<t
  if e['c']=='L':roots.append((v,e['t']));continue
  F[v]={'target':q,'voltage':l-k,'read_class':quotient(e['p'],d)[0],'L_phase':e['t'],'clock_gap':t-first[q][0]-(l-k)*P}
 C=circuits(F)
 print(name,'allC',len(H),'blackroots',roots,'cycles',C)
 for cy in C:
  print('profile',[(e['t'],''.join('NESW'[r['hi']] for h in z['read_histories'] if any(a['t']==e['t'] for a in h['reads']) for r in h['reads'])) for v in cy['vertices'] for _,e,_,_ in [first[v]]])

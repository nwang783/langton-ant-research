import sys,json,collections
sys.path.insert(0,'/workspace/shared/langton/autonomous_controllers_2026-10-24')
from certify_active_C_entry_exit_forests import analyze,active_C,circuits
from check_extremal_read_coupling import event_word,quotient
Z=json.load(open('/workspace/shared/langton/autonomous_controllers_2026-10-24/active_C_entry_exit_forests_certificate.json'))['base_controls']
for name,zz in Z.items():
 w=zz['word']
 for op,ww in [('base',w),('reverse',w[::-1]),('swap',w.translate(str.maketrans('RL','LR'))),('revswap',w[::-1].translate(str.maketrans('RL','LR')))]:
  z=analyze(ww);E,d,h=event_word(ww);P=len(E);H=collections.defaultdict(list)
  for e in E:
   for side in [0,1]:
    c=active_C(e['p'],(e['hi']+side*2)%4);q,k=quotient(c,d);H[q].append((e['t']-k*P,e,side,k))
  first={q:min(es,key=lambda e:e[0]) for q,es in H.items()};F={}
  for v,(t,e,side,k) in first.items():
   assert side==1
   c=active_C(e['p'],e['hi']);q,l=quotient(c,d);assert first[q][0]+(l-k)*P<t
   if e['c']=='L':continue
   F[v]={'target':q,'voltage':l-k,'read_class':quotient(e['p'],d)[0],'L_phase':e['t'],'clock_gap':t-first[q][0]-(l-k)*P}
  C=circuits(F);A=z['WHITE_first_entry_cycles'];Bsets=sorted([sorted(c['read_phases']) for c in C]);As={tuple(x['source']):x for x in z['WHITE_first_entry_edges']};Asets=sorted([sorted(As[tuple(v)]['R_owner_phase'] for v in c['vertices']) for c in A])
  print(name,op,'birth',Bsets,'entry',Asets,'same',Bsets==Asets)

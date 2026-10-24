import json,itertools,collections
from check_extremal_read_coupling import event_word,quotient
from certify_active_C_entry_exit_forests import active_C
z=json.load(open('active_C_entry_exit_forests_certificate.json'))['base_controls']['S104'];w=z['word'];P=len(w);pal={x:set()for x in ['E','F','G']}
for cl in z['read_histories']:
 for e,f in zip(cl['reads'],cl['reads'][1:]):
  a=e['canonical_time'];b=f['canonical_time'];word=''.join(w[t%P]for t in range(a,b));typ=None
  if e['c']=='R'and e['hi']==f['hi']:typ='E';h=2
  if e['c']=='L'and (f['hi']-e['hi'])%4==2:typ='F';h=0
  if e['c']=='L'and e['hi']==f['hi']:typ='G';h=2
  if typ is None:continue
  ee,d,hh=event_word(word,h=h,p=(-8,0));lev=[3*active_C(q['p'],q['hi'])[1]-active_C(q['p'],q['hi'])[0]for q in ee]
  good=(min(lev)>=7)if typ=='E' else(lev[0]==5 and min(lev[1:])>=7 and word[:2]=='LR')if typ=='F'else(word[:3]=='LLL' and lev[1]==5 and min(lev[:1]+lev[2:])>=7)
  if good:pal[typ].add(word)
pal={k:sorted(v,key=lambda s:(len(s),s))for k,v in pal.items()};stat=collections.Counter();stable=[];g8=[];finite=[];words=set();Pvals=[]
for mode,e1,e2,f1,f2,g in itertools.product(range(2),pal['E'],pal['E'],pal['F'],pal['F'],pal['G']):
 w='RRRR'+f1+ ('RLLL'+f2+e1+g if mode==0 else e1+g+'RLLL'+f2)+e2+'LRLRRRRLRRRRLLLLRL'; words.add(w)
 E,d,h=event_word(w,h=0,p=(-8,0));assert d==(3,1)and h==0;gr=w.count('R')-w.count('L');P=len(w);stat['total']+=1
 H=collections.defaultdict(list);HH=collections.defaultdict(list)
 for e in E:
  H[e['p']].append(e);q,k=quotient(e['p'],d);HH[q].append((e['t']-P*k,e))
 fbad=any(a['c']==b['c']for es in H.values()for a,b in zip(es,es[1:]));bad=False
 if not fbad:stat['finite']+=1;finite.append((mode,e1,e2,f1,f2,g,w))
 for es in HH.values():
  es.sort(key=lambda x:x[0]);bad|=any(a[1]['c']==b[1]['c']for a,b in zip(es,es[1:]))
 if bad:stat['nonalternating']+=1
 else:
  I=sum(es[0][1]['c']=='L'for es in HH.values());stat['stable']+=1;stable.append((P,gr,I,mode,e1,e2,f1,f2,g,w))
  if I==0:stat['WHITE']+=1
 if gr==8:stat['g8']+=1;Pvals.append(P)
print({k:len(v)for k,v in pal.items()},stat,'unique',len(words),'g8Ps',sorted(set(Pvals)))
print('stable',stable)
print('finite',len(finite))
for a in finite[:5]:print(a)
def legal(w):
 E,_,_=event_word(w,h=0,p=(-8,0));seen={}
 for e in E:
  p=e['p']
  if p in seen and seen[p]['c']==e['c']:return seen[p],e
  seen[p]=e
 return None
for mode in [0,1]:
 seq=[('D',['RRRR']),('F1',pal['F'])]+([('O',['RLLL']),('F2',pal['F']),('E1',pal['E']),('G',pal['G'])]if mode==0 else[('E1',pal['E']),('G',pal['G']),('O',['RLLL']),('F2',pal['F'])])+[('E2',pal['E']),('K',['LRLRRRRLRRRRLLLLRL'])]
 todo=[('',[])];rejects=[]
 for name,choices in seq:
  nxt=[]
  for pre,lab in todo:
   for i,w in enumerate(choices):
    bad=legal(pre+w)
    if bad:rejects.append((name,lab+[(name,i)],bad[0]['t'],bad[1]['t'],bad[0]['p'],bad[0]['c']))
    else:nxt.append((pre+w,lab+[(name,i)]))
  print('mode',mode,'block',name,'attempts',len(todo)*len(choices),'survivors',len(nxt));todo=nxt
 print('reject leaves',len(rejects));print(rejects[:12])

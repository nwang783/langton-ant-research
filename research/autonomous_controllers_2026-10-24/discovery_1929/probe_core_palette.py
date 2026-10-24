import json
from check_extremal_read_coupling import event_word,D
from certify_active_C_entry_exit_forests import active_C
src=json.load(open('active_C_entry_exit_forests_certificate.json'))['base_controls']
for name in ['S104','M10','F80']:
 z=src[name];w=z['word'];P=len(w);pal={x:{}for x in ['E','F','G']}
 for cl in z['read_histories']:
  for e,f in zip(cl['reads'],cl['reads'][1:]):
   a=e['canonical_time'];b=f['canonical_time'];word=''.join(w[t%P]for t in range(a,b));typ=None
   if e['c']=='R'and e['hi']==f['hi']:typ='E';h=2
   if e['c']=='L'and (f['hi']-e['hi'])%4==2:typ='F';h=0
   if e['c']=='L'and e['hi']==f['hi']:typ='G';h=2
   if typ is None:continue
   ee,d,hh=event_word(word,h=h,p=(-8,0));assert d==(0,0)
   lev=[3*active_C(q['p'],q['hi'])[1]-active_C(q['p'],q['hi'])[0]for q in ee]
   if typ=='E':good=min(lev)>=7
   if typ=='F':good=lev[0]==5 and min(lev[1:])>=7 and word[:2]=='LR'
   if typ=='G':good=word[:3]=='LLL' and lev[1]==5 and min(lev[:1]+lev[2:])>=7
   if good:pal[typ][word]=(a,b,lev)
 print(name, {k:len(v)for k,v in pal.items()})
 for typ,ls in pal.items():
  for w,(a,b,lev)in ls.items():print(typ,len(w),(a,b),w,'range',min(lev),max(lev))

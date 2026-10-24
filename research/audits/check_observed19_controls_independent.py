"""Literal finite-seed replay of all observed transfer controls, no author imports."""
from pathlib import Path
import json,hashlib,re
P=Path(__file__).resolve().parents[1];W=P/'word_stabilization'
words={'D':'LLLLRLRRRR','C':'LLLLRLRRRRLRRRR','V':'LLLLRLRRRRLRRLRRRR'};marker='LLLLRLRRRRL'
def trace(word):
 p=0j;h=1j;positions=[];req={};parity=set()
 for c in word:
  positions.append((p,h));bit=c=='L'
  if p in req:assert req[p]^(p in parity)==bit
  else:req[p]=bit^(p in parity)
  parity.symmetric_difference_update({p});h*=(-1j if c=='R'else 1j);p+=h
 return positions,(p,h),req,parity
core={p for p,b in trace(marker)[2].items()if b}
src=W/'dcv_observed19_witnesses.json';data=json.loads(src.read_text());seen=set();records=[]
for c in data['controls']:
 factor=c['factor_macro_word'];assert factor==c['whole_macro_word'][c['source_macro_index']:]
 packets=list(re.finditer('[DV]C*',factor));assert ''.join(m.group()for m in packets)==factor
 raw=''.join(words[x]for x in factor)+marker
 black={complex(*p)for p in c['initial_seed_normalized_at_source']};assert len(black)==c['initial_mass_at_source']
 p=0j;h=1j;poses=[];after_source=None
 source_end=sum(len(words[x])for x in packets[0].group())
 for t,turn in enumerate(raw):
  poses.append((p,h));assert(p in black)==(turn=='L')
  black.symmetric_difference_update({p});h*=(-1j if turn=='R'else 1j);p+=h
  if t+1==source_end:after_source=black.copy()
 offsets=[sum(len(words[x])for x in factor[:m.start()])for m in packets]
 target_relative=c['target_macro_index']-c['source_macro_index'];ti=next(i for i,m in enumerate(packets)if m.start()==target_relative)
 assert ti>0 and ti+1<len(packets) and packets[ti].end()==c['target_macro_last']+1-c['source_macro_index']
 typ=lambda m:(0 if m.group()[0]=='D'else 4)+len(m.group())-1
 assert [typ(m)for m in packets]==c['factor_packet_types']
 assert all(typ(m)in[0,1,4,5,6]for m in packets[:ti+1])
 a,b,x,y,hh,qx,qy=c['tuple'];assert a==typ(packets[0]) and b==typ(packets[ti]);q=complex(qx,qy)
 tp,th=poses[offsets[ti]];assert tp==complex(x,y) and th==(1j,1,-1j,-1)[hh] and c['target_pose']==[x,y,hh]
 assert q in after_source
 for i,m in enumerate(packets[:ti+1]):
  w=''.join(words[z]for z in m.group());local,end,first,flip=trace(w);context=trace(w+marker)[2];ep,eh=end
  entry={z for z,b in context.items()if b};inputs=entry-core;outputs=(entry^flip)-{ep+eh/1j*z for z in core}
  origin,heading=poses[offsets[i]];relative=(q-origin)/(heading/1j)
  assert raw[offsets[i]:offsets[i]+len(w)+len(marker)]==w+marker
  if i==0:assert q in outputs
  elif i==ti:assert relative in inputs
  else:assert relative not in context
 assert c['protected_contexts_verified']==ti-1
 seen.add(tuple(c['tuple']));records.append({'tuple':c['tuple'],'literal_reads':len(raw),'strict_intermediate_contexts':ti-1,'initial_mass':c['initial_mass_at_source']})
expected={tuple(map(int,l.split()))for l in(W/'dcv_companion_observed19.tsv').read_text().splitlines()}
assert seen==expected and len(seen)==19
result={'status':'PASS independent literal finite-seed controls','covered':len(seen),'witnesses':len(records),'records':records,'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items()if k!='records'}))

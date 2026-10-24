"""Independently enumerate EVERY finite packet word, not prefix-pruned discovery."""
from pathlib import Path
from itertools import product
import json,sys,hashlib
from check_dcuv_producer_model_independent import raws,mark,ROOT,digest
OUT=ROOT/'audits/packet_window_dfa_replays';OUT.mkdir(exist_ok=True)
def trace(seq):
 w=''.join(raws[a]for a in seq)+mark;z=0j;h=1j;reads={}
 for t,c in enumerate(w):
  if z in reads and reads[z][0]==c:
   return {'cell':[int(z.real),int(z.imag)],'previous_read':reads[z][1],'conflicting_read':t,'turn':c}
  reads[z]=(c,t);h*= -1j if c=='R'else 1j;z+=h
 return None

def check(path):
 path=Path(path).resolve();J=json.loads(path.read_text())
 if J['format']=='literal_packet_forbidden_factor_dfa_v1':
  from check_packet_forbidden_dfa_independent import check as forbiddencheck
  return forbiddencheck(path)
 assert J['format']=='literal_packet_window_dfa_v1';k=J['window'];assert k>=2
 keep=tuple(J['keep']);assert keep==(0,1,4,5,6,7,8,9)
 assert all((raws[a]+mark).startswith(mark)for a in keep)
 assert digest(Path(J['geometry_file']))==J['geometry_sha256']
 legal={()};bad={};counts=[1];tested=0
 for n in range(1,k+1):
  count=0
  for seq in product(keep,repeat=n):
   conflict=trace(seq);tested+=1
   if conflict is None:legal.add(seq);count+=1
   else:bad[seq]=conflict
  counts.append(count)
 assert J['legal_counts_by_length']==counts
 states=sorted(seq for seq in legal if len(seq)<k);assert J['states']==[list(s)for s in states];indices={s:i for i,s in enumerate(states)}
 rows=[]
 for seq in states:
  row=[]
  for a in keep:
   word=seq+(a,)
   if word not in legal:row.append(-1)
   else:
    suffix=word[-(k-1):];assert suffix in indices;row.append(indices[suffix])
  rows.append(row)
 parts=[0]*len(states)
 while True:
  signatures=[tuple(parts[j]if j>=0 else-1 for j in row)for row in rows]
  keys=sorted(set(signatures));next_parts=[keys.index(s)for s in signatures]
  # Class labels can differ; stabilize equivalence rather than label numbers.
  same=all((parts[i]==parts[j])==(next_parts[i]==next_parts[j])for i in range(len(states))for j in range(i))
  parts=next_parts
  if same:break
 authors=J['state_to_class'];assert len(authors)==len(states)
 equiv={}
 for a,b in zip(authors,parts):
  if a in equiv:assert equiv[a]==b
  else:equiv[a]=b
 assert len(equiv)==len(set(parts))==len(J['classes'])
 for c,members in enumerate(J['classes']):assert members==[list(states[i])for i,a in enumerate(authors)if a==c]
 for i,row in enumerate(rows):assert J['transitions'][authors[i]]==[authors[j]if j>=0 else-1 for j in row]
 assert J['initial_class']==authors[indices[()]]
 # Independently check every recorded first conflict and complete rejected-prefix coverage.
 wanted={seq:bad[seq]for seq in bad if seq[:-1]in legal}
 got={tuple(x['word']):x['conflict']for x in J['rejected_extensions']};assert got==wanted
 out={'status':'PASS independent full-word inventory and DFA congruence','window':k,'counts':counts,'tested_words':tested,'suffix_states':len(states),'classes':len(equiv),'rejected_extensions':len(got),'file_sha256':digest(path),'scope':'Exact necessary finite marked-factor language only; no infinite-language sufficiency.'}
 (OUT/(path.stem+'.independent.json')).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out));return out
if __name__=='__main__':
 for path in sys.argv[1:]:check(path)

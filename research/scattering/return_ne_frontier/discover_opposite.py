"""Explore an exceptional opposite corner after the new fixed NE endcaps."""
import sys,json,gzip
from pathlib import Path
from discover_caps import initial,HERE
from ant_exact import W,PHASES,plan
from crossing import tail

def run(r,k,limit=800000):
 f,p,h=initial(r);cap=next(c for c in json.loads((HERE/'fixed_caps.json').read_text())['rows'] if c['phase']==r);assert cap['tail_phase']==0
 cp,ch=cap['pose'];d0=plan(W[:72],tuple(cp),ch)[2];marker=(d0[0]+2*k,d0[1]+2*k);assert sum(marker)>100;f.flip(marker);word=[];reads=[];first=None
 for t in range(limit):
  if p==marker and first is None:first=t
  reads.append(p);p,h,c=f.step(p,h);word.append(c)
  if first is not None and t>first+20000 and (t+1)%104==0:
   tw=''.join(word[-104:])
   if tw in PHASES and ''.join(word[-312:])==tw*3:
    proof=tail(f,p,h,tw)
    if proof:
     fn=f'opposite_r{r}_k{k}.txt.gz'
     with gzip.open(HERE/fn,'wt') as o:o.write(''.join(word))
     out=dict(status='infinite endcap-model discovery only',phase=r,k=k,marker=marker,first_contact=first,capture=t+1,pose=[p,h],tail=proof,bounds=[min(x-y for x,y in reads),max(x-y for x,y in reads),min(map(sum,reads)),max(map(sum,reads))],word_file=fn);(HERE/f'opposite_r{r}_k{k}.json').write_text(json.dumps(out,indent=2)+'\n');return out
 return dict(status='no certified standard tail within exploration limit',phase=r,k=k,pose=[p,h],last_word=''.join(word[-500:]))
if __name__=='__main__':
 for r in (70,75):
  for k in (100,101,102):print(json.dumps(run(r,k)),flush=True)

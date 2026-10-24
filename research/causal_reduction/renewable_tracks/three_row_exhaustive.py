from three_row_transfer import *
M=int(sys.argv[1])if len(sys.argv)>1 else 6;t0=time.time();counts=Counter();outs={};parity=Counter();bestdepth=0;chains=[]
for z in range(1<<(3*M-1)):
 # All width-M A/B/C patterns with B0 black, which is a sufficient first-even root choice.
 raw=(z&1)|2|((z>>1)<<2);ab=raw&((1<<(2*M))-1);C=tuple(j for j in range(M)if raw>>(2*M+j)&1)
 nxt,st,w=step((ab,C));counts[st]+=1
 if nxt is None:continue
 outs.setdefault(nxt,dict(input=(ab,C),output=nxt,word=w));bs=[j for j in range((nxt[0].bit_length()+1)//2)if nxt[0]>>(2*j+1)&1];parity['empty'if not bs else min(bs)%2]+=1
 seq=[(ab,C),nxt];q=nxt;seen=set(seq)
 for k in range(20):
  q,st2,w2=step(q)
  if q is None:break
  seq.append(q)
  if q in seen:break
  seen.add(q)
 if len(seq)>bestdepth:bestdepth=len(seq);chains=[seq];print('DEPTH',bestdepth,'input',raw,flush=True)
 elif len(seq)==bestdepth and len(chains)<5:chains.append(seq)
 if z and z%65536==0:print('INPUTS',z,'seconds',time.time()-t0,flush=True)
out=dict(width=M,inputs=1<<(3*M-1),counts=dict(counts),output_min_B_parity=dict(parity),distinct_outputs=len(outs),max_chain=bestdepth,chains=chains,examples=list(outs.values()),seconds=time.time()-t0)
(HERE/f'three_row_exhaustive_{M}.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:v for k,v in out.items()if k!='examples'},indent=2))

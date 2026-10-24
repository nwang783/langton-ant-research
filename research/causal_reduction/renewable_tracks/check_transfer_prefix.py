from two_row_transfer import *
M=int(sys.argv[1]) if len(sys.argv)>1 else 10;t0=time.time();C=Counter();examples={};bad=[];outs={}
for mask in range(1<<(2*M)):
 rs,st=run_transfers(mask,M);C[st]+=1
 for d in rs:
  z=d['output'];outs.setdefault(z,d);examples.setdefault(d['word'],d);r=0
  while (z>>(2*r))&1:r+=1
  if any(z>>(2*j+1)&1 for j in range(2*(r//2)+1)):
   bad.append(d);print('PREFIX_COUNTEREXAMPLE',d,flush=True)
 if bad:break
 if mask and mask%65536==0:print('INPUTS',mask,'seconds',time.time()-t0,flush=True)
out=dict(width=M,completed_inputs=mask+1,counts=dict(C),distinct_words=len(examples),distinct_outputs=len(outs),prefix_counterexamples=bad,output_examples=list(outs.values()),seconds=time.time()-t0)
(HERE/f'two_row_transfer_prefix_{M}.json').write_text(json.dumps(out,indent=2));print('DONE',dict((k,v)for k,v in out.items()if k!='output_examples'),flush=True)

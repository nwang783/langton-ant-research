from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];B=R/'rank_two_plateau_2026-10-23';word=(R/'word_stabilization/standard_word.txt').read_text().strip();out=[]
for copies in(1,2,3):
 p=-1+0j;v=1j;leftsteps=[];Rcount=0
 for c in word*copies:
  incoming=p-v/2+v*(-1j)/2;w=v*(-1j if c=='R' else 1j);outgoing=p+w/2+w*(-1j)/2;delta=outgoing-incoming
  if c=='R':assert delta==0;Rcount+=1
  else:assert abs(delta.real)==abs(delta.imag)==1;leftsteps.append(delta)
  p+=w;v=w
 assert sum(leftsteps,0j)==p-(-1+0j)==complex(2*copies,2*copies)and v==1j
 out.append(dict(period=104*copies,L=len(leftsteps),R=Rcount,face_displacement=[int(sum(leftsteps,0j).real),int(sum(leftsteps,0j).imag)]))
# Local count identity at every corner incident to the global C maximum.
local=[]
for rf in range(3):
 for rg in range(3):
  if not(1<=rf+rg<=2):continue
  if rf==rg:assert rf==rg==1;nf=2;delta=0;maxreads=rf+rg
  else:nf=1;delta=int(max(rf,rg)==2);maxreads=max(rf,rg)
  assert maxreads==nf+delta;local.append([rf,rg,nf,delta,maxreads])
result=dict(status='PASS independent diagonal C-face projection and local max-face read count',note_sha256=hashlib.sha256((B/'C_face_L_transition_flow.md').read_bytes()).hexdigest(),standard_controls=out,local_count_rows=local,scope='Separate all-L diagonal face flow only. Selected first-L birth cycles subtract as actual L occurrences; L>=N+D|1-c|. Global-max count Rmax=4n+delta and L>=n give P>=4n+delta+max(n,N+D|1-c|). Not additive with overlapping physical A/B/C budgets.')
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(result)

"""Literal physical witnesses through generic exact/quotient/prophecy graphs."""
from pathlib import Path
import json,subprocess,sys,os
R=Path(__file__).resolve().parent;P=R.parent;profile=R/'profile.json';G=json.loads((R/'literal_residual_geometry.json').read_text())['geometry'];M=[{'word':g['word'],'end_marker':g['marker']}for g in G];J=json.loads(Path(sys.argv[1]).read_text());controls=J['witnesses'];adjacent=len(sys.argv)>2 and sys.argv[2]=='adjacent';controls=[c for c in controls if not adjacent or c['target_index']==c['source_index']+1];allrows={tuple(map(int,l.split()))for l in(R/'candidate_transfers.tsv').read_text().splitlines()};observed={tuple(c['tuple'])for c in J['witnesses']};H=allrows if adjacent else allrows-observed;tag=('adjacent'if adjacent else'depth'+str(J['packet_depth']))+'_scoped_source_inputs';directory=R/f'generic_{tag}_controls';directory.mkdir(exist_ok=True);hf=directory/'hypotheses.tsv';hf.write_text(''.join(' '.join(map(str,r))+'\n'for r in sorted(H)));D=((0,1),(1,0),(0,-1),(-1,0));records=[]
def rot(p,h):x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def walk(w,p,h,B):
 seen=set()
 for c in w:
  assert(c=='L')==(p in B),(p,h,c);seen.add(p);B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 return p,h,seen
def call(cmd):return subprocess.run(list(map(str,cmd)),cwd=P,capture_output=True,text=True,check=True,env={**os.environ,'PRODUCER_LABEL_ALLOW_WIDE':'1'}).stdout
for ci,c in enumerate(controls,1):
 a,b,x,y,h,qx,qy=c['tuple'];base=directory/f'control{ci:02d}_base';exact=directory/f'control{ci:02d}_exact';quot=directory/f'control{ci:02d}_quotient';prod=directory/f'control{ci:02d}_product';pf=directory/f'control{ci:02d}_points.json';pf.write_text(json.dumps([[x+rot(z,h)[0],y+rot(z,h)[1]]for z in G[b]['inputs']]));call(['python','generate_resource_transfer_patch.py',profile,a,b,x,y,h,qx,qy,base,'sourceplus:'+str(pf)]);B0=json.loads(base.with_suffix('.json').read_text());watch=[(qx,qy)]
 for cell in [(0,0)]:
  if cell not in watch and list(cell)in B0['points']:watch.append(cell)
 call(['python','add_resource_producer_labels.py',profile,base.with_suffix('.json'),exact,hf,';'.join(f'{x},{y}'for x,y in watch),R/'empty.tsv']);call(['python','quotient_resource_scoped_producers.py',exact.with_suffix('.json'),quot,R/'dcv_scope.json']);L=json.loads(exact.with_suffix('.json').read_text());Q=json.loads(quot.with_suffix('.json').read_text());call(['python','add_resource_target_prophecy.py',quot.with_suffix('.json'),prod,hf,R/'empty.tsv']);T=json.loads(prod.with_suffix('.json').read_text())
 B={tuple(z)for z in c['initial_black_seed']};p=(0,0);hh=0
 for aa in c['packet_ids'][:c['source_index']]:p,hh,_=walk(M[aa]['word'],p,hh,B)
 pp,heading=p,hh;B={rot((z[0]-pp[0],z[1]-pp[1]),-heading)for z in B};p=(0,0);hh=0;factor=c['packet_ids'][c['source_index']:c['target_index']+1];p,hh,_=walk(M[a]['word'],p,hh,B);initial=set(B);initialpose=p,hh;contexts=[];poses=[];tmp=set(B);tp,th=p,hh
 for aa in factor[1:]:
  poses.append((tp,th));_,_,seen=walk(M[aa]['word']+M[aa]['end_marker'],tp,th,set(tmp));contexts.append(seen);tp,th,_=walk(M[aa]['word'],tp,th,tmp)
 assert poses[-1]==((x,y),h)
 codes=[lab['outer_code']for lab in L['producer_labels']];positions={tuple(z):i for i,z in enumerate(L['poses'])};models=[L,Q,T];scope_allowed=set(Q['scope_packet_types']);clean=[int(code!=0 and a in scope_allowed and L['start'][0]!=L['out'])for code in codes]
 def flags_at(j):return [int(all(tuple(cell)not in contexts[k]for k in range(j,len(contexts)-1)))for cell in T['prophecy_cells']]
 def state(model,j):
  s=sum(1<<i for i,z in enumerate(model['points'])if tuple(z)in B)
  if 'producer_labels'in model:s|=sum(code<<lab['offset']for code,lab in zip(codes,model['producer_labels']))
  else:s|=sum(lab['exact_codes_to_class'][code]<<lab['offset']for code,lab in zip(codes,model['producer_label_classes']))
  if 'scope_packet_types'in model:s|=sum(bit<<lab['scope_offset']for bit,lab in zip(clean,model['producer_label_classes']))
  if 'prophecy_cells'in model:s|=sum(bit<<(model['prophecy_offset']+k)for k,bit in enumerate(flags_at(j)))
  return s
 for model in models:
  s=state(model,0);assert s&model['start'][1]==model['start'][2]
 near=far=0
 for j,aa in enumerate(factor[1:]):
  goal=j==len(factor)-2;sid=positions.get((*p,hh),L['out']);before=[state(model,j)for model in models];matching=[]
  for model,s in zip(models,before):
   if sid==model['out']:matching.append(None);assert not goal
   else:
    edges=[e for e in model['transitions']if e[0]==sid and e[-1]==aa and bool(e[-2])==goal and s&e[2]==e[3]];assert edges,(ci,j,'missing transition');matching.append(edges)
  pp,heading=p,hh;context=contexts[j];p,hh,_=walk(M[aa]['word'],p,hh,B)
  for k,lab in enumerate(L['producer_labels']):
   cell=tuple(lab['cell'])
   if cell in context:codes[k]=0
   if aa not in scope_allowed or cell in context or positions.get((*p,hh),L['out'])==L['out']:clean[k]=0
   local=rot((cell[0]-pp[0],cell[1]-pp[1]),-heading)
   if list(local)in G[aa]['outputs']:
    hits=[n for n,lab0 in enumerate(lab['codes'])if n and not lab0['outer_origin']and lab0['packet']==aa and lab0['slot']==G[aa]['outputs'].index(list(local))and lab0['pose']==[*pp,heading]];assert len(hits)==1;codes[k]=hits[0];clean[k]=int(aa in scope_allowed and positions.get((*p,hh),L['out'])!=L['out'])
  nextpos=positions.get((*p,hh),L['out'])
  for model,s,edges in zip(models,before,matching):
   after=state(model,j+1)
   if edges is None:
    assert after==s
    if nextpos!=model['out']:assert nextpos in model['reentry']
   else:assert any(after==(((s^e[4])&~e[5])|(e[6]&e[5]))and nextpos==e[1]for e in edges),(ci,j,'no exact reset branch')
  near+=sid!=L['out'];far+=sid==L['out']
 records.append({'control':ci,'tuple':c['tuple'],'watched':watch,'variables':[model['n']for model in models],'near_steps':near,'far_steps':far,'status':'PRESERVED_IN_EXACT_QUOTIENT_AND_PROPHECY'})
 print(ci,c['tuple'],'PASS',flush=True)
(R/f'generic_{tag}_controls.json').write_text(json.dumps({'status':'PASS','hypothesis_scope':'all candidate rows intentionally includes outer goals'if adjacent else'all candidate rows minus observed controls','records':records},indent=2))

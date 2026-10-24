"""Counterexample-guided finite-family discovery. No theorem until exact final coverage/audit.
The two reserved rows remain explicit UNSIGNED obligations owned by chronology.
"""
from pathlib import Path
import json,subprocess,os,time,hashlib,shutil
P=Path(__file__).resolve().parent;B=P.parent/'core_periodicity_new';O=P/'dcv_producer_mutual_family';O.mkdir(exist_ok=True);T=O/'tools';T.mkdir(exist_ok=True)
files=['generate_protected_transfer_patch.py','analyze_patch_witness_labels.py','add_protected_producer_labels.py','quotient_protected_producer_labels.py','protected_patch_bdd_witness','protected_patch_bdd_witness.cpp','protected_patch_bdd_labels','protected_patch_bdd_labels.cpp','protected_patch_bdd_labels_witness','protected_patch_bdd_labels_witness.cpp','verify_protected_patch_bdd_labels.py']
for name in files:
 src=B/name;dst=T/name
 if src.exists() and not dst.exists():shutil.copy2(src,dst)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
(O/'tools_manifest.json').write_text(json.dumps({name:sha(T/name)for name in files if(T/name).exists()},indent=2))
rows=[tuple(map(int,l.split()))for l in(P/'dcv_companion_candidate221.tsv').read_text().splitlines()];index={r:i for i,r in enumerate(rows,1)};observed={tuple(map(int,l.split()))for l in(P/'dcv_companion_observed19.tsv').read_text().splitlines()};signed_file=P/'dcv_anchored_signed102.tsv';signed={tuple(map(int,l.split()))for l in signed_file.read_text().splitlines()};reserved={(4,4,-3,0,1,0,0),(5,4,-3,0,1,0,0)};active=set(rows)-observed;priority={tuple(map(int,l.split()))for l in(P/'dcv_directional25_targets.tsv').read_text().splitlines()};F={tuple(map(int,l.split()[:5]))for l in(P/'seven_sub_dcv_star4_kernel.tsv').read_text().splitlines()};FP={tuple(map(int,l.split()[:7]))for l in(P/'dcv_protected_patch2_kernel.tsv').read_text().splitlines()}|signed;assert signed<=active and reserved<=active-signed
seeds={};preferred={}
# Existing successful watch sets are discovery hints only; every model is rebuilt.
for path in list(B.glob('*quotient*.json'))+list((B/'producer_helper_refinement').glob('*quotient*.json')):
 try:j=json.loads(path.read_text())
 except Exception:continue
 if 'producer_label_classes' not in j:continue
 row=(j['source'],j['target'],*j['target_pose'],*j['protected_q']);q=[tuple(l['cell'])for l in j['producer_label_classes']]
 if row in active and len(q)<=5 and(row not in seeds or len(q)<len(seeds[row])):seeds[row]=q
summary={'status':'DISCOVERY ONLY; reserved rows explicitly unproved; no family theorem','fixed_signed_file':str(signed_file),'fixed_signed_sha256':sha(signed_file),'reserved_rows':sorted(reserved),'initial_active':len(active),'stages':[]}
def save():(O/'summary.json').write_text(json.dumps(summary,indent=2))
def command(args,prefix,timeout=180):
 try:r=subprocess.run([str(x)for x in args],capture_output=True,text=True,timeout=timeout,env={**os.environ,'PRODUCER_LABEL_ALLOW_WIDE':'1'});out=r.stdout;err=r.stderr;code=r.returncode
 except subprocess.TimeoutExpired as e:out='status TIMEOUT\n';err=e.stderr or '';err=err.decode()if isinstance(err,bytes)else err;code=124
 Path(str(prefix)+'.txt').write_text(out);Path(str(prefix)+'.log').write_text(err);return out,code

def witness(model,pre):
 engine=T/('protected_patch_bdd_labels_witness'if'producer_label_classes'in model else'protected_patch_bdd_witness');out,code=command([engine,pre.with_suffix('.dat'),'2000000'],str(pre)+'_witness');path=[]
 for line in out.splitlines():
  if line.startswith('WITNESS '):
   _,s,c,a=line.split();s,c,a=map(int,(s,c,a));path.append({'pose':model['poses'][s]if s<model['out']else None,'color':c,'packet_id':a})
 dest=Path(str(pre)+'_witness.json')
 if path:dest.write_text(json.dumps(path,indent=2))
 return path,dest,out

def discover(row,H,stage):
 ci=index[row];record={'candidate_index':ci,'tuple':row,'attempts':[]};allseed=list(seeds.get(row,[]));modes=[preferred.get(row,'source')]+[x for x in['source','both']if x!=preferred.get(row,'source')]
 for mode in modes:
  base=O/f'base{ci:03}_{mode}'
  if not base.with_suffix('.json').exists():
   out,code=command(['python',T/'generate_protected_transfer_patch.py',*row,base,mode],str(base)+'_gen')
   if code:record['attempts'].append({'mode':mode,'status':'BASE_GENERATION_ERROR'});continue
  J=json.loads(base.with_suffix('.json').read_text());patch={tuple(p)for p in J['points']};Q=[q for q in allseed if q in patch][:5];model=J;current=base
  for rnd in range(7):
   pre=stage/f'candidate{ci:03}_{mode}_r{rnd}'
   if Q:
    exact=Path(str(pre)+'_exact');quot=Path(str(pre)+'_quotient');out,code=command(['python',T/'add_protected_producer_labels.py',base.with_suffix('.json'),exact,H,';'.join(f'{x},{y}'for x,y in Q),signed_file],str(exact)+'_gen')
    if code:record['attempts'].append({'mode':mode,'round':rnd,'watched':Q,'status':'LABEL_GENERATION_ERROR'});break
    out,code=command(['python',T/'quotient_protected_producer_labels.py',exact.with_suffix('.json'),quot],str(quot)+'_gen')
    if code:record['attempts'].append({'mode':mode,'round':rnd,'watched':Q,'status':'QUOTIENT_GENERATION_ERROR'});break
    model=json.loads(quot.with_suffix('.json').read_text());current=quot;out,code=command([T/'protected_patch_bdd_labels',quot.with_suffix('.dat'),'2000000',quot.with_suffix('.bdd')],quot);rr={'mode':mode,'round':rnd,'watched':list(Q),'variables':model['n'],'result':out.strip(),'prefix':str(quot)};record['attempts'].append(rr)
    if 'EXHAUSTED_NO_HIT'in out:
     verify,vc=command(['python',T/'verify_protected_patch_bdd_labels.py',quot.with_suffix('.dat'),quot.with_suffix('.bdd')],str(quot)+'_verify');assert vc==0 and'VERIFIED'in verify,(quot,verify);rr['verified']=verify.strip();record['status']='EXHAUSTED_NO_HIT';record['certificate_prefix']=str(quot);seeds[row]=list(Q);preferred[row]=mode;return record
    if 'ABSTRACT_WITNESS'not in out:break
   path,pathfile,out=witness(model,current)
   if not path:
    if 'EXHAUSTED_NO_HIT'in out and not Q:Q=[tuple(J['protected_q'])];continue
    record['attempts'].append({'mode':mode,'round':rnd,'status':'WITNESS_RECONSTRUCTION_CAP_OR_ERROR','result':out.splitlines()[:1]});break
   out,code=command(['python',T/'analyze_patch_witness_labels.py',base.with_suffix('.json'),pathfile],str(pre)+'_analysis');assert code==0
   events=json.loads(pathfile.with_suffix('.labels.json').read_text());choices={}
   for e in events:
    q=tuple(e['cell']);r=tuple(e['tuple']);known=r[:5]in F or r in FP;hyp=r in active and not e['outer_to_goal']
    if(known or hyp)and q not in Q and q in patch:choices[q]=min(choices.get(q,(9,9)),(0 if known else 1,e['target_step']))
   new=sorted(choices,key=lambda q:(choices[q],q))
   if not new or len(Q)>=5:
    record['attempts'].append({'mode':mode,'round':rnd,'status':'NO_NEW_ELIGIBLE_LINEAGE_CELL'if not new else'FIVE_CELL_LIMIT','events_file':str(pathfile.with_suffix('.labels.json'))});break
   Q+=new[:5-len(Q)];allseed=list(Q)
 record['status']='UNSUPPORTED';return record

for si in range(101):
 stage=O/f'stage{si:02}';stage.mkdir(exist_ok=True);H=stage/'hypotheses.tsv';H.write_text(''.join(' '.join(map(str,r))+'\n'for r in sorted(active)));sr={'stage':si,'active_count':len(active),'hypotheses_sha256':sha(H),'results':[]};summary['stages'].append(sr);supported=set(signed)|reserved;save()
 for row in sorted(active-signed-reserved,key=lambda r:(r not in priority,r)):
  t=time.time();rec=discover(row,H,stage);rec['seconds']=round(time.time()-t,3);sr['results'].append(rec)
  if rec['status']=='EXHAUSTED_NO_HIT':supported.add(row)
  save();print(json.dumps({'stage':si,'candidate_index':index[row],'tuple':row,'status':rec['status'],'seconds':rec['seconds'],'certificate_prefix':rec.get('certificate_prefix')}),flush=True)
 sr['supported_count_including_reserved']=len(supported);sr['removed_candidate_indices']=[index[r]for r in sorted(active-supported)];save()
 if supported==active:
  summary['status']='CLOSED EXCEPT TWO RESERVED UNSIGNED OBLIGATIONS; independent numerical and family audit still required';summary['stable_except_reserved']=True;save();print('STABLE_EXCEPT_RESERVED',len(active),flush=True);break
 active=supported

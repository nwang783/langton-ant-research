"""Record-conditioned target-input provenance, optionally with exact signed-pair signatures.
CLI FUSED_RECORD_MODEL.json PREFIX 'all|x,y;...' ; no unproved hypotheses.
Rebuild from its original 7-field base; all target inputs keep known/unknown origin.
"""
from pathlib import Path
import json,sys,hashlib
from resource_profile import load_profile
record,out=map(Path,sys.argv[1:3]);R=json.loads(record.read_text());B=json.loads(Path(R['base_model_file']).read_text());P,D,M=load_profile(B['resource_profile_file']);G=D['geometry']['geometry'];F=D['ordinary'];FP=D['protected'];precise=set(map(tuple,R['goal_input_cells']))if sys.argv[3]=='all'else set(tuple(map(int,s.split(',')))for s in sys.argv[3].split(';')if s);watch=set(map(tuple,R['goal_input_cells']));assert precise<=watch
removed=set(R['geometrically_filtered_base_transition_indices']);BT=[(i,r)for i,r in enumerate(B['transitions'])if i not in removed]
def rot(q,h):x,y=q;return [(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def complement(bad,bits):
 def rec(i,k,v,bs):
  if not bs:return [(k,v)]
  if i==bits:return []
  bit=1<<i;return rec(i+1,k|bit,v,[x for x in bs if not x&bit])+rec(i+1,k|bit,v|bit,[x for x in bs if x&bit])
 return rec(0,0,0,list(bad))
labels=[];n=B['n'];start=list(B['start'])
for q in sorted(watch):
 classes=[{'members':[None],'rejected_transitions':[]}];index={};codes={};descriptors=[]
 for a in B['keep']:
  for slot,z in enumerate(G[a]['outputs']):
   for h in range(4):
    rz=rot(z,h);px,py=q[0]-rz[0],q[1]-rz[1]
    if (px+py+h)%2:continue
    sig=[]
    if q in precise:
     for ti,(sid,to,k,v,f,goal,b)in BT:
      x,y,hh=B['poses'][sid];local=rot((q[0]-x,q[1]-y),-hh)
      if list(local)not in G[b]['inputs']:continue
      rel=rot((x-px,y-py),-h);row=(a,b,*rel,(hh-h)%4,*z)
      if row[:5]in F or row in FP:sig.append(ti)
    key=tuple(sig)
    if key not in index:index[key]=len(classes);classes.append({'members':[],'rejected_transitions':sig})
    cl=index[key];lab={'packet':a,'slot':slot,'heading':h,'pose':[px,py,h]};classes[cl]['members'].append(lab);codes[a,slot,h]=cl
 outer=codes.get((B['source'],G[B['source']]['outputs'].index(list(q)),0),0)if list(q)in G[B['source']]['outputs']else 0
 bits=(len(classes)-1).bit_length();mask=((1<<bits)-1)<<n;start[1]|=mask;start[2]|=outer<<n;labels.append({'cell':q,'offset':n,'bits':bits,'classes':classes,'initial_class':outer,'precise_signed_signature':q in precise,'code_map':[[*key,val]for key,val in sorted(codes.items())]});n+=bits
assert n<=50,('variable cap',n,[len(L['classes'])for L in labels])
T=[]
for ti,(sid,to,k,v,f,goal,a)in BT:
 x,y,h=B['poses'][sid];cubes=[(k,v)];clear=reset=0
 for lab in labels:
  q=lab['cell'];off=lab['offset'];bits=lab['bits'];z=rot((q[0]-x,q[1]-y),-h);bad={i for i,cl in enumerate(lab['classes'])if ti in cl['rejected_transitions']}
  if goal:bad.add(0)
  if bad:cubes=[(kk|(ck<<off),vv|(cv<<off))for kk,vv in cubes for ck,cv in complement(bad,bits)]
  if list(z)in [r[:2]for r in G[a]['requirements']]:clear|=((1<<bits)-1)<<off
  if list(z)in G[a]['outputs']:
   slot=G[a]['outputs'].index(list(z));cl=next(r[3]for r in lab['code_map']if r[:3]==[a,slot,h]);clear|=((1<<bits)-1)<<off;reset|=cl<<off
 for kk,vv in cubes:T.append([sid,to,kk,vv,f,clear,reset,goal,a])
J={**B,'n':n,'start':start,'transitions':T,'format':'guarded_reset_record_signed_labels_v1','record_condition_model_file':str(record.resolve()),'record_condition_model_sha256':hashlib.sha256(record.read_bytes()).hexdigest(),'producer_label_classes':labels,'conditional_scope':'Known goal-input producers with only signed HB subpair restrictions and strict historical-record conditioning; no unproved H'}
out.with_suffix('.json').write_text(json.dumps(J,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f"{n} {B['out']+1} {len(T)} {len(B['reentry'])}\n");f.write(' '.join(map(str,start))+'\n')
 for r in T:f.write(' '.join(map(str,r))+'\n')
 f.write(' '.join(map(str,B['reentry']))+'\n')
print(json.dumps({'variables':n,'classes':[len(L['classes'])for L in labels],'transitions':len(T),'precise_cells':sorted(precise)}))

"""Quotient exact producer labels by fixed-model rejection signatures.
CLI EXACT_LABEL_MODEL.json PREFIX. Unknown is class0; outer origins never merge.
The complete physical producer members and transition signatures are certificate metadata.
"""
from pathlib import Path
import json,sys,hashlib
from resource_profile import load_profile
inp=Path(sys.argv[1]);out=Path(sys.argv[2]);J=json.loads(inp.read_text());B=json.loads(Path(J['base_model_file']).read_text());profile,data,profile_meta=load_profile(J['resource_profile_file']);assert all(J.get(k)==v and B.get(k)==v for k,v in profile_meta.items());G=data['geometry']['geometry'];M=data['macro_words']['macro_words'];F=data['ordinary'];FP=data['protected']|{tuple(map(int,l.split()[:7]))for l in Path(J['extra_guard_file']).read_text().splitlines()if l.strip()};H={tuple(r)for r in J['candidate_hypotheses']};D=((0,1),(1,0),(0,-1),(-1,0))
def rot(p,h):
 x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def trace(w):
 p=(0,0);h=0;seen=set()
 for c in w:
  seen.add(p);h=(h+(1 if c=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 return seen
C=[trace(m['word']+m['end_marker'])for m in M];labels=[];n=B['n'];start=list(B['start'])
for L in J['producer_labels']:
 q=L['cell'];classes=[{'members':[None],'rejected_transitions':[],'outer_origin':False}];idx={(False,()):0};maps=[0]
 for lab in L['codes'][1:]:
  sig=[]
  for ii,(sid,to,k,v,f,goal,a)in enumerate(B['transitions']):
   x,y,h=B['poses'][sid];z=rot((q[0]-x,q[1]-y),-h)
   if list(z)not in G[a]['inputs']:continue
   px,py,hh=lab['pose'];rel=rot((x-px,y-py),-hh);row=(lab['packet'],a,*rel,(h-hh)%4,*G[lab['packet']]['outputs'][lab['slot']]);signed=row[:5]in F or row in FP;induct=row in H and(not goal or not lab['outer_origin'])
   if signed or induct:sig.append(ii)
  key=(lab['outer_origin'],tuple(sig))
  if key not in idx:idx[key]=len(classes);classes.append({'members':[],'rejected_transitions':sig,'outer_origin':lab['outer_origin']})
  ci=idx[key];classes[ci]['members'].append(lab);maps.append(ci)
 bits=(len(classes)-1).bit_length();outer=maps[L['outer_code']];labels.append({'cell':q,'offset':n,'bits':bits,'classes':classes,'outer_class':outer,'exact_codes_to_class':maps,'exact_codes':L['codes']});mask=((1<<bits)-1)<<n;start[1]|=mask;start[2]|=outer<<n;n+=bits
assert n<=50

def complement_cubes(bad,bits):
 def rec(i,k,v,bs):
  if not bs:return[(k,v)]
  if i==bits:return[]
  bit=1<<i;return rec(i+1,k|bit,v,[x for x in bs if not x&bit])+rec(i+1,k|bit,v|bit,[x for x in bs if x&bit])
 return rec(0,0,0,list(bad))
T=[]
for ti,(sid,to,k,v,f,goal,a)in enumerate(B['transitions']):
 x,y,h=B['poses'][sid];cubes=[(k,v)];resetmask=resetvalue=0
 for L in labels:
  q=L['cell'];off=L['offset'];bits=L['bits'];z=rot((q[0]-x,q[1]-y),-h);bad={ci for ci,cl in enumerate(L['classes'])if ti in cl['rejected_transitions']}
  if bad:cubes=[(kk|(ck<<off),vv|(cv<<off))for kk,vv in cubes for ck,cv in complement_cubes(bad,bits)]
  if z in C[a]:resetmask|=((1<<bits)-1)<<off
  if list(z)in G[a]['outputs']:
   matches=[i for i,lab in enumerate(L['exact_codes'])if i and not lab['outer_origin']and lab['packet']==a and lab['slot']==G[a]['outputs'].index(list(z))and lab['pose']==[x,y,h]];assert len(matches)==1;val=L['exact_codes_to_class'][matches[0]];resetmask|=((1<<bits)-1)<<off;resetvalue|=val<<off
 for kk,vv in cubes:T.append([sid,to,kk,vv,f,resetmask,resetvalue,goal,a])
new=dict(J);new.pop('producer_labels');new.update(n=n,start=start,transitions=T,format='guarded_xor_reset_producer_quotient_v1',producer_label_classes=labels,exact_label_model_file=str(inp),exact_label_model_sha256=hashlib.sha256(inp.read_bytes()).hexdigest());out.with_suffix('.json').write_text(json.dumps(new,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f"{n} {B['out']+1} {len(T)} {len(B['reentry'])}\n");f.write(' '.join(map(str,start))+'\n')
 for row in T:f.write(' '.join(map(str,row))+'\n')
 f.write(' '.join(map(str,B['reentry']))+'\n')
print(json.dumps({'variables':n,'old_variables':J['n'],'classes':[len(l['classes'])for l in labels],'bits':[l['bits']for l in labels],'transitions':len(T)}))

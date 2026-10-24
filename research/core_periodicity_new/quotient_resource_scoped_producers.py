"""Producer signature quotient with separately scoped signed-language authority.
CLI EXACT_LABEL_MODEL.json PREFIX SCOPE.json
The old full producer identity survives foreign packets. Its extra clean bit does
not: it is false after every foreign action or near→OUT step and at OUT starts.
Only already-signed scope relations use that bit; current H remains full-language.
"""
from pathlib import Path
import json,sys,hashlib
from resource_profile import load_profile
inp=Path(sys.argv[1]);out=Path(sys.argv[2]);scopepath=Path(sys.argv[3]);J=json.loads(inp.read_text());B=json.loads(Path(J['base_model_file']).read_text());profile,data,meta=load_profile(J['resource_profile_file']);assert all(J.get(k)==v and B.get(k)==v for k,v in meta.items());G=data['geometry']['geometry'];M=data['macro_words']['macro_words'];F=data['ordinary'];FP=data['protected']|{tuple(map(int,l.split()[:7]))for l in Path(J['extra_guard_file']).read_text().splitlines()if l.strip()};H={tuple(r)for r in J['candidate_hypotheses']};D=((0,1),(1,0),(0,-1),(-1,0));scope=json.loads(scopepath.read_text());allowed=set(scope['keep']);SD={}
for key,rec in scope['files'].items():
 p=Path(rec['path']);raw=p.read_bytes();assert hashlib.sha256(raw).hexdigest()==rec['sha256']
 SD[key]=json.loads(raw)if p.suffix=='.json'else{tuple(map(int,l.split()[:5 if key=='ordinary'else 7]))for l in raw.decode().splitlines()if l.strip()}
SF=SD['ordinary'];SP=SD['protected']|SD['signed_extra']
for a in allowed:
 assert M[a]['word']==SD['macro_words']['macro_words'][a]['word']
 assert M[a]['end_marker']==SD['macro_words']['macro_words'][a]['end_marker']
 for k in ['inputs','outputs','endpoint']:assert G[a][k]==SD['geometry']['geometry'][a][k]
def rot(p,h):x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def footprint(w):
 p=(0,0);h=0;seen=set()
 for c in w:seen.add(p);h=(h+(1 if c=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 return seen
C=[footprint(m['word']+m['end_marker'])for m in M];labels=[];n=B['n'];start=list(B['start'])
for L in J['producer_labels']:
 q=L['cell'];classes=[{'members':[None],'rejected_transitions':[],'scoped_rejected_transitions':[],'outer_origin':False}];idx={(False,(),()):0};maps=[0]
 for lab in L['codes'][1:]:
  sig=[];ssig=[]
  for ti,(sid,to,k,v,f,goal,a)in enumerate(B['transitions']):
   x,y,h=B['poses'][sid];z=rot((q[0]-x,q[1]-y),-h)
   if list(z)not in G[a]['inputs']:continue
   px,py,hh=lab['pose'];rel=rot((x-px,y-py),-hh);row=(lab['packet'],a,*rel,(h-hh)%4,*G[lab['packet']]['outputs'][lab['slot']])
   if row[:5]in F or row in FP or(row in H and(not goal or not lab['outer_origin'])):sig.append(ti)
   if lab['packet']in allowed and a in allowed and(row[:5]in SF or row in SP):ssig.append(ti)
  key=(lab['outer_origin'],tuple(sig),tuple(ssig))
  if key not in idx:idx[key]=len(classes);classes.append({'members':[],'rejected_transitions':sig,'scoped_rejected_transitions':ssig,'outer_origin':lab['outer_origin']})
  ci=idx[key];classes[ci]['members'].append(lab);maps.append(ci)
 bits=(len(classes)-1).bit_length();outer=maps[L['outer_code']];labels.append({'cell':q,'offset':n,'bits':bits,'classes':classes,'outer_class':outer,'exact_codes_to_class':maps,'exact_codes':L['codes']});mask=((1<<bits)-1)<<n;start[1]|=mask;start[2]|=outer<<n;n+=bits
for lab in labels:
 lab['scope_offset']=n;bit=1<<n;start[1]|=bit
 if lab['outer_class']and B['source']in allowed and start[0]!=B['out']:start[2]|=bit
 n+=1
assert n<=50,'quotient plus scope exceeds engine variable limit'
def complement_cubes(bad,bits):
 def rec(i,k,v,bs):
  if not bs:return[(k,v)]
  if i==bits:return[]
  bit=1<<i;return rec(i+1,k|bit,v,[x for x in bs if not x&bit])+rec(i+1,k|bit,v|bit,[x for x in bs if x&bit])
 return rec(0,0,0,list(bad))
T=[]
for ti,(sid,to,k,v,f,goal,a)in enumerate(B['transitions']):
 x,y,h=B['poses'][sid];cubes=[(k,v)];clear=reset=0
 for lab in labels:
  q=lab['cell'];off=lab['offset'];bits=lab['bits'];sb=1<<lab['scope_offset'];z=rot((q[0]-x,q[1]-y),-h);bad={ci for ci,c in enumerate(lab['classes'])if ti in c['rejected_transitions']};sbad={ci for ci,c in enumerate(lab['classes'])if ti in c['scoped_rejected_transitions']}
  if bad:cubes=[(kk|(ck<<off),vv|(cv<<off))for kk,vv in cubes for ck,cv in complement_cubes(bad,bits)]
  if sbad:
   parts=[]
   for kk,vv in cubes:
    parts.append((kk|sb,vv))
    for ck,cv in complement_cubes(sbad,bits):
     ck<<=off;cv<<=off
     if not((vv^cv)&kk&ck):parts.append((kk|ck|sb,vv|cv|sb))
   cubes=parts
  if z in C[a]:clear|=((1<<bits)-1)<<off
  if a not in allowed or to==B['out']or z in C[a]:clear|=sb
  if list(z)in G[a]['outputs']:
   hits=[i for i,ll in enumerate(lab['exact_codes'])if i and not ll['outer_origin']and ll['packet']==a and ll['slot']==G[a]['outputs'].index(list(z))and ll['pose']==[x,y,h]];assert len(hits)==1;value=lab['exact_codes_to_class'][hits[0]];clear|=((1<<bits)-1)<<off;reset|=value<<off;clear|=sb
   if a in allowed and to!=B['out']:reset|=sb
 for kk,vv in cubes:T.append([sid,to,kk,vv,f,clear,reset,goal,a])
new=dict(J);new.pop('producer_labels');new.update(n=n,start=start,transitions=T,format='guarded_xor_reset_scoped_producer_quotient_v1',producer_label_classes=labels,scope_specification_file=str(scopepath),scope_specification_sha256=hashlib.sha256(scopepath.read_bytes()).hexdigest(),scope_packet_types=sorted(allowed),scope_start_out_forgets=True,scope_near_to_out_forgets=True,exact_label_model_file=str(inp),exact_label_model_sha256=hashlib.sha256(inp.read_bytes()).hexdigest());out.with_suffix('.json').write_text(json.dumps(new,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f"{n} {B['out']+1} {len(T)} {len(B['reentry'])}\n");f.write(' '.join(map(str,start))+'\n')
 for row in T:f.write(' '.join(map(str,row))+'\n')
 f.write(' '.join(map(str,B['reentry']))+'\n')
print(json.dumps({'variables':n,'classes':[len(l['classes'])for l in labels],'scope_packet_types':sorted(allowed),'scope_bits':len(labels),'transitions':len(T)}))

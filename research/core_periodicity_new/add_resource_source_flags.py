"""Enrich a frozen patch graph with untouched-source-output flags.
8-field edge format: from,to,guardmask,guardvalue,xor,clear,goal,packet.
"""
from pathlib import Path
import json,sys,hashlib
from resource_profile import load_profile
inp=Path(sys.argv[1]);out=Path(sys.argv[2]);hyp=Path(sys.argv[3]);extra=Path(sys.argv[4]);J=json.loads(inp.read_text());profile,data,profile_meta=load_profile(J['resource_profile_file']);assert all(J.get(k)==v for k,v in profile_meta.items());R=data['geometry'];M=data['macro_words']['macro_words'];FP=data['protected']|{tuple(map(int,l.split()[:7]))for l in extra.read_text().splitlines()if l.strip()};source=J['source'];q=tuple(J['protected_q']);Q=[tuple(v)for v in R['geometry'][source]['outputs']if tuple(v)!=q];assert all(list(p)in J['points']for p in Q);H={tuple(map(int,l.split()[:7]))for l in hyp.read_text().splitlines()if l.strip()}
D=((0,1),(1,0),(0,-1),(-1,0))
def rot(p,h):
 x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def trace(w):
 p=(0,0);h=0;seen=set()
 for c in w:
  seen.add(p);h=(h+(1 if c=='R'else-1))%4;d=D[h];p=(p[0]+d[0],p[1]+d[1])
 return seen
C=[trace(m['word']+m['end_marker'])for m in M];n=J['n'];T=[]
for sid,to,k,v,f,g,a in J['transitions']:
 x,y,h=J['poses'][sid];clear=0
 for j,z in enumerate(Q):
  bit=1<<(n+j)
  if(source,a,x,y,h,*z)in FP or(not g and(source,a,x,y,h,*z)in H):k|=bit # live1 would contradict an independently forbidden protected pair
  local=rot((z[0]-x,z[1]-y),-h)
  if local in C[a]:clear|=bit
 T.append([sid,to,k,v,f,clear,g,a])
flags=((1<<len(Q))-1)<<n;sp,sk,sv=J['start'];new=dict(J);new.update(n=n+len(Q),base_n=n,source_flag_cells=Q,start=[sp,sk|flags,sv|flags],transitions=T,extra_guard_file=str(extra),extra_guard_sha256=hashlib.sha256(extra.read_bytes()).hexdigest(),candidate_hypotheses=[list(r)for r in sorted(H)],candidate_hypothesis_file=str(hyp)if hyp else None,candidate_hypothesis_sha256=hashlib.sha256(hyp.read_bytes()).hexdigest()if hyp else None,format='guarded_xor_clear_v1');out.with_suffix('.json').write_text(json.dumps(new,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f"{new['n']} {J['out']+1} {len(T)} {len(J['reentry'])}\n");f.write(' '.join(map(str,new['start']))+'\n')
 for row in T:f.write(' '.join(map(str,row))+'\n')
 f.write(' '.join(map(str,J['reentry']))+'\n')
print(json.dumps({'variables':new['n'],'source_flags':Q,'positions':J['out']+1,'transitions':len(T),'extra_sha256':new['extra_guard_sha256']}))

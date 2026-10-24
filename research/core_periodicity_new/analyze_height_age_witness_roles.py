"""Fixed-word chronology role-matching and literal forbidden-factor diagnostics."""
from pathlib import Path
import json,sys,collections
src,out=map(Path,sys.argv[1:3]);J=json.loads(src.read_text());G=json.loads(Path('chronology_dcuv/literal_residual_geometry.json').read_text())['geometry'];P={tuple(map(int,s.split()[:7]))for s in Path('chronology_dcuv/protected_patch2.tsv').read_text().splitlines()if s and not s.startswith('#')};age={(a,x,y):r for a,x,y,r in json.loads(Path('chronology_dcuv/counted_input_age_rules_complete.json').read_text())};F=-10;phase=1

def rot(p,h):x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def ht(p):return sum(rot(p,phase))
outputs=[];inputs=[]
for k,row in enumerate(J['rows']):
 a=row['packet'];h,q=row['pose'];C=row['C_before']
 if q is None:continue
 for slot in G[a]['inputs']:
  z=q+ht(rot(slot,h))
  if z>F:inputs.append({'packet_index':k,'packet':a,'heading':h,'slot':slot,'height':z,'C':C,'age':age[a,*slot]})
 if k<len(J['rows'])-1:
  for slot in G[a]['outputs']:
   z=q+ht(rot(slot,h))
   if z>F:outputs.append({'packet_index':k,'packet':a,'heading':h,'slot':slot,'height':z,'C':C})
adj=[]
for v in inputs:
 L=[]
 for i,u in enumerate(outputs):
  if u['packet_index']>=v['packet_index']or u['height']!=v['height']or v['C']-u['C']<v['age']:continue
  dh=(v['heading']-u['heading'])%4;x,y=rot(v['slot'],dh);ox,oy=u['slot'];tup=u['packet'],v['packet'],ox-x,oy-y,dh,ox,oy
  if tup not in P:L.append(i)
 adj.append(L)
matched=[-1]*len(outputs);matchedinput=[-1]*len(inputs)
def aug(k,seen):
 for i in adj[k]:
  if i in seen:continue
  seen.add(i)
  if matched[i]<0 or aug(matched[i],seen):matched[i]=k;matchedinput[k]=i;return True
 return False
unmatched=[]
for k in range(len(inputs)):
 if not aug(k,set()):unmatched.append(k)
word=J['word_including_goal']
def conflict(seq):
 x=y=h=0;last={}
 for i,c in enumerate(''.join(G[a]['word']for a in seq)+'LLLLRLRRRRL'):
  p=x,y
  if p in last and last[p][0]==c:return {'cell':p,'prior':last[p][1],'current':i,'turn':c}
  last[p]=c,i;h=(h+(1 if c=='R'else-1))%4;dx,dy=[(0,1),(1,0),(0,-1),(-1,0)][h];x+=dx;y+=dy
 return None
bad={}
for n in range(1,13):
 for k in range(len(word)-n+1):
  seq=tuple(word[k:k+n]);b=conflict(seq)
  if b:bad[seq]=b
 if bad:break
R={'status':'ROLE_AGE_MATCH_EXISTS'if not unmatched else'ROLE_AGE_MATCH_DEFICIT','input_tokens':len(inputs),'output_tokens':len(outputs),'matched':len(inputs)-len(unmatched),'unmatched_inputs':[inputs[k]for k in unmatched],'zero_candidate_inputs':[inputs[k]for k,L in enumerate(adj)if not L],'first_literal_conflict':conflict(word),'shortest_bad_factor_length':n,'shortest_bad_factors':[{'word':list(w),'conflict':b}for w,b in sorted(bad.items())],'scope':'Fixed-word necessary matching only; a perfect match is not physical ant legality.'};out.write_text(json.dumps(R,indent=2)+'\n');print({k:v for k,v in R.items()if k not in ['unmatched_inputs','zero_candidate_inputs','shortest_bad_factors']});print('bad factor count',len(bad))

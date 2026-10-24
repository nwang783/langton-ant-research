"""Exact all-parameter two-diagonal-strip read guard for existing parent words.

This is geometry only; physical validity of the literal word template is an
independent inherited proof. No parameter sampling is used.
"""
import sys,json,hashlib
from pathlib import Path
ROOT=Path('/workspace/shared/langton/continuation_2026-10-22')
sys.path.insert(0,str(ROOT/'ant_continuation'))
from ant_exact import plan,PHASES
PATH=ROOT/'ant_continuation2/planar_structure/exceptional_rectangle_template.json'
T=json.loads(PATH.read_text())
NORMS={'u':(1,-1),'z':(1,1)}
def dot(v,n):return v[0]*n[0]+v[1]*n[1]
def bound(points,coef,base,drift=(0,0)):
 valid=[(name,n) for name,n in NORMS.items() if dot(coef,n)==0 and dot(drift,n)==0]
 assert valid,('read piece leaves both fixed diagonal strips',coef,base,drift)
 rows=[]
 for name,n in valid:
  vals=[dot((base[0]+q[0],base[1]+q[1]),n) for q in points]
  rows.append((max(abs(x) for x in vals),name,min(vals),max(vals)))
 H,name,lo,hi=min(rows)
 return {'normal':name,'minimum':lo,'maximum':hi,'absolute_bound':H}

def main():
 coef=(0,0);base=(0,0);h=0;rows=[];parents=[]
 for i,s in enumerate(T['segments']):
  assert set(s['word'])<={'R','L'}
  points,_,d,eh=plan(s['word'],(0,0),h)
  if s['type']=='finite':
   row=bound(points,coef,base);base=(base[0]+d[0],base[1]+d[1])
  else:
   assert s['word'] in PHASES and eh==h
   aa,bb=s['count'];assert aa>=0 and aa*200+bb>=1
   row=bound(points,coef,base,d)
   coef=(coef[0]+aa*d[0],coef[1]+aa*d[1]);base=(base[0]+bb*d[0],base[1]+bb*d[1])
  row['stage']=i;rows.append(row);h=eh
  if i in (4,8,13):
   word=T['segments'][i+1]['word'] if i<13 else s['word']
   pts,_,dr,hh=plan(word,(0,0),h);assert word in PHASES and hh==h
   tail=bound(pts,coef,base,dr)
   H=max(*(r['absolute_bound'] for r in rows),tail['absolute_bound'])
   parents.append({'parent_after_stage':i,'entire_prefix_and_infinite_tail_H':H,
                   'tail_guard':tail,'pose_affine':[coef,base,h]})
 out={'status':'exact geometry passed; inherited template physical correctness required',
      'parameter_domain':'all integer n>=200','template_sha256':hashlib.sha256(PATH.read_bytes()).hexdigest(),
      'strip_union':'|x-y|<=H OR |x+y|<=H','parents':parents,'stages':rows}
 Path(__file__).with_name('rectangle_two_strip_guard.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()

"""Exact global upper-z bounds for all three pristine exceptional parents."""
import sys,json,hashlib
from pathlib import Path
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'scattering/fixed_core_rectangle'))
from bivariate import A
N=(0,1,200);C=lambda v:(0,0,v)
TFILE=ROOT/'continuation_2026-10-22/ant_continuation2/planar_structure/exceptional_rectangle_template.json'
def main():
 assert hashlib.sha256(TFILE.read_bytes()).hexdigest()=='16246ec40cbdd4ad94c35698992582b27a942dc7d539683f1b3684892cd5687d'
 T=json.loads(TFILE.read_text());p=A.point(0,0);h=0;records=[];upper=-10**9;read_count=0;parents={}
 for i,s in enumerate(T['segments']):
  assert s['type'] in ('finite','periods')
  word=s['word'];assert word and set(word)<={'R','L'};qs,_,end,eh=A.plan(word,(0,0),h)
  count=None if s['type']=='finite' else A.add(A.scale(N,s['count'][0]),C(s['count'][1]))
  if count is not None:assert len(word)==104 and eh==h and A.nonneg(A.sub(count,A.ONE))
  vals=[]
  for x,y in qs:
   z=A.add(A.add(p[0],p[1]),C(x+y))
   if count is not None and sum(end)>0:z=A.add(z,A.scale(A.sub(count,A.ONE),sum(end)))
   assert z[0]<=0 and z[1]<=0
   vals.append(z[2]);read_count+=1
  upper=max(upper,max(vals));records.append(dict(segment=i,read_upper=max(vals)))
  if i in (1,5,9):
   # These segment words extend forever for the blank, q, and q+a parent.
   assert sum(end)<=0
   local=max(A.add(A.add(p[0],p[1]),C(x+y))[2] for x,y in qs)
   parent_upper=max(upper,local);parents[{1:'blank',5:'q',9:'q+a'}[i]]=parent_upper
  if count is None:p=A.translate_local(end,p,0)
  else:p=A.padd(p,(A.scale(count,end[0]),A.scale(count,end[1])))
  h=eh
 word=T['infinite_tail_word'];assert word and set(word)<={'R','L'};qs,_,end,eh=A.plan(word,(0,0),h);assert end==(-2,2) and eh==h
 for x,y in qs:
  z=A.add(A.add(p[0],p[1]),C(x+y));assert z[0]<=0 and z[1]<=0;upper=max(upper,z[2]);read_count+=1
 parents['q+a+c']=upper
 assert parents=={'blank':35,'q':39,'q+a':71,'q+a+c':75},parents
 out=dict(status='exact whole-future read half-plane bounds',domain='n>=200',upper_z=parents,records=records,read_identities=read_count,source_template_sha256=hashlib.sha256(TFILE.read_bytes()).hexdigest(),scope='Geometry of already-certified words; color validity remains the old audited rectangle theorem.')
 (HERE/'upper_z_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

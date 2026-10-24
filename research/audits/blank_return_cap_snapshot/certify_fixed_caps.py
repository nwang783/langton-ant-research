"""Exact complete finite cap kernels, plus their infinite-rail comparison."""
import sys,json,gzip,hashlib
from pathlib import Path
from discover import initial,ROOT,HERE,BAD
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'))
from ant_exact import W,step,plan,certify_period
from crossing import tail

def main():
 source=json.loads((HERE/'discovery.json').read_text());assert [x['phase'] for x in source]==BAD;rows=[]
 for row in source:
  r=row['phase'];infinite,p,h=initial(r);assert [list(p),h]==row['start'];B=set(infinite.changes)
  for base,d,lo,hi in infinite.rays:
   assert lo==0 and hi is None
   for j in range(100):B.symmetric_difference_update({(base[0]+j*d[0],base[1]+j*d[1])})
   assert sum(base)+100*sum(d)<-250
  initial_mass=len(B);word=gzip.open(HERE/row['word_file'],'rt').read();assert word and set(word)<={'R','L'} and len(word)==row['capture'];reads=[]
  for expected in word:
   reads.append(p);before=p;before_h=h;p,h,ch=step(B,p,h);ip,ih,ic=infinite.step(before,before_h);assert (p,h,ch)==(ip,ih,ic) and ch==expected
  assert [list(p),h]==row['pose'];phase=row['tail']['phase'];tw=W[phase:]+W[:phase]
  finite_proof=certify_period(B,p,h,tw);infinite_proof=tail(infinite,p,h,tw);assert finite_proof and infinite_proof and list(finite_proof['drift'])==row['tail']['drift']
  qs,_,end,eh=plan(tw,p,h);drift=(end[0]-p[0],end[1]-p[1]);assert eh==h
  prefix_z=min(map(sum,reads));tail_z=min(map(sum,qs));guard=sum(drift)>=0
  assert prefix_z==row['z_bounds'][0] and prefix_z>=-125
  if guard:assert min(prefix_z,tail_z)>=-125
  rows.append(dict(phase=r,start=row['start'],capture=len(word),pose=[p,h],tail_phase=phase,drift=drift,finite_kernel_mass=initial_mass,finite_prefix_z_lower=prefix_z,entire_future_z_lower=min(prefix_z,tail_z) if guard else None,full_halfplane_transfer=guard,word_sha256=hashlib.sha256(word.encode()).hexdigest()))
 assert [x['phase'] for x in rows if x['full_halfplane_transfer']]==[13,60,70,75]
 out=dict(status='all five fixed endcaps exactly checked; four preserve z>=-250 forever',rows=rows,scope='The r28 fixed cap has a certified SW model tail, but its actual finite-history transfer is only a prefix statement.')
 (HERE/'fixed_caps.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

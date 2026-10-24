"""All-k>=200 failure of composing two clean U-turn crossings.

Complete finite seed: canonical13cellseed plus two finite settled rails, each
12*(2*80+1)=1932blackcells. This proves first mismatch of a proposed closed word,
not the complete long-term outcome. Discovery capture probes remain separate.
"""
import sys,json,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path[:0]=[str(HERE),str(HERE.parent/'transverse'),str(Path('/workspace/shared/langton/continuation_2026-10-22/ant_continuation/wake_clock')),str(Path('/workspace/shared/langton/continuation_2026-10-22/ant_continuation'))]
import certify_four_scatterer_prefix as a
from probe import REF,STATIC,alpha,row
import crossing as c
from ant_exact import plan
LOW=200;M=80

def main():
 a.LOW=LOW
 for key in a.STATS:a.STATS[key]=0
 a.READ_POINTS.clear();a.READ_RAYS.clear()
 assert set(REF)<={'R','L'} and len(REF)==21224
 assert set(c.WORD)<={'R','L'} and len(c.WORD)==104
 audited=json.loads((HERE.parent/'transverse/crossings_certificate.json').read_text())
 record=next(r for r in audited['records'] if (r['rotation'],r['a'],r['s'])==(3,0,1))
 assert hashlib.sha256(row['word'].encode()).hexdigest()==record['word_sha256']
 assert row['t0']==record['first_contact'] and row['cert']['phase']==record['tail']['phase']
 original={a.point(*q) for q in map(tuple,c.DATA['seed'])}
 lower={((c.D[0],b[0]+j*e[0]),(c.D[1],b[1]+j*e[1])) for b,e,_,_ in STATIC for j in range(-M,M+1)}
 upper={a.point(*c.plus(alpha,c.rotate(c.plus(b,c.times(j,e)),2))) for b,e,_,_ in STATIC for j in range(-M,M+1)}
 # Different diagonal sums make all three groups disjoint uniformly.
 assert len(original)==13 and len(lower)==len(upper)==1932
 def sumaff(q):return a.add(q[0],q[1])
 assert max(a.val(sumaff(q)) for q in lower)<min(a.val(sumaff(q)) for q in original)
 assert all(sumaff(q)[0]==-4 for q in lower)
 assert max(a.val(sumaff(q)) for q in original)<min(a.val(sumaff(q)) for q in upper)
 field=a.Field(original|lower|upper)
 assert not field.point_color(a.point(0,-2))
 wd=a.word_data(c.WORD,c.H0);fd=a.word_data(REF,c.H0)
 assert wd[2:]==(c.D,c.H0) and fd[2:]==(alpha,(c.H0+2)%4)
 p=a.point(0,0)
 p=a.apply_periods(field,wd,p,0,(1,0),'initial incoming flight')
 p=a.apply_finite(field,fd,p,0,'first U-turn reference')
 assert p==((c.D[0],alpha[0]),(c.D[1],alpha[1]))
 p=a.apply_periods(field,wd,p,2,(1,0),'opposite return flight')
 assert p==a.point(*alpha)
 partial=REF[:21072];pd=a.word_data(partial,c.H0)
 assert len(REF)-len(partial)==152
 first_time=[2*len(c.WORD),len(REF)+len(partial)]
 return_time=[2*len(c.WORD),2*len(REF)]
 assert first_time==[208,42296] and return_time==[208,42448]
 p=a.apply_finite(field,pd,p,2,'second U-turn until mismatch')
 assert p==a.point(0,-2) and (pd[3]+2)%4==c.H0
 assert REF[21072]=='R' and field.point_color(p)
 # Prove its most recent prior read is update100, an R in the first W.
 # Exact time inventory for the initial period run.
 qs,_,_,_=plan(c.WORD,(0,0),c.H0)
 hits=[]
 for i,q in enumerate(qs):
  j=a.line_coordinate(a.psub(p,a.point(*q)),c.D)
  if j is not None and a.in_range(j,(1,0)):hits.append((j[0]*104,j[1]*104+i,c.WORD[i]))
 assert hits==[(0,4,'R'),(0,8,'L'),(0,100,'R')]
 # The first recovery, return run and second recovery have not revisited it.
 # READ_POINTS and READ_RAYS are sets ofdistinct word read requirements; this
 # includes their endpoints only if actually read, as required.
 for q in a.READ_POINTS:assert a.no_point_collision(p,q)
 for idx,(base,d,N) in enumerate(a.READ_RAYS):
  if idx<len(a.word_data(c.WORD,c.H0)[0]):continue
  assert not a.ray_membership(p,base,d,N)
 assert p not in original
 out={'status':'all-parameter first-failure certificate passed; full capture not claimed',
  'parameter_domain':'integer k>=200','rail_half_length':M,'input_mass':3877,
  'planned_word':'(W^k REF)^2','planned_return_time':return_time,
  'first_difference_time':first_time,'first_difference_position':[0,-2],'heading':'W',
  'expected':'R','actual':'L','previous_read_time':100,'previous_letter':'R',
  'complete_previous_read_times':[4,8,100],'black_lifetime_age':[208,42196],'updates_before_planned_return':152,
  'reference_word_sha256':hashlib.sha256(REF.encode()).hexdigest(),
  'statistics':a.STATS,'finite_field_terms':len(field.points),'ray_terms':len(field.rays)}
 (HERE/'first_failure_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

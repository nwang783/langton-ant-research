"""All-parameter chronology of the two nonrenewing old-black collisions."""
import sys,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
SRC=Path('/workspace/shared/langton/continuation_2026-10-22/ant_continuation/wake_clock')
sys.path[:0]=[str(SRC),str(SRC.parent)]
import certify_four_scatterer_prefix as a
from ant_exact import step,plan,W,LEGAL10
from single_blocks import REFERENCE,block

T=json.loads((HERE/'completion_template.json').read_text())
OLD=json.loads((SRC/'four_scatterer_affine_prefix_certificate.json').read_text())
F=OLD['fixed_recovery_word'];P=OLD['period_word']
starts=[a.point(-127,-107),((-2,-151),(2,-82)),((0,-126),(4,-58)),((2,-102),(2,-83))]

def fixed_history(word,base,j,h,time,label):
 qs,hs,end,eh=plan(word,(0,0),h)
 return dict(label=label,points=[a.translate_local(q,base,j) for q in qs],word=word,time=time,drift=None,N=(0,1))

def periodic_history(word,base,j,h,time,N,label):
 row=fixed_history(word,base,j,h,time,label)
 _,_,d,eh=plan(word,(0,0),h);assert eh==h
 row.update(drift=a.rotate(d,j),N=N);return row

def visits(target,history):
 out=[]
 for row in history:
  for i,(q,c) in enumerate(zip(row['points'],row['word'])):
   if row['drift'] is None:
    if q!=target:
     assert a.no_point_collision(q,target);continue
    k=a.ZERO
   else:
    k=a.line_coordinate(a.psub(target,q),row['drift'])
    if k is None or not a.in_range(k,row['N']):continue
   time=a.add(row['time'],a.add(a.scale(k,len(row['word'])),(0,i)))
   out.append(dict(time=time,letter=c,stage=row['label'],phase=i,epoch=k))
 # Distinct within-stage read occurrences are sorted by affine time at LOW;
 # every adjacent order must then hold throughout the unbounded domain.
 out.sort(key=lambda r:a.val(r['time']))
 for u,v in zip(out,out[1:]):assert a.nonneg(a.sub(a.sub(v['time'],u['time']),a.ONE))
 assert all(u['letter']!=v['letter'] for u,v in zip(out,out[1:]))
 return out

def main():
 a.LOW=128
 assert a.LOW==128 and P==W[61:]+W[:61] and len(F)==7183
 for word in (F,P,T['prefix_word'],T['period_word'],T['suffix_word']):
  assert word and set(word)<={'R','L'}
 assert T['suffix_word'][0]=='L' and T['period_word'][0]=='R'
 # Bind this copied word to the same literal fixed source used in the
 # complete affine field checker, not just to another JSON label.
 rb,rp,rh,_=REFERENCE;rb=rb|block((-127,-108))
 for _ in range(5781):rp,rh,_=step(rb,rp,rh)
 assert rp==(-127,-107) and rh==2
 actual=[]
 for _ in range(7183):rp,rh,c=step(rb,rp,rh);actual.append(c)
 assert ''.join(actual)==F
 B=set();p=(0,0);h=0;prefix=[]
 for _ in range(15758):p,h,c=step(B,p,h);prefix.append(c)
 prefix=''.join(prefix)
 history=[fixed_history(prefix,a.point(0,0),0,0,a.ZERO,'initial prelude')]
 for j in range(4):
  time=(104*j,15758+7183*j)
  history.append(fixed_history(F,starts[j],j,2,time,'scatterer F'+str(j)))
  fd=a.word_data(F,2);base=a.translate_local(fd[2],starts[j],j)
  history.append(periodic_history(P,base,j,3,a.add(time,(0,7183)),(1,0) if j<3 else (1,-65),'old side P'+str(j)))
 fourth_base=starts[3];fd=a.word_data(F,2)
 fourth_base=a.translate_local(fd[2],fourth_base,3)
 fourth_base=a.padd(fourth_base,(a.scale((1,-65),-2),a.scale((1,-65),-2)))
 assert fourth_base==a.point(3,23)
 history.append(fixed_history(P[:10],fourth_base,3,3,(416,37730),'fourth side partial'))
 q1=a.point(4,22);v1=visits(q1,history)
 assert v1==[dict(time=(0,9500),letter='R',stage='initial prelude',phase=9500,epoch=(0,0))]
 q2=((-2,-23),(2,37));q2visits_before=visits(q2,history)
 history.append(fixed_history(T['prefix_word'],q1,0,2,(416,37740),'old-core recovery'))
 history.append(periodic_history(T['period_word'],a.point(-19,33),0,0,(416,39506),(1,2),'new NW flight'))
 v2=visits(q2,history)
 assert len(v2)==1
 assert v2[-1]['time']==(104,35382) and v2[-1]['letter']=='R'
 assert v2==q2visits_before
 # At input both collision sites are white, uniformly in L.
 G={(0,-1),(0,0),(1,-1),(1,0)}
 for q in (q1,q2):
  for j in range(4):
   for g in G:assert a.no_point_collision(q,a.translate_local(g,starts[j],j))
 # Every variable period is at least one full copy at L>=128. Inserting a
 # whole copy inside a >=104-letter standard run preserves the ordered
 # forbidden-ten sequence, without assuming legal exterior joins.
 L=128
 full=prefix+''.join(F+P*(L if j<3 else L-65) for j in range(4))+P[:10]+T['prefix_word']+T['period_word']*(L+2)+T['suffix_word']
 events=[full[i:i+10] for i in range(len(full)-9) if full[i:i+10] not in LEGAL10]
 assert len(full)==520*L+43111 and len(events)==19629
 mass=16+full.count('R')-full.count('L');assert mass==60*L+2905
 assert P.count('R')-P.count('L')==12
 assert T['period_word'].count('R')-T['period_word'].count('L')==12
 out={'parameter_domain':'integer L >= 128','first_collision':{'q':q1,'time':(416,37740),'prior_visits':v1,'black_lifetime_age':(416,28240)},
 'second_collision':{'q':q2,'time':(520,39714),'prior_visits':v2,'black_lifetime_age':(416,4332)},
 'forbidden_10_window_count':19629,'capture_mass_affine':(60,2905),
 'event_sequence_sha256':__import__('hashlib').sha256(''.join(events).encode()).hexdigest(),
 'status':'exact affine incidence/chronology checks passed; count invariance uses interior period insertion'}
 (HERE/'provenance_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

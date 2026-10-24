"""Canonical-tail interface geometry, independent of complete-field colors."""
import sys,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,'/workspace/shared/langton/continuation_2026-10-22/ant_continuation')
from ant_exact import canonical_source,certify_period,plan,W,PHASES

def rot(p,j):
 for _ in range(j%4):p=p[1],-p[0]
 return p

def interface(p,h,word):
 phase=PHASES[word];B,bp,bh=canonical_source(0,phase);r=(h-bh)%4;bp=rot(bp,r);delta=(p[0]-bp[0],p[1]-bp[1])
 clean={(rot(q,r)[0]+delta[0],rot(q,r)[1]+delta[1]) for q in B}
 assert certify_period(clean,p,h,word)
 qs,hs,end,eh=plan(word,p,h);d=(end[0]-p[0],end[1]-p[1]);skip=(104-phase)%104
 _,_,p0,h0=plan(word[:skip],p,h);rs,rhs,_,_=plan(W,p0,h0)
 return dict(phase=phase,drift=d,canonical_field_u_bounds=[min(x-y for x,y in clean),max(x-y for x,y in clean)],tail_first_period_u_bounds=[min(x-y for x,y in qs),max(x-y for x,y in qs)],tail_all_future_z_bounds=[min(x+y for x,y in qs),max(x+y for x,y in qs)],phase72_base=rs[72],phase72_heading=rhs[72])

def main():
 T=json.loads((HERE/'template.json').read_text())
 two=interface((40,-50),2,T['segments'][9]['word'])
 three=interface((-228,268),0,T['infinite_tail_word'])
 # Every final-tail point is translated by(-2(m-100),2(m-100)).
 three['phase72_base_affine_m']=[[-2,three['phase72_base'][0]+200],[2,three['phase72_base'][1]-200]]
 three['canonical_field_u_lower_affine_m']=[-4,three['canonical_field_u_bounds'][0]+400]
 assert three['phase72_base_affine_m']==[[-2,-36],[2,72]]
 assert (-36)%2==0 and (-33)%2==1
 out=dict(status='tail interface geometry checked; actual-state coupling uses bivariate certificate',two_bit=two,three_bit_at_m100=three,final_exceptional_ray_x_parity=0,original_q_column_x_parity=1)
 (HERE/'interface_geometry.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

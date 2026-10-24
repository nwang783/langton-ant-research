"""Exact asymptotic read-support classification, fixed far-SW site, n->infinity.
This is geometry of an already color-certified parent, not a new color proof.
"""
import sys,json,hashlib
from pathlib import Path
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'))
from ant_exact import plan,W,multiple
TFILE=ROOT/'continuation_2026-10-22/ant_continuation2/planar_structure/exceptional_rectangle_template.json'
def cross(p,d):return p[0]*d[1]-p[1]*d[0]
def uu(p):return sum(p)
def zz(p):return p[0]-p[1]
def main():
 assert hashlib.sha256(TFILE.read_bytes()).hexdigest()=='16246ec40cbdd4ad94c35698992582b27a942dc7d539683f1b3684892cd5687d'
 T=json.loads(TFILE.read_text());slope=(0,0);base=(0,0);h=0;limits=[];eligible=[];rows=[]
 for i,s in enumerate(T['segments']):
  assert s['type'] in ('finite','periods')
  assert set(s['word'])<={'R','L'}
  qs,_,end,eh=plan(s['word'],(0,0),h);pts=[(base[0]+q[0],base[1]+q[1]) for q in qs]
  if s['type']=='finite':
   if slope==(0,0):limits.extend(map(uu,pts))
   rows.append(dict(segment=i,type='finite',slope=slope,constant_read_u_bounds=[min(map(uu,pts)),max(map(uu,pts))]))
   base=(base[0]+end[0],base[1]+end[1])
  else:
   ca,cb=s['count'];assert ca>=0 and len(s['word'])==104 and eh==h
   tag='eventually absent'
   if ca==0:
    if slope==(0,0):limits.extend(uu(p)+min(0,(cb-1)*uu(end)) for p in pts)
   elif cross(slope,end)==0:
    ell=multiple(slope,end);assert ell is not None;alpha=-ell
    if 0<alpha<ca:
     if uu(end):tag='crosses every fixed on-line site'
     else:limits.extend(map(uu,pts));tag='fixed z level, excluded by cutoff'
    elif alpha==0:
     limits.extend(map(uu,pts));tag='hits far-SW sites' if uu(end)<0 else 'misses far-SW sites'
    elif alpha==ca:
     limits.extend(uu(p)+(cb-1)*uu(end) for p in pts);tag='hits far-SW sites' if uu(end)>0 else 'misses far-SW sites'
    if tag in ('crosses every fixed on-line site','hits far-SW sites'):
     assert zz(end)==0
     classes=sorted(set((zz(p),p[0]%2) for p in pts));zlo,zhi=min(z for z,_ in classes),max(z for z,_ in classes)
     assert classes==[(z,parity) for z in range(zlo,zhi+1) for parity in (0,1)]
     eligible.append(dict(segment=i,drift=end,u_range=[zlo,zhi],classes=classes))
   rows.append(dict(segment=i,type='periods',slope=slope,base=base,drift=end,count=[ca,cb],tag=tag))
   slope=(slope[0]+ca*end[0],slope[1]+ca*end[1]);base=(base[0]+cb*end[0],base[1]+cb*end[1])
  h=eh
 # The final NW tail starts farther NW as n grows, so no fixed far-SW site
 # lies ahead of its start for every sufficiently large n.
 assert set(T['infinite_tail_word'])<={'R','L'}
 qs,_,end,eh=plan(T['infinite_tail_word'],(0,0),h);assert end==(-2,2) and slope==end and eh==h
 cutoff=min(limits)-1;assert cutoff==-94
 fresh=[]
 for origin,heading,levels,advance in [((-15,10),3,range(-28,-17),(-2,-2)),((6,-43),1,range(42,53),(-2,-2))]:
  wreads,_,drift,_=plan(W,(0,0),heading);phases=[]
  for i,q in enumerate(wreads):
   if any((k:=multiple((p[0]-q[0],p[1]-q[1]),drift)) is not None and (k>0 or k==0 and j<i) for j,p in enumerate(wreads)):continue
   phases.append(i)
  assert phases==[13,14,15,27,28,29,32,38,45,46,47,55,56,57,60,61,62,70,71,72,75,89]
  bases=[(origin[0]+wreads[r][0],origin[1]+wreads[r][1]) for r in phases]
  assert sorted((zz(b),b[0]%2) for b in bases)==[(z,p) for z in levels for p in (0,1)]
  fresh.append(dict(origin=origin,heading=heading,phases=phases,bases=bases,translation_per_m=advance,base_z_bounds=[min(map(uu,bases)),max(map(uu,bases))],sufficient_z_for_m100=min(map(uu,bases))-400))
 assert [(e['segment'],e['u_range']) for e in eligible]==[(1,[-28,-18]),(3,[42,52])]
 out=dict(status='exact eventual read-support classification for each fixed site with z below cutoff',z_cutoff=cutoff,fresh_frontiers=fresh,eligible_period_bands=eligible,rows=rows,tail_slope=slope,scope='For each fixed lattice site s with z(s)<=cutoff, the original rectangle trace reads s for all sufficiently large n iff u(s) belongs to one of these bands. Isolated finite-n coincidences are not claimed absent uniformly.')
 (HERE/'pristine_sw_bands.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

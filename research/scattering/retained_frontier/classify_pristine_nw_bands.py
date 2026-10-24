"""Exact asymptotic read-support classification, fixed far-NW site, n->infinity.
This is geometry of an already color-certified parent, not a new color proof.
"""
import sys,json
from pathlib import Path
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'))
from ant_exact import plan,W,multiple
TFILE=ROOT/'continuation_2026-10-22/ant_continuation2/planar_structure/exceptional_rectangle_template.json'
def cross(p,d):return p[0]*d[1]-p[1]*d[0]
def uu(p):return p[0]-p[1]
def zz(p):return sum(p)
def main():
 T=json.loads(TFILE.read_text());slope=(0,0);base=(0,0);h=0;limits=[];eligible=[];rows=[]
 for i,s in enumerate(T['segments']):
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
    if 0<alpha<ca:tag='crosses every fixed on-line site'
    elif alpha==0:
     limits.extend(map(uu,pts));tag='hits far-NW sites' if uu(end)<0 else 'misses far-NW sites'
    elif alpha==ca:
     limits.extend(uu(p)+(cb-1)*uu(end) for p in pts);tag='hits far-NW sites' if uu(end)>0 else 'misses far-NW sites'
    if tag in ('crosses every fixed on-line site','hits far-NW sites'):
     assert zz(end)==0
     classes=sorted(set((zz(p),p[0]%2) for p in pts));zlo,zhi=min(z for z,_ in classes),max(z for z,_ in classes)
     assert classes==[(z,parity) for z in range(zlo,zhi+1) for parity in (0,1)]
     eligible.append(dict(segment=i,drift=end,z_range=[zlo,zhi],classes=classes))
   rows.append(dict(segment=i,type='periods',slope=slope,base=base,drift=end,count=[ca,cb],tag=tag))
   slope=(slope[0]+ca*end[0],slope[1]+ca*end[1]);base=(base[0]+cb*end[0],base[1]+cb*end[1])
  h=eh
 # The final NW tail starts farther NW as n grows, so no fixed far-NW site
 # lies ahead of its start for every sufficiently large n.
 assert set(T['infinite_tail_word'])<={'R','L'}
 qs,_,end,eh=plan(T['infinite_tail_word'],(0,0),h);assert end==(-2,2) and slope==end and eh==h
 cutoff=min(limits)-1;assert cutoff==-71
 # Bind the completed first-frontier lattice coverage to the actual canonical
 # read phases, not a handwritten list of geometric bases.
 ordinary=json.loads((HERE/'ordinary_interfaces.json').read_text())['rows']
 wreads,_,_,_=plan(W,(0,0),2)
 phases=sorted([r['phase'] for r in ordinary]+[72]);assert len(phases)==22 and len(set(phases))==22
 bases=[]
 for r in ordinary:
  b=tuple( (-15-wreads[r['phase']][0],29-wreads[r['phase']][1]) )
  assert b==tuple(r['core_ray_base']);bases.append(b)
 bases.append((-15-wreads[72][0],29-wreads[72][1]));assert bases[-1]==(-23,31)
 assert sorted((zz(b),b[0]%2) for b in bases)==[(z,p) for z in range(7,18) for p in (0,1)]
 assert min(map(uu,bases))==-54
 assert min(map(uu,bases))-400==-454
 assert [(e['segment'],e['z_range']) for e in eligible]==[(5,[7,17]),(7,[-63,-53]),(11,[55,65])]
 out=dict(status='exact eventual read-support classification for each fixed site with u below cutoff',u_cutoff=cutoff,eligible_period_bands=eligible,rows=rows,tail_slope=slope,scope='For each fixed lattice site s with u(s)<=cutoff, the original rectangle trace reads s for all sufficiently large n iff z(s) belongs to one of these bands. Isolated finite-n coincidences are not claimed absent uniformly.')
 (HERE/'pristine_nw_bands.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

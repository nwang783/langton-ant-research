"""Exact affine GEOMETRY audit of already certified exceptional parents.

Does not re-prove color realizability: that is supplied by the separately
replayed exceptional rectangle certificate. Every coordinate statement below
is an identity in n (and, for periods, in the epoch k), not a parameter sample.
"""
import hashlib,json
from pathlib import Path
P=Path('/workspace/shared/langton/continuation_2026-10-22/ant_continuation2/planar_structure/exceptional_rectangle_template.json')
T=json.loads(P.read_text()); D=((0,1),(1,0),(0,-1),(-1,0))
def plan(word,h):
    x=y=0;pts=[]
    for c in word:
        pts.append((x,y));h=(h+(1 if c=='R' else -1))%4
        dx,dy=D[h];x+=dx;y+=dy
    return pts,(x,y),h

def bound(base,pts,drift=None):
    vals=[];witnesses=[]
    for x,y in pts:
        coeffs=[(base[0][0]+base[1][0],0 if drift is None else sum(drift),base[0][1]+base[1][1]+x+y),
                (base[0][0]-base[1][0],0 if drift is None else drift[0]-drift[1],base[0][1]-base[1][1]+x-y)]
        candidates=[(abs(c),axis,c) for axis,(a,k,c) in enumerate(coeffs) if a==k==0]
        assert candidates,(base,drift,(x,y),coeffs)
        value,axis,c=min(candidates);vals.append(value);witnesses.append((axis,c))
    return max(vals),witnesses

base=((0,0),(0,0));h=0;records=[];parent=[];HH=0;elapsed=(0,0)
for i,s in enumerate(T['segments']):
    pts,drift,after=plan(s['word'],h)
    isperiod=s['type']=='periods';assert s['type'] in ('finite','periods')
    H,witnesses=bound(base,pts,drift if isperiod else None);HH=max(HH,H)
    old=base
    if isperiod:
        assert h==after and abs(drift[0])==abs(drift[1])==2
        aa,bb=s['count'];assert aa*200+bb>=1 and aa>=0
        base=tuple((base[j][0]+aa*drift[j],base[j][1]+bb*drift[j]) for j in (0,1))
        elapsed=(elapsed[0]+aa*len(pts),elapsed[1]+bb*len(pts))
    else:
        base=tuple((base[j][0],base[j][1]+drift[j]) for j in (0,1))
        elapsed=(elapsed[0],elapsed[1]+len(pts))
    h=after
    records.append({'segment':i,'type':s['type'],'start':old,'end':base,'strip_width':H,'read_identities':len(witnesses)})
    if i in (4,8):
        word=T['segments'][i+1]['word'];p,d,g=plan(word,h)
        assert g==h and abs(d[0])==abs(d[1])==2
        HT,_=bound(base,p,d)
        parent.append({'input_bits':1 if i==4 else 2,'checkpoint_time':elapsed,'prefix_width':HH,'infinite_tail_width':HT,'full_width':max(HH,HT)})
pts,d,g=plan(T['infinite_tail_word'],h)
assert g==h and d==(-2,2)
H,_=bound(base,pts,d);HH=max(HH,H)
parent.append({'input_bits':3,'checkpoint_time':elapsed,'prefix_width':HH,'infinite_tail_width':H,'full_width':max(HH,H)})
assert elapsed==tuple(T['time'])
assert HH==82
out={'status':'PASS exact affine geometry identities; color validity is separate audited dependency','parameter_range':'all integers n>=200','template_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),'statement':'Every read of each one-, two-, and three-bit exceptional parent lies in |x+y|<=82 or |x-y|<=82.','parents':parent,'segments':records,'all_read_identities':sum(r['read_identities'] for r in records)+len(pts)}
Path('/workspace/shared/langton/audits/exceptional_diagonal_strips.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='segments'},indent=2))

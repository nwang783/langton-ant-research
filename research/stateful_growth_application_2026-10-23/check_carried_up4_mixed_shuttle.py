#!/usr/bin/env python3
"""One motivated unbounded-state mixed-rail cap application, not a word scan.
The carried cap is physically positive; its natural W20 incoming join is impossible.
"""
from pathlib import Path
import sys,json,hashlib,time
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).parent
sys.path.insert(0,str(ROOT/'stateful_growth_quadratic_2026-10-23'))
from quadratic_lap_validator import Program,Context,add,scale,D
PTH=ROOT/'new_constructive_2026-10-23'
carrier=json.loads((PTH/'two_layer_carried_endpoint.json').read_text())
shuttle=json.loads((PTH/'two_layer_restored_bulk_shuttle.json').read_text())
standard=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())
T='LRRL';W='LLRLRRRRLRRRRLLLLRLL';S='RLLR'
E=shuttle['stages'][1]['word'];assert len(E)==46
ctx=Context(max_operations=100000000)
def xor(a,b):return a.subtract(b).union(b.subtract(a)).coalesce()
def K_blocks(r=(1,10),k=(1,10)):
    result=[]
    for j in range(4):result.extend([(T,*r),('RL',*k),('R',0,1)])
    for row in carrier['stages']:
        ar,ak,c=row['count'];a=ar*r[0]+ak*k[0];b=ar*r[1]+ak*k[1]+c
        result.append((row['word'],a,b))
    result.extend([(T,*r),(E,0,1),(T,*r),('RR',0,1)])
    return result

def J_blocks(r=(1,10)):
    return [(T,*r),(E,0,1),(T,*r),('RRRRLL',0,1)]

def frame(r,k,shift=0):
    # Exact signed I(r,k+shift)+(0,shift), literal four-side definition.
    kk=k+shift;v=(2*r+kk,-kk-1);pos=(0,0);out=set()
    def rot(q,j):
        x,y=q
        for z in range(j):x,y=y,-x
        return x,y
    local={(x,0)for x in range(2*r)}|{(2*r+s,-s-1)for s in range(kk)}
    for j in range(4):
        out|={(pos[0]+rot(q,j)[0],pos[1]+rot(q,j)[1]+shift)for q in local}
        pos=add(pos,rot(v,j))
    assert pos==(0,0)
    return out

def literal_on_field(word,B,p=(0,0),h=1):
    B=set(B)
    for i,t in enumerate(word):
        assert ('L'if p in B else'R')==t,(i,p,h,t)
        if p in B:B.remove(p)
        else:B.add(p)
        h=(h+(1 if t=='R'else-1))%4;p=add(p,D[h])
    return B,p,h

def main():
    # Positive all-r,k composite is exactly full shuttle minus its final RRLL.
    final4=ctx.set('[r,k]->{[x,y]:r>=10 and k>=10 and ((x=0 and y=4)or(x=0 and y=3)or(x=-1 and y=3)or(x=-1 and y=2))}')
    returned=xor(ctx.set(shuttle['complete_returned_relation']),final4)
    # Complete field copied from the exact positive source, not a clean target.
    cap=Program(K_blocks((0,10),(0,10)),1,'literal_prepared_up4_cap')
    kw=''.join(w*b for w,a,b in cap.blocks)
    stored=(PTH/'two_layer_gap_frame_r10_k10.word.txt').read_text()
    assert kw==stored[:956]
    initial=frame(10,10)|frame(10,10,2)
    B,p,h=literal_on_field(kw,initial)
    assert len(initial)==248 and len(B)==280 and p==(0,4)and h==1
    exact=ctx.set('[r,k]->{[x,y]:r=10 and k=10 and ('+' or '.join(f'(x={x} and y={y})'for x,y in sorted(B))+')}')
    assert returned.intersect_params(ctx.set('[r,k]->{[]:r=10 and k=10}')).is_equal(exact)
    # The full composite word, not a claimed clean output, is carried into one
    # concrete balanced growing mixed-shuttle candidate. No parameter search.
    balanced=[(W,3,50)]+K_blocks()+[(S,3,50)]+J_blocks()
    programs=[Program(balanced,1,'balanced_growing_mixed_shuttle'),
              Program(balanced+[(standard['word'],1,1)],1,'white_writer_powered_quadratic_shuttle')]
    records=[]
    for P in programs:
        assert not P.bundled
        g=P._by[0,17];f=P._by[1,1]
        assert g.turn==f.turn=='R'and g.heading==2 and f.heading==0
        # The selected pair has delta=0; common quadratic term cancels exactly.
        source_n=add(g.b,scale(3,g.c));source_const=add(g.d,scale(49,g.c))
        assert source_n==f.b and source_const==f.d
        same=ctx.set('{[n,j,k]:n>=0 and j=3n+49 and k=0}')
        equations=[]
        for axis in (0,1):
            equations.append(f'{g.b[axis]-f.b[axis]}*n+{g.c[axis]}*j+{-f.c[axis]}*k+{g.d[axis]-f.d[axis]}=0')
        exact_pair=ctx.set('{[n,j,k]:n>=0 and 0<=j<3n+50 and 0<=k<n+10 and '+' and '.join(equations)+'}')
        assert same.subtract(exact_pair).is_empty()
        # Exact literal phase locations of the three intervening events.
        intermediates=[P._by[0,18],P._by[0,19],P._by[1,0]]
        offsets=[]
        for row in intermediates:
            if row.block==0:
                nn=add(row.b,scale(3,row.c));dd=add(row.d,scale(49,row.c))
            else:nn=row.b;dd=row.d
            assert nn==source_n
            off=tuple(dd[i]-source_const[i]for i in(0,1));assert off!=(0,0);offsets.append(off)
        assert offsets==[(-1,0),(-1,-1),(0,-1)]
        # Direct ONE earliest-lap virtual read control; no new orbit horizon.
        reads={};failure=None
        for e,q,hh,t in P.literal(1):
            if q in reads and reads[q][1]==t:
                failure=dict(current=e,previous=reads[q][0],cell=q,turn=t);break
            reads[q]=(e,t)
        assert failure and failure['current']==(0,1,0,1)and failure['previous']==(0,0,49,17)
        length_a=sum(len(w)*a for w,a,b in P.blocks);length_b=sum(len(w)*b for w,a,b in P.blocks)
        mass_a=sum((w.count('R')-w.count('L'))*a for w,a,b in P.blocks)
        mass_b=sum((w.count('R')-w.count('L'))*b for w,a,b in P.blocks)
        records.append(dict(name=P.name,A=P.A,B=P.B,lap_length=[length_a,length_b],lap_mass_delta=[mass_a,mass_b],
          collision_bound=P.bound,source_event=['n',0,'3n+49',17],target_event=['n',1,0,1],
          shared_cell_quadratic=P.A,shared_cell_linear=source_n,shared_cell_constant=source_const,
          selected_same_cell_relation=str(exact_pair),all_n_bad_pair_subrelation=str(same),
          intervening_offsets=offsets,source_relative_time='60n+997',target_relative_time='60n+1001',
          literal_first_conflict=failure,scope='Impossible on EVERY initial field, finite or infinite, even after arbitrary true past. No clean reset or initial-fuel premise is used.'))
    assert records[0]['A']==(0,0)and records[0]['B']==(0,4)
    assert records[0]['lap_length']==[160,2288]and records[0]['lap_mass_delta']==[0,44]
    assert records[1]['A']==(1,1)and records[1]['B']==(1,5)
    assert records[1]['lap_length']==[264,2392]and records[1]['lap_mass_delta']==[12,56]
    # Positive leading midpoint budget, so the quadratic example is NOT already
    # rejected by the elementary bounded-mass-vs-quadratic-position obstruction.
    assert records[1]['lap_mass_delta'][0]>=4*max(map(abs,records[1]['A']))
    report=dict(status='EXACT POSITIVE UP4 CAP AND ALL-PARAMETER NATURAL W20 PORT EXCLUSION',
        cap=dict(word='P(r,k) T^r E46 T^r RR',domain='r,k>=10',start_pose=[[0,0],1],endpoint=[[0,4],1],
                 initial='I(r,k) UNION [I(r,k+2)+(0,2)]',initial_mass=[16,8,8],returned_mass=[16,8,40],
                 duration=[64,16,156],mass_delta=32,complete_returned_relation=str(returned),
                 relation_to_signed_shuttle='complete_returned_relation XOR {(0,4),(0,3),(-1,3),(-1,2)}',
                 canonical_one_seed_reads=956,canonical_initial_mass=248,canonical_returned_mass=280),
        general_interface=dict(incoming='W20^M, M>=1, from E',cap='K(r,k), r,k>=10, from its actual arrived E port',
          source='last W20 copy, phase17, R, at (-2M,1)',target='first K straight transfer, phase1, R, at (-2M,1)',
          intervening_cells=[[-2,-2]],intervening_offsets=[[-1,0],[-1,-1],[0,-1]],
          statement='The source and target are consecutive same-cell reads with equal letters, independently of M,r,k and every previous/future field.'),
        programs=records,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        bindings={name:hashlib.sha256((PTH/name).read_bytes()).hexdigest()for name in ['two_layer_carried_endpoint.json','two_layer_restored_bulk_shuttle.json','two_layer_gap_frame_r10_k10.word.txt']},
        geometry_validator_sha256=hashlib.sha256((ROOT/'stateful_growth_quadratic_2026-10-23/quadratic_lap_validator.py').read_bytes()).hexdigest(),
        scope=__doc__)
    # Remove an unused placeholder, keeping the actual complete three-cell list.
    report['general_interface'].pop('intervening_cells')
    (HERE/'carried_up4_mixed_shuttle.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items()if k not in('cap','programs')},indent=2))
    for r in records:print(r['name'],'A',r['A'],'B',r['B'],'mass',r['lap_mass_delta'],'FIRST R/R',r['literal_first_conflict'])
if __name__=='__main__':main()

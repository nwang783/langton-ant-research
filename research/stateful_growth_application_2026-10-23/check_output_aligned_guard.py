#!/usr/bin/env python3
"""One output-aligned/reach-corrected carried-frame candidate, not a phase scan."""
from check_carried_up4_mixed_shuttle import *

def main():
    W6=W[6:]+W[:6]
    # Original W phase6 is the unique E-heading output-row3 port. Its
    # relative output solid row is y=0, matching the first T input rail.
    assert W6=='RRLRRRRLLLLRLLLLRLRR'
    blocks=[(W6,3,50)]+K_blocks((3,51),(1,10))+[(S,3,50)]+J_blocks((3,51))+[(standard['word'],1,1)]
    P=Program(blocks,1,'output_aligned_reach_corrected_quadratic_shuttle')
    assert P.A==(1,1)and P.B==(1,5)
    length=[sum(len(w)*a for w,a,b in P.blocks),sum(len(w)*b for w,a,b in P.blocks)]
    mass=[sum((w.count('R')-w.count('L'))*a for w,a,b in P.blocks),sum((w.count('R')-w.count('L'))*b for w,a,b in P.blocks)]
    assert length==[408,5344]and mass==[12,56]
    g=P._by[0,19];target=P._by[12,0]
    assert g.turn==target.turn=='R'and g.heading==target.heading==0
    qn=add(g.b,scale(3,g.c));q0=add(g.d,scale(49,g.c))
    assert qn==target.b and q0==target.d
    # ALL read events in the entire first four-heading frame which touch q.
    touches=ctx.set('{[n,b,j,r]:false}')
    for f in P.families:
        if not 1<=f.block<=12:continue
        eq=[]
        for a in(0,1):eq.append(f'{f.b[a]-qn[a]}*n+{f.c[a]}*j+{f.d[a]-q0[a]}=0')
        relation=ctx.set('{[n,b,j,r]:'+f.dom()+' and '+' and '.join(eq)+'}')
        touches=touches.union(relation)
    expected=ctx.set('{[n,b,j,r]:n>=0 and b=12 and j=0 and r=0}')
    assert touches.coalesce().is_equal(expected)
    # Actual finite prefix on its unique minimal First-L field; not merely
    # virtual geometry. No seed is changed or supplied during the execution.
    virtual=P.literal(1);history={};Bmin=set();failure=None
    for i,(e,q,h,t)in enumerate(virtual):
        if q in history and history[q][1]==t:
            failure=dict(index=i,current=e,previous=history[q][0],previous_index=history[q][2],cell=q,turn=t);break
        if q not in history and t=='L':Bmin.add(q)
        history[q]=(e,t,i)
    assert failure==dict(index=1899,current=(0,12,0,0),previous=(0,0,49,19),previous_index=999,cell=(-101,0),turn='R')
    prefix=''.join(t for e,q,h,t in virtual[:failure['index']])
    after,p,h=literal_on_field(prefix,Bmin)
    assert p==(-101,0)and h==0 and p in after
    source_path=ROOT/'causal_reduction/unit_scale/chamfered_frames_certificate.json'
    report=dict(status='EXACT OUTPUT-ALIGNED CARRIED-FRAME CLOSING-GUARD EXCLUSION',
      candidate=dict(W6=W6,M='3n+50',r='3n+51=M+1',k='n+10',
        word='W6^M K(r,k) S^M J(r) H104^(n+1)',A=P.A,B=P.B,lap_length=length,lap_mass_delta=mass,
        quadratic_shared_cell=P.A,linear_shared_cell=qn,constant_shared_cell=q0,
        source_event=['n',0,'3n+49',19],target_event=['n',12,0,0],
        source_time='60n+999',target_time='116n+1899',frame_guard_touches=str(touches.coalesce()),
        finite_prefix_control=dict(reads=len(prefix),minimal_seed_mass=len(Bmin),final_mass=len(after),head=p,heading=h,
          guarded_cell_is_black=True,first_prohibited_read=failure)),
      all_parameter_theorem=dict(domain='M>=1,r>=10,k>=10',incoming='phase6 cyclic cut W6^M from E',
        source='last W6 copy final R at(-2M-1,0)',consumer='final R of first F(r,k) at(-2M-1,0)',
        protection='F is self-avoiding and this is its last read; no intervening event touches the source cell.',
        scope='Impossible on any initial coloring, finite or infinite, regardless of all retained caps, passives and past history.'),
      separate_rail_reach=dict(necessary='r>M',reason='If1<=r<=M, the first R after T^r hits a still-current even-parity W6 output R.',
        motivated_choice='r=M+1 is the minimal integer avoiding that earlier obstruction; no parameter scan.'),
      source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      geometry_validator_sha256=hashlib.sha256((ROOT/'stateful_growth_quadratic_2026-10-23/quadratic_lap_validator.py').read_bytes()).hexdigest(),
      application_checker_sha256=hashlib.sha256((HERE/'check_carried_up4_mixed_shuttle.py').read_bytes()).hexdigest(),
      signed_frame_self_avoidance_binding=hashlib.sha256(source_path.read_bytes()).hexdigest(),
      scope=__doc__)
    (HERE/'output_aligned_guard.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
if __name__=='__main__':main()

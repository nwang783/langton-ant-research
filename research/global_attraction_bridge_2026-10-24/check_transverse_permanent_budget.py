"""Exact retrospective stock and permanent production for the moving return."""
from pathlib import Path
import json
from check_return_permanent_output_debt import DXY,future
P=Path(__file__).parent
main=json.loads((P/'TRANSVERSE_FAR_MODULE_CHECKED.json').read_text())
rec=main['protected_reference'];fates={tuple(z['cell']):z['death'] for z in rec['initial_read_fates']}
W=json.loads((P/'MOVING_CAPACITY_REGRESSION_CHECKED.json').read_text())['actual_permanent_phase_cells']
old_inputs=[]
for r in W:
    for v in range(-30,36):
        q=(r['cell'][0]+2*v,r['cell'][1]+2*v-3)
        if (v<-3 or v==-3 and r['phase']<=71) and q in fates and fates[q] is not None:
            old_inputs.append(dict(relative_cell=q,outgoing_phase=r['phase'],relative_copy=v,post_contact_death=fates[q]))
assert len(old_inputs)==191 and min(r['relative_copy'] for r in old_inputs)>=-30
G={(0,-1),(1,1),(1,3),(2,2)};B={q:-i-1 for i,q in enumerate(sorted(G))};p=(0,0);h=1;word='';AP=[];Q=[]
for t in range(286):
    (AP if t<182 else Q).append(p)
    if t==254:front=(dict(B),p,h)
    old=B.pop(p,None)
    if old is None:B[p]=t;h=(h+1)%4;word+='R'
    else:h=(h-1)%4;word+='L'
    p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
fw,fd,ft,checks=future(*front);assert len(ft)==19 and max(ft.values())<=116
A,U=word[:182],word[182:];bal=lambda w:w.count('R')-w.count('L')
balances=dict(A=bal(A),U=bal(U),U61=bal(U[:61]),U71=bal(U[:71]),U56=bal(U[:56]),U72=bal(U[:72]))
assert balances==dict(A=32,U=12,U61=11,U71=11,U56=8,U72=12)

# Additional exact upper extrema; main certificate supplies the lower extrema.
from check_return_permanent_output_debt import rot
poses=[((0,0),(0,0)),((14,-1),(14,0)),((10,0),(18,-4)),((2,5),(10,0))]
rs=[(7,-4),(2,-5),(4,-6),(2,-6)];parts=[61,71,61,56];heads=[1,0,3,2]
upper_tests=0
for stage in range(4):
    samples=[(q,(0,0)) for q in AP]
    for q in Q:samples.extend([(q,(0,0)),(q,(rs[stage][0],rs[stage][1]-1))])
    samples.extend((Q[t],rs[stage]) for t in range(parts[stage]))
    for q,jj in samples:
        r=rot(q,heads[stage]-1);d=rot((2,2),heads[stage]-1)
        for axis,bound in enumerate([(14,1),(18,-1)]):
            a=bound[0]-poses[stage][axis][0]-jj[0]*d[axis]
            b=bound[1]-poses[stage][axis][1]-r[axis]-jj[1]*d[axis]
            assert a>=0 and 10*a+b>=0;upper_tests+=1
assert Q[56]==(9,7)

controls=[]
for r in main['controls']:
    n=r['n'];seed=set(map(tuple,r['initial_black']));b=156*n-59;a=b+1;c=780*n-1207;N=r['physical_updates'];peak=468*n-455
    B={q:-i-1 for i,q in enumerate(sorted(seed))};p=(0,0);h=1;dead={};turns=[];positions=[];masses=[]
    for t in range(N):
        positions.append(p);masses.append(len(B));old=B.pop(p,None)
        if old is None:B[p]=t;h=(h+1)%4;turns.append('R')
        else:dead[old]=t;h=(h-1)%4;turns.append('L')
        p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
    tw,dr,tail,tests=future(B,p,h);dead.update({i:N+t for i,t in tail.items()})
    L=sum(i in dead for i in range(-16,0));La=Lc=Lp=None;Pcount=0
    for t,ch in enumerate(turns):
        if t==a:La=L
        if t==c:Lc=L
        if t==peak:Lp=L
        if a<=t<c and ch=='R' and t not in dead:Pcount+=1
        L+=int(t in dead) if ch=='R' else -1
    assert (La,Lc)==(222,285) and masses[a]==18*n+24 and masses[c]==90*n-67 and Pcount==72*n-154
    q=(3*n,3*n+3);radius=max(max(abs(x-q[0]),abs(y-q[1])) for x,y in positions[a:c+1])
    assert radius==6*n-4 and positions[peak]==(5*n+2,9*n-1)
    controls.append(dict(n=n,birth_cut_mass=masses[a],birth_cut_relevant=La,return_cut_mass=masses[c],return_cut_relevant=Lc,
        actual_permanent_births_during_return=Pcount,return_radius=radius,peak_cut=peak,peak_pose=positions[peak],peak_relevant=Lp,
        debt_lhs=Pcount+La+2*Lp+Lc,debt_rhs=4*radius,full_future_tests=tests))
out=dict(status='AUTHOR all-parameter balance annotations; independent audit pending',
    already_written_relevant_periodic_output=old_inputs,already_written_count=191,
    standalone_phase72_relevant=19,standalone_phase72_latest_read=max(ft.values()),standalone_tail_tests=checks,
    unread_initial_remote_inputs=12,exact_birth_cut_relevant=222,exact_return_cut_relevant=285,
    source_word_balances=balances,full_birth_cut_mass='18n+24',full_return_cut_mass='90n-67',
    actual_permanent_births_during_return='72n-154',return_radius='6n-4',
    exact_affine_upper_extrema_tests=upper_tests,controls=controls,
    scope='Actual whole-future permanence in the signed moving family, not template predictions. Identical translated contact profile does not bound cumulative physical production during its previous return.')
(P/'TRANSVERSE_PERMANENT_BUDGET_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='already_written_relevant_periodic_output'},indent=2))

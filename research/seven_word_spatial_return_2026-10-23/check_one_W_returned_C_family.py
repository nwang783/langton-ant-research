"""Exact one-W-base family, ten physical positives and causal left-port closure.

No arbitrary prefix-depth cutoff. Reverse fullpacket gate closure is exact;
long D branches have an actual unread-output white-port obstruction.
"""
from pathlib import Path
from collections import Counter
from fractions import Fraction as Q
import importlib.util
import hashlib
import json

ROOT=Path('/workspace/shared/langton')
HERE=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('lit',ROOT/'word_stabilization/check_foreign_return_interfaces.py')
lit=importlib.util.module_from_spec(sp)
sp.loader.exec_module(lit)
GP=ROOT/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json'
WP=ROOT/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json'
G=json.loads(GP.read_text())['geometry']
W={a:r['word']for a,r in zip('DCVUFQB',json.loads(WP.read_text())['macro_words'])}
FULL={r['name']:r['word']for r in G}
KEEP=(0,1,4,5,6,7,8,9)


def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def det(p,q):return p[0]*q[1]-p[1]*q[0]


def orders(d,v,u):
    if d+v+u==0:return[()]
    return[(a,)+s for a,n in(('D',d),('V',v),('U',u))if n
           for s in orders(d-(a=='D'),v-(a=='V'),u-(a=='U'))]


def E_counts(delta):
    x,y=delta
    if y>0:return[]
    result=[]
    for v in range(-y+1):
        d=-y-v;rest=x-d-3*v
        if rest>=0 and rest%4==0:result.append((d,v,rest//4))
    return result


def allowed_last(foreign):return('V','U')if foreign!='B'else('U',)


def literal_word(tokens):return ''.join(FULL.get(a,W.get(a))for a in tokens)


def hit(a,b,c,d):
    u,v,z=sub(b,a),sub(d,c),sub(c,a);den=det(u,v)
    if den:
        s,t=Q(det(z,v),den),Q(det(z,u),den)
        return dict(kind='point',s=s,t=t)if 0<=s<=1 and 0<=t<=1 else None
    if det(z,u):return None
    k=0 if u[0]else 1
    ends=Q(c[k]-a[k],u[k]),Q(d[k]-a[k],u[k])
    lo,hi=max(Q(0),min(ends)),min(Q(1),max(ends))
    return dict(kind='collinear',s_interval=(lo,hi))if lo<=hi else None


cases=[];positives=[]
def check_case(source_id,W_id,S,E,foreign,kind,count_tuple):
    source=G[source_id]['name'];W_packet=G[W_id]['name']
    tokens=(source,W_packet)+tuple(S)+(('C',)if kind=='single_tail_W'else())+tuple(E)+(foreign,'C')
    raw=literal_word(tokens);tr=lit.trace(raw+lit.M)
    row=dict(old_full_source=source,old_C_index=1 if source_id in(1,5,8)else 2,
             W_packet=W_packet,S_bases=S,E_bases=E,foreign=foreign,returned='raw_C',
             family=kind,count_tuple=count_tuple,literal_tokens=tokens,
             feasible=tr['feasible'])
    if not tr['feasible']:
        row['conflict']=tr
    else:
        seed={p for p,(c,t)in tr['first'].items()if c=='L'}
        board=set(seed);p,h=(0,0),0
        for tick,c in enumerate(raw+lit.M):
            assert(p in board)==(c=='L')
            board.symmetric_difference_update({p});h=(h+(-1 if c=='L'else 1))%4
            p=add(p,lit.DIRS[h])
        assert(*p,h)==tr['pose']
        atoms=[]
        for a in tokens:
            atoms.extend([a]if a in('F','C')else[a[0]]+['C']*a.count('C'))
        assert ''.join(W[a]for a in atoms)==raw
        p,h=(0,0),0;segments=[]
        for a in atoms:
            start=add((2*p[0],2*p[1]),lit.rot((-1,-1),h));ep=lit.trace(W[a])['pose']
            p=add(p,lit.rot(ep[:2],h));h=(h+ep[2])%4
            end=add((2*p[0],2*p[1]),lit.rot((-1,-1),h));segments.append((start,end))
        # Each positive has a simple old+foreign proxy, then the same unique
        # old vertex: incoming firstD END/outgoing firstC START, returned END.
        for j in range(len(segments)-1):
            for i in range(j-1):assert hit(*segments[i],*segments[j])is None
        nonadj=[]
        for i in range(len(segments)-2):
            z=hit(*segments[i],*segments[-1])
            if z is not None:
                assert z['kind']=='point'and z['t']==1
                assert(i,z['s'])in((0,Q(1)),(1,Q(0)))
                nonadj.append((i,z))
        assert len(nonadj)==2 and segments[-1][1]==segments[1][0]==(1,1)
        row.update(control_id=len(positives),initial_black=sorted(seed),
                   initial_mass=len(seed),raw_length=len(raw),raw_exit_pose=(*p,h),
                   raw_exit_mass=len(seed)+raw.count('R')-raw.count('L'),
                   complete_marker_exit_mass=len(board),
                   old_plus_foreign_proxy_simple=True,
                   first_returned_contact_outgoing_old_C_index=1,
                   first_contact_point=(1,1))
        positives.append(dict(row,raw_word=raw))
    cases.append(row)


for source_id in(1,5,8,6,9):
    for foreign,(X,Y)in{'F':(2,-5),'Q':(4,-5),'B':(5,-4)}.items():
        # One W base may OWN BOTH remaining Cs; these are not omitted.
        for W_id in(6,9):
            endpoint=G[W_id]['endpoint'];E_start=add((0,1),lit.rot(endpoint[:2],3))
            assert(endpoint[2]+3)%4==1
            for counts in E_counts((X-E_start[0],Y-E_start[1])):
                for E in orders(*counts):
                    if E and E[-1]in allowed_last(foreign):
                        check_case(source_id,W_id,(),E,foreign,'double_tail_W',counts)
        # Or the one W base owns ONE C, and a real S base owns the other C.
        for W_id in(1,5,8):
            endpoint=G[W_id]['endpoint'];SX,SY=add((0,1),lit.rot(endpoint[:2],3))
            assert(endpoint[2]+3)%4==2
            budget=SY-1-Y
            for e in range(budget+1):
                for f in range((budget-e)//3+1):
                    for g in range((budget-e-3*f)//4+1):
                        if e+f+g==0:continue
                        remaining=budget-e-3*f-4*g
                        for v in range(remaining+1):
                            d=remaining-v;four_u=X-SX+e+f-d-3*v
                            if four_u<0 or four_u%4:continue
                            for S in orders(e,f,g):
                                for E in orders(d,v,four_u//4):
                                    if E and E[-1]in allowed_last(foreign):
                                        check_case(source_id,W_id,S,E,foreign,'single_tail_W',(e,f,g,d,v,four_u//4))

assert len(cases)==1890 and len(positives)==10
assert Counter((r['family'],r['feasible'])for r in cases)=={
    ('double_tail_W',False):60,('single_tail_W',False):1820,('single_tail_W',True):10}
assert all(r['old_full_source']=='DC'and r['foreign']=='F'for r in positives)
assert [r['initial_mass']for r in positives]==[30,27,31,31,31,28,32,32,32,36]

# Actual D-production archive invariant, for ALL later D copies.
D=lit.trace(W['D']);assert D['pose']==(1,1,0)and D['last'][(2,0)][0]=='R'
assert(1,-1)not in D['first']
assert min(y for x,y in D['first'])==-1
# Copy k>=2 would need local(2-k,-k), below RAW min y=-1; k=1 was explicit.
D_archive=dict(new_output=(2,0),birth_RAW_read=D['last'][(2,0)],
               copy_i_global_output='(i+2,i)',next_copy_local_cell=(1,-1),
               next_copy_unread=True,all_k_at_least2_below_RAW_min_y=-1,
               no_later_D_copy_physically_reads_identity=True)

rail_guards=[]
for control_id,extra_prefix,port in((0,('DC',),(0,-2)),(3,('DC',),(0,-2)),
                                  (5,(),(-2,-4)),(6,(),(-3,-5))):
    suffix=literal_word(extra_prefix)+positives[control_id]['raw_word']+lit.M
    tr=lit.trace(suffix);assert tr['feasible']
    assert tr['first'][port][0]=='R'and port[1]-port[0]==-2 and port[1]<0
    rail_guards.append(dict(control_id=control_id,extra_prefix=extra_prefix,
                            before_WHITE_port=port,first_suffix_read=tr['first'][port],
                            forbidden_D_run_lengths_at_least=-port[1],
                            actual_earlier_D_producer_index='n+port.y',
                            source_output_unread_by_all_later_D=True))

# These are explicit finite closure templates, not a requested maximum depth.
# EVERY possible predecessor of EVERY node is rechecked. A feasible edge outside
# these templates fails the checker; none is silently discarded.
node_prefixes={
    0:[(),('V',),('DC',),('D','DC')],1:[()],2:[(),('D',)],
    3:[(),('DC',),('D','DC')],4:[(),('V',)],
    5:[(),('D',),('D','D'),('D','D','D')],
    6:[(),('D',),('D','D'),('D','D','D'),('D','D','D','D')],
    7:[()],8:[(),('V',)],9:[(),('D',)]}
reverse_nodes=[]
for control_id,prefixes in node_prefixes.items():
    allowed_nodes=set(prefixes)
    for prefix in prefixes:
        suffix=literal_word(prefix)+positives[control_id]['raw_word']+lit.M
        assert lit.trace(suffix)['feasible']
        queries=[];incoming=[]
        for source_id in KEEP:
            name=G[source_id]['name'];tr=lit.trace(G[source_id]['word']+suffix)
            if tr['feasible']:
                assert(name,)+prefix in allowed_nodes
                assert source_id not in(7,8,9)
                incoming.append(name)
                queries.append(dict(full_predecessor=name,feasible=True,
                                     next_node_prefix=(name,)+prefix))
            else:queries.append(dict(full_predecessor=name,feasible=False,conflict=tr))
        reverse_nodes.append(dict(control_id=control_id,prefix=prefix,
                                  exact_incoming_full_packets=incoming,
                                  all_eight_queries=queries))
assert len(reverse_nodes)==26
assert sum(len(row['all_eight_queries'])for row in reverse_nodes)==208


def encode(x):
    if isinstance(x,Q):return int(x)if x.denominator==1 else str(x)
    if isinstance(x,dict):return{k:encode(v)for k,v in x.items()}
    if isinstance(x,(list,tuple)):return[encode(v)for v in x]
    return x


deps=[GP,WP,ROOT/'word_stabilization/check_foreign_return_interfaces.py',
      HERE/'returned_C_source_reduction_manifest.json',
      HERE/'returned_C_double_tail_source_manifest.json',
      HERE/'returned_C_prepared_loop_control_manifest.json',
      HERE/'complete8_foreign_adjacency_manifest.json']
out=dict(status='AUTHOR_FROZEN_ONE_W_FAMILY_AND_CAUSAL_LEFT_CLOSURE_PENDING_REVIEW',
    scope='Exactly ONE W base after one of the other five containing old-C roles; actual single/double ownership of the two remaining Cs retained.1890 exact words give10 prepared finite positive loops. All ten have exact finite reverse full-eight gate closure and persistent-D-output white-port horizons, excluding a U-entry cut at or before their selected old source. No arbitrary-W or global seven-word claim.',
    total_cases=len(cases),family_counts={str(k):v for k,v in Counter((r['family'],r['feasible'])for r in cases).items()},
    all_endpoint_driven_cases=cases,positive_complete_board_controls=positives,
    physical_D_archive_invariant=D_archive,
    causal_D_rail_white_port_guards=rail_guards,
    complete_reverse_full_packet_gate_nodes=reverse_nodes,
    reverse_node_count=26,reverse_query_count=208,
    maximum_possible_earlier_fullpacket_prefix_lengths=[max(map(len,node_prefixes[i]))for i in range(10)],
    actual_U_entry_lift_before_selected_old_source=False,
    dependencies={str(path.relative_to(ROOT)):hashlib.sha256(path.read_bytes()).hexdigest()for path in deps})
(HERE/'one_W_returned_C_family.json').write_text(json.dumps(encode(out),indent=2)+'\n')
print('1890 exact endpoint words:1880 immutable conflicts,10 physical positives.')
print('All10 old+foreign paths simple; returned rawC first contacts outgoing oldC.')
print('26 reverse nodes/208 exact gates; no U-entry lift; D branches have causal white-port horizons.')

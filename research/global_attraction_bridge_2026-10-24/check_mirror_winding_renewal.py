"""Exact mirror winding identity and complete actual record-gap controls."""
from pathlib import Path
import hashlib,json
from collections import Counter
from mirror_pairing_geometry import DXY,whole,local_surgery
from check_return_permanent_output_debt import future
P=Path(__file__).parent
small_class=Counter()
small_cells=[(x,y)for x in range(3)for y in range(3)]
for mask in range(512):
    small={q for i,q in enumerate(small_cells)if mask>>i&1}
    whole(small,((0,0),1))
    for q in small_cells:
        h=1 if sum(q)%2==0 else 0
        rr=local_surgery(small,(q,h))
        small_class[rr['kind'],rr['same_orientation']]+=1
source=json.loads((P/'SOUTHWEST_ARCHIVE_IMPORT_CHECKED.json').read_text())
seed=set(map(tuple,source['controls'][0]['initial_seed']))
assert len(seed)==22 and source['controls'][0]['n']==100
jobs=[('blank',set(),10081,{0,8,52,355,509,9977,10081},None),
      ('MT100',seed,109168,{0,33345,33639,40071,52605,109168},(33345,33639))]
controls=[]
for name,initial,N,cuts,packet in jobs:
    B={q:-i-1 for i,q in enumerate(sorted(initial))};p=(0,0);h=1
    snapshots={};word=[];events=[];ledger=[]
    hull=[max([0]+[q[1]for q in B]),max([0]+[q[0]for q in B]),
          max([0]+[-q[1]for q in B]),max([0]+[-q[0]for q in B])]
    for t in range(N+1):
        z=[p[1],p[0],-p[1],-p[0]]
        for a in range(4):
            if z[a]>hull[a]:events.append([t,a]);hull[a]=z[a]
        if t in cuts:snapshots[t]=(dict(B),p,h,whole(set(B),(p,h)))
        if t==N:break
        if packet and packet[0]<=t<packet[1]:
            row=local_surgery(set(B),(p,h));row.update(tick=t,cell=p,turn='L'if p in B else'R');ledger.append(row)
        old=B.pop(p,None);ch='R'if old is None else'L';word.append(ch)
        if old is None:B[p]=t
        h=(h+(1 if ch=='R'else-1))%4;p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
    tail,dr,deaths,tests=future(B,p,h)
    if name=='blank':
        assert [snapshots[t][3]['positive_winding_area']for t in(0,8,52,355,509,9977,10081)]==[0,0,0,2,0,220,222]
        assert [355,509] in [[events[i][0],events[i+1][0]]for i in range(len(events)-1)]
        assert [(u[0],v[0])for u,v in zip(events,events[1:])if v[0]<=509 and v[0]-u[0]>104]==[(355,509)]
        assert ''.join(word[9977:])==tail
        change=[]
    else:
        assert [33345,33639] in [[events[i][0],events[i+1][0]]for i in range(len(events)-1)]
        assert [(u[0],v[0])for u,v in zip(events,events[1:])if v[0]<=33639 and v[0]-u[0]>104]==[(33345,33639)]
        assert [40071,109168] in [[events[i][0],events[i+1][0]]for i in range(len(events)-1)]
        assert snapshots[33345][3]['positive_winding_area']==137
        assert snapshots[33639][3]['positive_winding_area']==139
        assert snapshots[40071][3]['positive_winding_area']==170
        assert snapshots[109168][3]['positive_winding_area']==504
        assert sum(r['positive_area_change']for r in ledger)==2
        assert sum(max(r['positive_area_change'],0)for r in ledger)==99
        assert sum(max(-r['positive_area_change'],0)for r in ledger)==97
        delta=Counter({tuple(q):n for q,n in snapshots[33639][3]['positive_winding']})
        delta.subtract({tuple(q):n for q,n in snapshots[33345][3]['positive_winding']})
        change=[dict(plaquette=q,change=n)for q,n in sorted(delta.items())if n]
        assert Counter(r['change']for r in change)==Counter({1:8,-1:6})
        # A single future noncanonical cut excludes earlier entry to an all-future canonical tail.
        later=''.join(word[33639:33639+208]);bad=[]
        for phase in range(104):
            expected=(tail[phase:]+tail[:phase])*2
            mismatch=next((i for i in range(208)if later[i]!=expected[i]),None)
            assert mismatch is not None;bad.append(mismatch)
    records=[]
    for t,(bb,pp,hh,g)in sorted(snapshots.items()):
        records.append(dict(cut=t,pose=[pp,hh],complete_black=[dict(cell=q,lifetime=i)for q,i in sorted(bb.items())],geometry=g))
    controls.append(dict(name=name,initial_black=sorted(initial),initial_pose=[[0,0],1],fine_reads=N,
                         whole_word=''.join(word),union_records=events,complete_cuts=records,
                         local_packet=packet,local_surgery_ledger=ledger,
                         positive_surgery_events=[r for r in ledger if r['positive_area_change']],
                         gross_positive_area_created=sum(max(r['positive_area_change'],0)for r in ledger),
                         gross_positive_area_cancelled=sum(max(-r['positive_area_change'],0)for r in ledger),
                         packet_positive_winding_change=change,
                         canonical_phase_rejection=bad if packet else None,
                         infinite_tail_word=tail,tail_drift=dr,tail_parity_tests=tests))
files=['ROTOR_EXCURSION_TRANSFER_AUDIT_BINDING.json','SOUTHWEST_ARCHIVE_IMPORT_MANIFEST.json',
       '../audits/check_southwest_archive_import_independent.json',
       'MT_COMPLETED_DROUGHT_INVENTORY_MANIFEST.json','../audits/check_MT_completed_drought_inventory_independent.json',
       '../../langton/first_principles_2026-10-21/ant_rethink/switching_geometry/tait_cursor_and_loop_surgery.md']
for f in files:assert(P/f).exists(),f
out=dict(status='AUTHOR: pointwise winding and actual renewal countercontrol; independent audit pending',
         controls=controls,total_full_reads=sum(c['fine_reads']for c in controls),
         all_3_by_3_boards=512,small_surgeries=4608,
         small_surgery_class_counts=[dict(kind=k[0],same_orientation=k[1],count=v)for k,v in sorted(small_class.items())],
         dependencies={f:hashlib.sha256((P/f).read_bytes()).hexdigest()for f in files},
         scope='General finite-board static mirror identity and exact surgery classification. Named full blank/MT100 histories only. No all-n area inference, monotonicity, permanence charge, or global capture claim.')
(P/'MIRROR_WINDING_RENEWAL_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n')
print('Full reads',out['total_full_reads'])
for c in controls:
    print(c['name'],[(r['cut'],r['geometry']['positive_winding_area'])for r in c['complete_cuts']])
    if c['local_packet']:
        print('surgery net',sum(r['positive_area_change']for r in c['local_surgery_ledger']),
              'nonzero events',len(c['positive_surgery_events']),
              'max rejection',max(c['canonical_phase_rejection']))

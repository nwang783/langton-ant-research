"""Axial pristine-record specialization of the whole mirror pairing identity."""
from pathlib import Path
import hashlib,json
from mirror_pairing_geometry import circuit,winding,local_surgery,DXY
P=Path(__file__).parent
S=json.loads((P/'MIRROR_WINDING_RENEWAL_CHECKED.json').read_text())
out=[]
for c in S['controls']:
    B={tuple(q):-i-1 for i,q in enumerate(c['initial_black'])};p=(0,0);h=1
    dot=lambda a,q:(q[1],q[0],-q[1],-q[0])[a]
    hull=[max([0]+[dot(a,q)for q in B])for a in range(4)]
    records=[]
    for t in range(len(c['whole_word'])+1):
        axes=[a for a in range(4)if dot(a,p)>hull[a]]
        for a in axes:
            assert h==a and p not in B
            assert all(dot(a,q)<dot(a,p)for q in B)
            other=circuit((p,(h+2)%4),set(B));ow,oa=winding(other)
            assert len(other)==4 and oa==-1 and all(dot(a,z[0])>=dot(a,p)for z in other)
            active=circuit((p,h),set(B));aw,aa=winding(active)
            assert aa<0 and all(dot(a,z[0])<=dot(a,p)for z in active)
            assert set(active).isdisjoint(other)
            r=local_surgery(set(B),(p,h))
            assert r['kind']=='merge' and r['same_orientation'] and r['positive_area_change']==0
            assert r['new_lengths']==[len(active)+4] and r['new_areas']==[aa-1]
            records.append(dict(tick=t,axis=a,pose=[p,h],active_before_length=len(active),
                                active_before_area=aa,active_after_length=len(active)+4,
                                active_after_area=aa-1,other_loop=other,
                                complete_field_sha256=hashlib.sha256(json.dumps(sorted(B.items()),separators=(',',':')).encode()).hexdigest()))
        for a in range(4):hull[a]=max(hull[a],dot(a,p))
        if t==len(c['whole_word']):break
        ch='L'if p in B else'R';assert ch==c['whole_word'][t]
        if ch=='R':B[p]=t
        else:B.pop(p)
        h=(h+(1 if ch=='R'else-1))%4;p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
    assert [[r['tick'],r['axis']]for r in records]==c['union_records']
    out.append(dict(name=c['name'],full_reads=len(c['whole_word']),records=records))
deps=['MIRROR_WINDING_RENEWAL_MANIFEST.json','MIRROR_WINDING_RENEWAL_CHECKED.json','mirror_pairing_geometry.py']
report=dict(status='AUTHOR: pristine-record mirror corollary; independent audit pending',controls=out,
            full_reads=sum(c['full_reads']for c in out),records=sum(len(c['records'])for c in out),
            dependencies={f:hashlib.sha256((P/f).read_bytes()).hexdigest()for f in deps},
            scope='Every genuine augmented-hull axial record: fresh clockwise unit-loop merger, active perimeter+4, positive winding area unchanged. No subsequent-return or clock-density conclusion.')
(P/'MIRROR_PRISTINE_RECORD_CHECKED.json').write_text(json.dumps(report,indent=2)+'\n')
print('whole reads',report['full_reads'],'exact record mergers',report['records'])

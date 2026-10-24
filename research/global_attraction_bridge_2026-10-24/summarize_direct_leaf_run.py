"""Read-only complete-output binding. A partial run cannot become COMPLETE here."""
from pathlib import Path
import json, gzip, hashlib, collections, re

P=Path(__file__).parent
R=P/'direct_leaf_complete_run'
def sha(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
    return h.hexdigest()

status=json.loads((R/'RUN_STATUS.json').read_text())
assert status['status']=='COMPLETE' and status['covered']==status['total']==4483915
plan=json.loads((R/'RUN_INPUT_MANIFEST.json').read_text())
source=json.loads((P/'TWO_BLACK_DIRECT_LEAF_SOURCE_PLAN.json').read_text())
assert sha(P/'TWO_BLACK_DIRECT_LEAF_SOURCE_PLAN.json')==plan['source_plan_sha256']
assert sha(P/'TWO_BLACK_PARENT_DIRECT_LEAVES.txt')==plan['parent_obligation_file_sha256']
assert len(source['parents'])==2432 and len(source['raised'])==32824
bh=sha(P/'run_all_direct_leaf_words'); ph=sha(R/'RUN_INPUT_MANIFEST.json')
assert bh==status['binary_sha256'] and ph==status['input_manifest_sha256']
ref='10110000110110000110000110100001011110000100100001111010000100001111010000101100111100110000110010110110'
assert len(ref)==104 and len({ref[i:]+ref[:i] for i in range(104)})==104
geometries={}
for phase in range(104):
    word=ref[phase:]+ref[:phase]
    for heading in range(4):
        h=heading;x=y=0
        for bit in word:
            h=(h+(3 if bit=='1' else 1))%4
            x+=(0,1,0,-1)[h];y+=(1,0,-1,0)[h]
        assert h==heading and abs(x)==abs(y)==2
        geometries[phase,heading]=(x,y)

counts=collections.Counter(); phases=collections.Counter(); drifts=collections.Counter()
child_reads=parent_reads=copied=0; total=0; maxT=(-1,None); maxS=(-1,None)
maxmass=(-1,None); rawall=hashlib.sha256(); chunk_bindings=[]
for c in plan['chunks']:
    assert c['first_id']==total
    name=c['name'];ip=R/c['input'];op=R/(name+'.observations.gz');cp=R/(name+'.checkpoint.json')
    ck=json.loads(cp.read_text())
    assert ck['status']=='COMPLETE' and ck['first_id']==total and ck['count']==c['count']
    assert ck['binary_sha256']==bh and ck['input_manifest_sha256']==ph
    assert sha(ip)==ck['input_sha256']==c['sha256']
    assert sha(op)==ck['compressed_output_sha256']
    m=re.fullmatch(r'COMPLETE first=(\d+) count=(\d+) child_reads=(\d+) parent_reads=(\d+) copied_black=(\d+) elapsed_ms=(\d+)\n',ck['stderr'])
    assert m and int(m[1])==total and int(m[2])==c['count']
    child_reads+=int(m[3]);parent_reads+=int(m[4]);copied+=int(m[5])
    raw=hashlib.sha256();n=0;localmax=0
    with open(ip) as inp,gzip.open(op,'rb') as out:
        for iline,line in zip(inp,out,strict=True):
            a=list(map(int,line.split()));b=list(map(int,iline.split()))
            assert len(a)==13 and a[0]==b[0]==total+n
            ident,before,s,T,dx,dy,A,x,y,h,phase,mass,statehash=a
            assert 0<=before<=s<T<=624000 and T-s==104
            assert geometries[phase,h]==(dx,dy) and 0<=statehash<2**64 and mass>=0
            if ident<4451091:
                assert b[1]==0 and len(b)==8 and before==b[3]
                p=source['parents'][b[2]]
                assert b[4:6]==p['point'] and p['tdiv']<=before<p['end']
                kind='parent_dynamic'
            else:
                r=source['raised'][ident-4451091]
                assert b[1]==1 and b[2]==len(r['cells']) and before==0
                assert b[3:]==[v for q in r['cells'] for v in q]
                kind=r['kind']
            counts[kind]+=1;phases[phase]+=1;drifts[str((dx,dy))]+=1
            if T>maxT[0]:maxT=(T,ident)
            if s>maxS[0]:maxS=(s,ident)
            if mass>maxmass[0]:maxmass=(mass,ident)
            localmax=max(localmax,T);raw.update(line);rawall.update(line);n+=1
    assert n==c['count'] and raw.hexdigest()==ck['uncompressed_output_sha256']
    assert localmax==ck['max_global_certificate_end']
    total+=n
    chunk_bindings.append(dict(name=name,first_id=c['first_id'],count=n,input_sha256=sha(ip),observations_sha256=sha(op),checkpoint_sha256=sha(cp)))
assert total==4483915 and counts['parent_dynamic']==4451091
assert sum(counts.values())==total
inventory=json.loads((P/'TWO_BLACK_WORD_JOB_INVENTORY.json').read_text())
root=Path('/workspace/shared/langton/sources/imfinn-two-black/lean/TwoBlack')
for name,digest in inventory['source_hashes'].items():
    assert sha(root/name)==digest
report=dict(status='AUTHOR COMPLETE; independent audit pending',total_obligations=total,counts=dict(counts),phase_counts=dict(sorted(phases.items())),drift_counts=dict(drifts),maximum_global_certificate_end=maxT,maximum_global_certificate_start=maxS,maximum_final_black_mass=maxmass,actual_child_reads=child_reads,shared_parent_reads=parent_reads,total_simulated_reads=child_reads+parent_reads,copied_full_parent_black_cells=copied,whole_raw_observation_stream_sha256=rawall.hexdigest(),canonical_reference_read_bits=ref,observation_columns=['id','before','certificate_start','certificate_end','dx','dy','halfplane_A','start_x','start_y','start_heading','canonical_phase','final_black_mass','diagnostic_full_black_hash'],phase_word_encoding='phase i denotes ref[i:]+ref[:i]; 1 means BLACK/L and 0 means WHITE/R',limits=status['limits'],run_cpu_seconds=status['total_child_cpu_seconds'],run_wall_seconds=status['wall_seconds'],run_max_rss_kib=max(json.loads((R/(c['name']+'.checkpoint.json')).read_text())['max_rss_kib'] for c in plan['chunks']),run_status_sha256=sha(R/'RUN_STATUS.json'),source_hashes=inventory['source_hashes'],chunk_bindings=chunk_bindings)
(P/'TWO_BLACK_DIRECT_WORD_ANNOTATIONS_CHECKED.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ['source_hashes','chunk_bindings','phase_counts']}))

"""Freeze a complete discovered producer family, without claiming independent signoff."""
from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parent;O=P/'dcv_producer_mutual_family_v2'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rows(p):return {tuple(map(int,l.split()))for l in p.read_text().splitlines()}
j=json.loads((O/'summary.json').read_text());assert j.get('stable_complete_family') and not j['reserved_rows']
st=j['stages'][-1];H=O/f"stage{st['stage']:02}"/'hypotheses.tsv';S=P/'dcv_anchored_signed102.tsv';hs,ss=rows(H),rows(S);assert ss<=hs and len(hs)==st['active_count'];R={tuple(r['tuple']):r for r in st['results']};assert set(R)==hs-ss
family=P/'dcv_producer_closed_family.tsv';assert not family.exists();family.write_bytes(H.read_bytes())
clauses=[]
for row in sorted(R):
 r=R[row];assert r['status']=='EXHAUSTED_NO_HIT';pre=Path(r['certificate_prefix']);q=json.loads(pre.with_suffix('.json').read_text());assert Path(q['candidate_hypothesis_file'])==H and q['candidate_hypothesis_sha256']==sha(H);assert rows(Path(q['extra_guard_file']))==ss
 assert tuple([q['source'],q['target'],*q['target_pose'],*q['protected_q']])==row
 files=[pre.with_suffix(ext)for ext in['.json','.dat','.bdd']]+[Path(str(pre)+'_verify.txt'),Path(q['base_model_file']),Path(q['base_model_file']).with_suffix('.dat'),Path(q['exact_label_model_file']),Path(q['exact_label_model_file']).with_suffix('.dat')]
 verify=json.loads(Path(str(pre)+'_verify.txt').read_text());assert verify['status']=='VERIFIED_INDUCTIVE_NO_HIT'
 clauses.append({'tuple':row,'candidate_index':r['candidate_index'],'model':str(pre.with_suffix('.json')),'invariant':str(pre.with_suffix('.bdd')),'variables':q['n'],'watched_cells':[a['cell']for a in q['producer_label_classes']],'verified_states':verify['states'],'files':{str(f):sha(f)for f in files}})
T=rows(P/'dcv_directional25_targets.tsv')
out={'status':'PROVISIONAL COMPLETE MUTUAL FAMILY; independent full-family audit required','family_file':str(family),'family_sha256':sha(family),'stage_family_file':str(H),'fixed_signed_file':str(S),'fixed_signed_sha256':sha(S),'family_count':len(hs),'known_signed_count':len(ss),'new_count':len(clauses),'stage':st['stage'],'directional25_covered':sorted(T&hs),'directional25_not_covered':sorted(T-hs),'protocol':'../core_periodicity_new/chronological_producer_certificate_protocol.md','clauses':clauses,'snapshot_tools_manifest':str(O/'tools_manifest.json'),'snapshot_tools_manifest_sha256':sha(O/'tools_manifest.json')}
(P/'dcv_producer_closed_family_manifest.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k!='clauses'},indent=2))

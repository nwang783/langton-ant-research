#!/usr/bin/env python3
"""Refresh derived research indexes after an explicitly reviewed manifest update.

This does not collect new files, sanitize prose, validate proofs, or rewrite
frozen certificates. Register reviewed additions/changes in artifacts.jsonl first.
"""
from pathlib import Path
from collections import defaultdict
import hashlib,json
R=Path(__file__).resolve().parents[1]
rows=[json.loads(line)for line in(R/'manifests/artifacts.jsonl').read_text().splitlines()]
seen=set();bydir=defaultdict(list);byhash=defaultdict(list)
for row in rows:
 rel=Path(row['path']);assert not rel.is_absolute()and'..'not in rel.parts
 assert row['path']not in seen;seen.add(row['path'])
 assert row['disposition']in['git','bulk_archive']
 if row['disposition']=='git':
  p=R/'research'/rel;assert p.is_file(),p
  b=p.read_bytes();assert len(b)==row['bytes']and hashlib.sha256(b).hexdigest()==row['sha256'],p
 bydir[str(rel.parent)].append(row);byhash[row['sha256']].append(row['path'])
dups=[{'sha256':h,'paths':paths}for h,paths in sorted(byhash.items())if len(paths)>1]
(R/'manifests/duplicate_artifacts.json').write_text(json.dumps(dups,indent=2)+'\n')
experiments=[]
for d,files in sorted(bydir.items()):
 if not any(Path(x['path']).suffix in ['.py','.cpp','.md','.lean']or'manifest'in Path(x['path']).name.lower()for x in files):continue
 experiments.append({'directory':d,'artifacts':len(files),'bytes':sum(x['bytes']for x in files),'bulk_artifacts':sum(x['disposition']=='bulk_archive'for x in files),'proof_notes':[x['path']for x in files if x['path'].endswith('.md')],'executable_sources':[x['path']for x in files if Path(x['path']).suffix in ['.py','.cpp','.c','.lean','.sh']],'manifest_and_report_candidates':[x['path']for x in files if'manifest'in Path(x['path']).name.lower()or Path(x['path']).name.lower().endswith(('independent.json','checked.json'))],'audit_status':'Consult exact artifact and dated audit; not inferred by index'})
(R/'manifests/experiments.jsonl').write_text(''.join(json.dumps(x,sort_keys=True)+'\n'for x in experiments))
heads=[{'heading':line.lstrip('# ').strip(),'line':i}for i,line in enumerate((R/'research/audit.md').read_text().splitlines(),1)if line.startswith('## ')]
(R/'manifests/audit_sections.json').write_text(json.dumps(heads,indent=2)+'\n')
s=json.loads((R/'manifests/snapshot_summary.json').read_text());s.update(git_artifacts=sum(x['disposition']=='git'for x in rows),git_artifact_bytes=sum(x['bytes']for x in rows if x['disposition']=='git'),bulk_artifacts=sum(x['disposition']=='bulk_archive'for x in rows),bulk_source_bytes=sum(x['bytes']for x in rows if x['disposition']=='bulk_archive'),sanitized_prose_files=sum(x.get('sanitized',False)for x in rows),indexed_directories=len(experiments),duplicate_groups=len(dups))
(R/'manifests/snapshot_summary.json').write_text(json.dumps(s,indent=2)+'\n')
metadata=[p for p in R.rglob('*')if p.is_file()and'.git'not in p.relative_to(R).parts and not p.is_relative_to(R/'research')and p.name!='repository_files.sha256']
(R/'manifests/repository_files.sha256').write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(R).as_posix()+'\n'for p in sorted(metadata)))
print(json.dumps({'research_artifacts':len(rows),'indexed_directories':len(experiments),'duplicate_groups':len(dups),'mathematical_status':'Not inferred or changed'},indent=2))

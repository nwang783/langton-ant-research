"""Finite retained-core superset from separately signed asymptotic exclusions."""
import json,pathlib,hashlib
P=pathlib.Path('/workspace/shared/langton');W=json.loads((P/'computability/singleton_first_block_input.json').read_text())['word'];D=((0,1),(1,0),(0,-1),(-1,0));PH=[13,14,15,27,28,29,32,38,45,46,47,55,56,57,60,61,62,70,71,72,75,89]
mapfile=P/'scattering/far_sw_core/pristine_sw_bands.json';old=json.loads(mapfile.read_text());assert old['z_cutoff']==-94
fronts=[];low=set()
for start,h,expected in [((-15,10),3,(-15,-8,-28,-18,1741)),((6,-43),1,(-34,-27,42,52,1840))]:
 x,y=start;pts=[]
 for c in W:
  pts.append((x,y));h=(h+(1 if c=='R' else -1))%4;dx,dy=D[h];x+=dx;y+=dy
 bases=[pts[r] for r in PH];assert (min(map(sum,bases)),max(map(sum,bases)),min(x-y for x,y in bases),max(x-y for x,y in bases))==expected[:4]
 row=next(a for a in old['fresh_frontiers'] if a['origin']==list(start));assert row['phases']==PH and row['bases']==[list(q) for q in bases]
 # Each ray is one residue in (u,z mod4), so these enumerate every low site exactly once.
 assert len({(x-y,(x+y)%4) for x,y in bases})==22
 cells={(x-y,x+y-4*m) for x,y in bases for m in range(100) if x+y-4*m<=-94};assert len(cells)==expected[4] and not (low&cells);low|=cells
 fronts.append({'origin':start,'fresh_bases':bases,'minimum_z_at_age99':min(map(sum,bases))-396,'excluded_uniform_z_cutoff':min(map(sum,bases))-397,'remaining_low_cells':len(cells)})
central={(u,z) for u in range(-460,502) for z in range(-93,76) if (u-z)%2==0 and (abs(u)<=82 or abs(z)<=82)}
assert len(central)==76905 and len(low)==3581 and not (central&low)
cells=central|low;assert len(cells)==80486 and min(z for u,z in cells)==-430
assert all(-460<=u<=501 and -430<=z<=75 and (abs(u)<=82 or abs(z)<=82) for u,z in cells)
pairs=sorted(((u+z)//2,(z-u)//2) for u,z in cells);blob=''.join(f'{x},{y}\n' for x,y in pairs).encode();out={'status':'PASS; finite necessary region only, not exclusion of its remaining cells','uv_bounding_box':[-460,501,-430,75],'common_negative_z_exclusion':-431,'central_count':len(central),'low_ray_count':len(low),'total_candidate_superset':len(cells),'sorted_xy_sha256':hashlib.sha256(blob).hexdigest(),'xy_bounding_box':[min(x for x,y in pairs),max(x for x,y in pairs),min(y for x,y in pairs),max(y for x,y in pairs)],'fronts':fronts,'read_map_sha256':hashlib.sha256(mapfile.read_bytes()).hexdigest(),'adjacent_manifest_sha256':hashlib.sha256((P/'audits/return_ne_adjacent_complete_manifest.json').read_bytes()).hexdigest()}
(P/'audits/fixed_core_finite_region.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))

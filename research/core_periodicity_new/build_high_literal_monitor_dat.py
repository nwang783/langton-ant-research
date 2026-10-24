"""Emit finite forbidden monitor plus high/low control classes for cube pilot.
CLI BAND_MODEL.json MONITOR.json OUTPUT.mon. The monitor is reset at low ports.
"""
from pathlib import Path
import sys,json
src,mp,out=map(Path,sys.argv[1:4]);B=json.loads(src.read_text());J=json.loads(Path(B['source_file']).read_text());M=json.loads(mp.read_text());ns=len(M['states']);assert ns<=64 and M['initial_state']==0
classes=[int(J['positions'][old][0]in['near','far'])for old,b in B['positions']]
with out.open('w')as f:
 f.write(f'{len(classes)} {ns} {M["initial_state"]}\n')
 f.write(' '.join(map(str,classes))+'\n')
 for row in M['transitions']:f.write(' '.join(map(str,row))+'\n')
print(dict(positions=len(classes),states=ns))

#!/usr/bin/env python3
"""Literal affine signatures of the retained22 genuinely fresh one-black anchors."""
from pathlib import Path
import runpy,json,re,ast
from collections import defaultdict,deque
ROOT=Path(__file__).parent
E=runpy.run_path(str(ROOT/'probe_pristine_channel_directions.py'))
base=E['base'];entry=E['entry'];eh=E['eh'];rows=E['rows'];heads=E['heads'];step=E['step'];rot=E['rot'];d=E['d'];out=[]
for num,(head,row)in enumerate(zip(heads,rows)):
 n=len(row);t=row[-1];obs=(head[0]+n*d[0],head[1]+n*d[1]);B=base|{obs};p=entry;h=eh
 for _ in range(t):p,h,ch=step(B,p,h)
 k=(h-eh)%4
 if k not in[1,3]:continue
 b=(p[0]-entry[0],p[1]-entry[1]);out.append({'id':num,'head_relative':[head[0]-entry[0],head[1]-entry[1]],'depth':n,'anchor':t,'rotation':k,'displacement':list(b),'pose':[list(p),h],'obstacle':list(obs),'b_residue':[b[0]-b[1],b[0]%2]})
# Compose two fresh corners with same rotation: output is opposite orientation.
pairs=[]
for a in out:
 for b in out:
  if a['rotation']!=b['rotation']:continue
  rb=rot(tuple(b['displacement']),a['rotation']);v=(a['displacement'][0]+rb[0],a['displacement'][1]+rb[1]);pairs.append({'ids':[a['id'],b['id']],'rotation':a['rotation'],'displacement':list(v),'target_residue':[(v[0]-v[1])%4,v[0]%2]})
res={'scope':'Literal retained stable anchors only; each obstacle is a first-read fresh addition. Affine composition is kinematics, NOT a combined whole-field pair theorem.','entry':list(entry),'heading':eh,'templates':out,'two_corner_residues':sorted({tuple(p['target_residue'])for p in pairs}),'pairs':pairs}
(ROOT/'fresh_quarter_anchor_signatures.json').write_text(json.dumps(res,indent=2)+'\n');print('FRESH QUARTERS',len(out),'TWO_CORNER_RESIDUES',res['two_corner_residues'])
for t in out:print(t)

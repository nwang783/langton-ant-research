from pathlib import Path
import importlib.util,json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent

def load(n,p):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=load('l',R/'word_stabilization/check_foreign_return_interfaces.py');o=load('o',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS

def after(w,p=(0,0,0)):
 x,y,h=p
 for c in w:h=(h+(1 if c=='R'else-1))%4;dx,dy=l.DIRS[h];x+=dx;y+=dy
 return x,y,h
T='DDDDCVCVCDV';p=(0,0,0);poses=[]
for a in T:poses.append(dict(atom=a,pose=p));p=after(W[a],p)
assert tuple(poses[-1]['pose'])==(0,1,1)and tuple(poses[1]['pose'])==(1,1,0)
rows=[]
for prev in['','U']:
 for A in'FQB':
  word=prev+A+T;raw=''.join(W[a]for a in word);t=l.trace(raw+l.M);assert not t['feasible']and t['turn']=='R'
  forestart=len(W['U'])if prev else 0;betaR=forestart+len(W[A])-2;lastVstart=len(raw)-len(W['V']);assert t['previous_read']==betaR and t['conflict_read']==lastVstart+7
  rows.append(dict(prescribed_word=word,actual_FOREIGN_beta_R_tick0=betaR,actual_FOREIGN_beta_R_read1=betaR+1,conflict=t,intended_final_V_start_tick0=lastVstart,uncompleted_final_V_owner=o.describe('V',7),no_intervening_read_of_same_R_born_beta=True,scope='Literal failure, not a complete control. Planned ordinary suffix is the shifted signed bud-sharpness word whose final formal V crosses its second plainD. No simplicity of added preFORE U/F/Q/B prefix is asserted; finalV does not complete.'))
out=dict(status='AUTHOR_EXACT_PRESCRIBED_NEGATIVE_REGRESSION_NOT_INDEPENDENTLY_REVIEWED',motivation='Lift the signed three-C bud-sharpness control one D to the right so its intended final ordinary V targets the SECOND postforeign D rather than b1. Three foreign types, with and without one actual U before them, are the complete prescribed family; no prefix/depth scan.',formal_ordinary_suffix=T,all_formal_ordinary_atom_poses=poses,all6_literal_failures=rows,not_claimed=['No completed finalV or full word.','No global simplicity of the added earlier prefix.','No later-source first-contact theorem or arbitrary-tail simplicity.'])
p=H/'shifted_beta_failures.json';p.write_text(json.dumps(out,indent=2)+'\n');m={'status':out['status'],'files':{q.name:hashlib.sha256(q.read_bytes()).hexdigest()for q in[Path(__file__),p]}};q=H/'manifest.json';q.write_text(json.dumps(m,indent=2)+'\n');print(hashlib.sha256(q.read_bytes()).hexdigest())

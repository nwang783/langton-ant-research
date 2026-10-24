"""Independent chronological equal-cell elimination without spatial coset grouping."""
from pathlib import Path
import sys,json,hashlib
ROOT=Path('/workspace/shared/langton');sys.path.insert(0,str(ROOT/'computability/unit_inductive_certificates'))
from presburger_read_set_solver import Context
ctx=Context(max_operations=100000000)
def trace(w,h):
 z=0j;events=[]
 for c in w:events.append((z,c));h*= -1j if c=='R'else 1j;z+=h
 return z,h,events
def form(a,b,c,index):return f'({a}*r+{b}*{index}+{c})'
def family(phase,j,z,c,a,b,q,v):
 x,y=int(z.real),int(z.imag);qx,qy=int(q.real),int(q.imag)
 if phase=='U':return {'x':(0,qx,x),'y':(0,qy,y),'t':(0,a,j),'dom':'0<=I<r','turn':c}
 if phase=='V':return {'x':(qx,-qx,x+int(v.real)),'y':(qy,-qy,y+int(v.imag)),'t':(a,b,1+j),'dom':'0<=I<r','turn':c}
 return {'x':(qx,0,0),'y':(qy,0,0),'t':(a,0,0),'dom':'I=0','turn':c}
def spec(f,index):return {key:form(*f[key],index)for key in ['x','y','t']},f['dom'].replace('I',index)
records=json.loads((ROOT/'causal_reduction/unit_scale/probe_decorated_transport_cycles.json').read_text())['records'];out=[]
for rec in records:
 U,V,c=rec['U'],rec['V'],rec['parent'];a,b=len(U),len(V)
 q,h,ur=trace(U,1j);v,hh,cr=trace(c,1j);qv,hv,vr=trace(V,hh);assert h==1j and hv==hh and qv==-q
 fs=[family('U',j,z,t,a,b,q,v)for j,(z,t)in enumerate(ur)]+[family('C',0,0,c,a,b,q,v)]+[family('V',j,z,t,a,b,q,v)for j,(z,t)in enumerate(vr)]
 bad=ctx.set('[r]->{[]:false}').params();pairs=0
 for f in fs:
  ff,df=spec(f,'i')
  for g in fs:
   if f['turn']!=g['turn']:continue
   gg,dg=spec(g,'j')
   relation=ctx.set('[r]->{[i,j]:r>=0 and '+df+' and '+dg+f" and {ff['x']}={gg['x']} and {ff['y']}={gg['y']} and {ff['t']}<{gg['t']}"+'}')
   if relation.is_empty():continue
   pairs+=1
   for h in fs:
    hh,dh=spec(h,'k')
    inside=ctx.set('[r]->{[i,j]:exists(k:'+dh+f" and {hh['x']}={ff['x']} and {hh['y']}={ff['y']} and {ff['t']}<{hh['t']} and {hh['t']}<{gg['t']}"+')}')
    relation=relation.subtract(inside)
   bad=bad.union(relation.params())
 good=rec['source']=='R21' and rec['recursive_read']==14
 expected=ctx.set('[r]->{[]:'+('false'if good else'r>=2')+'}').params()
 assert bad.is_equal(expected),(rec['source'],rec['recursive_read'],str(bad))
 out.append({'source':rec['source'],'recursive_read':rec['recursive_read'],'bad_depths':str(bad.coalesce()),'potential_same_turn_pairs':pairs})
 print(json.dumps(out[-1]),flush=True)
res={'status':'PASS independent all-depth equal-coordinate chronology relations for nine hairpins','records':out,'method':'Separate occurrence indices and two coordinate equations, removing every intermediate-read existential. No author coset construction or implementation imported.','hashes':{'auditor':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'inventory':hashlib.sha256((ROOT/'causal_reduction/unit_scale/probe_decorated_transport_cycles.json').read_bytes()).hexdigest()}}
(ROOT/'audits/hairpin_presburger_independent.json').write_text(json.dumps(res,indent=2)+'\n')

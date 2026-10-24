"""Targeted actual-epoch checks; analytic path-turning dependency is separate."""
from check_renewal_archive import *
import math
OUT=Path(__file__).parent

def check(name,B0,p,h,word):
 B=set(B0);m=len(B);k=wwhich(p,h);r=0;E=0;M=m;n=0;ordinary_gain=0;ws=[cursors(p,h)[1]];last_direction=None;interior=0;first_gain=None;epochs=[]
 for t,c in enumerate(word,1):
  assert ('L'if p in B else'R')==c
  ex=False
  if c=='R':r+=1
  else:ex=r>=3 or connected(B-{p},k,*endpoints(p,k))
  oldw=cursors(p,h)[1];p,h=step(B,p,h)
  if c=='L':
   if ex:
    assert ordinary_gain<=8*math.sqrt(M)+3
    assert len(B)<=M+8*math.sqrt(M)+6
    assert len(B)<=(math.sqrt(M)+4)**2+1e-9
    epochs.append({'entry_mass':M,'ordinary_blocks':n,'ordinary_gain':ordinary_gain,'interior_turn':interior,'first_gain':first_gain,'exit_mass':len(B)})
    E+=1;M=len(B);n=ordinary_gain=interior=0;first_gain=None;last_direction=None;ws=[cursors(p,h)[1]]
   else:
    neww=cursors(p,h)[1];assert neww not in ws;ws.append(neww);n+=1;ordinary_gain+=r-1
    direction=(neww[0]-oldw[0],neww[1]-oldw[1])
    if last_direction is None:first_gain=r-1
    else:
     cross=last_direction[0]*direction[1]-last_direction[1]*direction[0]
     dot=last_direction[0]*direction[0]+last_direction[1]*direction[1]
     turn=0 if dot>0 else (-1 if cross>0 else 1)
     assert turn==r-1
     interior+=turn
    last_direction=direction
    assert ordinary_gain==interior+first_gain
    assert abs(interior)<=8*math.sqrt(n)+2
    assert n<=M
   r=0
  assert M<=(math.sqrt(m)+4*E)**2+1e-9
  assert t<=3*(E+1)*m+12*math.sqrt(m)*E*(E+1)+8*E*(E+1)*(2*E+1)+5*E+4+1e-9
  assert t<=16*(E+math.sqrt(m)/4+1)**3+1e-9
 return {'name':name,'T':len(word),'m':m,'E':E,'epochs':epochs,'final_mass':len(B)}

if __name__=='__main__':
 S=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())
 runs=[check('standard104_three_periods',{tuple(q)for q in S['seed']},(0,0),S['heading'],S['word']*3)]
 for r in [1,3,30,100]:runs.append(check('single_cycle_rod_'+str(r),cycle_rod(r),(0,0),1,'LRRL'*r))
 B=set();p=(0,0);h=0;w=''
 for t in range(1000):w+='L'if p in B else'R';p,h=step(B,p,h)
 runs.append(check('blank1000',set(),(0,0),0,w))
 out={'status':'targeted arbitrary-cut, turn sign, mass recurrence and cubic-prefix controls PASS','runs':runs}
 (OUT/'cubic_renewal_controls.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':out['status'],'runs':[{k:v for k,v in d.items()if k!='epochs'}for d in runs]},indent=2))

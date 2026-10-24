"""Literal finite-word controls for the proposed arbitrary D/C/V-factor trim."""
from pathlib import Path
import json, hashlib
P=Path(__file__).resolve().parent
D='LLLLRLRRRR';C='LLLLRLRRRRLRRRR';V='LLLLRLRRRRLRRLRRRR';M=D+'L'
def trace(word):
 x=y=h=0;last={};dirs=[(0,1),(1,0),(0,-1),(-1,0)]
 for i,ch in enumerate(word):
  if (x,y) in last and last[x,y][1]==ch:
   return {'feasible':False,'conflict_read':i,'previous_read':last[x,y][0],'cell':[x,y]}
  last[x,y]=(i,ch);h=(h+(1 if ch=='R' else -1))%4;dx,dy=dirs[h];x+=dx;y+=dy
 return {'feasible':True,'endpoint':[x,y],'heading':h,'endpoint_last_read':last.get((x,y))}
words={'C5':C*5,'D_endpoint':D,'C4_M11':C*4+M,'VCCC_M11':V+C*3+M,
       'DCC_D':D+C*2+D,'DCC_D_L':D+C*2+D+'L','DCC_D_LL':D+C*2+D+'LL',
       'DCC_V':D+C*2+V,'DCC_D_C':D+C*2+D+C,'retained_DC_actual_marker':D+C+M}
out={k:trace(w)for k,w in words.items()}
assert out['DCC_D']['feasible'] and out['DCC_D_L']['feasible']
assert not out['DCC_D_LL']['feasible'] and out['DCC_D_LL']['conflict_read']==51
assert not out['DCC_V']['feasible'] and not out['DCC_D_C']['feasible']
assert out['retained_DC_actual_marker']['feasible']
# Of all possible removed terminal packets, only a standalone D leaves this exception.
out['DCC_terminal_packet_cases']={a+'C'*k:trace(D+C*2+w+C*k)for a,w in [('D',D),('V',V)]for k in range(5)}
assert [k for k,v in out['DCC_terminal_packet_cases'].items()if v['feasible']]==['D']
out.update(raw_lengths={'D':len(D),'C':len(C),'V':len(V)},trim_steps=193,entry_mass_extra=21,
 terminal_exception_steps=len(C)+len(D),
 status='Direct literal controls; corrected full trim argument awaits independent review',
 script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(P/'dcv_arbitrary_factor_trim_controls.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

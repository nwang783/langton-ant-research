"""Discovery only: recover affine word template, without extrapolation claims."""
import json,sys
from pathlib import Path
SRC=Path('/workspace/shared/langton/continuation_2026-10-22/ant_continuation/wake_clock')
sys.path[:0]=[str(SRC),str(SRC.parent)]
from four_scatterer_loop import build
from ant_exact import step,PHASES,certify_period

def trace(L):
 B,*_=build(L);p=(0,0);h=0
 t0=416*L+37740;t1=520*L+43111
 text=[];poses=[];blocks=[]
 for t in range(t1):
  if t>=t0:poses.append((p,h))
  p,h,c=step(B,p,h)
  if t>=t0:text.append(c)
 poses.append((p,h));w=''.join(text)
 assert w[-104:] in PHASES
 cert=certify_period(B,p,h,w[-104:])
 assert cert
 return w,poses,cert,len(B)

def main():
 rows={}
 for L in [128,129,130,192,256]:
  w,p,c,m=trace(L);rows[L]=(w,p)
  print(L,len(w),p[-1],c,m,flush=True)
 a,ap=rows[128];b,bp=rows[129]
 k=0
 while a[k]==b[k]:k+=1
 j=0
 while a[-j-1]==b[-j-1]:j+=1
 # Earliest legal insertion: a[:s]+standard period+a[s:] == b.
 matches=[]
 for s in range(max(0,k-104),k+1):
  if b[s:s+104] in PHASES and a[:s]+b[s:s+104]+a[s:]==b:matches.append(s)
 assert matches
 start=matches[0]
 period=b[start:start+104]
 # Maximal standard run in the 128 suffix aligned with this start.
 lo=start
 while lo>=104 and a[lo-104:lo]==period:lo-=104
 hi=start
 while a[hi:hi+104]==period:hi+=104
 count=(hi-lo)//104
 before=a[:lo];after=a[hi:]
 for L,(w,p) in rows.items():assert w==before+period*(count+L-128)+after
 out=dict(status='template discovery; NOT an all-parameter proof',prefix_word=before,period_word=period,suffix_word=after,period_count_constant=count-128,prefix_length=len(before),suffix_length=len(after),period_start_pose=ap[lo],period_end_pose_128=ap[hi],final_pose_128=ap[-1],L128_length=len(a),first_difference_between_128_129=k,common_suffix=j)
 Path(__file__).with_name('completion_template.json').write_text(json.dumps(out,indent=2)+'\n')
 print({k:v for k,v in out.items() if not k.endswith('word')})
if __name__=='__main__':main()

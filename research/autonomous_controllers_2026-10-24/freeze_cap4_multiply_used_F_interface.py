#!/usr/bin/env python3
"""Exact partial cap4 interface. Not a complete WHITE front or board control."""
import sys,json,re,hashlib
from pathlib import Path
from collections import Counter
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'periodic_classification_new'))
from probe_one_a_local_constraints import mkconfig,mkcontext,mksolver,inc,parse,solve,getmodel,modelstr
from synthesize_axis_compact_clock import values
from check_extremal_read_coupling import D,quotient,cycles
H=[tuple('NESW'.index(x)for x in w)for w in ['W','','N','SS','WE','WWE','SNN','SSNS','EEWE','WWEW']]
PTS=[(r,t-r)for t in range(-1,4)for r in(0,1)];IX={p:i for i,p in enumerate(PTS)};DRIFT=(2,-2);P=200

def main():
 nodes=[(i,j)for i,h in enumerate(H)for j in range(len(h))];out={};incoming={};ports=[];edges=[]
 for i,p in enumerate(PTS):
  for h in range(4):
   src=[j for j,x in enumerate(H[i])if(x+(1 if j%2==0 else-1))%4==h]
   if not src:continue
   q,k=quotient((p[0]+D[h][0],p[1]+D[h][1]),DRIFT)
   if q not in IX:
    ports +=[{'direction':'out','cell':i,'rank':j,'heading':h,'outside_class':q,'voltage':k}for j in src];continue
   ii=IX[q];dst=[j for j,x in enumerate(H[ii])if x==h];assert len(src)==len(dst)
   for ordinal,(u,v)in enumerate(zip(src,dst)):
    out[i,u]=((ii,v),k);incoming[ii,v]=((i,u),k);edges.append({'source':[i,u],'target':[ii,v],'voltage':k,'physical_ordinal':ordinal})
 for i,j in nodes:
  if(i,j)not in incoming:
   h=H[i][j];q,k=quotient((PTS[i][0]-D[h][0],PTS[i][1]-D[h][1]),DRIFT);assert q not in IX
   ports.append({'direction':'in','cell':i,'rank':j,'heading':h,'outside_class':q,'voltage':k})
 lines=['(set-logic QF_LIA)','(set-option :timeout 10000)']
 for i,j in nodes:
  lines.append(f'(declare-fun t{i}_{j} () Int)');res=(2*PTS[i][0]-sum(PTS[i])%2+1)%4;lines.append(f'(assert (= (mod t{i}_{j} 4) {res}))')
  if j:lines.append(f'(assert (>= t{i}_{j} (+ t{i}_{j-1} 4)))')
 lines += ['(assert (= t0_0 0))','(assert (distinct '+' '.join(f'(mod t{i}_{j} {P})'for i,j in nodes)+'))']
 for e in edges:
  i,j=e['source'];ii,jj=e['target'];k=e['voltage'];lines.append(f'(assert (= (+ t{ii}_{jj} {k*P}) (+ t{i}_{j} 1)))')
 text='\n'.join(lines)+'\n';base=Path(__file__).with_name('cap4_multiply_used_F_open_interface');base.with_suffix('.smt2').write_text(text)
 ctx=mkcontext(mkconfig());s=mksolver(ctx);inc(ctx,s);parse(ctx,s,text.encode());ans=solve(ctx,s);assert ans==1,ans
 mt=modelstr(ctx,getmodel(ctx,s)).decode();base.with_suffix('.model').write_text(mt);v=values(mt);clocks={f'{i}:{j}':int(v[f't{i}_{j}'])for i,j in nodes}
 assert len({t%P for t in clocks.values()})==len(nodes)
 for i,h in enumerate(H):
  for j in range(len(h)-1):assert clocks[f'{i}:{j+1}']>=clocks[f'{i}:{j}']+4
 for e in edges:
  i,j=e['source'];ii,jj=e['target'];assert clocks[f'{i}:{j}']+1==clocks[f'{ii}:{jj}']+e['voltage']*P
 F={};E={};uses={}
 for i,h in enumerate(H):
  if not h or(i,0)not in out:continue
  (ii,j),k=out[i,0];F[PTS[i]]=(PTS[ii],k)
  if j==len(H[ii])-1:E[PTS[i]]=(PTS[ii],k)
  hh=(h[0]+1)%4;uses[PTS[i]]=sum((x+(1 if j%2==0 else-1))%4==hh for j,x in enumerate(h))
 fc=cycles(F);assert len(fc)==1 and fc[0]['winding']==-1
 fc[0]['first_port_use_counts']=[uses[p]for p in fc[0]['cells']];assert sorted(fc[0]['first_port_use_counts'])==[1,1,2,2]
 result={'scope':__doc__,'full_drift':DRIFT,'named_classes':PTS,'complete_named_heading_words':[''.join('NESW'[x]for x in h)for h in H],'event_count':len(nodes),'maximum_named_multiplicity':max(map(len,H)),'clock_period':P,'representative_clocks':clocks,'distinct_clock_phases':len(nodes),'all_internal_ordinal_edges':edges,'all_open_ports':ports,'first_R_cycles':fc,'E_cycles':cycles(E),'limitations':'Only a complete finite LIST of named histories with exact internal ordinal edges and clocks. Upper port completions, remaining176 event phases, outside WHITE histories, a shared physical board and a single full event cycle are NOT supplied. Not a complete front or autonomous controller.'}
 base.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items()if k not in('representative_clocks','all_internal_ordinal_edges','all_open_ports','named_classes')},indent=2))
if __name__=='__main__':main()

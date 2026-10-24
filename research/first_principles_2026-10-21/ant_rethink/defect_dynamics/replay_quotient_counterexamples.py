"""Independent direct replay of the failed standard-subtracted cap bound.

Uses no highway detector, optimization, tail certificate, or search pruning.
Headings are N,E,S,W. A processed white cell turns right; black turns left.
"""
import hashlib
import json
from pathlib import Path

DIR=((0,1),(1,0),(0,-1),(-1,0))
ROOT=Path(__file__).resolve().parent


def run(initial,pose,steps):
    b=set(initial);x,y,h=pose
    counts={r:0 for r in range(-3,1)}
    delta={r:0 for r in range(-3,1)}
    top_times=[];A_times={};word=[];maxlevel=x+y;E_B=K_C=0
    for t in range(steps):
        level=x+y;black=(x,y) in b
        if level in counts:
            counts[level]+=1;delta[level]+= -1 if black else 1
        if level==0:top_times.append((t,x))
        if level==-1:A_times.setdefault(x,[]).append(t)
        if level==-2 and not black and h==3:E_B+=1
        if level==-3 and black and h==2:K_C+=1
        word.append('L' if black else 'R')
        if black:b.remove((x,y))
        else:b.add((x,y))
        h=(h+(3 if black else 1))%4
        x+=DIR[h][0];y+=DIR[h][1]
        maxlevel=max(maxlevel,x+y)
    M=counts[0];A=delta[-1];D=E_B-M;Q=2*M-A;Z=K_C+2*D-Q
    assert pose[0]+pose[1]<=-4 and x+y<=-4 and maxlevel==0
    assert all(sum(p)<=-2 for p in initial)
    assert len(set(r for t,r in top_times))==M
    assert counts[-1]==4*M-A
    assert D>=0 and Z>=0
    assert counts[-2]==8*M-4*A+delta[-2]-4*D
    assert counts[-3]==12*M-8*A+4*delta[-2]-delta[-3]-8*D-4*Z
    top=sorted(r for t,r in top_times)
    c=sum(i==0 or top[i]>top[i-1]+1 for i in range(len(top)))
    E=sum(len(ts)%2==0 for ts in A_times.values())
    phi=M-2*A
    assert len(A_times)==M+c and phi==2*E-M-2*c
    out={'initial_black':sorted(initial),'initial_pose':pose,'steps':steps,
         'heading_order':'N,E,S,W','end_pose':(x,y,h),'max_level':maxlevel,
         'M':M,'N_A':counts[-1],'Delta_A':A,'Phi':phi,'initial_mass':len(initial),
         'top_runs':c,'even_A_cells':E,'top_visit_order':top_times,
         'A_visit_times':A_times,'D':D,'K_C':K_C,'Z':Z,
         'row_counts':counts,'row_mass_changes':delta,
         'final_T':sorted(p for p in b if sum(p)==0),
         'final_A':sorted(p for p in b if sum(p)==-1),
         'turn_word_sha256':hashlib.sha256(''.join(word).encode()).hexdigest()}
    return out,''.join(word)


if __name__=='__main__':
    first,w=run({(2,-29)},(0,-13,2),7849)
    old=json.loads((ROOT/'quotient_charge_counterexample.json').read_text())
    assert old['word']==w and first['Phi']==4 and first['M']==8 and first['Delta_A']==2
    assert first['Phi']>2*first['initial_mass']+1
    second,w=run({(-5,-111)},(0,-122,1),72218)
    assert second['Phi']==4 and second['M']==4 and second['Delta_A']==0
    assert second['top_runs']==1
    out={'status':'two_exact_counterexamples_replayed','cases':[first,second]}
    (ROOT/'quotient_counterexample_replays.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

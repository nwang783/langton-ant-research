from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];B=ROOT/'nonlinear_global_budget_2026-10-23';H=json.loads((ROOT/'deliverables/constant_184_capturing_family/family_data.json').read_text())['standard_word'];V=(1j,1,-1j,-1)
factors={''.join(H[(i+j)%104]for j in range(10))for i in range(104)};S='RLLR';assert all(''.join(S[(s+j)%4]for j in range(10))not in factors for s in range(4))
def run(board,p,h,w):
 b=set(board)
 for c in w:assert(p in b)==(c=='L');b.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=V[h]
 return b,p,h
def inv10(board,p,h):
 b=set(board);letters=[]
 for _ in range(10):
  p-=V[h];c='R'if p in b else'L';b.symmetric_difference_update({p});h=(h-(1 if c=='R'else-1))%4;letters.append(c)
 return ''.join(letters[::-1])
rows=[]
for n in(3,4,5,10,31):
 br={1+y*1j for y in range(2*n)};bl={y*1j for y in range(2*n)}
 for initial,p,h,target,end in((br,0j,0,bl,2*n*1j),(bl,1+(2*n-1)*1j,2,br,1-1j)):
  assert(int(p.real+p.imag)+h)%2==0
  b,ep,eh=run(initial,p,h,S*n);assert b==target and ep==end and eh==h
  hist=inv10(initial,p,h);stream=hist+S*n;events=[t for t in range(4*n)if stream[t:t+10]not in factors and stream[t+1:t+11]not in factors]
  assert events[-1]==4*n-1 and len(events)>=4*n-10;rows.append((n,h,len(events),events[-1]))
# Stronger infinite projected descent retaining N heading and a fixed sector.
for n in(3,5,11):
 for x in range(-6,7):
  row=lambda a:{a+y*1j for y in range(2*n)}
  b,ep,eh=run(row(x),x-1+0j,0,'RLLR'*n);assert b==row(x-1)and ep==x-1+2*n*1j and eh==0
  b,ep,eh=run(row(x-1),x-1+0j,0,'LRRL'*n);assert b==row(x-2)and ep==x-1+2*n*1j and eh==0
  assert (x-1)%2==(x-3)%2
  stream=inv10(row(x-1),x-1+0j,0)+'LRRL'*n
  assert stream[-11:-1]not in factors and stream[-10:]not in factors
out=dict(status='PASS genuine opposed whole-board S-row transformations, same sector and true-history endpoint K',note_sha256=hashlib.sha256((B/'board_only_renewal_rank_obstruction.md').read_bytes()).hexdigest(),literal_controls=rows,all_n_proof='S at(0,0,N) reads0R,1L,1+i L,i R and ends2i,N; translations by2i concatenate disjoint four-cell strips. Proper180 rotation gives exact opposite whole-board map. All four periodic10 factors are bad; last read isK for n>=3.',scope='Excludes universal strictly decreasing natural-valued exact-K-renewal ranks using current board, heading AND conserved sector while forgetting cursor position. Opposed S factors give board-only cycle; alternating S/T gives infinite same-heading/sector projected descent. Different ant poses do not concatenate into a physical cycle. Full-state ranks and initial spatial upper bounds remain open.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)

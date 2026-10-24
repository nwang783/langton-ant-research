import json
D=((0,1),(1,0),(0,-1),(-1,0))
def G(a,n):
 if not n:return a*4
 b='L' if a=='R' else 'R';return a*2+G(b,n-1)+a*2
out=[]
for n in range(9):
 w=G('R',n);x=y=h=0;history={};initial={};token={};active='entry';reads=[]
 for t,c in enumerate(w):
  q=(x,y)
  if q not in history:
   initial[q]=c=='L'
   if c=='L':token[q]='initial'+str(q)
  else:assert history[q]!=c
  history[q]=c
  if c=='R':token[q]=active
  else:active=token.pop(q)
  reads.append(dict(t=t,cell=q,turn=c,active=active))
  h=(h+(1 if c=='R' else -1))%4;dx,dy=D[h];x+=dx;y+=dy
 rec=dict(depth=n,word=w,initial_black=[q for q,b in initial.items() if b],final_tokens=[[q,s] for q,s in sorted(token.items())],entry_descendants=sum(s=='entry' for s in token.values()),surviving_labels=len(set(token.values())),active_final=active)
 out.append(rec);print(n,'input',sum(initial.values()),'output',len(token),'entry descendants',rec['entry_descendants'],'labels',rec['surviving_labels'],'active final',active)
json.dump(out,open('/workspace/shared/langton/causal_reduction/g_ladder_labels.json','w'),indent=2)

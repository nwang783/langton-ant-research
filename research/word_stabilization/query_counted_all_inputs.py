from pathlib import Path
import sys,json,hashlib,collections
R=Path('/workspace/shared/langton');sys.path.insert(0,str(R/'audits'))
from check_dcuv_producer_model_independent import geometry,rotation,xy,walk,raws,ordinary,protected
D=R/'core_periodicity_new/chronology_dcuv/recurrent8_counted';ids=[0,1,4,5,6,7,8,9];mp={v:i for i,v in enumerate(ids)};cc=[0,1,0,1,2,0,1,2]
C={tuple(map(int,l.split()[:8]))for l in(D/'closure.tsv').read_text().splitlines()}
def kin(a,p,h,k):
 rem=k-cc[mp[a]]
 if rem<0:return False
 if rem>=2:return True
 end,dh,_,_=walk(raws[a]);z=-.5-.5j;delta=rotation(p+rotation(z,h)-end-rotation(z,dh),-dh);x,y=xy(delta)
 if rem==0:return x>=0 and y>=x and(x+y)%2==0 and(x!=0 or y%4==0)
 x-=1;y-=1;return y>=0 and x<=y and(x+y)%2==0 and(y!=0 or x%4==0)
J={};all_rows=[]
for b in ids:
 for z in geometry[b]['inputs']:
  rows=[]
  for a in ids:
   for q in geometry[a]['outputs']:
    for h in range(4):
     p=q-rotation(z,h);r=(a,b,*xy(p),h,*xy(q))
     if(sum(xy(p))+h)%2 or r[:5]in ordinary or r in protected:continue
     statuses=[]
     for k in range(4):
      status='heading' if k<cc[mp[a]] or (h+k)%4 else 'kinematic' if not kin(a,p,h,k) else 'signed_clause' if (mp[a],mp[b],*r[2:],k)in C else 'OPEN'
      statuses.append(status)
     rows.append(dict(tuple=r,statuses=statuses));all_rows.append(rows[-1])
  J[f'{b}:{xy(z)}']={'admitted_alignments':len(rows),'open_counts':[sum(x['statuses'][k]=='OPEN'for x in rows)for k in range(4)],'rows':rows}
W=json.loads((D.parent/'observed_transfers_fast_depth11.json').read_text())['witnesses'];controls=[]
for w in W:
 a,b,*_=w['tuple']
 if b not in[4,5,6]:continue
 age=sum(raws[t].count('C')for t in []) # Use packet names, not raw turns.
 age=sum(w['packet_names'][i].count('C')for i in range(w['source_index'],w['target_index']))
 controls.append({'tuple':w['tuple'],'input_slot':w['target_input_slot'],'C_age':age,'word':w['packet_ids'],'source_index':w['source_index'],'target_index':w['target_index']})
O={'status':'Exact membership queries against signed counted relation; unresolved rows are not possible transfers. Physical controls separately give realized ages.','queries':J,'observed_controls':controls,'hashes':{str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in[D/'closure.tsv',D.parent/'observed_transfers_fast_depth11.json',Path(__file__)]}}
p=D.parent/'counted_all_input_queries.json';p.write_text(json.dumps(O,indent=2)+'\n')
for k,v in J.items():print(k,v['admitted_alignments'],v['open_counts'])
print('observed minimum',min(x['C_age']for x in controls));print([x for x in controls if x['C_age']==min(y['C_age']for y in controls)])

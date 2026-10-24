"""Build the research report using Pandoc native equations and python-docx styles."""
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR','/tmp/ant_report/matplotlib')
import sys,subprocess
from docx import Document
from docx.shared import Inches,Pt,RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.enum.table import WD_TABLE_ALIGNMENT,WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
SOURCE=HERE/'report_body.md'
OUT=ROOT/'Langton_Ant_Research_Update_2026-10-21.docx'

# An exact illustration, generated directly from the literal ant dynamics.
sys.path.insert(0,str(HERE.parent))
from ant_exact import step
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
def hull(P):
 P=sorted(set(P));lower=[];upper=[]
 for q in P:
  while len(lower)>=2 and cross(lower[-2],lower[-1],q)<=0:lower.pop()
  lower.append(q)
 for q in reversed(P):
  while len(upper)>=2 and cross(upper[-2],upper[-1],q)<=0:upper.pop()
  upper.append(q)
 return lower[:-1]+upper[:-1]
B=set();p=(0,0);h=0;P=[p]
for t in range(40):p,h,c=step(B,p,h);P.append(p)
assert hull(P)==hull(list(B)+[P[0],P[-1]])
fig,ax=plt.subplots(figsize=(5.7,3.45))
ax.add_patch(Polygon(hull(P),closed=True,facecolor='#E7ECEF',edgecolor='#7C8790',linewidth=1.3,zorder=1))
ax.plot([q[0] for q in P],[q[1] for q in P],color='#376B89',linewidth=1.2,zorder=2,label='Path through 40 updates')
ax.scatter([q[0] for q in B],[q[1] for q in B],color='#151515',s=29,zorder=3,label='Cells whose color changed')
ax.scatter([P[0][0],P[-1][0]],[P[0][1],P[-1][1]],marker='s',s=52,color='#B35F19',zorder=4,label='Start and end positions')
ax.annotate('start',P[0],xytext=(8,8),textcoords='offset points',fontsize=9)
ax.annotate('end',P[-1],xytext=(8,-13),textcoords='offset points',fontsize=9)
ax.set_aspect('equal');ax.set_xlim(-3.7,1.7);ax.set_ylim(-4.7,1.7)
ax.set_xticks(range(-3,2));ax.set_yticks(range(-4,2));ax.grid(color='#D5DADF',linewidth=.5,zorder=0)
for s in ax.spines.values():s.set_visible(False)
ax.tick_params(labelsize=8,length=0);ax.set_xlabel('x',fontsize=9);ax.set_ylabel('y',fontsize=9,rotation=0)
ax.legend(loc='center left',bbox_to_anchor=(1.04,.5),frameon=False,fontsize=8.5,handlelength=2)
fig.subplots_adjust(left=.09,right=.51,bottom=.12,top=.98)
fig.savefig(HERE/'path_hull.png',dpi=220,bbox_inches='tight',facecolor='white');plt.close(fig)

text=SOURCE.read_text().replace('\n date:','\ndate:')
needle='This extends the corner argument used in Etse\'s no-repeated-coloring result [1].'
if 'path_hull.png' not in text:
 text=text.replace(needle,'![The first 40 updates from the blank grid. The shaded path hull is fixed by the changed cells and the two endpoint positions.](path_hull.png){width=5.5in}\n\n'+needle)
SOURCE.write_text(text)
subprocess.run(['pandoc',str(SOURCE),'-o',str(OUT),'--standalone','--resource-path',str(HERE)],check=True)
doc=Document(OUT)
sec=doc.sections[0]
sec.page_width=Inches(8.5);sec.page_height=Inches(11)
sec.top_margin=Inches(.72);sec.bottom_margin=Inches(.72)
sec.left_margin=Inches(.8);sec.right_margin=Inches(.8)
sec.header_distance=Inches(.25);sec.footer_distance=Inches(.3)
for style in doc.styles:
 if style.type==1:
  style.font.name='Calibri';style.font.size=Pt(11)
  style.font.color.rgb=RGBColor(0,0,0)
  pf=style.paragraph_format
  pf.line_spacing=1.05;pf.space_after=Pt(6)
  if style.name.startswith('Heading'):
   style.font.name='Calibri';style.font.bold=True
   pf.keep_with_next=True;pf.space_before=Pt(16);pf.space_after=Pt(7)
for name,size in [('Title',25),('Subtitle',13),('Heading 1',15),('Heading 2',12.5)]:
 if name in doc.styles:
  s=doc.styles[name];s.font.size=Pt(size);s.font.color.rgb=RGBColor(0,0,0)
  if name=='Title':s.font.bold=True
  if name=='Subtitle':s.paragraph_format.space_after=Pt(9)
for name in ['Verbatim Char','Source Code']:
 if name in doc.styles:doc.styles[name].font.name='Consolas';doc.styles[name].font.size=Pt(9)
paragraphs=doc.paragraphs
for idx,p in enumerate(paragraphs):
 if idx+1<len(paragraphs) and paragraphs[idx+1]._p.xpath('.//m:oMathPara'):
  p.paragraph_format.keep_with_next=True
 if p.style.name in ['Title','Subtitle','Date']:
  p.alignment=WD_ALIGN_PARAGRAPH.LEFT
 if p.style.name=='Image Caption':
  p.style=doc.styles['Caption'];p.paragraph_format.space_after=Pt(9)
  for r in p.runs:r.font.size=Pt(9.5)
 # Keep all display equations intact without large automatic gaps.
 if p._p.xpath('.//m:oMathPara') or p._p.xpath('.//m:oMath'):
  p.paragraph_format.keep_together=True
 for r in p.runs:
  if r.font.color and r.font.color.type is not None and p.style.name.startswith(('Title','Subtitle','Heading')):
   r.font.color.rgb=RGBColor(0,0,0)
# Explicit widths, borders, padding, repeat headers; no fixed row heights.
for ti,table in enumerate(doc.tables):
 table.alignment=WD_TABLE_ALIGNMENT.CENTER;table.autofit=False
 widths=[4.9,2.0] if ti==0 else [2.25,4.65]
 for j,column in enumerate(table.columns):
  column.width=Inches(widths[j])
 for row in table.rows:
  for j,cell in enumerate(row.cells):
   cell.width=Inches(widths[j]);cell.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
   tcPr=cell._tc.get_or_add_tcPr()
   margins=OxmlElement('w:tcMar')
   for side,val in [('top','80'),('bottom','80'),('left','100'),('right','100')]:
    el=OxmlElement('w:'+side);el.set(qn('w:w'),val);el.set(qn('w:type'),'dxa');margins.append(el)
   tcPr.append(margins)
   borders=OxmlElement('w:tcBorders')
   for side in ['top','left','bottom','right']:
    e=OxmlElement('w:'+side);e.set(qn('w:val'),'single');e.set(qn('w:sz'),'4');e.set(qn('w:color'),'D9D9D9');borders.append(e)
   tcPr.append(borders)
   for p in cell.paragraphs:
    p.paragraph_format.space_after=Pt(0);p.paragraph_format.line_spacing=1.05
    p.alignment=WD_ALIGN_PARAGRAPH.RIGHT if ti==0 and j==1 else WD_ALIGN_PARAGRAPH.LEFT
    for r in p.runs:r.font.size=Pt(10)
 header=table.rows[0]
 trPr=header._tr.get_or_add_trPr();repeat=OxmlElement('w:tblHeader');trPr.append(repeat)
 for cell in header.cells:
  shd=OxmlElement('w:shd');shd.set(qn('w:fill'),'E5ECF1');cell._tc.get_or_add_tcPr().append(shd)
  for p in cell.paragraphs:
   for r in p.runs:r.font.bold=True;r.font.color.rgb=RGBColor(0,0,0)
 # Long filenames wrap at underscores and slashes in the evidence table.
 for row in table.rows:
  trPr=row._tr.get_or_add_trPr();cant=OxmlElement('w:cantSplit');trPr.append(cant)
# A multi-page research handoff benefits from page numbers.
p=sec.footer.paragraphs[0];p.alignment=WD_ALIGN_PARAGRAPH.RIGHT
r=p.add_run();r.font.size=Pt(9)
fld=OxmlElement('w:fldSimple');fld.set(qn('w:instr'),'PAGE')
fr=OxmlElement('w:r');ft=OxmlElement('w:t');ft.text='1';fr.append(ft);fld.append(fr);p._p.append(fld)
doc.core_properties.title='Langton Ant Highway Research Continuation'
doc.core_properties.subject='Analytic lemmas, exact finite certificates, and remaining proof obligations'
doc.core_properties.author='ChatGPT'
doc.core_properties.keywords='Langton ant; highway conjecture; finite seed; exact certificate'
doc.save(OUT)
print(OUT)
print('native_math_objects',sum(len(p._p.xpath('.//m:oMath')) for p in doc.paragraphs))

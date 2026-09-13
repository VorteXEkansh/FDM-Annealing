"""Build the complete stage manuscript from the maintained Markdown source."""
from pathlib import Path
import os
import re
import json
import hashlib
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Flowable

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output/pdf/Constrained-Annealing-2026-DRAFT.pdf'
FONT = Path(os.environ.get('RESEARCH_FONT_DIR', 'C:/Windows/Fonts'))
for name, file in [('Body','times.ttf'),('Body-Bold','timesbd.ttf'),('Body-Italic','timesi.ttf'),('Sans','arial.ttf'),('Sans-Bold','arialbd.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(FONT / file)))
pdfmetrics.registerFont(TTFont('MathSymbols', str(FONT/'seguisym.ttf')))
pdfmetrics.registerFontFamily('Body', normal='Body', bold='Body-Bold', italic='Body-Italic', boldItalic='Body-Bold')
pdfmetrics.registerFontFamily('Sans', normal='Sans', bold='Sans-Bold', italic='Sans', boldItalic='Sans-Bold')

ST = {
    'body': ParagraphStyle('body', fontName='Body', fontSize=11, leading=14, spaceAfter=7, alignment=TA_LEFT),
    'title': ParagraphStyle('title', fontName='Sans-Bold', fontSize=21, leading=26, spaceAfter=12, textColor=colors.HexColor('#193b4b')),
    'subtitle': ParagraphStyle('subtitle', fontName='Sans', fontSize=13, leading=18, spaceAfter=14, textColor=colors.HexColor('#24576b')),
    'heading': ParagraphStyle('heading', fontName='Sans-Bold', fontSize=12.5, leading=16, spaceBefore=9, spaceAfter=8, keepWithNext=True, textColor=colors.HexColor('#193b4b')),
    'equation': ParagraphStyle('equation', fontName='Body', fontSize=12, leading=21, alignment=TA_CENTER, spaceBefore=3, spaceAfter=12),
    'caption': ParagraphStyle('caption', fontName='Sans', fontSize=8.8, leading=12, spaceAfter=10),
    'cell': ParagraphStyle('cell', fontName='Sans', fontSize=9, leading=12, spaceAfter=0),
    'thead': ParagraphStyle('thead', fontName='Sans-Bold', fontSize=9, leading=12, textColor=colors.white),
}
ST['tablecaption'] = ParagraphStyle('tablecaption', parent=ST['caption'], keepWithNext=True)

def P(text, style):
    # Explicit fallback avoids silently rendered missing-glyph boxes.
    for char, replacement in {
        '₀':'<sub>0</sub>','₁':'<sub>1</sub>','₂':'<sub>2</sub>','₃':'<sub>3</sub>',
        '₄':'<sub>4</sub>','₅':'<sub>5</sub>','₆':'<sub>6</sub>','₇':'<sub>7</sub>',
        '₈':'<sub>8</sub>','₉':'<sub>9</sub>','ᵢ':'<sub>i</sub>','ⱼ':'<sub>j</sub>',
        '⁻':'<super>−</super>','¹':'<super>1</super>','²':'<super>2</super>','³':'<super>3</super>',
    }.items():
        text=text.replace(char,replacement)
    for char in '∇∈⊥':
        text=text.replace(char, f'<font name="MathSymbols">{char}</font>')
    paragraph=Paragraph(text,style)
    for frag in paragraph.frags:
        if hasattr(frag,'text'):
            mapping=pdfmetrics.getFont(frag.fontName).face.charToGlyph
            missing={c for c in frag.text if not c.isspace() and ord(c) not in mapping}
            assert not missing, f'Missing glyphs {missing!r} in {frag.fontName}'
    return paragraph

class GapFigure(Flowable):
    def __init__(self):
        Flowable.__init__(self)
        self.width, self.height = 475, 230
    def draw(self):
        c = self.canv
        ink=colors.HexColor('#193b4b'); fixture=colors.HexColor('#d8e1e6'); pla=colors.HexColor('#8eb6c4'); line=colors.HexColor('#536d79')
        c.setStrokeColor(line); c.setFillColor(ink); c.setFont('Sans-Bold',9)
        c.drawString(35,218,'TOP VIEW')
        c.setFillColor(fixture); c.rect(35,137,315,60,fill=1,stroke=1)
        c.setFillColor(pla); c.rect(57.5,152,270,30,fill=1,stroke=1)
        c.setFillColor(ink); c.setFont('Sans',8.5); c.drawCentredString(192.5,162,'PLA specimen: 60 mm × 10 mm')
        c.setFont('Body',9); c.drawString(363,164,'y ↑'); c.drawString(363,150,'x →')
        c.line(35,207,350,207); c.line(35,203,35,211); c.line(350,203,350,211)
        c.drawCentredString(192.5,210,'70 mm')
        c.line(57.5,126,327.5,126); c.line(57.5,122,57.5,130); c.line(327.5,122,327.5,130)
        c.drawCentredString(192.5,115,'60 mm')
        c.setFont('Sans-Bold',9); c.drawString(35,99,'SIDE VIEW')
        c.setFillColor(fixture); c.rect(35,71,315,18,fill=1,stroke=1); c.rect(35,7,315,18,fill=1,stroke=1)
        c.setFillColor(pla); c.rect(57.5,36,270,24,fill=1,stroke=1)
        c.setFillColor(ink); c.setFont('Sans',8); c.drawCentredString(192.5,44,'60 mm × 4 mm specimen')
        c.setFont('Body',9)
        def vdim(x,y1,y2,label):
            c.line(x,y1,x,y2); c.line(x-4,y1,x+4,y1); c.line(x-4,y2,x+4,y2); c.drawString(x+7,(y1+y2)/2-3,label)
        vdim(410,25,71,'H₀ = h₀ + g₀')
        vdim(335,36,60,'h₀ = 4 mm')
        vdim(49,60,71,'g₀/2'); vdim(49,25,36,'g₀/2')
        c.setFont('Sans',8); c.drawString(365,79,'z ↑'); c.drawString(365,65,'x →')
        c.drawString(35,0,'Each fixture plate: 70 mm × 20 mm × 5 mm; 5 mm plan margin per side')

def footer(c, doc):
    c.saveState()
    c.setFont('Sans',8)
    c.setFillColor(colors.HexColor('#647680'))
    c.drawString(54,27,'CONSTRAINED ANNEALING  |  COMPUTATIONAL DRAFT')
    c.drawRightString(A4[0]-54,27,str(doc.page))
    c.restoreState()

def build():
    text = (ROOT/'manuscript/current.md').read_text(encoding='utf-8')
    lines = text.splitlines()
    story=[]
    i=0
    table_num=0
    while i<len(lines):
        line=lines[i].strip()
        if not line:
            i+=1; continue
        if line=='<!-- PAGE -->': story.append(PageBreak())
        elif line.startswith('TABLE:'):
            table_num+=1
            story.append(P(f'Table {table_num}. '+line[6:].strip(),ST['tablecaption']))
            rows=[]; i+=1
            while i<len(lines) and ' | ' in lines[i]:
                rows.append([v.strip() for v in lines[i].split('|')]); i+=1
            data=[[P(cell,ST['thead'] if r==0 else ST['cell']) for cell in row] for r,row in enumerate(rows)]
            tab=Table(data,colWidths=[117,143,227],repeatRows=1,hAlign='LEFT')
            tab.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#24576b')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.HexColor('#f0f5f7'),colors.white]),('LINEBELOW',(0,-1),(-1,-1),0.4,colors.HexColor('#ccd8de'))]))
            story.extend([tab,Spacer(1,12)])
            continue
        elif line.startswith('FIGURE:'): story.append(GapFigure())
        elif line.startswith('CAPTION:'): story.append(P(line[8:].strip(),ST['caption']))
        elif line.startswith('EQ:'): story.append(P(line[3:].strip(),ST['equation']))
        elif line.startswith('### '): story.append(P(line[4:],ST['heading']))
        elif line.startswith('## '): story.append(P(line[3:],ST['subtitle']))
        elif line.startswith('# '): story.append(P(line[2:],ST['title']))
        else: story.append(P(line,ST['body']))
        i+=1
    OUT.parent.mkdir(parents=True,exist_ok=True)
    doc=SimpleDocTemplate(str(OUT),pagesize=A4,rightMargin=54,leftMargin=54,topMargin=43,bottomMargin=48,title='Free and gap-constrained annealing of FFF-printed PLA: a thermo-mechanical computational study',author='Aadit Jain; Dheeraj Yadav; Ekansh Malhotra',pageCompression=1,invariant=1)
    doc.build(story,onFirstPage=footer,onLaterPages=footer)
    print(OUT)

if __name__=='__main__': build()

"""Build the publisher-neutral master from verified new results and retained SI."""
from pathlib import Path
import csv,json,re,html,hashlib,zipfile,io,subprocess,shutil,sys
from datetime import datetime,timezone
from docx import Document
from reportlab.lib import colors
import build_manuscript as pdf
import build_release as word
from scientific_format import number
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'output/master';OUT.mkdir(exist_ok=True)
def rows(path):return list(csv.DictReader((ROOT/path).open(encoding='utf-8-sig')))
def refs():
    corrections=json.loads((ROOT/'literature/master_metadata_corrections.json').read_text(encoding='utf-8'))
    files=['master_material/chapuis2025','master_material/bute2024','master/lorenzoni2024','master_material/hussam2025','master/frolich2025','master_material/chapuis2023','master/lluch2022','master/suder2020','master_material/benamor2026','master/trofimov2022']
    out=[]
    for n,file in enumerate(files,1):
        j=json.loads((ROOT/('literature/metadata/'+file+'.json')).read_text(encoding='utf-8-sig'));j=j.get('message',j)
        names=[(a.get('family','').title() if a.get('family','').isupper() else a.get('family',''))+', '+''.join(v[0]+'.' for v in a.get('given','').split() if v) for a in j.get('author',[])]
        names=corrections.get(file,{}).get('authors',names)
        author='; '.join(names[:4])+(' et al.' if len(names)>4 else '')
        year=j.get('published',j.get('issued'))['date-parts'][0][0]
        title=j['title'][0]
        if title.isupper():title=title[0]+title[1:].lower()
        title=html.escape(html.unescape(title));journal=html.escape(html.unescape(j.get('container-title',[''])[0]));doi=j['DOI']
        volume=corrections.get(file,{}).get('volume',j.get('volume',''))
        pages=corrections.get(file,{}).get('page',j.get('page',j.get('article-number','')))
        locator=(' '+str(volume) if volume else '')+(', '+str(pages) if pages else '')
        out.append(f'[{n}] {author} ({year}). {title}. <i>{journal}</i>{locator}. <link href="https://doi.org/{doi}" color="#24576b">doi:{doi}</link>.')
    out.append('[11] Outokumpu. Core range datasheet. Physical properties, Table 7, p. 10, Core 304/4301. <link href="https://www.outokumpu.com/en/products/product-ranges/core" color="#24576b">Manufacturer source</link>, accessed 30 October 2026. Exact document URL and coefficient convention are archived in the material register.')
    out.append('[12] Ansys (2026). Mechanical APDL Material Reference, release 2026 R1, §4.8.2; Command Reference, SHIFT and TBPT. <link href="https://ansyshelp.ansys.com/public/Views/Secured/corp/v261/en/pdf/Ansys_Mechanical_APDL_Material_Reference.pdf" color="#24576b">Official documentation</link>.')
    out.append('[13] Ansys (2026). Mechanical APDL Element Reference, release 2026 R1, CONTA178, Contact Normal Definition. <link href="https://ansyshelp.ansys.com/public/views/secured/corp/v261/en/ans_elem/Hlp_E_CONTA178.html" color="#24576b">Official documentation</link>.')
    return '\n\n'.join(out)

def main():
    stats=rows('verification/master_nonisothermal_summary.csv');final=next(r for r in stats if r['attempt']=='table_confirm_a01');assert final['run_accepted']=='True'
    refinements=rows('verification/master_nonisothermal_refinement.csv')
    for pair in [('fine_a01','confirm_a01'),('confirm_a01','table_confirm_a01')]:
        assert any(r['coarse']==pair[0] and r['fine']==pair[1] and r['all_pass']=='True' for r in refinements),pair
    err=float(final['max_abs_error_MPa']);rmse=float(final['rms_error_MPa']);referr=float(final['max_reference_check_change_MPa'])
    result=f'The 1 s and 0.1 s increments fail at some predeclared stress samples. Refining to 0.05 s satisfies all 26 comparison gates; a 0.025 s run and halving the shift-table interval from 0.25 to 0.125 °C confirm the response within the same mixed tolerance. The final maximum sampled stress error is {number(err)} MPa and RMS error {number(rmse)} MPa. Independent-reference step halving changes sampled stress by at most {number(referr,2)} MPa. Reaction equilibrium and recovered material temperature also pass their stated checks. These findings apply to the specified history and samples; they are not a global error bound. A coarser initial solver attempt failed equilibrium near the transition. Its output and the non-passing accuracy candidates are retained.'
    table='\n\nTABLE: Non-isothermal verification samples. Shift step is in temperature, not time.\nΔt (s) | Shift step (°C) | Max. error (MPa) | Pass / 26\n'
    for name in ['coarse_a03','medium_a01','fine_a01','confirm_a01','table_confirm_a01']:
        r=next(r for r in stats if r['attempt']==name);table+=f"{float(r['dt_s']):g} | {float(r['table_spacing_C']):g} | {float(r['max_abs_error_MPa']):.3g} | {r['passed_samples']}\n"
    text=(ROOT/'manuscript/master_body.md').read_text(encoding='utf-8').replace('{{NONISO_RESULT}}',result+table).replace('{{NONISO_CONCLUSION}}',f'The final temperature-shift test over 23–80–23 °C passes 26 sampled comparisons, with maximum stress error {number(err)} MPa and RMS error {number(rmse)} MPa. Time and shift-table refinement pass the predeclared mixed criterion.').replace('{{REFERENCES}}',refs())
    assert '{{' not in text
    (ROOT/'manuscript/master.md').write_text(text,encoding='utf-8',newline='\n')
    pdf.footer=word.footer
    for k in ['title','subtitle','heading']:pdf.ST[k].textColor=colors.black
    word.MATH=json.loads((ROOT/'manuscript/master_equations.json').read_text());word.OUT=OUT
    word.docx(text,ROOT/'figures/release/geometry.png')
    path=OUT/'Constrained-Annealing-2026.docx';doc=Document(path)
    # Old generic builder's fixed index is inappropriate to this shorter article.
    remove=False
    for p in list(doc.paragraphs):
        if p.text=='Cross reference index':remove=True
        if remove:p._element.getparent().remove(p._element)
    doc.core_properties.title=text.splitlines()[0][2:];doc.core_properties.subject='Numerical verification and contact feasibility; independent physical validation incomplete';doc.core_properties.created=doc.core_properties.modified=datetime(2026,11,1,tzinfo=timezone.utc)
    doc.save(path)
    raw=path.read_bytes();buf=io.BytesIO()
    with zipfile.ZipFile(io.BytesIO(raw)) as z,zipfile.ZipFile(buf,'w',zipfile.ZIP_DEFLATED) as out:
        for name in sorted(z.namelist()):
            info=zipfile.ZipInfo(name,(2026,11,1,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;out.writestr(info,z.read(name))
    path.write_bytes(buf.getvalue())
    subprocess.run([sys.executable,str(ROOT/'scripts/render_master_word.py')],cwd=ROOT,check=True,timeout=120)
    shutil.copyfile(OUT/'Constrained-Annealing-2026.pdf',ROOT/'output/pdf/Constrained-Annealing-2026-DRAFT.pdf')
    print('Built full revised master with 8 editable equations, 3 figures, 1 table and 13 references.')
if __name__=='__main__':main()

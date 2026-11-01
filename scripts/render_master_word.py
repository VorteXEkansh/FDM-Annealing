"""Read-only native Word export in isolated local scratch, without UI input."""
from pathlib import Path
import json,shutil,tempfile
import pythoncom
from win32com.client import DispatchEx
ROOT=Path(__file__).resolve().parents[1]
def main():
    work=Path(tempfile.mkdtemp(prefix='FDM-Word-Python-'))
    src=ROOT/'output/master/Constrained-Annealing-2026.docx'
    docx=work/'manuscript.docx';shutil.copyfile(src,docx)
    target=work/'manuscript.pdf'
    pythoncom.CoInitialize();app=None;doc=None
    try:
        app=DispatchEx('Word.Application');app.Visible=False;app.DisplayAlerts=0
        print('Opening generated copy',flush=True)
        doc=app.Documents.Open(str(docx),ConfirmConversions=False,ReadOnly=True,AddToRecentFiles=False)
        doc.Fields.Update()
        print('Repaginating',flush=True);doc.Repaginate()
        print('Exporting',flush=True)
        doc.ExportAsFixedFormat(str(target),17,False,0,0,1,1,0,False,False,0,False,True,False)
        assert target.stat().st_size>10000
        shutil.copyfile(target,ROOT/'output/master/Constrained-Annealing-2026.pdf')
        record=dict(application='Microsoft Word native PDF export via pywin32; source opened read-only',version=app.Version,build=app.Build,equation_transform='Office16 MML2OMML.XSL',export_format=17,doc_structure_tags=False,include_properties=False,input=str(src.relative_to(ROOT)).replace('\\','/'),output='output/master/Constrained-Annealing-2026.pdf',note='PDF metadata may vary; generated DOCX is not modified by export')
        (ROOT/'reproducibility/master_word_environment.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
        print('Native PDF complete',flush=True)
    finally:
        if doc is not None:doc.Close(False)
        if app is not None:app.Quit()
        pythoncom.CoUninitialize()
if __name__=='__main__':main()

"""Acquire public scholarly evidence. No solver or property values are generated."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import urllib.request, urllib.parse, json, hashlib, re
from pypdf import PdfReader
from lxml import etree

ROOT=Path(__file__).resolve().parents[1]
TMP=ROOT/'tmp/literature'
TMP.mkdir(parents=True,exist_ok=True)

SOURCES={
 'Bute2024':'https://matsc.ktu.lt/index.php/MatSc/article/download/35076/16400',
 'Trofimov2022':'https://publications.polymtl.ca/10438/8/2022_Trofimov_Experimentally_validated_modeling_temperature_distribution.pdf',
 'Laminate2025':'https://www.research-collection.ethz.ch/server/api/core/bitstreams/4ee31ad8-b00d-4089-8361-982f0760e6ad/content',
 'Prediction2023':'https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10006872/fullTextXML',
 'Process2025':'https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12525860/fullTextXML',
 'Mould2022':'https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9269357/fullTextXML',
 'Encapsulation2025':'https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12471281/fullTextXML',
 'Relaxation2022':'https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9147248/fullTextXML'
}

def get(url):
    req=urllib.request.Request(url,headers={'User-Agent':'FDM-Annealing literature research/Stage2'})
    with urllib.request.urlopen(req,timeout=45) as r:return r.read()

def acquire(item):
    key,url=item
    try:
        b=get(url)
        suffix='.pdf' if b.startswith(b'%PDF') else '.xml'
        p=TMP/(key+suffix);p.write_bytes(b)
        if suffix=='.pdf':
            texts=[f'PAGE {i+1}\n{p.extract_text()}' for i,p in enumerate(PdfReader(p).pages)]
        else:
            tree=etree.fromstring(b)
            texts=[' '.join(x.itertext()) for x in tree.xpath('//article-title|//article-id|//abstract|//sec/title|//p|//table-wrap|//fig/caption')]
        txt='\n\n'.join(texts)
        (TMP/(key+'.txt')).write_text(txt,encoding='utf-8')
        return {'key':key,'url':url,'sha256':hashlib.sha256(b).hexdigest(),'access':'full text retrieved','text_characters':len(txt),'local_review_copy':str(p.relative_to(ROOT))}
    except Exception as e:return {'key':key,'url':url,'access':'failed','error':str(e)}

if __name__=='__main__':
    results=list(ThreadPoolExecutor(max_workers=4).map(acquire,SOURCES.items()))
    out=ROOT/'literature/acquisition_manifest.json'
    out.write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(results,indent=2))

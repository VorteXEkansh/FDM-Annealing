import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {Workbook,SpreadsheetFile} from '@oai/artifact-tool';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const rows=JSON.parse(await fs.readFile(path.join(root,'literature/literature_matrix.json'),'utf8'));
const wb=Workbook.create();
const columns=['key','authors','year','title','journal','doi','PLA grade','geometry','print condition','annealing temperature','holding time','support/constraint','mechanical data','dimensional data','thermal data','constitutive properties','simulation method','validation usefulness','limitations','relevance','source locator','source URL','access level','adoption status'];
function col(n){let s='';while(n){n--;s=String.fromCharCode(65+n%26)+s;n=Math.floor(n/26)}return s}
function make(name,heads,data,widths){
 const sh=wb.worksheets.add(name);sh.showGridLines=false;
 const last=col(heads.length),range=sh.getRange(`A1:${last}${data.length+1}`);
 range.values=[heads,...data];range.format={font:{name:'Aptos',size:11,color:'#20323C'},wrapText:true,verticalAlignment:'top'};
 range.format.rowHeight=100;
 sh.getRange(`A1:${last}1`).format={fill:'#193B4B',font:{name:'Aptos',bold:true,color:'#FFFFFF'},wrapText:true};sh.getRange(`A1:${last}1`).format.rowHeight=36;
 for(let i=0;i<heads.length;i++)sh.getRange(`${col(i+1)}1:${col(i+1)}${data.length+1}`).format.columnWidth=widths[i]||34;
 for(let i=0;i<data.length;i++)if(i%2===1)sh.getRange(`A${i+2}:${last}${i+2}`).format.fill='#EEF4F6';
 sh.tables.add(`A1:${last}${data.length+1}`,true,name+'Table');sh.freezePanes.freezeRows(1);sh.freezePanes.freezeColumns(1);
 return sh;
}
make('Literature',columns,rows.map(r=>columns.map(c=>r[c])),[22,42,9,66,38,42,32,40,48,48,42,44,44,44,44,48,48,52,62,52,56,62,52,48]);
const sourcecols=['key','metadata_url','metadata_sha256','retrieved','verification','publication dates','reading limits'];
make('Sources',sourcecols,rows.map(r=>[r.key,r.metadata_url,r.metadata_sha256,r.retrieved,r.verification,JSON.stringify(r.publication_dates),'NR means not extracted from accessible evidence, not zero or proof of absence. Source data remain unadopted.']),[22,75,70,16,60,75,70]);
wb.recalculate();
console.log((await wb.inspect({kind:'region',sheetId:'Literature',range:'A1:F4',maxChars:1800,tableMaxCellChars:65})).ndjson);
await fs.mkdir(path.join(root,'tmp/literature_previews'),{recursive:true});
for(const [sheetName,range,label] of [['Literature','A1:F5','bibliography'],['Literature','G1:L5','conditions'],['Literature','M1:R5','response'],['Literature','S1:X5','appraisal'],['Sources','A1:D5','sources']]){
 const blob=await wb.render({sheetName,range,scale:1});await fs.writeFile(path.join(root,'tmp/literature_previews',label+'.png'),new Uint8Array(await blob.arrayBuffer()));
}
const output=await SpreadsheetFile.exportXlsx(wb);await output.save(path.join(root,'literature/literature_matrix.xlsx'));
console.log('Exported literature_matrix.xlsx with 34 records and source verification provenance');

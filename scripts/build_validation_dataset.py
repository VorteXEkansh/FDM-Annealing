"""Extract published observations directly from immutable primary-source XML."""
from pathlib import Path
import csv
import hashlib
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]

def text(element):
    return ' '.join(''.join(element.itertext()).split())

def extract():
    sources = json.loads((ROOT/'validation/source_manifest.json').read_text())['sources']
    rows = []
    for source in sources:
        path = ROOT/source['path']
        assert hashlib.sha256(path.read_bytes()).hexdigest() == source['sha256']
        root = ET.parse(path)
        common = dict(source_key=source['source_key'], doi=source['doi'],
                      source_path=source['path'], source_sha256=source['sha256'],
                      evidence_class='C: published experimental observation',
                      calibration_used='false', prediction='', error='',
                      split_frozen_date='2026-09-28', validation_solved='false')
        if source['source_key'] == 'Mould2022':
            table = root.find(".//table-wrap[@id='polymers-14-02607-t005']")
            for tr in table.findall('.//tbody/tr'):
                cells = [text(td).replace('−','-') for td in tr.findall('td')]
                temperature = cells[0]
                for support, start in [('without_mould',2),('alumina_mould',6)]:
                    for offset, (direction, nominal) in enumerate([('L','80'),('W','10'),('H','4')]):
                        primary = support == 'without_mould' and temperature != '155'
                        rows.append(dict(common, observation_id=f'LC22_{temperature}_{support}_{direction}',
                            dataset_role='reserved_validation' if primary else 'excluded_context',
                            admission_status='conditional_source_specific_reproduction' if primary else 'excluded_from_validation',
                            source_locator=f'Table 5; {temperature} degC; {support}; delta {direction}',
                            material='Ultimaker Pearl White PLA', geometry='rectangular bar 80 x 10 x 4 mm',
                            direction=direction, nominal_dimension_mm=nominal, orientation='XY+0; roads along L; build along H',
                            layer_height_mm='0.2', infill_percent='100', print_nozzle_C='215', print_bed_C='60', print_speed_mm_s='60',
                            temperature_C=temperature, holding_time_min='120', heating='furnace ramp 10 degC/min; part history unmeasured',
                            cooling='furnace cooling to room temperature before unpacking; cooling rate and observation delay unreported',
                            support=support, response='signed directional dimensional change', value=cells[start+offset], unit='percent',
                            normalization='100*(final-initial)/initial', statistic='mean of five specimens', replicate_count='5',
                            reported_response_sd='', uncertainty='caliper resolution 0.01 mm; accuracy +/-0.03 mm; response scatter unavailable',
                            restriction=('Independent of Prusament calibration; source-specific material and thermal/support closures needed' if primary else
                                '155 degC overlaps reported 145-160 degC melting range; Table 7 final temperature conflict' if temperature=='155' else
                                'Powder support not equivalent to plate-gap restraint; no DEM or surrogate clamp admitted')))
        else:
            table = root.find(".//table-wrap[@id='materials-16-04574-t008']")
            for i,tr in enumerate(table.findall('.//tbody/tr')[:3]):
                cells = [text(td) for td in tr.findall('td')]
                if i == 0: cells = cells[1:]
                direction = ['W','T','L'][i]
                layer,hold,temp = cells[4].split('/')
                rows.append(dict(common, observation_id=f'ST23_max_{direction}', dataset_role='secondary_quarantined',
                    admission_status='not_admitted_selected_extreme', source_locator=f'Table 8; PLA; delta {direction}; Max Change and parameter combination',
                    material='PrimaSelect PLA PRO', geometry='ASTM D638-14 dog-bone; Figure 1; overall 165 mm; narrow width 13 mm; thickness 3.2 mm',
                    direction=direction, nominal_dimension_mm=['13','3.2','165'][i], orientation='print-bed layout Figure 2; full road orientation not specified',
                    layer_height_mm=layer, infill_percent='75', print_nozzle_C='210', print_bed_C='60', print_speed_mm_s='50',
                    temperature_C=temp, holding_time_min=hold, heating='placed in oven preconditioned for 30 min; part ramp unreported',
                    cooling='dimensions measured one hour after annealing; cooling environment and part temperature unreported',
                    support='thin sand layer on steel plate', response='reported maximum dimensional change; sign unresolved',
                    value=cells[3], unit='mm', normalization='Table 8 mm magnitude; do not infer signed percent from source equations',
                    statistic='selected maximum over annealed conditions', replicate_count='', reported_response_sd='',
                    uncertainty='Table 8 pooled SD is not within-condition repeatability; no usable uncertainty for maximum',
                    restriction='Selection bias; different grade and porous architecture; sign and individual observations unresolved; no mean-response validation'))
    return rows

def main():
    rows = extract()
    with (ROOT/'validation/validation_dataset.csv').open('w',encoding='utf-8',newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator='\n')
        writer.writeheader(); writer.writerows(rows)
    print(f'Extracted {len(rows)} published observations; no predictions')

if __name__ == '__main__':
    main()

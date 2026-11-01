"""Register final figure/table sources; this does not certify visual inspection."""
from pathlib import Path
import csv, hashlib, re

ROOT = Path(__file__).resolve().parents[1]

def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()

def write(path, records):
    with (ROOT / path).open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(records[0]), lineterminator='\n')
        writer.writeheader()
        writer.writerows(records)

def main():
    figures = [
        ('nonisothermal', ['verification/master_nonisothermal.csv', 'verification/master_nonisothermal_summary.csv']),
        ('contact', ['data/processed/master_fixture_screen.csv'] + [f'simulation/master/stop/{x}_a02/comparison.csv' for x in ['fixed_inside_spacing', 'coexpanding_inside_spacers', 'fixed_outer_faces']]),
        ('recovery', ['verification/programmed_road_check.csv'])]
    records = []
    for n, (name, sources) in enumerate(figures, 1):
        for extension in ['png', 'pdf']:
            artifact = f'figures/master/{name}.{extension}'
            for source in sources:
                records.append(dict(figure=n, artifact=artifact, artifact_sha256=sha(artifact), source=source, source_sha256=sha(source), script='scripts/plot_master.py', script_sha256=sha('scripts/plot_master.py'), raw_lineage='reproducibility/master_result_traceability.csv'))
    write('reproducibility/master_figure_manifest.csv', records)
    si = 'supplementary/master.md'
    titles = re.findall(r'^SUPPTABLE: (.+)$', (ROOT / si).read_text(encoding='utf-8'), re.M)
    sources = [
        ['manuscript/current.md', 'literature/literature_matrix.json'],
        ['material/constitutive_reference.json'],
        ['material/fixture_properties.csv'],
        ['validation/validation_dataset.csv'],
        ['verification/thermal_verification.csv'],
        ['verification/structural_verification.csv'],
        ['convergence/contact_sensitivity.csv'],
        ['verification/structural_verification.csv'],
        ['verification/contact_verification.csv'],
        ['convergence/stage_19_audited_refinement.csv'],
        ['material/pla_properties.csv'],
        ['convergence/mesh_convergence.csv', 'convergence/timestep_convergence.csv', 'convergence/contact_sensitivity.csv'],
        sorted(str(p.relative_to(ROOT)).replace('\\', '/') for p in (ROOT / 'simulation/master').glob('*/*/manifest.json')),
        ['verification/master_nonisothermal.csv'],
        ['verification/programmed_road_check.csv'],
        [f'simulation/master/stop/{x}_a02/comparison.csv' for x in ['fixed_inside_spacing', 'coexpanding_inside_spacers', 'fixed_outer_faces']],
        ['data/processed/master_fixture_screen.csv']]
    assert len(titles) == len(sources) == 17
    records = []
    for n, (title, inputs) in enumerate(zip(titles, sources), 1):
        for source in inputs:
            records.append(dict(table=f'S{n}', title=title, manuscript=si, manuscript_sha256=sha(si), source=source, source_sha256=sha(source), builder='scripts/build_master_supplement.py', builder_sha256=sha('scripts/build_master_supplement.py')))
    source = 'verification/master_nonisothermal_summary.csv'
    records.append(dict(table='1', title='Non-isothermal verification samples', manuscript='manuscript/master.md', manuscript_sha256=sha('manuscript/master.md'), source=source, source_sha256=sha(source), builder='scripts/build_master.py', builder_sha256=sha('scripts/build_master.py')))
    write('reproducibility/master_table_manifest.csv', records)
    print('Registered 3 figures (raster/vector) and 18 tables with source hashes.')

if __name__ == '__main__':
    main()

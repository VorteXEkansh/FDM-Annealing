"""Report missing predictions as missing; plot only observed published means."""
from pathlib import Path
import csv,json
ROOT=Path(__file__).resolve().parents[1]

def main():
    admission=json.loads((ROOT/'simulation/validation/stage12_admission_01/admission.json').read_text())
    by_id={obs:c for c in admission['cases'] for obs in c['observation_ids']}
    raw=list(csv.DictReader((ROOT/'validation/validation_dataset.csv').open(encoding='utf-8')))
    rows=[]
    for r in raw:
        if r['dataset_role']!='reserved_validation':continue
        c=by_id[r['observation_id']]
        rows.append(dict(observation_id=r['observation_id'],case_id=c['case_id'],temperature_C=r['temperature_C'],
            direction=r['direction'],published_mean_percent=r['value'],ansys_prediction_percent='',
            signed_error_percentage_points='',absolute_error_percentage_points='',relative_error_percent='',
            status=c['status'],metric_status='not_computable_no_prediction',
            uncertainty_status='indeterminate_missing_uncertainty',blockers=';'.join(c['blockers']),
            source_doi=r['doi'],solver_output_path='',solver_output_sha256=''))
    p=ROOT/'validation/validation_results.csv'
    with p.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
    summaries=[dict(direction=d,expected_conditions=6,matched_predictions=0,MAE_percentage_points='',RMSE_percentage_points='',worst_absolute_error_percentage_points='',status='not_computable_no_prediction') for d in 'LWH']
    with (ROOT/'validation/validation_metrics.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(summaries[0]),lineterminator='\n');w.writeheader();w.writerows(summaries)
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'svg.hashsalt':'stage12-validation'})
    fig,axs=plt.subplots(1,3,figsize=(10,4.2),sharey=True)
    for ax,d,name,col in zip(axs,'LWH',['Length','Width','Height'],['#24576b','#836329','#8d4257']):
        data=sorted([r for r in rows if r['direction']==d],key=lambda r:float(r['temperature_C']))
        ax.scatter([float(r['temperature_C']) for r in data],[float(r['published_mean_percent']) for r in data],color=col,s=40,zorder=3)
        ax.axhline(0,color='#888888',linewidth=.7);ax.grid(axis='y',alpha=.2)
        ax.set_title(name);ax.set_xlabel('Annealing temperature (°C)');ax.set_xticks([63,86,109,132])
        ax.set_ylim(-4.2,4.5)
    axs[0].set_ylabel('Published signed dimensional change (%)')
    fig.suptitle('Reserved experimental observations — no ANSYS predictions',fontsize=13,y=.98)
    fig.text(.5,.03,'Lluch-Cerezo et al. (2022), Table 5: mould-free means; 120 min; five specimens per condition.\nNo error bars: condition-specific scatter unavailable. No parity or validation score can be calculated.',ha='center',fontsize=9)
    fig.tight_layout(rect=(0,.16,1,.94))
    fig.savefig(ROOT/'figures/validation_observations.png',dpi=300)
    fig.savefig(ROOT/'figures/validation_observations.svg',metadata={'Date':None})
    svg=ROOT/'figures/validation_observations.svg'
    svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8',newline='\n')
    plt.close(fig)
    print('18 status rows; three uncomputed metric groups; observation-only figure')

if __name__=='__main__':main()

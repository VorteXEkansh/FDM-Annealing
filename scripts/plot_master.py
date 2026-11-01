"""Scientific plots from explicit calculations and genuine solver exports."""
from pathlib import Path
import csv,json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'figures/master';OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':9,'axes.spines.top':False,'axes.spines.right':False,'svg.fonttype':'none','pdf.fonttype':42})
def read(p):return list(csv.DictReader((ROOT/p).open(encoding='utf-8-sig')))
def save(fig,name):
    fig.tight_layout();fig.savefig(OUT/(name+'.png'),dpi=260);fig.savefig(OUT/(name+'.pdf'));plt.close(fig)

def main():
    layouts=['fixed_inside_spacing','coexpanding_inside_spacers','fixed_outer_faces'];names=['Fixed inner spacing','Expanding inner spacers','Fixed outer faces'];colors=['#174f8c','#ca7828','#34817b']
    fig,ax=plt.subplots(1,2,figsize=(7.3,2.8));data=read('data/processed/master_fixture_screen.csv')
    for layout,name,col in zip(layouts,names,colors):
        rr=[r for r in data if r['layout']==layout and float(r['gap_mm'])==.02]
        ax[0].plot([float(r['temperature_C']) for r in rr],[100*float(r['critical_signed_thickness_recovery_strain']) for r in rr],label=name,color=col)
        path=f'simulation/master/stop/{layout}_a02';assert json.loads((ROOT/path/'manifest.json').read_text())['accepted']
        rr=read(path+'/comparison.csv')[:6];x=[float(r['T_C']) for r in rr]
        ax[1].plot(x,[float(r['ref_force_N']) for r in rr],color=col)
        ax[1].plot(x,[float(r['compressive_force_N']) for r in rr],marker='o',ms=3,linestyle='',color=col)
    ax[0].axhline(0,color='0.5',lw=.6,ls=':');ax[0].set(xlabel='Uniform temperature (°C)',ylabel='Critical thickness recovery (%)',title='(a) Contact threshold');ax[0].legend(fontsize=7)
    ax[1].set(xlabel='Prescribed temperature (°C)',ylabel='Normal stop force (N)',title='(b) Elastic stop reference');ax[1].text(.04,.94,'Lines: analytical\nDots: ANSYS',transform=ax[1].transAxes,va='top',fontsize=8)
    save(fig,'contact')
    rr=read('verification/master_nonisothermal.csv');select=[r for r in rr if r['attempt']=='table_confirm_a01'];assert select
    fig,ax=plt.subplots(1,2,figsize=(7.3,2.6));x=[float(r['time_s']) for r in select]
    ax[0].plot(x,[float(r['reference_stress_MPa']) for r in select],color='#174f8c',label='Independent reference');ax[0].plot(x,[float(r['ansys_stress_MPa']) for r in select],'o',ms=3,color='#ca7828',label='ANSYS');ax[0].set(xlabel='Time (s)',ylabel='Axial stress (MPa)',title='(a) Restrained thermal cycle');ax[0].legend(fontsize=7)
    stats=read('verification/master_nonisothermal_summary.csv')
    for r in stats:
        if float(r['table_spacing_C'])==.25:
            ax[1].plot(float(r['dt_s']),float(r['max_abs_error_MPa']),'o',color='#174f8c')
    ax[1].set(xscale='log',yscale='log',xlabel='Time increment (s)',ylabel='Maximum sampled error (MPa)',title='(b) Time refinement')
    save(fig,'nonisothermal')
    rr=read('verification/programmed_road_check.csv');fig,ax=plt.subplots(figsize=(6,2.4))
    for phase,col in zip(['heat','hold','cool'],colors):
        r=[r for r in rr if r['phase']==phase];ax.plot([int(v['substeps_per_phase']) for v in r],[100*float(v['axial_mechanical_strain']) for v in r],'-o',label=phase,color=col,ms=3)
    ax.axhline(-5.6175,color='0.5',ls=':',lw=.8,label='Programmed long-time limit');ax.set(xscale='log',xlabel='Substeps per phase',ylabel='Mechanical strain (%)',title='Programmed-road calculation, not measured coupon recovery');ax.legend(fontsize=7,ncols=2);save(fig,'recovery')
if __name__=='__main__':main()

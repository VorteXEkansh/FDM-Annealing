"""Record computed Prony conversion and supported scope, not an ANSYS input deck."""
from pathlib import Path
import hashlib,json,sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from src.constitutive import Prusament


def main():
    m=Prusament.from_database()
    g,k=m.shear_bulk(0,65)
    inputs=['material/pla_properties.csv','material/fixture_properties.csv','src/constitutive.py','scripts/build_constitutive_reference.py']
    result={
        'stage':5,'date':'2026-09-12','role':'Calculated reference conversion; no ANSYS material card or solver output',
        'formulation':'Prusament PLA','source':'Chapuis et al. (2025), DOI 10.1088/1361-665X/adeee4, supplementary Tables B.1–B.2',
        'domain':{'temperature_C':[23,85],'meaning':'Direct characterization temperature envelope only; no blanket duration, strain or geometry validity','thermal_reference_C':23,'relaxation_reference_C':65,'thermal_reference_status':'numerical verification convention; not final production boundary'},
        'instantaneous_moduli_MPa':{'E':m.instantaneous,'G':g,'K':k},
        'equilibrium_modulus_MPa':m.equilibrium,'poisson_ratio':m.poisson,
        'conversion':'g_i=k_i/E_inst; G_inst=E_inst/[2(1+nu)]; K_inst=E_inst/[3(1-2nu)]',
        'prony':[{'branch':i,'shear_fraction':fraction,'bulk_fraction':fraction,'reference_relaxation_time_s':tau,'temperature_C':65,'evidence_class':'B: arithmetic from source C; matching bulk spectrum is a constitutive assumption'} for i,(fraction,tau) in enumerate(m.normalized_prony(),1)],
        'equilibrium_fraction':m.equilibrium/m.instantaneous,
        'admitted_operations':['isotropic material-point stiffness and compliance','Prusament reversible thermal strain','piecewise temperature shift and reference reduced-time quadrature','generalized-Maxwell reference updates','conditional equal-fraction shear/bulk conversion','AISI 304 property interpolation and elastic response'],
        'blocked_operations':['production annealing simulation','bulk irreversible annealing strain','crystallization kinetics','complete orthotropic response','fixture thermal strain until expansion convention is known'],
        'input_code_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs}
    }
    (ROOT/'material/constitutive_reference.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
    print('Recorded source-derived reference conversion and evidence gates')


if __name__=='__main__':main()

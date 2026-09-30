"""Publication plots from unchanged verified convergence CSVs.

Plot selection and numeric values follow the archived verification plotter;
only editorial titles and output locations differ. No smoothing or fitting.
"""
from pathlib import Path
import csv,hashlib,json
ROOT=Path(__file__).resolve().parents[1]
FIG=ROOT/'figures/publication'
FIG.mkdir(parents=True,exist_ok=True)
def plot_tables(mesh_rows: list[dict], time_rows: list[dict], contact_rows: list[dict]) -> None:
    import matplotlib.pyplot as plt
    plt.rcParams.update({"font.size": 9, "axes.titlesize": 10, "axes.labelsize": 9, "figure.dpi": 140})
    FIG.mkdir(parents=True, exist_ok=True)
    colors = {"structural": "#24576b", "thermal": "#cc6b32", "contact_normal_lagrange": "#4c7a52"}
    panels = [
        ("structural", "W_max", r"$W_{\max}$ (mm)"),
        ("structural", "residual_displacement", "Residual displacement (mm)"),
        ("structural", "residual_stress_p95", r"Residual $\sigma_{\mathrm{res},95}$ (MPa)"),
        ("thermal", "temperature_gradient_at_300_s", "Temperature gradient (°C m⁻¹)"),
        ("contact_normal_lagrange", "mean_contact_pressure", "Mean contact pressure (MPa)"),
        ("contact_normal_lagrange", "maximum_contact_pressure", "Peak contact pressure (MPa)"),
    ]
    fig, axes = plt.subplots(2, 3, figsize=(10.2, 6.2), constrained_layout=True)
    for ax, (model, quantity, ylabel) in zip(axes.flat, panels):
        subset = [row for row in mesh_rows if row["model"] == model and row["quantity"] == quantity]
        x = [int(row["solid_elements"]) for row in subset]
        y = [float(row["value"]) for row in subset]
        ax.plot(x, y, "o-", color=colors[model], linewidth=1.7, markersize=4)
        ax.set_xscale("log")
        ax.set_xlabel("Solid elements")
        ax.set_ylabel(ylabel)
        ax.grid(True, alpha=0.25)
        ax.set_title({"structural": "Two-layer Prony benchmark", "thermal": "Plane-wall benchmark", "contact_normal_lagrange": "Normal-Lagrange contact"}[model])
    fig.suptitle("Mesh refinement of numerical reference configurations", fontsize=12, fontweight="bold")
    fig.savefig(FIG / "mesh_convergence.png", dpi=300, bbox_inches="tight")
    plt.close(fig)

    panels = [
        ("thermal", "thermal_lag_at_300_s", "Thermal lag (°C)", "thermal_dt_s"),
        ("thermal", "temperature_profile_L2_excursion", "Profile L2 excursion (°C)", "thermal_dt_s"),
        ("structural", "W_max", r"$W_{\max}$ (mm)", "structural_ramp_dt_s"),
        ("structural", "residual_stress_p95", r"Residual $\sigma_{\mathrm{res},95}$ (MPa)", "structural_ramp_dt_s"),
    ]
    fig, axes = plt.subplots(2, 2, figsize=(8.4, 6.2), constrained_layout=True)
    for ax, (model, quantity, ylabel, step_key) in zip(axes.flat, panels):
        subset = [row for row in time_rows if row["model"] == model and row["quantity"] == quantity]
        x = [float(row[step_key]) for row in subset]
        y = [float(row["value"]) for row in subset]
        ax.plot(x, y, "o-", color=colors[model], linewidth=1.7, markersize=4)
        ax.set_xscale("log")
        ax.invert_xaxis()
        ax.set_xlabel("Time increment (s)")
        ax.set_ylabel(ylabel)
        ax.grid(True, alpha=0.25)
    fig.suptitle("Time-step refinement of numerical reference configurations", fontsize=12, fontweight="bold")
    fig.savefig(FIG / "timestep_convergence.png", dpi=300, bbox_inches="tight")
    plt.close(fig)

    fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.6), constrained_layout=True)
    for algorithm, marker in (("penalty", "o"), ("augmented_lagrange", "s")):
        subset = [row for row in contact_rows if row["algorithm"] == algorithm and float(row["friction_coefficient"]) == 0.0]
        subset.sort(key=lambda row: float(row["FKN_factor"]))
        axes[0].plot([float(row["FKN_factor"]) for row in subset], [float(row["maximum_penetration_mm"]) for row in subset], marker + "-", label=algorithm.replace("_", " "))
    axes[0].set_xscale("log"); axes[0].set_yscale("log")
    axes[0].set_xlabel(r"$F_{\mathrm{KN}}$ factor"); axes[0].set_ylabel("Maximum penetration (mm)")
    axes[0].grid(True, which="both", alpha=0.25); axes[0].legend(frameon=False)
    friction = [row for row in contact_rows if row["algorithm"] == "augmented_lagrange" and float(row["FKN_factor"]) == 1.0]
    friction.sort(key=lambda row: float(row["friction_coefficient"]))
    mu = [float(row["friction_coefficient"]) for row in friction]
    axes[1].plot(mu, [float(row["mean_contact_pressure_MPa"]) for row in friction], "o-", label="mean pressure")
    axes[1].plot(mu, [float(row["maximum_contact_pressure_MPa"]) for row in friction], "s-", label="peak pressure")
    axes[1].set_xlabel("Friction coefficient, μ"); axes[1].set_ylabel("Contact pressure (MPa)")
    axes[1].grid(True, alpha=0.25); axes[1].legend(frameon=False)
    fig.suptitle("Contact-control sensitivity: numerical reference interface", fontsize=12, fontweight="bold")
    fig.savefig(FIG / "contact_sensitivity.png", dpi=300, bbox_inches="tight")
    plt.close(fig)


if __name__=='__main__':
    files=['convergence/mesh_convergence.csv','convergence/timestep_convergence.csv','convergence/contact_sensitivity.csv']
    data=[]
    for path in files:
        with (ROOT/path).open(encoding='utf-8') as stream:data.append(list(csv.DictReader(stream)))
    plot_tables(*data)
    paths=files+['scripts/build_publication_figures.py']+[p.relative_to(ROOT).as_posix() for p in sorted(FIG.glob('*.png'))]
    report={'stage':18,'scope':'Redrawn archived verification data; titles updated, numeric values unchanged','source_hashes':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}
    (ROOT/'docs/stage_18_figure_manifest.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n')

"""Build the Stage 4 material-property database from curated source extracts.

The script contains only transcribed published values and explicitly labelled
calculations.  It does not interpolate missing PLA data or combine formulations.
"""
from __future__ import annotations

from pathlib import Path
import csv
import hashlib
import json


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "material"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="raise")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    sources = [
        dict(source_key="PrusamentTDS2022", authors="Prusa Polymers a.s.", year="2022", title="Technical datasheet: Prusament PLA", journal_or_publisher="Prusa Polymers a.s.", doi_or_reference="Prusament PLA TDS v1.1 (27 July 2022)", formulation="Prusament PLA", source_locator="p. 2 and p. 3 note 3", source_url="https://prusament.com/materials/pla/", evidence_scope="Typical density and room-condition printed tensile modulus; the test temperature is not reported", compatibility_decision="Same named formulation as Chapuis et al.; usable only for the stated typical values, with temperature limitation retained", local_evidence="literature/evidence/stage_04/Prusament_PLA_TDS_2022_EN.pdf"),
        dict(source_key="Chapuis2025", authors="Joël N. Chapuis; Gian Teufen; Kristina Shea", year="2025", title="Thermo-viscoelastic laminate-based finite element modeling of fused filament fabrication direct 4D printing", journal_or_publisher="Smart Materials and Structures 34, 075034", doi_or_reference="10.1088/1361-665X/adeee4", formulation="Prusament PLA", source_locator="main text §§2.1–2.2 and 3.1; supplementary Tables B.1–B.2; main-text Table 5", source_url="https://doi.org/10.1088/1361-665X/adeee4", evidence_scope="Grade-specific DMA, 23-term generalized Maxwell model, WLF/Arrhenius shifting, constant ν and α, and calibrated AM pre-strain", compatibility_decision="Primary constitutive evidence set; direct characterization spans 23–85 °C and does not establish k(T), c_p(T), density temperature dependence, or bulk constrained-annealing shrinkage", local_evidence="literature/evidence/stage_04/Chapuis2025_supplement.pdf"),
        dict(source_key="Luberto2024", authors="Luca Luberto; Volker Böß; Kristin M. de Payrebrune", year="2024", title="Finite Difference Modeling and Experimental Investigation of Cyclic Thermal Heating in the Fused Filament Fabrication Process", journal_or_publisher="3D Printing and Additive Manufacturing 11, e1064–e1072", doi_or_reference="10.1089/3dp.2022.0282", formulation="PLA filament; commercial grade not identified", source_locator="Material and heat transfer model, Table 1", source_url="https://doi.org/10.1089/3dp.2022.0282", evidence_scope="ρ, c_p and k at 20 °C used as constants in an FFF heat-transfer model", compatibility_decision="Thermal comparator only; not transferred to Prusament PLA because the formulation is unidentified and temperature dependence was assumed away", local_evidence="literature/evidence/stage_04/Luberto2024_PMC.html"),
        dict(source_key="Trofimov2022", authors="Anton Trofimov et al.", year="2022", title="Experimentally validated modeling of the temperature distribution and the distortion during the Fused Filament Fabrication process", journal_or_publisher="Additive Manufacturing 54, 102693", doi_or_reference="10.1016/j.addma.2022.102693", formulation="Raise3D Premium PLA with transferred literature functions", source_locator="§3.2 and Table 1", source_url="https://doi.org/10.1016/j.addma.2022.102693", evidence_scope="Temperature-dependent model table for E, ν, α, k, c_p and ρ", compatibility_decision="Excluded from the Prusament law: the table combines room-temperature grade measurements with functions and thermal data from other literature", local_evidence="tmp/literature/Trofimov2022.pdf"),
        dict(source_key="Li2024", authors="Meiyu Li; Yanan Xu; Jianguang Fang", year="2024", title="Orthotropic mechanical properties of PLA materials fabricated by fused deposition modeling", journal_or_publisher="Thin-Walled Structures 199, 111800", doi_or_reference="10.1016/j.tws.2024.111800", formulation="FormFutura Premium PLA", source_locator="§2.1 and Table 4", source_url="https://doi.org/10.1016/j.tws.2024.111800", evidence_scope="Seven calibrated room-condition orthotropic elastic constants", compatibility_decision="Comparator only: different grade/road geometry, and G23 plus ν23 are absent, so the full ANSYS orthotropic matrix is not identifiable", local_evidence="literature/evidence/stage_04/Li2024_orthotropic.pdf"),
        dict(source_key="Bute2024", authors="Irina Bute; Sergejs Tarasovs; Jevgenijs Sevcenko; Andrey Aniskevich", year="2024", title="Thermomechanical Analysis and Numerical Simulations of Fused Filament Fabricated Polylactic Acid Parts", journal_or_publisher="Materials Science 30, 217–225", doi_or_reference="10.5755/j02.ms.35076", formulation="Black Devil Design PLA", source_locator="§§2.1–2.3 and 3.1–3.3; Figures 9–15", source_url="https://doi.org/10.5755/j02.ms.35076", evidence_scope="Directional CLTE and irreversible thermal strain during TMA; qualitative ANSYS residual-stress comparison", compatibility_decision="Recovery-mechanism comparator only; different grade and print architecture, with most numerical strain values available graphically rather than as a table", local_evidence="tmp/literature/Bute2024.pdf"),
        dict(source_key="Relaxation2022", authors="Roberto Giannella et al.", year="2022", title="Stress Relaxation Behavior of Additively Manufactured Polylactic Acid (PLA)", journal_or_publisher="Materials 15, 3509", doi_or_reference="10.3390/ma15103509", formulation="SUNLU PLA Plus", source_locator="§§2–3 and Tables 4–8", source_url="https://doi.org/10.3390/ma15103509", evidence_scope="Room-condition tensile stiffness and 500 s relaxation tests with Maxwell, standard-linear-solid and Findley fits", compatibility_decision="Comparator only; different modified PLA grade and no temperature-shifted Prony series for annealing temperatures", local_evidence="tmp/literature/Relaxation2022.xml"),
        dict(source_key="Pantani2010", authors="Roberto Pantani; Francesco De Santis; Andrea Sorrentino; Fabrizio De Maio; Giuseppe Titomanlio", year="2010", title="Crystallization kinetics of virgin and processed poly(lactic acid)", journal_or_publisher="Polymer Degradation and Stability 95, 1148–1159", doi_or_reference="10.1016/j.polymdegradstab.2010.04.018", formulation="Virgin and processed PLA studied in that paper; not Prusament PLA", source_locator="publication metadata and abstract; numerical kinetic tables not accepted without compatible full-text extraction", source_url="https://doi.org/10.1016/j.polymdegradstab.2010.04.018", evidence_scope="Isothermal/non-isothermal crystallization kinetics precedent", compatibility_decision="No kinetic coefficient transferred; formulation and thermal-history compatibility are unestablished", local_evidence="literature/metadata/Pantani2010.json"),
        dict(source_key="Nucleation2011", authors="Andrea Sorrentino; Roberto Pantani", year="2011", title="Nucleation and crystallization kinetics of poly(lactic acid)", journal_or_publisher="Thermochimica Acta 522, 128–134", doi_or_reference="10.1016/j.tca.2011.05.034", formulation="Commercial PLA grade studied in that paper; not Prusament PLA", source_locator="publication metadata and abstract", source_url="https://doi.org/10.1016/j.tca.2011.05.034", evidence_scope="Avrami and Lauritzen–Hoffman crystallization precedent", compatibility_decision="No kinetic coefficient transferred; the grade and thermal path do not identify Prusament behavior", local_evidence="literature/metadata/Nucleation2011.json"),
        dict(source_key="WLF1955", authors="Malcolm L. Williams; Robert F. Landel; John D. Ferry", year="1955", title="The Temperature Dependence of Relaxation Mechanisms in Amorphous Polymers and Other Glass-forming Liquids", journal_or_publisher="Journal of the American Chemical Society 77, 3701–3707", doi_or_reference="10.1021/ja01619a008", formulation="General glass-forming-polymer theory", source_locator="article", source_url="https://doi.org/10.1021/ja01619a008", evidence_scope="Time–temperature shift foundation", compatibility_decision="Theory source only; numerical constants used here come from the grade-specific Chapuis fit", local_evidence="literature/metadata/WLF1955.json"),
        dict(source_key="Meng2026", authors="Longhui Meng; Aqib Mashood Khan; Yicai Shan; Khalid A. Al-Ghamdi", year="2026", title="Saturation behavior and full-field reconstruction of residual stress in quenched AISI 304 stainless steel via the contour method", journal_or_publisher="Scientific Reports 16, 11694", doi_or_reference="10.1038/s41598-026-45542-w", formulation="AISI 304 stainless steel", source_locator="Material properties and model setup, Table 1", source_url="https://doi.org/10.1038/s41598-026-45542-w", evidence_scope="Tabulated temperature-dependent ρ, c_p, k, α, E and ν from 20–800 °C", compatibility_decision="Selected fixture-property source; 20, 100 and 200 °C rows bracket the planned 20–110 °C domain", local_evidence="literature/evidence/stage_04/Meng2026_AISI304_PMC.html"),
    ]
    for source in sources:
        local = ROOT / source["local_evidence"]
        source["sha256"] = sha256(local) if local.exists() else "evidence file not present in checkout"

    fields = ["record_id", "dataset_role", "property_symbol", "property_name", "component", "value", "unit", "temperature_C", "temperature_context", "source_key", "doi_or_reference", "PLA_formulation", "print_condition", "confidence_relevance", "compatibility_status", "how_used_in_ANSYS", "source_locator", "notes"]
    rows: list[dict[str, str]] = []

    def add(symbol: str, name: str, component: str, value: float | str, unit: str, temp: str,
            tcontext: str, source: str, formulation: str, print_condition: str, confidence: str,
            status: str, ansys: str, locator: str, notes: str = "", role: str = "candidate") -> None:
        rows.append(dict(record_id=f"PLA-{len(rows)+1:03d}", dataset_role=role, property_symbol=symbol,
                         property_name=name, component=component, value=str(value), unit=unit,
                         temperature_C=temp, temperature_context=tcontext, source_key=source,
                         doi_or_reference=next(s["doi_or_reference"] for s in sources if s["source_key"] == source),
                         PLA_formulation=formulation, print_condition=print_condition,
                         confidence_relevance=confidence, compatibility_status=status,
                         how_used_in_ANSYS=ansys, source_locator=locator, notes=notes))

    prusa_print = "Original Prusa i3 MK3; 100% rectilinear infill; 0.20 mm layers; 2 perimeters; 215 °C nozzle; 60 °C bed; 200 mm s⁻¹ infill"
    add("ρ", "mass density", "isotropic", 1240, "kg m⁻³", "not reported", "supplier typical value", "PrusamentTDS2022", "Prusament PLA", "not specified for density test", "moderate; exact formulation, temperature omitted", "candidate_missing_temperature", "Do not enter until the reference temperature treatment is declared", "TDS p. 2")
    add("E", "tensile modulus", "horizontal", 2300, "MPa", "not reported", "printed tensile test", "PrusamentTDS2022", "Prusament PLA", prusa_print, "moderate; mean ±0.1 GPa reported", "screening_only", "Room-condition cross-check only; not the viscoelastic relaxation modulus", "TDS pp. 2–3", "Reported as 2.3 ± 0.1 GPa")
    add("E", "tensile modulus", "vertical xz", 2400, "MPa", "not reported", "printed tensile test", "PrusamentTDS2022", "Prusament PLA", prusa_print, "moderate; mean ±0.1 GPa reported", "screening_only", "Room-condition cross-check only; not the viscoelastic relaxation modulus", "TDS pp. 2–3", "Reported as 2.4 ± 0.1 GPa")

    chapuis_print = "ASTM D638 Type IV; Prusament PLA; DMA frequency sweeps 1–18 Hz at 5 °C intervals; at least 3 specimens"
    add("ν", "Poisson ratio", "isotropic", 0.35, "1", "23–85", "constant in source model", "Chapuis2025", "Prusament PLA", chapuis_print, "high for the published model; uncertainty not reported", "admissible_within_source_domain", "Candidate constant ν in isotropic viscoelastic structural model", "Supplementary Table B.1")
    add("α", "coefficient of linear thermal expansion", "isotropic", 68.0, "µm m⁻¹ K⁻¹", "23–85", "constant in source model", "Chapuis2025", "Prusament PLA", chapuis_print, "high for the published model; uncertainty not reported", "admissible_within_source_domain", "Candidate constant isotropic thermal expansion for verification cases; irreversible pre-strain remains separate", "Supplementary Table B.1")
    add("T_g", "glass-transition temperature", "tan δ peak", 65, "°C", "65", "DMA tan δ peak", "Chapuis2025", "Prusament PLA", chapuis_print, "high; directly determined in source study", "admissible_within_source_domain", "Reference temperature for shift-factor law, not a structural boundary condition", "Main text §3.1.1 and Supplementary Table B.1")
    k0 = 10.598
    branches = [
        (6.228, 1.176e-14), (1.806, 1.228e-14), (7.849, 2.878e-14), (12.751, 1.701e-12),
        (20.857, 9.178e-12), (31.104, 6.034e-11), (45.566, 6.187e-9), (64.036, 1.102e-7),
        (92.484, 1.047e-6), (135.916, 6.903e-6), (113.488, 2.582e-5), (128.266, 5.363e-5),
        (173.470, 1.838e-4), (93.393, 4.386e-4), (163.804, 7.577e-4), (134.311, 1.795e-3),
        (119.266, 2.292e-3), (100.596, 6.576e-3), (80.534, 9.920e-3), (61.624, 3.290e-2),
        (44.508, 5.374e-2), (30.529, 6.586e-2), (18.610, 3.503e1),
    ]
    e_inst = k0 + sum(k for k, _ in branches)
    add("E_∞", "long-term Young modulus", "equilibrium Hookean element k₀", k0, "MPa", "65", "reference T_g; master-curve model", "Chapuis2025", "Prusament PLA", chapuis_print, "high; directly tabulated", "admissible_within_source_domain", "Long-term modulus term after ANSYS-compatible formulation is verified", "Supplementary Table B.1")
    add("E_0", "instantaneous Young modulus", "k₀ + Σkᵢ", f"{e_inst:.3f}", "MPa", "65", "calculated at reference T_g from 23 tabulated branches", "Chapuis2025", "Prusament PLA", chapuis_print, "high arithmetic traceability; model-transfer uncertainty remains", "calculated_candidate", "Candidate instantaneous modulus for normalized Prony conversion", "Supplementary Tables B.1–B.2", "Reproducible sum: 10.598 MPa + Σkᵢ = 1691.594 MPa")
    add("C₁", "WLF constant", "above T_g", 17.4, "1", "≥65", "T₀ = T_g", "Chapuis2025", "Prusament PLA", chapuis_print, "high for source model", "admissible_within_source_domain", "Candidate ANSYS shift law after convention/sign verification", "Supplementary Table B.1 and main-text Eq. (6)")
    add("C₂", "WLF constant", "above T_g", 51.6, "K", "≥65", "T₀ = T_g", "Chapuis2025", "Prusament PLA", chapuis_print, "high for source model", "admissible_within_source_domain", "Candidate ANSYS shift law after convention/sign verification", "Supplementary Table B.1 and main-text Eq. (6)")
    add("C₃", "Arrhenius shift constant", "below T_g", 35000, "K", "<65", "log₁₀a_T = C₃(1/T − 1/T_g)", "Chapuis2025", "Prusament PLA", chapuis_print, "high for source model", "requires_custom_or_tabulated_shift", "Native ANSYS representation must reproduce the published piecewise shift law", "Supplementary Table B.1 and main-text Eq. (6)")
    for i, (ki, tau) in enumerate(branches, 1):
        gi = ki / e_inst
        add("kᵢ", "Maxwell-branch stiffness", f"branch {i}", ki, "MPa", "65", "reference T_g", "Chapuis2025", "Prusament PLA", chapuis_print, "high; directly tabulated", "admissible_within_source_domain", "Convert to normalized ANSYS shear-relaxation ratio only after constant-ν equivalence is verified", "Supplementary Table B.2", f"Calculated normalized modulus fraction kᵢ/E₀ = {gi:.12g}")
        add("τᵢ", "Maxwell-branch relaxation time", f"branch {i}", f"{tau:.6g}", "s", "65", "reference T_g", "Chapuis2025", "Prusament PLA", chapuis_print, "high; directly tabulated", "admissible_within_source_domain", "Candidate Prony relaxation time paired with branch stiffness", "Supplementary Table B.2")

    prestrain = [
        (195, 75, 0.05618, 0.05605), (200, 75, 0.04206, 0.04199),
        (200, 90, 0.10350, 0.10290), (215, 90, 0.07957, 0.07926),
    ]
    for nozzle, activation, pattern, timo in prestrain:
        cond = f"25 mm × 5 mm, 0.1 mm layers; nozzle {nozzle} °C; activation {activation} °C; bilayer calibration"
        add("ε₁₁^AM", "programmed AM pre-strain", "pattern-search identification", pattern, "1", str(activation), "activation temperature", "Chapuis2025", "Prusament PLA", cond, "moderate; geometry-calibrated, no dispersion reported", "not_bulk_annealing_input", "Do not use as bulk annealing strain without a transfer and identifiability study", "Main-text Table 5")
        add("ε₁₁^AM", "programmed AM pre-strain", "Timoshenko-bilayer identification", timo, "1", str(activation), "activation temperature", "Chapuis2025", "Prusament PLA", cond, "moderate; analytical identification, no dispersion reported", "not_bulk_annealing_input", "Method bracket only; not an uncertainty distribution", "Main-text Table 5")

    for sym, name, val, unit in [("ρ", "mass density", 1240, "kg m⁻³"), ("c_p", "specific heat capacity", 1800, "J kg⁻¹ K⁻¹"), ("k", "thermal conductivity", 0.13, "W m⁻¹ K⁻¹")]:
        add(sym, name, "isotropic", val, unit, "20", "used constant up to 140 °C by source", "Luberto2024", "Unidentified PLA filament", "Prusa i3 MKS3 FFF cuboid", "low transfer relevance; exact source grade absent", "incompatible_comparator", "Do not use for Prusament PLA; retain for screening only", "Table 1", role="comparator")

    trofimov_condition = "Raise3D Premium PLA; Raise3D Pro2; 100% infill; 0.2 mm layers; 0.4 mm nozzle; 210 °C nozzle; 60 °C bed"
    for temp, val in [(25,1860),(40,1727),(50,1603),(60,1000),(70,300),(80,50),(90,10),(100,1),(150,1)]:
        add("E", "Young modulus", "isotropic model table", val, "MPa", str(temp), "model input; room value measured then reduced using another source", "Trofimov2022", "Raise3D Premium PLA with transferred functions", trofimov_condition, "moderate as reproduced model input; low grade purity", "incompatible_source_mixture", "Do not merge with Prusament properties", "Table 1 and §3.2", role="comparator")
    for sym, name, lo, hi, unit in [("α","coefficient of linear thermal expansion",79,147,"µm m⁻¹ K⁻¹"),("k","thermal conductivity",0.11,0.19,"W m⁻¹ K⁻¹"),("c_p","specific heat capacity",1590,1950,"J kg⁻¹ K⁻¹")]:
        add(sym, name, "isotropic low-temperature table value", lo, unit, "25–90", "piecewise source table", "Trofimov2022", "Raise3D Premium PLA with transferred functions", trofimov_condition, "low transfer relevance", "incompatible_source_mixture", "Do not merge with Prusament properties", "Table 1 and §3.2", role="comparator")
        add(sym, name, "isotropic high-temperature table value", hi, unit, "100–150", "piecewise source table", "Trofimov2022", "Raise3D Premium PLA with transferred functions", trofimov_condition, "low transfer relevance", "incompatible_source_mixture", "Do not merge with Prusament properties", "Table 1 and §3.2", role="comparator")
    add("ν", "Poisson ratio", "isotropic", 0.36, "1", "25–150", "constant in source model", "Trofimov2022", "Raise3D Premium PLA with transferred functions", trofimov_condition, "low transfer relevance", "incompatible_source_mixture", "Do not merge with Prusament properties", "Table 1 and §3.2", role="comparator")
    add("ρ", "mass density", "isotropic", 1250, "kg m⁻³", "25–150", "constant in source model", "Trofimov2022", "Raise3D Premium PLA with transferred functions", trofimov_condition, "low transfer relevance", "incompatible_source_mixture", "Do not merge with Prusament properties", "Table 1 and §3.2", role="comparator")

    li_condition = "FormFutura Premium PLA; Ultimaker S5; line infill; 0 mm road air gap; 0.2 mm layers; 0.8 mm line width; 210 °C; 45 mm s⁻¹; 60 °C bed"
    for sym, name, comp, val, unit in [
        ("E₁","Young modulus","road direction 1",2669,"MPa"),("E₂","Young modulus","transverse in-plane 2",2583,"MPa"),("E₃","Young modulus","build direction 3",2208,"MPa"),
        ("ν₁₂","Poisson ratio","12",0.43,"1"),("ν₁₃","Poisson ratio","13",0.37,"1"),("G₁₂","shear modulus","12",919,"MPa"),("G₃₁","shear modulus","31",844,"MPa")]:
        add(sym, name, comp, val, unit, "not reported", "laboratory tensile characterization", "Li2024", "FormFutura Premium PLA", li_condition, "high for reported architecture; low transfer relevance", "incomplete_incompatible_orthotropic_set", "Do not enter as Prusament orthotropy; G₂₃ and ν₂₃ are missing", "Table 4", role="comparator")

    relax_condition = "SUNLU PLA Plus; 0.4 mm nozzle; 210 °C; 60 mm s⁻¹; 50 °C bed; 0.1 mm layers; 100% single-direction infill; one contour"
    for direction, val in [("0°",3045),("45°",2914),("90°",2932)]:
        add("E", "tensile modulus", direction, val, "MPa", "not reported", "controlled laboratory environment", "Relaxation2022", "SUNLU PLA Plus", relax_condition, "high for reported specimens; low transfer relevance", "incompatible_comparator", "Do not use for Prusament; relaxation evidence is qualitative for model selection", "Table 4", "Published uncertainty ±3 MPa", role="comparator")
    add("ΔE/E₀", "normalized relaxation over 500 s", "0°/45°/90° summary", "≈11–13", "%", "not reported", "500 s constant-strain room-condition tests", "Relaxation2022", "SUNLU PLA Plus", relax_condition, "moderate; rounded textual summary", "incompatible_comparator", "Do not convert to a Prony series for annealing", "§3.2", role="comparator")

    write_csv(OUT / "pla_properties.csv", fields, rows)

    source_fields = ["source_key", "authors", "year", "title", "journal_or_publisher", "doi_or_reference", "formulation", "source_locator", "source_url", "evidence_scope", "compatibility_decision", "local_evidence", "sha256"]
    write_csv(OUT / "property_sources.csv", source_fields, sources)

    uncertainty_fields = ["range_id", "parameter", "component_or_condition", "lower", "upper", "unit", "temperature_C", "formulation", "basis", "source_key", "range_type", "probability_model", "ANSYS_use", "status"]
    uncertainty = [
        dict(range_id="U-001",parameter="E",component_or_condition="Prusament printed horizontal",lower="2200",upper="2400",unit="MPa",temperature_C="not reported",formulation="Prusament PLA",basis="Supplier mean 2.3 ± 0.1 GPa",source_key="PrusamentTDS2022",range_type="reported mean interval",probability_model="none",ANSYS_use="cross-check only",status="not admitted as temperature-dependent viscoelastic law"),
        dict(range_id="U-002",parameter="E",component_or_condition="Prusament printed vertical xz",lower="2300",upper="2500",unit="MPa",temperature_C="not reported",formulation="Prusament PLA",basis="Supplier mean 2.4 ± 0.1 GPa",source_key="PrusamentTDS2022",range_type="reported mean interval",probability_model="none",ANSYS_use="cross-check only",status="not admitted as temperature-dependent viscoelastic law"),
    ]
    for idx, (nozzle, activation, pattern, timo) in enumerate(prestrain, 3):
        uncertainty.append(dict(range_id=f"U-{idx:03d}",parameter="ε₁₁^AM",component_or_condition=f"nozzle {nozzle} °C; activation {activation} °C",lower=f"{min(pattern,timo):.5f}",upper=f"{max(pattern,timo):.5f}",unit="1",temperature_C=str(activation),formulation="Prusament PLA",basis="Bracket between pattern-search and Timoshenko identifications in the same source",source_key="Chapuis2025",range_type="method bracket",probability_model="none",ANSYS_use="not admitted as bulk annealing-strain uncertainty",status="source-supported bracket; geometry-transfer unresolved"))
    missing = [
        ("ρ(T)","isotropic","kg m⁻³"),("k(T)","isotropic","W m⁻¹ K⁻¹"),("c_p(T)","isotropic","J kg⁻¹ K⁻¹"),
        ("E(T)","instantaneous/equilibrium interpretation","MPa"),("ν(T)","isotropic","1"),("α(T)","isotropic","µm m⁻¹ K⁻¹"),
        ("orthotropic elasticity","E₁,E₂,E₃,G₁₂,G₂₃,G₁₃,ν₁₂,ν₂₃,ν₁₃","mixed"),("orthotropic expansion","α₁,α₂,α₃","µm m⁻¹ K⁻¹"),
        ("crystallization kinetics","grade-specific isothermal/non-isothermal coefficients","mixed"),("bulk irreversible annealing strain","signed x,y,z law versus T and time","1"),
    ]
    next_id = len(uncertainty) + 1
    for parameter, component, unit in missing:
        uncertainty.append(dict(range_id=f"U-{next_id:03d}",parameter=parameter,component_or_condition=component,lower="",upper="",unit=unit,temperature_C="20–110 target domain",formulation="Prusament PLA",basis="No compatible published lower and upper bounds located in the Stage 4 evidence set",source_key="Chapuis2025; PrusamentTDS2022",range_type="unresolved evidence gap",probability_model="none",ANSYS_use="blocked",status="no bound invented"))
        next_id += 1
    write_csv(OUT / "uncertainty_ranges.csv", uncertainty_fields, uncertainty)

    fixture_fields = ["record_id", "fixture_material", "property_symbol", "property_name", "value", "unit", "temperature_C", "source_key", "doi_or_reference", "confidence_relevance", "how_used_in_ANSYS", "source_locator", "notes"]
    fixture_rows = []
    table = {
        20: {"ρ":(7910,"mass density","kg m⁻³"),"c_p":(456,"specific heat capacity","J kg⁻¹ K⁻¹"),"k":(16.2,"thermal conductivity","W m⁻¹ K⁻¹"),"α":(15.5,"coefficient of linear thermal expansion","µm m⁻¹ K⁻¹"),"E":(200,"Young modulus","GPa"),"ν":(0.29,"Poisson ratio","1")},
        100:{"ρ":(7876,"mass density","kg m⁻³"),"c_p":(494,"specific heat capacity","J kg⁻¹ K⁻¹"),"k":(16.6,"thermal conductivity","W m⁻¹ K⁻¹"),"α":(16.3,"coefficient of linear thermal expansion","µm m⁻¹ K⁻¹"),"E":(191.4,"Young modulus","GPa"),"ν":(0.285,"Poisson ratio","1")},
        200:{"ρ":(7840,"mass density","kg m⁻³"),"c_p":(532,"specific heat capacity","J kg⁻¹ K⁻¹"),"k":(17.45,"thermal conductivity","W m⁻¹ K⁻¹"),"α":(16.7,"coefficient of linear thermal expansion","µm m⁻¹ K⁻¹"),"E":(183.5,"Young modulus","GPa"),"ν":(0.289,"Poisson ratio","1")},
    }
    for temp, props in table.items():
        for symbol, (value, name, unit) in props.items():
            fixture_rows.append(dict(record_id=f"FIX-{len(fixture_rows)+1:03d}",fixture_material="AISI 304 stainless steel (candidate plate fixture)",property_symbol=symbol,property_name=name,value=str(value),unit=unit,temperature_C=str(temp),source_key="Meng2026",doi_or_reference="10.1038/s41598-026-45542-w",confidence_relevance="moderate; peer-reviewed compiled input table, product heat not yet specified",how_used_in_ANSYS="Tabulated isotropic thermal/structural fixture property; linear interpolation across temperature",source_locator="Table 1",notes="20, 100 and 200 °C rows bracket the planned 20–110 °C domain; no extrapolation required"))
    write_csv(OUT / "fixture_properties.csv", fixture_fields, fixture_rows)

    evidence_paths = sorted((ROOT / "literature/evidence/stage_04").iterdir())
    outputs = [OUT / "pla_properties.csv", OUT / "property_sources.csv", OUT / "uncertainty_ranges.csv", OUT / "fixture_properties.csv"]
    manifest = {
        "stage": 4,
        "date": "2026-09-12",
        "method": "manual source transcription plus deterministic calculations in scripts/build_material_database.py",
        "script": {"path": "scripts/build_material_database.py", "sha256": sha256(Path(__file__))},
        "evidence": [{"path": str(p.relative_to(ROOT)).replace("\\", "/"), "sha256": sha256(p), "bytes": p.stat().st_size} for p in evidence_paths if p.is_file()],
        "outputs": [{"path": str(p.relative_to(ROOT)).replace("\\", "/"), "sha256": sha256(p), "rows": sum(1 for _ in p.open(encoding="utf-8-sig")) - 1} for p in outputs],
        "calculation_checks": {"Prusament_E0_MPa": round(e_inst, 3), "sum_normalized_branch_fractions": sum(k / e_inst for k, _ in branches), "long_term_fraction": k0 / e_inst},
        "limitations": ["No PLA formulations were numerically merged.", "No probability distributions were assigned.", "No ANSYS material card is admitted for production runs because compatible Prusament thermal functions and bulk irreversible strain remain missing."],
    }
    (OUT / "build_manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {len(rows)} PLA property rows, {len(sources)} source rows, {len(uncertainty)} uncertainty rows, and {len(fixture_rows)} fixture rows")


if __name__ == "__main__":
    main()

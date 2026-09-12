"""Validate the Stage 4 material database without treating it as solver evidence."""
from __future__ import annotations

from pathlib import Path
import csv
import hashlib
import json
import re


ROOT = Path(__file__).resolve().parents[1]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_csv(path: str) -> list[dict[str, str]]:
    with (ROOT / path).open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    checks: list[dict[str, str]] = []

    def check(name: str, condition: bool) -> None:
        assert condition, name
        checks.append({"check": name, "status": "pass"})

    pla = read_csv("material/pla_properties.csv")
    sources = read_csv("material/property_sources.csv")
    uncertainty = read_csv("material/uncertainty_ranges.csv")
    fixture = read_csv("material/fixture_properties.csv")
    manifest = json.loads((ROOT / "material/build_manifest.json").read_text(encoding="utf-8"))

    check("Expected record counts", (len(pla), len(sources), len(uncertainty), len(fixture)) == (96, 11, 16, 18))
    required = ["value", "unit", "temperature_C", "source_key", "doi_or_reference", "PLA_formulation", "confidence_relevance", "how_used_in_ANSYS", "source_locator"]
    check("Every PLA number has complete provenance fields", all(all(row[field] for field in required) for row in pla))
    check("Every fixture number has complete provenance fields", all(all(row[field] for field in ["value", "unit", "temperature_C", "source_key", "doi_or_reference", "confidence_relevance", "how_used_in_ANSYS", "source_locator"]) for row in fixture))
    check("Property source keys are unique", len({row["source_key"] for row in sources}) == len(sources))
    check("Every property record resolves to a source", {row["source_key"] for row in pla} <= {row["source_key"] for row in sources})
    check("Every source has an exact locator", all(row["source_locator"] for row in sources))
    check("Every source evidence file exists", all((ROOT / row["local_evidence"]).is_file() for row in sources))
    check("Every source evidence hash matches", all(digest(ROOT / row["local_evidence"]) == row["sha256"] for row in sources))
    check("Every stored source hash is SHA-256", all(re.fullmatch(r"[0-9a-f]{64}", row["sha256"]) for row in sources))

    prony_k = [row for row in pla if row["property_symbol"] == "kᵢ"]
    prony_t = [row for row in pla if row["property_symbol"] == "τᵢ"]
    check("Prusament spectrum contains 23 modulus branches", len(prony_k) == 23)
    check("Prusament spectrum contains 23 relaxation times", len(prony_t) == 23)
    check("Prony branch identifiers match", {row["component"] for row in prony_k} == {row["component"] for row in prony_t})
    equilibrium = float(next(row["value"] for row in pla if row["property_symbol"] == "E_∞"))
    instantaneous = float(next(row["value"] for row in pla if row["property_symbol"] == "E_0"))
    check("Instantaneous modulus is reproducible arithmetic", abs(equilibrium + sum(float(row["value"]) for row in prony_k) - instantaneous) < 1e-9)
    check("Recorded instantaneous modulus is 1691.594 MPa", instantaneous == 1691.594)
    check("Normalized branch fractions and long-term fraction sum to one", abs(manifest["calculation_checks"]["sum_normalized_branch_fractions"] + manifest["calculation_checks"]["long_term_fraction"] - 1.0) < 1e-14)
    check("Reference formulation is named", all(row["PLA_formulation"] for row in pla))
    check("No comparator formulation is admitted", all(row["compatibility_status"] != "admissible_within_source_domain" for row in pla if row["dataset_role"] == "comparator"))
    check("All unresolved bounds are blank", all(row["lower"] == row["upper"] == "" for row in uncertainty if row["range_type"] == "unresolved evidence gap"))
    check("All unresolved bounds say no bound invented", all(row["status"] == "no bound invented" for row in uncertainty if row["range_type"] == "unresolved evidence gap"))
    check("No probability distribution was assigned", all(row["probability_model"] == "none" for row in uncertainty))
    check("Fixture material is consistently AISI 304", {row["fixture_material"] for row in fixture} == {"AISI 304 stainless steel (candidate plate fixture)"})
    check("Fixture temperatures bracket 20–110 °C", {row["temperature_C"] for row in fixture} == {"20", "100", "200"})
    check("Fixture table is complete at every temperature", all({row["property_symbol"] for row in fixture if row["temperature_C"] == temperature} == {"ρ", "c_p", "k", "α", "E", "ν"} for temperature in {"20", "100", "200"}))
    check("Fixture values come from one identified source", {row["source_key"] for row in fixture} == {"Meng2026"})
    check("Manifest identifies Stage 4", manifest["stage"] == 4)
    check("Generator hash matches manifest", digest(ROOT / manifest["script"]["path"]) == manifest["script"]["sha256"])
    check("Material output hashes match manifest", all(digest(ROOT / item["path"]) == item["sha256"] for item in manifest["outputs"]))
    check("Stage 4 evidence hashes match manifest", all(digest(ROOT / item["path"]) == item["sha256"] for item in manifest["evidence"]))
    check("Manifest states that no production material card is admitted", any("No ANSYS material card is admitted" in item for item in manifest["limitations"]))

    report = {
        "stage": 4,
        "date": "2026-09-12",
        "checks": checks,
        "count": len(checks),
        "material_manifest_sha256": digest(ROOT / "material/build_manifest.json"),
        "scope": "Source, transcription, compatibility and arithmetic checks only; no ANSYS or physical validation evidence.",
    }
    (ROOT / "docs/stage_04_material_integrity.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"{len(checks)} material integrity checks passed")


if __name__ == "__main__":
    main()

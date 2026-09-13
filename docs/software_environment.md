# Software environment and execution boundary

Inspection date: **13 September 2026**, Asia/Calcutta. This record distinguishes
files present on disk, a successful executable invocation, and an untested GUI
or optional-product entitlement.

## Host

- Windows 11 Home Single Language, build 10.0.26200, 64-bit.
- ASUS TUF Gaming A15 FA507NUR.
- AMD Ryzen 7 7435HS: 8 physical cores, 16 logical processors, reported maximum
  clock 3100 MHz.
- Installed physical memory: 16,989,728,768 bytes (15.82 GiB). Windows reported
  16,591,532 KiB visible and 5,189,304 KiB free at inspection; free memory is a
  transient observation, not a reproducible capacity.
- The Student product page limits Ansys HPC to four CPU cores. Production launch
  settings will therefore request no more than four cores even though the host
  exposes 16 logical processors.

## Ansys installation

The root is `C:\Program Files\ANSYS Inc\ANSYS Student\v261`. Environment
variables `AWP_ROOT261` and `ANSYS261_DIR` point to this installation. Local
`builddate.txt` identifies **Ansys 2026 R1**, unified package
**R261RC2P01**, created 202602040408P01. Solver metadata reports
`ANSYS (R) ANS_ADMIN Release 2026 R1 20260202`.

Component | Present on disk | Invocation status | License/availability conclusion
Workbench | `RunWB2.exe`, product 26.1, file 26.01.00.2026020218 | Not launched in Stage 6 | Installed; GUI entitlement not separately checked
Mechanical | `AnsysWBU.exe`, product 26.1, file 26.2026.13.1 | Not launched in Stage 6 | Installed; MAPDL checked out the Student Mechanical product, but Mechanical GUI was not separately exercised
Transient Thermal | Workbench template `Transient Thermal (ANSYS)` | No model created or solved | Template installed; case-level availability remains to be confirmed
Transient Structural | Workbench template `Transient Structural (ANSYS)` | No model created or solved | Template installed; case-level availability remains to be confirmed
Static Structural | Workbench template `Static Structural (ANSYS)` | No model created or solved | Template installed; case-level availability remains to be confirmed
Mechanical APDL | `ANSYS261.exe` | Zero-analysis batch smoke test exited 0 | Confirmed usable; banner `2026 R1`, build `26.1`, update `20260202`, product `Ansys Mechanical Enterprise Academic Student`
DesignXplorer | add-in configuration and Workbench instruction files | Not launched | Installed files only; entitlement and workflow not confirmed
optiSLang | `optislang.exe`, 26.1.0 revision 1878 | Help attempt opened a process and was terminated; no project run | Installed; license entitlement not confirmed
PyMechanical | No `ansys-mechanical-core`, `ansys-mapdl-core`, or `ansys-api-mechanical` package in system Python; no matching installed package tree found | Not available | **PyMechanical is not installed** in the project/system Python environment

The successful MAPDL probe used one core and the immutable input
`ansys/apdl/environment_smoke.dat`. It intentionally issued only `/STATUS` and
`/EXIT,NOSAVE`; it created no nodes, elements, geometry, load, solution, or
numerical research result. Raw stdout, error/log files, and SHA-256 hashes are in
`simulation/runs/stage06_mapdl_smoke/`. A generic `lmutil lmstat -a` call could
not locate a conventional license file; this does not override the actual
successful embedded Student checkout reported by MAPDL.

## Student restrictions

The official Ansys Student 2026 R1 download page states that the built-in license
is valid through 31 March 2027, limits structural physics to **128,000
nodes/elements**, disallows geometry export, and supports up to four CPU cores for
HPC solutions. The same page lists Workbench, Mechanical and optiSLang in the
bundle and lists Static Structural, Transient Structural, and Transient Thermal
among Workbench analysis systems. Source: Ansys, “Ansys Student — Free Software
Download,” accessed 13 September 2026,
https://www.ansys.com/en-in/academic/students/ansys-student.

The phrase “128,000 nodes/elements” is reproduced as Ansys states it; the future
mesh-admission check must count solver-generated contact and auxiliary entities
as well as the user-visible base mesh. No mesh has yet been created.

## Python and reproducibility

The Ansys installation contains CPython 3.10.19 runtimes. The system command used
for repository checks is Python 3.14.3. `environment.yml` fixes the reproducible
project target to Python 3.10 so it can be aligned with Ansys-side automation;
the PDF dependencies remain exactly pinned in `requirements.txt`. The core
runner uses only the Python standard library and direct MAPDL batch execution.

`ansys/run_case.py` requires explicit temperature, hold time, fixture gap, and
material identity for a production case. It refuses a production execution if
any admission gate is false, and no production APDL deck exists. Result
registration likewise rejects an empty file or a row without case, time,
quantity, value, unit, location, and originating solver file. This architecture
parameterizes the intended workflow without implying that missing physics or
properties have been solved.


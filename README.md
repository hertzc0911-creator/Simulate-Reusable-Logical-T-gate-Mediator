# 3D color-code and logical-T simulations

This repository contains two independent simulation systems. They share the same notebook-facing organization, but they do not import code from each other.

## Repository layout

```text
Github/
├── non_circuit_library/              # Shared code for the non-circuit-level system
│   ├── configs/                      # Distance-specific stabilizers and geometry
│   ├── threshold.py                  # Shared 3D threshold measurement methods
│   ├── figure.py                     # Shared logical-T figure methods
│   └── reuse.py                      # Shared repeated-use logical-T methods
├── 3D_color_Threshold/               # Non-circuit-level memory/threshold notebooks
├── Logical_T_Figure/                 # Non-circuit-level logical-T notebooks
├── Logical_T_Figure_reuse/           # Repeated-use logical-T notebooks
└── Circuit-level/                    # Fully independent circuit-level system
    ├── circuit_library/              # Circuit-level stabilizers, schedules, and methods
    ├── Circuit-level_3D_code_server/ # Circuit-level memory notebooks
    └── Circuit-level_T_gate_server/  # Circuit-level logical-T notebooks
```

## System 1: non-circuit-level simulations

The notebooks in `3D_color_Threshold`, `Logical_T_Figure`, and `Logical_T_Figure_reuse` use the root-level `non_circuit_library` package.

- `threshold.py` is shared by the d3, d5, and d7 threshold notebooks.
- `figure.py` is shared by the d3, d5, and d7 logical-T figure notebooks.
- `reuse.py` is shared by every repeated-use notebook, including the 5S, 10S, and 20S variants.
- Distance-specific stabilizers and geometry are stored in `non_circuit_library/configs`.
- Every notebook keeps its own complete `circuit_generate` and `generate_tasks` definitions so that its concrete circuit remains visible when the notebook is opened.

Each notebook explicitly imports the stabilizers and reusable methods it uses:

```python
from non_circuit_library import figure as _circuit_library

_circuit_library.configure(5)

from non_circuit_library.figure import (
    stabilizers_k_z,
    stabilizers_k_x,
    stabilizers_k_z_enlarged,
    Stabilizers_measurement_general,
    Stabilizers_measurement_merged,
)
```

To install this system from the repository root:

```bash
python -m pip install -e .
```

## System 2: circuit-level simulations

The `Circuit-level` directory is a self-contained project. Its notebooks import only `Circuit-level/circuit_library`, which contains the flag SEQUENCE schedules and circuit-level measurement implementations.

To install it independently:

```bash
cd Circuit-level
python -m pip install -e .
```

The package names are intentionally different:

- Non-circuit-level notebooks import `non_circuit_library`.
- Circuit-level notebooks import `circuit_library`.

Neither package imports the other.

## Tests

From the repository root, test the non-circuit-level system with:

```bash
python -m unittest discover -s tests
```

Test the circuit-level system separately with:

```bash
cd Circuit-level
python -m unittest discover -s tests
```

The codes are built with the help of gpt 5.5

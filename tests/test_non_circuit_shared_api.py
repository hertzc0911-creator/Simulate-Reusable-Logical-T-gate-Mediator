import ast
import json
from pathlib import Path
import unittest

from non_circuit_library import figure, reuse, threshold


ROOT = Path(__file__).resolve().parents[1]


class NonCircuitSharedApiTest(unittest.TestCase):
    def test_threshold_distances_share_measurement_implementation(self):
        implementations = [
            threshold.configure(distance)["Stabilizers_measurement_general"]
            for distance in (3, 5, 7)
        ]
        self.assertIs(implementations[0], implementations[1])
        self.assertIs(implementations[1], implementations[2])

    def test_figure_distances_share_measurement_implementations(self):
        names = (
            "Stabilizers_measurement_general",
            "Stabilizers_measurement_merged",
            "Stabilizers_measurement_merged_string",
        )
        implementations = [
            tuple(figure.configure(distance)[name] for name in names)
            for distance in (3, 5, 7)
        ]
        self.assertEqual(implementations[0], implementations[1])
        self.assertEqual(implementations[1], implementations[2])

    def test_reuse_distances_share_measurement_implementations(self):
        names = (
            "Stabilizers_measurement_general",
            "Stabilizers_measurement_merged",
            "Stabilizers_measurement_merged_string",
        )
        implementations = [
            tuple(reuse.configure(distance)[name] for name in names)
            for distance in (3, 5, 7)
        ]
        self.assertEqual(implementations[0], implementations[1])
        self.assertEqual(implementations[1], implementations[2])

    def test_notebooks_keep_local_circuit_builders_and_explicit_imports(self):
        folders = (
            "3D_color_Threshold",
            "Logical_T_Figure",
            "Logical_T_Figure_reuse",
        )
        for folder in folders:
            for path in (ROOT / folder).glob("*.ipynb"):
                notebook = json.loads(path.read_text(encoding="utf-8"))
                source = "\n".join(
                    "".join(cell.get("source", []))
                    for cell in notebook["cells"]
                    if cell.get("cell_type") == "code"
                )
                tree = ast.parse(source)
                functions = {
                    node.name
                    for node in ast.walk(tree)
                    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
                }
                self.assertIn("circuit_generate", functions, path)
                self.assertIn("generate_tasks", functions, path)
                self.assertIn("from non_circuit_library.", source, path)
                self.assertNotIn("globals().update", source, path)

    def test_two_systems_have_no_cross_imports(self):
        non_circuit_sources = [
            path.read_text(encoding="utf-8")
            for path in (ROOT / "non_circuit_library").rglob("*.py")
        ]
        circuit_sources = [
            path.read_text(encoding="utf-8")
            for path in (ROOT / "Circuit-level" / "circuit_library").rglob("*.py")
        ]
        self.assertFalse(any("from circuit_library" in source for source in non_circuit_sources))
        self.assertFalse(any("import circuit_library" in source for source in non_circuit_sources))
        self.assertFalse(any("non_circuit_library" in source for source in circuit_sources))


if __name__ == "__main__":
    unittest.main()

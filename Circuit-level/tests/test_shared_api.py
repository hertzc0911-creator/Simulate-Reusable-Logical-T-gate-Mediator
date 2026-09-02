import unittest

from circuit_library import logical_t, memory


class SharedApiTest(unittest.TestCase):
    def test_logical_t_distances_share_measurement_implementations(self):
        names = (
            "Stabilizers_measurement_general",
            "Stabilizers_measurement_merged",
            "Stabilizers_measurement_merged_string",
        )
        implementations = []
        for distance in (3, 5, 7):
            exports = logical_t.configure(distance)
            implementations.append(tuple(exports[name] for name in names))
        self.assertEqual(implementations[0], implementations[1])
        self.assertEqual(implementations[1], implementations[2])

    def test_memory_distances_share_measurement_implementation(self):
        implementations = []
        for distance in (3, 5, 7):
            exports = memory.configure(distance)
            implementations.append(exports["Stabilizers_measurement_general"])
        self.assertIs(implementations[0], implementations[1])
        self.assertIs(implementations[1], implementations[2])

    def test_each_distance_has_its_own_stabilizer_configuration(self):
        logical_counts = []
        memory_counts = []
        for distance in (3, 5, 7):
            logical_counts.append(len(logical_t.configure(distance)["stabilizers_general"]))
            memory_counts.append(len(memory.configure(distance)["stabilizers_general"]))
        self.assertEqual(logical_counts, [20, 82, 210])
        self.assertEqual(memory_counts, [14, 64, 174])


if __name__ == "__main__":
    unittest.main()

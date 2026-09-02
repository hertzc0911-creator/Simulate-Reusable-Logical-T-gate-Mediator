import time
from pathlib import Path

import sinter


_CIRCUIT_GENERATOR = None
_TARGET_TASKS = None


def configure_experiments(circuit_generator):
    global _CIRCUIT_GENERATOR
    _CIRCUIT_GENERATOR = circuit_generator


def set_target_tasks(target_tasks):
    global _TARGET_TASKS
    _TARGET_TASKS = target_tasks


def benchmark_worker_count(num_workers, max_shots=200):
    if _TARGET_TASKS is None:
        raise RuntimeError("Call set_target_tasks before benchmarking worker counts.")

    csv_path = Path(
        f"benchmark_p2e-4_{num_workers}workers_{max_shots}shots.csv"
    )
    if csv_path.exists():
        raise FileExistsError(
            f"{csv_path} already exists; remove or rename it before benchmarking."
        )

    start = time.perf_counter()
    stats = sinter.collect(
        num_workers=num_workers,
        max_shots=max_shots,
        max_errors=None,
        start_batch_size=1,
        max_batch_size=50,
        max_batch_seconds=60,
        print_progress=True,
        tasks=_TARGET_TASKS,
        decoders=["hypergraph_union_find"],
        save_resume_filepath=csv_path,
    )
    elapsed = time.perf_counter() - start
    total_shots = sum(stat.shots for stat in stats)
    result = {
        "workers": num_workers,
        "shots": total_shots,
        "elapsed_seconds": elapsed,
        "wall_rate": total_shots / elapsed,
        "csv": str(csv_path.resolve()),
    }
    print()
    print(f"===== {num_workers} worker benchmark =====")
    print(f"shots: {total_shots}")
    print(f"wall time: {elapsed / 60:.2f} minutes")
    print(f"wall rate: {total_shots / elapsed:.4f} shots/second")
    print(f"CSV: {csv_path.resolve()}")
    return result


def generate_d7_task(error_rate):
    if _CIRCUIT_GENERATOR is None:
        raise RuntimeError("Call configure_experiments before generating tasks.")
    print(f"Building the distance-7 circuit at p={error_rate:g}", flush=True)
    yield sinter.Task(
        circuit=_CIRCUIT_GENERATOR(error_rate, error_rate),
        json_metadata={"p": error_rate},
    )


def show_samples(title, samples):
    print()
    print("=" * 80)
    print(title)
    print("=" * 80)
    for sample in samples:
        error_rate = (
            sample.errors / sample.shots
            if sample.shots > 0
            else float("nan")
        )
        print(f"p: {float(sample.json_metadata['p']):g}")
        print(f"cumulative shots: {sample.shots:,}")
        print(f"cumulative errors: {sample.errors:,}")
        print(f"logical error rate: {error_rate:.6e}")
        print()
    print("=" * 80)

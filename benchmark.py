import timeit
import time
import concurrent.futures
import pydn2
# import idna
import idna.compat

def bench_idna():
    # External idna package: returns bytes; decode to get a str.
    return idna.encode("i♥.com", uts46=False, std3_rules=False, transitional=True).decode("ascii")

def bench_pydn2():
    # pydn2.to_ascii_8z implements IDNA2008/TR46 conversion.
    return pydn2.to_ascii_8z("I♥.com", pydn2.IDN2_NFC_INPUT | pydn2.IDN2_TRANSITIONAL)

def bench_builtin():
    # Python's built-in codec uses the older IDNA2003 standard.
    return "I♥.com".encode("idna").decode("ascii")

def single_thread_bench():
    iterations = 1000000
    t_pydn2 = timeit.timeit("bench_pydn2()", setup="from __main__ import bench_pydn2", number=iterations)
    t_builtin = timeit.timeit("bench_builtin()", setup="from __main__ import bench_builtin", number=iterations)
    # t_idna = timeit.timeit("bench_idna()", setup="from __main__ import bench_idna", number=iterations)
    print("Single-thread benchmark:")
    print(f"  pydn2   (IDNA2008/TR46) : {t_pydn2:.6f} sec for {iterations} iterations")
    print(f"  builtin (IDNA2003)      : {t_builtin:.6f} sec for {iterations} iterations")
    # print(f"  idna (external)         : {t_idna:.6f} sec for {iterations} iterations")

def threaded_bench(func, iterations, n_threads):
    def task(n):
        for _ in range(n):
            func()
    iters_per_thread = iterations // n_threads
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=n_threads) as executor:
        futures = [executor.submit(task, iters_per_thread) for _ in range(n_threads)]
        concurrent.futures.wait(futures)
    end = time.perf_counter()
    return end - start

def multi_thread_bench():
    iterations = 1000000
    n_threads = 8
    t_pydn2 = threaded_bench(bench_pydn2, iterations, n_threads)
    t_builtin = threaded_bench(bench_builtin, iterations, n_threads)
    # t_idna = threaded_bench(bench_idna, iterations, n_threads)
    print(f"\nMulti-thread benchmark (using {n_threads} threads):")
    print(f"  pydn2   (IDNA2008/TR46) : {t_pydn2:.6f} sec for {iterations} iterations")
    print(f"  builtin (IDNA2003)      : {t_builtin:.6f} sec for {iterations} iterations")
    # print(f"  idna (external)         : {t_idna:.6f} sec for {iterations} iterations")

if __name__ == "__main__":
    print("Conversion outputs:")
    print("  pydn2   :", bench_pydn2())
    print("  builtin :", bench_builtin())
    # print("  idna    :", bench_idna())
    single_thread_bench()
    multi_thread_bench()

# Performance Comparison Table

**Hardware:** NVIDIA GeForce RTX 3060

## Matrix Multiplication Performance Results

| Implementation | N=512 | N=1024 | N=2048 |
|----------------|-------|--------|--------|
| CPU (C)        | 0.196 sec | 1.374 sec | 57.895 sec |
| Naïve CUDA     | 0.853 ms | 2.707 ms | 21.349 ms |
| Optimized CUDA | 0.405 ms | 2.084 ms | 19.510 ms |
| cuBLAS         | 1.644 ms | 0.538 ms | 2.321 ms |

## Speedup (CPU time / GPU time)

| Matrix Size | Naïve CUDA Speedup | Optimized CUDA Speedup | cuBLAS Speedup |
|-------------|-------------------|------------------------|----------------|
| 512         | 230×              | 484×                   | 119×           |
| 1024        | 507×              | 660×                   | 2554×          |
| 2048        | 2714×             | 2970×                  | 24,941×        |

## Notes

- CPU time in seconds, GPU time in ms. Speedup: `CPU_time_seconds / (GPU_time_ms / 1000.0)`.

## How to reproduce

From repo root, build with `scripts\build_all.bat`, then run:

```bat
matrix_cpu.exe 512
matrix_cpu.exe 1024
matrix_cpu.exe 2048
matrix_gpu.exe 512
matrix_gpu.exe 1024
matrix_gpu.exe 2048
matrix_gpu_tiled.exe 512
matrix_gpu_tiled.exe 1024
matrix_gpu_tiled.exe 2048
matrix_cublas.exe 512
matrix_cublas.exe 1024
matrix_cublas.exe 2048
```

Or run all at once: `python scripts\run_matrix_tests.py`

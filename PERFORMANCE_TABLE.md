# Performance Comparison Table

## Matrix Multiplication Performance Results

| Implementation | N=512 | N=1024 | N=2048 | N=4096 |
|----------------|-------|--------|--------|--------|
| CPU (C)        | X sec | Y sec  | Z sec  | ...    |
| Naïve CUDA     | A ms  | B ms   | C ms   | ...    |
| Optimized CUDA | D ms  | E ms   | F ms   | ...    |
| cuBLAS         | G ms  | H ms   | I ms   | ...    |

## Speedup Calculation

Speedup = CPU time / GPU time

| Matrix Size | Naïve CUDA Speedup | Optimized CUDA Speedup | cuBLAS Speedup |
|-------------|-------------------|----------------------|----------------|
| 512         | ...               | ...                  | ...            |
| 1024        | ...               | ...                  | ...            |
| 2048        | ...               | ...                  | ...            |
| 4096        | ...               | ...                  | ...            |

## Notes

- CPU time in seconds, GPU time in ms. Speedup: `CPU_time_seconds / (GPU_time_ms / 1000.0)`.

## Commands

1. CPU:
   ```bash
   gcc matrix_cpu.c -o matrix_cpu.exe -O2
   ./matrix_cpu.exe 512
   ./matrix_cpu.exe 1024
   ./matrix_cpu.exe 2048
   ```

2. Naïve CUDA:
   ```bash
   nvcc matrix_gpu_compare.cu -o matrix_gpu_compare.exe -O2
   ./matrix_gpu_compare.exe 512 0
   ./matrix_gpu_compare.exe 1024 0
   ./matrix_gpu_compare.exe 2048 0
   ```

3. Tiled CUDA:
   ```bash
   ./matrix_gpu_compare.exe 512 1
   ./matrix_gpu_compare.exe 1024 1
   ./matrix_gpu_compare.exe 2048 1
   ```

4. cuBLAS:
   ```bash
   nvcc matrix_cublas.cu -o matrix_cublas.exe -O2 -lcublas
   ./matrix_cublas.exe 512
   ./matrix_cublas.exe 1024
   ./matrix_cublas.exe 2048
   ```

5. Speedup = CPU_time / GPU_time (convert GPU ms to seconds first).

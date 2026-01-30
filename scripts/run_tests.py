import os
import subprocess

script_dir = os.path.dirname(os.path.abspath(__file__))

# Matrix sizes
sizes = [512, 1024, 2048]

print("=== MATRIX MULTIPLICATION ===\n")

# CPU
print("--- CPU ---")
for s in sizes:
    subprocess.run(["matrix_cpu.exe", str(s)], cwd=script_dir)

# Naive CUDA
print("\n--- Naive CUDA ---")
for s in sizes:
    subprocess.run(["matrix_gpu_compare.exe", str(s), "0"], cwd=script_dir)

# Tiled CUDA
print("\n--- Tiled CUDA ---")
for s in sizes:
    subprocess.run(["matrix_gpu_compare.exe", str(s), "1"], cwd=script_dir)

# cuBLAS
print("\n--- cuBLAS ---")
for s in sizes:
    subprocess.run(["matrix_cublas.exe", str(s)], cwd=script_dir)

print("\n\n=== CONVOLUTION ===\n")

# Convolution tests
img_sizes = [256, 512, 1024]
filters = ["sobel_x", "gaussian", "sharpen"]

print("--- CPU Convolution ---")
for img in img_sizes:
    for filt in filters:
        subprocess.run(["convolution.exe", str(img), "3", filt], cwd=script_dir)

print("\n--- GPU Convolution ---")
for img in img_sizes:
    for filt in filters:
        subprocess.run(["convolution_gpu.exe", str(img), "3", filt], cwd=script_dir)

print("\nDone.")

import math

# 1. Menentukan parameter awal
a = 25
x = 26
h = x - a
exact_val = math.sqrt(x)

# 2. Menentukan koefisien deret Taylor orde 0 sampai 4
coeffs = [
    5.0,
    0.1,
    -0.001,
    0.00002,
    -0.0000005
]

# 3. Inisialisasi variabel
p_val = 0.0
min_order = None

print(f"Nilai eksak sqrt(26) = {exact_val:.10f}\n")

# 4. Menghitung nilai hampiran dan galat absolut
for k in range(len(coeffs)):
    p_val += coeffs[k] * (h ** k)

    err = abs(exact_val - p_val)

    print(
        f"Orde P_{k}(26) = {p_val:.7f} | "
        f"Galat Absolut = {err:.10f}"
    )

    # Memeriksa orde pertama dengan galat kurang dari 10^-6
    if err < 1e-6 and min_order is None:
        min_order = k

# 5. Menampilkan orde minimal
if min_order is not None:
    print(
        f"\nOrde minimal agar galat < 10^-6 "
        f"adalah: Orde {min_order}"
    )
else:
    print("\nTidak ada orde yang memenuhi kriteria galat.")

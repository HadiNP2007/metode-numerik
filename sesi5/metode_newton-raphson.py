
import math

def f(t):
    return 40*t - 300 - 400 * math.exp(-0.3*t)

def df(t):
    return 40 + 120 * math.exp(-0.3*t)

t = 8.0
toleransi = 0.0001
iterasi = 0

print("METODE NEWTON-RAPHSON")
print("=" * 90)
print(f"{'Iterasi':<10}{'t_n':<15}{'f(t_n)':<15}{'f turunan':<15}{'t_n+1':<15}{'Delta':<15}")
print("=" * 90)

while True:
    ft = f(t)
    dft = df(t)

    t_baru = t - (ft / dft)
    delta = abs(t_baru - t)

    print(
        f"{iterasi:<10}"
        f"{t:<15.6f}"
        f"{ft:<15.6f}"
        f"{dft:<15.6f}"
        f"{t_baru:<15.6f}"
        f"{delta:<15.6f}"
    )

    iterasi += 1
    t = t_baru

    if delta < toleransi:
        break

print("=" * 90)
print(f"Waktu memori penuh : {t:.6f} jam")
print(f"Jumlah iterasi     : {iterasi}")
print("Rekomendasi restart: Setiap 8 jam")


# Concrete compression check (very basic)
# Units:
# N is kN, A in mm^2, strengths in MPa (N/mm^2)
# Stress: sigma = N / A -> result is Mpa
def concrete_compression_check(N_kn, A_mm2, fcd_MPa):
  sigma_MPa = (N_kN * 1000) / A_mm2 #kN -> N, then N/mm^2 = MPa
is_ok = sigma_MPa <= fcd_MPa
print(''=== Concrete Compression Check ==='')
print(f''N = {N_kn:.2f} kn'')
print(f''A = {A_mm2:.0f} mm^2'')
print(f"sigma = {sigma_MPa:.3f} MPa")
print(f"fcd = {fcd_MPa:.3f} MPa")
print("Result:", "OK ✅" if is_ok else "NG ❌ (Not OK)")
return sigma_MPa, is_ok
# Example values (you can change these)
N_kN_example = 800      # axial load in kN
A_mm2_example = 300000  # area in mm^2 (e.g., 300x1000 mm)
fcd_MPa_example = 17    # design compressive strength in MPa

concrete_compression_check(N_kN_example, A_mm2_example, fcd_MPa_example)

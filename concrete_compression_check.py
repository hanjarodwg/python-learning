# Concrete compression check (very basic)
# Units:
# N is kN, A in mm^2, strengths in MPa (N/mm^2)
# Stress: sigma = N / A -> result is MPa

def concrete_compression_check(N_kN, A_mm2, fcd_MPa):
    sigma_MPa = (N_kN * 1000) / A_mm2  # kN -> N, then N/mm^2 = MPa
    is_ok = sigma_MPa <= fcd_MPa

    print("=== Concrete Compression Check ===")
    print(f"N = {N_kN:.2f} kN")
    print(f"A = {A_mm2:.0f} mm^2")
    print(f"sigma = {sigma_MPa:.3f} MPa")
    print(f"fcd = {fcd_MPa:.3f} MPa")
    print("Result:", "OK ✅" if is_ok else "NG ❌ (Not OK)")

    return sigma_MPa, is_ok


# Example values
N_kN_example = 900        # axial load in kN
A_mm2_example = 150000   # 30 x 50 cm column
fcd_MPa_example = 17     # C25/30 design strength

concrete_compression_check(
    N_kN_example,
    A_mm2_example,
    fcd_MPa_example
)

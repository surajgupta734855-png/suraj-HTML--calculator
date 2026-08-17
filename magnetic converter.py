import math



MAGNETIC_QUANTITIES = {
    "1": {
        "name": "Magnetic induction (B)",
        "si_unit": "Tesla (T)",
        "cgs_unit": "Gauss (G)",
        "factor": 1e4,  # 1 T = 10^4 G
        "formula_si_to_cgs": lambda si: si * 1e4,
    },
    "2": {
        "name": "Magnetic field strength (H)",
        "si_unit": "A m⁻¹",
        "cgs_unit": "Oersted (Oe)",
        "factor": 4 * math.pi * 1e-3,  # 1 A m⁻¹ = 4π × 10⁻³ Oe
        "formula_si_to_cgs": lambda si: si * (4 * math.pi * 1e-3),
    },
    "3": {
        "name": "Magnetization (M)",
        "si_unit": "A m⁻¹",
        "cgs_unit": "emu cm⁻³",
        "factor": 1e-3,  # 1 A m⁻¹ = 10⁻³ emu cm⁻³[cite: 1]
        "formula_si_to_cgs": lambda si: si * 1e-3,
    },
    "4": {
        "name": "Magnetic polarization (J)",
        "si_unit": "Tesla (T)",
        "cgs_unit": "Gauss (G) / (emu cm⁻³)",
        "factor": 1e4,  # 1 T = 10^4 G = 10^4 / 4π emu cm⁻³[cite: 1]
        "formula_si_to_cgs": lambda si: si * 1e4,
    },
    "5": {
        "name": "Magnetic moment (m)",
        "si_unit": "A m²",
        "cgs_unit": "emu (G cm³)",
        "factor": 1e3,  # 1 A m² = 10³ emu[cite: 1]
        "formula_si_to_cgs": lambda si: si * 1e3,
    },
    "6": {
        "name": "Magnetic moment per unit mass (σ)",
        "si_unit": "A m² kg⁻¹",
        "cgs_unit": "emu g⁻¹",
        "factor": 1.0,  # 1 A m² kg⁻¹ = 1 emu g⁻¹[cite: 1]
        "formula_si_to_cgs": lambda si: si * 1.0,
    },
    "7": {
        "name": "Volume magnetic susceptibility (χ)",
        "si_unit": "dimensionless",
        "cgs_unit": "dimensionless",
        "factor": 1 / (4 * math.pi),  # 1 (SI) = 1/(4π) (CGS)[cite: 1]
        "formula_si_to_cgs": lambda si: si / (4 * math.pi),
    },
    "8": {
        "name": "Mass magnetic susceptibility (χ_mass)",
        "si_unit": "m³ kg⁻¹",
        "cgs_unit": "emu g⁻¹ (cm³ g⁻¹)",
        "factor": 1e3 / (4 * math.pi),  # 1 m³ kg⁻¹ = 10³/4π emu g⁻¹[cite: 1]
        "formula_si_to_cgs": lambda si: si * (1e3 / (4 * math.pi)),
    },
    "9": {
        "name": "Molar magnetic susceptibility (χ_m) [CORRECTED]",
        "si_unit": "m³ mol⁻¹",
        "cgs_unit": "emu mol⁻¹",
        "factor": 1e6 / (4 * math.pi),  # 1 m³ mol⁻¹ = 10⁶/4π emu mol⁻¹[cite: 1]
        "formula_si_to_cgs": lambda si: si * (1e6 / (4 * math.pi)),
    },
    "10": {
        "name": "Magnetic permeability (μ)",
        "si_unit": "H m⁻¹",
        "cgs_unit": "G Oe⁻¹",
        "factor": 1e7 / (4 * math.pi),  # 1 H m⁻¹ = 10⁷/4π G Oe⁻¹[cite: 1]
        "formula_si_to_cgs": lambda si: si * (1e7 / (4 * math.pi)),
    },
    "11": {
        "name": "Magnetic flux (Φ)",
        "si_unit": "Weber (Wb)",
        "cgs_unit": "Maxwell (Mx)",
        "factor": 1e8,  # 1 Wb = 10⁸ Mx[cite: 1]
        "formula_si_to_cgs": lambda si: si * 1e8,
    },
    "12": {
        "name": "Magnetic scalar potential / MMF (φ, F)",
        "si_unit": "Ampere (A)",
        "cgs_unit": "Gilbert (Gb)",
        "factor": (4 * math.pi) / 10,  # 1 A = 4π/10 Gilbert[cite: 1]
        "formula_si_to_cgs": lambda si: si * ((4 * math.pi) / 10),
    },
    "13": {
        "name": "Magnetic vector potential (A)",
        "si_unit": "Wb m⁻¹",
        "cgs_unit": "emu cm⁻¹ (G cm)",
        "factor": 1e6,  # 1 Wb m⁻¹ = 10⁶ emu cm⁻¹[cite: 1]
        "formula_si_to_cgs": lambda si: si * 1e6,
    },
    "14": {
        "name": "Magnetic pole strength (p)",
        "si_unit": "A m",
        "cgs_unit": "emu (G cm²)",
        "factor": 10.0,  # 1 A m = 10 emu[cite: 1]
        "formula_si_to_cgs": lambda si: si * 10.0,
    },
    "15": {
        "name": "Demagnetizing factor (N)",
        "si_unit": "dimensionless",
        "cgs_unit": "dimensionless",
        "factor": 4 * math.pi,  # 1 (SI) = 4π (CGS)[cite: 1]
        "formula_si_to_cgs": lambda si: si * (4 * math.pi),
    },
    "16": {
        "name": "Magnetostriction constant (λ)",
        "si_unit": "dimensionless",
        "cgs_unit": "dimensionless",
        "factor": 1.0,  # 1 (SI) = 1 (CGS)[cite: 1]
        "formula_si_to_cgs": lambda si: si * 1.0,
    },
    "17": {
        "name": "Anisotropy constant (K, K1, Ku)",
        "si_unit": "J m⁻³",
        "cgs_unit": "erg cm⁻³",
        "factor": 10.0,  # 1 J m⁻³ = 10 erg cm⁻³[cite: 1]
        "formula_si_to_cgs": lambda si: si * 10.0,
    },
    "18": {
        "name": "Magnetostatic energy (Em)",
        "si_unit": "J m⁻³",
        "cgs_unit": "erg cm⁻³",
        "factor": 10.0,  # 1 J m⁻³ = 10 erg cm⁻³[cite: 1]
        "formula_si_to_cgs": lambda si: si * 10.0,
    },
    "19": {
        "name": "Energy product ((BH)max)",
        "si_unit": "J m⁻³",
        "cgs_unit": "erg cm⁻³",
        "factor": 10.0,  # 1 J m⁻³ = 10 erg cm⁻³[cite: 1]
        "formula_si_to_cgs": lambda si: si * 10.0,
    },
}


def convert_si_to_cgs(key: str, value: float) -> float:
    """Converts a given value from SI unit to CGS unit[cite: 1]."""
    item = MAGNETIC_QUANTITIES[key]
    return item["formula_si_to_cgs"](value)


def convert_cgs_to_si(key: str, value: float) -> float:
    """Converts a given value from CGS unit to SI unit[cite: 1]."""
    item = MAGNETIC_QUANTITIES[key]
    return value / item["factor"]


def display_menu():
    print("=" * 65)
    print("      SU_PHYHBTU: SI ↔ CGS Magnetic Quantity Converter")
    print("=" * 65)
    for key, item in MAGNETIC_QUANTITIES.items():
        print(f"[{key}] {item['name']} ({item['si_unit']} ↔ {item['cgs_unit']})")
    print("=" * 65)


if __name__ == "__main__":
    display_menu()
    choice = input("Enter quantity number (1-19): ").strip()

    if choice in MAGNETIC_QUANTITIES:
        q = MAGNETIC_QUANTITIES[choice]
        direction = input(
            "Select direction -> [1] SI to CGS | [2] CGS to SI: "
        ).strip()
        val = float(input(f"Enter value: "))

        if direction == "1":
            res = convert_si_to_cgs(choice, val)
            print(f"\nResult: {val:e} {q['si_unit']} = {res:e} {q['cgs_unit']}")
        elif direction == "2":
            res = convert_cgs_to_si(choice, val)
            print(f"\nResult: {val:e} {q['cgs_unit']} = {res:e} {q['si_unit']}")
        else:
            print("Invalid direction selected.")
    else:
        print("Invalid selection.")

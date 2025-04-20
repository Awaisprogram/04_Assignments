"""
The program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula

Formula : e = mc**2
"""

C : int = 299792458

def main():
  mass_in_kg = float(input("Enter the mass in kg: "))
  energy_in_joule = float(mass_in_kg * C**2)

  print(f"🧪 E = m × c²")
  print(f"📦 Mass (m): {mass_in_kg}kg")
  print(f"⚡ Speed of light (c): {C}m/s")

  print(f"🔋 Energy (E): {energy_in_joule:.2e} joules of energy")


if __name__ == '__main__':
    main()
from Kendaraan import Vehicle, Car, Truck


print("=== Contoh Data Benar ===")

car1 = Car("Toyota", "Corolla", 4)
truck1 = Truck("Ford", "F-150", 1000)

car1.drive()
car1.honk()

truck1.drive()
truck1.load(800)





print("\n=== Contoh Error: Brand kosong ===")
car2 = Car("", "Civic", 4)



print("\n=== Contoh Error: Model bukan teks ===")
car3 = Car("Honda", 123, 4)



print("\n=== Contoh Error: Jumlah pintu huruf ===")
car4 = Car("Suzuki", "Ertiga", "empat")



print("\n=== Contoh Error: Jumlah pintu negatif ===")
car5 = Car("BMW", "X5", -2)



print("\n=== Contoh Error: Kapasitas truk huruf ===")
truck2 = Truck("Isuzu", "Giga", "seribu")



print("\n=== Contoh Error: Muatan melebihi kapasitas ===")
truck3 = Truck("Mitsubishi", "Canter", 1000)
truck3.load(1500)


print("\n=== Contoh Error: dibeberapa tempat")
car6 =Car("", 123, -2)
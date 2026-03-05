class Vehicle:
    def __init__(self, brand, model):

        if not isinstance(brand, str) or not isinstance(model, str):
            raise TypeError("Brand dan model harus berupa teks.")

        if brand.strip() == "" or model.strip() == "":
            raise ValueError("Brand dan model tidak boleh kosong.")

        self.brand = brand
        self.model = model




class Car:
    def __init__(self, brand, model, doors):

        errors = []

        if not isinstance(brand, str):
            errors.append("Brand harus berupa teks")

        if brand == "":
            errors.append("Brand tidak boleh kosong")

        if not isinstance(model, str):
            errors.append("Model harus berupa teks")

        if not isinstance(doors, int):
            errors.append("Jumlah pintu harus berupa angka")

        if isinstance(doors, int) and doors <= 0:
            errors.append("Jumlah pintu harus lebih dari 0")

        if errors:
            print("Terjadi error pada data car")
            for e in errors:
                print("-", e)
            return

        self.brand = brand
        self.model = model
        self.doors = doors

    def drive(self):
        print(f"Mobil {self.brand} model {self.model} dengan {self.doors} pintu")
    def honk(self):
        print("Beep! Beep!")


class Truck:
    def __init__(self, brand, model, load_capacity):

        errors = []

        if not isinstance(load_capacity, (int, float)):
            errors.append("Kapasitas muatan harus angka")

        if isinstance(load_capacity, (int, float)) and load_capacity <= 0:
            errors.append("Kapasitas muatan harus lebih dari 0")

        if errors:
            print("Terjadi error pada data Truk")
            for e in errors:
                print("-", e)
            return

        self.brand = brand
        self.model = model
        self.load_capacity = load_capacity
        



    def load(self, weight):

        errors = []

        if not isinstance(weight, (int, float)):
            errors.append("Berat muatan harus angka")

        if isinstance(weight, (int, float)) and weight <= 0:
            errors.append("Berat muatan harus lebih dari 0")

        if isinstance(weight, (int, float)) and weight > self.load_capacity:
            errors.append("Muatan melebihi kapasitas truk")

        if errors:
            print("Terjadi error saat memuat:")
            for e in errors:
                print("-", e)
            return

        print(f"Loaded {weight} kg")
        
    def drive(self):
        print(f"truck {self.brand} model {self.model} dengan kapasitas muatan {self.load_capacity} Kg")
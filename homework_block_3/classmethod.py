class Car:
    car_count = 0 # Классный атрибут для подсчёта созданных автомобилей


    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.car_count += 1


    @classmethod
    def from_string(cls, car_str):
        """
        Альтернативный конструктор, который принимает строку вида "Brand-Model"
        и возвращает новый объект Car.
        """
        brand, model = car_str.split('-')
        return cls(brand, model)


car1 = Car.from_string("Toyota-Corolla")
print(f"Бренд: {car1.brand}, Модель: {car1.model}")
print(f"Всего автомобилей: {Car.car_count}")


car2 = Car('Mitsubishi', 'Lancer')
print(f"Бренд: {car2.brand}, Модель: {car2.model}")
print(f"Всего автомобилей: {Car.car_count}")


car3 = Car.from_string('Nissan-350z')
print(f"Бренд: {car3.brand}, Модель: {car3.model}")
print(f"Всего автомобилей: {Car.car_count}")
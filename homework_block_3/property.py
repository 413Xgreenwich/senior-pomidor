from dataclasses import dataclass

@dataclass
class Car:
    brand: str
    model: str
    year: int
    speed: int = 0

    def accelerate(self, increment: int):
        """Увеличивает скорость автомобиля."""
        self.speed += increment
        print(f"{self.brand} {self.model} ускоряется до {self.speed} км/ч.")

    def brake(self, decrement: int):
        """Уменьшает скорость автомобиля, не опускаясь ниже 0."""
        self.speed = max(0, self.speed - decrement)
        print(f"{self.brand} {self.model} замедляется до {self.speed} км/ч.")

# Пример использования:
car = Car("Audi", "A4", 2022)
print(car)  # Автоматически использует сгенерированный __repr__
car.accelerate(50)
car.brake(20)
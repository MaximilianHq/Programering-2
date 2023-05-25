class Employee:
    def init(self, name) -> None:
        self.name = name

    def str(self) -> str:
        pass

    def calcSalary(self) -> float:
        return 0

class Seller(Employee):

    def init(self, name, provision, sale) -> None:
        super().init(name)
        self.provision = provision
        self.sale = sale

    def str(self) -> str:
        return f"{self.name} (Säljare)"

    def calcSalary(self) -> float:
        return float(self.provision * self.sale) / 100

class Consultant(Employee):
    def init(self, name, hourRate, hoursWorked) -> None:
        super().init(name)
        self.hourRate = hourRate
        self.hoursWorked = hoursWorked

    def str(self) -> str:
        return f"{self.name} (Konsult)"

    def calcSalary(self) -> float:
        return float(self.hourRate * self.hoursWorked)

class Penpusher(Employee):
    def init(self, name, monthsPay) -> None:
        super().init(name)
        self.monthsPay = monthsPay

    def str(self) -> str:
        return f"{self.name} (Kontorist)"

    def calcSalary(self) -> float:
        return self.monthsPay

# Andra programmet där alla klasser defineras
class Employee:
    TAX_RATE = 0.2  # 20% tax
    SOCIAL_SECURITY_RATE = 0.062  # 6.2% Social Security
    MEDICARE_RATE = 0.0145  # 1.45% Medicare

    def __init__(self, name: str, hourly_wage: float):
        self.name = name
        self.hourly_wage = hourly_wage

    def calculate_weekly_salary(self, hours_worked: float) -> float:
        return self.hourly_wage * hours_worked

    def calculate_deductions(self, gross_salary: float) -> float:
        return (gross_salary * self.TAX_RATE +
                gross_salary * self.SOCIAL_SECURITY_RATE +
                gross_salary * self.MEDICARE_RATE)

    def calculate_net_salary(self, hours_worked: float) -> float:
        gross_salary = self.calculate_weekly_salary(hours_worked)
        deductions = self.calculate_deductions(gross_salary)
        return gross_salary - deductions

# Example usage
if __name__ == "__main__":
    employee = Employee("John Doe", 20)
    hours_worked = 40
    gross_salary = employee.calculate_weekly_salary(hours_worked)
    net_salary = employee.calculate_net_salary(hours_worked)
    
    print(f"Gross Salary: ${gross_salary:.2f}")
    print(f"Net Salary: ${net_salary:.2f}")

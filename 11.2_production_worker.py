def employee():
    employee1 = main.ProductionWorker("","","","")
    print("Enter Information Please")
    employee1.set_name(input("Name of employee: "))
    employee1.set_number(input("Number of employees: "))
    employee1.set_shift(input("Shifts of employees: "))
    employee1.set_pay_rate(input("Pay rate of employee: "))

    print("\n________________________________\n")
    print("name: " + employee1.get_name())
    print("number: " + employee1.get_number())
    print("shift: " + employee1.get_shift())
    print("pay rate: " + employee1.get_pay_rate())


employee()

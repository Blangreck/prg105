def main():
    monthly_loan_payment = float(input("How much do you pay for your loan every month: "))
    monthly_insurance_payment = float(input("How much do you pay for your insurance every month: "))
    monthly_gas_payment = float(input("How much do you pay for your gas every month: "))
    monthly_maintenance_payment = float(input("How much do you pay for maintenance every month: "))
    calculate_total_monthly_cost(monthly_loan_payment, monthly_insurance_payment, monthly_gas_payment, monthly_maintenance_payment)


def calculate_total_monthly_cost(payment1, payment2, payment3, payment4):
    total_monthly_cost = payment1 + payment2 + payment3 + payment4
    print(total_monthly_cost)
    calculate_total_annual_cost(total_monthly_cost)


def calculate_total_annual_cost(total_monthly_cost):
    total_annual_cost = total_monthly_cost * 12
    print(total_annual_cost)


main()

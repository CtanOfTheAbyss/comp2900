payRate = float(input('Pago por hora:'))
hourRate = float(input('Horas trabajadas:'))

overtimehours = 0

if (hourRate > 40):
    overtimehours = hourRate - 40
    totalPay = (40 * payRate) + (overtimehours * (payRate * 2))
else:
    totalPay = hourRate * payRate

print(f'El sueldo a pagar es {totalPay}')
weight = float(input('Input you\'r weight in kg:\n'))
height = int(input('Input you\'r height in cm:\n'))

bmi = round(weight/(height/100)**2, 1)
print(f'Your body mass index is {bmi}')

r_m1 = round(18.5 * (height/100)**2, 1)
r_m2 = round(25.0 * (height/100)**2, 1)
print(f'The recommended weight should be {r_m1} - {r_m2}')

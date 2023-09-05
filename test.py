# weight = float(input('Input you\'r weight in kg:\n'))
# height = int(input('Input you\'r height in cm:\n'))
#
# bmi = round(weight/(height/100)**2, 1)
# print(f'Your body mass index is {bmi}')
#
# r_m1 = round(18.5 * (height/100)**2, 1)
# r_m2 = round(25.0 * (height/100)**2, 1)
# print(f'The recommended weight should be {r_m1} - {r_m2}')

lsat = [75, 'Set_param_weight']

user_data = {
    53234: lsat
}
a = [lsat[0]+32, lsat[1]]
user_data[53234] = a
b = [lsat[0]+42, lsat[1]]
user_data[53234] = b

print(user_data)

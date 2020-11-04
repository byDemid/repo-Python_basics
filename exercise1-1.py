name = input('Как вас зовут? ')
print(f'Привет, {name}!')
age = int(input('Сколько вам лет? '))
if age <= 17:
    print(f'Вы еще так молоды {name}!')
else:
    print(f'Добро пожаловать во взрослую жизнь {name}!')

# средний прожиточный возраст в россии
middle_age = 66
# процент прожитой жизни
percent_of_life = age * 100 / middle_age

print(f'{name}, в среднем Вы прожили {round(percent_of_life, 2)} % своей жизни.')

seconds = int(input('Введите время в секундах: '))
hours = seconds // 3600
minutes = (seconds // 60) % 60
seconds = seconds % 60
if hours < 10:
    hours = '0' + str(hours)
if minutes < 10:
    minutes = '0' + str(minutes)
if seconds < 10:
    seconds = '0' + str(seconds)
print(f'{hours}:{minutes}:{seconds}')

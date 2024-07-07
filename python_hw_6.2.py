

all_seconds = int(input('Please, enter the number of seconds (from 0 to 863999)'))

if 0 <= all_seconds <= 8640000:
    days, seconds_left = divmod(all_seconds, 86400)
    hours, seconds_left = divmod(seconds_left, 3600)
    minutes, seconds = divmod(seconds_left, 60)

    if days % 10 == 1 and days % 100 != 11:
        day_word = 'день'
    elif 2<= days % 10 <= 4 and (days % 100 < 10 or days % 100 >=20):
        day_word = 'дні'
    else:
        day_word = 'днів'

    print(f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
else:
    print('The number entered must be between 0 and 83999')
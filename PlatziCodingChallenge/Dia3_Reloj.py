"""
¿Sabes cuántos segundos hay en 32 horas y 20 minutos? No te preocupes, yo tampoco. Para eso tenemos a las computadoras.
El reto del día de hoy es escribir un programa que tome como parámetros las horas y los minutos y que nos calcule los segundos. ¿En cuántos lenguajes de programación puedes escribir este programa?
"""

# Objetivo: Definir cuantos segundos hay en 32 horas y 20 min

def welcome():
    print(f'''\n\t--- Welcome to the time translator ---\n\tTo start enter hours and minutes\n\t to find how many seconds are in that time:''')

    user_hours = int(input('\nHow many hours?: '))
    print(f'You set: {user_hours} hours.')

    user_minutes = int(input(f'\nHow many minutes?: '))
    print(f'You set: {user_minutes} minutes.')

    user_time = [user_hours, user_minutes]

    return (user_time)

def calc_seconds(time):
    hours_to_secs = 3600      # 1 hour = 3600 seconds
    minutes_to_secs = 60     # 1 minute = 60 seconds

    seconds = ((time[0] * hours_to_secs) + (time[1] * minutes_to_secs))

    return seconds
if __name__ == "__main__":
    time = welcome()
    secs = calc_seconds(time)
    print(f'\n--> There are {secs} seconds in the time you set.')

import datetime

#####################
## working with date
#####################

d = datetime.date(2000,8,8)
print(f'{d}')

print(f'this is todas\'s date {datetime.date.today()}')

print(f'this is todas\'s day number {datetime.date.today().weekday()}')
print(f'this is todas\'s iso day number {datetime.date.today().isoweekday()}')
 
tday = datetime.date.today()

tdalta = datetime.timedelta(days=8)

print(f'what is day after 8 days from today {tday + tdalta}')

print(f'what is the day 8 days ago from today {tday - tdalta} ')

btday = datetime.date(2022,8,8 )

print(f'this many days left till birthday this year {btday - tday}')

bday = datetime.date(2000,8,8)

print(f'this many days you lived in your life {tday-bday}')

########################
## working with datetime
########################

dtb = datetime.datetime(2000,8,8,8,8,8,8)

dtn = datetime.datetime.now()

print(f'this much time spant from your birthdate till now {dtn-dtb}')


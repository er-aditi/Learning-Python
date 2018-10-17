user_input = "2018-10-17 15:37:05"


def formatted_date(date_time):
    date_and_time = date_time.split(" ")
    my_date = date_and_time[0]
    my_time = date_and_time[1]
    date = my_date.split('-')
    print(date[2], end="th ")

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
              'September', 'October', 'November', 'December']
    var1 = date[1]
    convert = int(var1)

    print(months[convert-1], end=" ")
    print(date[0])
    time = my_time.split(':')
    if time[0] == '13':
        hr = '1'
    elif time[0] == '14':
        hr = '2'
    elif time[0] == '15':
        hr = '3'
    elif time[0] == '16':
        hr = '4'
    elif time[0] == '17':
        hr = '5'
    elif time[0] == '18':
        hr = '6'
    elif time[0] == '19':
        hr = '7'
    elif time[0] == '20':
        hr = '8'
    elif time[0] == '21':
        hr = '9'
    elif time[0] == '22':
        hr = '10'
    elif time[0] == '23':
        hr = '11'
    elif time[0] == '24':
        hr = '12'

    print(hr, end=":")
    print(time[1], end=" ")
    if time[0] < '12':
        print("PM")
    else:
        print("AM")


formatted_date(user_input)
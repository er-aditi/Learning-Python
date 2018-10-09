def make_album(artist, title):
    full = {'Artist = ': artist, 'Title = ': title}
    return full


while True:
    print("Please Enter album detail")
    user = input("If you want to exit press 'q': ")
    if user == 'q':
        break
    a_name = input("Artist: ")
    t_name = input("Title: ")

    print(make_album(a_name, t_name))


user_0 = {
    'aditi': 'jain',
    'vine': 'smith',
    'manya': 'john',
    'erin': 'smith'
    }

friends = ['aditi', 'vine' ]
for name in user_0.keys():
    # print(name.title())

    if name in friends:
        print(name.title() + " Surname is " + user_0[name] + ".")

if 'erin' not in user_0:
    print('erin, Please take poll.')
def exceptionHandling():
    try:
        a = 10
        b = 'aditi'
        c = 0

        d = (a+b) / c
        print(d)

    # except ZeroDivisionError:
    #     print("Excepted")
    # except TypeError:
    #     print("It's type error")
    except:
        print("IN except block")


exceptionHandling()



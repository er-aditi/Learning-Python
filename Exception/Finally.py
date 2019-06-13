def exceptionHandling():
    try:

        a = 10
        b=20
        c =0
        d =(a+b)/c

        print(d)

    except:
        print("In exception")
        # raise Exception("Exception")
    else:
        print("Lets exceute")
    finally:
        print("This is by default ")

exceptionHandling()

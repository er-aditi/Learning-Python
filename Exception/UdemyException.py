def exceptionHandling():

    try:
        car = {'make': '860i', 'model': 'i10', 'Year': 2018}

        print(car[color])

    except:
        print("Working fine.")
    finally:
        print("This will work")


exceptionHandling()


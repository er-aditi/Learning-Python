usernames = ['aditi', 'vine', 'admin', 'john']
message = 'would you like to see a status report?'
message_2 = 'thank you for logging in again.'
for username in usernames:
    if 'admin' in username:
        print("Hello " + username + ", " + message)
    else:
        print("Hello " + username + ", " + message_2)
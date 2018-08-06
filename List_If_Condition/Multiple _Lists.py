my_friends = ['mayra', 'john', 'berry', 'tom', 'nolan']
your_friends = ['tom', 'vine', 'john']

for your_friend in your_friends:
    if your_friend in my_friends:
        print(your_friend.title() + " my bestFriend")
    else:
        print(your_friend.title() + " not my friend")

print("My Friends")
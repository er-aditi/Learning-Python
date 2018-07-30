people = ['jon diesel', 'john Smith', 'ana bella', 'Tom Cruise', 'Ana Smith']
message = 'Sorry, I can invite only two people for Dinner.'
sorry_message = ', Sorry! New dinner table won’t arrive in time for the dinner. So, Plan Cancel.'

print(message)
sorry_ppl = people.pop(1)
print("\n" + sorry_ppl.title() + sorry_message.title())


sorry_ppl = people.pop(1)
print('\n' + sorry_ppl.title() + sorry_message.title())

sorry_ppl = people.pop(1)
print("\n" + sorry_ppl.title() + sorry_message.title())


welcome_message = "You are invited for Dinner."
welcome_message_1 = "Thankyou!"

print("\n" + people[0].title() + ", " + welcome_message.title() + "\n" + welcome_message_1)
print("\n" + people[1].title() + ", " + welcome_message.title() + "\n" + welcome_message_1)
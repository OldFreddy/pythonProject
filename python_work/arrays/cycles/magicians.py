magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)  # Перебор списка с помощью цикла

for magician in magicians:
    print(f"{magician.title()}, that was a great trick")  # Перебор списка с помощью цикла
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thanks for everyone. That was a great magic show")
# С использованием f-строки.
# Сообщение 1 будет выведено один раз - она вне цикла!
#
magicians = ['alice', 'david', 'corolina'] 
for magician in magicians: 
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can not wait to see your next track, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!") #1
message = \
    'It was a bright cold day in April, and the clocks were striking thirteen'
msg_dict = {}
for msg in list(message):
    msg_dict[msg] = message.count(msg)
print(msg_dict)

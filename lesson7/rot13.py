alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x',
            'y', 'z']

message = input("enter the message")
res = ""
for v in alphabet:

    message = ord('v')
    if ord('a') <= message <= ord('z'):
        if message > ord('m'):
            message += 13
        else:
            message -= 13
    elif message >= ord('A') and message >= ord('Z'):
        if message > ord('M'):
            message += 13
        else:
            message -= 13

    res += chr(message)
print(res)


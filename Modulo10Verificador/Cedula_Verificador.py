card_number = list(map(int, list(input('Enter the credit card number : '))))
card_number.reverse()
checksum = card_number.pop(0)

for i in range(len(card_number)):
    if i % 2 == 0:
        x = card_number[i] * 2
        if len(str(x)) == 2:
            x -= 9
        card_number[i] = x

total = sum(card_number) * 9
total %= 10

if total == checksum:
    print('It is a valid number')
else:
    print('It is not a valid number')
print('Hello, please join me on 31st July at ABC cafe for my leaving party')

# For loop
# Printing a message 5 times
for message in range (5):
    print('Hello, please join me on 31st July at ABC cafe for my leaving party')

# Printing with strings
for message in 'Faith':
    print(message)
    print('Hello, please join me on 31st July at ABC cafe for my leaving party')

# While loops
times = 0
while times < 5:
    print('Hello world')
    times = times + 1

ask = ''
while ask != 'no':
    ask = input('Do you want to print (yes/no)? ').lower()
    if ask == 'yes':
        print('Hello world')
num =20088002
num_string = str(num)
num_string_reversed = num_string[::-1]

if num_string == num_string_reversed:
    print('{} is a Palindrome'.format(num_string))
else:
    print('{} is a Not a Palindrome'.format(num_string))

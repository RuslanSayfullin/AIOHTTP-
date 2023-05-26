new_uppercase = sum(i for line in open('example.txt') for character in line if character.isupper())

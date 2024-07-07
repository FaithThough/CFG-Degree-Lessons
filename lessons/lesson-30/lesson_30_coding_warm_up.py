'''
Use the string "CodeFirstGirls" and only take a part of it: "Girls".
Then turn the word "Girls" into "G-i-r-l-s".
'''

string = "CodeFirstGirls"
print(string)

spliced_string = string[9:]
print(spliced_string)

for index, letter in enumerate(spliced_string):
    print(letter)

'''
Yo, I'll tell you what I want, what I really, really want
So tell me what you want, what you really, really want
I'll tell you what I want, what I really, really want
So tell me what you want, what you really, really want
I wanna, (ha) I wanna, (ha) I wanna, (ha) I wanna, (ha)
I wanna really, really, really wanna zigazig ah"

Count how many times the word "really" 
appears in the Spice Girls lyrics.
'''

lyrics = '''Yo, I'll tell you what I want, what I really, really want
So tell me what you want, what you really, really want
I'll tell you what I want, what I really, really want
So tell me what you want, what you really, really want
I wanna, (ha) I wanna, (ha) I wanna, (ha) I wanna, (ha)
I wanna really, really, really wanna zigazig ah'''

print(lyrics)

print(lyrics.count("really"))
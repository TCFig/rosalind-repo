# ==== Variables and Some Arithmetic ======

a = 949
b = 982
c = (a**2 + b**2)

print(f'INI2(result): {a}^2 x {b}^2 = {c}')

# ==== Strings and Lists ======

s = '7RD03XN98ovvUVQVw4TEPPm1qdRRqzimTMXjhqC8VWCrotaphytuseDlFkE6vaNIrVOBrv59IavdOarIH6rrScTh87W97HNYCWOmZpyS81dFxV6gb7situlaFKi1T0qDKXklNNK3jbjODrnEbP8vfBAFkUQ2zNem.'
a = 42
b = 52
c = 114
d = 119

print(f'INI3(result): {s[a:(b+1)]} {s[c:(d+1)]}')

# ==== Conditions and Loops ======

a = 4738
b = 9610
c = []
for i in range(a, (b+1)):
    if i % 2 != 0:
        c.append(i)

print(f'INI4(result): {sum(c)}')

# ==== Working with Files ======

i = 1
readFile = open('./exercise_files/rosalind_ini5.txt', 'r')
outFile = open('./exercise_files/output.txt', 'w')

for line in readFile.readlines():
    if i % 2 == 0:
        outFile.write(line)
    i = i + 1

outFile.close()
print(f'INI5(result) are in output.txt file')

# ==== Dictionaries ======

d = {}
phrase = 'When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be'
splitPhrase = phrase.split()

for word in splitPhrase:
    if word not in d:
        d[word] = 1
    else:
        d[word] = d[word] + 1

print('↓ INI6(result) ↓')

for word, value in d.items():
    print(f'{word} {value}')




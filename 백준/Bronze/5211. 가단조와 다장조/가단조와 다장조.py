notes = input().split("|")
a_minor = 'ADE'
c_minor = 'CFG'

tonics = ''

for note in notes:
    try:
        tonics += note[0]

    except:
        pass

a, c = 0, 0
for tonic in tonics:
    if tonic in a_minor:
        a += 1
    elif tonic in c_minor:
        c += 1

if a == c:
    print("A-minor" if notes[-1][-1] in a_minor else "C-major" )
elif a > c:
    print("A-minor")
else:
    print("C-major")
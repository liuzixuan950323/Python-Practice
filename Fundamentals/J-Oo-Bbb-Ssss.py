#Create a function that will do the following:
    #print accum("dEsGc") as "D-Ee-Sss-Gggg-Ccccc"


def accum(s):
    count = 1
    l = []
    for letter in s:
        l.append((str(letter) * count).capitalize())
        count = count + 1
    line = '-'.join(l)
    print(line)
    return

accum("jobs")

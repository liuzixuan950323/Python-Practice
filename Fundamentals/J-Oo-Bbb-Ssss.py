#Create a function that will do the following:
    #accum("abcd")    # "A-Bb-Ccc-Dddd"
    #accum("RqaEzty") # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
    #accum("cwAt")    # "C-Ww-Aaa-Tttt"


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

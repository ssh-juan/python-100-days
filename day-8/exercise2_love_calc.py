# You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 
# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   
# 2. Then check for the number of times the letters in the word LOVE occurs.   
# 3. Then combine these numbers to make a 2 digit number and print it out. 

#****This was the first solution that I built, but it's not 100% right comparing to the requirements.
#It's fixed on v2.

def calculated_love_score(name1, name2):
    t = 0
    r = 0
    u = 0
    e = 0
    l = 0
    o = 0
    v = 0

    for n in name1:
        if n in ("T","t"):
            t += 1
        elif n in ("R", "r"):
            r += 1
        elif n in ("U", "u"):
            u += 1
        elif n in ("E", "e"):
            e += 1
        elif n in ("L", "l"):
            l += 1
        elif n in ("O", "o"):
            o += 1
        elif n in ("V", "v"):
            v += 1
    
    n1 = [t,r,u,e,l,o,v]
    n1_score = sum(n1)

    t = 0
    r = 0
    u = 0
    e = 0
    l = 0
    o = 0
    v = 0

    for n in name2:
        if n in ("T","t"):
            t += 1
        elif n in ("R", "r"):
            r += 1
        elif n in ("U", "u"):
            u += 1
        elif n in ("E", "e"):
            e += 1
        elif n in ("L", "l"):
            l += 1
        elif n in ("O", "o"):
            o += 1
        elif n in ("V", "v"):
            v += 1
    
    n2 = [t,r,u,e,l,o,v]
    n2_score = sum(n2)

    print(n1_score, n2_score, sep='')

calculated_love_score("Juan", "Gabriela")
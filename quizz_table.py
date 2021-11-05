from random import randint as alea


def quizz_table():
    a = alea(1, 10)
    b = alea(1, 10)
    ab = str(a * b)

    c = alea(1, 10)
    d = alea(1, 10)
    cd = str(c * d)

    e = alea(1, 10)
    f = alea(1, 10)
    ef = str(e * f)

    g = alea(1, 10)
    h = alea(1, 10)
    gh = str(g * h)

    i = alea(1, 10)
    j = alea(1, 10)
    ij = str(i * j)

    k = alea(1, 10)
    l = alea(1, 10)
    kl = str(k * l)

    m = alea(1, 10)
    n = alea(1, 10)
    mn = str(m * n)

    o = alea(1, 10)
    p = alea(1, 10)
    op = str(o * p)

    q = alea(1, 10)
    r = alea(1, 10)
    qr = str(q * r)

    s = alea(1, 10)
    t = alea(1, 10)
    st = str(s * t)

    score = 0

    print("        ________________ ")
    print("       |                |")
    print("       |     QUIZZ      |")
    print("       |    TABLE DE    |")
    print("       | MULTIPLICATION |")
    print("       |________________|\n")

    # question 1

    print("Question 1 :")
    print(a, "*", b, "= ?")
    r1 = input("Resultat = ")
    if ab == r1.replace(" ", ""):
        print("Bonne reponse !\n")
        score += 1
    else:
        print("Mauvaise Reponse,\nle resultat etait : ", ab, "\n")

    # question 2

    print("Question 2 :")
    print(c, "*", d, "= ?")
    r2 = input("Resultat = ")
    if cd == r2.replace(" ", ""):
        print("Bonne reponse !\n")
        score += 1
    else:
        print("Mauvaise Reponse,\nle resultat etait : ", cd, "\n")

    # question 3

    print("Question 3 :")
    print(e, "*", f, "= ?")
    r3 = input("Resultat = ")
    if ef == r3.replace(" ", ""):
        print("Bonne reponse !\n")
        score += 1
    else:
        print("Mauvaise Reponse,\nle resultat etait : ", ef, "\n")

    # question 4

    print("Question 4 :")
    print(g, "*", h, "= ?")
    r4 = input("Resultat = ")
    if gh == r4.replace(" ", ""):
        print("Bonne reponse !\n")
        score += 1
    else:
        print("Mauvaise Reponse,\nle resultat etait : ", gh, "\n")

    # question 5

    print("Question 5 :")
    print(i, "*", j, "= ?")
    r5 = input("Resultat = ")
    if ij == r5.replace(" ", ""):
        print("Bonne reponse !\n")
        score += 1
    else:
        print("Mauvaise Reponse,\nle resultat etait : ", ij, "\n")

    # question 6

    print("Question 6 :")
    print(k, "*", l, "= ?")
    r6 = input("Resultat = ")
    if kl == r6.replace(" ", ""):
        print("Bonne reponse !\n")
        score += 1
    else:
        print("Mauvaise Reponse,\nle resultat etait : ", kl, "\n")

    # question 7

    print("Question 7 :")
    print(m, "*", n, "= ?")
    r7 = input("Resultat = ")
    if mn == r7.replace(" ", ""):
        print("Bonne reponse !\n")
        score += 1
    else:
        print("Mauvaise Reponse,\nle resultat etait : ", mn, "\n")

    # question 8

    print("Question 8 :")
    print(o, "*", p, "= ?")
    r8 = input("Resultat = ")
    if op == r8.replace(" ", ""):
        print("Bonne reponse !\n")
        score += 1
    else:
        print("Mauvaise Reponse,\nle resultat etait : ", op, "\n")

    # question 9

    print("Question 9 :")
    print(q, "*", r, "= ?")
    r9 = input("Resultat = ")
    if qr == r9.replace(" ", ""):
        print("Bonne reponse !\n")
        score += 1
    else:
        print("Mauvaise Reponse,\nle resultat etait : ", qr, "\n")

    # question 10

    print("Question 10 :")
    print(s, "*", t, "= ?")
    r10 = input("Resultat = ")
    if st == r10.replace(" ", ""):
        print("Bonne reponse !\n")
        score += 1
    else:
        print("Mauvaise Reponse,\nle resultat etait : ", st, "\n")

    # score

    print("Tu as obtenu", score, "points")
    if score == 10:
        print("CARTON PLEIN !\n")
    elif score == 9:
        print("A 1 point d'avoir tout juste,\ndommage...\n")
    elif score > 5:
        print("C'est bien ça !\n")
    elif score == 5:
        print("Bien joue !\nTu as obtenu la moyenne\n")
    elif score == 4:
        print("Grrrr à 1 point de la moyenne !\n")
    else:
        print("Continue à reviser,\ntu vas y arriver !!!\n")


boucle = True
while boucle:
    quizz_table()
    continuer = input("Voulez-vous rejouer ? (O/N): ")
    if continuer not in ('O', 'o', 'Y', 'y') and continuer in ('N', 'n', ''):
        boucle = False

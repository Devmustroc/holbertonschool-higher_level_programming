#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and type(roman_string) is str:
        spQr = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
        valeur = 0
        for i, j in zip(roman_string, roman_string[1:]):
            if spQr[i] < spQr[j]:
                valeur = valeur - spQr[i]
            else:
                valeur = valeur + spQr[i]
        valeur = valeur + spQr[roman_string[-1]]
        return valeur
    else:
        return 0

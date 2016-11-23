import Lab5Package.Addition
import Lab5Package.Multiplication


def utilizare_modul(list):

    print(Lab5Package.Addition.addition(list))
    print(Lab5Package.Addition.additionWithParam(3,list))
    print(Lab5Package.Multiplication.multiply(list))


print(utilizare_modul([3,5]))


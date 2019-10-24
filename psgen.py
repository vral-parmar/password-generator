from random import choice

basic = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
basicUrlsafe = basic + "-_"
mediumUrlReserved = basicUrlsafe + ";/?:@=&"
mediumUtf8 = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~="
high = basic + "!\"#$%&'()*+,-./:;=?@[]^_`{}~|¬¦"
veryHigh = basic + "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüý"

def main():
    print('Password Generator By Crimson One')
    PassLength = input('Length of password = ')
    passComplexity = input(
        '1) basic (alphanum)\n' +
        '2) basic url-safe\n' +
        '3) medium url-reserved\n' +
        '4) medium UTF-8\n' +
        '5) high\n' +
        '6) very high - ascii\n'
    )

    try:
        PassLength = int(PassLength)
        passComplexity = int(passComplexity)
    except:
        print('You have to provide a number. exit(0).')
        exit()


    if (0 == passComplexity or 1 == passComplexity):
        charSet = basic
        charsetName = "basic (alphanum)"
    elif (2 == passComplexity):
        charSet = basicUrlsafe
        charsetName = "basic url-safe"
    elif (3 == passComplexity):
        charSet = mediumUrlReserved
        charsetName = "medium url-reserved"
    elif (4 == passComplexity):
        charSet = mediumUtf8
        charsetName = "medium UTF-8"
    elif (5 == passComplexity):
        charSet = high
        charsetName = "hgh"
    elif (6 == passComplexity):
        charSet = veryHigh
        charsetName = "very high - ascii"    
    
    loop = ''
    while (loop != 'q'):
        output = ''
        print(f'\n length = {PassLength} choice = {charsetName}')
        for i in range(PassLength):
            output = output + choice(charSet)
        print(output)
        loop = input('Press Any key to generate another. or Press \'q\' to quit')

if __name__ == "__main__":
    main()


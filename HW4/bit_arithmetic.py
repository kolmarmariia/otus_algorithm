from datetime import datetime
import numpy as np


# Прогулка Короля - BITS * 00000000 00000000 00000011 00000010 = 2^9 +2^8 +2^1 =512+256 +2 = 770

# король находится в указанной клетке
# вывести кол-во возможных ходов короля

# 0-63 - индекс позиции укороля
# король ходит на одну клектку в любую сторону

def popcnt(mask):
    movesCount = 0
    while (mask > 0):
        if ((mask & np.ulonglong(1)) == 1):
            movesCount += 1
        mask >>= np.ulonglong(1)
    return movesCount


def movesCntKing(kingNr):
    kingBits = np.ulonglong(1) << np.ulonglong(kingNr)

    nA = np.ulonglong(0xFeFeFeFeFeFeFeFe)
    nH = np.ulonglong(0x7f7f7f7f7f7f7f7f)

    mask = nH & (kingBits >> np.ulonglong(1) | kingBits >> np.ulonglong(9) | kingBits << np.ulonglong(7)) | \
           nA & (kingBits << np.ulonglong(1) | kingBits << np.ulonglong(9) | kingBits >> np.ulonglong(7)) | \
           kingBits >> np.ulonglong(8) | kingBits << np.ulonglong(8)

    print("mask", mask)

    movesCount = popcnt(mask)
    return movesCount, mask


def popcnt2(mask):
    movesCount = 0
    while (mask > 0):
        movesCount += 1
        mask &= mask - 1

    return movesCount


def fillBits():
    b = []
    for i in range(0, 255):
        b.append(popcnt2(i))
    return b


def popcnt3(mask):
    movesCount = 0
    b = fillBits()
    while (mask > 0):
        movesCount += b[int(mask) & 255]
        mask = mask >> np.ulonglong(8)

    return movesCount


# конь
# позиция - 00000000 00000010 00000100 00000000 = 2^17 + 2^10 = 131072 + 1024 = 132096
def movesCntKnight(knightNr):
    knightBits = np.ulonglong(1) << np.ulonglong(knightNr)

    nA = np.ulonglong(0xFeFeFeFeFeFeFeFe)
    nAB = np.ulonglong(0xFcFcFcFcFcFcFcFc)
    nH = np.ulonglong(0x7f7f7f7f7f7f7f7f)
    nGH = np.ulonglong(0x3f3f3f3f3f3f3f3f)

    mask = nGH & (knightBits << np.ulonglong(6) | knightBits >> np.ulonglong(10)) | \
           nH & (knightBits << np.ulonglong(15) | knightBits >> np.ulonglong(17)) | \
           nA & (knightBits << np.ulonglong(17) | knightBits >> np.ulonglong(15)) | \
           nAB & (knightBits << np.ulonglong(10) | knightBits >> np.ulonglong(6))

    movesCount = popcnt3(mask)
    return movesCount, mask


# конь
# позиция - 00000000 00000010 00000100 00000000 = 2^17 + 2^10 = 131072 + 1024 = 132096
def movesCntRook(rooktNr):
    rookBits = np.ulonglong(1) << np.ulonglong(rooktNr)

    nA = np.ulonglong(0xFeFeFeFeFeFeFeFe)
    nH = np.ulonglong(0x7f7f7f7f7f7f7f7f)

    # сдвиг по вертикали можно не ограничивать
    mask = rookBits >> np.ulonglong(8) | rookBits >> np.ulonglong(16) | rookBits >> np.ulonglong(24) | \
           rookBits >> np.ulonglong(32) | rookBits >> np.ulonglong(40) | rookBits >> np.ulonglong(48) | \
           rookBits >> np.ulonglong(56) | \
           rookBits << np.ulonglong(8) | rookBits << np.ulonglong(16) | rookBits << np.ulonglong(24) | \
           rookBits << np.ulonglong(32) | rookBits << np.ulonglong(40) | rookBits << np.ulonglong(48) | \
           rookBits << np.ulonglong(56)

    i = 1
    rooktNr2 = rooktNr
    # добавляем сдвиг по горизонтали влево
    while (rooktNr2 % 8 != 0):
        rooktNr2 = rooktNr2 - 1
        mask = mask | rookBits >> np.ulonglong(i)
        i = i + 1

    i = 1
    rooktNr2 = rooktNr
    # добавляем сдвиг по горизонтали вправо
    while ((rooktNr2 % 7 > 0) | (rooktNr2 == 0)):
        rooktNr2 = rooktNr2 + 1
        mask = mask | rookBits << np.ulonglong(i)
        i = i + 1

    movesCount = popcnt3(mask)
    return movesCount, mask


print("кол-во ходов королем, битовая маска всех возможных ходов короля.:", movesCntKing(0))
print("кол-во ходов конем, битовая маска всех возможных ходов коня.:", movesCntKnight(0))
print("кол-во ходов ладьей, битовая маска всех возможных ходов ладьи:", movesCntRook(0))

from packaging import version as v


def ver(num):
    return v.parse(str(num))


def isnewer(taget, num):
    return taget > v.parse(str(num))


def isolder(taget, num):
    return taget < v.parse(str(num))

def nestedListSum(NL):
    if isinstance(NL, int):     
        return NL               

    sum = 0                     
    for i in range(0, len(NL)):
        sum = sum + nestedListSum(NL[i])
    return sum   
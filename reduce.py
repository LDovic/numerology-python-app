def get_input(var):
    print("Enter " + var)
    x = input()
    return x

def numerologize(num, masters):
    literals = [1,2,3,4,5,6,7,8,9,0]
    if masters:
        literals.append(11)
        literals.append(22)
        literals.append(33)

    lis = list(str(num))
    y = 0

    for l in lis:
        y += int(l)

    if y in literals:
        return y
    else:
        return numerologize(str(y), masters)

#Tyler Nguyen
# property tax calculator 1
def part1():
    nheac = .00004
    mwrdc = .00406
    pmab = .00006
    cpd = .00362
    MiscTx = nheac + mwrdc + pmab + cpd
    return MiscTx

def part2():
    bec = .03726
    cccd = .00169
    Schooltax = bec + cccd
    return Schooltax

def part3():
    csbif = .00128
    clf = .00122
    city = .01630
    City = csbif + clf + city
    return City

def part4():
    ccfpd = .00063
    cook = .00316
    ccps = .00130
    cchf = .00087
    CookCty = ccfpd + cook + ccps + cchf
    return CookCty

def main():
    print('-------------------------')
    mt = part1()
    st = part2()
    ct = part3()
    cc = part4()
    TotalTaxRate = mt + st + ct + cc
    print('Property Tax Rate is:', TotalTaxRate)

main(

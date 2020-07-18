
def solution(phoneBook):
    phoneBook = sorted(phoneBook)
    phoneBook.sort()
    print(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

pn_list_ex1 = ['12','123','1235','567','88']
pn_list_ex2 = ["123", "456", "789"]
res=solution(pn_list_ex1)
print(res)
bs=int(input("salary amount:"))
if bs <=10000:
    hra =(20%100)*bs
    da=(80%100)*bs
    gs=bs+hra+da
    print("gs:",gs)
elif bs <=20000:
    hra2 =(25%100)*bs
    da2=(90%100)*bs
    gs2=bs+hra2+da2
    print("gs:",gs2)
elif bs >=20000:
    hra3 =(30%100)*bs
    da3 =(95%100)*bs
    gs3=bs+hra3+da3
    print("gs:",gs3)
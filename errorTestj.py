def someFct(a):
    if a<10:
        raise ValueError('input number has to be equal or larger than 10 !!! j')
    print('input number is',a)


# try:
#     someFct(9)
# except Exception as e:
#     print('exception occured:',e)
#     raise

someFct(3)
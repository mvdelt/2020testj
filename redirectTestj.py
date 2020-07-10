import io

# from contextlib import redirect_stdout
# with io.StringIO() as buf, redirect_stdout(buf):
#     print('redirected')
#     output = buf.getvalue()
#     print('111',output)
#     output = buf.getvalue()

# print(output)


import contextlib
buffj = io.StringIO()
with contextlib.redirect_stdout(buffj):
    print('redirected j !!!!!!')
    print('redirected cc !!!!!!')
    print('redirected zzzz !!!!!!')
    outputj = buffj.getvalue()

print('-----------')
print('j)',outputj)

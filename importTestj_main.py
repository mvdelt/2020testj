# from importTestj_module import functionB 
import importTestj_module 
# i. 파이썬파일명에 '-' 를 넣으니까 임포트시 에러뜨네. '_'(언더바) 를 사용하는 이유가 다 있군.

print('this is importTestj_main.py... __name__:',__name__)
if __name__ == "__main__":
    print('j) this is a main file, and imported importTestj_module. I will call functionB...')
    importTestj_module.functionB()
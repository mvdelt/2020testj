"""
2020.10.26.월욜새벽1시. 그냥 두 어노테이션json파일이 동일한건지 확인하는 코드.
***이거 꼼꼼히 검토 안해봣음. 걍 졸린데 대충한거임!!***
"""
import json

def compareTwoAnnoFiles(annoFile1_path, annoFile2_path):

    with open(annoFile1_path) as f:
        anno1 = json.load(f)
    with open(annoFile2_path) as f:
        anno2 = json.load(f)
    
    print(anno1==anno2)

annoFile1_path = r"C:\Users\starriet\Desktop\pa_keypointj_lower2\pa_kp_lower_27over48.json"
annoFile2_path = r"C:\Users\starriet\Desktop\pa_keypointj_lower_merged\pa_kp_lower_27over48.json"
compareTwoAnnoFiles(annoFile1_path, annoFile2_path)

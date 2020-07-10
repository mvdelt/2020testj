#(제작일: 2020년 4월 18일 토요일 오전.)
# Pythono3 code to rename multiple files in a directory or folder 

# importing os module
import os 

# def testj():
#     s = "PA20181212save0000_"
#     a = len(s) 
#     print(a) # 19
#     print(s[-3:])


# Function for list sorting.
def listsortj(elem):
    """
    (제작일: 2020년 4월 18일 토요일 오전.)
    renamej 함수에서 리스트 정렬해줄때 사용하기위한 함수.
    예를들어 인풋값이  "PA20181212save0000.jpg"면 0을 리턴. "PA20181212save0000_0.jpg"면 1을 리턴. "PA20181212save0000_1.jpg"면 2를 리턴. 이런식.
    Args:
        elem: list의 각 원소.
    Returns:
        list를 sorting해줄 숫자.
    """
    if '_' not in elem:
        return 0
    else:
        baselen = len("PA20181212save0000_") # 19
        return (int(elem[baselen:-4]) + 1)


# Function to rename multiple files.
def renamej(pathj):
    """
    (제작일: 2020년 4월 18일 토요일 오전.)
    특정 디렉토리의 다수 파일들 한꺼번에 이름 변경해주는 함수.
    Args:
        pathj (str): 이름들 변경해줄 파일들이 있는 경로.
    하는일:
        pathj 에 있는 파일들을 지정해준대로 이름 바꿔줌.        
    """
    li = os.listdir(pathj)

    # listsortj 함수를 이용해서 정렬해줌.
    li.sort(key=listsortj)

    for _, filename in enumerate(li):
        src = os.path.join(pathj, filename)
        newname = "PA20181212_2nd_" + filename[len("PA20181212"):]
        dst = os.path.join(pathj, newname)
        
        # rename() function will rename all the files.
        os.rename(src, dst) 

# Driver Code 
if __name__ == '__main__': 
	
	# Calling main() function 
    # i. 작동 잘됨!!
	renamej("C:/Users/starriet/Desktop/pa_keypoint_upper2") 


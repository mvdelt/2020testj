#(제작일: 2020년 6월 9일 화요일 낮.)
# Pythono3 code to rename multiple files in a directory or folder 

# importing os module
import os 



# # Function for list sorting.
# def listsortj(elem):
#     """
#     (제작일: 2020년 4월 18일 토요일 오전.)
#     renamej 함수에서 리스트 정렬해줄때 사용하기위한 함수.
#     예를들어 인풋값이  "PA20181212save0000.jpg"면 0을 리턴. "PA20181212save0000_0.jpg"면 1을 리턴. "PA20181212save0000_1.jpg"면 2를 리턴. 이런식.
#     Args:
#         elem: list의 각 원소.
#     Returns:
#         list를 sorting해줄 숫자.
#     """
#     if '_' not in elem:
#         return 0
#     else:
#         baselen = len("PA20181212save0000_") # 19
#         return (int(elem[baselen:-4]) + 1)


# Function for list sorting.
def listsort2j(elem):
    """
    (제작일: 2020년 6월 9일 화요일 낮.)
    renamej 함수에서 리스트 정렬해줄때 사용하기위한 함수 2.
    예를들어 인풋값이
    20200429_0000.jpg 면 0 리턴,
    20200429_0000_0.jpg 면 1 리턴, 20200429_0000_1.jpg 면 2 리턴, ... 이런식.
    Args:
        elem: list의 각 원소.
    Returns:
        list를 sorting해줄 숫자.
    """
    if '20200429_0000.jpg' == elem:
        return 0
    else:
        baselen = len("20200429_0000_")
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
    # li = os.listdir(pathj)
    
    ## i. 특정 디렉토리에서 오직 파일만, 그리고 파일명에 특정 문자열을 포함한 파일만 골라서 리스트 만드는 코드.
    li = [i for i in os.listdir(pathj) if os.path.isfile(os.path.join(pathj, i)) and '20200429_0000' in i]

    # listsortj 함수를 이용해서 정렬해줌.
    li.sort(key=listsort2j)

    for _, filename in enumerate(li):
        src = os.path.join(pathj, filename)
        if '20200429_0000.jpg' == filename:
            sortNum = 0
        else:
            sortNum = int(filename[len("20200429_0000_"):-4]) + 1
        newname = "20200603_" + str(sortNum) + ".jpg"
        dst = os.path.join(pathj, newname)
        
        # rename() function will rename all the files.
        os.rename(src, dst) 

# Driver Code 
if __name__ == '__main__': 
	
	# Calling main() function 
    # i. 작동 잘됨!!
	# renamej("C:/Users/starriet/Desktop/pa_keypoint_upper2") 
	renamej(r"C:\Users\starriet\Desktop\박사논문\20200603sndh")
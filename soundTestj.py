import winsound
frequency = 250 # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)

def annoy(): 
    for i in range(1, 10): 
        winsound.Beep(i * 100, 200)

annoy()

# i. 참고로, jupyter notebook(또는 구글CoLab)에서는 Ipython.display.Audio 를 사용해서 어떤 음악파일이든(인터넷상의 url포함) 재생가능함.



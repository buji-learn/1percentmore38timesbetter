def duration(start, end):
    start = start.split(':')
    if end == "00:00":
        end = "24:00"
    end = end.split(':')
    diffHH = int(end[0])-int(start[0])
    diffMM = int(end[1])-int(start[1])
    # print(60*diffHH + diffMM)
    return 60*diffHH + diffMM

# -------- 1차 시도  --------
# def playedInfo(info):
#     listInfo = info.split(',')
#     # print(listInfo)
#     time = duration(listInfo[0], listInfo[1])
    
#     L = len(listInfo[3])
#     # print(L, listInfo[3])
#     playedMelody = ""
#     for i in range(time):
#         playedMelody += listInfo[3][i%L]
#     # print(time, playedMelody, listInfo[3])
#     return listInfo[2], playedMelody

# -------- '#' 포함된 음 고려 안 함 -------- 2차 시도
# def playedInfo(info):
#     listInfo = info.split(',')
#     # print(listInfo)
#     time = duration(listInfo[0], listInfo[1])
    
#     L = len(listInfo[3])
#     # print(L, listInfo[3])
#     playedMelody = ""
#     i = 0
#     count = 0
#     while count < time :
#         # print(listInfo[3][i%L])
#         playedMelody += listInfo[3][i%L]
#         if listInfo[3][i%L] == '#':
#             i += 1
#             continue
#         i += 1
#         count += 1
#     print(time, playedMelody, listInfo[3])
#     return listInfo[2], playedMelody

# -------- 조건이 일치하는 음악이 여러개일때 재생시간 긴 것 -------- 3차 시도
"""
def playedInfo(info):
    listInfo = info.split(',')
    # print(listInfo)
    time = duration(listInfo[0], listInfo[1])
    
    L = len(listInfo[3])
    # print(L, listInfo[3])
    playedMelody = ""
    i = 0
    count = 0
    while count < time :
        # print(listInfo[3][i%L])
        playedMelody += listInfo[3][i%L]
        if listInfo[3][i%L] == '#':
            i += 1
            continue
        i += 1
        count += 1
        print('i = ', i, '/ count = ', count)
    print(time, playedMelody, listInfo[3])
    return time, listInfo[2], playedMelody
"""


# -------- 1차 시도  --------
# def solution(m, musicinfos):
#     answer = [0]
#     # print(answer[0])
#     for info in musicinfos:
#         # print(playedInfo(info))
#         if m in playedInfo(info)[1]:
#             answer = playedInfo(info)
#     if answer == [0]:
#         answer = '(None)'
#     return answer[0]

# -------- 조건이 일치하는 음악이 여러개일때 재생시간 긴 것 -------- 3차 시도
"""
def solution(m, musicinfos):
    answer = [0]
    for info in musicinfos:
        played = playedInfo(info)
        print('here: ' , played)
        # test = m+'#'
        # print(test)
        if m in played[2] and m+'#' not in played[2]:
            print('1: ', answer)
            if answer[0] < played[0] :
                print('재생시간')
                answer = played
                print('2: ', answer)
    if answer == [0]:
        answer = [0, '(None)']
    return answer[1]
"""

# -------- 4차 시도 replace '#' --------
def replaceHigh(m):
    m = m.replace('C#', 'Z')
    m = m.replace('D#', 'Y')
    m = m.replace('F#', 'X')
    m = m.replace('G#', 'W')
    m = m.replace('A#', 'V')
    return m

def playedInfo(info):
    listInfo = info.split(',')
    time = duration(listInfo[0], listInfo[1])
    
    infoMelody = replaceHigh(listInfo[3])
    L = len(infoMelody)
    print(L, infoMelody)
    playedMelody = ""
    i = 0
    while i < time :
        # print(listInfo[3][i%L])
        playedMelody += infoMelody[i%L]
        i += 1
    print(time, playedMelody, infoMelody)
    return time, listInfo[2], playedMelody

def solution(m, musicinfos):
    answer = [0, (None)]
    m = replaceHigh(m)
    for info in musicinfos:
        played = playedInfo(info)
        print('here: ' , played)
        # if played[0] == 0:
        #     return '(None)'
        # answer = played
        # test = m+'#'
        # print(test)
        if m in played[2]:
            print('1: ', answer)
            if answer[0] < played[0] :
                print('재생시간 비교')
                answer = played
                print('2: ', answer)
    # if answer == '(None)':
    #     answer = [0, '(None)']
    return answer[1]


m = "ABC#"
# print(replaceHigh(m))
# musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
# musicinfos = ["13:00,13:05,WORLD,ABCDEF", "12:00,12:14,HELLO,C#DEFGAB"]
# musicinfos = ["12:55,13:05,WORLD,ABC#DEF", "12:04,12:14,HELLO,C#DEFGAB"]
# musicinfos = ["12:04,12:14,HELLO,C#DEFGAB", "12:55,13:05,WORLD,ABC#DEF"]
musicinfos = ["12:04,12:14,HELLO,C#DEFGAB", "12:55,13:08,WORLD,ABCDEF#", "12:54,13:05,ans,DEFABC#"]

# m = "ABDEFG"
# musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]

print(solution(m, musicinfos))




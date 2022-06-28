# PROGRAMMERS LV01 신고 결과 받기
# https://programmers.co.kr/learn/courses/30/lessons/92334

# 작성자 : 강동준
# 최초 작성일 : 2022-06-28
# 최종 작성일 : 2022-06-28

def solution(id_list, report, k):
    answer = []
    report_List = {}    # Report List, Key = defendant , Value = plaintiff
    report_Count = {}   # Key = plaintiff, Value = Report Count
    index = 0

    # Dictionary init, 
    for userName in id_list:
        report_List[userName] = []
        report_Count[userName] = 0

    # Report comment parsing
    for userReport in report:
        consumer, blackConsumer = userReport.split(' ')
        report_List[blackConsumer].append(consumer)
    
    # Deduplication
    for userName in id_list:
        report_List[userName] = list(set(report_List[userName]))

    # Check report count. Report Email Received Counting
    for userName in id_list:
        if len(report_List[userName]) >= k:
            for consumer in report_List[userName]:
                report_Count[consumer] += 1

    # Change from dictionary to list
    for key in id_list:
        answer.append(report_Count[key])

    return answer


id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3

answer = solution(id_list, report, k)
print(answer)
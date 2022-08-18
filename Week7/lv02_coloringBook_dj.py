# PROGRAMMERS LV2 컬러링북
# https://school.programmers.co.kr/learn/courses/30/lessons/1829

# 작성자 : 강동준
# 최초 작성일 : 2022-08-14
# 최종 작성일 : 2022-08

def soultion(m, n, picture):
  anwer = []
  find = []
  l = [1, 2, 3]
  visi = [[False]*n for _ in range(m)]
  count  = 0
  prev = n
  c = 0
  list_index = 0
  while True:
    if count >= m*n:
      break
    else:
      color = 0
      for i in range(m):
        for j in range(n):
          if visi[i][j] == False and picture[i][j] != 0:
            color = picture[i][j]
            break
            
    for i in range(m):
      for j in range(n):
        if visi[i][j] == False and picture[i][j] == 0:
          count += 1
          visi[i][j] = True
        if j > prev and c > 0 and picture[i][j] == 0:
          prev = j
          break
        if visi[i][j] == False and picture[i][j] != 0:
          if color == picture[i][j]:
            if c == 0:
              c += 1
              count += 1
              prev = j
              visi[i][j] = True
            elif picture[i][j] == picture[i-1][j] or picture[i][j] == picture[i][j-1]:
              c += 1
              count += 1
              visi[i][j] = True
          else:
            prev = j
            break
    anwer.append(c)
    find.append(color)
    print(visi)
    c = 0
    prev = n
  print(visi)
  print(find)
  return anwer
# m = 6
# n = 4
# picture = [[1,1,1,0],[1,2,2,0],[1,0,0,1],[0,0,0,3],[0,0,0,3],[0,0,0,3]]
m = 5
n = 5
picture = [[1,1,1,1,1],[1,2,2,2,1],[1,2,3,2,1],[1,2,2,2,1],[1,1,1,1,1]]
print(soultion(m, n, picture))
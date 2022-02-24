'''
* points.txt 파일의 숫자값을 모두 읽어서
총합과 평균을 구한 뒤
총점, 평균값을 result.txt라는 파일에
쓰는 프로그램을 작성해 보세요.
'''
file_path = 'C:/test/point.txt'

try:
  f = open(file_path,'r')
  text = f.read()
  print(text)
except:
  print('파일 로드 실패!')
finally:
  f.close()


f_path = 'C:/test/result.txt'

try:
  f = open(f_path,'a') 
  f.write(sum)
  f.write(avg)
  print('파일 저장 성공')
except:
  print('파일 저장 실패')
finally:
  f.close()










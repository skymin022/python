import datetime

# [모듈].[객체].함수()
nowtime = datetime.datetime.now()
print('현재 날짜와 시간 : {}'.format(nowtime))

today = datetime.date(2025, 5, 29)
print('현재 날짜와 시간 : {}'.format(today))

lastDay = datetime.date(2025, 9, 17)
print('종강일 : {}'.format(lastDay))

t1 = datetime.time(17,50,0)
print('현재시간 : {}'.format(t1)) 

t2 = datetime.time(18,20,0)
print('수업종료 : {}'.format(t2))

today = datetime.datetime.now()
print( datetime.datetime.today().strftime('%Y-%m-%d') )


print('{} 년'.format( today.year) )
print('{} 월'.format( today.month ) )
print( '%02d' % today.month )   # leading zero
print('{} 일'.format( today.day) )
print('{} 시'.format( today.hour) )
print('{} 분'.format( today.minute) )
print('{} 초'.format( today.second) )


# 오늘 날짜
today = datetime.datetime.today()

# 종강일
lastDay = datetime.datetime(2025,9,17)

# 남은 시간 계산
gap = lastDay - today

print('종강일 까지 {}일 남았습니다.'.format(gap.days) )




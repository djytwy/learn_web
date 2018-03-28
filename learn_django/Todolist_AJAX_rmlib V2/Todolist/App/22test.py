import datetime
import re
import time

p = re.compile('[a-z]')
s = re.findall(p, 'assdfw334567uuingr')
a = re.findall('[a-z]', 'ssddwdw122234141fefe')


#正则表达式的正确写法！！！
content = 'kajdlalkfjewidiv1234yydivjflkediv222233divjwfk'
pattern = re.compile('''div(.*?)div''', re.S)
items = re.findall(pattern, content)

a1 = datetime.datetime.now()
a2 = datetime.datetime(2015, 4, 7, 4, 30, 3, 628556)
r = (a1-a2).total_seconds()

c = "2013-10-10 23:18:45"
timeArray = datetime.datetime.strptime('2017-10-17 11:45:07', "%Y-%m-%d %H:%M:%S")
se = (a1-timeArray).total_seconds()
day = (a1-timeArray).days

# pr = datetime.datetime.strftime()
# print(type(a1), timeArray, se)

ap = ['1天 4小时20分钟59秒', '1天 4小时20分钟52秒']
ap.clear()
ap.append('asssd')
# if '秒' not in ap:
#     print('OK')
# else:
#     print('NO')
day_s = 0
hour_s = 0
minutes_s = 0
sec_s = 0
i = '电饭锅和 --- 23小时65分钟46秒前'

p1 = re.compile('(.*?) ---', re.S)
p2 = re.compile('---(.*)', re.S)

data_1 = re.findall(p1, i)
data_2 = re.findall(p2, i)
p_day = re.compile('(.*?)天', re.S)
day2 = re.findall(p_day, data_2[0])
if len(day2) == 0:
    day_s = ''
else:
    day2 = int(day2[0])
print(day2)
p_hour = re.compile('(.*?)小时', re.S)
hour = re.findall(p_hour, data_2[0])
if len(hour) == 0:
    hour_s = ''
else:
    hour = int(hour[0])
print(hour)
p_minutes = re.compile(' 小时(.*?)分钟', re.S)
minutes = re.findall(p_minutes, data_2[0])
if len(minutes) == 0:
    minutes_s = ''
else:
    minutes = int(minutes[0])
print(minutes)
p_sec = re.compile('分钟(.*?)秒', re.S)
sec = re.findall(p_sec, data_2[0])
sec = int(sec[0])
print(sec)
if sec >= 60:
    if minutes == '':
        minutes_s = '1'
    else:
        minutes += 1
        if minutes >= 60:
            if hour == '':
                hour_s = '1'
            else:
                hour += 1
                hour_s = str(hour)
                if hour > 24:
                    if day == '':
                        day_s = '1'
                    else:
                        day += 1
                        day_s = day
                        day_s = str(day_s)
                    hour_s = hour % 24
                    hour_s = str(hour_s)
                else:
                    day_s = day
            minutes_s = minutes % 60
            minutes_s = str(minutes_s)
        else:
            minutes_s = minutes
    sec_s = sec % 60
else:
    sec_s = sec
sec_s = sec_s + 5
sec_s = str(sec_s)
if day_s == '':
    if hour_s == '':
        if minutes_s == '':
            data_fin = data_1[0] + ' --- ' + '0分钟%s秒前' % sec_s
        else:
            data_fin = data_1[0] + ' --- ' + '%s分钟%s秒前' % (minutes_s, sec_s)
    else:
        data_fin = data_1[0] + ' --- ' + '%s小时%s分钟%s秒前' % (hour_s, minutes_s, sec_s)
else:
    data_fin = data_1[0] + ' --- ' + '%s天 %s小时%s分钟%s秒前' % (day_s, hour_s, minutes_s, sec_s)
print(data_fin)




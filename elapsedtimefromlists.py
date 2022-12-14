from datetime import datetime

ot = ['2022-12-22 20:55:33', '2022-12-23 17:22:33', '2022-12-23 16:44:33', '2012-12-24 15:33:12']
ct = ['2022-12-22 23:55:33', '2022-12-23 19:21:33', '2022-12-23 19:00:00', '2012-12-24 19:33:12']
time_format = "%Y-%m-%d %H:%M:%S"
##uncomment code to get the elapsed time for ot and ct [0]
#this is the premise idea of the code, but the later uses no hardcoded values
#open_time = '2022-12-22 20:55:33'
#closed_time = '2022-12-22 23:55:33'
#you can see out answer should be 3 hours elapsed
#start = datetime.strptime(open_time,time_format)
#stop = datetime.strptime(close_time,time_format)
#diff = stop - start
#print(diff)
#try to use dates that span over multiple days, ie 12/01 to 12/9 and see what you get 

##the following is a list implementation 
start = []
stop = []

for i in ot:
        temp = datetime.strptime(i,time_format)
        start.append(temp)
print(start)

for i in ct: 
        temp = datetime.strptime(i,time_format)
        stop.append(temp)
print(stop)

diff=[]
i = 0
while i < 4:
    diff.append(stop[i]- start[i])
    i+=1
print(diff)


for x in diff:
    x.total_seconds()/60/60
    print(x)
avg = (diff[0]+diff[1]+diff[2]+diff[3]) / 3
print("Avg elapsed times ", avg)
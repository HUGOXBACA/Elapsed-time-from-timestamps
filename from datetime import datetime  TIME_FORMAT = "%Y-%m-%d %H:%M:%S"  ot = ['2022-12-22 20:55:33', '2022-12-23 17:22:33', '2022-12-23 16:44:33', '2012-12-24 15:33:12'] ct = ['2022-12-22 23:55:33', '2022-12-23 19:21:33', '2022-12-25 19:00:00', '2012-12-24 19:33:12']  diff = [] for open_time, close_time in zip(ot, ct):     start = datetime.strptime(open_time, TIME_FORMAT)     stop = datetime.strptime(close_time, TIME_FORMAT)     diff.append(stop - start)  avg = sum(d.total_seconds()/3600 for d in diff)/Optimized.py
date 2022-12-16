from datetime import datetime

TIME_FORMAT = "%Y-%m-%d %H:%M:%S"

ot = ['2022-12-22 20:55:33', '2022-12-23 17:22:33', '2022-12-23 16:44:33', '2012-12-24 15:33:12']
ct = ['2022-12-22 23:55:33', '2022-12-23 19:21:33', '2022-12-25 19:00:00', '2012-12-24 19:33:12']

diff = []
for open_time, close_time in zip(ot, ct):
    start = datetime.strptime(open_time, TIME_FORMAT)
    stop = datetime.strptime(close_time, TIME_FORMAT)
    diff.append(stop - start)

avg = sum(d.total_seconds() / 3600 for d in diff) / len(diff)
print("AVG hours elapsed:", round(avg, 3))

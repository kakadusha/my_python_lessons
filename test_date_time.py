#import datetime
from datetime import datetime

#x = datetime.datetime('2019-10-10 11:11')
datetime_object = datetime.strptime('2019-10-10 11:11', '%Y-%m-%d %H:%M')

print(type(datetime_object))
print(datetime_object)  # printed in default format
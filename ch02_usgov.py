import json
from pandas import DataFrame, Series
import matplotlib
import pandas as pd

prefix = "E:/code/pydata-book/"
path = prefix + 'ch02/usagov_bitly_data2012-03-16-1331923249.txt'

open(path).readline()

records = [json.loads(line) for line in open(path)]
frame = DataFrame(records)


clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'

tz_counts = clean_tz.value_counts()

tz_counts[:10].plot(kind='barh', rot=0)

frame.a.notnull()
Series()

# time_zones = [rec['tz'] for rec in records if 'tz' in rec]
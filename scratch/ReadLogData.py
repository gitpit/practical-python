import os
import sys


work_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = work_dir +r'\data\'
sys.path.append(data_dir)
mes_file = data_dir + r'\meslog.txt'

print(f"work_dir: {work_dir}")
print(f"data_dir: {data_dir}")
print(f"mes_file: {mes_file}")
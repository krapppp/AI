import pandas as pd
pd.__version__

data1 = [10, 20, 30, 40, 50]
print(data1)

data2 = ['1반', '2반', '3반', '4반', '5반']
sr1 = pd.Series(data1)
print(sr1)

sr2 = pd.Series(data2)
print(sr2)

sr3 = pd.Series([101, 102, 103, 104, 105])
print(sr3)

sr4 = pd.Series(['월', '화', '수', '목', '금'])
print(sr4)

sr5 = pd.Series(data1, index = [1000, 1001, 1002, 1003, 1004])
print(sr5)

sr6 = pd.Series(data1, index = data2)
print(sr6)

sr7 = pd.Series(data2, index = data1)
print(sr7)

sr8 = pd.Series(data2, index = sr4)
print(sr8)

print(sr8[2], sr8['수'], sr8[-1], sr8[0:4])
print(sr8.index, sr8.values)

print(sr1+sr3)
print(sr4+sr2)

data_dic={'year': [2018, 2019, 2020], 'sales': [350, 380, 1099]}
df1 = pd.DataFrame(data_dic)
print(df1,type(df1))

df2 = pd.DataFrame([[89.2, 92.5, 90.8], [92.8, 89.9, 95.2]],
index = ['중간고사', '기말고사'], columns = data2[0:3])
print(df2,type(df2))

data_df = [['20201101', 'Hong', '90', '95'], ['20201102','Kim', '93', '94'], ['20201103', 'Lee', '87', '97']]
df3 = pd.DataFrame(data_df)
df3.columns = ['학번', '이름', '중간고사', '기말고사']
print(df3,type(df3))

df3.to_csv('C:/Users/hgd/Python_Project/score.csv', header = 'False')
df4 = pd.read_csv('C:/Users/hgd/Python_Project/score.csv', encoding='utf-8', index_col=0, engine='python')
print(df4,type(df4))
"""
如果字典中不存在color， 则加入color这个键并且赋值black， 如果已经存在了就不变
"""
spam = {'name': 'pengteng', 'age': 45}
spam.setdefault('color', 'black')
print(spam)
spam.setdefault('color', 'white')
print(spam)

# eg:
msg = ('asdasfasxfxzgasgangandgd')
cnt = {}
for ms in msg:
    cnt.setdefault(ms, 0)
    cnt[ms] = cnt[ms] + 1
print(cnt)
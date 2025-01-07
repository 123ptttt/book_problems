import pprint

msg = ('asdasfasxfxzgasgangandgd')
cnt = {}
for ms in msg:
    cnt.setdefault(ms, 0)
    cnt[ms] = cnt[ms] + 1
pprint.pprint(cnt)

#pprint.pprint(s) 等价于 print(pprint.pformat(s))
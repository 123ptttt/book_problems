def dou_hao_dai_ma(strs):
    strs[-1] = 'and' + ' ' + strs[-1]
    return strs

ample = ['cat', 'dog', 'rabbit']
ample = dou_hao_dai_ma(ample)
print(ample)
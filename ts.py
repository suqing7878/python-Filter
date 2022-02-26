import collections



def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # 使用字典标记字符第一次出现的位置然后当字母再次出现的时候计算长度即可
    res = -1
    dic = collections.defaultdict(int)
    for index, c in enumerate(s):
        if c not in dic:
            dic[c] = index
        else:
            res = max(res, index - dic[c] - 1)
    return res



import sys
ipt = sys.stdin.readline
N=int(ipt().rstrip())
st1 = ipt().rstrip()

for i in range(N-1):
    st2 = ipt().rstrip()
    for j in range(len(st2)):
        if st1[j]!=st2[j]:
            st1=st1[:j]+'?'+st1[j+1:]
print(st1)
"""
N=int(input())
*x,=(input()for _ in range(N))
       Generation Expression으로 Input을 받는다.
       애스터리스크(*)와 변수명(x), 그리고 콤마(,)를 함께 적었다.
       이렇게 하면 우측 컨테이너 타입 변수를 '언패킹'해서 리스트로 넣어준다.
        x = list(("config.sys", "config.inf", "configures")) 와
        *x, = ("config.sys", "config.inf", "configures")는 동일하다.
print(''.join([i[0],'?'][i.count(i[0])<N]for i in zip(*x)))
        리스트 x를 '언패킹'하여 zip에 넣어준다.
        여기서 i의 값은
        ('c', 'c', 'c')
        ('o', 'o', 'o')
        ('n', 'n', 'n')
        ('f', 'f', 'f')
        ('i', 'i', 'i')
        ('g', 'g', 'g')
        ('.', '.', 'u')
        ('s', 'i', 'r')
        ('y', 'n', 'e')
        ('s', 'f', 's')
        와 같다.
"""

#https://itholic.github.io/kata-1032/
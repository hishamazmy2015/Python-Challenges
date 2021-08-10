


# l=[[0],[0],[2],[3],[2,2,3],[5],[3,5],[7],[2,2,2,7],[3,2,3,7]]
L=["","","2","3","223","5","35","7","2227","3327"]
n=int(input())
print(''.join(sorted((''.join(sorted([L[int(i)] for i in  input()],reverse=True)[::-1]))[::-1],reverse=True ) ))


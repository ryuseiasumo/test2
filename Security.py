#りゅうせいの解答
S = list(input())
flag = False
for i in range(len(S)-1):
    if (S[i] == S[i+1]):
        flag = True
    if (flag == True):
        break

if (flag == True):
    print("Bad")

else:
    print("Good")


# s=list(input())
# for i in range(len(s)-1):
#   if s[i]==s[i+1]:
#     print("Bad")
#     exit()
# print("Good")
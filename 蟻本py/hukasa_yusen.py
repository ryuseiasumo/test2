#深さ優先探索は再帰関数で作れる
def dfs(i,sum,n,a_list,k):
    if i == n :
        return sum == k

    #a[i]を使わない場合
    if (dfs(i+1,sum,n,a_list,k)):
        return True

    #a[i]を使う場合
    if (dfs(i+1,sum+a_list[i],n,a_list,k)):
        return True

    return False

if dfs(0,0,4,[1,2,4,7],13):
    print("Yes")

else:
    print("No")
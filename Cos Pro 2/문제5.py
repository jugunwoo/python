#문제5
def solution(arr):
    left, right=0, len(arr)-1
    #왼쪽=0   오른쪽=0   숫자갯수
    while left<right: #오른쪽 이 더 클 경우에만
        arr[left],arr[right]=arr[right],arr[left]
        left+=1#왼쪽 1 증가
        right -=1#오른쪽 1 감소
    return arr
    #left 0 일경우 right 0 => 반복문
        #arr[0], arr[0]=arr[0], arr[0]
         #1      #1     #1      #1
        #left =1  right-1
    #left 1일경우 right -1
       #arr[1] , arr[-1]= arr[-1], arr[1]
        #4        #3       #3      #4
        #left +1  right -1
    #left 2일경우  right -2
      #arr[2]   , arr[-2]= arr[-2] ,  arr[2]
        #2          2       2            2
arr=[1,4,2,3]
ret=solution(arr)

print("solution:return value of the fuction is",ret,".")
#-*- coding:utf-8 -*-
# this is calculate Fibonacci function
# [Algorithms with Pytho 再帰定義 (recursive definition)](http://www.geocities.jp/m_hiroi/light/pyalgo01.html)
# [pythonにswitchはないけれど](https://qiita.com/Go-zen-chu/items/9bc7011616759dd2fc93)

def f(n):
	if n == 0:
		return 1
	elif n > 0 :
		return  1 + (1 / f(n-1))

if __name__ == '__main__' :
	
	print("please input limit number>")
	max = int(input())
	
	result = []
	
	for i in range(0, max) :
		result.append(f(i))
		print(" f(" + str(i) + ")= " + str(result[i]))
		print(str((result[i] * 2)-1))
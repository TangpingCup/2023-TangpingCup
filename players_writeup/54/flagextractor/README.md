# 解
vim得到flag1
IDA反编译得到密文

>synt{Mu6_K6R_jR6_Wv_6F_P5ZVat}

查看算法ROT13得明文flag2

>flag{Zh1_X1E_wE1_Ji_1S_C0MIng}

附小bugc++程序

```C++
#include<bits/stdc++.h>
using namespace std;

int main(){
	char a[114];
	for(int i=0;i<30;i++){
		cin>>a[i];
		cout<<int(a[i])<<" ";
	}
	for(int i=0;i<strlen(a);i++){
		char out=a[i];
		if(isalpha(a[i])!=0){
		if(tolower(a[i])<=110)out=a[i]+13;
		else out=a[i]-13;
		}
		else if(a[i]-48<=9){
		if(a[i]>52)out=a[i]-5;
		else out=a[i]+5;
		}
		else out=a[i];
		cout<<char(out);
    }
	return 0;
}
```

```console
$ g++ -o flagextractor flagextractor.cpp
$ ./flagextractor
synt{Mu6_K6R_jR6_Wv_6F_P5ZVat}
115 121 110 116 123 77 117 54 95 75 54 82 95 106 82 54 95 87 118 95 54 70 95 80 53 90 86 97 116 125 fl{g{Zh1_X1E_wE1_Ji_1S_C0MIng}
```

问题不大
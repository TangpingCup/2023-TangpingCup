# 解
下载附件，得到flag1.zip

```console
$ unzip flag1.zip
Archive:  flag1.zip
  inflating: flag1.gif               
error: invalid zip file with overlapped components (possible zip bomb)
```
正确的，overlapped contents，所以一般的解压工具都会报错。   
得到flag1.gif后，一眼汉信码，于是用[汉信码解码器](https://tuzim.net/hxdecode/)解码，居然扫不出来，反色后扫描，得到

>Good !Flag1: flag{domestic_2D_code} Go /media/boarding_pass.zip

下载boarding_pass.zip，解压，得到加密的download.gif和password.gif   
password一眼二维码，补定位角，扫码得到

>password:ecfbcf7a-0c77-ed48-2e2e-1a993ebd006e

输入密码，解压，download.gif一眼PDF417，扫码得到

>flag2:flag{L00k_l1k3_bo4rd1ng_p4ss} flag3:/media/enterpoint.gif

下载enterpoint.gif，一眼AZTEC，扫码得到

>Go /media/c0d3f14g3.zip

下载c0d3f14g3.zip，解压，得到part1.gif，part2.gif

part1.gif一眼Codablock，扫码得到

>U2FsdGVkX1+QTZuns6phvCNw3MWMReSM3yeB

part2.gif一眼MicroPDF417，扫码得到

>8ZXH4JZBpFxCGu5rDf/2pS4H6w7G
0B+1

pass.gif一眼GS1 Databar Composite，扫码得到

>11451419198103|Year2�oPassword

part1和part2组合，一眼Rabbit，解码即可得到flag3

请勿删除回车



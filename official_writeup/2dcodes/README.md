# [Misc] 二维的码

- 命题人：ZianTT
- 来自理塘的码：150 分
- 你管这叫码？：200 分
- 来自兔年的码：400 分

## 题目描述

<p>测测你的码（bushi）</p>
<div class="well">
<strong>第二阶段提示</strong>
<p>
汉信码，PDF417，Aztec……你可能需要一个能识别一切的网站？
</p>
</div>

**[【附件：下载题目附件（flag1.zip）】](attachment/flag1.zip)**

**[【隐藏附件：enterpoint.gif】](attachment/enterpoint.gif)**

**[【隐藏附件：boarding_pass.zip】](attachment/boarding_pass.zip)**

**[【隐藏附件：c0d3f14g3.zip】](attachment/c0d3f14g3.zip)**

## 预期解法

下载附件，得到flag1.zip

```console
$ unzip flag1.zip
Archive:  flag1.zip
  inflating: flag1.gif               
error: invalid zip file with overlapped components (possible zip bomb)
```

报错了，原因是这里伪加密了，把hex从09改回00，再进行解压。

得到flag1.gif后，一眼汉信码，于是用[汉信码解码器](https://tuzim.net/hxdecode/)解码，扫不出来，发现反色了。反色后扫描，得到

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

>11451419198103|Year2023Password

part1和part2组合，根据提示，兔子=>Rabbit，解码即可得到flag3

注：解密时，请勿删除回车

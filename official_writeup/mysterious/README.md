# [Misc] 神秘的……文字？

- 命题人：ZianTT
- 这么简单：200 分
- 毕加思索：300 分
- 喵？咕？唔~：400 分

## 题目描述

<p>喵喵喵喵</p>
<p>咕咕咕咕咕咕咕咕~</p>
<p>做不出来吧哈哈哈</p>
<div class="well">
<strong>第二阶段提示</strong>
<p>
1 - Base64改个表变成了XX加密
2 - 签了个到？滴滴滴哒哒？
3 - 嗷呜啊？听说鸽游又整了个什么解谜？去看看第一层咋解？
</p>
</div>

**[【附件：下载题目附件（decode.txt）】](attachment/decode.txt)**

**[【隐藏附件：f14g3ofpr0b04.html】](attachment/f14g3ofpr0b04.html)**

## 预期解法

### flag1

打开cyberchef，把密文丢进去

第一层正常base64解码

第二层是换表的base64，表+-0-9A-Za-z

flag1解出

### flag2

一堆表情符号，相信你们也做了签到题，base100解密

然后把喵呜分别替换 .- 然后解密。

根据题目信息重写格式即可得到flag2

### flag3

根据上一步得到的信息，前往目标地址。

兽音编码换了字符，解密得到一个base

base58换表（大小写转换）

然后发现单表替换，丢进quipquip，结束。

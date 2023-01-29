# [Misc] 躺平问答

- 命题人：ZianTT
- 部分的题目：100 分
- 全部的题目：200 分

## 题目描述

<p>你说得对，但是躺平问答绝非抄袭某game的猫咪问答或者某game的小北问答</p>
<p>我们的“自研”答题系统基于PKUGGG开发的答题系统，但是他们的答题系统是开源的</p>
<p>为什么一股homoOS的感觉(恼)</p>
<div class="well">
<strong>萌新入门</strong>
<p>
本题主要考察搜索引擎的运用。当你无法亲眼看到某时刻信息时，你可能需要一个互联网上的档案馆？
</p>
</div>

**【网页链接：访问题目网页】**

## 预期解法

0. 仔细观察会发现藏有`其实，这题没出错`的字样，`F12`查看网页元素可以看到注释里写了``<!-- 114514*1919810 -->``，计算一下就是答案
1. 百度一下`超文本咖啡壶控制协议`可以找到[RFC2324](https://www.rfc-editor.org/rfc/rfc2324)，里面的2.1.1节`The BREW method, and the use of POST`提到`Commands to control a coffee pot are sent from client to coffee  server using either the BREW or POST method, and a message body with Content-Type set to "application/coffee-pot-command".`
2. 使用百毒搜索`google leet`，在csdn里面能找到。
3. 在比赛主页最下面有一个运行状态，点进去。然后在网页最下面找到`Incident History`，点进去找到答案，**记得精确到30分钟**
4. 在[PKU-GeekGame的GitHub存档中](https://github.com/PKU-GeekGame/geekgame-2nd/tree/master/problemset)可以找到每道题的完成人数
5. 这题这个域名是故意过期的，所以直接whois不太行。比如[阿里云](https://whois.aliyun.com/)就行，微步啥的也行。
6. 终端使用`nslookup -type=txt weilei.studio `
7. `nslookup weilei.studio`得到ip，然后上[IPIP](https://tools.ipip.net/as.php)查ASN
8. 使用[互联网档案馆](web.archive.org)，然后翻一下archive就能找到日期。
9. 打开[GitHub](https://github.com/)，然后使用浏览器查看证书到期日期，你的电脑应该是CST，记得转成GMT。

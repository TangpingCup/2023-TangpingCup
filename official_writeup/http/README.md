# [Web] HTTP百解

- 命题人：ZianTT
- 神之眼：50 分
- 导引内卷之力：200 分

## 题目描述

<blockquote>
<p>你说的对，但是《躺平杯》是由BytesSec"自主"研发的一款全新CTF游戏。游戏发生在一个被称作「比赛平台」的幻想世界，在这里，被神选中的人将被授予「flag」，导引内[开]卷[摆]之力。你将扮演一位名为「CTFer」的神秘角色，在自由的旅行中邂逅性格各异、能力独特的群友们，和他们一起击败强敌，找回失散的Flag——同时，逐步发掘「屯flag」的真相。</p>
</blockquote>
<div class="well">
<strong>萌新入门</strong>
<p>
本题考察了对HTTP包的应用，你可能需要你一个支持直接发送HTTP原始包的应用？
</p>
<p>
同时，你应该再对HTTP包结构和传递参数的格式进行了解？
</p>
</div>

<div class="well">
<strong>第二阶段提示</strong>
<p>
你最后可能需要使用WebkitFrom传参？
</p>
</div>

**【网页链接：访问题目网页】**

## 预期解法

### 神之眼

F12里可以看到flag1

### 导引内卷之力

首先打开burpsuite（CLI强迫症用户打开curl）

> Please request me securely with Bytes Security Browser !

User-Agent 设置成`Bytes Security Browser`

> Hacker! You role isn't admin!

返回了一个`role=ee11cbb19052e40b07aac0ca060c23ee`的 Cookie，[md5解密](https://www.cmd5.com/)下是`user`改成 admin 加密回去`role=21232f297a57a5a743894a0e4a801fc3`

> Please request me with BYTES method!

请求方法修改为`BYTES`

> Please pass me form data
> variable: fruit
> value: (&#39;b&#39;+&#39;a&#39;++&#39;a&#39;+&#39;a&#39;).toLowerCase()
> variable: token
> value: Your Token From weilei.studio

`('b'+'a'+ +'a'+'a').toLowerCase()`执行的结果是`banana`

用 form-data 发下包就行

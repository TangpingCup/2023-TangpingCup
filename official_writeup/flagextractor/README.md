# [Binary] 躺平flag提取器

- 命题人：ZianTT
- 我真的不到啊：200 分
- 太美丽了家人们：400 分

## 题目描述

<p>畅销哥在使用了chatgpt之后感觉这太酷了，很符合他对未来人工智能的想象，科技并带着趣味，于是他爆肝十个甚至九个小时，做出了一个flaggpt，意在自动进行从做题到拿奖的所有工作，这是程序的第一次调试：</p>
<div class="well">
┌──(root㉿helang-dev-server)-[~]
<br>
└─# ./flaggpt "请给出一个UNIX程序，直接运行即可产生flag"
<br>
<br>
Saving to: ‘./flag’
<br>
 100%[=================================================>] 1/1
</div>

<p>但是畅销哥运行的时候，程序却出现了问题，原本应该给出flag的程序，却向他索要flag。他询问flaggpt，却被告知“我不到啊”，此后，无论询问什么，flaggpt只剩下同一句回复，“我不到啊”。</p>
<p>于是畅销哥询问了本题出题人，出题人使用了114514ms就告诉了畅销哥埋藏在生成的文件中的两个flag并拿到了一血。</p>
<p>畅销哥非常生气，他坚信让flaggpt魔怔的问题就在那个生成的文件中，你能帮助他拿到文件中的flag吗？</p>
<div class="well">
<strong>萌新入门指北</strong>
<p>这是一个Unix程序，你可以直接在命令行执行它。但是要想拿到它的内容，你似乎得反编译它？然后查看下它的……伪代码？</p>
</div>

<div class="well">
<strong>第二阶段提示</strong>
<p>
rot13不仅rot了文字，还干了什么？看看源码？
</p>
</div>

**[【附件：下载题目附件（reverseme）】](attachment/reverseme)**

## 预期解法

用ida打开，F5看源代码，打开CheckPassword看到flag1。

接下来在main函数中找到一段被简单加密的密文，跟踪ROT13函数，看看源码，分析后得到是对文字进行ROT13，数字进行ROT5，丢进CyberChef解密即可。

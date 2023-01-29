# [Algorithm] V我≈50

- 命题人：ZianTT
- 题目分值：400 分

## 题目描述

<ul>
<li>V我50！</li>
<li>我可以给你49.99，可以给你50.01，但不可以给你50！</li>
<li>V我50.01！</li>
<li>但我现在不想给你了，你猜猜我想给你多少？猜对我就V你！我很慷慨，至少给你45，但不会超过55！</li>
<li>你清高！</li>
</ul>
<p>此时，有一张纸向你飘来，上面写着</p>
<blockquote>
<p>seed = int(time.time())</p>
<p>random.seed(seed)</p>
<p>v = 45 + random.random()*10</p>
<p>target = "%1.2f" % v</p>
</blockquote>
<div class="well">
<strong>第二阶段提示</strong>
<p>
这个种子，是时间？那我也可以生成一个一样的？
</p>
</div>

**【网页链接：访问题目网页】**

## 预期解法

根据给出的代码片段，可以推出种子是当前时间戳

可以输两次，然后爆破种子

```python
import string
import time
import random

def strcmp(str1,str2):
    if str2[:len(str1)] == str1:
        return 1
    return 0

def rand01():
    return random.random()

def getv():
    v = 45 + rand01()*10
    return v

def main():
    rngmiddle = int(time.time());
    print(rngmiddle);
    maxjitter = 5000;
    

    v1 = float(input())
    v2 = float(input())

    sig = 1;
    for i in range(maxjitter):
        seed = rngmiddle + i * sig
        print(seed)
        random.seed(seed)
        vtest1 = getv()
        vtest2 = getv()
        diff1 = abs(vtest1 - v1)
        diff2 = abs(vtest2 - v2)
        if (diff1 < 1e-2 and diff2 < 1e-2):
            print("Match!")
            v3 = getv()
            print("%1.2f %1.2f" % (diff1, diff2))
            print("%1.2f" % v3)
            break
        else:
            print("%1.2f %1.2f" % (diff1, diff2))
        sig = sig * -1

main()
```
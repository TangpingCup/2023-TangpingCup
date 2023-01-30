# 解
F12得

```html
<!-- ARAS domain prob01.weilei.studio -->
```

通过提示，构造HTTP Basic Auth参数，得

```
Authentication: Basic base64("BytesSec:"+YOUR_TOKEN)
```

请求后获取cookie，得token和hint，token一眼jwt

然后在jwt里面检测digest是否匹配（密码114514），相同后把username改为admin

接下来解码得到的b64，得网址 https://ilrxbzij.weilei.studio/r3dp4cke7

无法登录去掉disabled属性

接下来助力，post了一个ip的参数，自己写脚本爆破去吧.


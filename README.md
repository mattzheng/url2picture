# url2picture
Let URL to Picture in python

笔者的URL格式如附件image.csv

核心是利用：urllib,urllib2中的urllib2.urlopen(URL).read()

总的来说，能够使用，但是如果数据量太大，可能会出现比较慢的情况。

而且遇见异常情况，会直接Pass，并不会保存URL。

URL中，图片保存的命名规则跟图像的唯一ID一致。

By Matt

2017-5-2

BLOG:http://blog.csdn.net/sinat_26917383

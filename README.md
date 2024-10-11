# url-domain-utils
custom url domain utils in python

# get_domain_from_url
>>> get_domain_from_url('http://www.abc.baidu.com.cn')
'abc.baidu.com.cn'
>>> get_domain_from_url('https://www.baidu.com.cn')
'baidu.com.cn'
>>> get_domain_from_url('www.baidu.com.cn')
'baidu.com.cn'
>>> get_domain_from_url('http://www..baidu.com.cn')
'baidu.com.cn'
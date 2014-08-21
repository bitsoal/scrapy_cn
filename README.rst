Scrapy project as a chinese tutorial 
====================================
scrapy中文学习项目

以抓取豆瓣图书中的编程图书为例：
地址：<http://book.douban.com/tag/Programming>

requirements::

    scrapy >= 0.22
    python == 2.7

Install::

    git clone https://github.com/addwork/scrapy_cn.git

Usage::

    $cd demo/scrapy_cn
    $scrapy list
    $scrapy crawl onepage

Build with docker::

    $sudo docker build -t addbook/scrapy-docker .
    $sudo docker -t -i addbook/scrapy-doccker
    $root@xxxxxx:scrapy

.. Image::./doc/images/scrapy_docker.jpg

项目介绍
--------------------------

项目结构::

    scrapy_cn/
        -doc/       ...关于工具插件的使用指南
        -tools/     ...开发中scrapy有用的插件，使用参考doc
        -demo/      ...简单的中文网站抓取爬虫实现
        -crawl/     ...较大规模的爬虫设计以及配置
        -linkbase/  ...Linkbase基础爬虫实现
        -schedule/  ...可调度爬虫的简单实现
        -distrib/   ...分布式负载

Contact:
----------

 * QQ群:282889215  
 * blog:<www.addbook.cn/scrapy>  

TODOS:
-----------------

 * 开放部分scrapy用到的组件
 * 设计一个大规模爬虫的范例，以示大规模爬虫设计的要点，以及解决常见问题手段
 * 开放Linkbase抓取的爬虫
 * 开放可管理调度任务的爬虫
 * 大规模任务负载的分布式处理实现

Lisence
===========

   BSD Lisence

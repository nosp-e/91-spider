# NineOne Spider

使用python异步框架写好的一个91的爬虫，可以爬取最近的视频信息。

使用方法：

```bash
python main.py list
python main.py page
```

需要体验一下的，只要安装依赖的库然后运行这两个命令就可以了，已经设置好了默认参数（国内的梯子请自己准备哈）

可以打印`python main.py list --help`看看帮助信息，默认的下载位置是本目录的data文件夹内。

专业的工具做专业的事，本仓库只专注于爬取信息，并不关心后续的下载；为了完整的下载，接下来要做的事情还有；

**一、去找一个m3u8下载器，将链接下载成视频。**

作者使用的是：https://github.com/HeiSir2014/M3U8-Downloader
，该项目的releases提供win和linux版本的GUI程序，同时可以批量下载，非常方便。

本项目生成的m3u8链接文件也是按照该下载器的批量下载格式生成的。

**二、找一个合适的播放器/视频管理器**

要求不高的话就随便找个播放器就完了，推荐几个还算好用的，

* windows：win10自带的“电影与电视”，将你的下载目录加入到该软件的视频库目录中，然后就可以预览所有的视频文件了；
* linux：使用类似NAS的解决方案，比如jellyfin；会用linux看这个的老哥起码的部署应该是懂的，可以用docker简化流程；

**Ref：**
* https://github.com/jakehu/91porn

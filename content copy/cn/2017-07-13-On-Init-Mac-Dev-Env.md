---
layout: post
title:  "如何优雅地配置Mac开发环境"
date:   2017-07-13 12:40:09 +0800
categories: tools
---

拿到新Mac机，要为程序开发来配置开发环境。这是个特殊的事，新手和老鸟感觉不同。新手不知道要做什么、怎么配置，什么都很困难、也很新鲜；老鸟轻车熟路，却觉得一步步操作很烦人。今天我看了[李笑来](http://lixiaolai.com/2016/06/16/makecs-basic-dev-env-settup/)、[nicolashery](https://github.com/nicolashery)、[donnemartin](https://github.com/donnemartin)三位前辈的配置说明，我想从新手的视角谈谈，怎么能把这事做得优雅。

## 有什么“不优雅”吗

给计算机安装软件工具包，这么简单的事情，还谈什么优雅？嗯，是的，因为我觉得自己之前做得不够优雅，表现如下：

### 不知轻重，闷头赶路

跟着全栈营公开课的指导，[安装Xcode](https://fullstack.xinshengdaxue.com/posts/8)，又[安装Command Line Tools](https://fullstack.xinshengdaxue.com/posts/9)，据说后者是Ruby的Library。

其实如果不是要开发Mac或iOS的app，没有必要安装几个G的Xcode（后续不时被App Store提示更新），可以只安装它下属的Command Line Tools就可以了。

全栈营的步骤冗余，说法有误。我不懂，也没查，听一家之言，给我我就抱着，先往前跑，赶路要紧。

### 不看文档，粗浅使用

全站营要求我们下载使用Atom，没有理由，就说新手推荐用Atom。我们的课程交流也都是Atom截屏。

李笑来老师没讲理由，但是给了以身作则的榜样。在编辑器部分，他让我们不要参与哪个编辑器最强的论战，不如节省时间和精力把能力练强。他建议我们在Atom体系下，做三件事：

1. 第一步读官方文档 [Atom Flight Manual](http://flight-manual.atom.io/) ，至少应该先认真阅读第一章。这是了解工具的能力。不至于把冲锋枪当做砍刀来用。
2. 上网搜Atom的[Cheatsheet](http://d2wy8f7a9ursnm.cloudfront.net/atom-editor-cheat-sheet.pdf)，好好读一读，或者打印出来。这里的半小时，省的是一辈子的时间。因为你也不知道跟这个工具要打多少交道，也许就是一辈子。
3. [积累自己的自动填充](http://lixiaolai.com/2016/06/17/makecs-atom-advanced/)Snippets集，为今后自己学习的每一种语言（Atom的Snippets有Scope功能），自己搜集和改造自动填充段子。这里强调“自己”，是因为只有知道“有”，才知道“用”啊。

你看，我没有耐心读官方文档，也没有好奇心去Google

> - Atom cheatsheet
> - favorite atom packages
> - most popular atom packages
> - must have packages for developer

更没有严肃认真地使用snippets功能。全栈营三个月来，敲html代码无数，都是`<%  %>`这么敲过来的。浪费这个时间是不是有必要？或者这个“笨功夫”，应该花在读文档上面？

### 有用没用，都想装装

前天为了建静态网页，需要安装jekyll。[Jekyll的官方安装指导](https://jekyllrb.com/docs/installation/)中说，前提要求是安装有GCC和Make。我就去找GCC来装。[GCC官网去看](https://gcc.gnu.org/install/)，字号好小，字数好多，怎么下载，怎么安装，老半天讲不到重点。第二天我还是下载到了，但是没有安装，因为没耐心了。我看[阮一峰大哥的建站指导](http://www.ruanyifeng.com/blog/2012/08/blogging_with_jekyll.html)，没有特别提到有“GCC这一难”呢。

果然不用装，也正常运行jekyll了。我真想骂人，官网随口一句话，给我这样的菜鸟挖大坑啊。

今天看到[nicolashery](https://github.com/nicolashery)、[donnemartin](https://github.com/donnemartin)二位的指导repo，一个娓娓道来，一个刷刷自动，让我佩服得五体投地，同时生发一种冲动：既然这么简单，不如把十八般武器都装到身上！多亏我有个毛病：看热闹行，执行力差，才没有让电脑和我自己都被拖累死。

## 什么是我心中的“优雅”做法

类比家里或办公室装修，在配置环境这件事上，我认为要把握三个问题：

1. 在这环境里做什么事？
2. 环境怎样和人互动？
3. 怎样良性发展，提升人与环境的和谐感？

具体落实到给Mac配置环境这件事情上，如果我拿到表弟的新电脑，我会做以下三件事：

1. 问他想开发什么东西，用什么语言？然后就只装现阶段必要的东西。
2. 给他看成熟程序员都用什么工具，配置什么东西，让他自己读最常用工具的必要文档。
3. 为了做好事情，如何与工具相互磨合，给他一些建议。

上面三点，从空间方面看是留白，从感情方面看是尊重，从时间方面看是和谐。也许这就是我心中的“优雅”。

---

2017年7月13日，周四，19:32初稿。

2017-07-21-Fri 补充安装过程记录。

---

PS：昨天的重装进程。

### 重装系统 50分钟。

### 设置system preference

- 光标移动速度调至最快，键入延迟减到最低。
- 设置鼠标移到右下角触发关闭屏幕动作，移到右上角出发回到桌面动作。
- 输入法添加日文，用cap键切换中英输入。
- Dock自动隐藏，移到屏幕左边，避免Dock不自动隐藏的话，干扰屏幕下方的输入区域。

### App Store的已购项目中恢复软件

- 微信
- 印象笔记
- MindNode 2
- 云梯从官网下载，这里的版本没有测速功能。
- 网易云音乐
- iPic图床
- 暂时不装Numbers
- 暂时不装Pages
- 暂时不装Keynote
- 装载2.5G的iMovie，我要做照片视频
- 肯定不装GarageBand
- 暂时不装有道云笔记
- 购买Moom，68块钱。

### 安装Chrome（链接VPN保证版本）

### 安装iTerm，官网下载dmg

- 配置色彩方案为Solarized Dark
- 安装微软字体Consolas
- 借用Nicolas的profile，promote，和aliases。

### 安装Command line tools

- xcode-select --install就够了。Xcode几个G，一般没有必要。
- 这个过程我第二次花了一刻钟。
- 有了它，你才能从源代码搭建东西。

### 安装[Homebrew](https://brew.sh)

- 它是OS X上最常用的安装包管理器。
- 记住brew help是个入口，众多用法在里面看。

### 安装Git

- 用brew装，很简单。我此时是2.23.3版。
- 借用Nicolas的gitconfig，给Git上点颜色，里面也写了几个aliases。
- 给gitconfig里添加用户名和邮箱。
- 用HTTPS加密，而不是SSH。
- .gitignore注意包含`.DS_Store`,还有其他隐藏文件。参考nicolas的文件实例。

### 安装编辑器Emacs

- 从陈斌那里Git下来就可用，但是不会用，开始很傻，连鼠标都动不了。

### Python的安装

- nicolas的做法有不足，brew装的是2.7版，还默认带了pip。我需要用3.X版。
- 准备用python.org的指导文档。
- 完毕。

## Mac自带的拼音输入法打出怪字

——2017-07-25-TUS 补此条

门，一个框子上面纵穿一个小竖。关，复，这两个字都只占右3/4字宽。好奇怪。

Google了“Mac OS 拼音输入法 怪字 字体”，似乎没有人遇到过我的问题。都是讲怎么安装新字体。

有人在知乎问[如何查看MAC OS默认的字体](https://www.zhihu.com/question/19693837)集。这给了我提示，是不是我的系统默认字体不那么支持中文简体，导致拼音输入法所调用的字体也就错乱。

我在system preference的language & Region里看到，我虽然在输入法中添加了拼音输入法，但是系统语言只有两种：英文和日文。果断添加中文，系统提示是否作为主要语言，是。重启电脑，拼音输入法不出现怪字了。把主要语言切换回英文，重启。拼音输入法一切正常。

在MindNode中接着打字，字还是怪。这里可以看到它正在使用一种日本罗马字命名的语言。懂了，只有英文和日文语言，拼音输入法找到了日文汉字包，所以出错。

明白了：

1. 语言和地区，选好地区，也注意语言。可以用英文为主，但是不要忘记添加中文。
2. 日文汉字有的很乖，比如哪个门字。
3. 语言和键盘，是操作系统的两个模块，互相有影响，但是不是一回事。

---



未完待续。




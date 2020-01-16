---
layout: post
title:  "怎样拥有一年成为python高手的能力(像科研一样严肃对待这个笑话)"
date: 2017-07-17 09:59 +0800
categories: roadmap
---

Python先天具有喜剧基因，但我不能把它当成一个笑话。陈斌学长写了一篇《[一年成为 Emacs 高手 (像神一样使用编辑器)](https://github.com/redguardtoo/mastering-emacs-in-one-year-guide/blob/master/guide-zh.org)》。文章侧重从方法论的高度讲怎么做。我读了以后很受启发。参考陈的指点，落实到自己身上，我想梳理一下我的想法——怎样在凸轮廓线设计这个项目中，拥有一年[成为python高手](http://200ok.ch/posts/how-to-become-a-proficient-python-programmer.html)的能力。

强调一下，我不是要一年成为python高手，而是拥有这种能力。从小白，到新手、熟手、专家，最后被称为大师，这不是短期可以走完的路，也不是自己努力就可以的。但是，我想，我可以参考前人的指点，做好三方面准备：1. 确立目标；2. 掌握方法；3. 积累知识。这样，当因缘际会来临时，我也可以在一年内成为python高手。

## 什么是python高手

让你证明自己已经跻身高手行列，你怎么讲？

陈在他的文章里，把这个“跨入高手行列”做成了超链接，指向他的Github主页。请你看他做的事情，看他的代码——这就是高手的明证。我能在一年内写几个项目，参与几个项目？江湖上，高手不是自封的——你杀了多少人，救了多少人，你谁跟你打过架（而当下你还活着）。

让你描述某种技术的高手的状态，你怎么讲？

具体到python，Lafon哥哥提出了四个方面：1. 多用[函数式编程](https://en.wikipedia.org/wiki/Functional_programming)，我理解是一种自律的思考方式，有好处，但是麻烦；2. 明白运行效率，是语言高级低效，还是程序员算法不够高明？3. 善用测试／行为驱动，好像不用这种做法，不是笨就是懒；4. 符合编码规范，让别人看着舒服，也包括将来的自己。通俗来说，就是：表述问题，设计算法，证明质量，保持优雅。这四个方面都做好了，一个工程师就堪称高手。

喜欢某种状态，同时做出某些成就，二者一致。这就是我心中定义的高手。

## 为什么要成高手

本文重点在于怎么做，而不是说理。这里只简单谈三句话。

首先，我有一个要完成的事，它最好用python写算法，与FreeCAD做接口。这个工作我想开源出去，需要搜集实例，需要持续更新改进，是个无底洞。

其次，我的朋友推荐从python入门做程序员，他们会提供帮助。当然，首先是我自助，python的文档写得很好——天龙八部里的扫地僧说：自救宝典给你们摆在那里……

最后，按我现在的价值观，一半没意思，要做就做到“非常”好，而python支持的领域里有[大项目](https://www.openstack.org/)（多出大牛），多是开源（能见到好代码）。

另外，补充一些非个人因素：

1. Python的库很多，有标准库，也第三方库，更新很快。
2. 目前最大的开源项目OpenStack就是用python写的，也就是说，python在可预见的未来，永远存在。
3. python语言规范与时俱进，新老版本兼容都成问题。
4. python是解释型语言，发布软件就等于公开源代码。软件更新，也会看到改了哪里，开发者也会写为什么改。

## 学习榜样是谁

榜样永远是人，人永远是最好的学习对象，因为我们脑子就是长成这个样子的。

### 中国的python开发者

廖雪峰，他写了本《[小白的Python教程](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000)》讲得简单易懂，内容全面，[Github](https://github.com/michaelliao)更新也很勤奋。

其他人，慢慢认识。

### 英语世界的python开发者

[Julien Danjou](https://julien.danjou.info/)，他参与openstack项目后，写了[The Hacker's Guide to Python 1st](http://ebook-dl.com/book/1642)这本书，讲编码的另一条腿。

Allen B. Downey，他的书《[Think Python: How to Think Like a Computer Scientist](http://greenteapress.com/thinkpython2/html/index.html)》我计划用三个月读两遍。[他的github](https://github.com/AllenDowney)上有所有图书的Latex源码。

### [FreeCAD的贡献者](https://www.freecadweb.org/wiki/Contributors)

Github上的[主程贡献者](https://github.com/FreeCAD/FreeCAD/graphs/contributors)。

[FreeCAD_assembly2](https://github.com/hamish2014/FreeCAD_assembly2)，16位贡献者。刚刚看了[BPLRFE](https://github.com/BPLRFE)，他在youtube上有德语和英语的FreeCAD使用教程。

论坛上有位哥哥冒泡，专业机械工程师，副业设计制造家具，六月份[申请做贡献者](https://forum.freecadweb.org/viewtopic.php?f=10&t=22858)，大家给了很具体的建议，比如从哪个模块开始。mika38[建议给所有潜在贡献者做引导贴](https://forum.freecadweb.org/viewtopic.php?f=21&t=21533)，大家热烈鼓掌，mika认真调研，yorik哥哥露面，建议他做在沙盒里面，先。

yorik哥哥的[个人博客中关于FreeCAD这个tag下的文章](http://yorik.uncreated.net/guestblog.php?tag=freecad&complete=3)，原来大家能做这么漂亮的模型了。

r-frank做了德语和[英语的tutorial视频](https://www.youtube.com/watch?v=_HEvhclR4-o&list=PL6fZ68Cq3L8k0JhxnIVjZQN26cn9idJrj)，他还在签名档贴出了他在[GrabCAD](https://grabcad.com/)这个平台上的[FreeCAD模型](http://grabcad.com/bpl.rfe-1/projects)。

## 为什么要跟人

1. 学以致用。学习软件是为了用，用来解决现实世界的问题。跟着正在解决问题的人，加入他们，尽快跟上他们，才是正确的姿态。
2. 镜像本能。他们在讨论，在吵架，在用riddled with misspellings的英文长篇大论地提建议。我看到这场景，就发生在眼前，发生在几天前，就好像自己也参加了一样。
3. 江湖成名。这是一个不以金钱为标杆的圈子。我能力如何，关心的问题是否真的有趣，解决办法是不是最佳，得由圈子里的技术同僚来评判。在一次一次的交往中，积攒点赞，积累名声，同时也是转化自己。我会变得更热心，更有效，更招人喜欢。

## 怎么跟他们学，学什么

订阅他们的某个Github项目，跟踪他们想什么问题，做什么，就像软件维护记录。学习怎么找bug，怎么改，怎么完善。

尽快入门（能读懂文档，能知道他们在讨论什么），快点明确自己关心的问题所属领域，然后在Quora、Reddit、Google+论坛上跟踪相应话题，反复精读。学习怎么提问，怎么调研，怎么建设性地提建议，怎么优雅地收工。

在领域内积累大牛名单，订阅他们的博客。看他们在思考什么问题，在用什么技术，在参加什么项目。同时也在学习怎么思考，怎么写作，怎么对世界有所助益。

善用Youtube平台。在youtube上搜索python tutorial/best practice/example/tricks/cookbook/awesome，试试看，python写的搜索引擎会推荐最受欢迎的影像。看到人在讲python，在用python，我才能有带入感，就好像是我在讲，我在用。

## 通读文档，通读文章

半天的争论，半辈子的偏见，也许就差半小时的文档通读。比如github主副协作那次争论，比如atom编辑器是给dummy用的，简单地看一看官方文档，问题烟消云散。

通读文档是个好习惯。哪怕暂时读不懂，也可以把它读完，至少大致了解它都讲了什么，以后再回来详细读，肯定要回来详细读。

一般来说，[官方文档](https://www.python.org/about/)和[官方教程](https://docs.python.org/3/tutorial/)比私人教程质量高，因为它往往由开发者中最擅长这个主题的人撰写，经很多人一起优化而成。当然，真正好的私人教材，也会被官方文档[推荐](https://wiki.python.org/moin/BeginnersGuide/Programmers)。

要搞清楚文档／教程的优先级。首先是官方Get stated，然后是官方tutorial，然后是youtube的screencast，然后是完整docu，然后是私人GuideBook，然后是Cookbook，然后是philosophy。我想最好是这样。而我现在，一上来就是Cookbook，活着是philosophy，要么只会抄代码，要么只谈经验。这样不行，要养成尊重文档的习惯，也养成写好文档的习惯。

## 足够的广度，适当的深度

陈斌说：作为新手，最重要的是打好基础，让自己的知识面有**足够的**的广度和**适当**的深度，否则会在一些琐碎问题上浪费时间。

我的做法是，一方面高到云端，一方面低到谷底。既然有缘捡到了《python高手之路》，那就先翻一下他讨论的主题。了解一下实际项目中，大家关心什么问题，为什么这些问题是一名hacker要解决好的问题。2014年，我启动了《Think Python》，学了三四章，后来忙起来就放下了。它的主题是怎样像计算机科学家一样思考，养成好的处理问题的习惯，并不局限于哪一种语言，所以同样的主题，先有think java，后有think C++。

打个跨界的比方。*Think Python*是达摩用少林拳这套动作打武术的根基，养成好身体。*The Hacker's Guide to Python*是索罗斯写的哲学书，超越于具体投资之上的见识。

当然，我要解决具体问题，不能两头够不着。下一步，官方的python tutorial，就很好地讲解了语法问题。那时，关键是我要编程用起来，解决我的问题。

## 用实际问题作为切入点

我要学python，就写一个[爬虫插件](http://webscraper.io/tutorials)，专门把水源BBS上的个人文章，搜集下来按照时间顺序做成epub书。

争取一个月一个车库项目。

先找点小成就，玩玩。

照顾好自己的情绪。据说，它是第一生产力。

## 给网络增添趣味

我想向[John Walker叔叔](http://www.fourmilab.ch/)学习，给网络世界增添一点我的趣味。

具体来说：

1. 记录我想了什么。虽然可能没人有精神读，但是未来外星文明瞬间扫描地球文明的时候，也许能见到有我这么一个个体的故事。
2. 消化我学了什么。从英文世界消化过来的东西，翻译回中文，大概没有必要，也真没有必要。记录消化过程的个性感悟也许有价值，我不知道，也许有人会看到价值——至少我会。
3. 积累我造了什么。我会写一些故事，几则笑话，若干幅画，读书提要，暗记卡片，等等。这是我的原创，别人看不看随意，我会积累在这里。
4. 搜集有趣的链接。比如，给某个领域的网页书签做一个索引说明，整理某种有用的公开资料，放在自己的网站上。
5. 建立个人云端库。我写的画的东西，也纳入github管辖吧，网站上不主推，但是我会让链接有效。

以上这些内容，都用汉语完成。我总觉得，跟中国人讲英语的人，也会去跟老外讲汉语。

## 答疑集

暂无。

---

以上，7/17起头，7/18写完。

英文名：2017-07-17-how-to-gain-competence-on-python-in-one-year

中文名：怎样拥有一年成为python高手的能力(像科研一样严肃对待这个笑话)
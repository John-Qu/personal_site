---
title: 学习做成我的兴趣雷达
subtitle: 
author: John Qu
date: 2020-07-24
slug: mechanics-on-attraction-radar
tags:
- 
categories:
- 
typora-root-url: ../../static
show_toc: yes
---

## 直达成果

这里是[我的兴趣雷达图](https://radar.thoughtworks.com/?sheetId=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F1_lHFMIZTJnjO0ZftooSPZ5ni3rrOhnNPz_2mwQeOzMU%2Fedit%23gid%3D0)。

![Screen Shot 2020-07-29 at 21.07.42](/images/2020-07-24-Build-my-own-Radar-on-Attraction/Screen%20Shot%202020-07-29%20at%2021.07.42.png)

四个象限的内容分别是：
![Screen Shot 2020-07-29 at 21.08.04](/images/2020-07-24-Build-my-own-Radar-on-Attraction/Screen%20Shot%202020-07-29%20at%2021.08.04.png)
![Screen Shot 2020-07-29 at 21.08.32](/images/2020-07-24-Build-my-own-Radar-on-Attraction/Screen%20Shot%202020-07-29%20at%2021.08.32.png)
![Screen Shot 2020-07-29 at 21.08.46](/images/2020-07-24-Build-my-own-Radar-on-Attraction/Screen%20Shot%202020-07-29%20at%2021.08.46.png)
![Screen Shot 2020-07-29 at 21.09.02](/images/2020-07-24-Build-my-own-Radar-on-Attraction/Screen%20Shot%202020-07-29%20at%2021.09.02.png)

单个条目展开是这个样子：
![Screen Shot 2020-07-29 at 21.24.24](/images/2020-07-24-Build-my-own-Radar-on-Attraction/Screen%20Shot%202020-07-29%20at%2021.24.24.png)

搜索框可以这样用：
![Screen Shot 2020-07-29 at 21.21.18](/images/2020-07-24-Build-my-own-Radar-on-Attraction/Screen%20Shot%202020-07-29%20at%2021.21.18.png)
![Screen Shot 2020-07-29 at 21.21.34](/images/2020-07-24-Build-my-own-Radar-on-Attraction/Screen%20Shot%202020-07-29%20at%2021.21.34.png)

原始文档中的数据这样就可以：
![Screen Shot 2020-07-29 at 21.13.05](/images/2020-07-24-Build-my-own-Radar-on-Attraction/Screen%20Shot%202020-07-29%20at%2021.13.05.png)

它通过 radar.thoughtworks.com 调用 Google Sheet 生成，我用的 [Google Chrome](http://www.google.cn/chrome/) 或 [Chromium](https://github.com/jjqqkk/jjqqkk) 浏览器。 

## 技术缘起

我这周都在看 Thoughtworkers 的文章，比如[熊节的](https://www.google.com/search?q=site:gigix.thoughtworkers.org+%E6%9C%9F%E6%9C%9B)。我喜欢他们的[洞见博客](https://insights.thoughtworks.cn/category/tech-radar/)和[技术雷达](https://www.thoughtworks.com/radar/faq)。[Darren Smith](https://www.thoughtworks.com/profiles/darren-smith) 在 *[Birth of the Technology Radar](https://www.thoughtworks.com/insights/blog/birth-technology-radar) / Tracking tech maturity* 小节讲了他想到雷达这个类比时的初衷：“gates that would trigger different activities”。Neal Ford 提倡“[Build Your Own Technology Radar](https://www.thoughtworks.com/insights/blog/build-your-own-technology-radar)（[打造你自己的技术雷达](https://insights.thoughtworks.cn/build-your-own-technology-radar/)）”，他讲了公司建技术雷达的[诸般好处](https://www.thoughtworks.com/radar/byor)，又说一个人理所应当地（他年轻时吃过亏）有自己的技术雷达。二者匹配性怎么样 ，甚至可以在面谈时碰撞一下子。

见贤思齐，我也想学着做一个，借机梳理一下自己的思路。

## 不是什么

### 技术雷达

我不是一个提供专业服务的公司，也没有稳定在某个职业路径上，写不出特定领域的技术雷达。如果不清楚搜寻哪类目标，雷达也就失去了预警的作用。一家德国的时尚在线平台 [Zalando](https://zalando.com/) 跟随 ThoughtWorks 做了自己的[技术雷达](https://opensource.zalando.com/tech-radar/)，薄荷网工作的[马陆骋](https://www.songofcode.com/sliders/build-your-own-technology-radar/index.html#/)做了一份[技术雷达](http://www.songofcode.com/technology-radar/tech.html)，一份[读书雷达](http://www.songofcode.com/technology-radar/reading.html)。

### 读书雷达

Thoughtworkers 们在张逸的带头之下，做了三版（[2013](http://agiledon.github.io/blog/2013/04/17/thoughtworks-developer-reading-radar/)、[2016](https://insights.thoughtworks.cn/reading-radar-2016/)、[2019](https://insights.thoughtworks.cn/reading-radar-2019/)）读书雷达，还有分语言的“[C#读书雷达](https://insights.thoughtworks.cn/csharp-reading-radar/)”，分领域的“[公益+互联网篇](https://insights.thoughtworks.cn/reading-radar-p3/)、[业务分析师（BA）篇](https://cloud.tencent.com/developer/article/1104501)”。在最近这一份读书雷达的[序言](https://www.douban.com/doulist/120532290/)中，张凯峰说“三年过来，并没有那么多令人振奋的知识或者技能，能够彻底触动我们的内心，心悦诚服地将它置于同一份书单中。”可见这份雷达并不是搜寻新目标用的，而是列出了在 ThoughtWorks 工作的一些人对些工作所需读的书的一个共识。这一个猜测也可以从他们把环分为“初级、进阶、高级”看出来。还有，头两版把“初级”放在内环，近一版把“高级”放在内环，虽然从环的角度都说得通，但是从雷达的角度，外环表示远，内环表示近，雷达图可能不是合适的类比工具。读书列清单就好了，没有必要画在图里，因为我们只能根据兴趣或问题，一本一本地读，不需要全盘考虑。

### 半径算法

需要用环形图全盘考虑的事情，有一种是喻颖正提出的“半径算法”，专治信心膨胀后的贪婪。人有三个半径：行动半径，能力半径，和认知半径。行动半径要尽量缩小，这样它与能力半径之间在有足够的安全空间。认知半径要努力扩大，这样才知道还有什么不知道。半径算法只是一种哲学比喻，都算不上形象，因为半径之内的空间并不是圆，边界也很难清晰定义。要分出象限来就更难了。它提醒了我要向哪个方向努力培养能力，也警告了我要在哪里深挖创造价值。

### 黄金圈

从老喻讲 OKRs 的文章中又一次看到“黄金圈法则”，讲更能让人买账的不是最终的产品，而是作为初衷的故事。核心是“为什么”，讲意义挖掘，内圈是“怎么办”，讲战略规划，外层是“做什么”，讲战术执行。我想了一下自己的故事，似乎能自圆其说，但这不适合用雷达象限图来表达。

### 资源列表

周一的时候本打算做三张雷达图，分别对应这三周来我调研的三个方向上的资源：1 工业软件技术服务工程师、2 传统企业数字化咨询师、3 技术冲击下人的转型再培训。随着思考的深入，我越来越发现这三个方向不是并行，而是串行。尤其在想通了黄金圈的故事之后，我意识到我只能先做好第一件事，才有信任资本来谈第二件、第三件。为了让给 OnShape 和 ThoughWorks 准备的简历不落空，我必须达成开源发布 TetraCamThon 项目这个目标，完成它的几个关键结果。对此，我需要找到一种办法管理自己的关注点，既能抓住技术新动向，学习有效经验，也能保证精力不分散，在重点题目上投入大块时间。所以，我要用雷达图来区分各方向上关注点与当下主题的远近，也就是说，我要做的是一张特定时段做特定主题时的兴趣雷达。

## 创建初衷

除了学以致用，我为什么要做这样一个雷达？它对我本身有什么好处？要回答好处的这样的问题可以有两个角度，一个是从正面说它能带来哪些利益，另一个是从反面说它阻止了哪些损失。目前它主要是一个防御性工具。将来在恰当的时机，比如找伙伴时，它也可能成为进攻性武器。

### 阻止自己喜新厌旧

我买书常常读不完。主要因为读书要时间得有耐心，读前想象得太美读下来灰心，另一方面这个时段内总有（或总能找到）新的书来激发新的想象。雷达这个圆环让我一目了然地知道自己的注意力分布在哪些主题上面，帮助我维持住足够的自知之明。

### 提醒自己不要健忘

我好奇的主题多，可往往没时间深究。去年在得到 app 的电子书库，我常常深夜翻它又上线了什么新书。遇到好书想读，不买，先截屏留个念想。现在有了电子书会员，却记不得去年心心念念的书大都是什么了。

### 知行合一要事要美

雷达侦测敌机或导弹，离得越近就越要重视，要采取行动。内圈的主题，要么正在做，要么做出点感觉，都要投入足够时间和精力。有了这个图，盯着中心的主题，我要对得起它们的地位。

## 原则纪律

### 实时记录

它只是我自己的雷达，不必与朋友同事讨论，不必设定半年一年的见面频率。我会在有新点子进来时就更新，顺便过一遍老条目，至少每半年做一次集中清理。注意，放进来新的项目一定要写注释，讲清楚：为什么放进来，打算怎么做，有哪些资源。在环间移动的项目，也一定在注释中记录一句。

### 有出有入

雷达监测物体动态，移动是应有之意。条目要尽可能具体，这样才容易判断它与目标的关系，决定它与我的远近，才可能及时移动。我想对粒度的把握以保证半年之内它可能完成或退出为宜。

### 名词主题

记录的是主题，而不是资源，也不是动作。在一个主题之下，可以有很多资源，比如好几本书、好几门课，我是为了搞懂这个主题下的几个问题，然后来做事情，而不是为了读完一本书、上完一门课。在一个主题之下，可能有几个相关的动作，而这些动作在不同的目标之下，指向也不同。因此不如留下空白，不指明具体动作。

## 技术细则

### 环

远近区分态度。“兴趣”的第一英译词是 interest，作动词用的 interest 有这样几个近意词 – To concern; excite; attract; entertain; engage; occupy; hold. 我看正好可以用来表达我的投入程度。

#### Hold 等等

Hold 在我这里一方面有“握住别放跑了”的意思，另一方面有“Hold on 等一下”的意思。在这个区间里的题目与眼下的工作和生活主题不相关，在可见的未来不宜投入时间精力，记录想过它就够了。如果是了结旧事，可以略作深入。

#### Concern 上心

Concern 是说我在关心，正在找材料研究一下这个主题。可能还没有实践，但在可见的将来有这个机会。

#### Engage 投入

Engage 是说我投入了，投入地在它上面做事情。我与它生活在一起，处于磨合之中。

#### Occupy 有了

Occupy 是说我获得了，已经在这个主题上有像样的成绩。我的生命已经打上了它的烙印。

### 象限

象限区分方向。用内外和根叶两个维度，划分出四个象限。也许我的分类命名并不完备，但我不喜欢在四个象限中加入“其它”。

#### Profession 专业

这是与专业工作有关的知识，讲概念，是什么。

#### Concrete Life 生活

吴军老师说，生活是具体的。生而为人不容易，有很多事情值得探究。

#### Meanings 意义

本来想用 “Spirite 精神文明”来指这个象限，但我想它谈的是与科学理性相对的体验和信仰问题。

#### Methodology 方法

在哲学层面讲认识论和方法论，我喜欢这些话题，也喜欢具体的操作指南。

### 图标

图标的形状表达这个点的动态，颜色表达区分象限。ThoughtWorks 最新一期技术雷达区分了三种状态：原位、移动和新加。我这里更新得比较频繁，只用三角是提示本版改动和新加入的项目。

图标的位置在环内分布可能是随机的，保证两个图标不会落在一起。环内的点互相平等，注意不要用距离圆心的远近来区分深浅，那没有意义。

## 文档维护

ThoughtWorks 在这里讲得很清楚，用 Google Sheet 维护文档，发布后将编辑页面的地址复制粘贴到 radar.thoughtworks.com 就可以了。

文档中很多内容都可以改，我改了环的名称、象限的名称，但都保持了四个。项目的说明虽然只能在一个单元格里，但可以用 HTML 语言，也就是说可以有超链接，可以加粗，可以分段。

我在本地电脑维护一个电子表格，写好了更新到 Google Sheet 里。本地每次更新时我复制一个工作表，命名为当下日期；在 Google Sheet 里新建一个工作表，粘贴入写好的内容。这样在生成的雷达图中也能选不同版本的数据来生成图象。

Thoughtworks 网站生成的雷达图是动态的，可以放大每个象限，可以展开项目说明。它能够通过固定的网址直接进入，也就可以链接到自己的博客里。由于某种原因，我在 Google Chrome 浏览器里贴入地址。每次刷新页面，它都会从 Google Sheet 文档中更新数据。我没试过能不能将 ThoughtWorks 开源的 js 代码部署到自己的网站上。

为了给别人看，我的工作流程是这样：在本地 markdown 文档中写内容，转成 HTML 文件，通过 Chrome 浏览器右键的 Inspect 功能查看段落的 HTML 格式写法，逐一复制到本地电子表格中、更新 Google Sheet 表格，在 radar.thoughtworks.com 生成雷达图，截屏更新本地 md 文件，发布到网站。

---

以上，希望对你也有提醒。2020-07-29 记。






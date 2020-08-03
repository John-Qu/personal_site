---
title: Attraction Radar
subtitle: 
author: John Qu
date: 2020-07-25
slug: attraction-radar
tags:
- 
categories:
- 
typora-root-url: ../../static
show_toc: no
---

Here is my Attraction Radar, powered by radar.thoughtworks.com. The URL of my [Google Sheet](https://www.thoughtworks.com/radar/how-to-byor) file is:

https://docs.google.com/spreadsheets/d/1_lHFMIZTJnjO0ZftooSPZ5ni3rrOhnNPz_2mwQeOzMU/edit#gid=0

![Screen Shot 2020-07-29 at 21.07.42](/images/2020-07-24-Build-my-own-Radar-on-Attraction/Screen%20Shot%202020-07-29%20at%2021.07.42.png)

The four quarters are：
![Screen Shot 2020-07-29 at 21.08.04](/images/2020-07-24-Build-my-own-Radar-on-Attraction/Screen%20Shot%202020-07-29%20at%2021.08.04.png)
![Screen Shot 2020-07-29 at 21.08.32](/images/2020-07-24-Build-my-own-Radar-on-Attraction/Screen%20Shot%202020-07-29%20at%2021.08.32.png)
![Screen Shot 2020-07-29 at 21.08.46](/images/2020-07-24-Build-my-own-Radar-on-Attraction/Screen%20Shot%202020-07-29%20at%2021.08.46.png)
![Screen Shot 2020-07-29 at 21.09.02](/images/2020-07-24-Build-my-own-Radar-on-Attraction/Screen%20Shot%202020-07-29%20at%2021.09.02.png)

Item expanded:
![Screen Shot 2020-07-29 at 21.24.24](/images/2020-07-24-Build-my-own-Radar-on-Attraction/Screen%20Shot%202020-07-29%20at%2021.24.24.png)

## Profession

### Occupy

#### The function of Jaw System

I had seen the working process of jaws on Tetra Pak's [TBA 19](http://tma1992.com/en/product/filling-line-for-fruit-puree-and-juices-tetra-pak-tba-19/) and [TBA 22](https://www.equipmatching.com/used_equipment/12/146/300335.php) filling machines when I was in the [dairy equipment](https://meticulousblog.org/top-10-companies-in-dairy-processing-equipment-market/) business. I see its general purpose, but I don't know the detailed functional time sequence in two collaborating circles of left-hand and right-hand jaws. I am studying the servo motor function in the drive unit of Tetra Pak's [A3/Flex](https://www.tetrapak.com/packaging/tetra-pak-a3-compactflex) filling machine. So I must clarify what task is performing in each stage as accurate as in machine degree. I noticed an acceleration chart on [a report slide](https://www.mscsoftware.com/sites/default/files/metodi-strumenti-calcolo-prototipaz.pdf) from Tetra Pak. It tells me some information about what it does by comparing it with video from youtube. It shows what is the relation of the left-hand jaw and right-hand jaw by [comparing](https://camo.githubusercontent.com/dcf37a147ddd9b73fcbd55e10478a3462b632a68/68747470733a2f2f747661312e73696e61696d672e636e2f6c617267652f303036744e6252776c793167396a686d74793472686a3331316930753037776a2e6a7067) it with itself of moving 180 degrees aside. I have measured that chart with LibreCAD and regenerated the [curve](https://camo.githubusercontent.com/69498dcaf1f297bafe57542fae8a6ae77a2af6a3/68747470733a2f2f747661312e73696e61696d672e636e2f6c617267652f303036744e6252776c793167396a693176673938646a333163313075306231362e6a7067) with SymPy. But I don't think I have understood enough about the functions until my cam profile runs on a real [A3/Flex](https://www.tetrapak.com/packaging/tetra-pak-a3-compactflex) filing machine smoothly. I will try to find and catch opportunities in industry [here](http://www.leiwest.com/productsshow.asp?id=248) and [there](http://gspak.com.cn/ProductInfo_13_4.aspx).

#### SymPy for Kinematics

I deduced equations in the kinematics of mechanism in Tetra Pak's [A3/Flex](https://www.tetrapak.com/packaging/tetra-pak-a3-compactflex) filling machine with SymPy. I didn't dive into SymPy, only using it as a calculator with a script. I wonder whether there is a similar [symbolic calculation in Julia](http://mth229.github.io/symbolic.html), and it seems the [answer](https://discourse.julialang.org/t/sympy-jl-vs-symengine-jl-vs-reduce-jl-vs/10381) is 'yes.' I will try some switching work when I finished the first round of refactoring.

### Engage

#### Vector Method in Kinematics

I have an analysis problem of rocker-slider four-bar mechanism in the Tetra Pak [A3/Flex](https://www.tetrapak.com/packaging/tetra-pak-a3-compactflex) filling machine. I need to know the end position, velocity, and acceleration according to the driving slider and vice verse. In the hacking process of [TetraCamThon](https://github.com/John-Qu/tetracamthon), I read chapters in the [Theory of Machines and Mechanisms (5th)](https://www.amazon.com/Theory-Machines-Mechanisms-John-Uicker/dp/0190658908). At that time, I took notes on white paper and made notations on it. I would like to write documentation for this project, so I need to make professional drawings and notations.

#### TDD with CAE application

Adding tests is a must-have step in refactoring. The code in [TetraCamThon](https://github.com/John-Qu/tetracamthon) is numerical computing, not UI, package, or App. On how to write unit tests for this kind of system, I need some examples. On the reading radar of thoughtworkers, books about testing are: 

- [单元测试之道Java版](https://book.douban.com/subject/1239651/) (pdf of en, and cn at library)
- [Google软件测试之道](https://book.douban.com/subject/25742200/) (cn bought), 
- [编写可读代码的艺术 ](https://book.douban.com/subject/10797189/)(cn at library), 
- [测试驱动开发](https://book.douban.com/subject/25735501/) (cn at library). 

I have read the first half of *[Test-driven development with Python](https://book.douban.com/subject/26640135/)* on [iTuring.com](https://www.ituring.com.cn/book/2052) and Harry Percival's [*Obey the Testing Goat* website](https://www.obeythetestinggoat.com/).

#### Grammar for Documentation

Writing in a simple sentence with simple words is good. However, too simple is not. [Grammarly.app](https://app.grammarly.com/) can tell me what is no good, but I have to write out my own ideas. I have scanned [The Elements of Style](https://en.wikipedia.org/wiki/The_Elements_of_Style), [English Grammar In Use](https://www.cambridge.org/us/cambridgeenglish/catalog/grammar-vocabulary-and-pronunciation/english-grammar-use-5th-edition). I am learning [Collins COBUILD English Grammar](https://www.amazon.com/Collins-COBUILD-English-Grammar-UK/dp/0008135819). I had better read Steven Pinker's [The Sense of Style](https://en.wikipedia.org/wiki/The_Sense_of_Style) first.

### Concern

#### Refactor of [TetraCamThon](https://github.com/John-Qu/tetracamthon)

Last year in the [TetraCamThon](https://github.com/John-Qu/tetracamthon) project, I have hacked the motion math functions of the Tetra Pak [A3/Flex](https://www.tetrapak.com/packaging/tetra-pak-a3-compactflex) filling machine's driving servo motor. Only I know the order of running sequence to get the proper result curve. Although [TetraCamThon](https://github.com/John-Qu/tetracamthon) is released from initial, it fails in meeting the release guidelines such as that in Zalando's "[How we release open source projects](https://opensource.zalando.com/blog/2019/05/How-We-Release-Code/)." I don't know whether someone else might be interested in this project. I noticed yesterday that there is [one star in this project](https://github.com/John-Qu/tetracamthon/stargazers), which comes from [luzpaz](https://github.com/luzpaz), a [veteran](https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=12229) on the FreeCAD forum. I thrived on doing it right, and now I am trying to do it well, to make it alive and longlived. So I need to arrange the hashing code, with professional know-how from [Martin Fowler](https://martinfowler.com/)'s book *[Refactor](https://refactoring.com/)*. I borrowed the [second edition's Chinese version](https://book.douban.com/subject/30468597/) from the library, then bought one on kongfz.com. It is translated by [Jeff Xiong](https://www.thoughtworks.com/cn/profiles/xiong-jie), a former thoughtworker who had [blogged](http://gigix.thoughtworkers.org/) twelve years weekly. The English version is available on [InformIT.com](https://martinfowler.com/articles/access-refactoring-web-edition.html).

#### Javascript Tutorial

I didn't learn Javascript when I studied in the course on [full-stack technology with Ruby on Rails in Spring 2017](https://xiaochu.ga/Content/fullstack.xinshengdaxue.com.html). I knew it is widely used in web applications, but I don't need that. Now I am eager to read [Martin Fowler](https://martinfowler.com/)'s book *[Refactor](https://refactoring.com/)*, which takes Javascript code as examples. I need to know the basics in Javascript, but not need to dig into the [subtleties in it](https://www.amazon.com/JavaScript-Good-Parts-Douglas-Crockford/dp/0596517742), as it has so many platforms, such as jQuery, Node.js, and Vue.js. I found that Prof. [Daniel Jackson at MIT](http://people.csail.mit.edu/dnj/) gave short [introduction pages on JavaScript](http://people.csail.mit.edu/dnj/teaching/6170/javascript-live/), which is [up to date](http://people.csail.mit.edu/dnj/teaching/6170/javascript-16/), and W3C has interactive [tutorials on JavaScript](https://www.w3schools.com/js/default.asp).

#### Economics in OSS

I am doing engineering work on mechanical analysis and software tools. The result is mine, but the effect is ours if it can trigger more work of others. I acknowledged [ESR](http://www.catb.org/~esr/who-is-ESR.html)'s [The Cathedral & the Bazaar](http://www.catb.org/~esr/writings/cathedral-bazaar/). I used it to argue with Brad on releasing the [FFI in Chinese](https://bookdown.org/johnqu1982/FFI/) for public reading. I am running at making [TetraCamThon](https://github.com/John-Qu/tetracamthon) truly usable on Github, so I need to consider the reactions among users. I would read the [open-source guide](https://opensource.guide/) created by Github, and participate in Xia Qingfeng's *[Module developer's guide to FreeCAD source code](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide)*, Realthunder's [FreeCAD Assembly3](https://github.com/realthunder/FreeCAD_assembly3), and one [add-on of FreeCAD](https://github.com/FreeCAD/FreeCAD-addons).

#### ThoughtWorks Insight

I like the tone in the insight blogs of [thoughtworkers](https://www.thoughtworks.com/insights). They have real projects from customers, and they have the mechanism and ability to write lessons from experience. The [ThoughtWorkers' Insight](https://insights.thoughtworks.cn/) has catalogs and tags, so I could search by topic or author. I wish I could grow to look similar to them, such as the [Insights of Jeff Xiong](https://insights.thoughtworks.cn/author/xiongjie/)

### Hold

#### Abstraction and Specification for [TetraCamThon](https://github.com/John-Qu/tetracamthon)

I read [Prof. Guttag](http://people.csail.mit.edu/guttag/)'s [Introduction to Computation and Programming Using Python](https://www.amazon.com/Introduction-Computation-Programming-Using-Python/dp/0262529629) in 2008. I am rereading it recently in preparing to rewrite the code in [TetraCamThon](https://github.com/John-Qu/tetracamthon). I noticed that Mr. Guttag has coauthored another book called [Program Development in Java - Abstraction, Specification, and Object-Oriented Design](https://www.amazon.com/Program-Development-Java-Specification-Object-Oriented/dp/0201657686). This book is classic, and [said](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-170-laboratory-in-software-engineering-fall-2005/readings/) to be "parallels the course material closely; it's a good book for background reading." in the [MIT-OCW course "Laboratory in Software Engineering" in 2005](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-170-laboratory-in-software-engineering-fall-2005/). I want to learn the best practices in software engineer, and I could learn Java along with the reading of this book. I borrowed [one book on Java](https://library.sh.cn/#/index/pBookDetails?bid=5422467&type=zbook) from the library and downloaded several books. However, no one asks for my specification now, and the data abstraction seems not so complicated in b-splines. In short, I need not care too much about the topic of specification, requirements, and abstraction, which are common in software engineering. Best practices achieve more effects in practice. I'd better leave it until I joined a team and learn from neighbor engineers. By the way, Prof. Guttag didn't mention this book in his [new course](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/readings/), neither in thoughtworkers in their three versions ([2013](http://agiledon.github.io/blog/2013/04/17/thoughtworks-developer-reading-radar/)、[2016](https://insights.thoughtworks.cn/reading-radar-2016/)、[2019](https://insights.thoughtworks.cn/reading-radar-2019/)) of [Reading Radar](https://insights.thoughtworks.cn/reading-radar-2019/).



#### Julia for [TetraCamThon](https://github.com/John-Qu/tetracamthon)

When I search "[Numerical Methods in Engineering with Python 3](https://www.cambridge.org/core/books/numerical-methods-in-engineering-with-python-3/95151C37C2F427F30DC90FA619FE79F9)" within site of ocw.mit.edu, I found that MIT is teaching a [Introduction to Numerical Methods](https://ocw.mit.edu/courses/mathematics/18-335j-introduction-to-numerical-methods-spring-2019/) course with a new language called [Julia](http://julialang.org/). It is [faster than Python](https://ocw.mit.edu/courses/mathematics/18-335j-introduction-to-numerical-methods-spring-2019/week-1/Julia-intro.pdf) on a large scale of data. My code runs about 20 minutes in some functions. I need to take one eye on it and see if there is a chance to switch to Julia, to change [TetraCamThon](https://github.com/John-Qu/tetracamthon) to TetraCamLia.

#### Onshape Features

 is the [first CAD tool initially in SAAS](https://en.wikipedia.org/wiki/Onshape). I would like to work with them, but they [don't have a business in China](https://careers.ptc.com/TGnewUI/Search/home/HomeWithPreLoad?partnerid=2&siteid=5213&PageType=searchResults&SearchType=linkquery&LinkID=4393247#keyWordSearch=&locationSearch=) mainland. When they come, I wish I have been prepared. I will take a tour on the onshape [forum](https://forum.onshape.com/#_ga=2.131834828.218102043.1595989237-1957610019.1593917704) and [blogs](https://www.onshape.com/cad-blog) weekly and see if my classmate could help me join their [Education Standard Plan](https://www.onshape.com/education-plan). 

- [Why We Started From Scratch (Again) In The CAD Business](https://www.onshape.com/cad-blog/why-we-started-from-scratch-again-in-the-cad-business)
- [PTC Snatches Up Cloud CAD Pioneer Onshape](https://www.digitalengineering247.com/article/ptc-snatches-up-cloud-cad-pioneer-onshape)
- [Carl Bass’ Parting Shots: Don’t Just Introduce New Tech; Work on Unsolved Problems](https://www.digitalengineering247.com/article/carl-bass-parting-shots/feed)
- [On Time, On Budget, Onshape](https://digital.hbs.edu/platform-rctom/submission/on-time-on-budget-onshape/)
- [Best General-Purpose CAD Software](https://www.g2.com/categories/general-purpose-cad)

#### Teach Tech to Adults

Although I don't have anything to teach now, I am doing something interesting to show former me. The purpose of doing these [TetraCamThon](https://github.com/John-Qu/tetracamthon) project series is for teaching. Teaching technology is not an easy task that can do naturally. [Greg Wilson](http://third-bit.com/), a coach in Rstudio, wrote a series of articles on [Teaching Tech Together](https://teachtogether.tech/).

#### FreeCAD Development

I like the discussion in the [forum of FreeCAD](https://forum.freecadweb.org/), and I am in the [Github](https://github.com/FreeCAD) mail list of developers. I would like to build an add-on of cam profile design for FreeCAD later. So I need to keep up with the development of FreeCAD. I will surf through the forum weekly, and read through then translate Xia Qingfeng's *[Module developer's guide to FreeCAD source code](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide)*.

#### FreeCAD Usage

I start modeling with FreeCAD when I was translating [FreeCAD For Inventors](https://forum.freecadweb.org/viewtopic.php?t=30959). If I really commit that FreeCAD has a future in being a platform for open mechanisms, I had better put in enough effort to show its certainty. There were [no good enough tutorials](https://bookauthority.org/books/new-freecad-ebooks) and books on FreeCAD now. Still, there are some [videos](https://www.youtube.com/results?search_query=freeCAD) on youtube, developed by [developers](https://www.youtube.com/channel/UCRGXbDM8raKr6t-4xhJDKJw).

#### Computation on Data

I have reviewed  [Prof. Guttag](http://people.csail.mit.edu/guttag/)'s *[Introduction to Computation and Programming Using Python](https://www.amazon.com/Introduction-Computation-Programming-Using-Python/dp/0262529629)* the first half, until Chapter 12. In the second half, Prof. Guttag talked about computation on data applications. Now I have no subject on data, so I had better put this book down for a while. When I am facing mass data, I will come back. Alternatively, I would like to learn along with my wife.

## Concrete Life

### Occupy

#### Being a Photographer

I like taking photos, but my picture is not touching for the general audience. I read a brochure [On Being a Photographer](https://www.amazon.com/Being-Photographer-Practical-Guide/dp/1888803061) the last winter before taking pictures of my sister-in-law's wedding party. Now I don't have a long term subject, like those I had in the past, such as running people, wedding ceremonies, and playing children.

#### Convict Conditioning

I couldn't left my arm to wash my face for two month in the summer of 2014 after I blowed myself on a bridge after running one night and blowed under an air conditioner the next morning. I have begun to practice convict conditioning since then. Now I can do 

- 2 sets of 15 close pushups, 
- 2 sets of 10 (both sides) one-leg squats, 
- 2 sets of 5 (both sides) close pullups, 
- 2 sets of 10 hanging straight leg raises, 
- 2 sets of 8 full bridges, and 
- 1 set of 5 half handstand pushups. 

I have the book [Convict Conditioning](https://www.amazon.com/Convict-Conditioning-Weakness-Using-Survival-Strength/dp/0938045768), and I had better progress step by step.

### Engage

#### Road Run in Summer

I recently have the proper training conditions, and I want to make this process a "strong track record of success." I use a training diagram that I prepared for the 2018 Shanghai marathon, but I found it hard to complete because of the hot weather. I need to figure out a new diagram which is suitable for summer. I am going to read through [Pete Pfitzinger's book *Faster road racing*](http://www.librarything.com/work/15248645/reviews/119802147).

### Concern

#### Sense in Numbers

Dr. Wu Jun gives [a Math course on Gotit.app](https://mp.weixin.qq.com/s/nQNB3iVxcRZvri0IY6PuIw), similar to Oxford's Very Short Introductions series. My elder child is approaching his six, and he is studying math apps on the iPad. I wish I could talk with him about the joy and concept in numbers, not just answering his questions. I would do DuckDuckMoose with him and read [Young Math Books](https://www.goodreads.com/series/164944-crowell-young-math-books) beforehand.

## Meanings

### Occupy

#### Migration in Breath

I found it hard to surf in waves of the mind, even that I cannot work and study continuously and effectively in the last winter. So I made a decision that I must learn to be able to live with that wave. I borrowed Swami Lama's *[Meditation and Its Practice](https://www.amazon.com/Meditation-Its-Practice-Swami-Rama/dp/0893891533)* from the library, and practice according to its guidance while residual in Wuhan in this spring 2020. 

### Concern

#### Live my Life out

I have listened to [Wu Zhihong's psychology course on Gotit.app](https://mp.weixin.qq.com/s/8v7MSUUZ2yKYnuQX40VyiQ) for two or three rounds. Maybe psychoanalysis is not a scientific approach, but it touched my soul and triggered my change. I am living out my own life with the power of action, like when I am a little drunk. Whenever I read paragraphs in [his book](https://book.douban.com/subject/30408662/), I can find some strength.

### Hold

#### The Analects of Confucius

Last year I took the course [Brand marketing of Mr. Hua Shan](https://mp.weixin.qq.com/s/wL6SNTcjxJQWmbKTse5WIQ) on Gotit.app. I enjoyed it in reading his book *[Hua Shan Explains The Analects of Confucius Completely](https://book.douban.com/subject/26913479/)* that I borrowed from the library. It tells some reasonings in everyday life in the Chinese culture, which I found to be my basis of feelings when contact with people. I had started to read Prof. Qian Mu's [New Explanation of The Analects of Confucius](https://book.douban.com/subject/6775830/) in 2017. But abandoned it with a new task because it is a luxury to read this kind of book as an adult without a job. Now, I have other issues to deal with, so I will hold on to these wishes until I found a job earning money.

## Methodology

### Occupy

#### Attraction Radar

This is what I adopted after engagement with [ThoughtWorks's Technology Radar](https://www.thoughtworks.com/radar). I think it might become a [proper tool](../cn/2020/07/mechanics-on-attraction-radar/) for me to manage my attention. As I will respect my attraction radar, I have read through their Technology Radar and keep an eye on it in the future.

### Engage

#### Personal OKRs

OKRs are practical tools for active workers besides KPIs in an organization full of intelligence. I am not in a particular firm, but I want to place myself in the community of open-source CAD software. I need to navigate my story finding the HOW and WHAT from WHY, and need to separate it into objectives and define the SMART vital results. I have seen [John Doerr's TED talk on OKRs](https://www.ted.com/talks/john_doerr_why_the_secret_to_success_is_setting_the_right_goals/transcript) in [Mr. Yu's article about OKRs](https://mp.weixin.qq.com/s/rnYHBCZy6HeEH-QVS3MWqg), and I am reading his book: [*Measure What Matters - How Google, Bono, and the Gates Foundation Rock the World with OKRs*](https://book.douban.com/subject/30396635/).

### Concern

#### Structures in Mathematics

If I want to learn the logical part, I need to spend most of my time deducing and solving problems. I have spent half of my study time reading mathematics. I recently heard from Dr. Wu Jun that there are clues in math that act as the bridge between its nature and usages, which doesn't need so much time to learn so much concrete points of knowledge. I had better understand Dr. Wu's [course](https://mp.weixin.qq.com/s/nQNB3iVxcRZvri0IY6PuIw) throughout.

#### Science in Learning

I am entering a new era of engineering software. I need to learn a lot of topics efficiently and effectively. Wan Weigang had gathered his articles about learning science into a book called [*What is Learning in the End*](https://book.douban.com/subject/35082292/). He has posted a series of articles reporting his new earnings in reading [How We Learn: Why Brains Learn Better Than Any Machine... for now](https://book.douban.com/subject/35013354/). I found some advice valuable about being a pragmatic programmer in the reading radar of thoughtworkers. 

### Hold

#### Reading Tech Documents

In [Dr. Wu Jun's course, Reading and Writing](https://mp.weixin.qq.com/s/JkfgFfZnKlvWyg3oSxzzdA), he proposed reading steps when entering a professional field: 1) Orthodox literature, 2) authoritative reviews and 3) academic monographs. I had better read and learn with such frameworks, rather than by instinct. There are several books recommended in the reading radars of ThoughtWorkers:

- [*Are Your Lights On?*](https://book.douban.com/subject/1350343/) cn borrowed from library and epub of en
- [Pragmatic Thinking and Learning: Refactor Your Wetware](https://book.douban.com/subject/26268555/), cn bought from kongfz, and pdf of en
- [The Clean Coder：A Code of Conduct for Professional Programmers](https://book.douban.com/subject/11614538/), cn borrowed from library, and pdf of en
- [软件开发践行录](https://book.douban.com/subject/25952573/), cn borrowed from library
- *[The Art of Readable Code](https://book.douban.com/subject/10797189/)*, cn borrowed from library and pdf of en

#### Open Source Releasing

I release [TetraCamThon](https://github.com/John-Qu/tetracamthon) with a ReadMe, but I don't know what to include in it. I just looked at what other repositories do. Still, there should have been some code of conduct in releasing an open-source project for public users and contributors, such as Zalando's "[How we release open source projects](https://opensource.zalando.com/blog/2019/05/How-We-Release-Code/)."

#### HTML Slide

I like the slides in HTML, such as [Xie Yihui's xaringan introduction](http://slides.yihui.org/xaringan/zh-CN.html) and Prof. [Daniel Jackson](http://people.csail.mit.edu/dnj/)'s [JavaScript Overview](http://people.csail.mit.edu/dnj/teaching/6170/javascript-live/modules/basics/slides.html#/). Xie said it is easy to construct this kind of [slides from Rmarkdown](https://bookdown.org/yihui/rmarkdown/xaringan.html). If I can figure out how to do it in half an hour, I would like to adopt it. Maybe I will try it when I make presentation the next time.


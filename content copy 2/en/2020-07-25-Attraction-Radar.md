---
title: Attraction Radar
subtitle: 
author: John Qu
date: 2020-08-05
slug: attraction-radar
tags:
- 
categories:
- 
typora-root-url: ../../static
show_toc: yes
---

Here is my Attraction Radar, powered by [radar.thoughtworks.com](https://www.thoughtworks.com/radar/how-to-byor), which use my [Google Sheet file](https://docs.google.com/spreadsheets/d/1_lHFMIZTJnjO0ZftooSPZ5ni3rrOhnNPz_2mwQeOzMU/edit#gid=0).

![Screen Shot 2020-08-07 at 21.05.24](/images/2020-07-25-Attraction-Radar/Screen%20Shot%202020-08-07%20at%2021.05.24.png)

The four quarters are：

![Screen Shot 2020-08-07 at 21.06.37](/images/2020-07-25-Attraction-Radar/Screen%20Shot%202020-08-07%20at%2021.06.37.png)
![Screen Shot 2020-08-07 at 21.06.22](/images/2020-07-25-Attraction-Radar/Screen%20Shot%202020-08-07%20at%2021.06.22.png)
![Screen Shot 2020-08-07 at 21.06.53](/images/2020-07-25-Attraction-Radar/Screen%20Shot%202020-08-07%20at%2021.06.53.png)
![Screen Shot 2020-08-07 at 21.07.07](/images/2020-07-25-Attraction-Radar/Screen%20Shot%202020-08-07%20at%2021.07.07.png)

Item expanded:
![Screen Shot 2020-08-07 at 21.07.52](/images/2020-07-25-Attraction-Radar/Screen%20Shot%202020-08-07%20at%2021.07.52.png)

# Profession

## Occupy

### The function of Jaw System

I had seen the working process of jaws on Tetra Pak's [TBA 19](http://tma1992.com/en/product/filling-line-for-fruit-puree-and-juices-tetra-pak-tba-19/) and [TBA 22](https://www.equipmatching.com/used_equipment/12/146/300335.php) filling machines when I was in the [dairy equipment](https://meticulousblog.org/top-10-companies-in-dairy-processing-equipment-market/) business. I see its general purpose, but I don't know the detailed functional time sequence in two collaborating circles of left-hand and right-hand jaws. I am studying the servo motor function in the drive unit of Tetra Pak's [A3/Flex](https://www.tetrapak.com/packaging/tetra-pak-a3-compactflex) filling machine. So I must clarify what task is performing in each stage as accurate as in machine degree. I noticed an acceleration chart on [a report slide](https://www.mscsoftware.com/sites/default/files/metodi-strumenti-calcolo-prototipaz.pdf) from Tetra Pak. It tells me some information about what it does by comparing it with video from youtube. It shows what is the relation of the left-hand jaw and right-hand jaw by [comparing](https://camo.githubusercontent.com/dcf37a147ddd9b73fcbd55e10478a3462b632a68/68747470733a2f2f747661312e73696e61696d672e636e2f6c617267652f303036744e6252776c793167396a686d74793472686a3331316930753037776a2e6a7067) it with itself of moving 180 degrees aside. I have measured that chart with LibreCAD and regenerated the [curve](https://camo.githubusercontent.com/69498dcaf1f297bafe57542fae8a6ae77a2af6a3/68747470733a2f2f747661312e73696e61696d672e636e2f6c617267652f303036744e6252776c793167396a693176673938646a333163313075306231362e6a7067) with SymPy. But I don't think I have understood enough about the functions until my cam profile runs on a real [A3/Flex](https://www.tetrapak.com/packaging/tetra-pak-a3-compactflex) filing machine smoothly. I will try to find and catch opportunities in industry [here](http://www.leiwest.com/productsshow.asp?id=248) and [there](http://gspak.com.cn/ProductInfo_13_4.aspx).

### SymPy for Kinematics

I deduced equations in the kinematics of mechanism in Tetra Pak's [A3/Flex](https://www.tetrapak.com/packaging/tetra-pak-a3-compactflex) filling machine with SymPy. I didn't dive into SymPy, only using it as a calculator with a script. I wonder whether there is a similar [symbolic calculation in Julia](http://mth229.github.io/symbolic.html), and it seems the [answer](https://discourse.julialang.org/t/sympy-jl-vs-symengine-jl-vs-reduce-jl-vs/10381) is 'yes.' I will try some switching work when I finished the first round of refactoring.

### Vector Method in Kinematics

I have an analysis problem of rocker-slider four-bar mechanism in the Tetra Pak [A3/Flex](https://www.tetrapak.com/packaging/tetra-pak-a3-compactflex) filling machine. I need to know the end position, velocity, and acceleration according to the driving slider and vice verse. In the hacking process of [TetraCamThon](https://github.com/John-Qu/tetracamthon), I read chapters in the [Theory of Machines and Mechanisms (5th)](https://www.amazon.com/Theory-Machines-Mechanisms-John-Uicker/dp/0190658908). At that time, I took notes on white paper and made notations on it. I would like to write documentation for this project, so I need to make professional drawings and notations.

## Engage

### Restructuring of TetraCamThon

Last year in the [TetraCamThon](https://github.com/John-Qu/tetracamthon) project, I have hacked the motion math functions of the Tetra Pak [A3/Flex](https://www.tetrapak.com/packaging/tetra-pak-a3-compactflex) filling machine's driving servo motor. I thrived on doing it right, and now I am trying to do it well.  [^someone is interested] I would like to make it 
1) alive and long-lived by obeying the [open-source guides](https://opensource.guide/) provided by Github, 
2) revealing my working knowledge about TDD, CI and Refactor by learning the best practices from those veterans' books, and 
3) showing off the professionalism that I devote.

[^someone is interested]: I don't know whether someone else might be interested in this project. I noticed there is [one star in this project](https://github.com/John-Qu/tetracamthon/stargazers), which comes from [luzpaz](https://github.com/luzpaz), a [veteran](https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=12229) on the FreeCAD forum.  

### Refactor

To restructure [TetraCamThon](https://github.com/John-Qu/tetracamthon) well, I will read these books on refactoring: 
1) [Martin Fowler](https://martinfowler.com/)'s *[Refactor](https://refactoring.com/)* is the definite book for this topic during the last twenty years. It is a mainly a reference book of listing the method of refactor. I bought [重构（第2版）改善既有代码的设计](https://book.douban.com/subject/30468597/) on kongfz.com, and used to borrow one from library. It is translated by [Jeff Xiong](https://www.thoughtworks.com/cn/profiles/xiong-jie), a former thoughtworker who had [blogged](http://gigix.thoughtworkers.org/) twelve years weekly. The canonical form of this book is its [web site](https://refactoring.com/) or [web edition](https://memberservices.informit.com/my_account/webedition/9780135425664/html/index.html?partner=53).
2) Michael Feathers' *Working Effectively with Legacy Code* (2005, Prentice Hall Professional Technical Reference) is a tutorial for beginners who need some step by step practices. The [chm](https://libgen.lc/ads.php?md5=CF14D97557880E9A1471704F9D59381E) and [pdf](https://libgen.lc/ads.php?md5=6407452C31E2901713E1DC414493A3BA) files was downloaded from libgen.lc. [修改代码的艺术](https://book.douban.com/subject/2248759/) was borrowed from [library](http://ipac.library.sh.cn/ipac20/ipac.jsp?aspect=basic_search&profile=sl&index=ISBN&term=9787115163622). 
3) William C. Wake's *Refactoring Workbook* (2003, Addison-Wesley Professional) contains many exercises to practice refactoring. It will take readers through the learning process.The chm file could be downloaded from [libgen.lc](https://libgen.lc/ads.php?md5=7BD8DDEAA18DACB1EBD0C28C31D4082C). [重构手册](https://book.douban.com/subject/1173730/) could be borrowed from [library](http://ipac.library.sh.cn/ipac20/ipac.jsp?aspect=basic_search&profile=sl&index=ISBN&term=7508322789).

### Self-testing code

To restructure [TetraCamThon](https://github.com/John-Qu/tetracamthon) well, I will read these books on self-testing code: 
1) Kent Beck's *Test Driven Development_ By Example* (2002, Addison-Wesley Professional) is the inventor's reflection on this topic which shows the implementation of xUnit in Python in its second section. The [chm](https://libgen.lc/ads.php?md5=1C0D9E39A4EFE28138A88A5A1BD54D5D), [pdf](https://libgen.lc/ads.php?md5=E1945A61FD668C6338EBCEA346B94525), and [epub](https://libgen.lc/ads.php?md5=D3E1D1A764429BFAADB9B28B453228F1) files could be downloaded from libgen.lc. [测试驱动开发——实践与模式解析](https://book.douban.com/subject/25735501/) was borrowed from [library](http://ipac.library.sh.cn/ipac20/ipac.jsp?session=15967844F33VH.113116&profile=sl&uri=full=3100001@!4226917@!9&ri=1&aspect=basic_search&menu=search&source=172.16.103.188@!shcl&ipp=20&staffonly=&term=%E6%B5%8B%E8%AF%95%E9%A9%B1%E5%8A%A8%E5%BC%80%E5%8F%91&index=.TW&uindex=&aspect=basic_search&menu=search&ri=1). 
2) Jeff Langr, Andy Hunt, Dave Thomas' *Pragmatic Unit Testing in Java 8 with JUnit* (2015, The Pragmatic Programmers) is 200 pages long, and is in the series of pragmatic starter kits. The [pdf](https://libgen.lc/ads.php?md5=1DA4410CEB9972264923E60815D69D25) file could be download from libgen.lc. [单元测试之道 Java 版：使用 JUnit](https://book.douban.com/subject/1239651/) was borrowed from [library](http://ipac.library.sh.cn/ipac20/ipac.jsp?aspect=basic_search&profile=sl&index=ISBN&term=7121006650). 
3) James A. Whittaker, Jason Arbon, Jeff Carollo's *How Google Tests Software* (2012, Addison Wesley) tells how a relatively few testing engineers helps many develop engineers write their own testing code. The [pdf](https://libgen.lc/ads.php?md5=6E5D1F1A5592F52FDC7232F917D5419D) and [epub](https://libgen.lc/ads.php?md5=7D783D5669C0D1557E0B82F70B9BB099) files could be downloaded from libgen.lc. I bought [Google软件测试之道](https://book.douban.com/subject/25742200/) from [duozhuayu.com](https://www.duozhuayu.com/books/59319476440533181?utm_source=douban&utm_medium=web&utm_content=in_stock), and it could be borrowed from [library](http://ipac.library.sh.cn/ipac20/ipac.jsp?session=1E967P360D012.113016&profile=sl&uri=link=3100006@!4181824@!3100001@!3100002&aspect=basic_search&menu=search&ri=5&source=172.16.103.188@!shcl&term=Google%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E4%B9%8B%E9%81%93&index=). 
4) David Sale's *Testing Python_ Applying Unit Testing, TDD, BDD and Acceptance Testing* (2014, Wiley). 
5) I have read the first half of *[Test-driven development with Python](https://book.douban.com/subject/26640135/)* on [iTuring.com](https://www.ituring.com.cn/book/2052) and Harry Percival's [*Obey the Testing Goat: Using Django, Selenium, and JavaScript* website](https://www.obeythetestinggoat.com/).

### Grammar for Documentation

Writing in a simple sentence with simple words is good. However, too simple is not. [Grammarly.app](https://app.grammarly.com/) can tell me what is no good, but I have to write out my own ideas. I have scanned [The Elements of Style](https://en.wikipedia.org/wiki/The_Elements_of_Style), [English Grammar In Use](https://www.cambridge.org/us/cambridgeenglish/catalog/grammar-vocabulary-and-pronunciation/english-grammar-use-5th-edition). I am learning [Collins COBUILD English Grammar](https://www.amazon.com/Collins-COBUILD-English-Grammar-UK/dp/0008135819). I had better read Steven Pinker's [The Sense of Style](https://en.wikipedia.org/wiki/The_Sense_of_Style) first.

## Concern

### Javascript Tutorial

I didn't learn Javascript when I studied in the course on [full-stack technology with Ruby on Rails in Spring 2017](https://xiaochu.ga/Content/fullstack.xinshengdaxue.com.html). I knew it is widely used in web applications, but I don't need that. Now I am eager to read [Martin Fowler](https://martinfowler.com/)'s book *[Refactor](https://refactoring.com/)*, which takes Javascript code as examples. I need to know the basics in Javascript, but not need to dig into the [subtleties in it](https://www.amazon.com/JavaScript-Good-Parts-Douglas-Crockford/dp/0596517742), as it has so many platforms, such as jQuery, Node.js, and Vue.js. I found that Prof. [Daniel Jackson at MIT](http://people.csail.mit.edu/dnj/) gave short [introduction pages on JavaScript](http://people.csail.mit.edu/dnj/teaching/6170/javascript-live/), which is [up to date](http://people.csail.mit.edu/dnj/teaching/6170/javascript-16/), and W3C has interactive [tutorials on JavaScript](https://www.w3schools.com/js/default.asp).

### Economics in OSS

I am doing engineering work on mechanical analysis and software tools. The result is mine, but the effect is ours if it can trigger more work of others. I acknowledged [ESR](http://www.catb.org/~esr/who-is-ESR.html)'s [The Cathedral & the Bazaar](http://www.catb.org/~esr/writings/cathedral-bazaar/). I used it to argue with Brad on releasing the [FFI in Chinese](https://bookdown.org/johnqu1982/FFI/) for public reading. I am running at making [TetraCamThon](https://github.com/John-Qu/tetracamthon) truly usable on Github, so I need to consider the reactions among users. I would read the [open-source guide](https://opensource.guide/) created by Github, and participate in Xia Qingfeng's *[Module developer's guide to FreeCAD source code](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide)*, Realthunder's [FreeCAD Assembly3](https://github.com/realthunder/FreeCAD_assembly3), and one [add-on of FreeCAD](https://github.com/FreeCAD/FreeCAD-addons).

### ThoughtWorks Insight

I like the tone in the insight blogs of [thoughtworkers](https://www.thoughtworks.com/insights). They have real projects from customers, and they have the mechanism and ability to write lessons from experience. The [ThoughtWorkers' Insight](https://insights.thoughtworks.cn/) has catalogs and tags, so I could search by topic or author. I wish I could grow to look similar to them, such as the [Insights of Jeff Xiong](https://insights.thoughtworks.cn/author/xiongjie/)

## Hold

### Abstraction and Specification for [TetraCamThon](https://github.com/John-Qu/tetracamthon)

I read [Prof. Guttag](http://people.csail.mit.edu/guttag/)'s [Introduction to Computation and Programming Using Python](https://www.amazon.com/Introduction-Computation-Programming-Using-Python/dp/0262529629) in 2008. I am rereading it recently in preparing to rewrite the code in [TetraCamThon](https://github.com/John-Qu/tetracamthon). I noticed that Mr. Guttag has coauthored another book called [Program Development in Java - Abstraction, Specification, and Object-Oriented Design](https://www.amazon.com/Program-Development-Java-Specification-Object-Oriented/dp/0201657686). This book is classic, and [said](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-170-laboratory-in-software-engineering-fall-2005/readings/) to be "parallels the course material closely; it's a good book for background reading." in the [MIT-OCW course "Laboratory in Software Engineering" in 2005](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-170-laboratory-in-software-engineering-fall-2005/). I want to learn the best practices in software engineer, and I could learn Java along with the reading of this book. I borrowed [one book on Java](https://library.sh.cn/#/index/pBookDetails?bid=5422467&type=zbook) from the library and downloaded several books. However, no one asks for my specification now, and the data abstraction seems not so complicated in b-splines. In short, I need not care too much about the topic of specification, requirements, and abstraction, which are common in software engineering. Best practices achieve more effects in practice. I'd better leave it until I joined a team and learn from neighbor engineers. By the way, Prof. Guttag didn't mention this book in his [new course](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/readings/), neither in thoughtworkers in their three versions ([2013](http://agiledon.github.io/blog/2013/04/17/thoughtworks-developer-reading-radar/)、[2016](https://insights.thoughtworks.cn/reading-radar-2016/)、[2019](https://insights.thoughtworks.cn/reading-radar-2019/)) of [Reading Radar](https://insights.thoughtworks.cn/reading-radar-2019/).

### Julia for [TetraCamThon](https://github.com/John-Qu/tetracamthon)

When I search "[Numerical Methods in Engineering with Python 3](https://www.cambridge.org/core/books/numerical-methods-in-engineering-with-python-3/95151C37C2F427F30DC90FA619FE79F9)" within site of ocw.mit.edu, I found that MIT is teaching a [Introduction to Numerical Methods](https://ocw.mit.edu/courses/mathematics/18-335j-introduction-to-numerical-methods-spring-2019/) course with a new language called [Julia](http://julialang.org/). It is [faster than Python](https://ocw.mit.edu/courses/mathematics/18-335j-introduction-to-numerical-methods-spring-2019/week-1/Julia-intro.pdf) on a large scale of data. My code runs about 20 minutes in some functions. I need to take one eye on it and see if there is a chance to switch to Julia, to change [TetraCamThon](https://github.com/John-Qu/tetracamthon) to TetraCamLia.

### Onshape Features

Onshape is the [first CAD tool initially in SAAS](https://en.wikipedia.org/wiki/Onshape). I would like to work with them, but they [don't have a business in China](https://careers.ptc.com/TGnewUI/Search/home/HomeWithPreLoad?partnerid=2&siteid=5213&PageType=searchResults&SearchType=linkquery&LinkID=4393247#keyWordSearch=&locationSearch=) mainland. When they come, I wish I have been prepared. I will take a tour on the onshape [forum](https://forum.onshape.com/#_ga=2.131834828.218102043.1595989237-1957610019.1593917704) and [blogs](https://www.onshape.com/cad-blog) weekly and see if my classmate could help me join their [Education Standard Plan](https://www.onshape.com/education-plan). Here are interesting articles: 
[Why We Started From Scratch (Again) In The CAD Business](https://www.onshape.com/cad-blog/why-we-started-from-scratch-again-in-the-cad-business). 
[PTC Snatches Up Cloud CAD Pioneer Onshape](https://www.digitalengineering247.com/article/ptc-snatches-up-cloud-cad-pioneer-onshape). 
[Carl Bass’ Parting Shots: Don’t Just Introduce New Tech; Work on Unsolved Problems](https://www.digitalengineering247.com/article/carl-bass-parting-shots/feed). 
[On Time, On Budget, Onshape](https://digital.hbs.edu/platform-rctom/submission/on-time-on-budget-onshape/). 
[Best General-Purpose CAD Software](https://www.g2.com/categories/general-purpose-cad).

### Teach Tech to Adults

Although I don't have anything to teach now, I am doing something interesting to show former me. The purpose of doing these [TetraCamThon](https://github.com/John-Qu/tetracamthon) project series is for teaching. Teaching technology is not an easy task that can do naturally. [Greg Wilson](http://third-bit.com/), a coach in Rstudio, wrote a series of articles on [Teaching Tech Together](https://teachtogether.tech/).

### FreeCAD Development

I like the discussion in the [forum of FreeCAD](https://forum.freecadweb.org/), and I am in the [Github](https://github.com/FreeCAD) mail list of developers. I would like to build an add-on of cam profile design for FreeCAD later. So I need to keep up with the development of FreeCAD. I will surf through the forum weekly, and read through then translate Xia Qingfeng's *[Module developer's guide to FreeCAD source code](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide)*.

### FreeCAD Usage

I start modeling with FreeCAD when I was translating [FreeCAD For Inventors](https://forum.freecadweb.org/viewtopic.php?t=30959). If I really commit that FreeCAD has a future in being a platform for open mechanisms, I had better put in enough effort to show its certainty. There were [no good enough tutorials](https://bookauthority.org/books/new-freecad-ebooks) and books on FreeCAD now. Still, there are some [videos](https://www.youtube.com/results?search_query=freeCAD) on youtube, developed by [developers](https://www.youtube.com/channel/UCRGXbDM8raKr6t-4xhJDKJw).

### Computation on Data

I have reviewed  [Prof. Guttag](http://people.csail.mit.edu/guttag/)'s *[Introduction to Computation and Programming Using Python](https://www.amazon.com/Introduction-Computation-Programming-Using-Python/dp/0262529629)* the first half, until Chapter 12. In the second half, Prof. Guttag talked about computation on data applications. Now I have no subject on data, so I had better put this book down for a while. When I am facing mass data, I will come back. Alternatively, I would like to learn along with my wife.

# Concrete Life

## Occupy

### Being a Photographer

I like taking photos, but my picture is not touching for the general audience. I read a brochure [On Being a Photographer](https://www.amazon.com/Being-Photographer-Practical-Guide/dp/1888803061) the last winter before taking pictures of my sister-in-law's wedding party. Now I don't have a long term subject, like those I had in the past, such as running people, wedding ceremonies, and playing children.

### Convict Conditioning

I couldn't left my arm to wash my face for two month in the summer of 2014 after I blowed myself on a bridge after running one night and blowed under an air conditioner the next morning. I have begun to practice convict conditioning since then. Now I can do 
2 sets of 15 close pushups, 
2 sets of 10 (both sides) one-leg squats, 
2 sets of 5 (both sides) close pullups, 
2 sets of 10 hanging straight leg raises, 
2 sets of 8 full bridges, and 
1 set of 5 half handstand pushups. 
I have the book [Convict Conditioning](https://www.amazon.com/Convict-Conditioning-Weakness-Using-Survival-Strength/dp/0938045768), and I had better progress step by step.

## Engage

### Road Run in Summer

I recently have the proper training conditions, and I want to make this process a "strong track record of success." I use a training diagram that I prepared for the 2018 Shanghai marathon, but I found it hard to complete because of the hot weather. I need to figure out a new diagram which is suitable for summer. I am going to read through [Pete Pfitzinger's book *Faster road racing*](http://www.librarything.com/work/15248645/reviews/119802147).

### Concern

### Sense in Numbers

Dr. Wu Jun gives [a Math course on Gotit.app](https://mp.weixin.qq.com/s/nQNB3iVxcRZvri0IY6PuIw), similar to Oxford's Very Short Introductions series. My elder child is approaching his six, and he is studying math apps on the iPad. I wish I could talk with him about the joy and concept in numbers, not just answering his questions. I would do DuckDuckMoose with him and read [Young Math Books](https://www.goodreads.com/series/164944-crowell-young-math-books) beforehand.

# Meanings

## Occupy

### Migration in Breath

I found it hard to surf in waves of the mind, even that I cannot work and study continuously and effectively in the last winter. So I made a decision that I must learn to be able to live with that wave. I borrowed Swami Lama's *[Meditation and Its Practice](https://www.amazon.com/Meditation-Its-Practice-Swami-Rama/dp/0893891533)* from the library, and practice according to its guidance while residual in Wuhan in this spring 2020. 

## Concern

### Live my Life out

I have listened to [Wu Zhihong's psychology course on Gotit.app](https://mp.weixin.qq.com/s/8v7MSUUZ2yKYnuQX40VyiQ) for two or three rounds. Maybe psychoanalysis is not a scientific approach, but it touched my soul and triggered my change. I am living out my own life with the power of action, like when I am a little drunk. Whenever I read paragraphs in [his book](https://book.douban.com/subject/30408662/), I can find some strength.

## Hold

### The Analects of Confucius

Last year I took the course [Brand marketing of Mr. Hua Shan](https://mp.weixin.qq.com/s/wL6SNTcjxJQWmbKTse5WIQ) on Gotit.app. I enjoyed it in reading his book *[Hua Shan Explains The Analects of Confucius Completely](https://book.douban.com/subject/26913479/)* that I borrowed from the library. It tells some reasonings in everyday life in the Chinese culture, which I found to be my basis of feelings when contact with people. I had started to read Prof. Qian Mu's [New Explanation of The Analects of Confucius](https://book.douban.com/subject/6775830/) in 2017. But abandoned it with a new task because it is a luxury to read this kind of book as an adult without a job. Now, I have other issues to deal with, so I will hold on to these wishes until I found a job earning money.

# Methodology

## Occupy

### Attraction Radar

This is what I adopted after engagement with [ThoughtWorks's Technology Radar](https://www.thoughtworks.com/radar). I think it might become a [proper tool](../cn/2020/07/mechanics-on-attraction-radar/) for me to manage my attention. As I will respect my attraction radar, I have read through their Technology Radar and keep an eye on it in the future.

## Engage

### Personal OKRs

OKRs are practical tools for active workers besides KPIs in an organization full of intelligence. I am not in a particular firm, but I want to place myself in the community of open-source CAD software. I need to navigate my story finding the HOW and WHAT from WHY, and need to separate it into objectives and define the SMART vital results. I have seen [John Doerr's TED talk on OKRs](https://www.ted.com/talks/john_doerr_why_the_secret_to_success_is_setting_the_right_goals/transcript) in [Mr. Yu's article about OKRs](https://mp.weixin.qq.com/s/rnYHBCZy6HeEH-QVS3MWqg), and I am reading his book: [*Measure What Matters - How Google, Bono, and the Gates Foundation Rock the World with OKRs*](https://book.douban.com/subject/30396635/).

### On Becoming a Programmer

No way staying at being an amateur, I want to join the roles of Onshape founders and ThoughtWorkers. I would like to read those guidelines as in these books:
1) Jeff Xiong's *Can't Stop - A Software Craftsman's 12 years* is the stories behind his amazing blogs. [不敢止步](https://book.douban.com/subject/26135794/) has been bought at duozhuayu.com.
2) Andy Hunt's *Pragmatic Thinking and Learning_ Refactor Your Wetware* (Pragmatic Programmers) (2008, Pragmatic Bookshelf). [程序员思维修炼](https://book.douban.com/subject/26268555/) has been bought from kongfz.com.
3) Robert C. Martin's *The Clean Coder - A Code of Conduct for Professional Programmers* (2011, Prentice Hall). [代码整洁之道:程序员的职业素养](https://book.douban.com/subject/26919457/) has been borrowed from library.
4) Robert C. Martin's *Clean Code - A Handbook of Agile Software Craftsmanship*. [代码整洁之道](https://book.douban.com/subject/4199741/) has been bought at duozhuayu.com.
5) Dustin Boswell, Trevor Foucher's *The Art of Readable Code* (2011, O'Reilly Media). [编写可读代码的艺术 ](https://book.douban.com/subject/10797189/) is on the bookshelf of Gotit.app. 
6) Jeff Xiong's *A History of Agile in China* . [敏捷中国史话](https://book.douban.com/subject/35066500/) has been borrowed from library.
7) Chinese ThoughtWorkers' [软件开发践行录 : ThoughtWorks中国区文集](https://book.douban.com/subject/25952573/) has been borrowed from library.
8) Neal Ford's *The productive programmer* (2008, O'Reilly Media) is translated by Jeff Xiong, too. [卓有成效的程序员](https://book.douban.com/subject/3558788/) could be bought at duozhuyu.com.

## Concern

### Structures in Mathematics

If I want to learn the logical part, I need to spend most of my time deducing and solving problems. I have spent half of my study time reading mathematics. I recently heard from Dr. Wu Jun that there are clues in math that act as the bridge between its nature and usages, which doesn't need so much time to learn so much concrete points of knowledge. I had better understand Dr. Wu's [course](https://mp.weixin.qq.com/s/nQNB3iVxcRZvri0IY6PuIw) throughout.

### Science in Learning

I am entering a new era of engineering software. I need to learn a lot of topics efficiently and effectively. Wan Weigang had gathered his articles about learning science into a book called [*What is Learning in the End*](https://book.douban.com/subject/35082292/). He has posted a series of articles reporting his new earnings in reading [How We Learn: Why Brains Learn Better Than Any Machine... for now](https://book.douban.com/subject/35013354/). I found some advice valuable about being a pragmatic programmer in the reading radar of thoughtworkers. 

## Hold

### Reading Tech Documents

In [Dr. Wu Jun's course, Reading and Writing](https://mp.weixin.qq.com/s/JkfgFfZnKlvWyg3oSxzzdA), he proposed reading steps when entering a professional field: 1) Orthodox literature, 2) authoritative reviews and 3) academic monographs. I had better read and learn with such frameworks, rather than by instinct. 

### Open Source Releasing

I release [TetraCamThon](https://github.com/John-Qu/tetracamthon) with a ReadMe, but I don't know what to include in it. I just looked at what other repositories do. Still, there should have been some code of conduct in releasing an open-source project for public users and contributors, such as Zalando's "[How we release open source projects](https://opensource.zalando.com/blog/2019/05/How-We-Release-Code/)."

### HTML Slide

I like the slides in HTML, such as [Xie Yihui's xaringan introduction](http://slides.yihui.org/xaringan/zh-CN.html) and Prof. [Daniel Jackson](http://people.csail.mit.edu/dnj/)'s [JavaScript Overview](http://people.csail.mit.edu/dnj/teaching/6170/javascript-live/modules/basics/slides.html#/). Xie said it is easy to construct this kind of [slides from Rmarkdown](https://bookdown.org/yihui/rmarkdown/xaringan.html). If I can figure out how to do it in half an hour, I would like to adopt it. Maybe I will try it when I make presentation the next time.


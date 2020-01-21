Hello sliptonic,

Happy new year. 

I am John Qu, the Chinese translator of your *FreeCAD For Inventors*. 

I notice in the subscribed mailing that you are active in developing Path workbench of FC. I have been on a personal [project](https://github.com/John-Qu/tetracamthon), calculating a cam profile, and translated half of @yorik's [manual](https://www.freecadweb.org/wiki/Manual:Introduction/zh-cn) pages in April and May last year.

Recently I was building [my blog site](http://johnqu.site) with [Yihui Xie](http://yihui.org) 's [blogdown](https://github.com/rstudio/blogdown) package. I wonder if I can put the translating work in my vitae with a link pointing to the online version as those books in "[www.bookdown.org](www.bookdown.org)".

I am sorry for failing to fetch an editor for proofreading of the Chinese version. How about FFI's German version? I noticed on your repo that @PLCris last committed seven months ago. 

If I can have your permission, I would like to

-  update the example screenshots with FC019 (and try to keep it up to date later on)
-  keep the contents and explanation as it is (you are author, I only translate your meaning)
-  make the Chinese version branch public on Github (for editing and comment)
-  publish FFI Chinese version on bookdown.org (they accept books other than R), and
-  give clear acclaim to [your post](https://forum.freecadweb.org/viewtopic.php?f=8&t=30959#p256564) and links to the pages on [amazon](https://www.amazon.com/dp/B07H9RV5X6/ref=cm_sw_r_cp_ep_dp_GNzNBb50V8HNH) and [kobo](https://www.kobo.com/us/en/ebook/freecad-for-inventors) (someone will decide to read the original version). 

What is your consideration if FFI (or its translated version) goes to the public domain? You have created a product. What is it a proper time to turn FFI into a gift? 

Best Regards

Yours sincerely

John Qu

2020-01-08

---

Hi John, Good to hear from you! You had a new baby didn't you? I hope all is well with you.

>  I notice in the subscribed mailing that you are active in developing Path workbench of FC. I have been on a personal [project](https://github.com/John-Qu/tetracamthon), calculating a cam profile, and translated half of @yorik's [manual](https://www.freecadweb.org/wiki/Manual:Introduction/zh-cn) pages in April and May last year.

Yes, I'm the 'workbench captain' for Path. I started the workbench with Yorik and Dan Falck back in about 2014.

>  Recently I was building [my blog site](http://johnqu.site) with [Yihui Xie](http://yihui.org) 's [blogdown](https://github.com/rstudio/blogdown) package. I wonder if I can put the translating work in my vitae with a link pointing to the online version as those books in "[www.bookdown.org](http://www.bookdown.org)". 

You can certainly list the work on your vitae. For discussion of linking to an online version, read below.

>  I am sorry for failing to fetch an editor for proofreading of the Chinese version. How about FFI's German version? I noticed on your repo that @PLCris last committed seven months ago. 

ChrisB has finished the german translation but has had a hard time getting it proofread. We're hoping to finish that up in the next week or so. Then it will go live on Kobo. We have another guy interested in doing a portuguese version.

>  If I can have your permission, I would like to
>
>  -  update the example screenshots with FC019 (and try to keep it up to date later on)
>  -  keep the contents and explanation as it is (you are author, I only translate your meaning)
>  -  make the Chinese version branch public on Github (for editing and comment)
>  -  publish FFI Chinese version on [bookdown.org](http://bookdown.org) (they accept books other than R), and
>  -  give clear acclaim to [your post](https://forum.freecadweb.org/viewtopic.php?f=8&t=30959#p256564) and links to the pages on [amazon](https://www.amazon.com/dp/B07H9RV5X6/ref=cm_sw_r_cp_ep_dp_GNzNBb50V8HNH) and [kobo](https://www.kobo.com/us/en/ebook/freecad-for-inventors) (someone will decide to read the original version). 
>  
>  What is your consideration if FFI (or its translated version) goes to the public domain? You have created a product. What is it a proper time to turn FFI into a gift? 

I don't intend to release the copyright of the book into the public domain at all. That would allow someone else to take the text, revise it in the future and sell it. 

However, I very much DO want to release a free (of charge) version online. I think that's the right thing to do for the community and for the book. The question is when. 

I've had some conversation with my publisher and a few others. I think I'd like to continue to revise the book for future versions and when a new version of FreeCAD is released, a new version of the book would come out and the old version would be released in a free form online. So when version 0.19 comes out, we would make 0.18 free to download and make the 0.19 version of the book available for sale.

In 2012 when Dan Falck and I wrote the first book for Packt publishing, we didn't make very much money and that was fine. We didn't do it to get rich. But a couple years later we had the opportunity to use that money to pay Yorik for development on the original core of Path workbench. This turned out to be incredibly important.

I don't make very much money from the sale of this new book but I feel strongly about making something because I believe it can lead to the next opportunity. Maybe I can sponsor a developer to work on other algorithms or pay to get developers to a conference. 

Sometimes making money is about putting groceries on the table but other times it's about reinvesting in the project itself. Does that make sense?

I would suggest this:

1) By all means, feel free to update the book for 0.19. Just keep the 0.19 changes in a new branch.

2) Let's publish the chinese version on kobo. You set the price. Anything more than $0.00 is fine with me. We split royalties as agreed through Purple Squirrel.

3) Release one chapter (Batman?) free of charge on github and bookdown.

4) when 0.19 version of the book is released, we release the rest of 0.18 for free.

Tell me what you think

-Brad

---

Re: [FFI/Chinese] Willing to accepted the offer but come with doult 

Hello Brad,

Thank you for your reply, with so much explanation. My son and daughter can play together now, and I spend most of my spare (someday full) time with them. They inspire me a lot.

I had accepted your proposals early this morning.

>  I would suggest this:
>
>  1) By all means, feel free to update the book for 0.19. Just keep the 0.19 changes in a new branch.
>
>  2) Let's publish the chinese version on kobo. You set the price. Anything more than $0.00 is fine with me. We split royalties as agreed through Purple Squirrel.
>
>  3) Release one chapter (Batman?) free of charge on github and bookdown.
>
>  4) when 0.19 version of the book is released, we release the rest of 0.18 for free.
>
>  Tell me what you think

But after considering them for a few hours, I have to say, "no, thanks." Here are my initial ideas and later considerations. 

First, let's discuss the money.

I was thinking about setting the price of the Chinese version as of 0.17 (about one yuan, a little tip for an article on Wechat App). But am I serious or just kidding? If I am serious, do I dare to speak aloud among friends that I am selling a translated book written for 0.17 but they actually found 0.19 is recommended now? If I am not serious, why do I bother you and Dupuy to publish it on Kobo? 

I admire your belief that money can lead to opportunities. I can't say how much, but your work does make some money. However, I believe cash both in my left and right pocket is mine, which is a kind of resource I can use to achieve my desires. It seems the amount you pay @yorik for the work of Path core code is equal to what you got with the first book for Packt publishing. I guess there surely will be a Path workbench if you didn't earn any money from that bookselling. Could @yorik help for free, couldn't he?

In this case, the money point opposite my direction. I want more people to see my work. But money, as a kind of wall, keep them away.

Second, let's discuss the publishing.

You recommended that I make a chapter (such as Batman) on GitHub and bookdown. I was thinking about the opportunity that we make more content public, such as chapter 5 feathers in part one and chapter 14 cam in part three because FFI has three parts, and these three chapters are most valuable for me. However, when I scan the translated texts, I am eager to edit the sentences and reformat the paragraphs. I realized that the publishing of these chapters means something for me, but fails in helping readers. It only shows I can translate such technical English texts into such a level of Chinese. It will not help the readers enter the CAD world for it is only sample chapters, saying, "go to buy, or go away."

I learn Python by reading Prof. Downey's Think Python. He felt the same inconvenience with you as he says:

>  If your book is your baby, it's hard to let strangers have their way with it. But if you want creative people to work with your material, you have to allow them to take ownership.
>
>  ---- [Free Books, Why Not](http://www.greenteapress.com/free_books.html).

His book is about computational thinking, while our book is about CAD tools. He sells 12/2000 hard copies in the first week, ten of them in his mother's hand. FreeCAD faces some engineering fields, and there are many other commercial tools in the market. FreeCAD is free to download and under a massive development, while my former colleagues are still using Solidworks 2011 without a license. Is there any better way to publish a tool coaching book for short shelf time? 

Xie believes the conventional way is not necessary nowadays. Although his book is publishing via a publisher, he asks no author money (actually he cannot get directly by law) to let the hard copy cheaper and easier to deliver to many R/Rstudio users. More readers, more comments, more typo trackers, more critics. Those sounds might trigger these action as to:

-  update quickly, on time, no known mistake hanging for the next edition
-  push author(s) continuously iterate, improve, keep up with version and
-  inspire more contributors and translators involved in this list.

You plan to release v017 (my objective version) for free when the book for 019 is on kobo. I am a little doubt whether someone will take his time to read it when he is struggling with FreeCAD 019. FC 017 is in python 2, and from 018 FC is in python 3. I know it makes no difference for FFI, but if I were a newcomer who knows nothing about the inner working of FC, I would be confused about choosing a new edition with money or the outdated version because it is free.

In general, what I want to say is the relationship.

To quote NormandC:

>  I think this close relationship between end users and developers that we have here is unrivalled in the CAD world. 
>
>  ---- [Re: FreeCAD For Inventors Book Published](https://forum.freecadweb.org/viewtopic.php?f=8&t=30959&start=10#p256732)

My intension in translating FFI in October 2018 are 1) admiring the gifts here and found a [chance to give back](https://forum.freecadweb.org/viewtopic.php?f=8&t=30959&start=10#p263141), 2) get used to FC's documentation and 3) learn the style of conduct with interactive with developers (yes, it's you, thank you, sliptonic :). Now what I got is more valuable for myself.

-  I realize that a translation needs a personal meaning. For me, if I cannot understand both the texts and intension and make the conversion more comfortable to read, I should better not to start it.
-  I notice that I am mostly inspired by people's reactions. Although I stopped at [Manual:Traditional_2D_drafting/zh-cn](https://www.freecadweb.org/wiki/Manual:Traditional_2D_drafting/zh-cn), but after noticing @wconly [acclaimed](https://forum.freecadweb.org/viewtopic.php?f=40&t=37167#p315958) at that, I am thinking about finishing the manual translation work.
-  I acknowledge that open-source development has its own economy. I read [The Cathedral and the Bazaar](http://www.catb.org/esr/writings/cathedral-bazaar/), and take steps (personal blog site, etc.) according to the FAQ on [How To Become A Hacker](http://www.catb.org/~esr/faqs/hacker-howto.html).

I have gotten what I want, you might have gotten yours. 

I thought you have forgotten FFI, leaving its repo uncommitted for over a year. So I mail you to ask and see if I need to spend some time on updating and editing in our traditional spring festival in China. Now I think I should put more effort into my own cam profile scripts, and see if someday I can write my book.

Thank you anyway for replying to me with a rich explanation. I love all the PM and mail discussions you sent to me. They gave me the feeling of doing something bigger than myself's study.

Best regards

Yours sincerely

John Qu

2020-01-09

---

John, 

This is a wonderful response! I don't agree with everything but your reasoning and explanation are very helpful. Thank you.

Also, I have made a mistake that I need to fix.

First, there is no version 0.19 of the software. That's how we refer to the development version but it has not been released and may never be released under that number. There's talk that the next version may be 1.0. We will have to wait and see.

The current stable version of the software is 0.18. There were very few changes to the software that affected the book and I consider the book to be fully applicable to 0.18. My mistake was that I thought we had already re-branded the book for 0.18 and revised the cover. Apparently we have not. 

So my suggestion was not that the free and paid version be 0.17 and 0.19 but rather 0.18 and 0.19/1.0. That's confusing but I think you understand. The goal would be to release a new paid version of the book as soon as possible after the stable software releases and make the previous version free.

>  I admire your belief that money can lead to opportunities. I can't say how much, but your work does make some money. However, I believe cash both in my left and right pocket is mine, which is a kind of resource I can use to achieve my desires. It seems the amount you pay @yorik for the work of Path core code is equal to what you got with the first book for Packt publishing. I guess there surely will be a Path workbench if you didn't earn any money from that bookselling. Could @yorik help for free, couldn't he?

Actually, no. Someone else might have written a CAM workbench but it would have been an add-on and not integrated into the core of FreeCAD. That happened because Yorik is a core developer and consulted with Juergen Riegel, the founder of FreeCAD, on the design. When this happened Brazil was having a very bad economic time. Yorik needed extra (paid) work because his architecture business wasn't bringing in enough. When he's able to work on FreeCAD for free, he prefers to work on Arch workbench. We were able to pay him to work on FreeCAD, just in a different area. He has not contributed to Path since then. It was good for everyone but would not have happened without the royalty money and he would have had to do some non-FreeCAD work. 

I also believe that the money in my pocket is mine to achieve my desires. Part of my desire is to further FreeCAD and sometimes that ONLY happens with money. At the end of the month, I will get to go to Brussels to the FOSDEM conference and meet yorik for the first time. We are doing a presentation together with another FreeCAD developer. This trip is possible because of the book and also because the FreeCAD project has received some donation money. 

>  I acknowledge that open-source development has its own economy. I read [The Cathedral and the Bazaar](http://www.catb.org/esr/writings/cathedral-bazaar/), and take steps (personal blog site, etc.) according to the FAQ on [How To Become A Hacker](http://www.catb.org/~esr/faqs/hacker-howto.html).

CatB is an amazing book that heavily inspired me, but it is now more than twenty years old and the open-source economy is still evolving. Github has acknowledged that we need more ways for open source contributors to make money. This video has gotten some discussion as well. The 'Heartbleed virus issue' was a wake-up call.

[ The Rise of Open-Source Software](https://youtu.be/SpeDK1TPbew)

I believe very strongly in open-source software but there's a saying "Do not muzzle an ox while it is treading out the grain". I think this means we need to strive to find a balance between taking value and giving it.

With that said, I don't feel so strongly to say, 'no'. If you want to release your translated version for free, I support it. But we should release a paid version on Kobo at the same time. 

This is what Downey did with his Python books so, why not? 

-Brad

---

Hi Brad,

I am glad to hear your kind reply. 

I watched the video of CNBC, but I can't catch up with its speed even with screen scripts. I'm afraid I don't understand much about the software world, not to mention the economy of the open-source movement. Sorry, I am not to teach you something, and I want to report to you what has taught me.

As for the relationship between you and @yorik, thank you for telling me more about the details of your collaboration experience. You did something in a field and earned an amount of money. When you need something you paid that money back. The former affair seemed to trigger the latter. If I haven't mistaken you too much, money is a kind of fire. Its growth means people need it. Its burning inspired you to do more for the community. In this consideration, money in this project is a must for you.

I found it seems to be an easy (actually not too easy) chance to make my contribution because [you were welcome to @shiftee's typo PM](https://forum.freecadweb.org/viewtopic.php?f=8&t=30959&start=10#p259153). I am (maybe extremely) eager to affect people. I want to receive reactions, no matter plus or minus. It is this feedback that pushes me to do more. In this consideration, show off in this project seems a must for me.

I want to keep up with your plan to release a new paid version when FC 1.0 is on board. Before that, I insist on making a free-to-read version online. From one hand, I would proofread the texts myself. With fresh eyes one-year latter, I think I can do it. From another hand, someone on the Chinese forum might found some error and make an issue for me. At the same time, I will regenerate the screenshots with FreeCAD-0.19-18775, which I downloaded at 2019-11-26. You might ask why not use 0.18 if I plan to publish it online? I noticed that 0.18.x is not recommended for Mac OS. I think that won't conflict with our new release version if the latter will incorporate a lot of updated texts(I am sure it does :).

Tomorrow (11, Jan.) I will go to my wife's home village in Wuhan and go back to shanghai on February 1st (You are in Brussels at that time). I am not sure my net condition can support many PR and email, but I will try to keep in touch with you and report any progress and actions of mine. I think at least by 2nd Feb, I will pull to your repo a completely edited Chinese translation. That can be the base material to publish on kobo then. 

I hope your FOSDEM conference report success and the offline meetup with other developers turn to be a happy story. I think I should do more and learn more in the FC community, in order to have something to say, in case that one day I meet with you guys. 

Best regards

Yours sincerely

John Qu

2020-01-10

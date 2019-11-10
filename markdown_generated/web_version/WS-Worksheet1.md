
<!-- File generated from pihw.com (_inc\web_version\start.txt) -->
##Pi-Stop Resource Files##
These Pi-Stop resource are available as fully customisable [Markdown documents](https://github.com/PiHw/Pi-Stop/tree/master/markdown_source) on the [Pi-Stop github](https://github.com/PiHw/Pi-Stop) page.

Each of the guides are also available in [PDF format](https://github.com/PiHw/Pi-Stop/tree/master/pdf), and in several other automatically [generated variants](https://github.com/PiHw/Pi-Stop/tree/master/markdownmark/down_generated/) (for example, this includes versions which have instructions for the [Model Plus only](https://github.com/PiHw/Pi-Stop/tree/master/markdownmark/down_generated/model_plus_only), or the [original model](https://github.com/PiHw/Pi-Stop/tree/master/markdownmark/down_generated/model_original_only)).


----------

----------
<!-- How to use comments in these files -->
<!-- ---------------------------------- -->
<!--Comments have been put in this file so that they can be customised for a range of workshops and uses.

[How to customise the Markdown documents](CustomMarkdown.md)-->

<!-- -----------------------------------------------------
-->
<!-- Enable sections for the new model plus (Post-July 2014) define  -->
<!-- Enable sections for the older model (Pre-July 2014)  define  -->
<!-- -----------------------------------------------------
-->


<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/pihwlogotm.png" width=150 />
----------

<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/space.png" height=10/>
<p>
##NAME:##
-----------------


##<a href="http://pihw.wordpress.com/lessons/pi-stop-workshops/Setup-ScratchGPIO.html">**Setup: Scratch GPIO**</a>##


<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/R.png" width=1000 height=50 />
Explains how to setup Scratch GPIO.

*You must perform this step in order to use the **Pi-Stop** with Scratch.*
<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/CheckClear.png" height=50/> **I have installed Scratch GPIO!**
<p>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/space.png" height=20/>
<p>
<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/CheckClear.png" height=50/> **I have powered down the Raspberry Pi and fitted the Pi-Stop in Location A**
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/space.png" height=20/>
<p>
**Location A for Model A+, B+ or Raspberry Pi 2 (purchased after July 2014)**
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/PiStopLocationPlusA.png" height=300 />
**Location A for Model A or B (purchased before July 2014)**
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/PiStopLocationA.png" height=300 />
<p>
<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/CheckClear.png" height=50/> **I have tested Scratch GPIO with the Pi-Stop and it works!** 
<p>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/space.png" height=10/>
<p>


##<a href="http://pihw.wordpress.com/lessons/pi-stop-workshops/ExploreScratchGPIO-PiStopFirstSteps.html">**Explore and Challenge Scratch GPIO: Pi-Stop First Steps**</a>##

<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/Y.png" width=1000 height=50 />
Introduces how to use Scratch and using Scratch GPIO.

*If you are already familiar with Scratch you can skip this.*
<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/CheckClear.png" height=50/> **I now know the different parts of Scatch**
<p>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/space.png" height=30/>
<p>
<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/CheckClear.png" height=50/> **Scratch GPIO with a Flashing RED Light Completed!**
<p>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/space.png" height=50/>
<p>


##<a href="http://pihw.wordpress.com/lessons/pi-stop-workshops/ExploreScratchGPIO-PiStopTrafficSequence.html">**Explore and Challenge Scratch GPIO: Pi-Stop Traffic Sequence**</a>##

<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/G.png" width=1000 height=50 />
Create your own traffic light sequence and learn how to use Scratch GPIO with the **Pi-Stop**.

**WORKSHEET:** Colour in the correct traffic light order below, then fill in the required **broadcast** commands **on** or **off**.
Use the following diagram to determine which pins are connected with each colour on the traffic light.
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/PiStopLocationA.png" height=200/>

First the traffic light sequence for changing from **STOP** to **GO**.
#STOP#
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/pi-stoptopR.png" height=180/>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/broadcastSTOP.png" height=80/>

-----------------
#PREPARE TO GO#
<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/pi-stoptopoff.png" height=180/>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/broadcastblockpin.png" height=140/>

-----------------
#Wait#
To stop the lights changing instantly, we need to wait before we change them again!
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/space.png" height=70 width=180/>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/wait1sec.png" height=50/>

-----------------
#GO#
<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/pi-stoptopoff.png" height=180/>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/broadcastblock.png" height=140/>
<p>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/space.png" height=50/>
<p>
<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/CheckClear.png" height=50/>**Traffic Light Sequence STOP to GO**

------------------
------------------
Next the traffic light sequence for changing from **GO** back to **STOP**. 
#GO#
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/pi-stoptopG.png" height=180/>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/broadcastGO.png" height=100/>

-----------------
#PREPARE TO STOP#
<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/pi-stoptopoff.png" height=180/>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/broadcastblock.png" height=140/>
-----------------
#Wait#
Again, to stop the lights changing instantly, we need to wait.
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/space.png" height=70 width=180/>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/wait1sec.png" height=50/>
-----------------

#STOP#
<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/pi-stoptopoff.png" height=180/>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/broadcastblock.png" height=140/>

<p>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/space.png" height=50/>
<p>
<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/CheckClear.png" height=50/>**Traffic Light Sequence GO to STOP**
<p>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/space.png" height=30/>
--------
<p>
<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/CheckClear.png" height=50/>**I've created the Pi-Stop STOP and GO sequences**
<p>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/space.png" height=30/>
<p>
<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/CheckClear.png" height=50/>**I've created the Pi-Stop the full Traffic Light Sequence**
<p>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/space.png" height=30/>
<p>
<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/CheckClear.png" height=50/>**Extended Task: Created a racing start light control**
<p>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/space.png" height=30/>
<p>
<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/CheckClear.png" height=50/>**Extended Task: Controlled two Pi-Stops at the same time!**
<p>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/space.png" height=60/>


##<a href="http://pihw.wordpress.com/lessons/pi-stop-workshops/ExploreScratchGPIO-PiStopReactionGame.html">**Explore and Challenge Scratch GPIO: Pi-Stop Reaction Game**</a>##

<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/G.png" width=1000 height=50 />
How fast are your reflexes?  Test your reaction time with the Pi-Stop Reaction game.
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/space.png" height=20/>
<p>

<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/CheckClear.png" height=50/> **WORKSHEET:** Tick the checkbox marked **"I've created the Pi-Stop Reaction Game"**.

***Don't forget to write down your best score!***
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/CheckBlank.png" height=100 width=140/>
<p>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/space.png" height=10/>


##<a href="http://pihw.wordpress.com/lessons/pi-stop-workshops/ExploreScratchGPIO-PiStopSimonGame.html">**Explore and Challenge Scratch GPIO: Pi-Stop Simon Memory Game**</a>##

<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/G.png" width=1000 height=50 />
Challenge your memory and get the highest score!

<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/CheckClear.png" height=50/> **WORKSHEET:** Tick the checkbox marked **"The first part of the Pi-Stop Simon Memory Game works!"**.
<p>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/space.png" height=20/>
<p>
<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/CheckClear.png" height=50/> **WORKSHEET:** Tick the checkbox marked **"I've created the Pi-Stop Simon Memory Game"**.

***Don't forget to write down your best score!***
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/CheckBlank.png" height=100 width=140/>
<p>

--------------------
**Congratulations: You have reached the end of the workshop!**

<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/LogoDesignNormal.png" height=100/>
I hope you enjoyed it.

***You can buy your own Pi-Stop today, £3 each or two for £5.***

The **Pi-Stop** are also available to buy from [www.4tronix.co.uk](http://www.4tronix.co.uk), and additional material and guides are available from my website [www.PiHardware.com ](http://www.PiHardware.com )


> For further Raspberry Pi help/advice or to enquire about **classroom/workshop packs**:

> Contact  me (Tim Cox) at [pihw-orders@hotmail.co.uk](pihw-orders@hotmail.co.uk)

My ***Raspberry Pi Python Cookbook for Python Programmers*** is available to buy:
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/book.jpg" height=300/><p>

**[http://goo.gl/dmVtsc](http://goo.gl/dmVtsc)**

<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/space.png" height=20/><p>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/pihwlogotm.png" width=80 /><img style="float:right" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/4tronix.jpg" width=100 />



----------

----------

#Where to get your Pi-Stop#
The Pi-Stop was designed in partnership between [4Tronix.co.uk](http://4Tronix.co.uk) and [PiHardware.com](http://pihardware.com).

<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/4tronix.jpg" width=100 />
The [Pi-Stop](http://4tronix.co.uk/store/index.php?rt=product/product&product_id=390) and accessories are available from the [4Tronix.co.uk](http://4Tronix.co.uk) shop.


--------------------------
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="http://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />The Pi-Stop workshop materials are licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>

----------------------
*The Pi-Stop name and logo are Trademark of PiHardware.com and the design is Copyright 2014 of 4Tronix.com and PiHardware.com.*


<!-- File generated from pihw.com (_inc\web_version\stop.txt) -->

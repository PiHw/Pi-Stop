
<!-- File generated from pihw.com (_inc\webgit_version\start.txt) -->


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


<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/pihwlogotm.png" width=225 />
----------
<p>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/space.png" height=20/>
<p>
##NAME:##
-----------------


##<a href="https://github.com/PiHw/Pi-Stop/blob/master/markdown_source/Setup-ScratchGPIO.md">**Setup: Scratch GPIO**</a>##


<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/R.png" width=1000 height=50 />
Explains how to setup Scratch GPIO.

*You must perform this step in order to use the **Pi-Stop** with Scratch.*
<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/CheckClear.png" height=50/> **I have installed Scratch GPIO!**
<p>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/space.png" height=20/>
<p>
<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/CheckClear.png" height=50/> **I have powered down the Raspberry Pi and fitted the Pi-Stop in Location A**
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/space.png" height=20/>
<p>
**Location A for Model A+ or B+ (purchased after July 2014)**
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/PiStopLocationPlusA.png" height=300 />
**Location A for Model A or B (purchased before July 2014)**
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/PiStopLocationA.png" height=300 />
<p>
<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/CheckClear.png" height=50/> **I have tested Scratch GPIO with the Pi-Stop and it works!** 
<p>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/space.png" height=10/>
<p>


##<a href="https://github.com/PiHw/Pi-Stop/blob/master/markdown_source/ExploreScratchGPIO-PiStopFirstSteps.md">**Explore and Challenge Scratch GPIO: Pi-Stop First Steps**</a>##

<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/Y.png" width=1000 height=50 />
Introduces how to use Scratch and using Scratch GPIO.

*If you are already familiar with Scratch you can skip this.*
<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/CheckClear.png" height=50/> **I now know the different parts of Scatch**
<p>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/space.png" height=30/>
<p>
<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/CheckClear.png" height=50/> **Scratch GPIO with a Flashing RED Light Completed!**
<p>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/space.png" height=50/>
<p>


##<a href="https://github.com/PiHw/Pi-Stop/blob/master/markdown_source/ExploreScratchGPIO-PiStopTrafficSequence.md">**Explore and Challenge Scratch GPIO: Pi-Stop Traffic Sequence**</a>##

<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/G.png" width=1000 height=50 />
Create your own traffic light sequence and learn how to use Scratch GPIO with the **Pi-Stop**.

**WORKSHEET:** Colour in the correct traffic light order below, then fill in the required **broadcast** commands **on** or **off**.
Use the following diagram to determine which pins are connected with each colour on the traffic light.
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/PiStopLocationA.png" height=200/>

First the traffic light sequence for changing from **STOP** to **GO**.
#STOP#
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/pi-stoptopR.png" height=180/>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/broadcastSTOP.png" height=80/>

-----------------
#PREPARE TO GO#
<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/pi-stoptopoff.png" height=180/>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/broadcastblockpin.png" height=140/>

-----------------
#Wait#
To stop the lights changing instantly, we need to wait before we change them again!
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/space.png" height=70 width=180/>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/wait1sec.png" height=50/>

-----------------
#GO#
<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/pi-stoptopoff.png" height=180/>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/broadcastblock.png" height=140/>
<p>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/space.png" height=50/>
<p>
<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/CheckClear.png" height=50/>**Traffic Light Sequence STOP to GO**

------------------
------------------
Next the traffic light sequence for changing from **GO** back to **STOP**. 
#GO#
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/pi-stoptopG.png" height=180/>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/broadcastGO.png" height=100/>

-----------------
#PREPARE TO STOP#
<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/pi-stoptopoff.png" height=180/>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/broadcastblock.png" height=140/>
-----------------
#Wait#
Again, to stop the lights changing instantly, we need to wait.
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/space.png" height=70 width=180/>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/wait1sec.png" height=50/>
-----------------

#STOP#
<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/pi-stoptopoff.png" height=180/>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/broadcastblock.png" height=140/>

<p>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/space.png" height=50/>
<p>
<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/CheckClear.png" height=50/>**Traffic Light Sequence GO to STOP**
<p>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/space.png" height=30/>
--------
<p>
<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/CheckClear.png" height=50/>**I've created the Pi-Stop STOP and GO sequences**
<p>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/space.png" height=30/>
<p>
<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/CheckClear.png" height=50/>**I've created the Pi-Stop the full Traffic Light Sequence**
<p>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/space.png" height=30/>
<p>
<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/CheckClear.png" height=50/>**Extended Task: Created a racing start light control**
<p>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/space.png" height=30/>
<p>
<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/CheckClear.png" height=50/>**Extended Task: Controlled two Pi-Stops at the same time!**
<p>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/space.png" height=60/>


##<a href="https://github.com/PiHw/Pi-Stop/blob/master/markdown_source/ExploreScratchGPIO-PiStopReactionGame.md">**Explore and Challenge Scratch GPIO: Pi-Stop Reaction Game**</a>##

<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/G.png" width=1000 height=50 />
How fast are your reflexes?  Test your reaction time with the Pi-Stop Reaction game.
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/space.png" height=20/>
<p>

<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/CheckClear.png" height=50/> **WORKSHEET:** Tick the checkbox marked **"I've created the Pi-Stop Reaction Game"**.

***Don't forget to write down your best score!***
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/CheckBlank.png" height=100 width=140/>
<p>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/space.png" height=10/>


##<a href="https://github.com/PiHw/Pi-Stop/blob/master/markdown_source/ExploreScratchGPIO-PiStopSimonGame.md">**Explore and Challenge Scratch GPIO: Pi-Stop Simon Memory Game**</a>##

<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/G.png" width=1000 height=50 />
Challenge your memory and get the highest score!

<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/CheckClear.png" height=50/> **WORKSHEET:** Tick the checkbox marked **"The first part of the Pi-Stop Simon Memory Game works!"**.
<p>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/space.png" height=20/>
<p>
<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/CheckClear.png" height=50/> **WORKSHEET:** Tick the checkbox marked **"I've created the Pi-Stop Simon Memory Game"**.

***Don't forget to write down your best score!***
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/CheckBlank.png" height=100 width=140/>
<p>

--------------------
**Congratulations: You have reached the end of the workshop!**

<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/LogoDesignNormal.png" height=100/>
I hope you enjoyed it.

Remember the **Pi-Stop** will be available to buy from [www.4tronix.co.uk](http://www.4tronix.co.uk), and additional material and guides will be available from my website [www.PiHardware.com ](http://www.PiHardware.com )


> To reserve your own Pi-Stops, to enquire about **classroom/workshop packs**, or for Raspberry Pi help/advice:

> Contact  me (Tim Cox) at [pihw-orders@hotmail.co.uk](pihw-orders@hotmail.co.uk)

My ***Raspberry Pi Python Cookbook for Python Programmers*** is available to buy:

**[http://goo.gl/dmVtsc](http://goo.gl/dmVtsc)**

<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/space.png" height=20/><p>
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/pihwlogotm.png" width=80 /><img style="float:right" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/4tronix.jpg" width=100 />


<!-- File generated from pihw.com (_inc\webgit_version\stop.txt) -->

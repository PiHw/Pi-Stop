<!---#include "define.txt"--->
<!---#include "start.txt"--->
<!-- How to use comments in these files -->
<!-- ---------------------------------- -->
<!--Comments have been put in this file so that they can be customised for a range of workshops and uses.

[How to customise the Markdown documents](CustomMarkdown.md)-->

<!-- -----------------------------------------------------
-->
<!-- Enable sections for the new model plus (Post-July 2014) define WANT_MODEL_PLUS -->
<!-- Enable sections for the older model (Pre-July 2014)  define WANT_MODEL_ORG -->
<!-- -----------------------------------------------------
-->


<img src="img/pihwlogotm.png" width=150 />
----------

<img src="img/space.png" height=10/>
<p>
##NAME:##
-----------------

<!---#ifdef ALT_LINK--->
<!---
##<a href="FILE_SRC/Setup-ScratchGPIO.FILE_SRC_EXT">**Setup: Scratch GPIO**</a>##
--->
<!---#else--->
##[**Setup: Scratch GPIO**](Setup-ScratchGPIO.md)##
<!---#endif--->

<img src="img/R.png" width=1000 height=50 />
Explains how to setup Scratch GPIO.

*You must perform this step in order to use the **Pi-Stop** with Scratch.*
<img style="float:left" src="img/CheckClear.png" height=50/> **I have installed Scratch GPIO!**
<p>
<img src="img/space.png" height=20/>
<p>
<img style="float:left" src="img/CheckClear.png" height=50/> **I have powered down the Raspberry Pi and fitted the Pi-Stop in Location A**
<img src="img/space.png" height=20/>
<p>
<!---#ifdef WANT_MODEL_PLUS--->
**Location A for Model A+, B+ or Raspberry Pi 2 (purchased after July 2014)**
<img src="img/PiStopLocationPlusA.png" height=300 />
<!---#endif--->
<!---#ifdef WANT_MODEL_ORG--->
**Location A for Model A or B (purchased before July 2014)**
<img src="img/PiStopLocationA.png" height=300 />
<!---#endif--->
<p>
<img style="float:left" src="img/CheckClear.png" height=50/> **I have tested Scratch GPIO with the Pi-Stop and it works!** 
<p>
<img src="img/space.png" height=10/>
<p>

<!---#ifdef ALT_LINK--->
<!---
##<a href="FILE_SRC/ExploreScratchGPIO-PiStopFirstSteps.FILE_SRC_EXT">**Explore and Challenge Scratch GPIO: Pi-Stop First Steps**</a>##
--->
<!---#else--->
##[**Explore and Challenge Scratch GPIO: Pi-Stop First Steps**](ExploreScratchGPIO-PiStopFirstSteps.md)##
<!---#endif--->
<img src="img/Y.png" width=1000 height=50 />
Introduces how to use Scratch and using Scratch GPIO.

*If you are already familiar with Scratch you can skip this.*
<img style="float:left" src="img/CheckClear.png" height=50/> **I now know the different parts of Scatch**
<p>
<img src="img/space.png" height=30/>
<p>
<img style="float:left" src="img/CheckClear.png" height=50/> **Scratch GPIO with a Flashing RED Light Completed!**
<p>
<img src="img/space.png" height=50/>
<p>

<!---#ifdef ALT_LINK--->
<!---
##<a href="FILE_SRC/ExploreScratchGPIO-PiStopTrafficSequence.FILE_SRC_EXT">**Explore and Challenge Scratch GPIO: Pi-Stop Traffic Sequence**</a>##
--->
<!---#else--->
##[**Explore and Challenge Scratch GPIO: Pi-Stop Traffic Sequence**](ExploreScratchGPIO-PiStopTrafficSequence.md)##
<!---#endif--->
<img src="img/G.png" width=1000 height=50 />
Create your own traffic light sequence and learn how to use Scratch GPIO with the **Pi-Stop**.

**WORKSHEET:** Colour in the correct traffic light order below, then fill in the required **broadcast** commands **on** or **off**.
Use the following diagram to determine which pins are connected with each colour on the traffic light.
<img src="img/PiStopLocationA.png" height=200/>

First the traffic light sequence for changing from **STOP** to **GO**.
#STOP#
<img src="img/pi-stoptopR.png" height=180/>
<img src="img/broadcastSTOP.png" height=80/>

-----------------
#PREPARE TO GO#
<img style="float:left" src="img/pi-stoptopoff.png" height=180/>
<img src="img/broadcastblockpin.png" height=140/>

-----------------
#Wait#
To stop the lights changing instantly, we need to wait before we change them again!
<img src="img/space.png" height=70 width=180/>
<img src="img/wait1sec.png" height=50/>

-----------------
#GO#
<img style="float:left" src="img/pi-stoptopoff.png" height=180/>
<img src="img/broadcastblock.png" height=140/>
<p>
<img src="img/space.png" height=50/>
<p>
<img style="float:left" src="img/CheckClear.png" height=50/>**Traffic Light Sequence STOP to GO**

------------------
------------------
Next the traffic light sequence for changing from **GO** back to **STOP**. 
#GO#
<img src="img/pi-stoptopG.png" height=180/>
<img src="img/broadcastGO.png" height=100/>

-----------------
#PREPARE TO STOP#
<img style="float:left" src="img/pi-stoptopoff.png" height=180/>
<img src="img/broadcastblock.png" height=140/>
-----------------
#Wait#
Again, to stop the lights changing instantly, we need to wait.
<img src="img/space.png" height=70 width=180/>
<img src="img/wait1sec.png" height=50/>
-----------------

#STOP#
<img style="float:left" src="img/pi-stoptopoff.png" height=180/>
<img src="img/broadcastblock.png" height=140/>

<p>
<img src="img/space.png" height=50/>
<p>
<img style="float:left" src="img/CheckClear.png" height=50/>**Traffic Light Sequence GO to STOP**
<p>
<img src="img/space.png" height=30/>
--------
<p>
<img style="float:left" src="img/CheckClear.png" height=50/>**I've created the Pi-Stop STOP and GO sequences**
<p>
<img src="img/space.png" height=30/>
<p>
<img style="float:left" src="img/CheckClear.png" height=50/>**I've created the Pi-Stop the full Traffic Light Sequence**
<p>
<img src="img/space.png" height=30/>
<p>
<img style="float:left" src="img/CheckClear.png" height=50/>**Extended Task: Created a racing start light control**
<p>
<img src="img/space.png" height=30/>
<p>
<img style="float:left" src="img/CheckClear.png" height=50/>**Extended Task: Controlled two Pi-Stops at the same time!**
<p>
<img src="img/space.png" height=60/>

<!---#ifdef ALT_LINK--->
<!---
##<a href="FILE_SRC/ExploreScratchGPIO-PiStopReactionGame.FILE_SRC_EXT">**Explore and Challenge Scratch GPIO: Pi-Stop Reaction Game**</a>##
--->
<!---#else--->
##[**Explore and Challenge Scratch GPIO: Pi-Stop Reaction Game**](ExploreScratchGPIO-PiStopReactionGame.md)##
<!---#endif--->
<img src="img/G.png" width=1000 height=50 />
How fast are your reflexes?  Test your reaction time with the Pi-Stop Reaction game.
<img src="img/space.png" height=20/>
<p>

<img style="float:left" src="img/CheckClear.png" height=50/> **WORKSHEET:** Tick the checkbox marked **"I've created the Pi-Stop Reaction Game"**.

***Don't forget to write down your best score!***
<img src="img/CheckBlank.png" height=100 width=140/>
<p>
<img src="img/space.png" height=10/>

<!---#ifdef ALT_LINK--->
<!---
##<a href="FILE_SRC/ExploreScratchGPIO-PiStopSimonGame.FILE_SRC_EXT">**Explore and Challenge Scratch GPIO: Pi-Stop Simon Memory Game**</a>##
--->
<!---#else--->
##[**Explore and Challenge Scratch GPIO: Pi-Stop Simon Memory Game**](ExploreScratchGPIO-PiStopSimonGame.md)##
<!---#endif--->
<img src="img/G.png" width=1000 height=50 />
Challenge your memory and get the highest score!

<img style="float:left" src="img/CheckClear.png" height=50/> **WORKSHEET:** Tick the checkbox marked **"The first part of the Pi-Stop Simon Memory Game works!"**.
<p>
<img src="img/space.png" height=20/>
<p>
<img style="float:left" src="img/CheckClear.png" height=50/> **WORKSHEET:** Tick the checkbox marked **"I've created the Pi-Stop Simon Memory Game"**.

***Don't forget to write down your best score!***
<img src="img/CheckBlank.png" height=100 width=140/>
<p>

--------------------
**Congratulations: You have reached the end of the workshop!**

<img src="img/LogoDesignNormal.png" height=100/>
I hope you enjoyed it.

***You can buy your own Pi-Stop today, £3 each or two for £5.***

The **Pi-Stop** are also available to buy from [www.4tronix.co.uk](http://www.4tronix.co.uk), and additional material and guides are available from my website [www.PiHardware.com ](http://www.PiHardware.com )


> For further Raspberry Pi help/advice or to enquire about **classroom/workshop packs**:

> Contact  me (Tim Cox) at [pihw-orders@hotmail.co.uk](pihw-orders@hotmail.co.uk)

My ***Raspberry Pi Python Cookbook for Python Programmers*** is available to buy:
<img src="img/book.jpg" height=300/><p>

**[http://goo.gl/dmVtsc](http://goo.gl/dmVtsc)**

<img src="img/space.png" height=20/><p>
<img src="img/pihwlogotm.png" width=80 /><img style="float:right" src="img/4tronix.jpg" width=100 />


<!---#include "stop.txt"--->

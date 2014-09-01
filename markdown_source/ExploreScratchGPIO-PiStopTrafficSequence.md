<img src="img/pihwlogotm.png" width=180 />

----------
<img src="img/G.png" width=1000 height=50 />

#Explore and Challenge:#
##The Pi-Stop Traffic Light Sequence##
<img src="img/LogoDesignNormal.png" height=100/>
> <img src="img/note.png" height=40/>
> **SEE ALSO:**
>
> [**Discover: The Pi-Stop**](Discover-PiStop.md): For more information about Pi-Stop and how to use it.
>  
> [**Setup: Scratch GPIO**](Setup-ScratchGPIO.md): For instructions on how to setup Scratch GPIO with Pi-Stop *(which is needed for this section)*.
>
> [**Explore and Challenge Scratch GPIO: Pi-Stop First Steps**](ExploreScratchGPIO-PiStopTrafficSequence.md): If you've not used Scratch before, this will provide a quick introduction to building your first Scratch GPIO program.

In this guide we make use of Scratch GPIO produce a standard traffic light sequence with the Pi-Stop.

###Getting Started###
The Pi-Stop should be connected to the Raspberry Pi in Location A, as follows:
<img src="img/PiStopLocationA.png" height=300/>
With the Pi-Stop fitted in the correct position you can now power up your Raspberry Pi.

###Run Scratch GPIO###
If you are still in the Raspberry Pi terminal, start the desktop environment using:

`startx
`

Open Scratch GPIO from the desktop using the Scratch GPIO icon (we do not need the *ScratchGPIO 5 Plus*):
<img src="img/ScratchGPIOIconOnly.png" height=100/>


**Scratch GPIO 5** is the standard version, while **Scratch GPIO 5 plus** provides additional support for several add-on boards.

> <img style="float:left" src="img/note.png" height=40/>
> **NOTE:** If you are using **X-Forwarding**, you can run Scratch GPIO with the following commands:
>
    sudo cp ~/.Xauthority ~root/
    sudo ~/scratchgpio5/./scratchgpio5.sh


###Get ready###
In this example we will use the following blocks, all of which are located in the **control** section:
<img src="img/ScratchControl.png" height=100/>

We will use one or more of the following:

- **broadcast** blocks
<img src="img/broadcastpin.png" height=30/>
- **wait** blocks
<img src="img/wait1sec.png" height=35/>
- **when I receive** blocks
<img src="img/broadcastGO.png" height=60/>
- **forever** block

> <img style="float:left" src="img/note.png" height=40/>
> **NOTE:** For more information on the **broadcast**, **wait** and **forever** blocks see
> [**Explore and Challenge Scratch GPIO: Pi-Stop First Steps**](ExploreScratchGPIO-PiStopTrafficSequence.md) which introduced them for the first time.

###Designing our traffic sequence###

Before we go any further we should take some time to work out what the correct sequence of lights a traffic light should show.  This way we can design our program and then test to see if it behaves as we wanted.
####The STOP Sequence####
<img src="img/quest.png" height=50/>**QUESTION:** When a traffic light is ***GREEN (GO)*** and starts to change, what lights will be lit as it changes to ***STOP*** the traffic?
 
<img src="img/pi-StopG.png" height=250/>
<img src="img/pi-StopBlank.png" height=250/>
<img src="img/pi-StopBlank.png" height=250/>
<img src="img/broadcastblockpin.png" height=120/>
<img src="img/broadcastblock.png" height=120/>

<p>
<img src="img/check.png" height=50/> **WORKSHEET:** On your worksheet colour in the correct traffic light sequence, starting with ***GREEN*** (as shown above) and ending with the light showing ***STOP***.

**WORKSHEET:** On the broadcast blocks fill in the required commands to switch **on** or **off** the appropriate LEDs (by switching **on** or **off** the pins),


####The GO Sequence####
<img src="img/quest.png" height=50/>**QUESTION:** When a traffic light is ***RED (STOP)*** and changes to ***GO***, what is the normal sequence of lights?

Again, fill in the required **broadcast** commands.
<img src="img/pi-StopR.png" height=250/>
<img src="img/pi-StopBlank.png" height=250/>
<img src="img/pi-StopBlank.png" height=250/>
<img src="img/broadcastblock.png" height=120/>
<img src="img/broadcastblock.png" height=120/>
<p>
<img src="img/check.png" height=50/> **WORKSHEET:** On your worksheet colour in the correct traffic light sequence, starting with ***RED*** and ending with the light showing GO.

**WORKSHEET:** Again, complete the required broadcast blocks to switch each of the lights on or off. 

*Great work!*

*You can now create each of the **broadcast** blocks in Scratch and click on them to test each step.*

<img src="img/space.png" height=60/>

###Putting the blocks together###
We will now create a new **broadcast** group of blocks to recreate the required LED sequence.
####The broadcast STOP Block####
Start the group with a **when I receive** block called **STOP**:
<img src="img/broadcastSTOP.png" height=60/>
Add our first light change:
<img src="img/broadcastblock.png" height=100/>
<p>
<img src="img/space.png" height=0/>
Add a wait block (so the lights do not change instantly):
<img src="img/wait1sec.png" height=40/>
<p>
<img src="img/space.png" height=0/>
Add our second light change:
<img src="img/broadcastblock.png" height=100/>
####Broadcast GO Block####
Simply do the same with the other light changes, but call this **when I receive** block **GO**:
<img src="img/broadcastGO.png" height=60/>

***Excellent!*** *Now you can test these blocks by clicking on them directly and see if we have our correct traffic light sequences!*
<img src="img/space.png" height=30/>
<p>
<img style="float:left" src="img/check.png" height=50/> **WORKSHEET:** Tick the checkbox marked **"I've created the Pi-Stop STOP and GO sequences"**
<img src="img/space.png" height=30/>
<p>
##The Final Program - Changing Lights##
At the moment our program will not do anything unless we click on it.

Just like we did in the previous guide ([**Explore and Challenge Scratch GPIO: Pi-Stop First Steps**](ExploreScratchGPIO-PiStopTrafficSequence.md)) we will use a **forever** block to repeat our sequence.

<img src="img/foreverblock.png" height=60/>

We will also add a **when green flag clicked** block to kick off our sequence (allowing you to use the small flag in the top right to **start**, and the red circle to **stop**. 
<img src="img/whenflagclickedblock.png" height=60/>

For our traffic lights we want them to start by changing to **GO** (by broadcasting "GO") then wait for some time (for example 10 seconds) and then change to **STOP** (by broadcasting "STOP").

Putting the blocks together we end up with:
<img src="img/04-trafficloop.png" height=180/>

When you run the program (by clicking on the **Green Flag**) you will see each part is highlighted with a white outline while it runs through the **forever** loop and runs each of the **broadcast** group blocks **GO** and **STOP**.
<img src="img/space.png" height=30/>
<p>
<img style="float:left" src="img/check.png" height=50/> **WORKSHEET:** Tick the checkbox marked **"I've created the Pi-Stop the full Traffic Light Sequence"**
<img src="img/space.png" height=30/>
<p>
Remember to save your completed work by selecting **File** and **Save As...** from the menu.

<img src="img/space.png" height=30/>

###Behold the Changing Lights!###
<img src="img/pi-StopR.png" width=50/>
<img src="img/pi-StopRY.png" width=50/>
<img src="img/pi-StopG.png" width=50/>
<img src="img/space.png" height=30/>
<img src="img/pi-StopG.png" width=50/>
<img src="img/pi-StopY.png" width=50/>
<img src="img/pi-StopR.png" width=50/>

##Try your own projects...##
Now you have your very own traffic light you can use in your own projects!

*Below are some ideas, or you can move onto the next guide:*

[**Explore and Challenge Scratch GPIO: Pi-Stop Reaction Game**](ExploreScratchGPIO-PiStopReactionGame.md).


###Start a race###
<img style="float:left" src="img/idea.png" height=50/> **IDEA:** Fed up with unfair starts when starting a race?  Why not start your races with your own starting lights!

Use the Pi-Stop to start your **Scalextric** (TM) or **Hot Wheels** (TM) races, ensuring everyone gets a fair chance.

<img style="float:left" src="img/quest.png" height=50/>**QUESTION:** Can you create a Formula 1 style starting lights (where each light lights up and they all go off, the race starts when the lights are off).

<img style="float:left" src="img/quest.png" height=50/>**QUESTION:** Can you change the program to make the light change with a random wait time (making it harder to go before they change)?

*Hint: See the next guide ([**Explore and Challenge Scratch GPIO: Pi-Stop Reaction Game**](ExploreScratchGPIO-PiStopReactionGame.md)) which makes use of random delays.*

<p>
<img style="float:left" src="img/check.png" height=50/> **WORKSHEET:** Tick the checkbox marked **"Extended Task: Created a racing start light control"**
<p>
<img src="img/space.png" height=20/>


###Control multiple Traffic Lights###
<img style="float:left" src="img/idea.png" height=50/> **IDEA:** Perhaps your **LEGO City** (TM) needs some traffic control.
<img src="img/legotrafficcontrol.jpg" height=200/>
<p>
<img style="float:left" src="img/quest.png" height=50/>**QUESTION:** Can you extend the traffic light sequence to use a second **Pi-Stop** fitted in **Location B** so you can control traffic at a junction?
<img src="img/PiStopLocationB.png" height=300/>

<img src="img/space.png" height=30/>
*If you want to try this, please ask for an extra Pi-Stop to use in your project.*

<img src="img/junction.png" height=300/>
*Hint: You will need to create new **broadcast** blocks using the 2nd set of pins. Also, think about giving drivers time to react before the other set of lights turns GREEN!*

<p>
<img style="float:left" src="img/check.png" height=50/> **WORKSHEET:** Tick the checkbox marked **"Extended Task: Controlled two Pi-Stops at the same time!"**

*The next guide is:*

[**Explore and Challenge Scratch GPIO: Pi-Stop Reaction Game**](ExploreScratchGPIO-PiStopReactionGame.md).

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


<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/pihwlogotm.png" width=180 />

----------
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/Y.png" width=1000 height=50 />

#Explore and Challenge:#
##The Pi-Stop First Steps##
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/LogoDesignNormal.png" height=100/>
> <img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/note.png" height=40/>
> **SEE ALSO:**
> 

> <a href="http://pihw.wordpress.com/lessons/pi-stop-workshops/Discover-PiStop.html">**Discover: The Pi-Stop**</a>: For more information about Pi-Stop and how to use it.
>
> <a href="http://pihw.wordpress.com/lessons/pi-stop-workshops/Setup-ScratchGPIO.html">**Setup: Scratch GPIO**</a>: For instructions on how to setup Scratch GPIO with Pi-Stop *(which is needed for this guide)*.

We shall take our first steps using Scratch GPIO to control the Pi-Stop's LEDs.

###Getting Started###
The Pi-Stop should be connected to the Raspberry Pi in **Location A** (LEDs facing outwards), as follows:

**Location A for Model A+, B+ or Raspberry Pi 2 (purchased after July 2014)**
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/PiStopLocationPlusA.png" height=320 />
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/pi-stopsmbl.png" height=300 />
> <img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/idea.png" height=40/>
> **TIP:** To find **Pi-Stop Location A** on the 40 pin GPIO header, ensure you count 7 pins directly up from the bottom (that will leave 7 unconnected pins below the Pi-Stop).
> 
> Your Pi-Stop should be facing towards the nearest side of the Raspberry Pi and inserted on the row of pins nearest the edge.
> 
> If you are unsure then please ask!

<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/space.png" height=80/>
**Location A for Model A or B (purchased before July 2014)**
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/PiStopLocationA.png" height=300 />
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/pi-stopsmbl.png" height=300 />

###Run Scratch GPIO###
If you are still in the Raspberry Pi terminal, start the desktop environment using:

`startx
`

Open Scratch GPIO from the desktop using the Scratch GPIO icon (we do not need the *ScratchGPIO 7 Plus*):
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/ScratchGPIO7IconOnly.png" height=80/>


**Scratch GPIO 7** is the standard version, while **Scratch GPIO 7 plus** provides additional support for several add-on boards.

> <img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/note.png" height=40/>
> **NOTE:** If you are using **X-Forwarding**, you can run Scratch GPIO with the following commands:
>
    sudo cp ~/.Xauthority ~root/
    sudo /opt/scratchgpio7/./scratchgpio7.sh

###The Scratch Interface###
When Scratch GPIO starts it will look similar to the following:

<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/ScratchGPIOStartSmall.png" height=300>

This is just the same as the normal Scratch interface - the only difference is the hidden background GPIO handler started at the same time (and the message window).

The first thing you will find is a small window with the message `"Remote sensor connections enabled"`.  This indicates that the GPIO handler (the part which is listening for the **broadcast** commands from Scratch is active and ready.

You can press **OK** to clear this message.

><img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/warn.png" height=40/> **WARNING:** If for some reason this doesn't show, check you clicked on **ScratchGPIO 7** rather than the normal **Scratch** icon.
>
>Otherwise, try **rebooting** (terminal command `sudo reboot`) just in case something you ran previously hasn't released the GPIO for example.  Finally, you can try re-installing Scratch GPIO by re-running the install scripts.

Next you will see the standard Scratch interface which is split into three main sections (left to right):

####1 - *Command Blocks Section*####
This is where you select the various types of blocks you can use to make your scripts from.  The blocks are organised into 8 different types depending on their function/use.  When you wish to use a block, simply drag and drop them over into the space to the right.

####2 - *Program Script Area*####
This is where you build your scripts by locking various blocks together.  If you double click on a block (group of blocks) it will run immediately, otherwise they will run according to events which are triggered (from key presses, the actions by the sprite/in the canvas or using the **green flag** icon and block).

> <img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/idea.png" height=40/>
> **TIP:** Each sprite (the default is our friend *Scratch*) can contain their own set of scripts (so if you create extra sprites your scripts will only appear in the one you first built them in).

####3 - *Canvas and Sprites*####
The Canvas area is typically where things happen in the Scratch world.  Usually we interact with the sprites (such as Scratchy) or draw things on the Canvas to see the results from our script.

However since we are also making things happen in the **real world** by using the GPIO pins we don't have to use the canvas to see something happen, the results of our script will be produced by the Pi-Stop instead.  

<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/check.png" height=50/> **WORKSHEET:** Tick the checkbox marked **"I now know the different parts of Scatch"**

*Lets now introduce the blocks we will use in our first example.* 

###The broadcast block###
The **broadcast** block, is located in the **control** section:
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/ScratchControl.png" height=100/>
You may have already come across the **broadcast** block previously while setting up **Scratch GPIO**.  This block simply announces a message to anything which is listening.
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/broadcastpin.png" height=30/>

In this case, `pin26on` is a message which **GPIO Scratch** understands, and will cause **Pin 26** of the GPIO header to switch **on** which will light up the Red light of the **Pi-Stop**.

By default **Scratch GPIO** will start with two **broadcast** blocks, `pin26on` and `pin26off`.

If they are not, you can add your own using the following steps:

1. Select the **control** section in the top-left of the Scratch window.
2. Drag over a **broadcast** block and click on the text space and add a *"new..."* message.
3. Type in `pin26on` for the first, and `pin26off` for the second.
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/gpiotest.png" height=30/>

###The wait block###
Next we will take a wait block, again from the **control** section.
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/wait1sec.png" height=35/>
1. Select the **control** section in the top-left of the Scratch window.
2. Drag over two **wait** blocks.
3. Form together the four blocks into the following shape.
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/flashredled.png" height=100/>

You can test the block by clicking on it, you should see the Red LED of the Pi-Stop switch on for 1 second and then go off automatically.
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/pi-StopR-F.png" height=200/>


###The forever block###
The final block in this section, is called a **forever** block, this will cause anything it contains to repeat over and over for...well...forever!

<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/foreverblock.png" height=60/>

1. Select the **control** section in the top-left of the Scratch window.
2. Drag over a forever block.
3. Move the group of **broadcast** and **wait** into the middle of the **forever** block, you will find that it clicks into place to make the following block.

<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/02-ledtest.png" height=140/>

When you test it this time, by clicking on it, you will find the flashing LED sequence continues to repeat over and over.

<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/check.png" height=50/> **WORKSHEET:** Tick the checkbox marked **"Scratch GPIO with a Flashing RED Light Completed!"**
<img style="float:left" src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/idea.png" height=40/>
Remember to save your completed work by selecting **File** and **Save As...** from the menu.

*Congratulations you have created your first Scratch GPIO program with the Pi-Stop!*

*You are now ready to move onto the next guide:*

<a href="http://pihw.wordpress.com/lessons/pi-stop-workshops/ExploreScratchGPIO-PiStopTrafficSequence.html">**Explore and Challenge Scratch GPIO: Pi-Stop Traffic Sequence**</a>



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

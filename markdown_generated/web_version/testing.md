
<!-- File generated from pihw.com (_inc\web_version\start.txt) -->
##Pi-Stop Resource Files##
These Pi-Stop resource are available as fully customisable [Markdown documents](https://github.com/PiHw/Pi-Stop/tree/master/markdown_source) on the [Pi-Stop github](https://github.com/PiHw/Pi-Stop) page.

Each of the guides are also available in [PDF format](https://github.com/PiHw/Pi-Stop/tree/master/pdf), and in several other automatically [generated variants](https://github.com/PiHw/Pi-Stop/tree/master/markdownmark/down_generated/) (for example, this includes versions which have instructions for the [Model Plus only](https://github.com/PiHw/Pi-Stop/tree/master/markdownmark/down_generated/model_plus_only), or the [original model](https://github.com/PiHw/Pi-Stop/tree/master/markdownmark/down_generated/model_original_only)).


----------

----------
#Test file#
<!-- How to use comments in these files -->
<!-- ---------------------------------- -->
<!--
## This is just an idea at the moment, however this may be a good way to create common worksheets which are adaptable for everyone! ## 

Comments have been put in this file so that they can be customised for a range of workshops and uses.

The convention will be to create a TAG for your purpose and add this to the top of the file with a description.  ## More details will be added when I've experimented further with this concept ##

You can then add comments around any specific sections you need for your workshop and allow others to use the same setups (i.e. if you change to using different hardware you can have alternative sections which describe using that hardware instead of the Pi-Stop).

Once established, we can switch between setups by using a Python Script to generate specific PDFs based on the selected TAGS.

## This is just an idea at the moment, however this may be a good way to create common worksheets which are adaptable for everyone! ## 
-->
#Testing with defines#
<!-- -----------------------------------------------------
-->
<!-- Enable sections for the new model plus (Post-July 2014) define  -->
<!-- Enable sections for the older model (Pre-July 2014)  define  -->
<!-- -----------------------------------------------------
-->

#Testing with WANT_ONLINE_IMG_PATH#


<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/pihwlogotm.png" height=200 />

#Testing with ONLINE_IMG_PATH#

<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/PiStopLocationsPlus.png" height=200 />


#Testing with IMG_PATH#








<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/PiStopLocationsPlus.png" height=200 />

##GPIO Connections for Model A+ and B+##
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/GPIOConnections01Plus.png" height=200 />
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/GPIOConnections02Plus.png" height=200 />



##GPIO Connections for Model A and B##
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/GPIOConnections01.png" height=200 />
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/GPIOConnections02.png" height=200 />

<!--Use the following commandline:-->
<!--  .win-gppgpp.exe -DTEST1 -o ..markdown_generatedtesting#.md output.txt -->


<!--This is a standard comment-->



Keep this text (always defined within the file)


This text is shown if disabled

#Dealing with image references#
We treat image references as a special case, anything with img / will be converted to IMG_ SRC by our TextParser.
We can then define IMG_ SRC to be our webpage path for images:
i.e. https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/
This allows us to define a new path for the images.
<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/markdown/img/pihwlogotm.png" height=200 /> 

Text always here


#Dealing with markdown file references - using find and replace#
> [**Discover: The Pi-Stop**](Discover-PiStop.md): For more information about Pi-Stop and how to use it.




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

<!-- File generated from pihw.com (_inc\both_models\start.txt) -->
<!-- File generated from pihw.com (_inc\standard\start.txt) -->




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


<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/../../markdown_source/markdown/img/pihwlogotm.png" height=200 />

#Testing with ONLINE_IMG_PATH#

<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/../../markdown_source/markdown/img/PiStopLocationsPlus.png" height=200 />


#Testing with IMG_PATH#








<img src="https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img/PiStopLocationsPlus.png" height=200 />

##GPIO Connections for Model A+ and B+##
<img src="../../markdown_source/markdown/img/GPIOConnections01Plus.png" height=200 />
<img src="../../markdown_source/markdown/img/GPIOConnections02Plus.png" height=200 />



##GPIO Connections for Model A and B##
<img src="../../markdown_source/markdown/img/GPIOConnections01.png" height=200 />
<img src="../../markdown_source/markdown/img/GPIOConnections02.png" height=200 />

<!--Use the following commandline:-->
<!--  .win-gppgpp.exe -DTEST1 -o ..markdown_generatedtesting#.md output.txt -->


<!--This is a standard comment-->



Keep this text (always defined within the file)


This text is shown if disabled

#Dealing with image references#
We treat image references as a special case, anything with img / will be converted to IMG_ SRC by our TextParser.
We can then define IMG_ SRC to be our webpage path for images:
i.e. https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/../../markdown_source/markdown/img/
This allows us to define a new path for the images.
<img src="../../markdown_source/markdown/img/pihwlogotm.png" height=200 /> 

Text always here


#Dealing with markdown file references - using find and replace#
> [**Discover: The Pi-Stop**](Discover-PiStop.md): For more information about Pi-Stop and how to use it.



<!-- File generated from pihw.com (_inc\both_models\stop.txt) -->
<!-- File generated from pihw.com (_incstandardstop.txt) -->
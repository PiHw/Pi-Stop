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
#Tesing with defines#

<!--#define WANT_MODEL_PLUS-->
<!--#define WANT_MODEL_ORG-->

<!--#ifdef WANT_MODEL_PLUS-->
##GPIO Connections for Model A+ and B+##
<img style="float:left" src="img/GPIOConnections01Plus.png" height=200 />
<img style="float:right" src="img/GPIOConnections02Plus.png" height=200 />
<!--#endif-->
<!--#ifdef WANT_MODEL_ORG-->
##GPIO Connections for Model A and B##
<img style="float:left" src="img/GPIOConnections01.png" height=200 />
<img style="float:right" src="img/GPIOConnections02.png" height=200 />
<!--#endif-->



#Testing with webtags
<head>
<style>
h1 {color: sienna;}
p {margin-left: 20px;}
body {background-image: url("images/background.gif");}
#showMe{display:none;}
showMe2{display:none;}
showMe3{display:none;}

</style>
</head>


<script language="javascript"> 
function toggle() {
	var ele = document.getElementById("toggleText");
	var text = document.getElementById("displayText");
	if(ele.style.display == "block") {
    		ele.style.display = "none";
		text.innerHTML = "show";
  	}
	else {
		ele.style.display = "block";
		text.innerHTML = "hide";
	}
} 
</script>


<a id="displayText" href="javascript:toggle();">show</a> <== click Here



<div id="toggleText" style="display:showme3">peek-a-boo 1</div>

<showMe3 style="display:none">
##peek-a-boo 2##
</showMe3>

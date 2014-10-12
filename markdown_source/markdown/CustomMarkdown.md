
#Making markdown more powerful#
The whole oncept behind markdown is to keep things as simple as possible, however for the purpoes of our workshop materials we have found it a little limited.

One particular limitation is the lack of ability to allow easy customisation of workshop materials to suit a specific setup (rather than a general one) or for example to be able to switch to using totally different hardware.

By inserting a few additional things into our files we will be able to customise and adjust our workshops to suit out needs and also to generate versions suitable for the website.

However we still want our source files to function normally within a standard Markdown editor.  I believe I now have a workable solution.

##Adding comments##
Various sections of the markdown doument can have additional comments or information which, while useful background for a teacher/instructor, may be too much detail for a student.  By using html comments (indicaed by using <!-- and -->) we are able to provide content which is not normally seen.

The comments are hidden when viewed using a markdown viewer/browser so we can add special notes inside the documents which will not be seen or printed.

##Creating Hidden Tags and Optional Sections##

In addition to comments we will also hide special commands (so-called precompiler directives) which we can use to Enable and Disable specific sections of the text by defining special tags.

Within the files we will use the standard #ifdef, #else and #endif directives to mark various sections of the file to be added or removed from the generated files depending on the #define values used.

We simply hide these special commands within comments so they do not show within the standard editor.  When we generate our files, we can then use a simple text parser to strip out these comments (marked with <!--- and --->).  Finally we use the pre-processor to process this file and generate output files based on the defines we have enabled.

#Configuring our markdown documents#
We shall use the following setup for our workshop files, each file will have:
`<!--- #include define.txt --->`

`<! --- #include start.txt --->`

`Content`

`<! --- #include stop.txt --->`

We can now create a directory with a set of files to include for a particular version of the document:

 - a define.txt to contain all the #define values
 - a start.txt which can contain any additional text we want to include as header content
 - a stop.txt which allows additional content to also be inserted at the end of the file.
 
This allows us to include a different set of include files when we run the preprocessor to generate all the documents.

##Handling images##
One particular problem with generating markdown documents in different folders is that images are referenced relative to the document itself (i.e. img/anImage.png will use the image placed in a subdirectory called img).

Markdown supports referencing of images in directory in the path below (i.e ../img/anImage.png will use an image placed in the img a level below the actual document).  Unfortunately, although github's Markdown preview handles this my current Markdown editor doesn't yet.

Ideally we want all our generated files to reference the same images so that they do not need to be replicated.  This will also include any versions intended for the website.  To avoid the need to create duplicate image references we allow our text parser to detect "img/" and replace it with a suitable reference "IMG_PATH/" and #define IMG_PATH img.

For webpages, we can use:

`#define IMG_PATH https://raw.githubusercontent.com/PiHw/Pi-Stop/master/markdown_source/img`

##Dealing with document references##
Other documents can be referenced in Markdown as follows:

A link to a local document [Discover: The Pi-Stop](Discover-PiStop.md)

A link to a remote document using html links <a href="FILE_SRC/Discover-PiStop.FILE_SRC_EXT">Discover: The Pi-Stop</a>

A link to a remote document using Markdown links [Discover: The Pi-Stop] (FILE_SRC/Discover-PiStop.FILE_SRC_EXT)

**Note:**
These links have to include FILE_SRC and FILE_SRC_EXT so we can #define the full file path (if required) and extension.  To ensure that our source file remains a valid document in our Markdown editor, the alternative remote link should be commented out and enabled/disabled using #ifdef...#else...#endif as follows:

`<!---#ifdef ALT_LINK --->`

`<!---A link to a remote document using html links --->`

`<!---<a href="FILE_SRC/Discover-PiStop.FILE_SRC_EXT">Discover: The Pi-Stop</a> --->`

`<!---#else --->`

`A link to a local document`

`[Discover: The Pi-Stop](Discover-PiStop.md)`

`<!---#endif --->`

Which will produce the following in the standard editor:

> A link to a local document [Discover: The Pi-Stop](Discover-PiStop.md)

With `#define ALT_LINK`:

> A link to a remote document using html links
<a href="FILE_SRC/Discover-PiStop.FILE_SRC_EXT">Discover: The Pi-Stop</a>

The file target can be location can then be defined using:

`#define FILE_SRC`

`#define FILE_SRC_EXT`

For the github site:

`#define FILE_SRC https://github.com/PiHw/Pi-Stop/tree/master/markdown_source/markdown`
`#define FILE_SRC_EXT md`

Or the pdf:

`#define FILE_SRC https://github.com/PiHw/Pi-Stop/blob/master/pdf`
`#define FILE_SRC_EXT pdf?raw=true`

Or on a website:

`#define FILE_SRC http://pihw.wordpress.com/lessons/pi-stop-workshops/`
`#define FILE_SRC_EXT html`

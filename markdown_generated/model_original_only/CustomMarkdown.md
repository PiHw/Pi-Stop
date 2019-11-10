
#Making markdown more powerful#
The whole concept behind markdown is to keep things as simple as possible, however for the purposes of our workshop materials we have found it a little limited.

One particular limitation is the lack of ability to allow easy customisation of workshop materials to suit a specific setup (rather than a general one) or for example to be able to switch to using totally different hardware.

By inserting a few additional things into our files we will be able to customise and adjust our workshops to suit out needs and also to generate versions suitable for the website.

However we still want our source files to function normally within a standard Markdown editor.  I believe I now have a workable solution.

##Adding comments##
Various sections of the markdown doument can have additional comments or information which, while useful background for a teacher/instructor, may be too much detail for a student.  By using html comments (indicaed by using <!-- and -->) we are able to provide content which is not normally seen.

The comments are hidden when viewed using a markdown viewer/browser so we can add special notes inside the documents which will not be seen or printed.

##Creating Hidden Tags and Optional Sections##

In addition to comments we will also hide special commands (so-called precompiler directives) which we can use to Enable and Disable specific sections of the text by defining special tags.

Within the files we will use the standard #ifdef, 
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](http://doctoc.herokuapp.com/)*

- [Things I might need in a pinch but forgot](#things-i-might-need-in-a-pinch-but-forgot)
    - [LD_DEBUG env variable](#ld_debug-env-variable)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

#Things I might need in a pinch but forgot



###LD_DEBUG env variable
urls: 
- http://www.bnikolic.co.uk/blog/linux-ld-debug.html
- http://www.shrubbery.net/solaris9ab/SUNWdev/LLM/p17.html

ex:

  LD_DEBUG=help cat
  Valid options for the LD_DEBUG environment variable are:

    libs        display library search paths
    reloc       display relocation processing
    files       display progress for input file
    symbols     display symbol table processing
    bindings    display information about symbol binding
    versions    display version dependencies
    all         all previous options combined
    statistics  display relocation statistics
    unused      determined unused DSOs
    help        display this help message and exit

  To direct the debugging output into a file instead of standard output
  a filename can be specified using the LD_DEBUG_OUTPUT environment



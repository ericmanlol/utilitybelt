<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](http://doctoc.herokuapp.com/)*

- [Cool things to implement](#cool-things-to-implement)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

#Cool things to implement

1. vim syntax highlighting with less

url: http://www.bit-integrity.com/2011/08/vim-syntax-highlighting-with-less.html 


  VLESS=$(find /usr/share/vim -name 'less.sh')
  if [ ! -z $VLESS ]; then
    alias less=$VLESS
    fi


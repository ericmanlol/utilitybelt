#Cool things to implement

1. vim syntax highlighting with less

url: http://www.bit-integrity.com/2011/08/vim-syntax-highlighting-with-less.html 


  VLESS=$(find /usr/share/vim -name 'less.sh')
  if [ ! -z $VLESS ]; then
    alias less=$VLESS
    fi


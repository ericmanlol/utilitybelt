<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  

- [Personal One Liners](#personal-one-liners)
  - [Fonts](#fonts)
      - [enumerate colors supported by terminals](#enumerate-colors-supported-by-terminals)
      - [enumerate terminal capabilities](#enumerate-terminal-capabilities)
  - [Photos](#photos)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

#Personal One Liners

## Fonts

####enumerate colors supported by terminals

  for T in `find /usr/share/terminfo -type f -printf '%f '`;do echo "$T `tput -T $T colors`";done|sort -nk2


####enumerate terminal capabilities

  infocmp -1 | sed -nu 's/^[ \000\t]*//;s/[ \000\t]*$//;/[^ \t\000]\{1,\}/!d;/acsc/d;s/=.*,//p'|column -c80



## Photos

find . -type f -name '*.jpg' | while read filename; do mv -v "${filename}" "`echo "${filename}" | sed -e 's/_[0-9][x0-9]*//g'`"; done


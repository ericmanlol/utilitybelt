#Personal One Liners

## Fonts

####enumerate colors supported by terminals

  for T in `find /usr/share/terminfo -type f -printf '%f '`;do echo "$T `tput -T $T colors`";done|sort -nk2


####enumerate terminal capabilities

  infocmp -1 | sed -nu 's/^[ \000\t]*//;s/[ \000\t]*$//;/[^ \t\000]\{1,\}/!d;/acsc/d;s/=.*,//p'|column -c80



## Photos

find . -type f -name '*.jpg' | while read filename; do mv -v "${filename}" "`echo "${filename}" | sed -e 's/_[0-9][x0-9]*//g'`"; done


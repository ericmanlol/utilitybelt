<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  

- [AWK & SED](#awk-&-sed)
  - [Basic awk & sed](#basic-awk-&-sed)
    - [AWK](#awk)
    - [SED](#sed)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

#AWK & SED

## Basic awk & sed

###AWK
Extract fields 2, 4, and 5 from file.txt:

    awk '{print $2,$4,$5}' input.txt 


Print each line where the 5th field is equal to ‘abc123’:

    awk '$5 == "abc123"' file.txt


Print each line where the 5th field is *not* equal to ‘abc123’:

    awk '$5 != "abc123"' file.txt


Print each line whose 7th field matches the regular expression:

    awk '$7  ~ /^[a-f]/' file.txt


Print each line whose 7th field *does not* match the regular expression:

    awk '$7 !~ /^[a-f]/' file.txt


Get unique entries in file.txt based on column 1 (takes only the first instance):

    awk '!arr[$2]++' file.txt


Print rows where column 3 is larger than column 5 in file.txt:

    awk '$3>$5' file.txt


Sum column 1 of file.txt:

    awk '{sum+=$1} END {print sum}' file.txt


Compute the mean of column 2: 

    awk '{x+=$2}END{print x/NR}' file.txt




###SED
Number each line in file.txt:

    sed = file.txt | sed 'N;s/\n/ /'


Replace all occurances of `foo` with `bar` in file.txt:

    sed 's/foo/bar/g' file.txt


Trim leading whitespace in file.txt:

    sed 's/^[ \t]*//' file.txt


Trim trailing whitespace in file.txt:

    sed 's/[ \t]*$//' file.txt


Trim leading and trailing whitespace in file.txt:

    sed 's/^[ \t]*//;s/[ \t]*$//' file.txt


Delete blank lines in file.txt:

    sed '/^$/d' file.txt

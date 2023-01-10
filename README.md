# sub2par

This program removes subtitle data such as timestamps and markup tags from a VTT file and turns the caption into one clean paragraph. The output can be saved to a file and piped to xsel or xclip.

Usage:

```sh
$ ./sub2par.py -i "avttfile.vtt" -p | xclip -sel clipboard
```

```sh
$ ./sub2par.py -i "avttfile.vtt" -o "paragraph.txt"
```

#!/usr/bin/env python3

from collections import OrderedDict
import argparse
import re


def main():

    parser = argparse.ArgumentParser(
        prog='sub2post',
        description='Convert VTT subs to a big paragraph'
    )

    parser.add_argument('-i', '--input', type=str, nargs=1, required=True,
                        help='VTT file')
    parser.add_argument('-o', '--output', type=str, nargs=1,
                        help='File in which to save the paragraph')
    parser.add_argument('-p', '--print', action="store_true",
                        help='Send the paragraph to stdout to e.g. pipe to xclip.')

    args = parser.parse_args()

    with open(args.input[0], 'r', encoding='utf-8') as sub:

        lines = sub.readlines()

        # Filter newlines
        filt = filter(lambda text: text != '\n', lines)
        filt = filter(lambda text: text != ' \n', filt)

        # Filter timestamp lines
        filt = filter(lambda text: not re.match(r"^\d\d:\d\d:\d\d.\d\d\d --> \d\d:\d\d:\d\d.\d\d\d", text), filt)

        # Filter timestamps within caption lines
        filt = map(lambda t: re.sub(r"<\d\d:\d\d:\d\d.\d\d\d>", "", t), filt)

        # Replace <c>, </c>, and double whitespaces within caption lines
        filt = map(lambda t: t.replace("<c>", ""), filt)
        filt = map(lambda t: t.replace("</c>", ""), filt)
        filt = map(lambda t: t.replace("\n", ""), filt)
        filt = map(lambda t: t.replace("  ", " "), filt)

        # Remove duplicate lines and metadata and join all strings in the list
        filt = ' '.join(list(OrderedDict.fromkeys(filt))[3:])

    if args.output:
        with open(args.output[0], 'w', encoding='utf-8') as post:
            post.write(filt)

    if args.print:
        print(filt)


if __name__ == '__main__':
    main()

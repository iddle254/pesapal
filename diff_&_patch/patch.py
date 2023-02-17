#!/usr/bin/python3
import errno


def patch(file, diff):
    """

       :param file1: first file
       :param file2: second file
       :return: differences is a list of tuples representing the differences between file1 and file2
               Each tuple has a format of (flag, line) where flag is either '+' or '-'
               representing an addition or a deletion and line is the corresponding line in the file.

        :test patch_output == stoic_tester.txt
              # python diff.py stoic_tester.txt patch_output.txt == []
           """
    try:
        with open(file, "r") as f, open(diff, "r") as d:
            lines = f.readlines()
            diff = d.readlines()
            n = len(lines)
            m = len(diff)
            patch_output = []
            i, j = 0, 0
            while i < n and j < m:
                if diff[j].startswith("-"):
                    j += 1
                elif diff[j].startswith("+"):
                    patch_output.append(diff[j][1:])
                    j += 1
                else:
                    patch_output.append(lines[i])
                    i += 1
            while i < n:
                patch_output.append(lines[i])
                i += 1
            while j < m:
                if diff[j].startswith("+"):
                    patch_output.append(diff[j][1:])
                j += 1
    except IOError as e:
        if e.errno == errno.EACCES:
            print("Error accessing file contents")
            raise e
        elif e.errno == errno.ENOENT:
            print("Please check on the file paths for one or more of the files specified")
            raise e
    return patch_output

if __name__ == "__main__":
    import sys

    """IN TERMINAL RUN"""
    # python patch.py stoic_tester2.txt differences.txt
    file, diff = sys.argv[1], sys.argv[2]
    result = patch(file, diff)
    for line in result:
        print(line, end="")

#!/usr/bin/python3
import errno


def diff(file1, file2):
    """

    :param file1: first file
    :param file2: second file
    :return: differences is a list of tuples representing the differences between file1 and file2
            Each tuple has a format of (flag, line) where flag is either '+' or '-'
            representing an addition or a deletion and line is the corresponding line in the file.

        """
    try:
        with open(file1, "r") as f1, open(file2, "r") as f2:

            f1_contents = f1.readlines()
            # print(f"f1_contents >> {f1_contents}")
            f2_contents = f2.readlines()
            # print(f"f2_contents >> {f2_contents}")
            x = len(f1_contents)
            y = len(f2_contents)
            differences = []
            i, j = 0, 0
            while i < x and j < y:
                """compare the lines in f1 and f2"""
                if f1_contents[i] != f2_contents[j]:
                    differences.append(f"-{f1_contents[i]}")
                    differences.append(f"+{f2_contents[j]}")
                    i += 1
                    j += 1
                else:
                    differences.append(f" {f1_contents[i]}")
                    i += 1
                    j += 1
            while i < x:
                differences.append(f"-{f1_contents[i]}")
                i += 1
            while j < y:
                differences.append(f"+{f2_contents[j]}")
                j += 1
        # print(f"differences >> {differences}")
    except IOError as e:
        if e.errno == errno.EACCES:
            print("Error accessing file contents")
            raise e
        elif e.errno == errno.ENOENT:
            print("Please check on the file paths for one or more of the files specified")
            raise e

    return differences


if __name__ == "__main__":
    import sys

    """IN TERMINAL RUN"""
    # python diff.py stoic_tester.txt stoic_tester2.txt
    file1, file2 = sys.argv[1], sys.argv[2]
    result = diff(file1, file2)
    # print(result)
    for line in result:
        if line[0] == '+':
            print(line)
        elif line[0] == '-':
            print(line)
        else:
            pass


import argparse


def fix_config_file(line):
    if (line.count('=') == 2) & ('==' not in line):
        ll = '='.join(line.split('=')[:-1])
        if not ll.endswith('\n'):
            ll = ll + '\n'
        return ll
    else:
        return line


def main():
    """
    Main function
    """

    parser = argparse.ArgumentParser(description='Parse arguments.')

    parser.add_argument('infile', type=str,
                        help='input environment file')

    parser.add_argument('outfile', type=str,
                        help='output environment file')

    args = parser.parse_args()

    with open(args.infile) as f:
        lines = f.readlines()
        new_lines = [fix_config_file(line) for line in lines]

    with open(args.outfile, 'w') as dst:
        dst.writelines(new_lines)


if __name__ == "__main__":
    main()

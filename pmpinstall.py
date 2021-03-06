import sys
import getopt
from ProcessProduct import ProcessProduct
from ProcessPCF import ProcessPCF

help_str = '''

Please supply the arguments for -s, -p and -a
        -s, --source - source path to the PolicyCenter configuration directory e.g .../PolicyCenter/modules/configuration
        -p, --products - comma separated list of lines, this is a list of the code identifiers for the line(s) e.g CPLine,IMLine
        -a, --abbreviations - comma separated list of product abbreviations, the abbreviations correspond to the sub folder 
        under the pcf lob directory e.g. ba,cp
        -l, --location - location where the code is generated e.g. ext.lob
        -m, --model - process only the product model

        -h, --help - displays this text

        '''


def main(argv):
    pc_path = ''
    pc_product_line = ''
    pc_product_abbreviations = ''
    pc_product_location = ''
    pc_product_only = ''

    try:
        opts, args = getopt.getopt(argv, 'hs:p:a:l:m:', ['help', 'source =', 'products =', 'abbreviations =', 'location =', 'model ='])
    except getopt.GetoptError:
        print(help_str)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ['-s', '--source']:
            pc_path = arg
        elif opt in ['-p', '--products']:
            pc_product_line = arg
        elif opt in ['-a', '--abbreviations']:
            pc_product_abbreviations = arg
        elif opt in ['-l', '--location']:
            pc_product_location = arg
        elif opt in ['-m', '--model']:
            pc_product_only = arg
        elif opt in ['-h', '--help']:
            print(help_str)
            sys.exit()
        else:
            sys.exit()

    if pc_path == '':
        print("-s (--source) missing and is required")
        print(help_str)
        sys.exit()

    if pc_product_line == '':
        print("-p (--product) is  missing and is required")
        print(help_str)
        sys.exit()

    if pc_product_abbreviations == '':
        print("-a (--abbreviations) is  missing and is required")
        print(help_str)
        sys.exit()

    if pc_product_location == '':
        print("-l (--location) is  missing and will default to ext.lob")
        pc_product_location = 'ext.lob'

    if pc_product_only == '':
        pc_product_only = 'false'

    if pc_product_only != 'true' and pc_product_only != 'false':
        print("-m (--model) must be 'true' or 'false' ")
        sys.exit()

    print(f'pc_path : {pc_path}')
    print(f'pc_product_line : {pc_product_line}')
    print(f'pc_product_abbreviations : {pc_product_abbreviations}')
    print(f'pc_product_location : {pc_product_location}')
    print(f'pc_product_only : {pc_product_only}')

    if pc_product_line != '':
        for line in pc_product_line.split(','):
            pass
            product_process = ProcessProduct(pc_path, line)
            product_process.process_clause_patterns()

    if pc_product_abbreviations != '' and pc_product_only == 'false':
        for abbreviation in pc_product_abbreviations.split(','):
            product_process = ProcessPCF(pc_path, abbreviation)
            product_process.process_pcf()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(help_str)
        sys.exit()
    main(sys.argv[1:])

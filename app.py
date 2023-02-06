import os
import sys
import argparse
from loren_txt import lorem

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description="File with lines generator")
        parser.add_argument('--lines_number', '-n', required=True, type=int, help="number of lines will be generator")
        args   = parser.parse_args()
        
        paragraph_length = args.lines_number
        paragraph  = lorem.paragraphs(paragraphs_length)
        
        with open(os.path.join('.', 'file_with_lines.txt), 'w') as f:
            f.write(paragraph)
            
            
    except Exception as exc:
        print(f"There was an unepected behavior from user side, Error : '{exc}'")
        sys.exit(1)
    
    sys.exit(0)

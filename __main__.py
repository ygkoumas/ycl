import sys

import parser
import executor

with open(sys.argv[1], 'r') as f:
    source = f.read()

parsed_source = parser.parse(source)
executor.run(parsed_source)

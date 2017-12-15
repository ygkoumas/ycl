GLOBAL_PROCS = {}
GLOBAL_VARS = {}

# Foreach tcl command there is a function which executes it.
# Function name format is: c_<tcl_command_name>
def c_proc(code_line):
    "NOT FINISHED"
    GLOBAL_PROCS[code_line[1]] = "python equivalent of " + code_line[2]

def c_set (code_line):
    GLOBAL_VARS[code_line[1]] = tcl_execute(code_line[2])
GLOBAL_PROCS['set'] = c_set

def c_puts (code_line):
    print tcl_execute(code_line[1])
GLOBAL_PROCS['puts'] = c_puts

def tcl_execute(code):
    if code[0] == '$':
        return GLOBAL_VARS[code[1:]]
    return code

def run(parsed_source):
    for l in parsed_source:
        GLOBAL_PROCS[l[0]](l)

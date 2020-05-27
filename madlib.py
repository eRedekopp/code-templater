#!/bin/python3
import sys
import re

VARSTRING = "<VAR>"  # The string we use to indicate variables in the template

def print_help():
    print("Usage:")
    print("{} TEMPLATE_FILE ARG_FILE".format(sys.argv[0]))
    exit(1)


def fill_madlib(template, args):
    """
    Given a template and the correct number of args for that template, fill it in
    and return the result as a string
    """
    out = template
    argcount = 0
    match = re.search(VARSTRING, out)
    while match is not None:
        assert argcount < len(args)
        out = out[0 : match.start(0)] + args[argcount] + out[match.end(0) : ]
        match = re.search(VARSTRING, out)
        argcount += 1
    out = out + '\n'
    assert argcount == len(args)
    return out
    
    
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print_help()
    template_filename = sys.argv[1]
    arg_filename = sys.argv[2]

    # Get the template as a string
    with open(template_filename, 'r') as template_file:
        template = template_file.read();

    # Get the args as a list of strings
    with open(arg_filename, 'r') as arg_file:
        args = []
        for line in arg_file:
            args.append(line.rstrip('\n'))

    # Make sure there are the right number of args
    num_template_vars = len(re.findall(VARSTRING, template))
    num_arg_vars = len(args)
    if num_arg_vars % num_template_vars != 0:
        print("{} Error: Found {} args in file ({}) but expected {}"
              .format(sys.argv[0], num_arg_vars, arg_filename,
                      num_arg_vars + num_arg_vars % num_template_vars))
        exit(1)

    # Fill in and print the madlib as many times as we need to
    for i in range(num_arg_vars // num_template_vars):
        print(fill_madlib(template, args[i * num_template_vars : (i+1) * num_template_vars]))

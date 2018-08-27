# -*- coding: utf-8 -*-
"""
Spyder Editor

N = set of nonterminal symbols
S = set of terminal symbols
P = set of parsing rules
e_s = starting expression

A parsing grammar PEG
PEG = (N, S, P, e_s)

Each Parsing rule p in P has the form: A <- e,
where A is a nonterminal symbol (A in N).
A parsing expression is a hierarchical expression similar to a regular expression,
which is constructed in the following fashion

1. (n, )
"""

import ast


if __name__ == "__main__":
    node = ast.Expression( ast.BinOp(ast.Str('xy'),
                                     ast.Mult(),
                                     ast.Num(3)))

    fixed = ast.fix_missing_locations(node)
    
    codeobj = compile(fixed, '<string>', 'eval')
    print (eval(codeobj))
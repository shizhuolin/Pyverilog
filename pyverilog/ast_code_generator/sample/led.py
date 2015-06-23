import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))) )

import pyverilog.vparser.ast as vast
from pyverilog.ast_code_generator.codegen import ASTCodeGenerator

params = vast.Paramlist(())
clk = vast.Ioport( vast.Input('CLK') )
rst = vast.Ioport( vast.Input('RST') )
width = vast.Width( vast.IntConst('7'), vast.IntConst('0') )
led = vast.Ioport( vast.Output('led', width=width) )
ports = vast.Portlist( (clk, rst, led) )
items = ( vast.Assign( vast.Identifier('led'), vast.IntConst('8') ) ,)
ast = vast.ModuleDef("top", params, ports, items)

codegen = ASTCodeGenerator()
rslt = codegen.visit(ast)
print(rslt)
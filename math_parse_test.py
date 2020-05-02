from simpleeval import simple_eval
import ast
import operator



def SimpleEval(x):
    return simple_eval(x)

s = SimpleEval()
s.operators[ast.BitXor] = operator.xor


print(simple_eval('21/4*3'))
print(simple_eval('234**3'))
print(s.eval('2^2'))
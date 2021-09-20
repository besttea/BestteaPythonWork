'''
Author: your name
Date: 2021-09-20 11:56:44
LastEditTime: 2021-09-20 13:34:59
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \0001\自动绘制流程图.py
'''
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

with PyCallGraph(output=GraphvizOutput()):
    # 需要绘制流程图的代码，可以是函数
    # ... ...

# ...省略大部分代码...
if __name__ == '__main__':
    from pycallgraph import PyCallGraph
    from pycallgraph.output import GraphvizOutput

    with PyCallGraph(output=GraphvizOutput()):
        main()
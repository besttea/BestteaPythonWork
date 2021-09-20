'''
Author: your name
Date: 2021-09-20 11:00:30
LastEditTime: 2021-09-20 11:42:08
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \0001\流程图.py
'''
import yaml
import os
import ibm_db
from graphviz import Digraph
from datetime import datetime
# db连接
def db2_query(sql): 
    conn = ibm_db.connect(
    "DATABASE=%s;HOSTNAME=%s;PORT=%s;PROTOCOL=TCPIP;UID=%s;PWD=%s" % (
        config['db2_databse'],
        config['db2_host'],
        config['db2_port'],
        config['db2_user'],
        config['db2_password'            ]
        )
    ,"","") 
    if conn:  # 执行
        stmt = ibm_db.exec_immediate(conn, sql) 
        result = ibm_db.fetch_both(stmt) 
    return result,stmt,conn
# 添加所有的点
def add_nodes(): 
    sql = "SELECT * FROM AML.DEP_OFTEN_TRAD 
        WHERE ACCOUNT_NO=" + ACCOUNT_NO +
        " ORDER BY NUM DESC fetch first 10 rows ONLY;" 
    result,stmt,
    conn = db2_query(sql) 
    nodes = [] 
    nodes_dict = {} 
    nodes_dict[ACCOUNT_NO] = 'A' count = 0 
        while (result): count = count + 1 
    print(chr(ord('A') + count) + "," + result[3]) 
    dot.node(chr(ord('A') + count),result[3],    
             shape="rectangle",
            color="orange") 
    nodes.append(result[2]) 
    nodes_dict[result[2]] = chr(ord('A') + count)
    print('-----------------')
    result = ibm_db.fetch_both(stmt)
# 关闭数据库连接
    ibm_db.close(conn)
    nodes.append(ACCOUNT_NO)
    return dot, nodes, nodes_dict
# 添加所有的边
def add_edges(nodes): 
    nodes_back = nodes 
    print(nodes_back) 
    for p in range(len(nodes_back)): 
        nodes_temp = nodes.copy() 
        from_nodes = nodes_temp.pop(p) 
        print(  "len of nodes_temp:" + str(len(nodes_temp)) + ",from_nodes:" + from_nodes
            ) 
        nodes_temp_in = ",".join(nodes_temp) 
        nodes_temp_in = '(' + nodes_temp_in + ')' 
        sql = "SELECT * FROM AML.DEP_OFTEN_TRAD WHERE ACCOUNT_NO=" + 
            from_nodes + " and CNTPRT_ACCOUNT_NO IN" + \ 
            nodes_temp_in result,stmt,conn = db2_query(sql) 
        if (result): 
            while (result): 
                print('-----------------') 
                print(result) 
                print(result ['CNTPRT_ACCOUNT_NO'] + nodes_dict [result['CNTPRT_ACCOUNT_NO']])
                print("add edges," + result['TRAD_VAL'] + 
                      " from:" + from_nodes + ",to:" + 
                      result ['CNTPRT_ACCOUNT_NO']) 
                dot.edge(nodes_dict [from_nodes],
                         nodes_dict [result['CNTPRT_ACCOUNT_NO']], result['TRAD_VAL']) 
                result = ibm_db.fetch_both(stmt) # 关闭数据库连接
                ibm_db.close(conn) 
    return dot

if __name__ == "__main__":
yaml_path = os.path.join('../', 'config.yaml')
with open(yaml_path, 'r') as f:
config = yaml.load(f)
dot = Digraph(
    engine="circo",
    comment='The Test Table',
    format="png"
)
ACCOUNT_NO = '10100002181'
# 添加圆点A,A的标签是Dot A
dot.node('A', '中心客户', shape="rectangle", color="blue")
nodes_begin = datetime.now()
print(str(nodes_begin) + " nodes_begin")
dot, nodes, nodes_dict = add_nodes()
print(nodes_dict)
edges_begin = datetime.now()
print(str(edges_begin) + " edges_begin")
dot = add_edges(nodes)
print(dot.source)
render_begin = datetime.now()
print(str(render_begin) + " render_begin")
dot.render('./file/db2-table.gv', view=True)

import re
from packages.FileData import FileData


def load(filename):
    try:
        with open(f'{filename}.txt', 'r') as file:
            data = FileData()
            lines = file.readlines()
            nodeTypes = None
            edgeTypes = None
            pattern = "(\w)[ ]?(\=|is)[ ]?(\w+[ ]?\w*)"  # pattern to extract node types and edge types
            for curline in lines:
                curline = curline.strip()
                # load ncode
                if curline.startswith('Ncode'):
                    _, code, weight = curline.split(' ')
                    data.addNcode(code, int(weight))
                # load node
                elif curline.startswith('Node'):
                    _, label, code = curline.split(' ')
                    data.addNode(label, code)
                # load ecode
                elif curline.startswith('Ecode'):
                    _, code, weight = curline.split(' ')
                    data.addEcode(code, int(weight))
                # load edge
                elif curline.startswith('Edge'):
                    _, fromLabel, toLabel, code = curline.split(' ')
                    data.addEdge(fromLabel, toLabel, code)
                # load start
                elif curline.startswith('Start'):
                    _, label = curline.split(' ')
                    data.setStart(label)
                # load end
                elif curline.startswith('Target'):
                    _, label = curline.split(' ')
                    data.setEnd(label)
                # load node types
                elif curline.startswith('# Node types'):
                    types = re.findall(pattern, curline)
                    if types:
                        nodeTypes = types
                # load edge types
                elif curline.startswith('# Edge types'):
                    types = re.findall(pattern, curline)
                    if types:
                        edgeTypes = types

            if nodeTypes:  # if there are match types to pattern above, add to ncode
                for item in nodeTypes:
                    code, _, des = item
                    ncode = data.getNcode(code.strip())
                    if ncode:
                        ncode.setDescription(des.strip())
            if edgeTypes:  # if there are match types to pattern above, add to ecode
                for item in edgeTypes:
                    code, _, des = item
                    ecode = data.getEcode(code.strip())
                    if ecode:
                        ecode.setDescription(des.strip())
        return data
    except FileNotFoundError:
        print('\nFILE DOES NOT EXIST')

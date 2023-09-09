from packages.DSAHashEntry import DSAHashEntryState
from packages.DSALinkedList import DSALinkedList


def generate(data):
    rows = DSALinkedList()
    _generateInfo(rows)
    _generateNodeType(data, rows)
    _generateNodeCode(data, rows)
    _generateNode(data, rows)
    _generateEdgeType(data, rows)
    _generateEdgeCode(data, rows)
    _generateEdge(data, rows)
    _generateStartEnd(data, rows)
    return rows


def _generateInfo(rows):
    rows.insertLast('# comment line that can be ignored')
    rows.insertLast('#')
    rows.insertLast('# File format:')
    rows.insertLast('#')
    rows.insertLast('# Node label code')
    rows.insertLast('# Edge label label code')
    rows.insertLast('# Ncode code weight')
    rows.insertLast('# Ecode code weight')
    rows.insertLast('# Start label')
    rows.insertLast('# Target label')
    rows.insertLast('#')


def _generateNodeType(data, rows):
    row = '# Node types '
    for ncode in data.getNcodes():
        if ncode.getState() == DSAHashEntryState.USED:
            code = ncode.getValue().getCode()
            description = ncode.getValue().getDescription()
            if code != '-' and description:
                row += f'{code} = {description}, '
    if data.getNcode('-'):
        row = row + '- has no impact/empty'
    else:
        row = row.rstrip(', ')  # remove last comma if there is no node type minus
    rows.insertLast(row)


def _generateNodeCode(data, rows):
    for ncode in data.getNcodes():
        if ncode.getState() == DSAHashEntryState.USED:
            code = ncode.getValue().getCode()
            weight = ncode.getValue().getWeight()
            row = f'Ncode {code} {weight}'
            rows.insertLast(row)


def _generateNode(data, rows):
    rows.insertLast('# Define nodes and labels')
    for node in data.getNodes():
        if node.getState() == DSAHashEntryState.USED:
            label = node.getValue().getLabel()
            code = node.getValue().getCode()
            row = f'Node {label} {code}'
            rows.insertLast(row)


def _generateEdgeType(data, rows):
    row = '# Edge types '
    for ecode in data.getEcodes():
        if ecode.getState() == DSAHashEntryState.USED:
            code = ecode.getValue().getCode()
            description = ecode.getValue().getDescription()
            if code != '-':
                if description:
                    row += f'{code} = {description}, '
                else:
                    row += f'{code} = {code} units, '  # if there is no description for edge type, use {code + units} to show as description
    if data.getEcode('-'):
        row = row + '- is a standard 1 unit per edge'
    else:
        row = row.rstrip(', ')  # remove last comma if there is no edge type minus
    rows.insertLast(row)


def _generateEdgeCode(data, rows):
    for ecode in data.getEcodes():
        if ecode.getState() == DSAHashEntryState.USED:
            code = ecode.getValue().getCode()
            weight = ecode.getValue().getWeight()
            row = f'Ecode {code} {weight}'
            rows.insertLast(row)


def _generateEdge(data, rows):
    rows.insertLast('# Define edges')
    for edge in data.getEdges():
        if edge.getState() == DSAHashEntryState.USED:
            fromLabel = edge.getValue().getFrom()
            toLabel = edge.getValue().getTo()
            code = edge.getValue().getCode()
            row = f'Edge {fromLabel} {toLabel} {code}'
            rows.insertLast(row)


def _generateStartEnd(data, rows):
    rows.insertLast('# Define Start and Target(s)')
    rows.insertLast(f'Start {data.getStart()}')
    rows.insertLast(f'Target {data.getEnd()}')

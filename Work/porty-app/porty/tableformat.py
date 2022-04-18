# tableformat.py

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headers
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data
        '''
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for header in headers:
            print(f'{header:>10s}', end=' ')
        print()
        print(('-' * 10 + ' ') * len(headers))
    
    def row(self, rowdata):
        for data in rowdata:
            print(f'{data:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML Table format
    '''
    def open(self):
        print('<table>')

    def headings(self, headers):
        print('  <tr>')
        for header in headers:
            print(f'    <th>{header}</th>')
        print('  </tr>')

    def row(self, rowdata):
        print('  <tr>')
        for data in rowdata:
            print(f'    <td>{data}</td>')
        print('  </tr>')
    
    def close(self):
        print('</table>')

class FormatError(Exception):
    pass

def create_formatter(name):
    '''
    Create an appropriate formatter given an output format name
    '''
    if name == 'txt':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown format {name}')

def print_table(objects, columns, formatter):
    '''
    Make a nicely formatted table from a list of objects and attribute names.
    '''
    formatter.headings(columns)
    for object in objects:
        formatter.row([str(getattr(object, column)) for column in columns])
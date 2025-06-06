# tableformat.py
'''
class which does nothign and provides template is known as abstract class (also in c++)
'''
class TableFormatter:       # is an abstract class
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
    raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
    raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in text fromat
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end= ' ')
        print()
        print(('-'*10 + ' ')*len(headers))
        #return super().headings(headers)
    def row(self,rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end= ' ')
        print()

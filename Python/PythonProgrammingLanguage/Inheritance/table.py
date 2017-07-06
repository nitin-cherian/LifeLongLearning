# table.py
import sys
from abc import ABC, abstractmethod


def print_table(objects, colname, formatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError("formatter must be a TableFormatter")

    # Emits the header
    formatter.heading(colname)

    for obj in objects:
        # Emits the rows
        rowdata = [str(getattr(obj, col)) for col in colname]
        formatter.row(rowdata)


class TableFormatter(ABC):
    # This class serves as a design spec which forces the subclasses to implement the methods.
    def __init__(self, outfile=None):
        if outfile is None:
            outfile = sys.stdout
        self.outfile = outfile

    @abstractmethod
    def heading(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass


class TextTableFormatter(TableFormatter):
    def __init__(self, outfile=None, width=10):
        super().__init__(outfile)
        self.width = width

    def heading(self, headers):
        for header in headers:
            print("{:>{}}".format(header, self.width), end=" ", file=self.outfile)
        print(file=self.outfile)

    def row(self, rowdata):
        for item in rowdata:
            print("{:>{}}".format(item, self.width), end=" ", file=self.outfile)
        print(file=self.outfile)


class HTMLTableFormatter(TableFormatter):
    def heading(self, headers):
        print('<tr>', end="", file=self.outfile)
        for header in headers:
            print("<th>{}</th>".format(header), end="", file=self.outfile)
        print("</tr>", file=self.outfile)

    def row(self, rowdata):
        print('<tr>', end="", file=self.outfile)
        for item in rowdata:
            print("<td>{}</td>".format(item), end="", file=self.outfile)
        print("</tr>", file=self.outfile)


class CSVTableFormatter(TableFormatter):
    def heading(self, headers):
        print(','.join(headers), file=self.outfile)

    def row(self, rowdata):
        print(','.join(rowdata), file=self.outfile)








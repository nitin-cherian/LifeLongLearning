# table.py


def print_table(objects, colname, formatter):
    # Emits the header
    formatter.heading(colname)

    for obj in objects:
        # Emits the rows
        rowdata = [str(getattr(obj, col)) for col in colname]
        formatter.row(rowdata)


class TableFormatter:
    # This class serves as a design spec which forces the subclasses to implement the methods.

    def heading(self, headers):
        raise NotImplementedError

    def row(self, rowdata):
        raise NotImplementedError


class TextTableFormatter(TableFormatter):
    def heading(self, headers):
        for header in headers:
            print("{:>10}".format(header), end=" ")
        print()

    def row(self, rowdata):
        for item in rowdata:
            print("{:>10}".format(item), end=" ")
        print()


class HTMLTableFormatter(TableFormatter):
    def heading(self, headers):
        print('<tr>', end="")
        for header in headers:
            print("<th>{}</th>".format(header), end="")
        print("</tr>")

    def row(self, rowdata):
        print('<tr>', end="")
        for item in rowdata:
            print("<td>{}</td>".format(item), end="")
        print("</tr>")


class CSVTableFormatter(TableFormatter):
    def heading(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))








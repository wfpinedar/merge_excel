import os
import xlwt
import xlrd
import Tkinter, Tkconstants, tkFileDialog

lst = []

def getdir():
    root = Tkinter.Tk()
    path = tkFileDialog.askdirectory(parent=root, initialdir='.')
    return path

def listar_xls(path):
    for file in os.listdir(path):
        if file.endswith(".xls") or file.endswith(".xlsx"):
            lst.append(os.path.join(path, file))
    return lst

wkbk = xlwt.Workbook()

def fusion():
    path = getdir()
    xlsfiles = listar_xls(path)
    outrow_idx = 0
    for f in xlsfiles:
        insheet = xlrd.open_workbook(f).sheets()[0]
        outsheet = wkbk.add_sheet(xlrd.open_workbook(f).sheets()[0].name)
        for row_idx in xrange(insheet.nrows):
            for col_idx in xrange(insheet.ncols):
                outsheet.write(outrow_idx, col_idx,
                insheet.cell_value(row_idx, col_idx))
            outrow_idx += 1
        outrow_idx = 0
    wkbk.save(os.path.join(path, r'combined.xls'))

def __init__():
    fusion()

__init__()
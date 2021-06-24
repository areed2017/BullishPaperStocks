import numpy

from pyqtgraph import PlotWidget, mkPen, AxisItem

from UI.Styles import GRAPH, Colors


class TimeAxisItem(AxisItem):
    def __init__(self, xdict, *args, **kwargs):
        AxisItem.__init__(self, *args, **kwargs)
        self.x_values = numpy.asarray(list(xdict.keys()))
        self.x_strings = list(xdict.values())

    def tickStrings(self, values, scale, spacing):
        strings = []
        for v in values:
            vs = int(v * scale)
            if vs in self.x_values:
                vstr = self.x_strings[numpy.abs(self.x_values - vs).argmin()].replace('T', '-').replace('Z', "")
            else:
                vstr = ""
            strings.append(vstr)
        return strings


class IntraDayClose(PlotWidget):

    def __init__(self, days, close):
        days = dict(enumerate(days))
        super().__init__(axisItems={'bottom': TimeAxisItem(days, orientation='bottom')})

        self.setStyleSheet(GRAPH)
        self.setBackground((0, 0, 0, 1))
        self.getAxis('left').setTextPen(Colors.C4)
        self.getAxis('bottom').setTextPen(Colors.C4)
        self.hideButtons()
        self.setTitle(f"<span style=\"color: {Colors.C4}\">1 Minute Chart</span>")
        self.setMouseEnabled(x=True, y=False)
        self.setAspectLocked(False)
        self.setAutoVisible(y=True)
        self.enableAutoRange(axis='y', enable=True)
        self.plot(list(days.keys()), close, pen=mkPen(Colors.C4, width=3))

        self.setLimits(xMin=1, xMax=len(days.items())+10)
        self.setXRange(len(days.items()) - 7, len(days.items()))

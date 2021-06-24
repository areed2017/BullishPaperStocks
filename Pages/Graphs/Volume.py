import numpy

from pyqtgraph import PlotWidget, mkPen, AxisItem, BarGraphItem

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
                vstr = self.x_strings[numpy.abs(self.x_values - vs).argmin()]
            else:
                vstr = ""
            strings.append(vstr)
        return strings


class Volume(PlotWidget):

    def __init__(self, label, days, volume):
        days = dict(enumerate(days))
        super().__init__(axisItems={'bottom': TimeAxisItem(days, orientation='bottom')})

        self.setStyleSheet(GRAPH)
        self.setMaximumHeight(150)
        self.setBackground((0, 0, 0, 1))
        self.getAxis('left').setTextPen(Colors.C4)
        self.getAxis('bottom').setTextPen(Colors.C4)
        self.hideButtons()
        self.setTitle(f"<span style=\"color: {Colors.C4}\">{label}</span>")
        self.setMouseEnabled(x=True, y=False)
        self.setAspectLocked(False)
        self.setAutoVisible(y=True)
        self.enableAutoRange(axis='y', enable=True)

        volume = BarGraphItem(x=list(days.keys()), width=0.6, height=volume, brush='g')
        self.addItem(volume)

        self.setLimits(xMin=1, xMax=len(days.items())+10, yMin=0)
        self.setXRange(len(days.items()) - 7, len(days.items()))

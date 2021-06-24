from PyQt5.QtGui import QColor, QLinearGradient


class Colors:
    C1 = "#1D2D50"
    C2 = "#133B5C"
    C3 = "#1E5F74"
    C4 = "#FCDAB7"
    SHADOW1 = QColor("#1D2D50").darker(115).name()
    SHADOW2 = QColor("#133B5C").darker(115).name()
    SHADOW3 = QColor("#1E5F74").darker(115).name()
    LIGHT2 = QColor("#133B5C").lighter(115).name()
    LIGHT4 = QColor("#FCDAB7").lighter(115).name()

    GRADIENT_C1 = QLinearGradient(0, 0, 0, 400)


Colors.GRADIENT_C1.setColorAt(0.0, QColor(Colors.C1))
Colors.GRADIENT_C1.setColorAt(1.0, QColor(Colors.C1).lighter(115))

TOP_BAR = f"""
background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                 stop: 0 {Colors.C1}, 
                                 stop: 0.1 {QColor(Colors.C1).lighter(50).name()},
                                 stop: 0.5 {QColor(Colors.C1).lighter(100).name()}, 
                                 stop: 1.0 {QColor(Colors.C1).lighter(115).name()});
border-bottom: 4px solid {Colors.SHADOW1};
"""

# background-color: {Colors.C2};
NAVIGATION = f"""
background-color: {Colors.C2};
padding: 0;
margin: 0;
border-right: 4px solid {Colors.SHADOW2};
"""

# background-color: {Colors.C3};
BODY = f"""
background: qlineargradient(x1: 1, y1: .1, x2: 0, y2: 0,
                                 stop: 0 {Colors.C3}, 
                                 stop: 0.3 {QColor(Colors.C3).darker(50).name()},
                                 stop: 0.8 {QColor(Colors.C3).lighter(100).name()}, 
                                 stop: 1.0 {QColor(Colors.C3).lighter(115).name()});
"""


BUTTON_BORDER = f"""
border-top: 4px solid qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 {Colors.C2},
                                stop: 1 {QColor(Colors.C2).darker(50).name()});
border-bottom: 4px solid qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 {Colors.C2},
                                stop: 1 {QColor(Colors.C2).darker(50).name()});
"""

BUTTON = f"""
border: none;
color: {Colors.C4};
border-right: 4px solid {Colors.SHADOW2};
font-weight: bold;
font-size: 22px;
background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,
                                stop: 0 {QColor(Colors.C2).darker(115).name()},
                                stop: 0.1 {QColor(Colors.C2).lighter(100).name()},
                                stop: 0.2 {QColor(Colors.C2).lighter(155).name()},
                                stop: 0.8 {QColor(Colors.C2).lighter(155).name()},
                                stop: 0.9 {QColor(Colors.C2).lighter(100).name()}, 
                                stop: 1.0 {QColor(Colors.C2).darker(115).name()});
{BUTTON_BORDER}
"""

BUTTON_SELECTED = f"""
border: none;
color: {Colors.C4};
font-weight: bold;
font-size: 26px;
text-decoration: underline;
background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,
                                stop: 0 {QColor(Colors.C2).darker(115).name()},
                                stop: 0.05 {QColor(Colors.C2).lighter(100).name()},
                                stop: 0.1 {QColor(Colors.C2).lighter(155).name()},
                                stop: 0.9 {QColor(Colors.C2).lighter(155).name()},
                                stop: 0.95 {QColor(Colors.C2).lighter(100).name()}, 
                                stop: 1.0 {QColor(Colors.C2).darker(115).name()});
{BUTTON_BORDER}
"""

HEADER = f"""
background: rgba(255, 255, 255, 10);
color: {Colors.C1};
font-size: 26px;
padding: 10px;
font-weight: bold;
border: 2px solid {Colors.C4};
"""

HEADER_2 = f"""
background: rgba(255, 255, 255, 10);
color: {Colors.C1};
font-size: 26px;
padding: 10px;
font-weight: bold;
border: None;
"""


SEARCH_BAR = f"""
border: none;
padding-left: 16px;
padding-right: 16px;
padding-top: 8px;
padding-bottom: 8px;
color: {Colors.C4};
font-size: 22px;
{BUTTON_BORDER}
"""

Refresh_BUTTON = f"""
background: qlineargradient(x1: 1, y1: 0.4, x2: 0, y2: 0,
                                 stop: 0 {QColor('#343d52').name()},
                                 stop: 0.2 {QColor('#343d52').name()},
                                 stop: 0.9 {QColor('#343d52').lighter(155).name()},
                                 stop: 1.0 {QColor('#343d52').name()});
color: {Colors.C4};
font-size: 22px;
"""

BUY_BUTTON = f"""
background: qlineargradient(x1: 1, y1: 0.4, x2: 0, y2: 0,
                                 stop: 0 {QColor('#059142').name()},
                                 stop: 0.2 {QColor('#059142').name()},
                                 stop: 0.9 {QColor('#059142').lighter(155).name()},
                                 stop: 1.0 {QColor('#059142').name()});
color: {Colors.C4};
font-size: 22px;
"""

SELL_BUTTON = f"""
background: qlineargradient(x1: 1, y1: 0.4, x2: 0, y2: 0,
                                 stop: 0 {QColor('#EE0000').name()},
                                 stop: 0.2 {QColor('#EE0000').name()},
                                 stop: 0.9 {QColor('#EE0000').lighter(155).name()},
                                 stop: 1.0 {QColor('#EE0000').name()});
color: {Colors.C4};
font-size: 22px;
"""

PORTFOLIO_CARD = f"""
border: 2px solid {Colors.C4};
border-radius: 5px;
"""

TRANSACTION_CARD = f"""
border-top: 2px solid {Colors.C4};
"""

# border: 2px solid {Colors.C4};
# border-radius: 5px;

HEADER_3 = f"""
background: rgba(255, 255, 255, 10);
color: {Colors.C1};
font-size: 24px;
font-weight: bold;
border: None;
"""

TOP_BAR_BUTTON = f"""
border: none;
"""

TABLE_STYLE = f"""
QHeaderView::section {'{'} 
    background: rgba(255, 255, 255, 10);
    color: {Colors.C1};
    font-size: 24px;
    font-weight: bold;
{'}'}

QTableView::item {'{'} 
    color: {Colors.C4};
    font-size: 24px;
    font-weight: bold;
    background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,
                                    stop: 0 {QColor(Colors.C2).darker(115).name()},
                                    stop: 0.1 {QColor(Colors.C2).lighter(100).name()},
                                    stop: 0.2 {QColor(Colors.C2).lighter(155).name()},
                                    stop: 0.8 {QColor(Colors.C2).lighter(155).name()},
                                    stop: 0.9 {QColor(Colors.C2).lighter(100).name()}, 
                                    stop: 1.0 {QColor(Colors.C2).darker(115).name()});
    {BUTTON_BORDER}
{'}'}
"""


GRAPH = f"""
    border: 2px solid {Colors.C4};
"""
import qtools
from qtpy.QtWidgets import QMainWindow, QLabel, QToolBar, QPushButton
import qtpy.QtCore
from qtpy.QtCore import QThread
from rx.scheduler import ThreadPoolScheduler
import rx
from rx import operators as ops

app = qtools.qtApp
win = QMainWindow()
win.show()

toolbar = win.addToolBar("File")
btn = QPushButton("ADD", toolbar)
toolbar.addWidget(btn)

gui_scheduler = qtools.QtUiScheduler(qtpy.QtCore, app)
thread_pool = ThreadPoolScheduler()


def addLabel(x):
    label = QLabel("A", toolbar)
    toolbar.addWidget(label)


def bgAlg(x):
    QThread.sleep(10)
    return x


def onClicked():
    xs = rx.from_([1, 2, 3, 4, 5])
    xs.pipe(
        ops.map(bgAlg),
        ops.subscribe_on(thread_pool),
        ops.observe_on(gui_scheduler),
    ).subscribe(addLabel)


btn.clicked.connect(onClicked)

app.exec()

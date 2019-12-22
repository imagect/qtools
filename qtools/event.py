
from qtpy.QtCore import QThread, QObject, QEvent


class CallbackEvent(QEvent):
    typeid = QEvent.User + 1

    def __init__(self, cb=None):
        super().__init__(CallbackEvent.typeid)
        if cb is not None:
            self.cb = cb
        else :
            self.cb = lambda x : x
    pass



class EventSpy(QObject):

    def __init__(self, target: QObject, cb=None):
        QObject.__init__(self)
        self.target = target
        self.cb = cb

    def eventFilter(self, watched: QObject, ev: QEvent):
        if watched is self.target and ev.type() == CallbackEvent.typeid:
            if self.cb:
                self.cb(ev)
                return True
        return super().eventFilter(watched, ev)


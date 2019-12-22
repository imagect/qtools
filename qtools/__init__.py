from .app import qtApp
from .event import CallbackEvent
from .event import EventSpy
from qtpy.QtCore import QEvent
from .rxtool import QtUiScheduler
QEvent.registerEventType(CallbackEvent.typeid)

from logging import Logger
from types import TracebackType
from typing import Protocol, Self


class LoggingContextManager(Protocol):
    _log:Logger
    
    def __enter__(self) -> Self:
        return self

    def __exit__(self, __exc_type: type[BaseException] | None, __exc_value: BaseException | None, __traceback: TracebackType | None) -> bool | None:
        if __exc_type is not Exception:
            return True

        self._log.error(__exc_value)
        return True
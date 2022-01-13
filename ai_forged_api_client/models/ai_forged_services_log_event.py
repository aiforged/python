import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AIForgedServicesLogEvent")


@attr.s(auto_attribs=True)
class AIForgedServicesLogEvent:
    """
    Attributes:
        timestamp (Union[Unset, datetime.datetime]):
        level (Union[Unset, str]):
        message (Union[Unset, str]):
        exception (Union[Unset, None, str]):
        context (Union[Unset, None, str]):
    """

    timestamp: Union[Unset, datetime.datetime] = UNSET
    level: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    exception: Union[Unset, None, str] = UNSET
    context: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        level = self.level
        message = self.message
        exception = self.exception
        context = self.context

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if level is not UNSET:
            field_dict["level"] = level
        if message is not UNSET:
            field_dict["message"] = message
        if exception is not UNSET:
            field_dict["exception"] = exception
        if context is not UNSET:
            field_dict["context"] = context

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        level = d.pop("level", UNSET)

        message = d.pop("message", UNSET)

        exception = d.pop("exception", UNSET)

        context = d.pop("context", UNSET)

        ai_forged_services_log_event = cls(
            timestamp=timestamp,
            level=level,
            message=message,
            exception=exception,
            context=context,
        )

        return ai_forged_services_log_event

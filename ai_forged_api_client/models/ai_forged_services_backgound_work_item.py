import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AIForgedServicesBackgoundWorkItem")


@attr.s(auto_attribs=True)
class AIForgedServicesBackgoundWorkItem:
    """
    Attributes:
        conn_id (Union[Unset, None, str]):
        user_id (Union[Unset, None, str]):
        id (Union[Unset, str]):
        info (Union[Unset, None, str]):
        exception (Union[Unset, None, str]):
        progress (Union[Unset, float]):
        start (Union[Unset, None, datetime.datetime]):
        end (Union[Unset, None, datetime.datetime]):
    """

    conn_id: Union[Unset, None, str] = UNSET
    user_id: Union[Unset, None, str] = UNSET
    id: Union[Unset, str] = UNSET
    info: Union[Unset, None, str] = UNSET
    exception: Union[Unset, None, str] = UNSET
    progress: Union[Unset, float] = UNSET
    start: Union[Unset, None, datetime.datetime] = UNSET
    end: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        conn_id = self.conn_id
        user_id = self.user_id
        id = self.id
        info = self.info
        exception = self.exception
        progress = self.progress
        start: Union[Unset, None, str] = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat() if self.start else None

        end: Union[Unset, None, str] = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat() if self.end else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if conn_id is not UNSET:
            field_dict["connId"] = conn_id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if id is not UNSET:
            field_dict["id"] = id
        if info is not UNSET:
            field_dict["info"] = info
        if exception is not UNSET:
            field_dict["exception"] = exception
        if progress is not UNSET:
            field_dict["progress"] = progress
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        conn_id = d.pop("connId", UNSET)

        user_id = d.pop("userId", UNSET)

        id = d.pop("id", UNSET)

        info = d.pop("info", UNSET)

        exception = d.pop("exception", UNSET)

        progress = d.pop("progress", UNSET)

        _start = d.pop("start", UNSET)
        start: Union[Unset, None, datetime.datetime]
        if _start is None:
            start = None
        elif isinstance(_start, Unset):
            start = UNSET
        else:
            start = isoparse(_start)

        _end = d.pop("end", UNSET)
        end: Union[Unset, None, datetime.datetime]
        if _end is None:
            end = None
        elif isinstance(_end, Unset):
            end = UNSET
        else:
            end = isoparse(_end)

        ai_forged_services_backgound_work_item = cls(
            conn_id=conn_id,
            user_id=user_id,
            id=id,
            info=info,
            exception=exception,
            progress=progress,
            start=start,
            end=end,
        )

        return ai_forged_services_backgound_work_item

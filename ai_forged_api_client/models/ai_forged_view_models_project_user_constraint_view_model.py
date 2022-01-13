import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.ai_forged_dal_constraint_interval_type import AIForgedDALConstraintIntervalType
from ..models.ai_forged_dal_constraint_status import AIForgedDALConstraintStatus
from ..models.ai_forged_dal_constraint_type import AIForgedDALConstraintType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AIForgedViewModelsProjectUserConstraintViewModel")


@attr.s(auto_attribs=True)
class AIForgedViewModelsProjectUserConstraintViewModel:
    """
    Attributes:
        id (int):
        project_user_id (int):
        type (Union[Unset, AIForgedDALConstraintType]):
        status (Union[Unset, AIForgedDALConstraintStatus]):
        interval_type (Union[Unset, AIForgedDALConstraintIntervalType]):
        interval (Union[Unset, None, str]):
        from_date (Union[Unset, datetime.datetime]):
        to_date (Union[Unset, None, datetime.datetime]):
        key (Union[Unset, None, str]):
        value (Union[Unset, None, int]):
        comment (Union[Unset, None, str]):
        user_id (Union[Unset, None, str]):
    """

    id: int
    project_user_id: int
    type: Union[Unset, AIForgedDALConstraintType] = UNSET
    status: Union[Unset, AIForgedDALConstraintStatus] = UNSET
    interval_type: Union[Unset, AIForgedDALConstraintIntervalType] = UNSET
    interval: Union[Unset, None, str] = UNSET
    from_date: Union[Unset, datetime.datetime] = UNSET
    to_date: Union[Unset, None, datetime.datetime] = UNSET
    key: Union[Unset, None, str] = UNSET
    value: Union[Unset, None, int] = UNSET
    comment: Union[Unset, None, str] = UNSET
    user_id: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        project_user_id = self.project_user_id
        type: Union[Unset, int] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        interval_type: Union[Unset, int] = UNSET
        if not isinstance(self.interval_type, Unset):
            interval_type = self.interval_type.value

        interval = self.interval
        from_date: Union[Unset, str] = UNSET
        if not isinstance(self.from_date, Unset):
            from_date = self.from_date.isoformat()

        to_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.to_date, Unset):
            to_date = self.to_date.isoformat() if self.to_date else None

        key = self.key
        value = self.value
        comment = self.comment
        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "projectUserId": project_user_id,
            }
        )
        if type is not UNSET:
            field_dict["type"] = type
        if status is not UNSET:
            field_dict["status"] = status
        if interval_type is not UNSET:
            field_dict["intervalType"] = interval_type
        if interval is not UNSET:
            field_dict["interval"] = interval
        if from_date is not UNSET:
            field_dict["fromDate"] = from_date
        if to_date is not UNSET:
            field_dict["toDate"] = to_date
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value
        if comment is not UNSET:
            field_dict["comment"] = comment
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        project_user_id = d.pop("projectUserId")

        _type = d.pop("type", UNSET)
        type: Union[Unset, AIForgedDALConstraintType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = AIForgedDALConstraintType(_type)

        _status = d.pop("status", UNSET)
        status: Union[Unset, AIForgedDALConstraintStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AIForgedDALConstraintStatus(_status)

        _interval_type = d.pop("intervalType", UNSET)
        interval_type: Union[Unset, AIForgedDALConstraintIntervalType]
        if isinstance(_interval_type, Unset):
            interval_type = UNSET
        else:
            interval_type = AIForgedDALConstraintIntervalType(_interval_type)

        interval = d.pop("interval", UNSET)

        _from_date = d.pop("fromDate", UNSET)
        from_date: Union[Unset, datetime.datetime]
        if isinstance(_from_date, Unset):
            from_date = UNSET
        else:
            from_date = isoparse(_from_date)

        _to_date = d.pop("toDate", UNSET)
        to_date: Union[Unset, None, datetime.datetime]
        if _to_date is None:
            to_date = None
        elif isinstance(_to_date, Unset):
            to_date = UNSET
        else:
            to_date = isoparse(_to_date)

        key = d.pop("key", UNSET)

        value = d.pop("value", UNSET)

        comment = d.pop("comment", UNSET)

        user_id = d.pop("userId", UNSET)

        ai_forged_view_models_project_user_constraint_view_model = cls(
            id=id,
            project_user_id=project_user_id,
            type=type,
            status=status,
            interval_type=interval_type,
            interval=interval,
            from_date=from_date,
            to_date=to_date,
            key=key,
            value=value,
            comment=comment,
            user_id=user_id,
        )

        return ai_forged_view_models_project_user_constraint_view_model

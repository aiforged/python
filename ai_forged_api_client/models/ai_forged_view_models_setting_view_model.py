import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.ai_forged_dal_setting_status import AIForgedDALSettingStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="AIForgedViewModelsSettingViewModel")


@attr.s(auto_attribs=True)
class AIForgedViewModelsSettingViewModel:
    """
    Attributes:
        id (Union[Unset, int]):
        user_id (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        key (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        value (Union[Unset, None, str]):
        status (Union[Unset, AIForgedDALSettingStatus]): The status of a setting related to a parameter
        dtc (Union[Unset, datetime.datetime]):
        dtm (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, int] = UNSET
    user_id: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    key: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    value: Union[Unset, None, str] = UNSET
    status: Union[Unset, AIForgedDALSettingStatus] = UNSET
    dtc: Union[Unset, datetime.datetime] = UNSET
    dtm: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        user_id = self.user_id
        name = self.name
        key = self.key
        description = self.description
        value = self.value
        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        dtc: Union[Unset, str] = UNSET
        if not isinstance(self.dtc, Unset):
            dtc = self.dtc.isoformat()

        dtm: Union[Unset, str] = UNSET
        if not isinstance(self.dtm, Unset):
            dtm = self.dtm.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if name is not UNSET:
            field_dict["name"] = name
        if key is not UNSET:
            field_dict["key"] = key
        if description is not UNSET:
            field_dict["description"] = description
        if value is not UNSET:
            field_dict["value"] = value
        if status is not UNSET:
            field_dict["status"] = status
        if dtc is not UNSET:
            field_dict["dtc"] = dtc
        if dtm is not UNSET:
            field_dict["dtm"] = dtm

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        user_id = d.pop("userId", UNSET)

        name = d.pop("name", UNSET)

        key = d.pop("key", UNSET)

        description = d.pop("description", UNSET)

        value = d.pop("value", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, AIForgedDALSettingStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AIForgedDALSettingStatus(_status)

        _dtc = d.pop("dtc", UNSET)
        dtc: Union[Unset, datetime.datetime]
        if isinstance(_dtc, Unset):
            dtc = UNSET
        else:
            dtc = isoparse(_dtc)

        _dtm = d.pop("dtm", UNSET)
        dtm: Union[Unset, datetime.datetime]
        if isinstance(_dtm, Unset):
            dtm = UNSET
        else:
            dtm = isoparse(_dtm)

        ai_forged_view_models_setting_view_model = cls(
            id=id,
            user_id=user_id,
            name=name,
            key=key,
            description=description,
            value=value,
            status=status,
            dtc=dtc,
            dtm=dtm,
        )

        return ai_forged_view_models_setting_view_model

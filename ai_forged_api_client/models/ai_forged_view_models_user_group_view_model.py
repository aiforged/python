import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.ai_forged_dal_user_group_status import AIForgedDALUserGroupStatus
from ..models.ai_forged_dal_user_group_type import AIForgedDALUserGroupType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AIForgedViewModelsUserGroupViewModel")


@attr.s(auto_attribs=True)
class AIForgedViewModelsUserGroupViewModel:
    """User groups for sharing services and billing

    Attributes:
        id (int):
        user_id (str):
        type (Union[Unset, AIForgedDALUserGroupType]): User group type
        status (Union[Unset, AIForgedDALUserGroupStatus]): User group status
        name (Union[Unset, None, str]):
        dtc (Union[Unset, datetime.datetime]):
        dtm (Union[Unset, datetime.datetime]):
    """

    id: int
    user_id: str
    type: Union[Unset, AIForgedDALUserGroupType] = UNSET
    status: Union[Unset, AIForgedDALUserGroupStatus] = UNSET
    name: Union[Unset, None, str] = UNSET
    dtc: Union[Unset, datetime.datetime] = UNSET
    dtm: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        user_id = self.user_id
        type: Union[Unset, int] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        name = self.name
        dtc: Union[Unset, str] = UNSET
        if not isinstance(self.dtc, Unset):
            dtc = self.dtc.isoformat()

        dtm: Union[Unset, str] = UNSET
        if not isinstance(self.dtm, Unset):
            dtm = self.dtm.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "userId": user_id,
            }
        )
        if type is not UNSET:
            field_dict["type"] = type
        if status is not UNSET:
            field_dict["status"] = status
        if name is not UNSET:
            field_dict["name"] = name
        if dtc is not UNSET:
            field_dict["dtc"] = dtc
        if dtm is not UNSET:
            field_dict["dtm"] = dtm

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        user_id = d.pop("userId")

        _type = d.pop("type", UNSET)
        type: Union[Unset, AIForgedDALUserGroupType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = AIForgedDALUserGroupType(_type)

        _status = d.pop("status", UNSET)
        status: Union[Unset, AIForgedDALUserGroupStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AIForgedDALUserGroupStatus(_status)

        name = d.pop("name", UNSET)

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

        ai_forged_view_models_user_group_view_model = cls(
            id=id,
            user_id=user_id,
            type=type,
            status=status,
            name=name,
            dtc=dtc,
            dtm=dtm,
        )

        return ai_forged_view_models_user_group_view_model

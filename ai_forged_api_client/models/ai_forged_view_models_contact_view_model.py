import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.ai_forged_dal_contact_status import AIForgedDALContactStatus
from ..models.ai_forged_dal_notification_type import AIForgedDALNotificationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AIForgedViewModelsContactViewModel")


@attr.s(auto_attribs=True)
class AIForgedViewModelsContactViewModel:
    """
    Attributes:
        id (Union[Unset, int]):
        user_id (Union[Unset, None, str]):
        status (Union[Unset, AIForgedDALContactStatus]): Contact status
        type (Union[Unset, AIForgedDALNotificationType]): Notification provider type
        address (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        comment (Union[Unset, None, str]):
        dtc (Union[Unset, datetime.datetime]):
        dtm (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, int] = UNSET
    user_id: Union[Unset, None, str] = UNSET
    status: Union[Unset, AIForgedDALContactStatus] = UNSET
    type: Union[Unset, AIForgedDALNotificationType] = UNSET
    address: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    comment: Union[Unset, None, str] = UNSET
    dtc: Union[Unset, datetime.datetime] = UNSET
    dtm: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        user_id = self.user_id
        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        type: Union[Unset, int] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        address = self.address
        name = self.name
        comment = self.comment
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
        if status is not UNSET:
            field_dict["status"] = status
        if type is not UNSET:
            field_dict["type"] = type
        if address is not UNSET:
            field_dict["address"] = address
        if name is not UNSET:
            field_dict["name"] = name
        if comment is not UNSET:
            field_dict["comment"] = comment
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

        _status = d.pop("status", UNSET)
        status: Union[Unset, AIForgedDALContactStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AIForgedDALContactStatus(_status)

        _type = d.pop("type", UNSET)
        type: Union[Unset, AIForgedDALNotificationType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = AIForgedDALNotificationType(_type)

        address = d.pop("address", UNSET)

        name = d.pop("name", UNSET)

        comment = d.pop("comment", UNSET)

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

        ai_forged_view_models_contact_view_model = cls(
            id=id,
            user_id=user_id,
            status=status,
            type=type,
            address=address,
            name=name,
            comment=comment,
            dtc=dtc,
            dtm=dtm,
        )

        return ai_forged_view_models_contact_view_model

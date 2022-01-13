import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.ai_forged_dal_availability import AIForgedDALAvailability
from ..models.ai_forged_dal_verification_status import AIForgedDALVerificationStatus
from ..models.ai_forged_dal_verification_type import AIForgedDALVerificationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AIForgedViewModelsCustomDataSetValue")


@attr.s(auto_attribs=True)
class AIForgedViewModelsCustomDataSetValue:
    """
    Attributes:
        def_id (Union[Unset, int]):
        id (Union[Unset, int]):
        parent_id (Union[Unset, None, int]):
        index (Union[Unset, None, int]):
        value (Union[Unset, None, str]):
        availability (Union[Unset, None, AIForgedDALAvailability]): Avalability of a record
        verification_id (Union[Unset, None, int]):
        ver_value (Union[Unset, None, str]):
        dt (Union[Unset, None, datetime.datetime]):
        confidence (Union[Unset, None, float]):
        type (Union[Unset, None, AIForgedDALVerificationType]): Type of verification
        status (Union[Unset, None, AIForgedDALVerificationStatus]): Verification status flags
        provider (Union[Unset, None, str]):
        result (Union[Unset, None, str]):
    """

    def_id: Union[Unset, int] = UNSET
    id: Union[Unset, int] = UNSET
    parent_id: Union[Unset, None, int] = UNSET
    index: Union[Unset, None, int] = UNSET
    value: Union[Unset, None, str] = UNSET
    availability: Union[Unset, None, AIForgedDALAvailability] = UNSET
    verification_id: Union[Unset, None, int] = UNSET
    ver_value: Union[Unset, None, str] = UNSET
    dt: Union[Unset, None, datetime.datetime] = UNSET
    confidence: Union[Unset, None, float] = UNSET
    type: Union[Unset, None, AIForgedDALVerificationType] = UNSET
    status: Union[Unset, None, AIForgedDALVerificationStatus] = UNSET
    provider: Union[Unset, None, str] = UNSET
    result: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        def_id = self.def_id
        id = self.id
        parent_id = self.parent_id
        index = self.index
        value = self.value
        availability: Union[Unset, None, int] = UNSET
        if not isinstance(self.availability, Unset):
            availability = self.availability.value if self.availability else None

        verification_id = self.verification_id
        ver_value = self.ver_value
        dt: Union[Unset, None, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat() if self.dt else None

        confidence = self.confidence
        type: Union[Unset, None, int] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value if self.type else None

        status: Union[Unset, None, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value if self.status else None

        provider = self.provider
        result = self.result

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if def_id is not UNSET:
            field_dict["defId"] = def_id
        if id is not UNSET:
            field_dict["id"] = id
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if index is not UNSET:
            field_dict["index"] = index
        if value is not UNSET:
            field_dict["value"] = value
        if availability is not UNSET:
            field_dict["availability"] = availability
        if verification_id is not UNSET:
            field_dict["verificationId"] = verification_id
        if ver_value is not UNSET:
            field_dict["verValue"] = ver_value
        if dt is not UNSET:
            field_dict["dt"] = dt
        if confidence is not UNSET:
            field_dict["confidence"] = confidence
        if type is not UNSET:
            field_dict["type"] = type
        if status is not UNSET:
            field_dict["status"] = status
        if provider is not UNSET:
            field_dict["provider"] = provider
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        def_id = d.pop("defId", UNSET)

        id = d.pop("id", UNSET)

        parent_id = d.pop("parentId", UNSET)

        index = d.pop("index", UNSET)

        value = d.pop("value", UNSET)

        _availability = d.pop("availability", UNSET)
        availability: Union[Unset, None, AIForgedDALAvailability]
        if _availability is None:
            availability = None
        elif isinstance(_availability, Unset):
            availability = UNSET
        else:
            availability = AIForgedDALAvailability(_availability)

        verification_id = d.pop("verificationId", UNSET)

        ver_value = d.pop("verValue", UNSET)

        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, None, datetime.datetime]
        if _dt is None:
            dt = None
        elif isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        confidence = d.pop("confidence", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, None, AIForgedDALVerificationType]
        if _type is None:
            type = None
        elif isinstance(_type, Unset):
            type = UNSET
        else:
            type = AIForgedDALVerificationType(_type)

        _status = d.pop("status", UNSET)
        status: Union[Unset, None, AIForgedDALVerificationStatus]
        if _status is None:
            status = None
        elif isinstance(_status, Unset):
            status = UNSET
        else:
            status = AIForgedDALVerificationStatus(_status)

        provider = d.pop("provider", UNSET)

        result = d.pop("result", UNSET)

        ai_forged_view_models_custom_data_set_value = cls(
            def_id=def_id,
            id=id,
            parent_id=parent_id,
            index=index,
            value=value,
            availability=availability,
            verification_id=verification_id,
            ver_value=ver_value,
            dt=dt,
            confidence=confidence,
            type=type,
            status=status,
            provider=provider,
            result=result,
        )

        return ai_forged_view_models_custom_data_set_value

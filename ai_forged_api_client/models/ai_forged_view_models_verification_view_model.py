import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.ai_forged_dal_verification_status import AIForgedDALVerificationStatus
from ..models.ai_forged_dal_verification_type import AIForgedDALVerificationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AIForgedViewModelsVerificationViewModel")


@attr.s(auto_attribs=True)
class AIForgedViewModelsVerificationViewModel:
    """System and user verification info for fields on documents

    Attributes:
        id (int):
        parameter_id (int):
        user_id (Union[Unset, None, str]):
        value (Union[Unset, None, str]):
        dt (Union[Unset, datetime.datetime]):
        confidence (Union[Unset, None, float]):
        symbols_confidence (Union[Unset, None, str]):
        type (Union[Unset, AIForgedDALVerificationType]): Type of verification
        status (Union[Unset, AIForgedDALVerificationStatus]): Verification status flags
        result (Union[Unset, None, str]):
        box (Union[Unset, None, str]):
        info (Union[Unset, None, str]):
        data (Union[Unset, None, str]):
        user_name (Union[Unset, None, str]):
        service_id (Union[Unset, None, int]):
        service_doc_id (Union[Unset, None, int]):
        provider (Union[Unset, None, str]):
        setting_id (Union[Unset, None, int]):
        work_item (Union[Unset, None, int]):
        transaction_id (Union[Unset, None, int]):
        charge (Union[Unset, float]):
    """

    id: int
    parameter_id: int
    user_id: Union[Unset, None, str] = UNSET
    value: Union[Unset, None, str] = UNSET
    dt: Union[Unset, datetime.datetime] = UNSET
    confidence: Union[Unset, None, float] = UNSET
    symbols_confidence: Union[Unset, None, str] = UNSET
    type: Union[Unset, AIForgedDALVerificationType] = UNSET
    status: Union[Unset, AIForgedDALVerificationStatus] = UNSET
    result: Union[Unset, None, str] = UNSET
    box: Union[Unset, None, str] = UNSET
    info: Union[Unset, None, str] = UNSET
    data: Union[Unset, None, str] = UNSET
    user_name: Union[Unset, None, str] = UNSET
    service_id: Union[Unset, None, int] = UNSET
    service_doc_id: Union[Unset, None, int] = UNSET
    provider: Union[Unset, None, str] = UNSET
    setting_id: Union[Unset, None, int] = UNSET
    work_item: Union[Unset, None, int] = UNSET
    transaction_id: Union[Unset, None, int] = UNSET
    charge: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        parameter_id = self.parameter_id
        user_id = self.user_id
        value = self.value
        dt: Union[Unset, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat()

        confidence = self.confidence
        symbols_confidence = self.symbols_confidence
        type: Union[Unset, int] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        result = self.result
        box = self.box
        info = self.info
        data = self.data
        user_name = self.user_name
        service_id = self.service_id
        service_doc_id = self.service_doc_id
        provider = self.provider
        setting_id = self.setting_id
        work_item = self.work_item
        transaction_id = self.transaction_id
        charge = self.charge

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "parameterId": parameter_id,
            }
        )
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if value is not UNSET:
            field_dict["value"] = value
        if dt is not UNSET:
            field_dict["dt"] = dt
        if confidence is not UNSET:
            field_dict["confidence"] = confidence
        if symbols_confidence is not UNSET:
            field_dict["symbolsConfidence"] = symbols_confidence
        if type is not UNSET:
            field_dict["type"] = type
        if status is not UNSET:
            field_dict["status"] = status
        if result is not UNSET:
            field_dict["result"] = result
        if box is not UNSET:
            field_dict["box"] = box
        if info is not UNSET:
            field_dict["info"] = info
        if data is not UNSET:
            field_dict["data"] = data
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if service_id is not UNSET:
            field_dict["serviceId"] = service_id
        if service_doc_id is not UNSET:
            field_dict["serviceDocId"] = service_doc_id
        if provider is not UNSET:
            field_dict["provider"] = provider
        if setting_id is not UNSET:
            field_dict["settingId"] = setting_id
        if work_item is not UNSET:
            field_dict["workItem"] = work_item
        if transaction_id is not UNSET:
            field_dict["transactionId"] = transaction_id
        if charge is not UNSET:
            field_dict["charge"] = charge

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        parameter_id = d.pop("parameterId")

        user_id = d.pop("userId", UNSET)

        value = d.pop("value", UNSET)

        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, datetime.datetime]
        if isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        confidence = d.pop("confidence", UNSET)

        symbols_confidence = d.pop("symbolsConfidence", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, AIForgedDALVerificationType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = AIForgedDALVerificationType(_type)

        _status = d.pop("status", UNSET)
        status: Union[Unset, AIForgedDALVerificationStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AIForgedDALVerificationStatus(_status)

        result = d.pop("result", UNSET)

        box = d.pop("box", UNSET)

        info = d.pop("info", UNSET)

        data = d.pop("data", UNSET)

        user_name = d.pop("userName", UNSET)

        service_id = d.pop("serviceId", UNSET)

        service_doc_id = d.pop("serviceDocId", UNSET)

        provider = d.pop("provider", UNSET)

        setting_id = d.pop("settingId", UNSET)

        work_item = d.pop("workItem", UNSET)

        transaction_id = d.pop("transactionId", UNSET)

        charge = d.pop("charge", UNSET)

        ai_forged_view_models_verification_view_model = cls(
            id=id,
            parameter_id=parameter_id,
            user_id=user_id,
            value=value,
            dt=dt,
            confidence=confidence,
            symbols_confidence=symbols_confidence,
            type=type,
            status=status,
            result=result,
            box=box,
            info=info,
            data=data,
            user_name=user_name,
            service_id=service_id,
            service_doc_id=service_doc_id,
            provider=provider,
            setting_id=setting_id,
            work_item=work_item,
            transaction_id=transaction_id,
            charge=charge,
        )

        return ai_forged_view_models_verification_view_model

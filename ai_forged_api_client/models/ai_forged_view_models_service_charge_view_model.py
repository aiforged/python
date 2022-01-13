import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.ai_forged_dal_charge_status import AIForgedDALChargeStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="AIForgedViewModelsServiceChargeViewModel")


@attr.s(auto_attribs=True)
class AIForgedViewModelsServiceChargeViewModel:
    """
    Attributes:
        id (int):
        service_id (int):
        status (Union[Unset, AIForgedDALChargeStatus]):
        dtc (Union[Unset, datetime.datetime]):
        dtm (Union[Unset, datetime.datetime]):
        from_date (Union[Unset, datetime.datetime]):
        to_date (Union[Unset, None, datetime.datetime]):
        cost (Union[Unset, None, float]):
        charge (Union[Unset, None, float]):
        comment (Union[Unset, None, str]):
        user_id (Union[Unset, None, str]):
    """

    id: int
    service_id: int
    status: Union[Unset, AIForgedDALChargeStatus] = UNSET
    dtc: Union[Unset, datetime.datetime] = UNSET
    dtm: Union[Unset, datetime.datetime] = UNSET
    from_date: Union[Unset, datetime.datetime] = UNSET
    to_date: Union[Unset, None, datetime.datetime] = UNSET
    cost: Union[Unset, None, float] = UNSET
    charge: Union[Unset, None, float] = UNSET
    comment: Union[Unset, None, str] = UNSET
    user_id: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        service_id = self.service_id
        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        dtc: Union[Unset, str] = UNSET
        if not isinstance(self.dtc, Unset):
            dtc = self.dtc.isoformat()

        dtm: Union[Unset, str] = UNSET
        if not isinstance(self.dtm, Unset):
            dtm = self.dtm.isoformat()

        from_date: Union[Unset, str] = UNSET
        if not isinstance(self.from_date, Unset):
            from_date = self.from_date.isoformat()

        to_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.to_date, Unset):
            to_date = self.to_date.isoformat() if self.to_date else None

        cost = self.cost
        charge = self.charge
        comment = self.comment
        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "serviceId": service_id,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if dtc is not UNSET:
            field_dict["dtc"] = dtc
        if dtm is not UNSET:
            field_dict["dtm"] = dtm
        if from_date is not UNSET:
            field_dict["fromDate"] = from_date
        if to_date is not UNSET:
            field_dict["toDate"] = to_date
        if cost is not UNSET:
            field_dict["cost"] = cost
        if charge is not UNSET:
            field_dict["charge"] = charge
        if comment is not UNSET:
            field_dict["comment"] = comment
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        service_id = d.pop("serviceId")

        _status = d.pop("status", UNSET)
        status: Union[Unset, AIForgedDALChargeStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AIForgedDALChargeStatus(_status)

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

        cost = d.pop("cost", UNSET)

        charge = d.pop("charge", UNSET)

        comment = d.pop("comment", UNSET)

        user_id = d.pop("userId", UNSET)

        ai_forged_view_models_service_charge_view_model = cls(
            id=id,
            service_id=service_id,
            status=status,
            dtc=dtc,
            dtm=dtm,
            from_date=from_date,
            to_date=to_date,
            cost=cost,
            charge=charge,
            comment=comment,
            user_id=user_id,
        )

        return ai_forged_view_models_service_charge_view_model

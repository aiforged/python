import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AIForgedDALModelsTransactionsAuditViewModel")


@attr.s(auto_attribs=True)
class AIForgedDALModelsTransactionsAuditViewModel:
    """
    Attributes:
        id (int):
        service_id (Union[Unset, None, int]):
        project_id (Union[Unset, None, int]):
        bundle_id (Union[Unset, None, int]):
        payment_id (Union[Unset, None, int]):
        charge_id (Union[Unset, None, int]):
        related_txn_id (Union[Unset, None, int]):
        user_id (Union[Unset, None, str]):
        run_id (Union[Unset, None, str]):
        dtc (Union[Unset, datetime.datetime]):
        dtm (Union[Unset, datetime.datetime]):
        qty (Union[Unset, int]):
        price (Union[Unset, float]):
        cost (Union[Unset, float]):
        is_credit (Union[Unset, bool]):
    """

    id: int
    service_id: Union[Unset, None, int] = UNSET
    project_id: Union[Unset, None, int] = UNSET
    bundle_id: Union[Unset, None, int] = UNSET
    payment_id: Union[Unset, None, int] = UNSET
    charge_id: Union[Unset, None, int] = UNSET
    related_txn_id: Union[Unset, None, int] = UNSET
    user_id: Union[Unset, None, str] = UNSET
    run_id: Union[Unset, None, str] = UNSET
    dtc: Union[Unset, datetime.datetime] = UNSET
    dtm: Union[Unset, datetime.datetime] = UNSET
    qty: Union[Unset, int] = UNSET
    price: Union[Unset, float] = UNSET
    cost: Union[Unset, float] = UNSET
    is_credit: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        service_id = self.service_id
        project_id = self.project_id
        bundle_id = self.bundle_id
        payment_id = self.payment_id
        charge_id = self.charge_id
        related_txn_id = self.related_txn_id
        user_id = self.user_id
        run_id = self.run_id
        dtc: Union[Unset, str] = UNSET
        if not isinstance(self.dtc, Unset):
            dtc = self.dtc.isoformat()

        dtm: Union[Unset, str] = UNSET
        if not isinstance(self.dtm, Unset):
            dtm = self.dtm.isoformat()

        qty = self.qty
        price = self.price
        cost = self.cost
        is_credit = self.is_credit

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
            }
        )
        if service_id is not UNSET:
            field_dict["serviceId"] = service_id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if bundle_id is not UNSET:
            field_dict["bundleId"] = bundle_id
        if payment_id is not UNSET:
            field_dict["paymentId"] = payment_id
        if charge_id is not UNSET:
            field_dict["chargeId"] = charge_id
        if related_txn_id is not UNSET:
            field_dict["relatedTxnId"] = related_txn_id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if run_id is not UNSET:
            field_dict["runId"] = run_id
        if dtc is not UNSET:
            field_dict["dtc"] = dtc
        if dtm is not UNSET:
            field_dict["dtm"] = dtm
        if qty is not UNSET:
            field_dict["qty"] = qty
        if price is not UNSET:
            field_dict["price"] = price
        if cost is not UNSET:
            field_dict["cost"] = cost
        if is_credit is not UNSET:
            field_dict["isCredit"] = is_credit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        service_id = d.pop("serviceId", UNSET)

        project_id = d.pop("projectId", UNSET)

        bundle_id = d.pop("bundleId", UNSET)

        payment_id = d.pop("paymentId", UNSET)

        charge_id = d.pop("chargeId", UNSET)

        related_txn_id = d.pop("relatedTxnId", UNSET)

        user_id = d.pop("userId", UNSET)

        run_id = d.pop("runId", UNSET)

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

        qty = d.pop("qty", UNSET)

        price = d.pop("price", UNSET)

        cost = d.pop("cost", UNSET)

        is_credit = d.pop("isCredit", UNSET)

        ai_forged_dal_models_transactions_audit_view_model = cls(
            id=id,
            service_id=service_id,
            project_id=project_id,
            bundle_id=bundle_id,
            payment_id=payment_id,
            charge_id=charge_id,
            related_txn_id=related_txn_id,
            user_id=user_id,
            run_id=run_id,
            dtc=dtc,
            dtm=dtm,
            qty=qty,
            price=price,
            cost=cost,
            is_credit=is_credit,
        )

        return ai_forged_dal_models_transactions_audit_view_model

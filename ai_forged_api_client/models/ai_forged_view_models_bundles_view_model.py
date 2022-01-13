import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.ai_forged_dal_bundle_type import AIForgedDALBundleType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AIForgedViewModelsBundlesViewModel")


@attr.s(auto_attribs=True)
class AIForgedViewModelsBundlesViewModel:
    """A bundle for payments and credits

    Attributes:
        id (int):
        type (AIForgedDALBundleType): Type of a bundle
        name (str):
        description (Union[Unset, None, str]):
        count (Union[Unset, int]):
        price (Union[Unset, float]):
        discount (Union[Unset, float]):
        dtc (Union[Unset, datetime.datetime]):
        dtm (Union[Unset, datetime.datetime]):
        is_active (Union[Unset, bool]):
        expiry_date (Union[Unset, None, datetime.datetime]):
        product_code (Union[Unset, None, str]):
    """

    id: int
    type: AIForgedDALBundleType
    name: str
    description: Union[Unset, None, str] = UNSET
    count: Union[Unset, int] = UNSET
    price: Union[Unset, float] = UNSET
    discount: Union[Unset, float] = UNSET
    dtc: Union[Unset, datetime.datetime] = UNSET
    dtm: Union[Unset, datetime.datetime] = UNSET
    is_active: Union[Unset, bool] = UNSET
    expiry_date: Union[Unset, None, datetime.datetime] = UNSET
    product_code: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type = self.type.value

        name = self.name
        description = self.description
        count = self.count
        price = self.price
        discount = self.discount
        dtc: Union[Unset, str] = UNSET
        if not isinstance(self.dtc, Unset):
            dtc = self.dtc.isoformat()

        dtm: Union[Unset, str] = UNSET
        if not isinstance(self.dtm, Unset):
            dtm = self.dtm.isoformat()

        is_active = self.is_active
        expiry_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.expiry_date, Unset):
            expiry_date = self.expiry_date.isoformat() if self.expiry_date else None

        product_code = self.product_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "type": type,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if count is not UNSET:
            field_dict["count"] = count
        if price is not UNSET:
            field_dict["price"] = price
        if discount is not UNSET:
            field_dict["discount"] = discount
        if dtc is not UNSET:
            field_dict["dtc"] = dtc
        if dtm is not UNSET:
            field_dict["dtm"] = dtm
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if expiry_date is not UNSET:
            field_dict["expiryDate"] = expiry_date
        if product_code is not UNSET:
            field_dict["productCode"] = product_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        type = AIForgedDALBundleType(d.pop("type"))

        name = d.pop("name")

        description = d.pop("description", UNSET)

        count = d.pop("count", UNSET)

        price = d.pop("price", UNSET)

        discount = d.pop("discount", UNSET)

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

        is_active = d.pop("isActive", UNSET)

        _expiry_date = d.pop("expiryDate", UNSET)
        expiry_date: Union[Unset, None, datetime.datetime]
        if _expiry_date is None:
            expiry_date = None
        elif isinstance(_expiry_date, Unset):
            expiry_date = UNSET
        else:
            expiry_date = isoparse(_expiry_date)

        product_code = d.pop("productCode", UNSET)

        ai_forged_view_models_bundles_view_model = cls(
            id=id,
            type=type,
            name=name,
            description=description,
            count=count,
            price=price,
            discount=discount,
            dtc=dtc,
            dtm=dtm,
            is_active=is_active,
            expiry_date=expiry_date,
            product_code=product_code,
        )

        return ai_forged_view_models_bundles_view_model

from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AIForgedViewModelsOrderViewModel")


@attr.s(auto_attribs=True)
class AIForgedViewModelsOrderViewModel:
    """Credit card transaction order information

    Attributes:
        order_id (Union[Unset, None, str]):
        authorization_id (Union[Unset, None, str]):
    """

    order_id: Union[Unset, None, str] = UNSET
    authorization_id: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        order_id = self.order_id
        authorization_id = self.authorization_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if order_id is not UNSET:
            field_dict["orderId"] = order_id
        if authorization_id is not UNSET:
            field_dict["authorizationId"] = authorization_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        order_id = d.pop("orderId", UNSET)

        authorization_id = d.pop("authorizationId", UNSET)

        ai_forged_view_models_order_view_model = cls(
            order_id=order_id,
            authorization_id=authorization_id,
        )

        return ai_forged_view_models_order_view_model

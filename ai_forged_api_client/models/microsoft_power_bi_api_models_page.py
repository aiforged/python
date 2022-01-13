from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="MicrosoftPowerBIApiModelsPage")


@attr.s(auto_attribs=True)
class MicrosoftPowerBIApiModelsPage:
    """
    Attributes:
        name (Union[Unset, None, str]):
        display_name (Union[Unset, None, str]):
        order (Union[Unset, None, int]):
    """

    name: Union[Unset, None, str] = UNSET
    display_name: Union[Unset, None, str] = UNSET
    order: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        display_name = self.display_name
        order = self.order

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if order is not UNSET:
            field_dict["order"] = order

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        display_name = d.pop("displayName", UNSET)

        order = d.pop("order", UNSET)

        microsoft_power_bi_api_models_page = cls(
            name=name,
            display_name=display_name,
            order=order,
        )

        return microsoft_power_bi_api_models_page

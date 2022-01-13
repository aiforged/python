from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.ai_forged_dal_availability import AIForgedDALAvailability
from ..models.ai_forged_view_models_custom_data_set_value import AIForgedViewModelsCustomDataSetValue
from ..types import UNSET, Unset

T = TypeVar("T", bound="AIForgedViewModelsCustomDataSetRecord")


@attr.s(auto_attribs=True)
class AIForgedViewModelsCustomDataSetRecord:
    """
    Attributes:
        key_id (Union[Unset, int]):
        key_def_id (Union[Unset, int]):
        key_value (Union[Unset, None, str]):
        availability (Union[Unset, None, AIForgedDALAvailability]): Avalability of a record
        values (Union[Unset, None, List[AIForgedViewModelsCustomDataSetValue]]):
    """

    key_id: Union[Unset, int] = UNSET
    key_def_id: Union[Unset, int] = UNSET
    key_value: Union[Unset, None, str] = UNSET
    availability: Union[Unset, None, AIForgedDALAvailability] = UNSET
    values: Union[Unset, None, List[AIForgedViewModelsCustomDataSetValue]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        key_id = self.key_id
        key_def_id = self.key_def_id
        key_value = self.key_value
        availability: Union[Unset, None, int] = UNSET
        if not isinstance(self.availability, Unset):
            availability = self.availability.value if self.availability else None

        values: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.values, Unset):
            if self.values is None:
                values = None
            else:
                values = []
                for values_item_data in self.values:
                    values_item = values_item_data.to_dict()

                    values.append(values_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if key_id is not UNSET:
            field_dict["keyId"] = key_id
        if key_def_id is not UNSET:
            field_dict["keyDefId"] = key_def_id
        if key_value is not UNSET:
            field_dict["keyValue"] = key_value
        if availability is not UNSET:
            field_dict["availability"] = availability
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key_id = d.pop("keyId", UNSET)

        key_def_id = d.pop("keyDefId", UNSET)

        key_value = d.pop("keyValue", UNSET)

        _availability = d.pop("availability", UNSET)
        availability: Union[Unset, None, AIForgedDALAvailability]
        if _availability is None:
            availability = None
        elif isinstance(_availability, Unset):
            availability = UNSET
        else:
            availability = AIForgedDALAvailability(_availability)

        values = []
        _values = d.pop("values", UNSET)
        for values_item_data in _values or []:
            values_item = AIForgedViewModelsCustomDataSetValue.from_dict(values_item_data)

            values.append(values_item)

        ai_forged_view_models_custom_data_set_record = cls(
            key_id=key_id,
            key_def_id=key_def_id,
            key_value=key_value,
            availability=availability,
            values=values,
        )

        return ai_forged_view_models_custom_data_set_record

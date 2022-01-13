from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.ai_forged_dal_data_type_category import AIForgedDALDataTypeCategory
from ..models.ai_forged_dal_value_type import AIForgedDALValueType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AIForgedViewModelsDataTypeViewModel")


@attr.s(auto_attribs=True)
class AIForgedViewModelsDataTypeViewModel:
    """Data types used for rules and internal processing

    Attributes:
        id (AIForgedDALValueType): The type of values used for rules and settings
        name (str):
        description (Union[Unset, None, str]):
        category (Union[Unset, None, AIForgedDALDataTypeCategory]): The category of data types
        value_type_name (Union[Unset, None, str]):
        default_value (Union[Unset, None, str]):
        data (Union[Unset, None, str]):
    """

    id: AIForgedDALValueType
    name: str
    description: Union[Unset, None, str] = UNSET
    category: Union[Unset, None, AIForgedDALDataTypeCategory] = UNSET
    value_type_name: Union[Unset, None, str] = UNSET
    default_value: Union[Unset, None, str] = UNSET
    data: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id.value

        name = self.name
        description = self.description
        category: Union[Unset, None, int] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value if self.category else None

        value_type_name = self.value_type_name
        default_value = self.default_value
        data = self.data

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if category is not UNSET:
            field_dict["category"] = category
        if value_type_name is not UNSET:
            field_dict["valueTypeName"] = value_type_name
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = AIForgedDALValueType(d.pop("id"))

        name = d.pop("name")

        description = d.pop("description", UNSET)

        _category = d.pop("category", UNSET)
        category: Union[Unset, None, AIForgedDALDataTypeCategory]
        if _category is None:
            category = None
        elif isinstance(_category, Unset):
            category = UNSET
        else:
            category = AIForgedDALDataTypeCategory(_category)

        value_type_name = d.pop("valueTypeName", UNSET)

        default_value = d.pop("defaultValue", UNSET)

        data = d.pop("data", UNSET)

        ai_forged_view_models_data_type_view_model = cls(
            id=id,
            name=name,
            description=description,
            category=category,
            value_type_name=value_type_name,
            default_value=default_value,
            data=data,
        )

        return ai_forged_view_models_data_type_view_model

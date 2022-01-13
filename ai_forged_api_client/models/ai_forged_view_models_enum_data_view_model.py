from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.ai_forged_dal_enum_type import AIForgedDALEnumType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AIForgedViewModelsEnumDataViewModel")


@attr.s(auto_attribs=True)
class AIForgedViewModelsEnumDataViewModel:
    """List of system Enums and basic UI info

    Attributes:
        id (int):
        type_name (str):
        name (str):
        type (Union[Unset, AIForgedDALEnumType]): Enum of all enums in the system
        value (Union[Unset, int]):
        description (Union[Unset, None, str]):
        info (Union[Unset, None, str]):
        icon (Union[Unset, None, str]):
        color (Union[Unset, None, str]):
    """

    id: int
    type_name: str
    name: str
    type: Union[Unset, AIForgedDALEnumType] = UNSET
    value: Union[Unset, int] = UNSET
    description: Union[Unset, None, str] = UNSET
    info: Union[Unset, None, str] = UNSET
    icon: Union[Unset, None, str] = UNSET
    color: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type_name = self.type_name
        name = self.name
        type: Union[Unset, int] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        value = self.value
        description = self.description
        info = self.info
        icon = self.icon
        color = self.color

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "typeName": type_name,
                "name": name,
            }
        )
        if type is not UNSET:
            field_dict["type"] = type
        if value is not UNSET:
            field_dict["value"] = value
        if description is not UNSET:
            field_dict["description"] = description
        if info is not UNSET:
            field_dict["info"] = info
        if icon is not UNSET:
            field_dict["icon"] = icon
        if color is not UNSET:
            field_dict["color"] = color

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        type_name = d.pop("typeName")

        name = d.pop("name")

        _type = d.pop("type", UNSET)
        type: Union[Unset, AIForgedDALEnumType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = AIForgedDALEnumType(_type)

        value = d.pop("value", UNSET)

        description = d.pop("description", UNSET)

        info = d.pop("info", UNSET)

        icon = d.pop("icon", UNSET)

        color = d.pop("color", UNSET)

        ai_forged_view_models_enum_data_view_model = cls(
            id=id,
            type_name=type_name,
            name=name,
            type=type,
            value=value,
            description=description,
            info=info,
            icon=icon,
            color=color,
        )

        return ai_forged_view_models_enum_data_view_model

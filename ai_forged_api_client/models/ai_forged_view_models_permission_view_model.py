from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AIForgedViewModelsPermissionViewModel")


@attr.s(auto_attribs=True)
class AIForgedViewModelsPermissionViewModel:
    """
    Attributes:
        name (Union[Unset, None, str]):
        value (Union[Unset, None, str]):
        group_name (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
    """

    name: Union[Unset, None, str] = UNSET
    value: Union[Unset, None, str] = UNSET
    group_name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        value = self.value
        group_name = self.group_name
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if value is not UNSET:
            field_dict["value"] = value
        if group_name is not UNSET:
            field_dict["groupName"] = group_name
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        value = d.pop("value", UNSET)

        group_name = d.pop("groupName", UNSET)

        description = d.pop("description", UNSET)

        ai_forged_view_models_permission_view_model = cls(
            name=name,
            value=value,
            group_name=group_name,
            description=description,
        )

        return ai_forged_view_models_permission_view_model

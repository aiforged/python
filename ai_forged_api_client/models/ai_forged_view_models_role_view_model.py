from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.ai_forged_view_models_permission_view_model import AIForgedViewModelsPermissionViewModel
from ..types import UNSET, Unset

T = TypeVar("T", bound="AIForgedViewModelsRoleViewModel")


@attr.s(auto_attribs=True)
class AIForgedViewModelsRoleViewModel:
    """
    Attributes:
        name (str):
        id (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        users_count (Union[Unset, int]):
        permissions (Union[Unset, None, List[AIForgedViewModelsPermissionViewModel]]):
    """

    name: str
    id: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    users_count: Union[Unset, int] = UNSET
    permissions: Union[Unset, None, List[AIForgedViewModelsPermissionViewModel]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        id = self.id
        description = self.description
        users_count = self.users_count
        permissions: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.permissions, Unset):
            if self.permissions is None:
                permissions = None
            else:
                permissions = []
                for permissions_item_data in self.permissions:
                    permissions_item = permissions_item_data.to_dict()

                    permissions.append(permissions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if users_count is not UNSET:
            field_dict["usersCount"] = users_count
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        id = d.pop("id", UNSET)

        description = d.pop("description", UNSET)

        users_count = d.pop("usersCount", UNSET)

        permissions = []
        _permissions = d.pop("permissions", UNSET)
        for permissions_item_data in _permissions or []:
            permissions_item = AIForgedViewModelsPermissionViewModel.from_dict(permissions_item_data)

            permissions.append(permissions_item)

        ai_forged_view_models_role_view_model = cls(
            name=name,
            id=id,
            description=description,
            users_count=users_count,
            permissions=permissions,
        )

        return ai_forged_view_models_role_view_model

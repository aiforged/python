from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.microsoft_power_bi_api_models_group_user_access_right import MicrosoftPowerBIApiModelsGroupUserAccessRight
from ..models.microsoft_power_bi_api_models_principal_type import MicrosoftPowerBIApiModelsPrincipalType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MicrosoftPowerBIApiModelsGroupUser")


@attr.s(auto_attribs=True)
class MicrosoftPowerBIApiModelsGroupUser:
    """
    Attributes:
        group_user_access_right (Union[Unset, MicrosoftPowerBIApiModelsGroupUserAccessRight]):
        email_address (Union[Unset, None, str]):
        display_name (Union[Unset, None, str]):
        identifier (Union[Unset, None, str]):
        graph_id (Union[Unset, None, str]):
        principal_type (Union[Unset, None, MicrosoftPowerBIApiModelsPrincipalType]):
    """

    group_user_access_right: Union[Unset, MicrosoftPowerBIApiModelsGroupUserAccessRight] = UNSET
    email_address: Union[Unset, None, str] = UNSET
    display_name: Union[Unset, None, str] = UNSET
    identifier: Union[Unset, None, str] = UNSET
    graph_id: Union[Unset, None, str] = UNSET
    principal_type: Union[Unset, None, MicrosoftPowerBIApiModelsPrincipalType] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        group_user_access_right: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.group_user_access_right, Unset):
            group_user_access_right = self.group_user_access_right.to_dict()

        email_address = self.email_address
        display_name = self.display_name
        identifier = self.identifier
        graph_id = self.graph_id
        principal_type: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.principal_type, Unset):
            principal_type = self.principal_type.to_dict() if self.principal_type else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if group_user_access_right is not UNSET:
            field_dict["groupUserAccessRight"] = group_user_access_right
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if graph_id is not UNSET:
            field_dict["graphId"] = graph_id
        if principal_type is not UNSET:
            field_dict["principalType"] = principal_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _group_user_access_right = d.pop("groupUserAccessRight", UNSET)
        group_user_access_right: Union[Unset, MicrosoftPowerBIApiModelsGroupUserAccessRight]
        if isinstance(_group_user_access_right, Unset):
            group_user_access_right = UNSET
        else:
            group_user_access_right = MicrosoftPowerBIApiModelsGroupUserAccessRight.from_dict(_group_user_access_right)

        email_address = d.pop("emailAddress", UNSET)

        display_name = d.pop("displayName", UNSET)

        identifier = d.pop("identifier", UNSET)

        graph_id = d.pop("graphId", UNSET)

        _principal_type = d.pop("principalType", UNSET)
        principal_type: Union[Unset, None, MicrosoftPowerBIApiModelsPrincipalType]
        if _principal_type is None:
            principal_type = None
        elif isinstance(_principal_type, Unset):
            principal_type = UNSET
        else:
            principal_type = MicrosoftPowerBIApiModelsPrincipalType.from_dict(_principal_type)

        microsoft_power_bi_api_models_group_user = cls(
            group_user_access_right=group_user_access_right,
            email_address=email_address,
            display_name=display_name,
            identifier=identifier,
            graph_id=graph_id,
            principal_type=principal_type,
        )

        return microsoft_power_bi_api_models_group_user

from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="MicrosoftAspNetCoreIdentityUserLoginInfo")


@attr.s(auto_attribs=True)
class MicrosoftAspNetCoreIdentityUserLoginInfo:
    """
    Attributes:
        login_provider (Union[Unset, None, str]):
        provider_key (Union[Unset, None, str]):
        provider_display_name (Union[Unset, None, str]):
    """

    login_provider: Union[Unset, None, str] = UNSET
    provider_key: Union[Unset, None, str] = UNSET
    provider_display_name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        login_provider = self.login_provider
        provider_key = self.provider_key
        provider_display_name = self.provider_display_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if login_provider is not UNSET:
            field_dict["loginProvider"] = login_provider
        if provider_key is not UNSET:
            field_dict["providerKey"] = provider_key
        if provider_display_name is not UNSET:
            field_dict["providerDisplayName"] = provider_display_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        login_provider = d.pop("loginProvider", UNSET)

        provider_key = d.pop("providerKey", UNSET)

        provider_display_name = d.pop("providerDisplayName", UNSET)

        microsoft_asp_net_core_identity_user_login_info = cls(
            login_provider=login_provider,
            provider_key=provider_key,
            provider_display_name=provider_display_name,
        )

        return microsoft_asp_net_core_identity_user_login_info

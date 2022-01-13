import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AIForgedViewModelsUserEditViewModel")


@attr.s(auto_attribs=True)
class AIForgedViewModelsUserEditViewModel:
    """
    Attributes:
        user_name (str):
        email (str):
        id (Union[Unset, None, str]):
        full_name (Union[Unset, None, str]):
        job_title (Union[Unset, None, str]):
        phone_number (Union[Unset, None, str]):
        configuration (Union[Unset, None, str]):
        is_enabled (Union[Unset, bool]):
        is_locked_out (Union[Unset, bool]):
        friendly_name (Union[Unset, None, str]):
        created_by (Union[Unset, None, str]):
        updated_by (Union[Unset, None, str]):
        created_date (Union[Unset, datetime.datetime]):
        updated_date (Union[Unset, datetime.datetime]):
        roles (Union[Unset, None, List[str]]):
        current_password (Union[Unset, None, str]):
        new_password (Union[Unset, None, str]):
        confirm_password (Union[Unset, None, str]):
        captcha_token (Union[Unset, None, str]):
    """

    user_name: str
    email: str
    id: Union[Unset, None, str] = UNSET
    full_name: Union[Unset, None, str] = UNSET
    job_title: Union[Unset, None, str] = UNSET
    phone_number: Union[Unset, None, str] = UNSET
    configuration: Union[Unset, None, str] = UNSET
    is_enabled: Union[Unset, bool] = UNSET
    is_locked_out: Union[Unset, bool] = UNSET
    friendly_name: Union[Unset, None, str] = UNSET
    created_by: Union[Unset, None, str] = UNSET
    updated_by: Union[Unset, None, str] = UNSET
    created_date: Union[Unset, datetime.datetime] = UNSET
    updated_date: Union[Unset, datetime.datetime] = UNSET
    roles: Union[Unset, None, List[str]] = UNSET
    current_password: Union[Unset, None, str] = UNSET
    new_password: Union[Unset, None, str] = UNSET
    confirm_password: Union[Unset, None, str] = UNSET
    captcha_token: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_name = self.user_name
        email = self.email
        id = self.id
        full_name = self.full_name
        job_title = self.job_title
        phone_number = self.phone_number
        configuration = self.configuration
        is_enabled = self.is_enabled
        is_locked_out = self.is_locked_out
        friendly_name = self.friendly_name
        created_by = self.created_by
        updated_by = self.updated_by
        created_date: Union[Unset, str] = UNSET
        if not isinstance(self.created_date, Unset):
            created_date = self.created_date.isoformat()

        updated_date: Union[Unset, str] = UNSET
        if not isinstance(self.updated_date, Unset):
            updated_date = self.updated_date.isoformat()

        roles: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.roles, Unset):
            if self.roles is None:
                roles = None
            else:
                roles = self.roles

        current_password = self.current_password
        new_password = self.new_password
        confirm_password = self.confirm_password
        captcha_token = self.captcha_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userName": user_name,
                "email": email,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if job_title is not UNSET:
            field_dict["jobTitle"] = job_title
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if is_locked_out is not UNSET:
            field_dict["isLockedOut"] = is_locked_out
        if friendly_name is not UNSET:
            field_dict["friendlyName"] = friendly_name
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if updated_by is not UNSET:
            field_dict["updatedBy"] = updated_by
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if updated_date is not UNSET:
            field_dict["updatedDate"] = updated_date
        if roles is not UNSET:
            field_dict["roles"] = roles
        if current_password is not UNSET:
            field_dict["currentPassword"] = current_password
        if new_password is not UNSET:
            field_dict["newPassword"] = new_password
        if confirm_password is not UNSET:
            field_dict["confirmPassword"] = confirm_password
        if captcha_token is not UNSET:
            field_dict["captchaToken"] = captcha_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_name = d.pop("userName")

        email = d.pop("email")

        id = d.pop("id", UNSET)

        full_name = d.pop("fullName", UNSET)

        job_title = d.pop("jobTitle", UNSET)

        phone_number = d.pop("phoneNumber", UNSET)

        configuration = d.pop("configuration", UNSET)

        is_enabled = d.pop("isEnabled", UNSET)

        is_locked_out = d.pop("isLockedOut", UNSET)

        friendly_name = d.pop("friendlyName", UNSET)

        created_by = d.pop("createdBy", UNSET)

        updated_by = d.pop("updatedBy", UNSET)

        _created_date = d.pop("createdDate", UNSET)
        created_date: Union[Unset, datetime.datetime]
        if isinstance(_created_date, Unset):
            created_date = UNSET
        else:
            created_date = isoparse(_created_date)

        _updated_date = d.pop("updatedDate", UNSET)
        updated_date: Union[Unset, datetime.datetime]
        if isinstance(_updated_date, Unset):
            updated_date = UNSET
        else:
            updated_date = isoparse(_updated_date)

        roles = cast(List[str], d.pop("roles", UNSET))

        current_password = d.pop("currentPassword", UNSET)

        new_password = d.pop("newPassword", UNSET)

        confirm_password = d.pop("confirmPassword", UNSET)

        captcha_token = d.pop("captchaToken", UNSET)

        ai_forged_view_models_user_edit_view_model = cls(
            user_name=user_name,
            email=email,
            id=id,
            full_name=full_name,
            job_title=job_title,
            phone_number=phone_number,
            configuration=configuration,
            is_enabled=is_enabled,
            is_locked_out=is_locked_out,
            friendly_name=friendly_name,
            created_by=created_by,
            updated_by=updated_by,
            created_date=created_date,
            updated_date=updated_date,
            roles=roles,
            current_password=current_password,
            new_password=new_password,
            confirm_password=confirm_password,
            captcha_token=captcha_token,
        )

        ai_forged_view_models_user_edit_view_model.additional_properties = d
        return ai_forged_view_models_user_edit_view_model

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

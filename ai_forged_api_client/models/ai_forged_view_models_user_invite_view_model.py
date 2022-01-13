from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AIForgedViewModelsUserInviteViewModel")


@attr.s(auto_attribs=True)
class AIForgedViewModelsUserInviteViewModel:
    """
    Attributes:
        email (str):
        project_id (Union[Unset, int]):
        service_id (Union[Unset, int]):
        message (Union[Unset, None, str]):
    """

    email: str
    project_id: Union[Unset, int] = UNSET
    service_id: Union[Unset, int] = UNSET
    message: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        email = self.email
        project_id = self.project_id
        service_id = self.service_id
        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "email": email,
            }
        )
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if service_id is not UNSET:
            field_dict["serviceId"] = service_id
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email")

        project_id = d.pop("projectId", UNSET)

        service_id = d.pop("serviceId", UNSET)

        message = d.pop("message", UNSET)

        ai_forged_view_models_user_invite_view_model = cls(
            email=email,
            project_id=project_id,
            service_id=service_id,
            message=message,
        )

        return ai_forged_view_models_user_invite_view_model

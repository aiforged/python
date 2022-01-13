from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="AIForgedViewModelsUserActivateViewModel")


@attr.s(auto_attribs=True)
class AIForgedViewModelsUserActivateViewModel:
    """
    Attributes:
        user_name (str):
        token (str):
    """

    user_name: str
    token: str

    def to_dict(self) -> Dict[str, Any]:
        user_name = self.user_name
        token = self.token

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "userName": user_name,
                "token": token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_name = d.pop("userName")

        token = d.pop("token")

        ai_forged_view_models_user_activate_view_model = cls(
            user_name=user_name,
            token=token,
        )

        return ai_forged_view_models_user_activate_view_model

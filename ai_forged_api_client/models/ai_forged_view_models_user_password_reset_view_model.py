from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="AIForgedViewModelsUserPasswordResetViewModel")


@attr.s(auto_attribs=True)
class AIForgedViewModelsUserPasswordResetViewModel:
    """
    Attributes:
        user_name (str):
        token (str):
        password (str):
        confirm_password (str):
    """

    user_name: str
    token: str
    password: str
    confirm_password: str

    def to_dict(self) -> Dict[str, Any]:
        user_name = self.user_name
        token = self.token
        password = self.password
        confirm_password = self.confirm_password

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "userName": user_name,
                "token": token,
                "password": password,
                "confirmPassword": confirm_password,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_name = d.pop("userName")

        token = d.pop("token")

        password = d.pop("password")

        confirm_password = d.pop("confirmPassword")

        ai_forged_view_models_user_password_reset_view_model = cls(
            user_name=user_name,
            token=token,
            password=password,
            confirm_password=confirm_password,
        )

        return ai_forged_view_models_user_password_reset_view_model

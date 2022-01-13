import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AIForgedViewModelsRatingViewModel")


@attr.s(auto_attribs=True)
class AIForgedViewModelsRatingViewModel:
    """
    Attributes:
        id (int):
        param_def_id (int):
        parameter_id (Union[Unset, None, int]):
        verification_id (Union[Unset, None, int]):
        user_id (Union[Unset, None, str]):
        dt (Union[Unset, datetime.datetime]):
        value (Union[Unset, float]):
        comment (Union[Unset, None, str]):
        user_name (Union[Unset, None, str]):
    """

    id: int
    param_def_id: int
    parameter_id: Union[Unset, None, int] = UNSET
    verification_id: Union[Unset, None, int] = UNSET
    user_id: Union[Unset, None, str] = UNSET
    dt: Union[Unset, datetime.datetime] = UNSET
    value: Union[Unset, float] = UNSET
    comment: Union[Unset, None, str] = UNSET
    user_name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        param_def_id = self.param_def_id
        parameter_id = self.parameter_id
        verification_id = self.verification_id
        user_id = self.user_id
        dt: Union[Unset, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat()

        value = self.value
        comment = self.comment
        user_name = self.user_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "paramDefId": param_def_id,
            }
        )
        if parameter_id is not UNSET:
            field_dict["parameterId"] = parameter_id
        if verification_id is not UNSET:
            field_dict["verificationId"] = verification_id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if dt is not UNSET:
            field_dict["dt"] = dt
        if value is not UNSET:
            field_dict["value"] = value
        if comment is not UNSET:
            field_dict["comment"] = comment
        if user_name is not UNSET:
            field_dict["userName"] = user_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        param_def_id = d.pop("paramDefId")

        parameter_id = d.pop("parameterId", UNSET)

        verification_id = d.pop("verificationId", UNSET)

        user_id = d.pop("userId", UNSET)

        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, datetime.datetime]
        if isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        value = d.pop("value", UNSET)

        comment = d.pop("comment", UNSET)

        user_name = d.pop("userName", UNSET)

        ai_forged_view_models_rating_view_model = cls(
            id=id,
            param_def_id=param_def_id,
            parameter_id=parameter_id,
            verification_id=verification_id,
            user_id=user_id,
            dt=dt,
            value=value,
            comment=comment,
            user_name=user_name,
        )

        return ai_forged_view_models_rating_view_model

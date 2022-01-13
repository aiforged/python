from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="MicrosoftPowerBIApiModelsReportUserAccessRight")


@attr.s(auto_attribs=True)
class MicrosoftPowerBIApiModelsReportUserAccessRight:
    """ """

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        src_dict.copy()
        microsoft_power_bi_api_models_report_user_access_right = cls()

        return microsoft_power_bi_api_models_report_user_access_right

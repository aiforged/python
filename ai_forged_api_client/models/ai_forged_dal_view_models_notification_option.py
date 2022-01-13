from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.ai_forged_dal_view_models_notification_setting import AIForgedDALViewModelsNotificationSetting
from ..types import UNSET, Unset

T = TypeVar("T", bound="AIForgedDALViewModelsNotificationOption")


@attr.s(auto_attribs=True)
class AIForgedDALViewModelsNotificationOption:
    """
    Attributes:
        name (Union[Unset, None, str]):
        settings (Union[Unset, None, List[AIForgedDALViewModelsNotificationSetting]]):
    """

    name: Union[Unset, None, str] = UNSET
    settings: Union[Unset, None, List[AIForgedDALViewModelsNotificationSetting]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        settings: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.settings, Unset):
            if self.settings is None:
                settings = None
            else:
                settings = []
                for settings_item_data in self.settings:
                    settings_item = settings_item_data.to_dict()

                    settings.append(settings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        settings = []
        _settings = d.pop("settings", UNSET)
        for settings_item_data in _settings or []:
            settings_item = AIForgedDALViewModelsNotificationSetting.from_dict(settings_item_data)

            settings.append(settings_item)

        ai_forged_dal_view_models_notification_option = cls(
            name=name,
            settings=settings,
        )

        return ai_forged_dal_view_models_notification_option

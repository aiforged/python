from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.ai_forged_dal_notification_event import AIForgedDALNotificationEvent

T = TypeVar("T", bound="AIForgedDALViewModelsNotificationPreferencesMap")


@attr.s(auto_attribs=True)
class AIForgedDALViewModelsNotificationPreferencesMap:
    """ """

    additional_properties: Dict[str, List[AIForgedDALNotificationEvent]] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = []
            for additional_property_item_data in prop:
                additional_property_item = additional_property_item_data.value

                field_dict[prop_name].append(additional_property_item)

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ai_forged_dal_view_models_notification_preferences_map = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = []
            _additional_property = prop_dict
            for additional_property_item_data in _additional_property:
                additional_property_item = AIForgedDALNotificationEvent(additional_property_item_data)

                additional_property.append(additional_property_item)

            additional_properties[prop_name] = additional_property

        ai_forged_dal_view_models_notification_preferences_map.additional_properties = additional_properties
        return ai_forged_dal_view_models_notification_preferences_map

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> List[AIForgedDALNotificationEvent]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: List[AIForgedDALNotificationEvent]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

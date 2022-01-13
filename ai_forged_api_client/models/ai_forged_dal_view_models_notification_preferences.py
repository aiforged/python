from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.ai_forged_dal_view_models_notification_preferences_map import (
    AIForgedDALViewModelsNotificationPreferencesMap,
)
from ..models.ai_forged_dal_view_models_notification_preferences_preferences import (
    AIForgedDALViewModelsNotificationPreferencesPreferences,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AIForgedDALViewModelsNotificationPreferences")


@attr.s(auto_attribs=True)
class AIForgedDALViewModelsNotificationPreferences:
    """
    Attributes:
        preferences (Union[Unset, None, AIForgedDALViewModelsNotificationPreferencesPreferences]):
        map_ (Union[Unset, None, AIForgedDALViewModelsNotificationPreferencesMap]):
    """

    preferences: Union[Unset, None, AIForgedDALViewModelsNotificationPreferencesPreferences] = UNSET
    map_: Union[Unset, None, AIForgedDALViewModelsNotificationPreferencesMap] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        preferences: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.preferences, Unset):
            preferences = self.preferences.to_dict() if self.preferences else None

        map_: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.map_, Unset):
            map_ = self.map_.to_dict() if self.map_ else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if preferences is not UNSET:
            field_dict["preferences"] = preferences
        if map_ is not UNSET:
            field_dict["map"] = map_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _preferences = d.pop("preferences", UNSET)
        preferences: Union[Unset, None, AIForgedDALViewModelsNotificationPreferencesPreferences]
        if _preferences is None:
            preferences = None
        elif isinstance(_preferences, Unset):
            preferences = UNSET
        else:
            preferences = AIForgedDALViewModelsNotificationPreferencesPreferences.from_dict(_preferences)

        _map_ = d.pop("map", UNSET)
        map_: Union[Unset, None, AIForgedDALViewModelsNotificationPreferencesMap]
        if _map_ is None:
            map_ = None
        elif isinstance(_map_, Unset):
            map_ = UNSET
        else:
            map_ = AIForgedDALViewModelsNotificationPreferencesMap.from_dict(_map_)

        ai_forged_dal_view_models_notification_preferences = cls(
            preferences=preferences,
            map_=map_,
        )

        return ai_forged_dal_view_models_notification_preferences

from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.ai_forged_dal_notification_event import AIForgedDALNotificationEvent
from ..models.ai_forged_dal_notification_type import AIForgedDALNotificationType
from ..models.ai_forged_dal_view_models_notification_setting_contacts import (
    AIForgedDALViewModelsNotificationSettingContacts,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AIForgedDALViewModelsNotificationSetting")


@attr.s(auto_attribs=True)
class AIForgedDALViewModelsNotificationSetting:
    """
    Attributes:
        name (Union[Unset, None, str]):
        event (Union[Unset, AIForgedDALNotificationEvent]): Notification event / trigger
        type (Union[Unset, AIForgedDALNotificationType]): Notification provider type
        enabled (Union[Unset, bool]):
        contacts (Union[Unset, None, AIForgedDALViewModelsNotificationSettingContacts]):
        contact_ids (Union[Unset, None, List[int]]):
    """

    name: Union[Unset, None, str] = UNSET
    event: Union[Unset, AIForgedDALNotificationEvent] = UNSET
    type: Union[Unset, AIForgedDALNotificationType] = UNSET
    enabled: Union[Unset, bool] = UNSET
    contacts: Union[Unset, None, AIForgedDALViewModelsNotificationSettingContacts] = UNSET
    contact_ids: Union[Unset, None, List[int]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        event: Union[Unset, int] = UNSET
        if not isinstance(self.event, Unset):
            event = self.event.value

        type: Union[Unset, int] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        enabled = self.enabled
        contacts: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.contacts, Unset):
            contacts = self.contacts.to_dict() if self.contacts else None

        contact_ids: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.contact_ids, Unset):
            if self.contact_ids is None:
                contact_ids = None
            else:
                contact_ids = self.contact_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if event is not UNSET:
            field_dict["event"] = event
        if type is not UNSET:
            field_dict["type"] = type
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if contacts is not UNSET:
            field_dict["contacts"] = contacts
        if contact_ids is not UNSET:
            field_dict["contactIds"] = contact_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _event = d.pop("event", UNSET)
        event: Union[Unset, AIForgedDALNotificationEvent]
        if isinstance(_event, Unset):
            event = UNSET
        else:
            event = AIForgedDALNotificationEvent(_event)

        _type = d.pop("type", UNSET)
        type: Union[Unset, AIForgedDALNotificationType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = AIForgedDALNotificationType(_type)

        enabled = d.pop("enabled", UNSET)

        _contacts = d.pop("contacts", UNSET)
        contacts: Union[Unset, None, AIForgedDALViewModelsNotificationSettingContacts]
        if _contacts is None:
            contacts = None
        elif isinstance(_contacts, Unset):
            contacts = UNSET
        else:
            contacts = AIForgedDALViewModelsNotificationSettingContacts.from_dict(_contacts)

        contact_ids = cast(List[int], d.pop("contactIds", UNSET))

        ai_forged_dal_view_models_notification_setting = cls(
            name=name,
            event=event,
            type=type,
            enabled=enabled,
            contacts=contacts,
            contact_ids=contact_ids,
        )

        return ai_forged_dal_view_models_notification_setting

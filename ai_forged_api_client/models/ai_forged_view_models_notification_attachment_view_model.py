from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AIForgedViewModelsNotificationAttachmentViewModel")


@attr.s(auto_attribs=True)
class AIForgedViewModelsNotificationAttachmentViewModel:
    """Attachment to system notifications

    Attributes:
        id (int):
        notification_id (int):
        content_type (Union[Unset, None, str]):
        content_id (Union[Unset, None, str]):
        data (Union[Unset, None, str]):
    """

    id: int
    notification_id: int
    content_type: Union[Unset, None, str] = UNSET
    content_id: Union[Unset, None, str] = UNSET
    data: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        notification_id = self.notification_id
        content_type = self.content_type
        content_id = self.content_id
        data = self.data

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "notificationId": notification_id,
            }
        )
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if content_id is not UNSET:
            field_dict["contentId"] = content_id
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        notification_id = d.pop("notificationId")

        content_type = d.pop("contentType", UNSET)

        content_id = d.pop("contentId", UNSET)

        data = d.pop("data", UNSET)

        ai_forged_view_models_notification_attachment_view_model = cls(
            id=id,
            notification_id=notification_id,
            content_type=content_type,
            content_id=content_id,
            data=data,
        )

        return ai_forged_view_models_notification_attachment_view_model

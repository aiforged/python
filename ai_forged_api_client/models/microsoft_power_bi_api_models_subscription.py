import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.microsoft_power_bi_api_models_subscription_user import MicrosoftPowerBIApiModelsSubscriptionUser
from ..types import UNSET, Unset

T = TypeVar("T", bound="MicrosoftPowerBIApiModelsSubscription")


@attr.s(auto_attribs=True)
class MicrosoftPowerBIApiModelsSubscription:
    """
    Attributes:
        id (Union[Unset, str]):
        title (Union[Unset, None, str]):
        artifact_id (Union[Unset, None, str]):
        artifact_display_name (Union[Unset, None, str]):
        sub_artifact_display_name (Union[Unset, None, str]):
        artifact_type (Union[Unset, None, str]):
        is_enabled (Union[Unset, None, bool]):
        frequency (Union[Unset, None, str]):
        start_date (Union[Unset, None, datetime.datetime]):
        end_date (Union[Unset, None, datetime.datetime]):
        link_to_content (Union[Unset, None, bool]):
        preview_image (Union[Unset, None, bool]):
        attachment_format (Union[Unset, None, str]):
        users (Union[Unset, None, List[MicrosoftPowerBIApiModelsSubscriptionUser]]):
    """

    id: Union[Unset, str] = UNSET
    title: Union[Unset, None, str] = UNSET
    artifact_id: Union[Unset, None, str] = UNSET
    artifact_display_name: Union[Unset, None, str] = UNSET
    sub_artifact_display_name: Union[Unset, None, str] = UNSET
    artifact_type: Union[Unset, None, str] = UNSET
    is_enabled: Union[Unset, None, bool] = UNSET
    frequency: Union[Unset, None, str] = UNSET
    start_date: Union[Unset, None, datetime.datetime] = UNSET
    end_date: Union[Unset, None, datetime.datetime] = UNSET
    link_to_content: Union[Unset, None, bool] = UNSET
    preview_image: Union[Unset, None, bool] = UNSET
    attachment_format: Union[Unset, None, str] = UNSET
    users: Union[Unset, None, List[MicrosoftPowerBIApiModelsSubscriptionUser]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        title = self.title
        artifact_id = self.artifact_id
        artifact_display_name = self.artifact_display_name
        sub_artifact_display_name = self.sub_artifact_display_name
        artifact_type = self.artifact_type
        is_enabled = self.is_enabled
        frequency = self.frequency
        start_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat() if self.start_date else None

        end_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat() if self.end_date else None

        link_to_content = self.link_to_content
        preview_image = self.preview_image
        attachment_format = self.attachment_format
        users: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.users, Unset):
            if self.users is None:
                users = None
            else:
                users = []
                for users_item_data in self.users:
                    users_item = users_item_data.to_dict()

                    users.append(users_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if artifact_id is not UNSET:
            field_dict["artifactId"] = artifact_id
        if artifact_display_name is not UNSET:
            field_dict["artifactDisplayName"] = artifact_display_name
        if sub_artifact_display_name is not UNSET:
            field_dict["subArtifactDisplayName"] = sub_artifact_display_name
        if artifact_type is not UNSET:
            field_dict["artifactType"] = artifact_type
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if link_to_content is not UNSET:
            field_dict["linkToContent"] = link_to_content
        if preview_image is not UNSET:
            field_dict["previewImage"] = preview_image
        if attachment_format is not UNSET:
            field_dict["attachmentFormat"] = attachment_format
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        artifact_id = d.pop("artifactId", UNSET)

        artifact_display_name = d.pop("artifactDisplayName", UNSET)

        sub_artifact_display_name = d.pop("subArtifactDisplayName", UNSET)

        artifact_type = d.pop("artifactType", UNSET)

        is_enabled = d.pop("isEnabled", UNSET)

        frequency = d.pop("frequency", UNSET)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, None, datetime.datetime]
        if _start_date is None:
            start_date = None
        elif isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, None, datetime.datetime]
        if _end_date is None:
            end_date = None
        elif isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        link_to_content = d.pop("linkToContent", UNSET)

        preview_image = d.pop("previewImage", UNSET)

        attachment_format = d.pop("attachmentFormat", UNSET)

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = MicrosoftPowerBIApiModelsSubscriptionUser.from_dict(users_item_data)

            users.append(users_item)

        microsoft_power_bi_api_models_subscription = cls(
            id=id,
            title=title,
            artifact_id=artifact_id,
            artifact_display_name=artifact_display_name,
            sub_artifact_display_name=sub_artifact_display_name,
            artifact_type=artifact_type,
            is_enabled=is_enabled,
            frequency=frequency,
            start_date=start_date,
            end_date=end_date,
            link_to_content=link_to_content,
            preview_image=preview_image,
            attachment_format=attachment_format,
            users=users,
        )

        return microsoft_power_bi_api_models_subscription

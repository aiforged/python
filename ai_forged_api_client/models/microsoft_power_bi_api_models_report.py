from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.microsoft_power_bi_api_models_report_user import MicrosoftPowerBIApiModelsReportUser
from ..models.microsoft_power_bi_api_models_subscription import MicrosoftPowerBIApiModelsSubscription
from ..types import UNSET, Unset

T = TypeVar("T", bound="MicrosoftPowerBIApiModelsReport")


@attr.s(auto_attribs=True)
class MicrosoftPowerBIApiModelsReport:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, None, str]):
        dataset_id (Union[Unset, None, str]):
        app_id (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        report_type (Union[Unset, None, str]):
        web_url (Union[Unset, None, str]):
        embed_url (Union[Unset, None, str]):
        users (Union[Unset, None, List[MicrosoftPowerBIApiModelsReportUser]]):
        subscriptions (Union[Unset, None, List[MicrosoftPowerBIApiModelsSubscription]]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    dataset_id: Union[Unset, None, str] = UNSET
    app_id: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    report_type: Union[Unset, None, str] = UNSET
    web_url: Union[Unset, None, str] = UNSET
    embed_url: Union[Unset, None, str] = UNSET
    users: Union[Unset, None, List[MicrosoftPowerBIApiModelsReportUser]] = UNSET
    subscriptions: Union[Unset, None, List[MicrosoftPowerBIApiModelsSubscription]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        dataset_id = self.dataset_id
        app_id = self.app_id
        description = self.description
        report_type = self.report_type
        web_url = self.web_url
        embed_url = self.embed_url
        users: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.users, Unset):
            if self.users is None:
                users = None
            else:
                users = []
                for users_item_data in self.users:
                    users_item = users_item_data.to_dict()

                    users.append(users_item)

        subscriptions: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subscriptions, Unset):
            if self.subscriptions is None:
                subscriptions = None
            else:
                subscriptions = []
                for subscriptions_item_data in self.subscriptions:
                    subscriptions_item = subscriptions_item_data.to_dict()

                    subscriptions.append(subscriptions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if dataset_id is not UNSET:
            field_dict["datasetId"] = dataset_id
        if app_id is not UNSET:
            field_dict["appId"] = app_id
        if description is not UNSET:
            field_dict["description"] = description
        if report_type is not UNSET:
            field_dict["reportType"] = report_type
        if web_url is not UNSET:
            field_dict["webUrl"] = web_url
        if embed_url is not UNSET:
            field_dict["embedUrl"] = embed_url
        if users is not UNSET:
            field_dict["users"] = users
        if subscriptions is not UNSET:
            field_dict["subscriptions"] = subscriptions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        dataset_id = d.pop("datasetId", UNSET)

        app_id = d.pop("appId", UNSET)

        description = d.pop("description", UNSET)

        report_type = d.pop("reportType", UNSET)

        web_url = d.pop("webUrl", UNSET)

        embed_url = d.pop("embedUrl", UNSET)

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = MicrosoftPowerBIApiModelsReportUser.from_dict(users_item_data)

            users.append(users_item)

        subscriptions = []
        _subscriptions = d.pop("subscriptions", UNSET)
        for subscriptions_item_data in _subscriptions or []:
            subscriptions_item = MicrosoftPowerBIApiModelsSubscription.from_dict(subscriptions_item_data)

            subscriptions.append(subscriptions_item)

        microsoft_power_bi_api_models_report = cls(
            id=id,
            name=name,
            dataset_id=dataset_id,
            app_id=app_id,
            description=description,
            report_type=report_type,
            web_url=web_url,
            embed_url=embed_url,
            users=users,
            subscriptions=subscriptions,
        )

        return microsoft_power_bi_api_models_report

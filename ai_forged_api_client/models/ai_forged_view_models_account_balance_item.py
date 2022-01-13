from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AIForgedViewModelsAccountBalanceItem")


@attr.s(auto_attribs=True)
class AIForgedViewModelsAccountBalanceItem:
    """Accounting info for projects and services

    Attributes:
        id (Union[Unset, str]):
        service_id (Union[Unset, None, int]):
        service_type_id (Union[Unset, None, int]):
        project_id (Union[Unset, None, int]):
        group_id (Union[Unset, None, int]):
        bundle_id (Union[Unset, None, int]):
        user_id (Union[Unset, None, str]):
        dr_count (Union[Unset, None, float]):
        cr_count (Union[Unset, None, float]):
        dr (Union[Unset, None, float]):
        cr (Union[Unset, None, float]):
        balance (Union[Unset, None, float]):
        project (Union[Unset, None, str]):
        service (Union[Unset, None, str]):
        service_type (Union[Unset, None, str]):
        bundle (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        user_name (Union[Unset, None, str]):
    """

    id: Union[Unset, str] = UNSET
    service_id: Union[Unset, None, int] = UNSET
    service_type_id: Union[Unset, None, int] = UNSET
    project_id: Union[Unset, None, int] = UNSET
    group_id: Union[Unset, None, int] = UNSET
    bundle_id: Union[Unset, None, int] = UNSET
    user_id: Union[Unset, None, str] = UNSET
    dr_count: Union[Unset, None, float] = UNSET
    cr_count: Union[Unset, None, float] = UNSET
    dr: Union[Unset, None, float] = UNSET
    cr: Union[Unset, None, float] = UNSET
    balance: Union[Unset, None, float] = UNSET
    project: Union[Unset, None, str] = UNSET
    service: Union[Unset, None, str] = UNSET
    service_type: Union[Unset, None, str] = UNSET
    bundle: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    user_name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        service_id = self.service_id
        service_type_id = self.service_type_id
        project_id = self.project_id
        group_id = self.group_id
        bundle_id = self.bundle_id
        user_id = self.user_id
        dr_count = self.dr_count
        cr_count = self.cr_count
        dr = self.dr
        cr = self.cr
        balance = self.balance
        project = self.project
        service = self.service
        service_type = self.service_type
        bundle = self.bundle
        name = self.name
        user_name = self.user_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if service_id is not UNSET:
            field_dict["serviceId"] = service_id
        if service_type_id is not UNSET:
            field_dict["serviceTypeId"] = service_type_id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if bundle_id is not UNSET:
            field_dict["bundleId"] = bundle_id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if dr_count is not UNSET:
            field_dict["drCount"] = dr_count
        if cr_count is not UNSET:
            field_dict["crCount"] = cr_count
        if dr is not UNSET:
            field_dict["dr"] = dr
        if cr is not UNSET:
            field_dict["cr"] = cr
        if balance is not UNSET:
            field_dict["balance"] = balance
        if project is not UNSET:
            field_dict["project"] = project
        if service is not UNSET:
            field_dict["service"] = service
        if service_type is not UNSET:
            field_dict["serviceType"] = service_type
        if bundle is not UNSET:
            field_dict["bundle"] = bundle
        if name is not UNSET:
            field_dict["name"] = name
        if user_name is not UNSET:
            field_dict["userName"] = user_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        service_id = d.pop("serviceId", UNSET)

        service_type_id = d.pop("serviceTypeId", UNSET)

        project_id = d.pop("projectId", UNSET)

        group_id = d.pop("groupId", UNSET)

        bundle_id = d.pop("bundleId", UNSET)

        user_id = d.pop("userId", UNSET)

        dr_count = d.pop("drCount", UNSET)

        cr_count = d.pop("crCount", UNSET)

        dr = d.pop("dr", UNSET)

        cr = d.pop("cr", UNSET)

        balance = d.pop("balance", UNSET)

        project = d.pop("project", UNSET)

        service = d.pop("service", UNSET)

        service_type = d.pop("serviceType", UNSET)

        bundle = d.pop("bundle", UNSET)

        name = d.pop("name", UNSET)

        user_name = d.pop("userName", UNSET)

        ai_forged_view_models_account_balance_item = cls(
            id=id,
            service_id=service_id,
            service_type_id=service_type_id,
            project_id=project_id,
            group_id=group_id,
            bundle_id=bundle_id,
            user_id=user_id,
            dr_count=dr_count,
            cr_count=cr_count,
            dr=dr,
            cr=cr,
            balance=balance,
            project=project,
            service=service,
            service_type=service_type,
            bundle=bundle,
            name=name,
            user_name=user_name,
        )

        return ai_forged_view_models_account_balance_item

from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="MicrosoftPowerBIApiModelsGroup")


@attr.s(auto_attribs=True)
class MicrosoftPowerBIApiModelsGroup:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, None, str]):
        is_read_only (Union[Unset, None, bool]):
        is_on_dedicated_capacity (Union[Unset, None, bool]):
        capacity_id (Union[Unset, None, str]):
        dataflow_storage_id (Union[Unset, None, str]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    is_read_only: Union[Unset, None, bool] = UNSET
    is_on_dedicated_capacity: Union[Unset, None, bool] = UNSET
    capacity_id: Union[Unset, None, str] = UNSET
    dataflow_storage_id: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        is_read_only = self.is_read_only
        is_on_dedicated_capacity = self.is_on_dedicated_capacity
        capacity_id = self.capacity_id
        dataflow_storage_id = self.dataflow_storage_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if is_read_only is not UNSET:
            field_dict["isReadOnly"] = is_read_only
        if is_on_dedicated_capacity is not UNSET:
            field_dict["isOnDedicatedCapacity"] = is_on_dedicated_capacity
        if capacity_id is not UNSET:
            field_dict["capacityId"] = capacity_id
        if dataflow_storage_id is not UNSET:
            field_dict["dataflowStorageId"] = dataflow_storage_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        is_read_only = d.pop("isReadOnly", UNSET)

        is_on_dedicated_capacity = d.pop("isOnDedicatedCapacity", UNSET)

        capacity_id = d.pop("capacityId", UNSET)

        dataflow_storage_id = d.pop("dataflowStorageId", UNSET)

        microsoft_power_bi_api_models_group = cls(
            id=id,
            name=name,
            is_read_only=is_read_only,
            is_on_dedicated_capacity=is_on_dedicated_capacity,
            capacity_id=capacity_id,
            dataflow_storage_id=dataflow_storage_id,
        )

        return microsoft_power_bi_api_models_group

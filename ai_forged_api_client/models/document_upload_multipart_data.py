import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentUploadMultipartData")


@attr.s(auto_attribs=True)
class DocumentUploadMultipartData:
    """
    Attributes:
        data (Union[Unset, None, List[Any]]):
    """

    data: Union[Unset, None, List[Any]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, None, List[Any]] = UNSET
        if not isinstance(self.data, Unset):
            if self.data is None:
                data = None
            else:
                data = []
                for data_item_data in self.data:
                    data_item = data_item_data

                    data.append(data_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        data: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.data, Unset):
            if self.data is None:
                data = None
            else:
                _temp_data = []
                for data_item_data in self.data:
                    data_item = data_item_data

                    _temp_data.append(data_item)
                data = (None, json.dumps(_temp_data), "application/json")

        field_dict: Dict[str, Any] = {}
        field_dict.update({key: (None, str(value), "text/plain") for key, value in self.additional_properties.items()})
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = data_item_data

            data.append(data_item)

        document_upload_multipart_data = cls(
            data=data,
        )

        document_upload_multipart_data.additional_properties = d
        return document_upload_multipart_data

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

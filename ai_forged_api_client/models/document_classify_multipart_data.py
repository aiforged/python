from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="DocumentClassifyMultipartData")


@attr.s(auto_attribs=True)
class DocumentClassifyMultipartData:
    """
    Attributes:
        file (Union[Unset, None, File]):
    """

    file: Union[Unset, None, File] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        file: Union[Unset, None, FileJsonType] = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_tuple() if self.file else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file is not UNSET:
            field_dict["file"] = file

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        file: Union[Unset, None, FileJsonType] = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_tuple() if self.file else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({key: (None, str(value), "text/plain") for key, value in self.additional_properties.items()})
        field_dict.update({})
        if file is not UNSET:
            field_dict["file"] = file

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _file = d.pop("file", UNSET)
        file: Union[Unset, None, File]
        if _file is None:
            file = None
        elif isinstance(_file, Unset):
            file = UNSET
        else:
            file = File(payload=BytesIO(_file))

        document_classify_multipart_data = cls(
            file=file,
        )

        document_classify_multipart_data.additional_properties = d
        return document_classify_multipart_data

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

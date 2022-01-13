from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="MicrosoftAspNetCoreJsonPatchOperationsOperationBase")


@attr.s(auto_attribs=True)
class MicrosoftAspNetCoreJsonPatchOperationsOperationBase:
    """
    Attributes:
        path (Union[Unset, None, str]):
        op (Union[Unset, None, str]):
        from_ (Union[Unset, None, str]):
    """

    path: Union[Unset, None, str] = UNSET
    op: Union[Unset, None, str] = UNSET
    from_: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        path = self.path
        op = self.op
        from_ = self.from_

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if op is not UNSET:
            field_dict["op"] = op
        if from_ is not UNSET:
            field_dict["from"] = from_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        path = d.pop("path", UNSET)

        op = d.pop("op", UNSET)

        from_ = d.pop("from", UNSET)

        microsoft_asp_net_core_json_patch_operations_operation_base = cls(
            path=path,
            op=op,
            from_=from_,
        )

        return microsoft_asp_net_core_json_patch_operations_operation_base

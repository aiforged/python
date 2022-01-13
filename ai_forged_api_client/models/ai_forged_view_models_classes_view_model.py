import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.ai_forged_dal_class_type import AIForgedDALClassType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AIForgedViewModelsClassesViewModel")


@attr.s(auto_attribs=True)
class AIForgedViewModelsClassesViewModel:
    """Categories/Classes for training and classification

    Attributes:
        id (Union[Unset, int]):
        user_id (Union[Unset, None, str]):
        project_id (Union[Unset, int]):
        name (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        comment (Union[Unset, None, str]):
        dtc (Union[Unset, datetime.datetime]):
        dtm (Union[Unset, datetime.datetime]):
        type (Union[Unset, None, AIForgedDALClassType]): System category type
        related (Union[Unset, None, int]):
    """

    id: Union[Unset, int] = UNSET
    user_id: Union[Unset, None, str] = UNSET
    project_id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    comment: Union[Unset, None, str] = UNSET
    dtc: Union[Unset, datetime.datetime] = UNSET
    dtm: Union[Unset, datetime.datetime] = UNSET
    type: Union[Unset, None, AIForgedDALClassType] = UNSET
    related: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        user_id = self.user_id
        project_id = self.project_id
        name = self.name
        description = self.description
        comment = self.comment
        dtc: Union[Unset, str] = UNSET
        if not isinstance(self.dtc, Unset):
            dtc = self.dtc.isoformat()

        dtm: Union[Unset, str] = UNSET
        if not isinstance(self.dtm, Unset):
            dtm = self.dtm.isoformat()

        type: Union[Unset, None, int] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value if self.type else None

        related = self.related

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if comment is not UNSET:
            field_dict["comment"] = comment
        if dtc is not UNSET:
            field_dict["dtc"] = dtc
        if dtm is not UNSET:
            field_dict["dtm"] = dtm
        if type is not UNSET:
            field_dict["type"] = type
        if related is not UNSET:
            field_dict["related"] = related

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        user_id = d.pop("userId", UNSET)

        project_id = d.pop("projectId", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        comment = d.pop("comment", UNSET)

        _dtc = d.pop("dtc", UNSET)
        dtc: Union[Unset, datetime.datetime]
        if isinstance(_dtc, Unset):
            dtc = UNSET
        else:
            dtc = isoparse(_dtc)

        _dtm = d.pop("dtm", UNSET)
        dtm: Union[Unset, datetime.datetime]
        if isinstance(_dtm, Unset):
            dtm = UNSET
        else:
            dtm = isoparse(_dtm)

        _type = d.pop("type", UNSET)
        type: Union[Unset, None, AIForgedDALClassType]
        if _type is None:
            type = None
        elif isinstance(_type, Unset):
            type = UNSET
        else:
            type = AIForgedDALClassType(_type)

        related = d.pop("related", UNSET)

        ai_forged_view_models_classes_view_model = cls(
            id=id,
            user_id=user_id,
            project_id=project_id,
            name=name,
            description=description,
            comment=comment,
            dtc=dtc,
            dtm=dtm,
            type=type,
            related=related,
        )

        return ai_forged_view_models_classes_view_model

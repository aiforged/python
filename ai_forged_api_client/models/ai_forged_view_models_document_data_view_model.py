from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.ai_forged_dal_availability import AIForgedDALAvailability
from ..models.ai_forged_dal_document_data_type import AIForgedDALDocumentDataType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AIForgedViewModelsDocumentDataViewModel")


@attr.s(auto_attribs=True)
class AIForgedViewModelsDocumentDataViewModel:
    """Document blob data

    Attributes:
        id (Union[Unset, int]):
        document_id (Union[Unset, int]):
        blob_id (Union[Unset, None, int]):
        type (Union[Unset, None, AIForgedDALDocumentDataType]): Indicate the type of data related to a document
        data (Union[Unset, None, str]):
        preview (Union[Unset, None, str]):
        text (Union[Unset, None, str]):
        info (Union[Unset, None, str]):
        content_type (Union[Unset, None, str]):
        result_id (Union[Unset, None, str]):
        index (Union[Unset, None, int]):
        width (Union[Unset, None, float]):
        height (Union[Unset, None, float]):
        resolution (Union[Unset, None, float]):
        availability (Union[Unset, None, AIForgedDALAvailability]): Avalability of a record
    """

    id: Union[Unset, int] = UNSET
    document_id: Union[Unset, int] = UNSET
    blob_id: Union[Unset, None, int] = UNSET
    type: Union[Unset, None, AIForgedDALDocumentDataType] = UNSET
    data: Union[Unset, None, str] = UNSET
    preview: Union[Unset, None, str] = UNSET
    text: Union[Unset, None, str] = UNSET
    info: Union[Unset, None, str] = UNSET
    content_type: Union[Unset, None, str] = UNSET
    result_id: Union[Unset, None, str] = UNSET
    index: Union[Unset, None, int] = UNSET
    width: Union[Unset, None, float] = UNSET
    height: Union[Unset, None, float] = UNSET
    resolution: Union[Unset, None, float] = UNSET
    availability: Union[Unset, None, AIForgedDALAvailability] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        document_id = self.document_id
        blob_id = self.blob_id
        type: Union[Unset, None, int] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value if self.type else None

        data = self.data
        preview = self.preview
        text = self.text
        info = self.info
        content_type = self.content_type
        result_id = self.result_id
        index = self.index
        width = self.width
        height = self.height
        resolution = self.resolution
        availability: Union[Unset, None, int] = UNSET
        if not isinstance(self.availability, Unset):
            availability = self.availability.value if self.availability else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if blob_id is not UNSET:
            field_dict["blobId"] = blob_id
        if type is not UNSET:
            field_dict["type"] = type
        if data is not UNSET:
            field_dict["data"] = data
        if preview is not UNSET:
            field_dict["preview"] = preview
        if text is not UNSET:
            field_dict["text"] = text
        if info is not UNSET:
            field_dict["info"] = info
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if result_id is not UNSET:
            field_dict["resultId"] = result_id
        if index is not UNSET:
            field_dict["index"] = index
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if availability is not UNSET:
            field_dict["availability"] = availability

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        document_id = d.pop("documentId", UNSET)

        blob_id = d.pop("blobId", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, None, AIForgedDALDocumentDataType]
        if _type is None:
            type = None
        elif isinstance(_type, Unset):
            type = UNSET
        else:
            type = AIForgedDALDocumentDataType(_type)

        data = d.pop("data", UNSET)

        preview = d.pop("preview", UNSET)

        text = d.pop("text", UNSET)

        info = d.pop("info", UNSET)

        content_type = d.pop("contentType", UNSET)

        result_id = d.pop("resultId", UNSET)

        index = d.pop("index", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        resolution = d.pop("resolution", UNSET)

        _availability = d.pop("availability", UNSET)
        availability: Union[Unset, None, AIForgedDALAvailability]
        if _availability is None:
            availability = None
        elif isinstance(_availability, Unset):
            availability = UNSET
        else:
            availability = AIForgedDALAvailability(_availability)

        ai_forged_view_models_document_data_view_model = cls(
            id=id,
            document_id=document_id,
            blob_id=blob_id,
            type=type,
            data=data,
            preview=preview,
            text=text,
            info=info,
            content_type=content_type,
            result_id=result_id,
            index=index,
            width=width,
            height=height,
            resolution=resolution,
            availability=availability,
        )

        return ai_forged_view_models_document_data_view_model

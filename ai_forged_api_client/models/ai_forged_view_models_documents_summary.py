import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.ai_forged_dal_document_status import AIForgedDALDocumentStatus
from ..models.ai_forged_dal_usage_type import AIForgedDALUsageType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AIForgedViewModelsDocumentsSummary")


@attr.s(auto_attribs=True)
class AIForgedViewModelsDocumentsSummary:
    """Document summary for statistics

    Attributes:
        project_id (Union[Unset, None, int]):
        service_type (Union[Unset, int]):
        service_id (Union[Unset, int]):
        usage (Union[Unset, AIForgedDALUsageType]): Why do we store this document
        status (Union[Unset, AIForgedDALDocumentStatus]): Indicate the status of a document in the system
        name (Union[Unset, None, str]):
        class_id (Union[Unset, None, int]):
        class_name (Union[Unset, None, str]):
        service_name (Union[Unset, None, str]):
        file_type (Union[Unset, None, str]):
        dt (Union[Unset, None, datetime.datetime]):
        count (Union[Unset, int]):
        labelled_count (Union[Unset, None, int]):
    """

    project_id: Union[Unset, None, int] = UNSET
    service_type: Union[Unset, int] = UNSET
    service_id: Union[Unset, int] = UNSET
    usage: Union[Unset, AIForgedDALUsageType] = UNSET
    status: Union[Unset, AIForgedDALDocumentStatus] = UNSET
    name: Union[Unset, None, str] = UNSET
    class_id: Union[Unset, None, int] = UNSET
    class_name: Union[Unset, None, str] = UNSET
    service_name: Union[Unset, None, str] = UNSET
    file_type: Union[Unset, None, str] = UNSET
    dt: Union[Unset, None, datetime.datetime] = UNSET
    count: Union[Unset, int] = UNSET
    labelled_count: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        project_id = self.project_id
        service_type = self.service_type
        service_id = self.service_id
        usage: Union[Unset, int] = UNSET
        if not isinstance(self.usage, Unset):
            usage = self.usage.value

        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        name = self.name
        class_id = self.class_id
        class_name = self.class_name
        service_name = self.service_name
        file_type = self.file_type
        dt: Union[Unset, None, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat() if self.dt else None

        count = self.count
        labelled_count = self.labelled_count

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if service_type is not UNSET:
            field_dict["serviceType"] = service_type
        if service_id is not UNSET:
            field_dict["serviceId"] = service_id
        if usage is not UNSET:
            field_dict["usage"] = usage
        if status is not UNSET:
            field_dict["status"] = status
        if name is not UNSET:
            field_dict["name"] = name
        if class_id is not UNSET:
            field_dict["classId"] = class_id
        if class_name is not UNSET:
            field_dict["className"] = class_name
        if service_name is not UNSET:
            field_dict["serviceName"] = service_name
        if file_type is not UNSET:
            field_dict["fileType"] = file_type
        if dt is not UNSET:
            field_dict["dt"] = dt
        if count is not UNSET:
            field_dict["count"] = count
        if labelled_count is not UNSET:
            field_dict["labelledCount"] = labelled_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        project_id = d.pop("projectId", UNSET)

        service_type = d.pop("serviceType", UNSET)

        service_id = d.pop("serviceId", UNSET)

        _usage = d.pop("usage", UNSET)
        usage: Union[Unset, AIForgedDALUsageType]
        if isinstance(_usage, Unset):
            usage = UNSET
        else:
            usage = AIForgedDALUsageType(_usage)

        _status = d.pop("status", UNSET)
        status: Union[Unset, AIForgedDALDocumentStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AIForgedDALDocumentStatus(_status)

        name = d.pop("name", UNSET)

        class_id = d.pop("classId", UNSET)

        class_name = d.pop("className", UNSET)

        service_name = d.pop("serviceName", UNSET)

        file_type = d.pop("fileType", UNSET)

        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, None, datetime.datetime]
        if _dt is None:
            dt = None
        elif isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        count = d.pop("count", UNSET)

        labelled_count = d.pop("labelledCount", UNSET)

        ai_forged_view_models_documents_summary = cls(
            project_id=project_id,
            service_type=service_type,
            service_id=service_id,
            usage=usage,
            status=status,
            name=name,
            class_id=class_id,
            class_name=class_name,
            service_name=service_name,
            file_type=file_type,
            dt=dt,
            count=count,
            labelled_count=labelled_count,
        )

        return ai_forged_view_models_documents_summary

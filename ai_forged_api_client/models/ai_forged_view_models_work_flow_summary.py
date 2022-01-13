import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.ai_forged_dal_document_status import AIForgedDALDocumentStatus
from ..models.ai_forged_dal_usage_type import AIForgedDALUsageType
from ..models.ai_forged_dal_work_item_action import AIForgedDALWorkItemAction
from ..models.ai_forged_dal_work_item_method import AIForgedDALWorkItemMethod
from ..models.ai_forged_dal_work_item_status import AIForgedDALWorkItemStatus
from ..models.ai_forged_dal_work_item_type import AIForgedDALWorkItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AIForgedViewModelsWorkFlowSummary")


@attr.s(auto_attribs=True)
class AIForgedViewModelsWorkFlowSummary:
    """Workflow summary for statistics

    Attributes:
        project_id (Union[Unset, None, int]):
        user_id (Union[Unset, None, str]):
        user_name (Union[Unset, None, str]):
        service_id (Union[Unset, None, int]):
        def_id (Union[Unset, None, int]):
        doc_id (Union[Unset, None, int]):
        filename (Union[Unset, None, str]):
        doc_status (Union[Unset, None, AIForgedDALDocumentStatus]): Indicate the status of a document in the system
        doc_usage (Union[Unset, None, AIForgedDALUsageType]): Why do we store this document
        doc_class_id (Union[Unset, None, int]):
        doc_class_name (Union[Unset, None, str]):
        action (Union[Unset, AIForgedDALWorkItemAction]): Actount for work item
        type (Union[Unset, AIForgedDALWorkItemType]): Type of work item
        status (Union[Unset, AIForgedDALWorkItemStatus]): Work item status
        method (Union[Unset, None, AIForgedDALWorkItemMethod]): Work items assignment method
        dt (Union[Unset, None, datetime.datetime]):
        duration (Union[Unset, None, str]):
        active_duration (Union[Unset, None, str]):
        count (Union[Unset, int]):
    """

    project_id: Union[Unset, None, int] = UNSET
    user_id: Union[Unset, None, str] = UNSET
    user_name: Union[Unset, None, str] = UNSET
    service_id: Union[Unset, None, int] = UNSET
    def_id: Union[Unset, None, int] = UNSET
    doc_id: Union[Unset, None, int] = UNSET
    filename: Union[Unset, None, str] = UNSET
    doc_status: Union[Unset, None, AIForgedDALDocumentStatus] = UNSET
    doc_usage: Union[Unset, None, AIForgedDALUsageType] = UNSET
    doc_class_id: Union[Unset, None, int] = UNSET
    doc_class_name: Union[Unset, None, str] = UNSET
    action: Union[Unset, AIForgedDALWorkItemAction] = UNSET
    type: Union[Unset, AIForgedDALWorkItemType] = UNSET
    status: Union[Unset, AIForgedDALWorkItemStatus] = UNSET
    method: Union[Unset, None, AIForgedDALWorkItemMethod] = UNSET
    dt: Union[Unset, None, datetime.datetime] = UNSET
    duration: Union[Unset, None, str] = UNSET
    active_duration: Union[Unset, None, str] = UNSET
    count: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        project_id = self.project_id
        user_id = self.user_id
        user_name = self.user_name
        service_id = self.service_id
        def_id = self.def_id
        doc_id = self.doc_id
        filename = self.filename
        doc_status: Union[Unset, None, int] = UNSET
        if not isinstance(self.doc_status, Unset):
            doc_status = self.doc_status.value if self.doc_status else None

        doc_usage: Union[Unset, None, int] = UNSET
        if not isinstance(self.doc_usage, Unset):
            doc_usage = self.doc_usage.value if self.doc_usage else None

        doc_class_id = self.doc_class_id
        doc_class_name = self.doc_class_name
        action: Union[Unset, int] = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value

        type: Union[Unset, int] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        method: Union[Unset, None, int] = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value if self.method else None

        dt: Union[Unset, None, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat() if self.dt else None

        duration = self.duration
        active_duration = self.active_duration
        count = self.count

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if service_id is not UNSET:
            field_dict["serviceId"] = service_id
        if def_id is not UNSET:
            field_dict["defId"] = def_id
        if doc_id is not UNSET:
            field_dict["docId"] = doc_id
        if filename is not UNSET:
            field_dict["filename"] = filename
        if doc_status is not UNSET:
            field_dict["docStatus"] = doc_status
        if doc_usage is not UNSET:
            field_dict["docUsage"] = doc_usage
        if doc_class_id is not UNSET:
            field_dict["docClassId"] = doc_class_id
        if doc_class_name is not UNSET:
            field_dict["docClassName"] = doc_class_name
        if action is not UNSET:
            field_dict["action"] = action
        if type is not UNSET:
            field_dict["type"] = type
        if status is not UNSET:
            field_dict["status"] = status
        if method is not UNSET:
            field_dict["method"] = method
        if dt is not UNSET:
            field_dict["dt"] = dt
        if duration is not UNSET:
            field_dict["duration"] = duration
        if active_duration is not UNSET:
            field_dict["activeDuration"] = active_duration
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        project_id = d.pop("projectId", UNSET)

        user_id = d.pop("userId", UNSET)

        user_name = d.pop("userName", UNSET)

        service_id = d.pop("serviceId", UNSET)

        def_id = d.pop("defId", UNSET)

        doc_id = d.pop("docId", UNSET)

        filename = d.pop("filename", UNSET)

        _doc_status = d.pop("docStatus", UNSET)
        doc_status: Union[Unset, None, AIForgedDALDocumentStatus]
        if _doc_status is None:
            doc_status = None
        elif isinstance(_doc_status, Unset):
            doc_status = UNSET
        else:
            doc_status = AIForgedDALDocumentStatus(_doc_status)

        _doc_usage = d.pop("docUsage", UNSET)
        doc_usage: Union[Unset, None, AIForgedDALUsageType]
        if _doc_usage is None:
            doc_usage = None
        elif isinstance(_doc_usage, Unset):
            doc_usage = UNSET
        else:
            doc_usage = AIForgedDALUsageType(_doc_usage)

        doc_class_id = d.pop("docClassId", UNSET)

        doc_class_name = d.pop("docClassName", UNSET)

        _action = d.pop("action", UNSET)
        action: Union[Unset, AIForgedDALWorkItemAction]
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = AIForgedDALWorkItemAction(_action)

        _type = d.pop("type", UNSET)
        type: Union[Unset, AIForgedDALWorkItemType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = AIForgedDALWorkItemType(_type)

        _status = d.pop("status", UNSET)
        status: Union[Unset, AIForgedDALWorkItemStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AIForgedDALWorkItemStatus(_status)

        _method = d.pop("method", UNSET)
        method: Union[Unset, None, AIForgedDALWorkItemMethod]
        if _method is None:
            method = None
        elif isinstance(_method, Unset):
            method = UNSET
        else:
            method = AIForgedDALWorkItemMethod(_method)

        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, None, datetime.datetime]
        if _dt is None:
            dt = None
        elif isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        duration = d.pop("duration", UNSET)

        active_duration = d.pop("activeDuration", UNSET)

        count = d.pop("count", UNSET)

        ai_forged_view_models_work_flow_summary = cls(
            project_id=project_id,
            user_id=user_id,
            user_name=user_name,
            service_id=service_id,
            def_id=def_id,
            doc_id=doc_id,
            filename=filename,
            doc_status=doc_status,
            doc_usage=doc_usage,
            doc_class_id=doc_class_id,
            doc_class_name=doc_class_name,
            action=action,
            type=type,
            status=status,
            method=method,
            dt=dt,
            duration=duration,
            active_duration=active_duration,
            count=count,
        )

        return ai_forged_view_models_work_flow_summary

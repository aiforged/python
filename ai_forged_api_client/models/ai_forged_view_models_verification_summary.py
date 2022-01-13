import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.ai_forged_dal_document_status import AIForgedDALDocumentStatus
from ..models.ai_forged_dal_usage_type import AIForgedDALUsageType
from ..models.ai_forged_dal_verification_status import AIForgedDALVerificationStatus
from ..models.ai_forged_dal_verification_type import AIForgedDALVerificationType
from ..models.system_day_of_week import SystemDayOfWeek
from ..types import UNSET, Unset

T = TypeVar("T", bound="AIForgedViewModelsVerificationSummary")


@attr.s(auto_attribs=True)
class AIForgedViewModelsVerificationSummary:
    """System and user verification info for fields on documents

    Attributes:
        id (int):
        parameter_id (int):
        user_id (Union[Unset, None, str]):
        value (Union[Unset, None, str]):
        dt (Union[Unset, datetime.datetime]):
        confidence (Union[Unset, None, float]):
        symbols_confidence (Union[Unset, None, str]):
        type (Union[Unset, AIForgedDALVerificationType]): Type of verification
        status (Union[Unset, AIForgedDALVerificationStatus]): Verification status flags
        result (Union[Unset, None, str]):
        box (Union[Unset, None, str]):
        info (Union[Unset, None, str]):
        data (Union[Unset, None, str]):
        user_name (Union[Unset, None, str]):
        service_id (Union[Unset, None, int]):
        service_doc_id (Union[Unset, None, int]):
        provider (Union[Unset, None, str]):
        setting_id (Union[Unset, None, int]):
        work_item (Union[Unset, None, int]):
        transaction_id (Union[Unset, None, int]):
        charge (Union[Unset, float]):
        param_def_id (Union[Unset, int]):
        param_def_name (Union[Unset, None, str]):
        project_id (Union[Unset, int]):
        project_name (Union[Unset, None, str]):
        doc_id (Union[Unset, int]):
        doc_file_name (Union[Unset, None, str]):
        doc_content_type (Union[Unset, None, str]):
        doc_usage (Union[Unset, None, AIForgedDALUsageType]): Why do we store this document
        doc_status (Union[Unset, None, AIForgedDALDocumentStatus]): Indicate the status of a document in the system
        class_id (Union[Unset, None, int]):
        class_name (Union[Unset, None, str]):
        year (Union[Unset, int]):
        month (Union[Unset, int]):
        day (Union[Unset, int]):
        day_of_week (Union[Unset, SystemDayOfWeek]):
        count (Union[Unset, int]):
        average (Union[Unset, None, float]):
        min_ (Union[Unset, None, float]):
        max_ (Union[Unset, None, float]):
    """

    id: int
    parameter_id: int
    user_id: Union[Unset, None, str] = UNSET
    value: Union[Unset, None, str] = UNSET
    dt: Union[Unset, datetime.datetime] = UNSET
    confidence: Union[Unset, None, float] = UNSET
    symbols_confidence: Union[Unset, None, str] = UNSET
    type: Union[Unset, AIForgedDALVerificationType] = UNSET
    status: Union[Unset, AIForgedDALVerificationStatus] = UNSET
    result: Union[Unset, None, str] = UNSET
    box: Union[Unset, None, str] = UNSET
    info: Union[Unset, None, str] = UNSET
    data: Union[Unset, None, str] = UNSET
    user_name: Union[Unset, None, str] = UNSET
    service_id: Union[Unset, None, int] = UNSET
    service_doc_id: Union[Unset, None, int] = UNSET
    provider: Union[Unset, None, str] = UNSET
    setting_id: Union[Unset, None, int] = UNSET
    work_item: Union[Unset, None, int] = UNSET
    transaction_id: Union[Unset, None, int] = UNSET
    charge: Union[Unset, float] = UNSET
    param_def_id: Union[Unset, int] = UNSET
    param_def_name: Union[Unset, None, str] = UNSET
    project_id: Union[Unset, int] = UNSET
    project_name: Union[Unset, None, str] = UNSET
    doc_id: Union[Unset, int] = UNSET
    doc_file_name: Union[Unset, None, str] = UNSET
    doc_content_type: Union[Unset, None, str] = UNSET
    doc_usage: Union[Unset, None, AIForgedDALUsageType] = UNSET
    doc_status: Union[Unset, None, AIForgedDALDocumentStatus] = UNSET
    class_id: Union[Unset, None, int] = UNSET
    class_name: Union[Unset, None, str] = UNSET
    year: Union[Unset, int] = UNSET
    month: Union[Unset, int] = UNSET
    day: Union[Unset, int] = UNSET
    day_of_week: Union[Unset, SystemDayOfWeek] = UNSET
    count: Union[Unset, int] = UNSET
    average: Union[Unset, None, float] = UNSET
    min_: Union[Unset, None, float] = UNSET
    max_: Union[Unset, None, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        parameter_id = self.parameter_id
        user_id = self.user_id
        value = self.value
        dt: Union[Unset, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat()

        confidence = self.confidence
        symbols_confidence = self.symbols_confidence
        type: Union[Unset, int] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        result = self.result
        box = self.box
        info = self.info
        data = self.data
        user_name = self.user_name
        service_id = self.service_id
        service_doc_id = self.service_doc_id
        provider = self.provider
        setting_id = self.setting_id
        work_item = self.work_item
        transaction_id = self.transaction_id
        charge = self.charge
        param_def_id = self.param_def_id
        param_def_name = self.param_def_name
        project_id = self.project_id
        project_name = self.project_name
        doc_id = self.doc_id
        doc_file_name = self.doc_file_name
        doc_content_type = self.doc_content_type
        doc_usage: Union[Unset, None, int] = UNSET
        if not isinstance(self.doc_usage, Unset):
            doc_usage = self.doc_usage.value if self.doc_usage else None

        doc_status: Union[Unset, None, int] = UNSET
        if not isinstance(self.doc_status, Unset):
            doc_status = self.doc_status.value if self.doc_status else None

        class_id = self.class_id
        class_name = self.class_name
        year = self.year
        month = self.month
        day = self.day
        day_of_week: Union[Unset, int] = UNSET
        if not isinstance(self.day_of_week, Unset):
            day_of_week = self.day_of_week.value

        count = self.count
        average = self.average
        min_ = self.min_
        max_ = self.max_

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "parameterId": parameter_id,
            }
        )
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if value is not UNSET:
            field_dict["value"] = value
        if dt is not UNSET:
            field_dict["dt"] = dt
        if confidence is not UNSET:
            field_dict["confidence"] = confidence
        if symbols_confidence is not UNSET:
            field_dict["symbolsConfidence"] = symbols_confidence
        if type is not UNSET:
            field_dict["type"] = type
        if status is not UNSET:
            field_dict["status"] = status
        if result is not UNSET:
            field_dict["result"] = result
        if box is not UNSET:
            field_dict["box"] = box
        if info is not UNSET:
            field_dict["info"] = info
        if data is not UNSET:
            field_dict["data"] = data
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if service_id is not UNSET:
            field_dict["serviceId"] = service_id
        if service_doc_id is not UNSET:
            field_dict["serviceDocId"] = service_doc_id
        if provider is not UNSET:
            field_dict["provider"] = provider
        if setting_id is not UNSET:
            field_dict["settingId"] = setting_id
        if work_item is not UNSET:
            field_dict["workItem"] = work_item
        if transaction_id is not UNSET:
            field_dict["transactionId"] = transaction_id
        if charge is not UNSET:
            field_dict["charge"] = charge
        if param_def_id is not UNSET:
            field_dict["paramDefId"] = param_def_id
        if param_def_name is not UNSET:
            field_dict["paramDefName"] = param_def_name
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if project_name is not UNSET:
            field_dict["projectName"] = project_name
        if doc_id is not UNSET:
            field_dict["docId"] = doc_id
        if doc_file_name is not UNSET:
            field_dict["docFileName"] = doc_file_name
        if doc_content_type is not UNSET:
            field_dict["docContentType"] = doc_content_type
        if doc_usage is not UNSET:
            field_dict["docUsage"] = doc_usage
        if doc_status is not UNSET:
            field_dict["docStatus"] = doc_status
        if class_id is not UNSET:
            field_dict["classId"] = class_id
        if class_name is not UNSET:
            field_dict["className"] = class_name
        if year is not UNSET:
            field_dict["year"] = year
        if month is not UNSET:
            field_dict["month"] = month
        if day is not UNSET:
            field_dict["day"] = day
        if day_of_week is not UNSET:
            field_dict["dayOfWeek"] = day_of_week
        if count is not UNSET:
            field_dict["count"] = count
        if average is not UNSET:
            field_dict["average"] = average
        if min_ is not UNSET:
            field_dict["min"] = min_
        if max_ is not UNSET:
            field_dict["max"] = max_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        parameter_id = d.pop("parameterId")

        user_id = d.pop("userId", UNSET)

        value = d.pop("value", UNSET)

        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, datetime.datetime]
        if isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        confidence = d.pop("confidence", UNSET)

        symbols_confidence = d.pop("symbolsConfidence", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, AIForgedDALVerificationType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = AIForgedDALVerificationType(_type)

        _status = d.pop("status", UNSET)
        status: Union[Unset, AIForgedDALVerificationStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AIForgedDALVerificationStatus(_status)

        result = d.pop("result", UNSET)

        box = d.pop("box", UNSET)

        info = d.pop("info", UNSET)

        data = d.pop("data", UNSET)

        user_name = d.pop("userName", UNSET)

        service_id = d.pop("serviceId", UNSET)

        service_doc_id = d.pop("serviceDocId", UNSET)

        provider = d.pop("provider", UNSET)

        setting_id = d.pop("settingId", UNSET)

        work_item = d.pop("workItem", UNSET)

        transaction_id = d.pop("transactionId", UNSET)

        charge = d.pop("charge", UNSET)

        param_def_id = d.pop("paramDefId", UNSET)

        param_def_name = d.pop("paramDefName", UNSET)

        project_id = d.pop("projectId", UNSET)

        project_name = d.pop("projectName", UNSET)

        doc_id = d.pop("docId", UNSET)

        doc_file_name = d.pop("docFileName", UNSET)

        doc_content_type = d.pop("docContentType", UNSET)

        _doc_usage = d.pop("docUsage", UNSET)
        doc_usage: Union[Unset, None, AIForgedDALUsageType]
        if _doc_usage is None:
            doc_usage = None
        elif isinstance(_doc_usage, Unset):
            doc_usage = UNSET
        else:
            doc_usage = AIForgedDALUsageType(_doc_usage)

        _doc_status = d.pop("docStatus", UNSET)
        doc_status: Union[Unset, None, AIForgedDALDocumentStatus]
        if _doc_status is None:
            doc_status = None
        elif isinstance(_doc_status, Unset):
            doc_status = UNSET
        else:
            doc_status = AIForgedDALDocumentStatus(_doc_status)

        class_id = d.pop("classId", UNSET)

        class_name = d.pop("className", UNSET)

        year = d.pop("year", UNSET)

        month = d.pop("month", UNSET)

        day = d.pop("day", UNSET)

        _day_of_week = d.pop("dayOfWeek", UNSET)
        day_of_week: Union[Unset, SystemDayOfWeek]
        if isinstance(_day_of_week, Unset):
            day_of_week = UNSET
        else:
            day_of_week = SystemDayOfWeek(_day_of_week)

        count = d.pop("count", UNSET)

        average = d.pop("average", UNSET)

        min_ = d.pop("min", UNSET)

        max_ = d.pop("max", UNSET)

        ai_forged_view_models_verification_summary = cls(
            id=id,
            parameter_id=parameter_id,
            user_id=user_id,
            value=value,
            dt=dt,
            confidence=confidence,
            symbols_confidence=symbols_confidence,
            type=type,
            status=status,
            result=result,
            box=box,
            info=info,
            data=data,
            user_name=user_name,
            service_id=service_id,
            service_doc_id=service_doc_id,
            provider=provider,
            setting_id=setting_id,
            work_item=work_item,
            transaction_id=transaction_id,
            charge=charge,
            param_def_id=param_def_id,
            param_def_name=param_def_name,
            project_id=project_id,
            project_name=project_name,
            doc_id=doc_id,
            doc_file_name=doc_file_name,
            doc_content_type=doc_content_type,
            doc_usage=doc_usage,
            doc_status=doc_status,
            class_id=class_id,
            class_name=class_name,
            year=year,
            month=month,
            day=day,
            day_of_week=day_of_week,
            count=count,
            average=average,
            min_=min_,
            max_=max_,
        )

        return ai_forged_view_models_verification_summary

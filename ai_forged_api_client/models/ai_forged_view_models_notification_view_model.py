import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.ai_forged_dal_notification_area import AIForgedDALNotificationArea
from ..models.ai_forged_dal_notification_event import AIForgedDALNotificationEvent
from ..models.ai_forged_dal_notification_level import AIForgedDALNotificationLevel
from ..models.ai_forged_dal_notification_status import AIForgedDALNotificationStatus
from ..models.ai_forged_dal_notification_type import AIForgedDALNotificationType
from ..models.ai_forged_view_models_contact_view_model import AIForgedViewModelsContactViewModel
from ..models.ai_forged_view_models_notification_attachment_view_model import (
    AIForgedViewModelsNotificationAttachmentViewModel,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AIForgedViewModelsNotificationViewModel")


@attr.s(auto_attribs=True)
class AIForgedViewModelsNotificationViewModel:
    """System Notifications

    Attributes:
        id (int):
        user_id (str):
        project_id (Union[Unset, None, int]):
        class_id (Union[Unset, None, int]):
        service_id (Union[Unset, None, int]):
        document_id (Union[Unset, None, int]):
        work_item_id (Union[Unset, None, int]):
        shred_id (Union[Unset, None, int]):
        verification_id (Union[Unset, None, int]):
        contact_id (Union[Unset, None, int]):
        type (Union[Unset, AIForgedDALNotificationType]): Notification provider type
        status (Union[Unset, AIForgedDALNotificationStatus]): Notification status
        area (Union[Unset, AIForgedDALNotificationArea]): Area of notification
        event (Union[Unset, AIForgedDALNotificationEvent]): Notification event / trigger
        level (Union[Unset, AIForgedDALNotificationLevel]): Notification level
        to (Union[Unset, None, str]):
        address (Union[Unset, None, str]):
        subject (Union[Unset, None, str]):
        content_type (Union[Unset, None, str]):
        body (Union[Unset, None, str]):
        error (Union[Unset, None, str]):
        dtc (Union[Unset, datetime.datetime]):
        dtm (Union[Unset, datetime.datetime]):
        sent (Union[Unset, None, datetime.datetime]):
        delivered (Union[Unset, None, datetime.datetime]):
        read_date (Union[Unset, None, datetime.datetime]):
        contact (Union[Unset, None, AIForgedViewModelsContactViewModel]):
        attachments (Union[Unset, None, List[AIForgedViewModelsNotificationAttachmentViewModel]]):
    """

    id: int
    user_id: str
    project_id: Union[Unset, None, int] = UNSET
    class_id: Union[Unset, None, int] = UNSET
    service_id: Union[Unset, None, int] = UNSET
    document_id: Union[Unset, None, int] = UNSET
    work_item_id: Union[Unset, None, int] = UNSET
    shred_id: Union[Unset, None, int] = UNSET
    verification_id: Union[Unset, None, int] = UNSET
    contact_id: Union[Unset, None, int] = UNSET
    type: Union[Unset, AIForgedDALNotificationType] = UNSET
    status: Union[Unset, AIForgedDALNotificationStatus] = UNSET
    area: Union[Unset, AIForgedDALNotificationArea] = UNSET
    event: Union[Unset, AIForgedDALNotificationEvent] = UNSET
    level: Union[Unset, AIForgedDALNotificationLevel] = UNSET
    to: Union[Unset, None, str] = UNSET
    address: Union[Unset, None, str] = UNSET
    subject: Union[Unset, None, str] = UNSET
    content_type: Union[Unset, None, str] = UNSET
    body: Union[Unset, None, str] = UNSET
    error: Union[Unset, None, str] = UNSET
    dtc: Union[Unset, datetime.datetime] = UNSET
    dtm: Union[Unset, datetime.datetime] = UNSET
    sent: Union[Unset, None, datetime.datetime] = UNSET
    delivered: Union[Unset, None, datetime.datetime] = UNSET
    read_date: Union[Unset, None, datetime.datetime] = UNSET
    contact: Union[Unset, None, AIForgedViewModelsContactViewModel] = UNSET
    attachments: Union[Unset, None, List[AIForgedViewModelsNotificationAttachmentViewModel]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        user_id = self.user_id
        project_id = self.project_id
        class_id = self.class_id
        service_id = self.service_id
        document_id = self.document_id
        work_item_id = self.work_item_id
        shred_id = self.shred_id
        verification_id = self.verification_id
        contact_id = self.contact_id
        type: Union[Unset, int] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        area: Union[Unset, int] = UNSET
        if not isinstance(self.area, Unset):
            area = self.area.value

        event: Union[Unset, int] = UNSET
        if not isinstance(self.event, Unset):
            event = self.event.value

        level: Union[Unset, int] = UNSET
        if not isinstance(self.level, Unset):
            level = self.level.value

        to = self.to
        address = self.address
        subject = self.subject
        content_type = self.content_type
        body = self.body
        error = self.error
        dtc: Union[Unset, str] = UNSET
        if not isinstance(self.dtc, Unset):
            dtc = self.dtc.isoformat()

        dtm: Union[Unset, str] = UNSET
        if not isinstance(self.dtm, Unset):
            dtm = self.dtm.isoformat()

        sent: Union[Unset, None, str] = UNSET
        if not isinstance(self.sent, Unset):
            sent = self.sent.isoformat() if self.sent else None

        delivered: Union[Unset, None, str] = UNSET
        if not isinstance(self.delivered, Unset):
            delivered = self.delivered.isoformat() if self.delivered else None

        read_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.read_date, Unset):
            read_date = self.read_date.isoformat() if self.read_date else None

        contact: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict() if self.contact else None

        attachments: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attachments, Unset):
            if self.attachments is None:
                attachments = None
            else:
                attachments = []
                for attachments_item_data in self.attachments:
                    attachments_item = attachments_item_data.to_dict()

                    attachments.append(attachments_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "userId": user_id,
            }
        )
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if class_id is not UNSET:
            field_dict["classId"] = class_id
        if service_id is not UNSET:
            field_dict["serviceId"] = service_id
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if work_item_id is not UNSET:
            field_dict["workItemId"] = work_item_id
        if shred_id is not UNSET:
            field_dict["shredId"] = shred_id
        if verification_id is not UNSET:
            field_dict["verificationId"] = verification_id
        if contact_id is not UNSET:
            field_dict["contactId"] = contact_id
        if type is not UNSET:
            field_dict["type"] = type
        if status is not UNSET:
            field_dict["status"] = status
        if area is not UNSET:
            field_dict["area"] = area
        if event is not UNSET:
            field_dict["event"] = event
        if level is not UNSET:
            field_dict["level"] = level
        if to is not UNSET:
            field_dict["to"] = to
        if address is not UNSET:
            field_dict["address"] = address
        if subject is not UNSET:
            field_dict["subject"] = subject
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if body is not UNSET:
            field_dict["body"] = body
        if error is not UNSET:
            field_dict["error"] = error
        if dtc is not UNSET:
            field_dict["dtc"] = dtc
        if dtm is not UNSET:
            field_dict["dtm"] = dtm
        if sent is not UNSET:
            field_dict["sent"] = sent
        if delivered is not UNSET:
            field_dict["delivered"] = delivered
        if read_date is not UNSET:
            field_dict["readDate"] = read_date
        if contact is not UNSET:
            field_dict["contact"] = contact
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        user_id = d.pop("userId")

        project_id = d.pop("projectId", UNSET)

        class_id = d.pop("classId", UNSET)

        service_id = d.pop("serviceId", UNSET)

        document_id = d.pop("documentId", UNSET)

        work_item_id = d.pop("workItemId", UNSET)

        shred_id = d.pop("shredId", UNSET)

        verification_id = d.pop("verificationId", UNSET)

        contact_id = d.pop("contactId", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, AIForgedDALNotificationType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = AIForgedDALNotificationType(_type)

        _status = d.pop("status", UNSET)
        status: Union[Unset, AIForgedDALNotificationStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AIForgedDALNotificationStatus(_status)

        _area = d.pop("area", UNSET)
        area: Union[Unset, AIForgedDALNotificationArea]
        if isinstance(_area, Unset):
            area = UNSET
        else:
            area = AIForgedDALNotificationArea(_area)

        _event = d.pop("event", UNSET)
        event: Union[Unset, AIForgedDALNotificationEvent]
        if isinstance(_event, Unset):
            event = UNSET
        else:
            event = AIForgedDALNotificationEvent(_event)

        _level = d.pop("level", UNSET)
        level: Union[Unset, AIForgedDALNotificationLevel]
        if isinstance(_level, Unset):
            level = UNSET
        else:
            level = AIForgedDALNotificationLevel(_level)

        to = d.pop("to", UNSET)

        address = d.pop("address", UNSET)

        subject = d.pop("subject", UNSET)

        content_type = d.pop("contentType", UNSET)

        body = d.pop("body", UNSET)

        error = d.pop("error", UNSET)

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

        _sent = d.pop("sent", UNSET)
        sent: Union[Unset, None, datetime.datetime]
        if _sent is None:
            sent = None
        elif isinstance(_sent, Unset):
            sent = UNSET
        else:
            sent = isoparse(_sent)

        _delivered = d.pop("delivered", UNSET)
        delivered: Union[Unset, None, datetime.datetime]
        if _delivered is None:
            delivered = None
        elif isinstance(_delivered, Unset):
            delivered = UNSET
        else:
            delivered = isoparse(_delivered)

        _read_date = d.pop("readDate", UNSET)
        read_date: Union[Unset, None, datetime.datetime]
        if _read_date is None:
            read_date = None
        elif isinstance(_read_date, Unset):
            read_date = UNSET
        else:
            read_date = isoparse(_read_date)

        _contact = d.pop("contact", UNSET)
        contact: Union[Unset, None, AIForgedViewModelsContactViewModel]
        if _contact is None:
            contact = None
        elif isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = AIForgedViewModelsContactViewModel.from_dict(_contact)

        attachments = []
        _attachments = d.pop("attachments", UNSET)
        for attachments_item_data in _attachments or []:
            attachments_item = AIForgedViewModelsNotificationAttachmentViewModel.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        ai_forged_view_models_notification_view_model = cls(
            id=id,
            user_id=user_id,
            project_id=project_id,
            class_id=class_id,
            service_id=service_id,
            document_id=document_id,
            work_item_id=work_item_id,
            shred_id=shred_id,
            verification_id=verification_id,
            contact_id=contact_id,
            type=type,
            status=status,
            area=area,
            event=event,
            level=level,
            to=to,
            address=address,
            subject=subject,
            content_type=content_type,
            body=body,
            error=error,
            dtc=dtc,
            dtm=dtm,
            sent=sent,
            delivered=delivered,
            read_date=read_date,
            contact=contact,
            attachments=attachments,
        )

        return ai_forged_view_models_notification_view_model

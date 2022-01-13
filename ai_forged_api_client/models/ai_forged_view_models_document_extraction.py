import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.ai_forged_dal_grouping_type import AIForgedDALGroupingType
from ..models.ai_forged_dal_parameter_definition_category import AIForgedDALParameterDefinitionCategory
from ..models.ai_forged_dal_value_type import AIForgedDALValueType
from ..models.ai_forged_dal_verification_status import AIForgedDALVerificationStatus
from ..models.ai_forged_dal_verification_type import AIForgedDALVerificationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AIForgedViewModelsDocumentExtraction")


@attr.s(auto_attribs=True)
class AIForgedViewModelsDocumentExtraction:
    """Transposed extraction of structured document results

    Attributes:
        id (Union[Unset, int]):
        parent_id (Union[Unset, None, int]):
        name (Union[Unset, None, str]):
        label (Union[Unset, None, str]):
        category (Union[Unset, None, AIForgedDALParameterDefinitionCategory]): Category of definition
        grouping (Union[Unset, None, AIForgedDALGroupingType]): Type of field grouping
        value_type (Union[Unset, AIForgedDALValueType]): The type of values used for rules and settings
        index (Union[Unset, None, int]):
        param_id (Union[Unset, int]):
        parent_param_id (Union[Unset, None, int]):
        param_index (Union[Unset, None, int]):
        param_value (Union[Unset, None, str]):
        verification_id (Union[Unset, None, int]):
        user_id (Union[Unset, None, str]):
        user_name (Union[Unset, None, str]):
        value (Union[Unset, None, str]):
        dt (Union[Unset, None, datetime.datetime]):
        confidence (Union[Unset, None, float]):
        type (Union[Unset, None, AIForgedDALVerificationType]): Type of verification
        status (Union[Unset, None, AIForgedDALVerificationStatus]): Verification status flags
        charge (Union[Unset, None, float]):
        provider (Union[Unset, None, str]):
        result (Union[Unset, None, str]):
    """

    id: Union[Unset, int] = UNSET
    parent_id: Union[Unset, None, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    label: Union[Unset, None, str] = UNSET
    category: Union[Unset, None, AIForgedDALParameterDefinitionCategory] = UNSET
    grouping: Union[Unset, None, AIForgedDALGroupingType] = UNSET
    value_type: Union[Unset, AIForgedDALValueType] = UNSET
    index: Union[Unset, None, int] = UNSET
    param_id: Union[Unset, int] = UNSET
    parent_param_id: Union[Unset, None, int] = UNSET
    param_index: Union[Unset, None, int] = UNSET
    param_value: Union[Unset, None, str] = UNSET
    verification_id: Union[Unset, None, int] = UNSET
    user_id: Union[Unset, None, str] = UNSET
    user_name: Union[Unset, None, str] = UNSET
    value: Union[Unset, None, str] = UNSET
    dt: Union[Unset, None, datetime.datetime] = UNSET
    confidence: Union[Unset, None, float] = UNSET
    type: Union[Unset, None, AIForgedDALVerificationType] = UNSET
    status: Union[Unset, None, AIForgedDALVerificationStatus] = UNSET
    charge: Union[Unset, None, float] = UNSET
    provider: Union[Unset, None, str] = UNSET
    result: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        parent_id = self.parent_id
        name = self.name
        label = self.label
        category: Union[Unset, None, int] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value if self.category else None

        grouping: Union[Unset, None, int] = UNSET
        if not isinstance(self.grouping, Unset):
            grouping = self.grouping.value if self.grouping else None

        value_type: Union[Unset, int] = UNSET
        if not isinstance(self.value_type, Unset):
            value_type = self.value_type.value

        index = self.index
        param_id = self.param_id
        parent_param_id = self.parent_param_id
        param_index = self.param_index
        param_value = self.param_value
        verification_id = self.verification_id
        user_id = self.user_id
        user_name = self.user_name
        value = self.value
        dt: Union[Unset, None, str] = UNSET
        if not isinstance(self.dt, Unset):
            dt = self.dt.isoformat() if self.dt else None

        confidence = self.confidence
        type: Union[Unset, None, int] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value if self.type else None

        status: Union[Unset, None, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value if self.status else None

        charge = self.charge
        provider = self.provider
        result = self.result

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if name is not UNSET:
            field_dict["name"] = name
        if label is not UNSET:
            field_dict["label"] = label
        if category is not UNSET:
            field_dict["category"] = category
        if grouping is not UNSET:
            field_dict["grouping"] = grouping
        if value_type is not UNSET:
            field_dict["valueType"] = value_type
        if index is not UNSET:
            field_dict["index"] = index
        if param_id is not UNSET:
            field_dict["paramId"] = param_id
        if parent_param_id is not UNSET:
            field_dict["parentParamId"] = parent_param_id
        if param_index is not UNSET:
            field_dict["paramIndex"] = param_index
        if param_value is not UNSET:
            field_dict["paramValue"] = param_value
        if verification_id is not UNSET:
            field_dict["verificationId"] = verification_id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if value is not UNSET:
            field_dict["value"] = value
        if dt is not UNSET:
            field_dict["dt"] = dt
        if confidence is not UNSET:
            field_dict["confidence"] = confidence
        if type is not UNSET:
            field_dict["type"] = type
        if status is not UNSET:
            field_dict["status"] = status
        if charge is not UNSET:
            field_dict["charge"] = charge
        if provider is not UNSET:
            field_dict["provider"] = provider
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        parent_id = d.pop("parentId", UNSET)

        name = d.pop("name", UNSET)

        label = d.pop("label", UNSET)

        _category = d.pop("category", UNSET)
        category: Union[Unset, None, AIForgedDALParameterDefinitionCategory]
        if _category is None:
            category = None
        elif isinstance(_category, Unset):
            category = UNSET
        else:
            category = AIForgedDALParameterDefinitionCategory(_category)

        _grouping = d.pop("grouping", UNSET)
        grouping: Union[Unset, None, AIForgedDALGroupingType]
        if _grouping is None:
            grouping = None
        elif isinstance(_grouping, Unset):
            grouping = UNSET
        else:
            grouping = AIForgedDALGroupingType(_grouping)

        _value_type = d.pop("valueType", UNSET)
        value_type: Union[Unset, AIForgedDALValueType]
        if isinstance(_value_type, Unset):
            value_type = UNSET
        else:
            value_type = AIForgedDALValueType(_value_type)

        index = d.pop("index", UNSET)

        param_id = d.pop("paramId", UNSET)

        parent_param_id = d.pop("parentParamId", UNSET)

        param_index = d.pop("paramIndex", UNSET)

        param_value = d.pop("paramValue", UNSET)

        verification_id = d.pop("verificationId", UNSET)

        user_id = d.pop("userId", UNSET)

        user_name = d.pop("userName", UNSET)

        value = d.pop("value", UNSET)

        _dt = d.pop("dt", UNSET)
        dt: Union[Unset, None, datetime.datetime]
        if _dt is None:
            dt = None
        elif isinstance(_dt, Unset):
            dt = UNSET
        else:
            dt = isoparse(_dt)

        confidence = d.pop("confidence", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, None, AIForgedDALVerificationType]
        if _type is None:
            type = None
        elif isinstance(_type, Unset):
            type = UNSET
        else:
            type = AIForgedDALVerificationType(_type)

        _status = d.pop("status", UNSET)
        status: Union[Unset, None, AIForgedDALVerificationStatus]
        if _status is None:
            status = None
        elif isinstance(_status, Unset):
            status = UNSET
        else:
            status = AIForgedDALVerificationStatus(_status)

        charge = d.pop("charge", UNSET)

        provider = d.pop("provider", UNSET)

        result = d.pop("result", UNSET)

        ai_forged_view_models_document_extraction = cls(
            id=id,
            parent_id=parent_id,
            name=name,
            label=label,
            category=category,
            grouping=grouping,
            value_type=value_type,
            index=index,
            param_id=param_id,
            parent_param_id=parent_param_id,
            param_index=param_index,
            param_value=param_value,
            verification_id=verification_id,
            user_id=user_id,
            user_name=user_name,
            value=value,
            dt=dt,
            confidence=confidence,
            type=type,
            status=status,
            charge=charge,
            provider=provider,
            result=result,
        )

        return ai_forged_view_models_document_extraction

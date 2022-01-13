import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.ai_forged_dal_marking_type import AIForgedDALMarkingType
from ..models.ai_forged_dal_option_status_flags import AIForgedDALOptionStatusFlags
from ..models.ai_forged_dal_orientation import AIForgedDALOrientation
from ..models.ai_forged_dal_setting_status import AIForgedDALSettingStatus
from ..models.ai_forged_dal_setting_type import AIForgedDALSettingType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AIForgedDALModelsParameterDefSettingViewModel")


@attr.s(auto_attribs=True)
class AIForgedDALModelsParameterDefSettingViewModel:
    """Detailed settings for rules and settings

    Attributes:
        id (Union[Unset, int]):
        parameter_def_id (Union[Unset, int]):
        type (Union[Unset, AIForgedDALSettingType]): The type of setting related to a parameter
        status (Union[Unset, AIForgedDALSettingStatus]): The status of a setting related to a parameter
        dtc (Union[Unset, datetime.datetime]):
        dtm (Union[Unset, datetime.datetime]):
        comment (Union[Unset, None, str]):
        info (Union[Unset, None, str]):
        data (Union[Unset, None, str]):
        min_value (Union[Unset, None, str]):
        max_value (Union[Unset, None, str]):
        confidence (Union[Unset, None, float]):
        min_confidence (Union[Unset, None, float]):
        max_confidence (Union[Unset, None, float]):
        is_case_sensative (Union[Unset, bool]):
        invert (Union[Unset, bool]):
        one_line (Union[Unset, bool]):
        one_word (Union[Unset, bool]):
        is_handwriting (Union[Unset, bool]):
        orientation (Union[Unset, None, AIForgedDALOrientation]): Text orientation of a field
        marking (Union[Unset, None, AIForgedDALMarkingType]): Marking type of text
        cells (Union[Unset, None, int]):
        clear_before (Union[Unset, AIForgedDALOptionStatusFlags]): Status flag of options
        clear_after (Union[Unset, AIForgedDALOptionStatusFlags]): Status flag of options
        cleanup_values_before (Union[Unset, bool]):
        cleanup_values_after (Union[Unset, bool]):
        validate_values_before (Union[Unset, bool]):
        validate_values_after (Union[Unset, bool]):
        abort_on_validation_error (Union[Unset, bool]):
        is_replacement_case_sensative (Union[Unset, bool]):
        compile_results (Union[Unset, None, str]):
        max_retry (Union[Unset, int]):
        timeout (Union[Unset, None, str]):
        user_id (Union[Unset, None, str]):
    """

    id: Union[Unset, int] = UNSET
    parameter_def_id: Union[Unset, int] = UNSET
    type: Union[Unset, AIForgedDALSettingType] = UNSET
    status: Union[Unset, AIForgedDALSettingStatus] = UNSET
    dtc: Union[Unset, datetime.datetime] = UNSET
    dtm: Union[Unset, datetime.datetime] = UNSET
    comment: Union[Unset, None, str] = UNSET
    info: Union[Unset, None, str] = UNSET
    data: Union[Unset, None, str] = UNSET
    min_value: Union[Unset, None, str] = UNSET
    max_value: Union[Unset, None, str] = UNSET
    confidence: Union[Unset, None, float] = UNSET
    min_confidence: Union[Unset, None, float] = UNSET
    max_confidence: Union[Unset, None, float] = UNSET
    is_case_sensative: Union[Unset, bool] = UNSET
    invert: Union[Unset, bool] = UNSET
    one_line: Union[Unset, bool] = UNSET
    one_word: Union[Unset, bool] = UNSET
    is_handwriting: Union[Unset, bool] = UNSET
    orientation: Union[Unset, None, AIForgedDALOrientation] = UNSET
    marking: Union[Unset, None, AIForgedDALMarkingType] = UNSET
    cells: Union[Unset, None, int] = UNSET
    clear_before: Union[Unset, AIForgedDALOptionStatusFlags] = UNSET
    clear_after: Union[Unset, AIForgedDALOptionStatusFlags] = UNSET
    cleanup_values_before: Union[Unset, bool] = UNSET
    cleanup_values_after: Union[Unset, bool] = UNSET
    validate_values_before: Union[Unset, bool] = UNSET
    validate_values_after: Union[Unset, bool] = UNSET
    abort_on_validation_error: Union[Unset, bool] = UNSET
    is_replacement_case_sensative: Union[Unset, bool] = UNSET
    compile_results: Union[Unset, None, str] = UNSET
    max_retry: Union[Unset, int] = UNSET
    timeout: Union[Unset, None, str] = UNSET
    user_id: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        parameter_def_id = self.parameter_def_id
        type: Union[Unset, int] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        dtc: Union[Unset, str] = UNSET
        if not isinstance(self.dtc, Unset):
            dtc = self.dtc.isoformat()

        dtm: Union[Unset, str] = UNSET
        if not isinstance(self.dtm, Unset):
            dtm = self.dtm.isoformat()

        comment = self.comment
        info = self.info
        data = self.data
        min_value = self.min_value
        max_value = self.max_value
        confidence = self.confidence
        min_confidence = self.min_confidence
        max_confidence = self.max_confidence
        is_case_sensative = self.is_case_sensative
        invert = self.invert
        one_line = self.one_line
        one_word = self.one_word
        is_handwriting = self.is_handwriting
        orientation: Union[Unset, None, int] = UNSET
        if not isinstance(self.orientation, Unset):
            orientation = self.orientation.value if self.orientation else None

        marking: Union[Unset, None, int] = UNSET
        if not isinstance(self.marking, Unset):
            marking = self.marking.value if self.marking else None

        cells = self.cells
        clear_before: Union[Unset, int] = UNSET
        if not isinstance(self.clear_before, Unset):
            clear_before = self.clear_before.value

        clear_after: Union[Unset, int] = UNSET
        if not isinstance(self.clear_after, Unset):
            clear_after = self.clear_after.value

        cleanup_values_before = self.cleanup_values_before
        cleanup_values_after = self.cleanup_values_after
        validate_values_before = self.validate_values_before
        validate_values_after = self.validate_values_after
        abort_on_validation_error = self.abort_on_validation_error
        is_replacement_case_sensative = self.is_replacement_case_sensative
        compile_results = self.compile_results
        max_retry = self.max_retry
        timeout = self.timeout
        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if parameter_def_id is not UNSET:
            field_dict["parameterDefId"] = parameter_def_id
        if type is not UNSET:
            field_dict["type"] = type
        if status is not UNSET:
            field_dict["status"] = status
        if dtc is not UNSET:
            field_dict["dtc"] = dtc
        if dtm is not UNSET:
            field_dict["dtm"] = dtm
        if comment is not UNSET:
            field_dict["comment"] = comment
        if info is not UNSET:
            field_dict["info"] = info
        if data is not UNSET:
            field_dict["data"] = data
        if min_value is not UNSET:
            field_dict["minValue"] = min_value
        if max_value is not UNSET:
            field_dict["maxValue"] = max_value
        if confidence is not UNSET:
            field_dict["confidence"] = confidence
        if min_confidence is not UNSET:
            field_dict["minConfidence"] = min_confidence
        if max_confidence is not UNSET:
            field_dict["maxConfidence"] = max_confidence
        if is_case_sensative is not UNSET:
            field_dict["isCaseSensative"] = is_case_sensative
        if invert is not UNSET:
            field_dict["invert"] = invert
        if one_line is not UNSET:
            field_dict["oneLine"] = one_line
        if one_word is not UNSET:
            field_dict["oneWord"] = one_word
        if is_handwriting is not UNSET:
            field_dict["isHandwriting"] = is_handwriting
        if orientation is not UNSET:
            field_dict["orientation"] = orientation
        if marking is not UNSET:
            field_dict["marking"] = marking
        if cells is not UNSET:
            field_dict["cells"] = cells
        if clear_before is not UNSET:
            field_dict["clearBefore"] = clear_before
        if clear_after is not UNSET:
            field_dict["clearAfter"] = clear_after
        if cleanup_values_before is not UNSET:
            field_dict["cleanupValuesBefore"] = cleanup_values_before
        if cleanup_values_after is not UNSET:
            field_dict["cleanupValuesAfter"] = cleanup_values_after
        if validate_values_before is not UNSET:
            field_dict["validateValuesBefore"] = validate_values_before
        if validate_values_after is not UNSET:
            field_dict["validateValuesAfter"] = validate_values_after
        if abort_on_validation_error is not UNSET:
            field_dict["abortOnValidationError"] = abort_on_validation_error
        if is_replacement_case_sensative is not UNSET:
            field_dict["isReplacementCaseSensative"] = is_replacement_case_sensative
        if compile_results is not UNSET:
            field_dict["compileResults"] = compile_results
        if max_retry is not UNSET:
            field_dict["maxRetry"] = max_retry
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        parameter_def_id = d.pop("parameterDefId", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, AIForgedDALSettingType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = AIForgedDALSettingType(_type)

        _status = d.pop("status", UNSET)
        status: Union[Unset, AIForgedDALSettingStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AIForgedDALSettingStatus(_status)

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

        comment = d.pop("comment", UNSET)

        info = d.pop("info", UNSET)

        data = d.pop("data", UNSET)

        min_value = d.pop("minValue", UNSET)

        max_value = d.pop("maxValue", UNSET)

        confidence = d.pop("confidence", UNSET)

        min_confidence = d.pop("minConfidence", UNSET)

        max_confidence = d.pop("maxConfidence", UNSET)

        is_case_sensative = d.pop("isCaseSensative", UNSET)

        invert = d.pop("invert", UNSET)

        one_line = d.pop("oneLine", UNSET)

        one_word = d.pop("oneWord", UNSET)

        is_handwriting = d.pop("isHandwriting", UNSET)

        _orientation = d.pop("orientation", UNSET)
        orientation: Union[Unset, None, AIForgedDALOrientation]
        if _orientation is None:
            orientation = None
        elif isinstance(_orientation, Unset):
            orientation = UNSET
        else:
            orientation = AIForgedDALOrientation(_orientation)

        _marking = d.pop("marking", UNSET)
        marking: Union[Unset, None, AIForgedDALMarkingType]
        if _marking is None:
            marking = None
        elif isinstance(_marking, Unset):
            marking = UNSET
        else:
            marking = AIForgedDALMarkingType(_marking)

        cells = d.pop("cells", UNSET)

        _clear_before = d.pop("clearBefore", UNSET)
        clear_before: Union[Unset, AIForgedDALOptionStatusFlags]
        if isinstance(_clear_before, Unset):
            clear_before = UNSET
        else:
            clear_before = AIForgedDALOptionStatusFlags(_clear_before)

        _clear_after = d.pop("clearAfter", UNSET)
        clear_after: Union[Unset, AIForgedDALOptionStatusFlags]
        if isinstance(_clear_after, Unset):
            clear_after = UNSET
        else:
            clear_after = AIForgedDALOptionStatusFlags(_clear_after)

        cleanup_values_before = d.pop("cleanupValuesBefore", UNSET)

        cleanup_values_after = d.pop("cleanupValuesAfter", UNSET)

        validate_values_before = d.pop("validateValuesBefore", UNSET)

        validate_values_after = d.pop("validateValuesAfter", UNSET)

        abort_on_validation_error = d.pop("abortOnValidationError", UNSET)

        is_replacement_case_sensative = d.pop("isReplacementCaseSensative", UNSET)

        compile_results = d.pop("compileResults", UNSET)

        max_retry = d.pop("maxRetry", UNSET)

        timeout = d.pop("timeout", UNSET)

        user_id = d.pop("userId", UNSET)

        ai_forged_dal_models_parameter_def_setting_view_model = cls(
            id=id,
            parameter_def_id=parameter_def_id,
            type=type,
            status=status,
            dtc=dtc,
            dtm=dtm,
            comment=comment,
            info=info,
            data=data,
            min_value=min_value,
            max_value=max_value,
            confidence=confidence,
            min_confidence=min_confidence,
            max_confidence=max_confidence,
            is_case_sensative=is_case_sensative,
            invert=invert,
            one_line=one_line,
            one_word=one_word,
            is_handwriting=is_handwriting,
            orientation=orientation,
            marking=marking,
            cells=cells,
            clear_before=clear_before,
            clear_after=clear_after,
            cleanup_values_before=cleanup_values_before,
            cleanup_values_after=cleanup_values_after,
            validate_values_before=validate_values_before,
            validate_values_after=validate_values_after,
            abort_on_validation_error=abort_on_validation_error,
            is_replacement_case_sensative=is_replacement_case_sensative,
            compile_results=compile_results,
            max_retry=max_retry,
            timeout=timeout,
            user_id=user_id,
        )

        return ai_forged_dal_models_parameter_def_setting_view_model

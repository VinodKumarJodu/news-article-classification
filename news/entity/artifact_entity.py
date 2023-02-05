from dataclasses import dataclass 

@dataclass
class DataIngestionArtifact:
    train_file_path: str
    test_file_path: str

@dataclass
class ValidationResult:
    validate_number_of_columns: bool
    column_name_validation: bool
    datatype_validation: bool
    target_label_validation:bool

@dataclass
class DataValidationArtifact:
    validation_results: ValidationResult
    valid_train_file_path: str
    valid_test_file_path: str
    invalid_train_file_path: str
    invalid_test_file_path: str


@dataclass 
class DataTransformationArtifact:
    transformed_object_file_path: str 
    transformed_train_file_path: str 
    transformed_test_file_path: str 

from core.domain.entities.document import Document
from core.domain.entities.ConfigDoc import ConfigDoc
from core.domain.entities.resultOCR import ResultOCR
from core.domain.entities.user import User
from .models import UserProfile, ResultOCRModel, DocumentModel, ConfigDocModel


class EntitiesMappers:

    @staticmethod
    def document_to_document_model(entity: Document) -> DocumentModel:
        doc_model = DocumentModel(
            user=entity.id_user,
            config=entity.id_config_doc,
            result=entity.id_resultOCR,
            processed=entity.processed,
            doc_file=entity.doc_file,
        )

        if entity.id is not None:
            doc_model.id = entity.id

        return doc_model

    @staticmethod
    def document_model_to_document(model: "DocumentModel") -> Document:
        return Document(
            id=model.id,
            id_user=model.user.id,
            id_config_doc=model.config.id,
            id_resultOCR=model.result.id,
            doc_file=model.doc_file,
            processed=model.processed,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )

    @staticmethod
    def user_to_user_model(entiy: User) -> UserProfile:
        user_model = UserProfile(
            email=entiy.email,
            name=entiy.name,
            last_name=entiy.last_name,
            birth=entiy.birth,
            permission=entiy.permission,
        )

        if entiy.id is not None:
            user_model.id = entiy.id

        return user_model

    @staticmethod
    def user_model_to_user(model: UserProfile) -> User:
        return User(
            id=model.id,
            email=model.email,
            name=model.name,
            last_name=model.last_name,
            birth=model.birth,
            permission=model.permission,
        )

    @staticmethod
    def resultOCR_to_resultOCR_model(entity: ResultOCR) -> ResultOCRModel:
        result_model = ResultOCRModel(
            raw=entity.raw,
            clean=entity.clean,
            success=entity.success,
            mistakes=entity.mistakes,
        )

        if entity.id is not None:
            result_model.id = entity.id

        return result_model

    @staticmethod
    def resultOCR_model_to_resultOCR(model: ResultOCRModel) -> ResultOCR:
        return ResultOCR(
            id=model.id,
            raw=model.raw,
            clean=model.clean,
            success=model.success,
            mistakes=model.mistakes,
            created_at=model.created_at,
        )

    @staticmethod
    def configDoc_to_configDoc_model(entity: ConfigDoc) -> ConfigDocModel:
        config_model = ConfigDocModel(
            ocr_chosen=entity.ocr_chosen,
            type_doc=entity.type_doc,
            language=entity.language,
        )

        if entity.id is not None:
            config_model = entity.id

        return config_model

    @staticmethod
    def configDoc_model_to_configDoc(model: ConfigDocModel) -> ConfigDoc:
        return ConfigDoc(
            id=model.id,
            ocr_chosen=model.ocr_chosen,
            type_doc=model.type_doc,
            language=model.language,
        )

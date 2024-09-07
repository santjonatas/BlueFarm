from typing import Type, TypeVar, Generic, List, Optional
from app.domain.entities.common.base_entity import BaseEntity

T = TypeVar('T', bound=BaseEntity)


class BaseRepository(Generic[T]):
    def __init__(self, session, entity: Type[T]):
        self.session = session
        self.entity = entity

    def add(self, obj: T) -> T:
        try:
            self.session.add(obj)
            self.session.commit()
            self.session.refresh(obj)
            return obj
        except Exception as e:
            self.session.rollback()
            raise e

    def get(self, obj_id: int) -> Optional[T]:
        try:
            return self.session.query(self.entity).filter(self.entity.id == obj_id).first()
        except Exception as e:
            self.session.rollback()
            raise e

    def update(self, obj: T) -> T:
        try:
            self.session.merge(obj)
            self.session.commit()
            return obj
        except Exception as e:
            self.session.rollback()
            raise e

    def delete(self, obj_id: int) -> None:
        try:
            obj = self.get(obj_id)
            if obj:
                self.session.delete(obj)
                self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

    def list(self) -> List[T]:
        try:
            return self.session.query(self.entity).all()
        except Exception as e:
            self.session.rollback()
            raise e

    def delete_all(self) -> None:
        try:
            self.session.query(self.entity).delete()
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

    def add_bulk(self, objs: List[T]) -> List[T]:
        try:
            self.session.bulk_save_objects(objs)
            self.session.commit()
            return objs
        except Exception as e:
            self.session.rollback()
            raise e

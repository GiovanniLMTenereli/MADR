from sqlalchemy.orm import Mapped, mapped_column, registry, relationship

from ..books import Books

table_registry = registry()


@table_registry.mapped_as_dataclass
class Writers:
    __tablename__ = "writers"
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str]
    books: Mapped[list[Books]] = relationship(
        init=False, back_populates="writers", cascade="all, delete-orphan"
    )

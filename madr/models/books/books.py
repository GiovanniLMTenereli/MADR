from sqlalchemy.orm import Mapped, mapped_column, registry, relationship

from ..writers import Writers

table_registry = registry()


@table_registry.mapped_as_dataclass
class Books:
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    title: Mapped[str]
    year: Mapped[int]
    writer: Mapped[Writers] = relationship(init=False, back_populates="books")

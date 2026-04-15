from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_as_dataclass, registry, mapped_column

table_registry = registry()

@mapped_as_dataclass(table_registry)
class User:
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(init = False ,primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(init = False, server_default= func.now())
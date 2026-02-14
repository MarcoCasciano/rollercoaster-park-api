# importo la classe Base dichiarativa di SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

# definisco lista per silenziare avvisi 'unused import statement'
# __all__ = ["Base", "Attrazione", "Famiglia", "Visitatore", "Giro"]

# espongo metadata che raccoglie tutti i modelli importati
# lo rendo facilmente accessibile a SQLAlchemy e Alembic
metadata = Base.metadata
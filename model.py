# coding: utf-8
from sqlalchemy import BigInteger, Column, Float, Index, Integer, Numeric, Table, Text, UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


# output from: sqlacodegen --outfile model.py postgresql://database_URL


class Company(Base):
    __tablename__ = 'company'

    stock_id = Column(BigInteger, primary_key=True)
    name = Column(Text)
    acronym = Column(Text)
    director = Column(Text)
    benefit_description = Column(Text)
    benefit_requirement = Column(BigInteger)


class NewCompany(Base):
    __tablename__ = 'new_company'
    __table_args__ = (
        Index('new_company_stock_id_acronym_uindex', 'stock_id', 'acronym', unique=True),
    )

    stock_id = Column(Integer, primary_key=True)
    name = Column(Text)
    acronym = Column(Text)
    benefit_description = Column(Text)
    benefit_requirement = Column(Integer)
    benefit_frequency = Column(Integer)


class NewStock(Base):
    __tablename__ = 'new_stocks'
    __table_args__ = (
        Index('new_stocks_timestamp_acronym_index', 'timestamp', 'acronym'),
        Index('new_stocks_acronym_timestamp_uindex', 'acronym', 'timestamp', unique=True),
        Index('new_stock_index_timestamp_acronym', 'acronym', 'timestamp')
    )

    serial = Column(Integer, primary_key=True, unique=True,
                    server_default=text("nextval('new_stocks_serial_seq'::regclass)"))
    acronym = Column(Text, nullable=False, index=True)
    current_price = Column(Float, nullable=False)
    timestamp = Column(Integer, index=True)
    market_cap = Column(BigInteger)
    total_shares = Column(BigInteger)


t_stocks = Table(
    'stocks', metadata,
    Column('timestamp', BigInteger, index=True),
    Column('stock_id', BigInteger, index=True),
    Column('current_price', Numeric),
    Column('market_cap', BigInteger),
    Column('total_shares', BigInteger),
    Column('available_shares', BigInteger),
    Column('forecast', Text),
    Column('demand', Text),
    Column('id', Integer, nullable=False, server_default=text("nextval('stocks_id_seq'::regclass)")),
    UniqueConstraint('stock_id', 'timestamp'),
    Index('idx_25629_stock_query_index', 'stock_id', 'timestamp')
)

t_stocks_price = Table(
    'stocks_price', metadata,
    Column('id', Integer, nullable=False, server_default=text("nextval('stocks_price_id_seq'::regclass)")),
    Column('acronym', Text),
    Column('timestamp', Integer),
    Column('current_price', Numeric),
    Index('stocks_price_timestamp_acronym_uindex', 'timestamp', 'acronym', unique=True)
)

t_stocks_price_short = Table(
    'stocks_price_short', metadata,
    Column('id', Integer, nullable=False, server_default=text("nextval('stocks_price_short_id_seq'::regclass)")),
    Column('acronym', Text),
    Column('timestamp', Integer),
    Column('current_price', Numeric),
    Index('stocks_price_short_timestamp_acronym_uindex', 'timestamp', 'acronym', unique=True)
)

t_stocks_value = Table(
    'stocks_value', metadata,
    Column('id', Integer, nullable=False, server_default=text("nextval('stocks_value_id_seq'::regclass)")),
    Column('acronym', Text),
    Column('total_shares', BigInteger),
    Column('timestamp', Integer),
    Column('current_price', Numeric),
    Index('stocks_value_timestamp_acronym_uindex', 'timestamp', 'acronym', unique=True)
)

t_stocks_volume = Table(
    'stocks_volume', metadata,
    Column('id', Integer, nullable=False, server_default=text("nextval('stocks_volume_id_seq'::regclass)")),
    Column('acronym', Text),
    Column('total_shares', BigInteger),
    Column('timestamp', Integer),
    Column('current_price', Numeric),
    Index('stocks_volume_timestamp_acronym_uindex', 'timestamp', 'acronym', unique=True),
    Index('stocks_volume_double_timestamp_acronym_uindex', 'timestamp', 'acronym', unique=True)
)

t_stocks_volume_double = Table(
    'stocks_volume_double', metadata,
    Column('id', Integer, nullable=False, server_default=text("nextval('stocks_volume_double_id_seq'::regclass)")),
    Column('acronym', Text),
    Column('total_shares', BigInteger),
    Column('timestamp', Integer),
    Column('current_price', Numeric),
    Index('stocks_volume_double_timestamp_acronym_uindex_2', 'timestamp', 'acronym', unique=True)
)

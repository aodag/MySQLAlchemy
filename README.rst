====================
MySQLAlchemy
====================

SQLAlchemy expression library for MySQL dialect.

Install
====================

::

 easy_install MySQLALchemy
 or
 pip install MySQLAlchemy

USAGE
======================

::

 import sqlalchemy as sa
 from sqlalchemy.sql import func
 from mysqlalchemy.expressions import INTERVAL

 engine = sa.create_engine('mysql+pymysql://root@localhost/mysqlalchemy')
 q = sa.select(func.CURRENT_TIMESTAMP - INTERVAL(hours=2))
 engine.execute(q)

Supported Expressions
================================

- INRERVAL
- MATCH AGAINST

import unittest

class IntervalTests(unittest.TestCase):
    def _getTarget(self):
        from . import expressions
        return expressions.Interval

    def _makeOne(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def _assertCompiled(self, expression, sql):
        from sqlalchemy.dialects.mysql.base import MySQLDialect
        result = expression.compile(dialect=MySQLDialect())
        self.assertEqual(str(result), sql)

    def test_it(self):
        target = self._makeOne(self._getTarget().HOUR, hours=10)
        self._assertCompiled(target, "INTERVAL 10 HOUR")
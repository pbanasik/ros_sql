import sqlalchemy.types as s
import ros_sql.models as models

type_map = {
    'bool':
        s.Boolean(),
    'char':
        s.SmallInteger(),
    'int8':
        s.SmallInteger(),
    'uint8':
        s.SmallInteger(),
    'byte':
        s.SmallInteger(),
    'int16':
        s.Integer(),
    'uint16':
        s.Integer(),
    'int32':
        s.Integer(),
    'uint32':
        s.Integer(),
    'int64':
        s.BigInteger(),
    'uint64':
        s.BigInteger(),
    'float32':
        s.Float(precision=32),
    'float64':
        s.Float(precision=53),
    'string':
        s.Text(),
    }

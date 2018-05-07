"""Support for Graphite."""

import attr
from attr.validators import instance_of

@attr.s
class GraphiteTarget(object):

    target = attr.ib()
    refId = attr.ib(default="")
    hide = attr.ib(default=False, validator=instance_of(bool))

    def to_json_data(self):

        return {
            'target': self.target,
            'refId': self.refId,
            'hide': self.hide,
        }

from ml.base.base_utils import find_subclass_by_name


class MLGraph(object):

    def __init__(self, global_config):
        self.global_config = global_config
        self.graph_config = self.global_config.graph_config

        self.input = None
        self.output = None

    @classmethod
    def from_config(cls, global_config):
        subcls = find_subclass_by_name(cls, global_config.graph.graph_name)
        return subcls.from_config(global_config)

    def add_forward_pass(self, features, mode):
        raise NotImplementedError
        return self.output

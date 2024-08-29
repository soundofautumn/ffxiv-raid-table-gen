from data import InputData, OutputData


class Algorithm:

    @staticmethod
    def process(data: InputData) -> OutputData:
        raise NotImplementedError


class DefaultAlgorithm(Algorithm):
    def process(self, data: InputData) -> OutputData:
        data = data.data
        result = [[] for _ in range(1 + len(data) // 8)]
        for (idx, d) in enumerate(data):
            result[idx // 8].append(OutputData.OutputEntity(d.name, d.duties[0]))
        return OutputData(result)

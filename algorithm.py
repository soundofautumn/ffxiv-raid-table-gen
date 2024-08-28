from data import InputData, OutputData


class Algorithm:

    @staticmethod
    def process(data: list[InputData]) -> list[list[OutputData]]:
        raise NotImplementedError


class DefaultAlgorithm(Algorithm):
    def process(self, data: list[InputData]) -> list[list[OutputData]]:
        result = [[] for _ in range(1 + len(data) // 8)]
        for (idx, d) in enumerate(data):
            result[idx // 8].append(OutputData(d.name, d.duties[0]))
        return result

import os

from data import InputData, OutputData

INPUT_DIR = './data'
OUTPUT_DIR = './output'


class Adapter:
    def __init__(self):
        self.input_file = ''
        self.output_file = ''

    def set_file(self, filename: str):
        self.input_file = os.path.join(INPUT_DIR, filename)
        self.output_file = os.path.join(OUTPUT_DIR, filename)

    def get_input(self) -> InputData:
        raise NotImplementedError

    def save_output(self, data: OutputData):
        raise NotImplementedError


class QQBotInputAdapter(Adapter):

    def get_input(self) -> InputData:
        import pandas as pd
        df = pd.read_csv(self.input_file)
        data = []
        for i in range(len(df)):
            key = df.iloc[i]['QQ(报名使用)']
            name = df.iloc[i]['角色姓名']
            duties = [df.iloc[i]['主选职能']]
            if not pd.isna(df.iloc[i]['次选职能']):
                duties.append(df.iloc[i]['次选职能'])
            data.append(InputData.InputEntity(key, name, duties))
        return InputData(data)


class DefaultOutputAdapter(Adapter):

    def save_output(self, data: OutputData):
        import pandas as pd
        data = data.data
        output = []
        for d in data:
            output.append([x.name for x in d])
        df = pd.DataFrame(output)
        df.to_csv(self.output_file, index=False, header=False)


class DefaultAdapter(QQBotInputAdapter, DefaultOutputAdapter):
    pass

from adapter import DefaultAdapter
from algorithm import DefaultAlgorithm

adapter = DefaultAdapter()
algorithm = DefaultAlgorithm()


def main():
    adapter.set_file('49团.csv')
    data = adapter.get_input()
    result = algorithm.process(data)
    adapter.save_output(result)


if __name__ == '__main__':
    main()

import pandas as pd

from Test import Test


def test_magic04(max_iteration, n_random_choice):
    data = pd.read_csv('DataSets/magic04.txt')

    data.replace('g', 1, True)
    data.replace('h', -1, True)

    test = Test(data, 'magic04 dataset', n_random_choice)

    test.run_test_get_result(max_iteration, n_random_choice)


def test_frogs(max_iteration, n_random_choice):
    data = pd.read_csv('DataSets/Frogs_MFCCs.csv')
    data = data.iloc[:, :23]

    data.replace('Leptodactylidae', 1, True)
    data.replace('Hylidae', -1, True)

    index_to_remove = data.index[data['Family'] == 'Bufonidae'].tolist()
    data = data.drop(index_to_remove, axis=0)

    index_to_remove = data.index[data['Family'] == 'Dendrobatidae'].tolist()
    data = data.drop(index_to_remove, axis=0)

    test = Test(data, 'Frogs_MFCCs dataset', n_random_choice)

    test.run_test_get_result(max_iteration, n_random_choice)


def test_avila(max_iteration, n_random_choice):
    data_1 = pd.read_csv('DataSets/avila-tr.txt')
    data_2 = pd.read_csv('DataSets/avila-ts.txt')

    data = pd.concat([data_1, data_2], ignore_index=True)

    data.replace('A', 1, True)
    data.replace('F', -1, True)

    index_to_remove = data.index[data.iloc[:, 10] == 'B'].tolist()
    data = data.drop(index_to_remove, axis=0)

    index_to_remove = data.index[data.iloc[:, 10] == 'B'].tolist()
    data = data.drop(index_to_remove, axis=0)

    index_to_remove = data.index[data.iloc[:, 10] == 'C'].tolist()
    data = data.drop(index_to_remove, axis=0)

    index_to_remove = data.index[data.iloc[:, 10] == 'D'].tolist()
    data = data.drop(index_to_remove, axis=0)

    index_to_remove = data.index[data.iloc[:, 10] == 'E'].tolist()
    data = data.drop(index_to_remove, axis=0)

    index_to_remove = data.index[data.iloc[:, 10] == 'G'].tolist()
    data = data.drop(index_to_remove, axis=0)

    index_to_remove = data.index[data.iloc[:, 10] == 'H'].tolist()
    data = data.drop(index_to_remove, axis=0)

    index_to_remove = data.index[data.iloc[:, 10] == 'I'].tolist()
    data = data.drop(index_to_remove, axis=0)

    index_to_remove = data.index[data.iloc[:, 10] == 'W'].tolist()
    data = data.drop(index_to_remove, axis=0)

    index_to_remove = data.index[data.iloc[:, 10] == 'X'].tolist()
    data = data.drop(index_to_remove, axis=0)

    index_to_remove = data.index[data.iloc[:, 10] == 'Y'].tolist()
    data = data.drop(index_to_remove, axis=0)

    test = Test(data, 'avila dataset', n_random_choice)

    test.run_test_get_result(max_iteration, n_random_choice)


def test_skin(max_iteration, n_random_choice):
    data = pd.read_csv('DataSets/Skin_NonSkin.txt', delim_whitespace=True)

    data.replace(2, -1, True)

    test = Test(data, 'Skin_NonSkin dataset', n_random_choice)

    test.run_test_get_result(max_iteration, n_random_choice)


def input_value_for_test():
    print("TEST 1: 'magic04' ")
    max_iteration_1 = int(input("Inserire numero massimo di iterazioni: "))
    n_random_choice_1 = int(input("Inserire numero di valori selezionati in modo random per la selezione della soglia: "))

    print("TEST 2: 'Frogs_MFCCs' ")
    max_iteration_2 = int(input("Inserire numero massimo di iterazioni: "))
    n_random_choice_2 = int(input("Inserire numero di valori selezionati in modo "
                                  "random per la selezione della soglia: "))

    print("TEST 3: 'avila-tr' ")
    max_iteration_3 = int(input("Inserire numero massimo di iterazioni: "))
    n_random_choice_3 = int(input("Inserire numero di valori selezionati in modo "
                                  "random per la selezione della soglia: "))

    print("TEST 4: 'Skin_NonSkin' ")
    max_iteration_4 = int(input("Inserire numero massimo di iterazioni: "))
    n_random_choice_4 = int(input("Inserire numero di valori selezionati in modo "
                                  "random per la selezione della soglia: "))

    test_magic04(max_iteration_1, n_random_choice_1)

    test_frogs(max_iteration_2, n_random_choice_2)

    test_avila(max_iteration_3, n_random_choice_3)

    test_skin(max_iteration_4, n_random_choice_4)


if __name__ == '__main__':
    input_value_for_test()

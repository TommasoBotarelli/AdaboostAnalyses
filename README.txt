I datasets utilizzati sono reperibili tramite i link nella relazione allegata al progetto.
Nella relazione è descritto come replicare i risultati discussi.
In questo file viene descritto con maggior precisione l''implementazione del progetto.
All'interno del progetto sono presenti tre file:

1) main.py
    All'interno di questo file si può trovare le funzioni utilizzate per preparare i datasets per i test:
    - Prendendo ad esempio "test_magic04()" questa funzione prepare il datasets eliminando
      la classificazione di "g" e "h" e sostituendo con i numeri -1 e 1.
    - La funzione "input_value_for_test()" permette l'introduzione da tastiera dei valori utili per
      eseguire il test. Dopodichè sempre la stessa funzione lancia i test per ogni datasets.

2) Test.py
    Questo file contiene la classe utilizzata per lanciare i test:
    - run_test_get_result(self, max_iteration, n_random_choice) permette la creazione di una classe "Adaboost",
      ne esegue il training, esegue il testing sia con il training set che con il testing set e
      restituisce un plot dell'accuratezza (calcolata come frazione fra gli esempi classificati in modo giusto
      e il numero totale di esempi nel set) rispetto al numero di boosting round.

3) Adaboost.py
    Questo file contiene le classi "Adaboost" e "DecisionStump":
    La classe "DecisionStump" è di appoggio all'algoritmo di Adaboost. Questa classe contiene tre attributi:
        - feature_id: indica l'indice della feature del test
        - threshold: indica il valore del test
        - alpha: indica il peso della ipotesi nell'algoritmo Adaboost.
        - polarity: durante la scelta del decision stump potrebbe accadere che un determinato
          test commette un errore maggiore di 0.5. In questo caso il valore di questo attributo
          permette di invertire il test (a questo punto l'errore commesso sarà 1-errore), e cioè:
                    if self.polarity == 1:
                        predictions[x_column < self.threshold] = -1
                    else:
                        predictions[x_column > self.threshold] = -1
    La classe Adaboost contiene due metodi:
        - training_predict(self, x_train, y_train, x_test)
            metodo che implementa l'algoritmo Adaboost. L'unica differenza con una implementazione
            classica dell'algoritmo è il fatto che ad ogni boosting round eseguito il training
            esegue il testing nel training sets e nel testing sets. Questo permette di mantenere
            i risultati di entrambi le predizioni per poterli mostrare graficamente.
        - get_decision_stump(self, x, y, w)
            permette il training del decision stump. Il training viene effettuato ciclando su ciascun attributo,
            per ogni attributo vengono considerati un valore prefissato dall'utente di valori
            random (nel caso in cui i valori dell'attributo siano numerici, altrimenti se discreti
            vengono considerati tutti) e su quelli viene scelto il valore che permette un errore minore.
            L'errore è calcolato come somma di tutti gli esempi classificati in modo erroneo pesata
            rispetto al peso di ciascun esempio. All'interno di questo metodo si comprende l'importanza
            dell'attributo "polarity" della classe DecisionStump. Infatti nel caso in cui l'errore commesso
            sia maggiore di 0.5 quello che viene fatto è impostare la polarity a -1 per permettere un
            test con errore <0.5.
        - predict(self, x)
            metodo utilizzato per eseguire la predizione considerando tutte le ipotesi create fino a
            quel momento. La predizione sarà in accordo con la predizione dell'algoritmo Adaboost cioè
            sarà il segno della somma delle predizioni pesata rispetto al peso dell'ipotesi.

Il progetto è facilmente ampliabile a nuovi datasets eseguendo i seguenti passaggi:
    1) Aggiungere alla cartella Datasets il nuovo set.
    2) Aggiungere un metodo nel main che renda conforme il set alla classificazione binaria (questo
       consiste nell'avere come etichette i numeri -1 e 1 che stanno ad indicare la classe negativa e positiva).
       All'interno del metodo creare un oggetto di tipo Test.
    3) Eseguire "test.run_test_get_result(max_iteration, n_random_choice)" all'interno del metodo.

Per replicare i risultati illustrati nella relazione eseguire il main ed indicare:
    - numero massimo di iterazioni: 200
    - numero di valori selezionati in modo random per la selezione della soglia: 50
Per ciascun test.


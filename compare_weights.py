def compare_weights(model_1, model_2):

    same = True
    for i in range(len(model_1.layers)):
        for j in range(len(model_1.layers[i].get_weights())):
            if not (np.array_equal(model_1.layers[i].get_weights()[j], model_2.layers[i].get_weights()[j])):
                same = False
        print(same)

def classification_model(tp = 2, fp = 3, fn = 4):
    #Check type variable
    if not isinstance(tp, int):
        return print('tp must be int')
    if not isinstance(fp, int):
        return print('fp must be int')
    if not isinstance(fn, int):
        return print('fn must be int')
        
    #Check value variable
    if not all(i > 0 for i in [tp, fp, fn]):
        return print('tp and fp and fn must be greater than zero')
    else:
        precision = tp/(tp+fp)
        recall = tp/(tp+fn)
        f1_score = 2*(precision*recall)/(precision+recall)
        print(f'Precision is {precision}\nRecall is {recall}\nF1-score is {f1_score}')

if __name__ == "__main__":
    classification_model()
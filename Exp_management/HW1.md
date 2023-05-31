# Домашнее задание для лекции/семинара "Experiment management" 

На занятиях мы обсуждали и пробовали работать с версионированием данных и логированием экспериментов. 
В качестве домашнего задания предлагаю провести такой эксперимент самостоятельно.

## Задача:
Проведите эксперимент с обучением модели, используя такие инструменты для оптимизации ML-моделей и отслеживания экспериментов, как *Optuna*, *Hyperopt*, *Pandas*, *Polars* и *DVC*.

## Шаги

### Dataset
- Поработаем с данными для бинарной классификации хейт-спича(eng). Датасет [живет по этой ссылке](https://github.com/intelligence-csd-auth-gr/Ethos-Hate-Speech-Dataset/blob/master/ethos/ethos_data/Ethos_Dataset_Binary.csv). 

### Model Selection
- Выберите модель/архитектуру, с которой вам было бы интересно поработать(классические, как random forest, KNN или DL-модели, типа CNN и тд).

*Совет: не выбирайте что-то громоздкое, будет удобнее если обучение пройдет быстро. Цель этого дз -- не создать наилучшую модель, а научиться удобно логировать эксперименты.*

### Hyperparameter Optimization
- Выполните поиск  наилучших значений для гиперпараметров для вашей модели с помощью Optuna или Hyperopt.<br>
- Сделайте эвалюацию вашей модели/моделей. 

*Подсказка: чтобы сделать поиск гиперпараметров, вам нужно определить search space, objective function и optimization strategy*

### Experiment Tracking with DVC
- Настройте DVC- репозиторий 
- Залогируйте в нем все изменения, которые случились в ходе эксперимента: hyperparameters, evaluation metrics, dataset versions, model versions, etc
- Напишите короткий summary report ваших экспериментов в отдельном файле.

*Подсказка: [data registry](https://dvc.org/doc/use-cases/data-registry), [model registry](https://dvc.org/doc/use-cases/model-registry), [эксперименты](https://dvc.org/doc/use-cases/experiment-tracking)*


### HW Submission:
- Организуйте код, логи экспериментов, и summary report в соответствующих папках внутри DVC-репозитория.
Сохраните код и результаты экспериментов как zip-файл, запушьте на гитхаб, пришлите ссылку на Ваш репозиторий [в эту HW-submission форму](https://forms.gle/BXUpob3G4iReRGgD6)  

## Оценки:
- Dataset loading and model selection: 5 points
- Hyperparameter optimization: 5 points
- DVC experiment tracking: 5 points
- Evaluation and comparison: 5 points
- Code organization and submission: 5 points
- Summary report: 5 points

Итого: максимум 30 баллов

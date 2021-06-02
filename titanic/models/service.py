from titanic.models.dataset import Dataset
import pandas as pd
import numpy as np
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier


class Service(object):  # 요구사항 모음

    dataset = Dataset()

    def new_model(self, payload) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis=1)

    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived']

    @staticmethod
    def drop_feature(this, *feature) -> object:
        for i in feature:
            this.train = this.train.drop([i], axis=1)  # axis=0: 가로축 삭제 axis=1: 세로축 삭제
            this.test = this.test.drop([i], axis=1)
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        this.train = this.train.fillna({'Embarked': 'S'})
        this.test = this.test.fillna({'Embarked': 'S'})
        this.train['Embarked'] = this.train['Embarked'].map({'S': 1, 'C': 2, 'Q': 3})
        this.test['Embarked'] = this.test['Embarked'].map({'S': 1, 'C': 2, 'Q': 3})
        return this

    @staticmethod
    def fare_ordinal(this) -> object:
        this.test['Fare'] = this.test.fillna({'Fare': 1})
        this.train['FareBand'] = pd.qcut(this.train['Fare'], 4)
        #  bins = list(pd.qcut(this.train['Fare'], 4, retbins=True))
        #  qcut으로 bins 값 설정 {this.train["FareBand"].head()}
        bins = [-1, 8, 15, 31, np.inf]
        this.train = this.train.drop(['FareBand'], axis=1)
        for these in this.train, this.test:
            these['FareBand'] = pd.cut(these['Fare'], bins=bins, labels=[1, 2, 3, 4])
        this.test['FareBand'] = this.test.fillna({'FareBand': 1})
        return this

    @staticmethod
    def title_norminal(this) -> object:
        combine = [this.train, this.test]  # 두 개 한번씩 돌면서 작동
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)
            # Title이 없으니 컬럼추가 됨 -> feature는 변할 수 있기때문
        for dataset in combine:
            dataset['Title'] = dataset['Title'].replace(['Capt', 'Col', 'Don', 'Dr', 'Major',
                                                         'Rev', 'Jonkheer', 'Dona'], 'Rare')
            dataset['Title'] = dataset['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            dataset['Title'] = dataset['Title'].replace('Mlle', 'Mr')
            dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
            dataset['Title'] = dataset['Title'].replace('Mme', 'Rare')
            title_mapping = {'Mr': 1, 'Miss': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}
            dataset['Title'] = dataset['Title'].fillna(0)
            dataset['Title'] = dataset['Title'].map(title_mapping)
        return this

    @staticmethod
    def gender_norminal(this) -> object:
        for dataset in this.train, this.test:
            dataset['Gender'] = dataset['Sex'].map({'male': 0, 'female': 1})
        return this

    @staticmethod
    def age_ordinal(this) -> object:
        for dataset in this.train, this.test:
            dataset['Age'] = dataset['Age'].fillna(-0.5)
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]  # np.inf - 주어진 범위 그 이후 값 통합, -1: (미상에 대한 처리)
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        age_title_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4, 'Young Adult': 5,
                             'Adult': 6, 'Senior': 7}
        for dataset in this.train, this.test:
            dataset['AgeGroup'] = pd.cut(dataset['Age'], bins=bins, labels=labels)  # key, value 이름이 같으면 key 생략가능
            dataset['AgeGroup'] = dataset['AgeGroup'].map(age_title_mapping)
        return this

    @staticmethod
    def create_k_fold():  # 사이킷런으로 러닝 시키는 것
        return KFold(n_splits=10, shuffle=True, random_state=0)

    @staticmethod
    def accuracy_by_svm(this) -> object:
        score = cross_val_score(RandomForestClassifier(),
                                this.train,
                                this.label,
                                cv=KFold(n_splits=10,
                                         shuffle=True,
                                         random_state=0),
                                n_jobs=1,
                                scoring='accuracy')
        return round(np.mean(score) * 100, 2)

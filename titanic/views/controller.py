import pandas as pd
from titanic.models.dataset import Dataset
from titanic.models.service import Service
from sklearn.ensemble import RandomForestClassifier


class Controller(object):

    dataset = Dataset()
    service = Service()

    def modeling(self, train, test) -> object:
        service = self.service
        this = self.preprocess(train, test)
        this.label = service.create_label(this)
        this.train = service.create_train(this)
        return this

    def learning(self, train, test):
        this = self.modeling(train, test)
        print(f'사이킷런의 SVC 알고리즘 정확도 {self.service.accuracy_by_svm(this)} %')

    def submit(self, train, test):
        this = self.modeling(train, test)
        clf = RandomForestClassifier()
        clf.fit(this.train, this.label)
        prediction = clf.predict(this.test)
        pd.DataFrame({'PassengerId': this.id, 'Survived': prediction}).to_csv('./data/submission.csv', index=False)

    def preprocess(self, train, test) -> object:
        service = self.service
        this = self.dataset
        # 초기모델 생성, Hook 패턴 -> 순서 중요!
        this.train = service.new_model(train)
        this.test = service.new_model(test)
        this.id = this.test['PassengerId']
        # normianl, ordinal로 정형화
        this = service.embarked_nominal(this)
        this = service.title_norminal(this)
        this = service.gender_norminal(this)
        this = service.age_ordinal(this)
        this = service.fare_ordinal(this)
        # 불필요한 feature 제거
        this = service.drop_feature(this, 'Ticket', 'Cabin', 'Name', 'Sex', 'Age', 'Fare')
        self.print_this(this)
        # 위와같은 순서(프로세스)가 존재 -> 알고리즘
        return this

    @staticmethod
    def print_this(this):
        n = 10
        print('*'*30, 'Train 테스트', '*'*30)
        print(f'1. Train 의 Type 은 {type(this.train)}')
        print(f'2. Train 의 column 은 {this.train.columns}')
        print(f'3. Train 의 상위 {n}개 행은 \n{this.train.head(n)}')
        print(f'4. Train null 의 개수 \n{this.train.isnull().sum()}개')
        print('*'*30, 'Test 테스트', '*'*30)
        print(f'6. Test 의 Type 은 \n {type(this.test)}')
        print(f'7. Test 의 column 은 \n {this.test.columns}')
        print(f'8. Test 의 상위 {n}개 행은 \n{this.test.head(n)} ')
        print(f'9. Test null 의 개수 \n{this.test.isnull().sum()}개')
        print(f'10. Test null 의 개수 {this.test[this.test.isna().any(axis=1)]}')
        print('*'*100)

from titanic.models.dataset import Dataset
from titanic.models.service import Service


class Controller(object):

    dataset = Dataset()
    service = Service()

    def modeling(self, train, test) -> object:
        service = self.service
        this = self.preprocess(train, test)
        this.label = service.create_label(this)
        this.train = service.create_train(this)
        return this

    def preprocess(self, train, test) -> object:
        service = self.service
        this = self.dataset
        # 초기모델 생성
        this.train = service.new_model(train)
        this.test = service.new_model(test)
        # 불필요한 feature (Cabin, Ticket)제거
        this = service.drop_feature(this, 'Ticket')
        this = service.drop_feature(this, 'Cabin')
        # normianl, ordinal로 정형화
        this = service.embarked_nominal(this)
        this = service.title_norminal(this)
        # 불필요한 feature (Name)제거
        this = service.drop_feature(this, 'Name')
        this = service.gender_norminal(this)
        this = service.drop_feature(this, 'Sex')
        self.print_this(this)
        # 위와같은 순서(프로세스)가 존재 -> 알고리즘
        return this

    @staticmethod
    def print_this(this):
        print('*'*100)
        print(f'Train 의 Type 은 {type(this.train)} ')
        print(f'Train 의 column 은 {this.train.columns} ')
        print(f'Train 의 상위 5개 행은 \n{this.train.head()} ')
        print(f'Test 의 Type 은 {type(this.test)} ')
        print(f'Test 의 column 은 {this.test.columns} ')
        print(f'Test 의 상위 5개 행은 \n{this.test.head()} ')
        print('*'*100)

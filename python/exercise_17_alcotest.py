from dataclasses import dataclass

LEGAL_BAC_LIMIT = 0.08
ALCOHOL_DISTRIBUTION_RATIO_FEMALE = 0.66
ALCOHOL_DISTRIBUTION_RATIO_MALE = 0.73
ALCOHOL_CONSUMPTION_RATIO = 5.14
ALCOHOL_DECAY_RATE = 0.015  # per hour


@dataclass
class Person:
    alcohol_consumed: float = 0.0
    time_passed: float = 0.0
    body_weight: float = 1.0
    alcohol_distribution_ratio: float = 1.0

    @staticmethod
    def male(body_weight):
        return Person(body_weight=body_weight,
                      alcohol_distribution_ratio=ALCOHOL_DISTRIBUTION_RATIO_MALE)

    @staticmethod
    def female(body_weight):
        return Person(body_weight=body_weight,
                      alcohol_distribution_ratio=ALCOHOL_DISTRIBUTION_RATIO_FEMALE)

    def consume(self, alcohol_amount):
        return Person(self.alcohol_consumed + alcohol_amount,
                      self.time_passed,
                      self.body_weight,
                      self.alcohol_distribution_ratio)

    def pass_time(self, hours):
        return Person(self.alcohol_consumed,
                      self.time_passed + hours,
                      self.body_weight,
                      self.alcohol_distribution_ratio)

    def compute_bac(self):
        return self.alcohol_consumed * ALCOHOL_CONSUMPTION_RATIO / (
                    self.body_weight * self.alcohol_distribution_ratio) - ALCOHOL_DECAY_RATE * self.time_passed

    def legal_to_drive(self):
        return legal_to_drive(self.compute_bac())


def legal_to_drive(bac):
    return bac < LEGAL_BAC_LIMIT

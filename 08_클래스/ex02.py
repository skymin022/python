class Stuendt:
    def __init__ (self, no, name, major):
        self.no = no
        self.name = name
        self.major = major

    # 매직 메소드
    # : 특수한 이름의 메소드, __(이름)__ 형태의 메소드
    # * 미리 정의된 이름이며, 특수한 상황해서 호출되도록 정의되어있다.
    # __init__      : 생성자
    # __del__       : 소멸자
    # __str__       : 객체를 출력할 때 호출되는 메소드
    # __eq__        : 인스턴스가 같은지 비교하는 메소드
    # __ne__        : 인스턴스가 다르지 비교하는 메소드

    def __str__ (self):
        return '{} / {} / {}'.format(self.no, self.name, self.major)

    # A == B => __eq__ 호출
    # __eq__ 를 정의하지 않으면, A == B는 인스턴스를 비교
    def __eq__(self, obj):
        return self.no == obj.no

    # A != B => __ne__ 호출
    # __eq__ 를 정의하지 않으면, A != B는 인스턴스를 비교
    def __ne__(self, obj):
        return self.no != obj.no

# 객체 리스트
students = [
    Stuendt(101, '김조은', '컴퓨터공학과'),
    Stuendt(102, '이재명', '법학과'),
    Stuendt(103, '김문수', '정치학과'),
    Stuendt(104, '이준석', '컴퓨터과학')
]

for student in students:
    # str(객체) : 해당 객체의 __str__ 메소드를 호출하는 메소드
    print(str(student) )

# == 기호를 이용하여 두 객체를 비교하면,
# 해당 객체의 __eq__ 메소드가 호출됩니다.
print( students[0] == students[1])
print( students[0] == students[3])
print( students[0] == students[0])

# != 기호를 이용하여 두 객체를 비교하면,
# 해당 객체의 __ne__ 메소드가 호출됩니다.
print( students[0] != students[1])
print( students[0] != students[3])
print( students[0] != students[0])
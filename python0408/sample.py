class RangeException(Exception):
    def __init__(self, typeoferr, content):
        if typeoferr == 'menu':
            super().__init__(f'Out of Menu Range - {content}')
        elif typeoferr == 'score':
            super().__init__(f'Out of Score Range - kor: {content[0]}, eng: {content[1]}, math: {content[2]}')


def get_rank(avg):
    if avg >= 90:
        return '수'
    elif avg >= 80:
        return '우'
    elif avg >= 70:
        return '미'
    elif avg >= 60:
        return '양'
    else:
        return '가'


def get_scores():
    try:
        kor = int(input('국어 입력 => '))
        eng = int(input('영어 입력 => '))
        math = int(input('수학 입력 => '))

        if min(kor, eng, math) < 0 or max(kor, eng, math) > 100:
            err = RangeException('score', (kor, eng, math))
            print(type(err), err)
            return
    except Exception as e:
        print(type(e), e)
        return
    else:
        return kor, eng, math


def get_input():
    dict1 = {}

    hakbun = input('학번 입력 => ')
    if hakbun in total_dict:
        print('이미 존재하는 학번입니다. 입력을 종료합니다.')
        return
    erum = input('이름 입력 => ')

    scores = get_scores()
    if not scores: return
    kor, eng, math = scores

    tot = kor + eng + math
    avg = tot / 3
    rank = get_rank(avg)

    dict1['이름'] = erum
    dict1['국어'] = kor
    dict1['영어'] = eng
    dict1['수학'] = math
    dict1['총점'] = tot
    dict1['평균'] = avg
    dict1['등급'] = rank
    total_dict[hakbun] = dict1

    print('-' * 55)


def print_scores():
    if len(total_dict) > 0:
        total = 0
        print('\n\t\t\t *** 성적표 ***')
        print('=' * 55)
        print('학번     이름    국어   영어   수학   총점     평균     등급')
        print('=' * 55)
        for hakbun, dict1 in total_dict.items():
            print(hakbun, dict1['이름'], dict1['국어'], dict1['영어'],
                  dict1['수학'], dict1['총점'], round(dict1['평균'], 2), dict1['등급'], sep='    ')
            total += dict1['평균']
        print('=' * 55)
        print(f'학생 수: {len(total_dict)}, 전체 평균: {total/len(total_dict):.2f}')
    else:
        print('출력할 성적이 없습니다.')


def read_score():
    hakbun = input('조회할 학번 입력: ')
    if hakbun in total_dict:
        print('학번     이름    국어   영어   수학   총점     평균     등급')
        print(hakbun, total_dict[hakbun]['이름'], total_dict[hakbun]['국어'], total_dict[hakbun]['영어'],
              total_dict[hakbun]['수학'], total_dict[hakbun]['총점'], round(total_dict[hakbun]['평균'], 2),
              total_dict[hakbun]['등급'], sep='    ')
    else:
        print('존재하지 않는 학번입니다.')


def update_score():
    hakbun = input('수정할 학번 입력: ')
    if hakbun in total_dict:
        scores = get_scores()
        if not scores: return
        kor, eng, math = scores

        total_dict[hakbun]['국어'] = kor
        total_dict[hakbun]['영어'] = eng
        total_dict[hakbun]['수학'] = math
        total_dict[hakbun]['총점'] = total_dict[hakbun]['국어'] + total_dict[hakbun]['영어'] + total_dict[hakbun]['수학']
        total_dict[hakbun]['평균'] = total_dict[hakbun]['총점'] / 3
        total_dict[hakbun]['등급'] = get_rank(total_dict[hakbun]['평균'])
        print('수정 완료')
    else:
        print('존재하지 않는 학번입니다.')


def del_score():
    hakbun = input('삭제할 학번 입력: ')
    if hakbun in total_dict:
        del (total_dict[hakbun])
        print('삭제 완료')
    else:
        print('존재하지 않는 학번입니다.')


if __name__ == '__main__':
    total_dict = {}  # 전역변수

    while True:
        print('메뉴: 1. 성적 입력 / 2. 성적 출력 / 3. 성적 조회 / 4. 성적 수정 / 5. 성적 삭제 / 6. 프로그램 종료')
        menu = input('메뉴 선택 (숫자 입력): ')

        try:
            menu = int(menu)
        except ValueError as e:
            print(type(e), e)
        except Exception as e:
            print(type(e), e)
        else:
            if menu == 1:
                get_input()
            elif menu == 2:
                print_scores()
            elif menu == 3:
                read_score()
            elif menu == 4:
                update_score()
            elif menu == 5:
                del_score()
            elif menu == 6:
                print('프로그램을 종료합니다.')
                break
            else:
                err = RangeException('menu', menu)
                print(type(err), err)
        finally:
            print()
import random
from collections import defaultdict
from itertools import combinations
from statistics import mean

# 설정
NUM_PEOPLE = 31
NUM_ROUNDS = 8
GROUPS_OF_4 = 7
GROUPS_OF_3 = 1
ATTEMPTS_PER_ROUND = 10_000_000_000  # 💥 회차당 1천만번 시도

people = list(range(1, NUM_PEOPLE + 1))
pair_history = defaultdict(int)

def score_group(group):
    return sum(pair_history[tuple(sorted(pair))] for pair in combinations(group, 2))

def update_pair_history(group):
    for pair in combinations(group, 2):
        pair_history[tuple(sorted(pair))] += 1

def generate_best_groups():
    best_config = None
    lowest_score = float('inf')

    for _ in range(ATTEMPTS_PER_ROUND):
        random.shuffle(people)
        groups = []
        idx = 0
        for _ in range(GROUPS_OF_4):
            groups.append(people[idx:idx+4])
            idx += 4
        groups.append(people[idx:idx+3])  # 마지막 3명 조

        score = sum(score_group(group) for group in groups)
        if score < lowest_score:
            best_config = groups
            lowest_score = score
            if lowest_score == 0:  # 💡 완벽한 조합이 나오면 조기 종료 가능
                break

    return best_config

# 전체 회차 실행
all_rounds = []

for round_num in range(1, NUM_ROUNDS + 1):
    print(f"🚀 Generating round {round_num}... (this may take a while)")
    best_groups = generate_best_groups()
    all_rounds.append(best_groups)
    for group in best_groups:
        update_pair_history(group)

# 결과 출력
print("\n📋 조 편성 결과 (총 8회차)")
for i, round_groups in enumerate(all_rounds, 1):
    print(f"\n🔁 Round {i}")
    for j, group in enumerate(round_groups, 1):
        print(f"  Group {j}: {group}")

# 통계 출력
all_pair_counts = list(pair_history.values())
max_overlap = max(all_pair_counts)
avg_overlap = mean(all_pair_counts)
num_pairs = len(all_pair_counts)
zero_overlap = sum(1 for count in all_pair_counts if count == 0)

print("\n📊 중복 통계 분석")
print(f"👥 총 인원 쌍 수: {num_pairs}")
print(f"🔁 최대 겹침 횟수 (최악의 경우): {max_overlap}번")
print(f"📉 평균 겹침 횟수: {avg_overlap:.2f}번")
print(f"❌ 한 번도 안겹친 쌍 수: {zero_overlap}쌍")

print("\n⚠️ 2번 이상 겹친 쌍:")
for (a, b), count in pair_history.items():
    if count >= 2:
        print(f"  - ({a}, {b}): {count}번")
